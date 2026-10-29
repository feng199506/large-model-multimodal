# 大模型与多模态模型文献库

本库收集大语言模型与多模态模型的论文、大学课程讲义包和教科书/专著。只做收集、核验与编目，没有下载模型权重或数据集，也没有训练、部署或复现实验。与本机此前的“机器学习与深度学习”“时间序列”文献库分开管理，没有修改它们的文件。

- 检索与下载日期：2026-10-29（UTC）。
- 论文近三年窗口：首次公开日期（arXiv v1 提交日）≥ 2023-10-29。
- 只有完整原文已保存在本地、且通过核验的资料才计数。下载失败、待核验、仅有链接或只有部分正文的资料都不计数，统一登记在 [download_failures_cn.csv](download_failures_cn.csv)。

## 数量

统一进度句式：“已核验完整资料 X / 目标约 50；待核验 Y；下载失败 Z。”

| 类别 | 已核验 | 待核验 | 下载失败 | 近三年占比 | 三年前补充 | 2026 年首次公开 |
|---|---|---|---|---|---|---|
| 01 大语言模型基础 | 54 | 0 | 0 | 92.6% | 4 | 6 |
| 02 预训练与数据 | 55 | 0 | 0 | 92.7% | 4 | 6 |
| 03 微调与对齐 | 57 | 0 | 0 | 91.2% | 5 | 1 |
| 04 推理与测试时计算 | 61 | 0 | 0 | 91.8% | 5 | 3 |
| 05 检索增强与知识 | 57 | 0 | 0 | 93.0% | 4 | 2 |
| 06 智能体与工具使用 | 58 | 0 | 0 | 91.4% | 5 | 2 |
| 07 多模态基础与视觉语言模型 | 52 | 0 | 0 | 92.3% | 4 | 5 |
| 08 图像与视频生成 | 59 | 0 | 0 | 91.5% | 5 | 3 |
| 09 音频与语音大模型 | 56 | 0 | 0 | 91.1% | 5 | 5 |
| 10 视频理解与具身多模态 | 54 | 0 | 0 | 92.6% | 4 | 8 |
| 11 高效训练与部署 | 63 | 0 | 0 | 92.1% | 5 | 7 |
| 12 评测与可信性 | 63 | 0 | 0 | 95.2% | 3 | 6 |
| 13 大学课程讲义包 | 42（缺 8） | 0 | 3 | 近三年学期 41/42 | 1（Stanford CS324，2022 冬） | 16 |
| 14 教科书、专著与参考书 | 39（缺 11） | 0 | 1 | 2023 年及以后版本 31/39 | 8 本为较早版本（写了年份例外理由） | — |

- 全库去重后共 **770 份独立完整资料**：论文 689 篇、课程讲义包 42 份、书籍 39 本。
- 每份资料只有一个主分类，没有一份资料被两个类别同时计数。交叉分类只作标签，每类的交叉标签列表见 `domains/*/index_cn.md`。
- 获取方式：770 份都是本轮新下载，没有复用本地已有文件。其中 162 份与同期在建的“机器学习与深度学习”库中的文件**完全相同**（SHA256 一致），记为“跨库重复”。与“时间序列”库没有重复。

## 目录

| 路径 | 内容 |
|---|---|
| [catalog_cn.csv](catalog_cn.csv) | 总目录（UTF-8 带 BOM），每行一份已核验资料，共 57 列，字段说明见下 |
| [reading_map_cn.md](reading_map_cn.md) | 三条阅读路线：大语言模型、多模态理解、多模态生成 |
| [search_log_cn.md](search_log_cn.md) | 检索来源、候选数量、纳入与排除原则、人工处理记录、已知局限 |
| [download_failures_cn.csv](download_failures_cn.csv) | 下载失败或核验未通过、未计数的资料 |
| [checksums_en.sha256](checksums_en.sha256) | 全部 2915 个实体文件的 SHA256，可在本目录执行 `sha256sum -c checksums_en.sha256` 校验 |
| [papers/](papers/) | 论文 PDF，命名为 `首次公开年份_第一作者姓_短标题_en.pdf` |
| [university_materials/](university_materials/) | 每门课一个目录，命名为 `学校_课程代码_学期_LectureMaterials_en`（中文课程以 `_cn` 结尾）。目录内是讲义文件和 `manifest_en.json`（每个文件的来源 URL、讲次标签与 SHA256） |
| [books/](books/) | 单文件书籍直接放在这里；多卷或 HTML 书各占一个目录，内含 `manifest_en.json` |
| [domains/](domains/) | 14 个类别目录，每个含 `index_cn.md`：主分类资料（按优先阅读排名排序）和交叉标签资料，链接指向库内唯一的实体文件 |
| [scripts/](scripts/) | 脚本、种子、注释、核验结果与断点状态（见下） |

文件名的语言后缀：`_en` 为英文，`_cn` 为中文。只改文件名，不改内容。HTML 书籍保留原始的内部文件名和相对链接，以免破坏离线阅读，只在外层目录名加后缀（`..._html_en`）。

## 总目录字段

- **通用字段**：文献编号（`LMM-类别-序号`）、主分类、交叉分类及依据、资料类型、子方向、标题、作者或教师、学校或机构、渠道或出版社、发表状态及依据、首次公开日期、日期精度、首次公开依据、下载版本、版本日期、正式发表年份、时间窗口、较早资料保留理由、DOI、arXiv ID、ISBN、原始来源、下载链接、语言、格式、本地路径、完整性、核验状态、核验详情、SHA256、获取方式、跨库关系、选入理由、阅读优先级、优先阅读排名及理由。
- **论文另有**：研究问题、方法类别、输入模态、输出模态、模型规模、数据可用性、代码可用性、主要评测任务、简介、字段依据。这些字段只依据摘要、arXiv 注释和 PDF 首页链接；摘要没有提到的写“待全文核实”。简介中的结论都以“作者称/摘要称”转述，未经精读核实。
- **课程与书籍另有**：课程代码、学期或书籍版本、原著年份、版本或学期年份、先修要求、章节覆盖、内容完整性说明、阅读阶段、一般基础材料理由。
- **多文件资料的 SHA256**：是资料包哈希，即把各文件的 `sha256  路径` 行排序后再算一次 SHA256。单个文件的哈希见 `checksums_en.sha256` 和各目录的 `manifest_en.json`。

### 发表状态的含义

| 状态 | 依据 |
|---|---|
| 正式发表：会议 年份 | 在官方论文集索引中标题完全匹配。来源：NeurIPS、ICLR、ICML、CoRL、CVPR、ICCV、ECCV、ACL 系列、Interspeech、TMLR |
| 正式发表（期刊/会议论文集） | Crossref 中有标题匹配的非预印本记录 |
| 作者声明已接收 / 已发表（未独立核实） | 仅见于 arXiv 注释或 journal_ref |
| 技术报告（以预印本形式公开） | 机构技术报告，且没有找到正式发表记录 |
| 预印本（未发现正式发表信息） | 以上来源都没有匹配。不代表一定没有发表：NeurIPS 2025 官方页检索时只列出 64 篇，COLM、AAAI 等未覆盖 |

## 核验标准

- **论文**：HTTP 200；`%PDF-` 文件头；pypdf 可解析；≥4 页；可抽取字符 ≥12000；不是补充材料；首页两页内标题有效词匹配 ≥0.8；正文中能找到首作者姓氏或团队名；有参考文献标题。只有软性检查不过的进入“待核验”，人工用首页文本核对后才计入，核对说明记录在结果文件中。
- **书籍**：主 PDF 页数达到下限（一般 100 页）、标题与作者见于前部、有目录。中文书若因字体编码抽取乱码，人工核对后在种子的 `manual_check_note` 中写明。HTML 书用 wget 做离线镜像（遵守 robots），书中目录链接到的全部章节文件都必须在本地存在，并抽查关键章节的文字。
- **课程**：官方日程页上有讲义链接的讲次全部下载，且每个文件都通过类型检查。官方没有发布讲义的讲次（如嘉宾讲座）在“内容完整性说明”中如实写明。

## 续跑与复核

宿主机没有 pip。pypdf 用 PyPI 上的纯 Python wheel 解压到库外目录；下载暂存目录也在库外：

```bash
mkdir -p /root/.cache/lmm_lit/pylib /root/.cache/lmm_lit/staging
curl -sSL -o /root/.cache/lmm_lit/pypdf-5.1.0.whl \
  https://files.pythonhosted.org/packages/04/fc/6f52588ac1cb4400a7804ef88d0d4e00cfe57a7ac6793ec3b00de5a8758b/pypdf-5.1.0-py3-none-any.whl
echo "3bd4f503f4ebc58bae40d81e81a9176c400cbbac2ba2d877367595fb524dfdfc  /root/.cache/lmm_lit/pypdf-5.1.0.whl" | sha256sum -c \
  && python3 -I -c "import zipfile; zipfile.ZipFile('/root/.cache/lmm_lit/pypdf-5.1.0.whl').extractall('/root/.cache/lmm_lit/pylib')"

cd /root/large_model_multimodal_literature
python3 -I scripts/papers_en.py status 01            # 任一论文类别的进度、近三年占比、失败明细
python3 -I scripts/papers_en.py resolve 01           # 新增种子后：解析 arXiv 元数据
python3 -I scripts/papers_en.py download 01          # 断点续跑：只处理未完成条目；--retry-failed 重试失败项
python3 -I scripts/materials_en.py status 13         # 课程（13）/ 书籍（14）
python3 -I scripts/materials_en.py fetch 14 --sid 14-040   # 重试单条（例如 IIR 网络恢复后）
python3 -I scripts/venues_en.py match                # 新论文的发表状态核验（已有结果自动跳过）
python3 -I scripts/build_catalog_en.py               # 重新生成总目录、失败表、校验和、domains 索引
sha256sum -c checksums_en.sha256                     # 全量校验
```

### scripts/ 说明

| 文件 | 作用 |
|---|---|
| `lmm_common_en.py` | 公共函数：路径、类别表、跨进程按主机限速与退避、下载、标题匹配 |
| `papers_en.py` | 论文流水线：resolve / download / status / brief / search / text / manual |
| `materials_en.py` | 课程讲义包与书籍：下载、类型检查、完整性检查、HTML 离线镜像、资料包哈希 |
| `venues_en.py` | 官方论文集标题索引的构建与匹配，Crossref 补充 |
| `build_catalog_en.py` | 生成总目录、失败表、校验和、domains 索引与统计（`state/stats_en.json`） |
| `inspect_pdf_en.py` | 人工核验辅助：打印 PDF 指定页的文本 |
| `pipeline_guide_cn.md` | 种子与注释字段说明、命令与核验标准 |
| `seeds/` | 每类候选种子，包括选入理由、三年前保留理由、交叉分类、备选与排除记录 |
| `annotations/` | 论文注释：研究问题、模态、规模、可用性、评测任务、简介、前 10 名 |
| `state/` | 断点状态：各类核验结果、arXiv 元数据缓存、主分类认领表、发表状态核验结果 |
| `work/` | 子任务说明、摘要汇编（brief）、运行日志 |

## 已知问题

- 第 13 类缺 8 份，第 14 类缺 11 本，都标为**未完成**。原因是许多课程的讲义放在 Google Drive、Dropbox 或需登录的平台上，而近年大模型相关书籍大多没有合法的公开全文。没有用零散章节或重复版本补数。
- 下载失败 4 项：NYU DS-GA 1011（第 10 讲讲义 404）、UW CSE 447/517（讲义链接全部 404）、Columbia COMS 6706（2 份讲义 404）、《Introduction to Information Retrieval》（本机到 nlp.stanford.edu 网络不可达）。
- 两本 HTML 书的正文、图片和章节间链接都在本地。数学公式依赖 MathJax CDN，离线时显示为 LaTeX 源码。
- 中国人民大学《大语言模型》课程课件（13-A18）是教材配套的官方课件，没有单一课程编号和学期，按“2025 课件版”记录。
