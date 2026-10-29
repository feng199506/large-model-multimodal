# 下载与解压恢复说明（large_model_multimodal 文献全文，2026-10-29）

本资料库按“轻量 Git 仓库 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含脚本、文献目录（`catalog_cn.csv`、`domains/*/index_cn.md` 等）、报告、分包索引和本说明，不含 PDF 全文。
- **Release `lmml-full-20261029`**：8 个独立的不压缩 `.tar` 包，合起来就是完整的资料库，包括全部文献、教材、讲义、目录、报告和脚本。

Release 页面：https://github.com/feng199506/large-model-multimodal/releases/tag/lmml-full-20261029

## 1. 包列表

| 包文件名 | 内容范围（按路径顺序） |
|---|---|
| `large_model_multimodal_20261029_batch001_cn_en.tar` | 顶层目录与报告、`domains/`、`scripts/`、`books/` 前半 |
| `large_model_multimodal_20261029_batch002_cn_en.tar` | `books/` 后半、`papers/`（至 2024_Hayou） |
| `large_model_multimodal_20261029_batch003_cn_en.tar` | `papers/`（2024_He … 2025_Alrashed） |
| `large_model_multimodal_20261029_batch004_cn_en.tar` | `papers/` 剩余部分、`university_materials/`（至 Berkeley_CS285 lec13） |
| `large_model_multimodal_20261029_batch005_cn_en.tar` | `university_materials/`（Berkeley_CS285 lec14 … CMU_11-766 第 24 讲） |
| `large_model_multimodal_20261029_batch006_cn_en.tar` | `university_materials/`（CMU_11-766 第 25 讲 … Cornell_CS5788 lec23） |
| `large_model_multimodal_20261029_batch007_cn_en.tar` | `university_materials/`（Cornell_CS5788 lec24 … Stanford_CS224S lecture10） |
| `large_model_multimodal_20261029_batch008_cn_en.tar` | `university_materials/` 剩余部分 |

每个文件属于哪个包，见 `archive_index_cn.csv`（UTF-8 带 BOM，可直接用 Excel 打开）。表中列出包文件名、批次、相对路径、类型和字节数。

- 每个包都可以**单独解压**，不需要拼接。只要某几类资料时，可以只下载对应的包。
- 各包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包未压缩（PDF 本身已经是压缩格式），因此解压很快，所需磁盘空间约等于包的大小。全部解压约需 **11.1 GiB**，建议预留 15 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 8 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\lmml\`。
3. 单个包约 1.1–1.5 GB。浏览器提示“是否保留”时选择保留。下载中断可在浏览器下载列表里点“恢复”或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，在文件属性里核对每个包的大小（属性窗口里看“大小”的字节数，不要看“占用空间”）。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

建议目标目录用**短路径**，例如 `D:\lmml\`。包内最长相对路径为 168 个字符，目标目录过深可能超过 Windows 260 字符的路径上限。

**方法 A：一次批量解压（推荐）**

1. 在下载文件夹中，按住 Ctrl 选中全部 8 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\lmml\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 确定。所有包会解压到同一个 `D:\lmml\` 下，恢复出完整的目录结构：

```
D:\lmml\
├─ README_cn.md、catalog_cn.csv、reading_map_cn.md …
├─ books\
├─ domains\
├─ papers\
├─ scripts\
└─ university_materials\
```

**方法 B：逐个解压**

对每个 `.tar` 文件：右键 → WinRAR → **解压文件…** → 目标路径都填同一个 `D:\lmml\` → 确定。

注意：不要用“解压到 large_model_multimodal_..._batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

**Windows 文件名兼容处理（已在发布包中完成，解压时不应再出现文件名报错）：**
原资料中，离线网页版书 `books/Austin_HowToScaleYourModel_2025_html_en/scaling-book_site/scaling-book/assets/` 下有 28 个网页资源文件（css/js/字体/图标）的文件名含 `?`，例如 `main.css?d41d8cd98f00b204e9800998ecf8427e.css`。Windows 不允许文件名中出现 `?`。发布包中已做如下处理：

- 这 28 个文件名中的 `?` 改为 `_`，例如 `main.css_d41d8cd98f00b204e9800998ecf8427e.css`。文件内容不变。
- 该书 13 个 HTML 页面和 `main.css` 中指向这些文件的引用同步改成新文件名，在 Windows 上离线打开时样式、脚本和图标字体都能正常加载。
- 该书的 `manifest_en.json`、`scripts/state/results/14_books_en.json` 中的路径同步更新。
- 根目录 `checksums_en.sha256` 中对应的 41 行已更新为新路径，改过内容的文件使用新的 SHA-256。
- 全部 44 项改动列在 `windows_rename_map_cn.csv` 中（原路径 → 发布包内路径），`archive_index_cn.csv` 的“备注”列也有标注。

其余 3,009 个文件（包括全部 PDF 文献）与原件逐字节相同，未做任何改动。

包内另有 24 个中文文件名（RUC 课程讲义），按 tar 标准以 UTF-8 记录。WinRAR 5 及以上版本能正确显示，建议使用最新版 WinRAR。

## 4. Linux / macOS

```bash
mkdir -p ~/lmml
for f in large_model_multimodal_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/lmml || echo "FAILED: $f"; done
```

（macOS 自带 bsdtar，同样支持此格式。）

## 5. 完整性说明

- 本次发布只登记了上传状态（以 GitHub API 显示附件为 `uploaded`、远端大小等于本地大小为准），**没有**做下载回验和哈希校验。
- 解压后的根目录有 `checksums_en.sha256`，这是下载流程生成的文献 SHA-256 清单，需要时可以自行核对，例如在 Linux 上运行 `sha256sum -c checksums_en.sha256`。
- 打包时排除了：`.git/`、`scripts/__pycache__/`、`scripts/state/` 下 16 个空的 `.*.lock` 运行锁文件。除此之外，资料库中的全部文件都已打包。
