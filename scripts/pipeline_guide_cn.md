# 论文流水线说明（第 01–12 类）

所有命令在 `/root/large_model_multimodal_literature` 下运行，一律用 `python3 -I`（宿主机无 pip；pypdf 解压在 `/root/.cache/lmm_lit/pylib`，下载暂存在 `/root/.cache/lmm_lit/staging`）。

## 日期规则
- 检索日 2026-10-29；近三年窗口：首次公开日期 ≥ 2023-10-29。
- 首次公开日期 = arXiv v1 提交日（无 arXiv 时用最早公开版本日期，并写精度）。正式发表日期、最新版本日期另记，旧研究的新版本不算新研究。
- 每类已核验资料中近三年 ≥ 85%（争取 ≥ 90%）；三年前经典补充每类最多 5 篇，种子里逐篇写 `old_reason`。

## 种子文件 `scripts/seeds/<NN_slug>_seed_cn.json`
JSON 数组，每项一个候选：

| 字段 | 说明 |
|---|---|
| `sid` | 类内编号，如 `03-017`，唯一且不复用 |
| `arxiv` | arXiv ID（无版本号）。不确定时可只给 `title`，`resolve` 会按标题检索并回写 |
| `title` | 英文原题（用于核对 ID 是否正确） |
| `subtopic` | 子方向（中文，取本类说明中的子方向词） |
| `type` | `原始研究` / `综述` / `学术教程` / `技术报告` |
| `priority` | 阅读优先级 `高` / `中` / `低` |
| `reason` | 选入理由（中文一句，说明它代表的问题/方法，不写未经核实的结论） |
| `old_reason` | 首次公开早于 2023-10-29 时必填：为何必须作为经典补充 |
| `cross` | 交叉分类编号列表，如 `["11"]`；`cross_reason` 写实质依据 |
| `reserve` | `true` 表示备选：主列表核验数不足 `--target` 时才下载 |
| `cross_only` | `true` 表示该文主分类在别类（已被别类认领），本类只作交叉标签，不下载不计数；需写 `cross_reason` |
| `exclude` | `true` 表示人工排除（写 `exclude_reason`），不下载 |
| `team` | 作者为团队署名时的团队名（如 `Qwen Team`），用于首作者核验 |
| 非 arXiv 文献 | 另给 `pdf_url`（合法公开全文）、`landing_url`、`authors`（列表）、`first_public_date`、`date_precision`（日/月/年）、`first_public_basis`、`version`、`version_date`、`doi` |

## 命令
```bash
python3 -I scripts/papers_en.py resolve NN          # 元数据（arXiv API，被限流时回退 abs 页面），标题不符时按标题改正 ID
python3 -I scripts/papers_en.py download NN         # 逐个下载核验，直到本类核验数达到 --target（默认 50）
python3 -I scripts/papers_en.py status NN           # 统一进度句式 + 近三年占比 + 待核验/失败明细 + 子方向分布
python3 -I scripts/papers_en.py search '<arXiv 查询>' --max 40 --sort submittedDate
                                                    # 例：'abs:"process reward" AND submittedDate:[202501010000 TO 202610290000]'
python3 -I scripts/papers_en.py text NN <sid> --pages 2   # 查看已下载 PDF 首页文本（人工核对）
python3 -I scripts/papers_en.py manual NN <sid> --note '<核对了什么>'  # 仅限 pending 且硬性检查通过
python3 -I scripts/papers_en.py brief NN [--missing-only]   # 生成 scripts/work/<NN_slug>_brief_en.md（摘要等）供写注释
```
- `download` 只处理未完成项，可重复运行（断点续跑）；`--retry-failed` 重试失败项。
- 同一论文只能有一个主分类：被别类认领的会记为 `duplicate_elsewhere`，不计数；需要时在本类加 `cross_only` 条目。
- 若本机此前的文献库（机器学习深度学习库、时间序列库）的目录里已有同一 arXiv ID 的文件，脚本复制并重新核验，记为“本地已有且复用”。

## 核验标准（计数前提）
HTTP 200、`%PDF-` 文件头、pypdf 可解析、≥4 页、可抽取字符 ≥12000、非补充材料；首页两页内标题有效词匹配 ≥0.8；首作者姓氏（或团队名）出现在正文；存在参考文献标题。仅软性检查不过的进 `pending`，人工用 `text` 核对后才能 `manual` 提升，`--note` 要写明核对内容。

## 注释文件 `scripts/annotations/<NN_slug>_annot_cn.json`
以 `sid` 为键的对象。只依据摘要、arXiv 注释和 PDF 首页可见内容；摘要未提供的写“待全文核实”，不得编造模型规模、实验结论或数值。

```json
{
 "03-017": {
  "research_question": "研究问题（中文一句）",
  "method_category": "方法类别（如：偏好优化/离线；数据合成；检索增强）",
  "input_modalities": "文本",
  "output_modalities": "文本",
  "model_scale": "摘要所述规模，如“7B/70B（摘要）”；未提及写“待全文核实”；不适用写“不适用”",
  "data_availability": "公开/部分公开/未说明（依据）",
  "code_availability": "公开：URL / 摘要未提及，待全文核实",
  "eval_tasks": "主要评测任务或基准（摘要所列）",
  "summary": "中文简介 2–3 句：做了什么、怎么做；结论用“作者称/摘要称”转述",
  "field_basis": "摘要 / 摘要+arXiv注释 / 摘要+PDF首页链接",
  "top10_rank": 3,
  "top10_reason": "仅前 10 篇填写：为什么优先读"
 }
}
```
