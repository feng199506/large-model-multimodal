# 子任务说明：第 13 类 著名大学课程教材与讲义（课程讲义包）

总任务：在 /root/large_model_multimodal_literature/ 建立“大模型与多模态模型”文献库。第 13 类目标约 50 份**完整课程讲义包**：系统讲授大语言模型、多模态学习及必要基础的**官方教学材料**。两名子代理分工检索（见各自任务说明中的方向），合计目标约 50；你的份额约 25。

只用脚本 scripts/materials_en.py 下载与核验（先读它开头的说明和 cmd_fetch 逻辑）；不要改 scripts/*.py（发现缺陷就停下并在回报中说明）。只写你自己的种子文件；不要碰本目录以外的文件。

## 计数口径
- 一门课的一个学期 = 一份资料包（讲义/幻灯片/讲稿的完整集合）；不把每讲分别计数。相同课程不同学期内容基本一致时只收一个（优先最近学期）。
- 完整：课程官方日程页上发布的**全部讲义文件**都下载并核验通过（expected_items = 官方日程中有讲义链接的讲次数，脚本会核对文件数）。官方本就没有发布讲义的讲次（如嘉宾讲座无幻灯片）要在 completeness_note 中如实写明“N 讲中 M 讲官方发布了讲义”。只有视频、只有阅读清单、讲义放在需登录/Google Drive 预览页的课程，不计数（可登记为失败并说明原因）。
- 来源优先：课程官方主页、教师主页、机构仓储、课程官方 GitHub（可用 GitHub release 或 `https://codeload.github.com/<org>/<repo>/zip/refs/heads/<branch>` 下载整个讲义仓库的 zip，kind=zip；仓库须是课程官方仓库且以讲义为主，不要下载含模型权重或数据集的大仓库）。不得绕过登录或访问控制；robots 禁止的不抓。
- 核验并记录：学校、课程代码、课程名、学期、教师（来自官方页面），以及依据 URL。
- 内容须与本任务直接相关（大模型、NLP 与 LLM、多模态、生成模型、语音大模型、具身/机器人学习、高效 ML 系统、AI 安全等）；一般深度学习基础课最多 2–3 门，并写明必要性。不以学校名气代替内容审核。
- 学期优先近三年（2023 秋及以后）；更早的经典课程需写 old_reason。

## 种子文件
写到你自己的文件（见任务说明给的文件名），JSON 数组，每项：
```json
{"sid": "13-A01", "kind": "course", "university": "Stanford University", "course_code": "CS336",
 "course_title": "Language Modeling from Scratch", "term": "Spring 2025", "term_year": 2025,
 "instructors": ["Tatsunori Hashimoto", "Percy Liang"], "official_url": "...", "schedule_url": "...",
 "verification_basis": "课程主页标题与教师名、学期见 <URL>",
 "dir_name": "Stanford_CS336_2025Spring_LectureMaterials_en",
 "files": [{"url": "...", "name": "lecture01_overview_en.pdf", "kind": "pdf", "label": "Lecture 1 Overview"}],
 "expected_items": 17, "completeness_note": "官方日程 17 讲均有讲义，全部下载",
 "prereq": "先修要求（官方页面所写）", "coverage": "章节/主题覆盖（中文一句）",
 "stage": "初学/进阶研究/工程实践", "language": "en",
 "reason": "选入理由（中文）", "priority": "高/中/低", "old_reason": "",
 "cross": ["07"]}
```
- 文件名一律在扩展名前加语言后缀（英文 `_en`、中文 `_cn`），只改文件名不改内容；`dir_name` 也以 `_en`/`_cn` 结尾。
- 辅助文件（课程大纲页 HTML 等）可加 `"aux": true`，不计入讲义数。
- 用 `python3 -I scripts/materials_en.py links <官方日程页URL> --pattern '\.pdf$'` 列出官方页上的讲义链接，再写入 files。
- 下载：`python3 -I scripts/materials_en.py fetch 13 --sid <sid>`（逐个跑，不要并行）；查看：`status 13`。

## 礼貌访问
脚本已按主机限速（≥3 秒）。不要自己用 curl 批量抓取。每门课先确认可行再写全部文件链接。

## 最终回报（简短，中文）
- 统一进度句（只算你负责的部分）：“已核验完整资料 X / 目标约 25；待核验 Y；下载失败 Z。”
- 近三年学期占比；较早课程及保留理由。
- 每门已核验课程一行：sid、学校、课程代码、学期、讲义数/官方讲次数。
- 失败或放弃的课程及原因；明显缺口。
