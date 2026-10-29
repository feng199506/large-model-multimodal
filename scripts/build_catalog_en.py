#!/usr/bin/env python3
"""Build catalog_cn.csv, download_failures_cn.csv, checksums_en.sha256, domains/*/index_cn.md and
scripts/state/stats_en.json from seeds + results + annotations + venue checks.

  python3 -I scripts/build_catalog_en.py
Only VERIFIED items enter the catalog; failed / pending / unresolved items go to download_failures_cn.csv.
"""
import csv
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lmm_common_en as C  # noqa: E402

OTHER_LIBS = {"machine_learning_deep_learning_literature": Path("/root/machine_learning_deep_learning_literature"),
              "time_series_literature": Path("/root/time_series_literature")}
CATNAME = {c: n for c, _, n in C.CATEGORIES}

COLS = ["文献编号", "主分类", "交叉分类", "交叉分类依据", "资料类型", "子方向", "标题", "作者或教师", "学校或机构",
        "渠道或出版社", "发表状态", "发表状态依据", "首次公开日期", "日期精度", "首次公开依据", "下载版本", "版本日期",
        "正式发表年份", "时间窗口", "较早资料保留理由", "DOI", "arXiv ID", "ISBN", "原始来源", "下载链接", "语言", "格式",
        "本地路径", "完整性", "核验状态", "核验详情", "SHA256", "获取方式", "跨库关系", "选入理由", "阅读优先级",
        "研究问题", "方法类别", "输入模态", "输出模态", "模型规模", "数据可用性", "代码可用性", "主要评测任务", "简介",
        "字段依据", "优先阅读排名", "优先阅读理由",
        "课程代码", "学期或书籍版本", "原著年份", "版本或学期年份", "先修要求", "章节覆盖", "内容完整性说明", "阅读阶段",
        "一般基础材料理由"]


def load_seeds_all(code):
    out = []
    for p in sorted(C.SEEDS.glob(f"{C.cat_key(code)}_seed*_cn.json")):
        out += C.load_json(p, [])
    return out


def other_lib_files():
    """sha256 -> (lib, relpath) and arXiv id -> (lib, relpath) for the earlier libraries."""
    by_sha, by_arxiv = {}, {}
    for lib, root in OTHER_LIBS.items():
        if not root.exists():
            continue
        cks = root / "checksums_en.sha256"
        if not cks.exists():
            # no checksum list yet (library still being built): hash its PDFs directly (read-only)
            cache = C.load_json(C.STATE / "other_lib_hash_cache_en.json", {})
            for pdf in sorted(root.rglob("*.pdf")):
                if "/.git/" in str(pdf):
                    continue
                st = pdf.stat()
                ck = f"{pdf}|{st.st_size}|{int(st.st_mtime)}"
                if ck not in cache:
                    cache[ck] = C.sha256_file(pdf)
                by_sha.setdefault(cache[ck], (lib, str(pdf.relative_to(root))))
            C.save_json(C.STATE / "other_lib_hash_cache_en.json", cache)
        if cks.exists():
            for line in cks.read_text("utf-8", "replace").splitlines():
                m = re.match(r"([0-9a-f]{64})\s+\*?(.+)", line.strip())
                if m:
                    by_sha.setdefault(m.group(1), (lib, m.group(2)))
        cat = root / "catalog_cn.csv"
        if cat.exists():
            with open(cat, encoding="utf-8-sig") as f:
                for row in csv.DictReader(f):
                    a = (row.get("arXiv ID") or "").strip()
                    a = re.sub(r"v\d+$", "", a)
                    rel = row.get("本地相对路径") or row.get("本地路径") or ""
                    if a:
                        by_arxiv.setdefault(a, (lib, rel))
                    sha = (row.get("SHA256") or "").strip()
                    if re.fullmatch(r"[0-9a-f]{64}", sha):
                        by_sha.setdefault(sha, (lib, rel))
    return by_sha, by_arxiv


def pub_status(seed, rec, meta, venue):
    """(status, basis, year)."""
    v = venue or {}
    hits = v.get("official_index") or []
    if hits:
        h = hits[0]
        det = f"（{h['detail']}）" if h.get("detail") else ""
        return (f"正式发表：{h['venue']} {h['year'] or ''}{det}".strip(), f"官方论文集索引标题完全匹配：{h['url']}", h.get("year") or "")
    cr = v.get("crossref") or []
    if cr:
        h = cr[0]
        kind = {"journal-article": "期刊", "proceedings-article": "会议论文集", "book-chapter": "图书章节"}.get(h.get("type"), h.get("type"))
        return (f"正式发表（{kind}）：{h['venue']}", f"Crossref 记录标题匹配：https://doi.org/{h['doi']}", h.get("year") or "")
    jr = (meta or {}).get("journal_ref", "")
    if jr:
        return ("作者声明已发表（未独立核实）", f"arXiv journal_ref：{jr}", "")
    com = (meta or {}).get("comment", "")
    m = re.search(r"(accepted|to appear|published|camera[- ]ready|oral|spotlight)[^.;]{0,80}", com, re.I)
    if m:
        return ("作者声明已接收（未独立核实）", f"arXiv 注释：{m.group(0).strip()}", "")
    if seed.get("type") == "技术报告":
        return ("技术报告（以预印本形式公开）", "资料类型为机构技术报告；未在所查官方论文集索引与 Crossref 中发现正式发表记录", "")
    if seed.get("pdf_url") and seed.get("venue"):
        return (f"种子记录渠道：{seed['venue']}", "种子人工记录（来源页面）", "")
    return ("预印本（未发现正式发表信息）", "所查官方论文集索引（NeurIPS 2023–2025、ICLR 2024–2026、ICML 2023–2026、CVPR/ICCV/ECCV、ACL 系列、Interspeech、CoRL、TMLR）与 Crossref 均无匹配；不代表未发表", "")


def window_label(date):
    if not date:
        return "日期待核实"
    return "近三年" if date >= C.WINDOW_START else "三年前补充"


def main():
    meta = C.load_json(C.STATE / "arxiv_meta_en.json", {})
    venues = C.load_json(C.STATE / "venue_check_en.json", {})
    by_sha, by_arxiv = other_lib_files()
    rows, fails, sums, stats = [], [], [], {}
    cross_tags = {}  # key -> list of (code, reason)
    for code, slug, name in C.CATEGORIES[:12]:
        for s in load_seeds_all(code):
            if s.get("cross_only") and s.get("arxiv"):
                cross_tags.setdefault("arxiv:" + re.sub(r"v\d+$", "", s["arxiv"]), []).append((code, s.get("cross_reason", "")))
    seen_keys = {}
    for code, slug, name in C.CATEGORIES:
        seeds = load_seeds_all(code)
        res = C.load_json(C.RESULTS / f"{code}_{slug}_en.json", {})
        ann = C.load_json(C.ANNOT / f"{code}_{slug}_annot_cn.json", {})
        st = {"verified": 0, "pending": 0, "failed": 0, "recent": 0, "old": 0, "undated": 0, "new_download": 0,
              "reused": 0, "cross_library_dup": 0, "dup_elsewhere": 0, "cross_only": 0}
        for s in seeds:
            sid = s["sid"]
            r = res.get(sid, {})
            status = r.get("status")
            if s.get("cross_only"):
                st["cross_only"] += 1
                continue
            if s.get("exclude"):
                continue
            if status == "duplicate_elsewhere":
                st["dup_elsewhere"] += 1
                continue
            if status != "verified":
                if status in ("failed", "pending") or (status is None and not s.get("reserve")):
                    st["pending" if status == "pending" else "failed" if status == "failed" else "pending"] += 1 if status else 0
                    if status:
                        fails.append({"编号": f"LMM-{sid}", "类别": f"{code} {name}", "标题": r.get("title") or s.get("title") or s.get("course_title", ""),
                                      "来源": r.get("source_url") or (s.get("files") or [{}])[0].get("url", "") or s.get("pdf_url", ""),
                                      "状态": {"failed": "下载失败或核验未通过", "pending": "待核验（未计数）"}[status],
                                      "原因": "; ".join(r.get("notes", []))[:400],
                                      "处理": ("未找到可替代的合规完整来源，计为缺口" if code in ("13", "14") else "已由备选/新候选替换") if status == "failed" else "保留待人工核验，不计数",
                                      "时间": r.get("time", "")})
                continue
            st["verified"] += 1
            a = re.sub(r"v\d+$", "", s.get("arxiv", "") or "")
            m = meta.get(a, {}) if a else {}
            key = r.get("key") or (f"arxiv:{a}" if a else f"{code}:{sid}")
            seen_keys.setdefault(key, []).append(f"LMM-{sid}")
            an = ann.get(sid, {})
            row = {c: "" for c in COLS}
            row["文献编号"] = f"LMM-{sid}"
            row["主分类"] = f"{code} {name}"
            xs = list(dict.fromkeys([x for x in s.get("cross", []) if x != code] + [c for c, _ in cross_tags.get(key, [])]))
            row["交叉分类"] = "；".join(f"{x} {CATNAME.get(x, '')}" for x in xs)
            reasons = [s.get("cross_reason", "")] + [f"{c}：{rr}" for c, rr in cross_tags.get(key, []) if rr]
            row["交叉分类依据"] = "；".join(x for x in reasons if x)
            row["子方向"] = s.get("subtopic", "")
            row["选入理由"] = s.get("reason", "")
            row["阅读优先级"] = s.get("priority", "")
            row["语言"] = {"zh": "中文", "en": "英文"}.get(s.get("language", "en"), s.get("language", ""))
            if code in ("13", "14"):
                files = r.get("files", [])
                row["SHA256"] = r.get("pack_sha256", "")
                row["本地路径"] = r.get("local_path", "")
                row["核验状态"] = "已核验全文" if code == "14" else "已核验完整讲义包"
                if code == "14":
                    bc = r.get("book_check", {})
                    mir = r.get("mirror", {})
                    det = []
                    if bc:
                        det.append(f"主 PDF {bc.get('pages')} 页；标题匹配 {bc.get('title_match')}；目录{'已见' if bc.get('toc_found') else '人工核对'}；作者{'已见' if bc.get('author_found') else '人工核对'}")
                    if mir:
                        det.append(f"HTML 离线镜像 {mir.get('html_pages')} 页，关键章节内容检查通过")
                    if s.get("manual_check_note"):
                        det.append(s["manual_check_note"])
                    det.append(f"{len(files)} 个文件均 HTTP 200 且类型检查通过；SHA256 为{'单文件哈希' if len(files) == 1 else '资料包哈希（各文件哈希排序后再哈希）'}")
                    row["核验详情"] = "；".join(det)
                    row["资料类型"] = "教科书/专著/参考书"
                    row["标题"] = s["title"]
                    row["作者或教师"] = "; ".join(s.get("authors", []))
                    row["渠道或出版社"] = s.get("publisher", "")
                    row["学校或机构"] = s.get("institution", "")
                    row["DOI"] = s.get("doi", "")
                    row["arXiv ID"] = s.get("arxiv", "")
                    row["ISBN"] = s.get("isbn", "")
                    row["原始来源"] = s.get("landing_url", "")
                    row["下载链接"] = " | ".join(f.get("url", "") for f in files if not f.get("mirror")) or (s.get("mirror", {}).get("start", [""])[0])
                    row["格式"] = s.get("format", "PDF")
                    row["学期或书籍版本"] = s.get("edition", "")
                    row["原著年份"] = s.get("orig_year") or ""
                    row["版本或学期年份"] = s.get("edition_year") or ""
                    row["首次公开日期"] = str(s.get("orig_year") or "")
                    row["日期精度"] = "年"
                    row["首次公开依据"] = "原著首版年份（出版社/作者页）"
                    row["下载版本"] = s.get("edition", "")
                    row["版本日期"] = str(s.get("edition_year") or "")
                    ey = s.get("edition_year") or 0
                    row["时间窗口"] = "近三年版本" if ey and ey >= 2023 else ("版本年份待核实" if not ey else "较早版本（年份例外）")
                    row["较早资料保留理由"] = s.get("year_exception_reason", "")
                    row["发表状态"] = "已出版图书" if re.search(r"Press|Springer|Cambridge|Taylor|出版社|Foundations and Trends|Morgan", s.get("publisher", "")) else "作者/机构公开书稿"
                    row["发表状态依据"] = s.get("publisher", "")
                else:
                    aux_names = {f["name"] for f in s.get("files", []) if f.get("aux")}
                    n_ok = sum(1 for f in files if f.get("ok") and not f.get("mirror") and Path(f.get("path", "")).name not in aux_names)
                    row["核验详情"] = f"{len(files)} 个文件均 HTTP 200 且类型检查通过；讲义文件 {n_ok} / 官方讲次 {s.get('expected_items')}；{s.get('verification_basis', '')}"
                    row["资料类型"] = "大学课程讲义包"
                    row["标题"] = f"{s.get('course_code', '')} {s.get('course_title', '')}".strip()
                    row["作者或教师"] = "; ".join(s.get("instructors", []))
                    row["学校或机构"] = s.get("university", "")
                    row["渠道或出版社"] = "课程官方页面/官方仓库"
                    row["原始来源"] = s.get("official_url", "")
                    row["下载链接"] = s.get("schedule_url", "")
                    row["格式"] = "、".join(sorted({(f.get('path', '').rsplit('.', 1)[-1]).upper() for f in files if f.get('path')}))
                    row["课程代码"] = s.get("course_code", "")
                    row["学期或书籍版本"] = s.get("term", "")
                    row["版本或学期年份"] = s.get("term_year") or ""
                    row["首次公开日期"] = str(s.get("term_year") or "")
                    row["日期精度"] = "学期"
                    row["首次公开依据"] = "课程学期（官方页面）"
                    ty = s.get("term_year") or 0
                    row["时间窗口"] = "近三年学期" if ty and ty >= 2023 else "较早学期（经典课程例外）"
                    row["较早资料保留理由"] = s.get("old_reason", "")
                    row["发表状态"] = "官方课程材料"
                    row["发表状态依据"] = s.get("verification_basis", "")
                row["完整性"] = s.get("completeness_note", "") or ("完整书籍" if code == "14" else "")
                row["内容完整性说明"] = s.get("completeness_note", "") or ("完整正文（含目录）" if code == "14" else "")
                row["先修要求"] = s.get("prereq", "")
                row["章节覆盖"] = s.get("coverage", "")
                row["阅读阶段"] = s.get("stage", "")
                row["一般基础材料理由"] = s.get("general_ml_reason", "")
                row["优先阅读排名"] = s.get("top10_rank", "")
                row["优先阅读理由"] = s.get("top10_reason", "")
                for f in files:
                    if f.get("sha256") and f.get("path"):
                        sums.append((f["sha256"], f["path"]))
                st["recent"] += 1 if row["时间窗口"].startswith("近三年") else 0
                st["old"] += 0 if row["时间窗口"].startswith("近三年") else 1
                rel_hits = [by_sha.get(f.get("sha256")) for f in files if by_sha.get(f.get("sha256"))]
            else:
                v = r.get("verification", {})
                row["资料类型"] = s.get("type", "原始研究")
                row["标题"] = r.get("title") or s.get("title", "")
                au = m.get("authors") or s.get("authors", [])
                row["作者或教师"] = "; ".join(au[:12]) + (f"; 等（共 {len(au)} 位）" if len(au) > 12 else "")
                row["DOI"] = s.get("doi") or m.get("doi", "")
                row["arXiv ID"] = a
                row["原始来源"] = r.get("landing", "")
                row["下载链接"] = r.get("source_url", "")
                row["格式"] = "PDF"
                row["本地路径"] = r.get("local_path", "")
                row["SHA256"] = r.get("sha256", "")
                fp = m.get("published") or s.get("first_public_date", "")
                row["首次公开日期"] = fp
                row["日期精度"] = "日" if m else s.get("date_precision", "")
                row["首次公开依据"] = "arXiv v1 提交日" if m else s.get("first_public_basis", "")
                row["下载版本"] = r.get("version", "")
                row["版本日期"] = r.get("version_date", "")
                row["时间窗口"] = window_label(fp)
                row["较早资料保留理由"] = s.get("old_reason", "") if fp and fp < C.WINDOW_START else ""
                ps, basis, yr = pub_status(s, r, m, venues.get(key))
                row["发表状态"] = ps
                row["发表状态依据"] = basis
                row["正式发表年份"] = yr
                det = (f"HTTP {r.get('http_status', '200')}；%PDF 头；pypdf 可解析 {v.get('pages')} 页（抽取 {v.get('pages_extracted')} 页、"
                       f"{v.get('chars_extracted')} 字符）；首页标题匹配 {v.get('title_match')}；首作者{ {'first_pages': '见于首页', 'later_pages': '见于正文后部（作者名单）', 'team_name': '团队署名已见', 'not_found': '未自动找到'}.get(v.get('author_check'), '') }；"
                       f"参考文献标题{'已见' if v.get('references_heading') else '未见'}")
                if r.get("manual_verification"):
                    det += f"；人工核对：{r['manual_verification']['note']}"
                row["核验详情"] = det
                row["核验状态"] = "已核验全文" + ("（含人工核对）" if r.get("manual_verification") else "")
                row["完整性"] = "完整论文全文（非摘要页/补充材料）"
                for k_cn, k in (("研究问题", "research_question"), ("方法类别", "method_category"), ("输入模态", "input_modalities"),
                                ("输出模态", "output_modalities"), ("模型规模", "model_scale"), ("数据可用性", "data_availability"),
                                ("代码可用性", "code_availability"), ("主要评测任务", "eval_tasks"), ("简介", "summary"),
                                ("字段依据", "field_basis"), ("优先阅读排名", "top10_rank"), ("优先阅读理由", "top10_reason")):
                    row[k_cn] = an.get(k, "") if an else ""
                if not an:
                    row["字段依据"] = "待补注释"
                sums.append((r.get("sha256", ""), r.get("local_path", "")))
                if fp and fp >= C.WINDOW_START:
                    st["recent"] += 1
                elif fp:
                    st["old"] += 1
                else:
                    st["undated"] += 1
                rel_hits = []
                if by_sha.get(r.get("sha256")):
                    rel_hits.append(by_sha[r["sha256"]])
                if a in by_arxiv:
                    rel_hits.append(by_arxiv[a])
            # acquisition / cross-library
            if r.get("origin") == "reused_other_library":
                row["获取方式"] = "本地已有且复用"
                row["跨库关系"] = f"复制自 {r.get('origin_path')}（重新核验通过）"
                st["reused"] += 1
            else:
                row["获取方式"] = "本轮新下载"
                st["new_download"] += 1
                if rel_hits:
                    lib, rel = rel_hits[0]
                    row["跨库关系"] = f"跨库重复：{lib} 中也有同一资料（{rel}）；本库文件为本轮独立下载"
                    st["cross_library_dup"] += 1
            rows.append(row)
        stats[code] = st
    # write catalog
    with open(C.ROOT / "catalog_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    fcols = ["编号", "类别", "标题", "来源", "状态", "原因", "处理", "时间"]
    with open(C.ROOT / "download_failures_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fcols)
        w.writeheader()
        for row in fails:
            w.writerow(row)
    uniq = {}
    for sha, path in sums:
        if path:
            uniq[path] = sha
    with open(C.ROOT / "checksums_en.sha256", "w") as f:
        for path in sorted(uniq):
            f.write(f"{uniq[path]}  {path}\n")
    # domains
    for code, slug, name in C.CATEGORIES:
        d = C.ROOT / "domains" / f"{code}_{slug}"
        d.mkdir(parents=True, exist_ok=True)
        prim = [r for r in rows if r["主分类"].startswith(code + " ")]
        cross = [r for r in rows if not r["主分类"].startswith(code + " ") and re.search(rf"(^|；){code} ", r["交叉分类"])]
        lines = [f"# {code} {name}\n", f"主分类资料 {len(prim)} 份；交叉标签资料 {len(cross)} 份。实体文件只保存一份，下列链接指向库内唯一副本。\n",
                 "## 主分类\n", "| 编号 | 标题 | 首次公开/版本 | 类型 | 子方向 | 优先级 | 本地文件 |", "|---|---|---|---|---|---|---|"]
        for r in sorted(prim, key=lambda x: (str(x["优先阅读排名"] or 99).zfill(3), x["文献编号"])):
            link = f"[打开](../../{r['本地路径']})" if r["本地路径"] else ""
            lines.append(f"| {r['文献编号']} | {r['标题'].replace('|', '/')} | {r['首次公开日期']} | {r['资料类型']} | {r['子方向']} | {r['阅读优先级']} | {link} |")
        if cross:
            lines += ["\n## 交叉标签（主分类在别处）\n", "| 编号 | 标题 | 主分类 | 本地文件 |", "|---|---|---|---|"]
            for r in cross:
                lines.append(f"| {r['文献编号']} | {r['标题'].replace('|', '/')} | {r['主分类']} | [打开](../../{r['本地路径']}) |")
        (d / "index_cn.md").write_text("\n".join(lines) + "\n", "utf-8")
    dup_keys = {k: v for k, v in seen_keys.items() if len(v) > 1}
    papers = sum(1 for r in rows if r["文献编号"][4:6] not in ("13", "14"))
    out = {"per_category": stats, "rows": len(rows), "papers": papers,
           "course_packs": sum(1 for r in rows if r["文献编号"].startswith("LMM-13")),
           "books": sum(1 for r in rows if r["文献编号"].startswith("LMM-14")),
           "duplicate_keys_across_categories": dup_keys, "failures": len(fails), "checksum_lines": len(uniq)}
    C.save_json(C.STATE / "stats_en.json", out)
    print(json.dumps({k: v for k, v in out.items() if k != "per_category"}, ensure_ascii=False))
    for code, st in stats.items():
        print(code, st)


if __name__ == "__main__":
    main()
