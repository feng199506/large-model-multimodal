#!/usr/bin/env python3
"""Publication-venue check by exact title match against official proceedings indexes,
then Crossref (journals / IEEE / ACM / Springer) for the rest.

  python3 -I scripts/venues_en.py build     # download official index pages -> scripts/state/venue_index_en.json
  python3 -I scripts/venues_en.py match     # match all verified papers -> scripts/state/venue_check_en.json

Index sources (public, no login): NeurIPS proceedings (papers.nips.cc), ICLR proceedings
(proceedings.iclr.cc), PMLR (ICML, CoRL), CVF open access (CVPR, ICCV), ECVA (ECCV),
ACL Anthology event pages, ISCA archive (Interspeech), TMLR paper list (jmlr.org/tmlr).
OpenReview API (403), DBLP (bot challenge), Semantic Scholar (429) and OpenAlex (daily budget
exhausted) were not usable on 2026-10-29. A Crossref hit is accepted only for a non-preprint
record whose title matches (similarity >= 0.95).
"""
import html
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lmm_common_en as C  # noqa: E402

RAW = Path("/root/.cache/lmm_lit/venue_raw")
INDEX = C.STATE / "venue_index_en.json"
CHECK = C.STATE / "venue_check_en.json"


def norm(t):
    return " ".join(C.tokens(html.unescape(t or "")))


def get(url):
    RAW.mkdir(parents=True, exist_ok=True)
    f = RAW / re.sub(r"[^A-Za-z0-9._-]+", "_", url)
    if f.exists() and f.stat().st_size > 1000:
        return f.read_text("utf-8", "replace")
    try:
        data = C.http_get(url, timeout=300, max_bytes=80 * 1024 * 1024).decode("utf-8", "replace")
    except C.HttpError as e:
        print(f"  skip {url}: {e}")
        return ""
    f.write_text(data, "utf-8")
    return data


def sources():
    s = []
    for y in (2023, 2024, 2025):
        s.append(("NeurIPS", y, f"https://papers.nips.cc/paper_files/paper/{y}", "nips"))
    for y in (2023, 2024, 2025, 2026):
        s.append(("ICLR", y, f"https://proceedings.iclr.cc/paper_files/paper/{y}", "nips"))
    for v, name, y in (("v202", "ICML", 2023), ("v235", "ICML", 2024), ("v267", "ICML", 2025), ("v306", "ICML", 2026),
                       ("v229", "CoRL", 2023), ("v270", "CoRL", 2024), ("v305", "CoRL", 2025)):
        s.append((name, y, f"https://proceedings.mlr.press/{v}/", "pmlr"))
    for conf, y in (("CVPR", 2023), ("CVPR", 2024), ("CVPR", 2025), ("CVPR", 2026), ("ICCV", 2023), ("ICCV", 2025)):
        s.append((conf, y, f"https://openaccess.thecvf.com/{conf}{y}?day=all", "cvf"))
    s.append(("ECCV", 0, "https://www.ecva.net/papers.php", "ecva"))
    for ev in ("acl-2023", "acl-2024", "acl-2025", "acl-2026", "emnlp-2023", "emnlp-2024", "emnlp-2025",
               "naacl-2024", "naacl-2025", "eacl-2024", "eacl-2026", "coling-2025"):
        s.append((ev.split("-")[0].upper(), int(ev.split("-")[1]), f"https://aclanthology.org/events/{ev}/", "acl"))
    for y in (2023, 2024, 2025):
        s.append(("Interspeech", y, f"https://www.isca-archive.org/interspeech_{y}/index.html", "isca"))
    s.append(("TMLR", 0, "https://jmlr.org/tmlr/papers/", "tmlr"))
    return s


def parse(kind, page, base):
    out = []
    if kind == "nips":
        for href, t in re.findall(r'<a[^>]*href="(/paper_files/paper/\d+/hash/[^"]+)"[^>]*>(.*?)</a>', page, re.S):
            track = "Datasets and Benchmarks Track" if "Datasets_and_Benchmarks" in href else "Main Conference"
            out.append((t, urllib.parse.urljoin(base, href), track))
    elif kind == "pmlr":
        for t, rest in re.findall(r'<p class="title">(.*?)</p>(.*?)</div>', page, re.S):
            m = re.search(r'href="([^"]+\.html)"', rest)
            out.append((t, urllib.parse.urljoin(base, m.group(1)) if m else base, ""))
    elif kind in ("cvf", "ecva"):
        for href, t in re.findall(r'<dt class="ptitle">\s*(?:<br>)?\s*<a href="?([^"> ]+)"?>(.*?)</a>', page, re.S):
            u = urllib.parse.urljoin(base, href)
            yr = re.search(r"eccv_(\d{4})", href)
            out.append((t, u, f"ECCV {yr.group(1)}" if yr else ""))
    elif kind == "acl":
        for href, t in re.findall(r'<strong><a class=align-middle href=(/[^ >]+)>(.*?)</a></strong>', page, re.S):
            vol = re.search(r"\d{4}\.([a-z]+)-([a-z]+)", href)
            out.append((re.sub(r"<[^>]+>", "", t), "https://aclanthology.org" + href,
                        f"{vol.group(1)}-{vol.group(2)}" if vol else ""))
    elif kind == "isca":
        for href, t in re.findall(r'<a[^>]+href="([^"]+\.html)"[^>]*>\s*<p[^>]*>(.*?)</p>', page, re.S):
            out.append((t, urllib.parse.urljoin(base, href), ""))
        if not out:
            for href, t in re.findall(r'<a class="w3-text" href="([^"]+)">\s*(.*?)\s*<br', page, re.S):
                out.append((t, urllib.parse.urljoin(base, href), ""))
    elif kind == "tmlr":
        for t, rest in re.findall(r"<b>(.*?)</b>(.{0,600})", page, re.S):
            m = re.search(r'href="(https://openreview\.net/forum\?id=[^"]+)"', rest)
            out.append((t, m.group(1) if m else base, ""))
    return out


def cmd_build():
    idx = {}
    for venue, year, url, kind in sources():
        page = get(url)
        items = parse(kind, page, url) if page else []
        for t, u, extra in items:
            n = norm(re.sub(r"<[^>]+>", "", t))
            if len(n) < 8:
                continue
            v = venue
            y = year
            if kind == "ecva":
                m = re.search(r"ECCV (\d{4})", extra)
                y = int(m.group(1)) if m else 0
                extra = ""
            idx.setdefault(n, []).append({"venue": v, "year": y, "url": u, "detail": extra, "source": url})
        print(f"{venue} {year}: {len(items)} titles")
    C.save_json(INDEX, idx)
    print(f"index: {len(idx)} titles")


def verified_papers():
    for code, slug, _ in C.CATEGORIES[:12]:
        res = C.load_json(C.RESULTS / f"{code}_{slug}_en.json", {})
        for sid, r in res.items():
            if r.get("status") == "verified":
                yield code, sid, r


def crossref(title):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query.bibliographic": title, "rows": 6, "select": "DOI,title,type,container-title,published,publisher"})
    data = json.loads(C.http_get(url, timeout=60))
    hits = []
    for it in data.get("message", {}).get("items", []):
        t = (it.get("title") or [""])[0]
        if it.get("type") in ("posted-content", "dataset", "component", "peer-review"):
            continue
        if C.title_similarity(title, t) < 0.95:
            continue
        ct = (it.get("container-title") or [""])[0]
        if re.search(r"arxiv|ssrn|research square|preprint", ct, re.I):
            continue
        dp = (it.get("published") or {}).get("date-parts", [[None]])[0]
        hits.append({"venue": ct or it.get("publisher", ""), "type": it.get("type"), "doi": it.get("DOI"),
                     "year": dp[0] if dp else None, "date_parts": dp, "url": f"https://doi.org/{it.get('DOI')}"})
    return hits


def cmd_match(refresh=False):
    idx = C.load_json(INDEX, {})
    check = C.load_json(CHECK, {})
    meta = C.load_json(C.STATE / "arxiv_meta_en.json", {})
    for code, sid, r in verified_papers():
        key = r["key"]
        if key in check and not refresh:
            continue
        title = r.get("title", "")
        n = norm(title)
        hits = idx.get(n, [])
        rec = {"title": title, "checked": time.strftime("%F"), "official_index": hits, "crossref": []}
        if not hits:
            try:
                rec["crossref"] = crossref(title)
            except Exception as e:
                rec["crossref_error"] = str(e)[:120]
        a = key.split(":", 1)[1] if key.startswith("arxiv:") else ""
        m = meta.get(a, {})
        rec["arxiv_journal_ref"] = m.get("journal_ref", "")
        rec["arxiv_doi"] = m.get("doi", "")
        rec["arxiv_comment"] = m.get("comment", "")
        check[key] = rec
        C.save_json(CHECK, check)
        v = hits[0]["venue"] + " " + str(hits[0]["year"]) if hits else (rec["crossref"][0]["venue"] if rec["crossref"] else "-")
        print(f"[{sid}] {v} | {title[:60]}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "build":
        cmd_build()
    elif cmd == "match":
        cmd_match("--refresh" in sys.argv)
