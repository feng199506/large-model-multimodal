# 阅读地图：三条阅读路线

编号对应 [catalog_cn.csv](catalog_cn.csv) 中的“文献编号”。每类“优先阅读前 10”见各类目录 [domains/](domains/) 下的 `index_cn.md`（按排名排序），理由写在总目录的“优先阅读理由”列。

路线按“教材/课程打底 → 经典 → 近三年主线 → 前沿与评测”排列。论文简介只依据摘要，未经精读核实。

## 路线一：大语言模型

| 阶段 | 资料 | 作用 |
|---|---|---|
| 1 打底 | LMM-14-023《Understanding Deep Learning》；LMM-13-A01 Stanford CS224N（2026 冬） | 深度学习与 NLP 基础，进入 Transformer |
| 1 打底 | LMM-14-001《Foundations of Large Language Models》或中文 LMM-14-007《大语言模型》 | 大模型全流程主教材，二选一 |
| 2 架构 | LMM-01-057 Transformer → LMM-01-002 RoPE → LMM-01-003 Mamba → LMM-01-045 Kimi Linear / LMM-01-012 Gated Attention | 注意力、位置编码与线性/混合架构 |
| 2 规模 | LMM-01-058 Kaplan 规模定律 → LMM-01-038 过训练与下游预测 | 计算、数据与参数的权衡 |
| 3 数据 | LMM-02-002 FineWeb → LMM-02-003 DCLM → LMM-02-030 数据配比定律 → LMM-02-049 GSM1k 污染检查 | 数据收集、筛选、配比与污染 |
| 3 动手 | LMM-13-A02 Stanford CS336（2026 春） | 从零实现分词、训练、并行与推理 |
| 4 后训练 | LMM-03-004 InstructGPT → LMM-03-003 DPO → LMM-03-021 Tulu 3 → LMM-14-010《RLHF》书 | 指令微调、偏好优化与开放后训练配方 |
| 5 推理 | LMM-04-001 CoT → LMM-04-003 过程监督 → LMM-04-010 测试时计算 → LMM-04-006 DeepSeek-R1 → LMM-04-038 RL 是否提升推理能力 | 测试时计算与推理强化学习 |
| 6 知识与智能体 | LMM-05-036 RAG 综述 → LMM-05-023 Search-R1 → LMM-06-002 ReAct → LMM-06-047 SWE-agent → LMM-14-014《Agentic LLMs》 | 检索、工具与智能体 |
| 7 工程 | LMM-11-051 vLLM → LMM-11-038 投机解码 → LMM-11-022 QuaRot → LMM-14-029《How to Scale Your Model》→ LMM-13-A10 CMU 11-868 | 服务、加速、量化与并行 |
| 8 评测可信 | LMM-12-010 评测误差条 → LMM-12-001 Chatbot Arena → LMM-12-018 幻觉成因 → LMM-12-036 HarmBench → LMM-14-030 AI 安全教材 | 评测方法学、幻觉与安全 |

## 路线二：多模态理解

| 阶段 | 资料 | 作用 |
|---|---|---|
| 1 打底 | LMM-13-B05 Stanford CS231n（2025 春）；LMM-14-035《Foundations of Computer Vision》（HTML） | 视觉表示与视觉 Transformer |
| 1 综览 | LMM-14-018《Multimodal Foundation Models》；LMM-13-B03 CMU 11-777 多模态机器学习 | 多模态问题全景 |
| 2 对齐 | LMM-07-001 CLIP → LMM-07-005 SigLIP 2 | 对比式图文对齐与视觉编码器 |
| 3 融合与 VLM | LMM-07-055 VLM 导论 → LMM-07-004 LLaVA → LMM-07-014 MM1 → LMM-07-013 Cambrian-1 → LMM-07-025 Molmo | 连接器设计、数据与训练配方 |
| 4 规模与原生多模态 | LMM-07-018 原生多模态规模定律 → LMM-07-023 Qwen3-VL | 前沿开放模型与训练规律 |
| 5 文档与 OCR | LMM-07-041 DeepSeek-OCR 及 07 类 OCR/文档子方向 | 文档理解与视觉文本压缩 |
| 6 视频 | LMM-10-008 Video-MME → LMM-10-015 Apollo → LMM-10-024 Thinking in Space → LMM-10-022 V-JEPA 2 | 视频理解、空间推理与视频表示 |
| 7 具身 | LMM-10-001 RT-2 → LMM-10-002 Open X-Embodiment → LMM-10-027 OpenVLA → LMM-10-028 π0 → LMM-14-039《Robot Learning: A Tutorial》→ LMM-13-B14 港大具身智能 | 视觉语言动作模型 |
| 8 语音理解 | LMM-09-043 语音语言模型综述 → LMM-09-014 Audio Flamingo 3 → LMM-09-029 MMAU | 音频语言模型与评测 |
| 9 可信 | 12 类多模态幻觉条目（交叉 07，见 domains/07 交叉标签） | 多模态幻觉评测 |

## 路线三：多模态生成

| 阶段 | 资料 | 作用 |
|---|---|---|
| 1 打底 | LMM-14-023《Understanding Deep Learning》生成模型章节；LMM-13-B02 MIT 6.S184 讲义 | 扩散与流匹配的数学基础 |
| 1 主教材 | LMM-14-021《The Principles of Diffusion Models》；LMM-14-022 扩散教程 | 变分、得分、流三种视角 |
| 2 经典 | LMM-08-001 DDPM → LMM-08-007 LDM → LMM-08-013 DiT → LMM-08-002 Flow Matching | 现代图像生成的四个基石 |
| 3 流匹配与扩展 | LMM-08-038 Flow Matching Guide → LMM-08-014 SD3（整流 Transformer）→ LMM-08-031 REPA | 训练目标与表示对齐 |
| 4 自回归与统一 | LMM-08-004 VAR → LMM-08-016 无 VQ 自回归 → LMM-08-046 BAGEL（统一理解与生成） | 自回归生成与统一模型 |
| 5 控制与编辑 | LMM-08-003 ControlNet → LMM-08-041 FLUX.1 Kontext → LMM-08-053 FireRed-Image-Edit（2026） | 条件控制与指令编辑 |
| 6 视频 | LMM-08-024 Wan → LMM-08-036 Self Forcing → LMM-08-058 Rolling Forcing → LMM-08-059 对角蒸馏（2026） | 视频生成与实时流式生成 |
| 7 对齐 | LMM-08-008 Flow-GRPO | 生成模型的强化学习对齐 |
| 8 音频生成 | LMM-09-012 Seed-TTS → LMM-09-022 CosyVoice 2 → LMM-09-005 Moshi → LMM-09-053 MMAudio | 语音合成、实时对话与视频配音 |
| 9 世界模型 | LMM-10-047 Genie → LMM-10-078 机器人世界模型综述（2026） | 交互式生成与世界模型 |
| 课程 | LMM-13-B04 CMU 10-423 生成式 AI；LMM-13-B01 MIT 6.S978；LMM-13-B06 Stanford CS236 | 系统课程 |
