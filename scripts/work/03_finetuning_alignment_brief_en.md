# Brief for annotation: 03 微调与对齐

## 03-001 | What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning
- arXiv: 2312.15685  first public: 2023-12-25  latest: 2024-04-16  primary cat: cs.CL
- authors (5): Wei Liu; Weihao Zeng; Keqing He; Yong Jiang; Junxian He
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: ICLR2024 Camera Ready. Data and model checkpoints are available at https://github.com/hkust-nlp/deita
- URLs on first pages of PDF: https://github.com/hkust-nlp/deita
- pages: 21

ABSTRACT: Instruction tuning is a standard technique employed to align large language models to end tasks and user preferences after the initial pretraining phase. Recent research indicates the critical role of data engineering in instruction tuning -- when appropriately selected, only limited data is necessary to achieve superior performance. However, we still lack a principled understanding of what makes good instruction tuning data for alignment, and how we should select data automatically and effectively. In this work, we delve deeply into automatic data selection strategies for alignment. We start with controlled studies to measure data across three dimensions: complexity, quality, and diversity, along which we examine existing methods and introduce novel techniques for enhanced data measurement. Subsequently, we propose a simple strategy to select data samples based on the measurement. We present deita (short for Data-Efficient Instruction Tuning for Alignment), a series of models fine-tuned from LLaMA and Mistral models using data samples automatically selected with our proposed approach. Empirically, deita performs better or on par with the state-of-the-art open-source alignment models with only 6K SFT training data samples -- over 10x less than the data used in the baselines. When further trained with direct preference optimization (DPO), deita-Mistral-7B + DPO trained with 6K SFT and 10K DPO samples achieve 7.55 MT-Bench and 90.06% AlpacaEval scores. We anticipate this work to provide tools on automatic data selection, facilitating data-efficient alignment. We release our models as well as the selected datasets for future researches to effectively align models more efficiently.

## 03-002 | LoRA: Low-Rank Adaptation of Large Language Models
- arXiv: 2106.09685  first public: 2021-06-17  latest: 2021-10-16  primary cat: cs.CL
- authors (8): Edward J. Hu; Yelong Shen; Phillip Wallis; Zeyuan Allen-Zhu; Yuanzhi Li; Shean Wang ...
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: Draft V2 includes better baselines, experiments on GLUE, and more on adapter latency
- URLs on first pages of PDF: https://github.com/microsoft/LoRA
- pages: 26

ABSTRACT: An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at https://github.com/microsoft/LoRA.

## 03-003 | Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- arXiv: 2305.18290  first public: 2023-05-29  latest: 2024-07-29  primary cat: cs.LG
- authors (6): Rafael Rafailov; Archit Sharma; Eric Mitchell; Stefano Ermon; Christopher D. Manning; Chelsea Finn
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- pages: 27

ABSTRACT: While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavior is difficult due to the completely unsupervised nature of their training. Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF). However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model. In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss. The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for sampling from the LM during fine-tuning or performing significant hyperparameter tuning. Our experiments show that DPO can fine-tune LMs to align with human preferences as well as or better than existing methods. Notably, fine-tuning with DPO exceeds PPO-based RLHF in ability to control sentiment of generations, and matches or improves response quality in summarization and single-turn dialogue while being substantially simpler to implement and train.

## 03-004 | Training language models to follow instructions with human feedback
- arXiv: 2203.02155  first public: 2022-03-04  latest: 2022-03-04  primary cat: cs.CL
- authors (20): Long Ouyang; Jeff Wu; Xu Jiang; Diogo Almeida; Carroll L. Wainwright; Pamela Mishkin ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- pages: 68

ABSTRACT: Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

## 03-005 | Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning
- arXiv: 2402.04833  first public: 2024-02-07  latest: 2024-06-04  primary cat: cs.CL
- authors (4): Hao Zhao; Maksym Andriushchenko; Francesco Croce; Nicolas Flammarion
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2024. This camera-ready version adds MT-Bench evaluations, a human study, more thorough analysis of length bias. Code at https://github.com/tml-epfl/long-is-more-for-alignment
- pages: 30

ABSTRACT: There is a consensus that instruction fine-tuning of LLMs requires high-quality data, but what are they? LIMA (NeurIPS 2023) and AlpaGasus (ICLR 2024) are state-of-the-art methods for selecting such high-quality examples, either via manual curation or using GPT-3.5-Turbo as a quality scorer. We show that the extremely simple baseline of selecting the 1,000 instructions with longest responses -- that intuitively contain more learnable information and are harder to overfit -- from standard datasets can consistently outperform these sophisticated methods according to GPT-4 and PaLM-2 as judges, while remaining competitive on the Open LLM benchmarks that test factual knowledge. We demonstrate this for several LLMs (Llama-2-7B, Llama-2-13B, Mistral-7B-v0.1) and datasets (Alpaca-52k, Evol-Instruct-70k). In addition, a lightweight refinement of such long instructions can further improve the abilities of the fine-tuned LLMs, and allows us to obtain competitive results on MT-Bench and the 2nd highest-ranked Llama-2-7B-based model on AlpacaEval 2.0, while training on only 1,000 examples and no extra preference data. We also conduct a thorough analysis of our models to ensure that their enhanced performance is not simply due to GPT-4's preference for longer responses. Overall, our findings suggest that fine-tuning on the longest responses should be the default baseline for any work on instruction fine-tuning. We provide our code at https://github.com/tml-epfl/long-is-more-for-alignment.

## 03-006 | QLoRA: Efficient Finetuning of Quantized LLMs
- arXiv: 2305.14314  first public: 2023-05-23  latest: 2023-05-23  primary cat: cs.LG
- authors (4): Tim Dettmers; Artidoro Pagnoni; Ari Holtzman; Luke Zettlemoyer
- seed subtopic: 参数高效微调; type: 原始研究; cross: ['11']
- arXiv comment: Extended NeurIPS submission
- URLs on first pages of PDF: https://github.com/TimDettmers/bitsandbytes https://github.com/artidoro/qlora
- pages: 26

ABSTRACT: We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters~(LoRA). Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) double quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) paged optimziers to manage memory spikes. We use QLoRA to finetune more than 1,000 models, providing a detailed analysis of instruction following and chatbot performance across 8 instruction datasets, multiple model types (LLaMA, T5), and model scales that would be infeasible to run with regular finetuning (e.g. 33B and 65B parameter models). Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when using smaller models than the previous SoTA. We provide a detailed analysis of chatbot performance based on both human and GPT-4 evaluations showing that GPT-4 evaluations are a cheap and reasonable alternative to human evaluation. Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots. A lemon-picked analysis demonstrates where Guanaco fails compared to ChatGPT. We release all of our models and code, including CUDA kernels for 4-bit training.

## 03-007 | KTO: Model Alignment as Prospect Theoretic Optimization
- arXiv: 2402.01306  first public: 2024-02-02  latest: 2026-09-08  primary cat: cs.LG
- authors (5): Kawin Ethayarajh; Winnie Xu; Niklas Muennighoff; Dan Jurafsky; Douwe Kiela
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: ICML 2024
- pages: 21

ABSTRACT: Kahneman & Tversky's $\textit{prospect theory}$ tells us that humans perceive random variables in a biased but well-defined manner (1992); for example, humans are famously loss-averse. We show that objectives for aligning LLMs with human feedback implicitly incorporate many of these biases -- the success of these objectives (e.g., DPO) over cross-entropy minimization can partly be ascribed to them belonging to a family of loss functions that we call $\textit{human-aware losses}$ (HALOs). However, the utility functions these methods attribute to humans still differ from those in the prospect theory literature. Using a Kahneman-Tversky model of human utility, we propose a HALO that directly maximizes the utility of generations instead of maximizing the log-likelihood of preferences, as current methods do. We call this approach KTO, and it matches or exceeds the performance of preference-based methods at scales from 1B to 30B, despite only learning from a binary signal of whether an output is desirable. More broadly, our work suggests that there is no one HALO that is universally superior; the best loss depends on the inductive biases most appropriate for a given setting, an oft-overlooked consideration.

## 03-008 | Constitutional AI: Harmlessness from AI Feedback
- arXiv: 2212.08073  first public: 2022-12-15  latest: 2022-12-15  primary cat: cs.CL
- authors (51): Yuntao Bai; Saurav Kadavath; Sandipan Kundu; Amanda Askell; Jackson Kernion; Andy Jones ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: ['12']
- pages: 34

ABSTRACT: As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

## 03-009 | LESS: Selecting Influential Data for Targeted Instruction Tuning
- arXiv: 2402.04333  first public: 2024-02-06  latest: 2024-06-13  primary cat: cs.CL
- authors (5): Mengzhou Xia; Sadhika Malladi; Suchin Gururangan; Sanjeev Arora; Danqi Chen
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: ICML 2024; Code and data are available at https://github.com/princeton-nlp/LESS
- pages: 29

ABSTRACT: Instruction tuning has unlocked powerful capabilities in large language models (LLMs), effectively using combined datasets to develop generalpurpose chatbots. However, real-world applications often require a specialized suite of skills (e.g., reasoning). The challenge lies in identifying the most relevant data from these extensive datasets to effectively develop specific capabilities, a setting we frame as targeted instruction tuning. We propose LESS, an optimizer-aware and practically efficient algorithm to effectively estimate data influences and perform Low-rank gradiEnt Similarity Search for instruction data selection. Crucially, LESS adapts existing influence formulations to work with the Adam optimizer and variable-length instruction data. LESS first constructs a highly reusable and transferable gradient datastore with low-dimensional gradient features and then selects examples based on their similarity to few-shot examples embodying a specific capability. Experiments show that training on a LESS-selected 5% of the data can often outperform training on the full dataset across diverse downstream tasks. Furthermore, the selected data is highly transferable: smaller models can be leveraged to select useful data for larger models and models from different families. Our qualitative analysis shows that our method goes beyond surface form cues to identify data that exemplifies the necessary reasoning skills for the intended downstream application.

## 03-010 | DoRA: Weight-Decomposed Low-Rank Adaptation
- arXiv: 2402.09353  first public: 2024-02-14  latest: 2024-07-09  primary cat: cs.CL
- authors (7): Shih-Yang Liu; Chien-Yi Wang; Hongxu Yin; Pavlo Molchanov; Yu-Chiang Frank Wang; Kwang-Ting Cheng ...
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: ICML2024(Oral)
- pages: 23

ABSTRACT: Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs. However, there still often exists an accuracy gap between these methods and full fine-tuning (FT). In this work, we first introduce a novel weight decomposition analysis to investigate the inherent differences between FT and LoRA. Aiming to resemble the learning capacity of FT from the findings, we propose Weight-Decomposed Low-Rank Adaptation (DoRA). DoRA decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning, specifically employing LoRA for directional updates to efficiently minimize the number of trainable parameters. By employing \ours, we enhance both the learning capacity and training stability of LoRA while avoiding any additional inference overhead. \ours~consistently outperforms LoRA on fine-tuning LLaMA, LLaVA, and VL-BART on various downstream tasks, such as commonsense reasoning, visual instruction tuning, and image/video-text understanding. Code is available at https://github.com/NVlabs/DoRA.

## 03-011 | ORPO: Monolithic Preference Optimization without Reference Model
- arXiv: 2403.07691  first public: 2024-03-12  latest: 2024-03-14  primary cat: cs.CL
- authors (3): Jiwoo Hong; Noah Lee; James Thorne
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/xfactlab/orpo https://huggingface.co/kaist-ai/
- pages: 22

ABSTRACT: While recent preference alignment algorithms for language models have demonstrated promising results, supervised fine-tuning (SFT) remains imperative for achieving successful convergence. In this paper, we study the crucial role of SFT within the context of preference alignment, emphasizing that a minor penalty for the disfavored generation style is sufficient for preference-aligned SFT. Building on this foundation, we introduce a straightforward and innovative reference model-free monolithic odds ratio preference optimization algorithm, ORPO, eliminating the necessity for an additional preference alignment phase. We demonstrate, both empirically and theoretically, that the odds ratio is a sensible choice for contrasting favored and disfavored styles during SFT across the diverse sizes from 125M to 7B. Specifically, fine-tuning Phi-2 (2.7B), Llama-2 (7B), and Mistral (7B) with ORPO on the UltraFeedback alone surpasses the performance of state-of-the-art language models with more than 7B and 13B parameters: achieving up to 12.20% on $\text{AlpacaEval}_{2.0}$ (Figure 1), 66.19% on IFEval (instruction-level loose, Table 6), and 7.32 in MT-Bench (Figure 12). We release code and model checkpoints for Mistral-ORPO-$α$ (7B) and Mistral-ORPO-$β$ (7B).

## 03-012 | Self-Rewarding Language Models
- arXiv: 2401.10020  first public: 2024-01-18  latest: 2025-03-28  primary cat: cs.CL
- authors (7): Weizhe Yuan; Richard Yuanzhe Pang; Kyunghyun Cho; Xian Li; Sainbayar Sukhbaatar; Jing Xu ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: ICML 2024
- pages: 23

ABSTRACT: We posit that to achieve superhuman agents, future models require superhuman feedback in order to provide an adequate training signal. Current approaches commonly train reward models from human preferences, which may then be bottlenecked by human performance level, and secondly these separate frozen reward models cannot then learn to improve during LLM training. In this work, we study Self-Rewarding Language Models, where the language model itself is used via LLM-as-a-Judge prompting to provide its own rewards during training. We show that during Iterative DPO training that not only does instruction following ability improve, but also the ability to provide high-quality rewards to itself. Fine-tuning Llama 2 70B on three iterations of our approach yields a model that outperforms many existing systems on the AlpacaEval 2.0 leaderboard, including Claude 2, Gemini Pro, and GPT-4 0613. While there is much left still to explore, this work opens the door to the possibility of models that can continually improve in both axes.

## 03-013 | Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing
- arXiv: 2406.08464  first public: 2024-06-12  latest: 2024-10-07  primary cat: cs.CL
- authors (7): Zhangchen Xu; Fengqing Jiang; Luyao Niu; Yuntian Deng; Radha Poovendran; Yejin Choi ...
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: Link: https://magpie-align.github.io/
- pages: 32

ABSTRACT: High-quality instruction data is critical for aligning large language models (LLMs). Although some models, such as Llama-3-Instruct, have open weights, their alignment data remain private, which hinders the democratization of AI. High human labor costs and a limited, predefined scope for prompting prevent existing open-source data creation methods from scaling effectively, potentially limiting the diversity and quality of public alignment datasets. Is it possible to synthesize high-quality instruction data at scale by extracting it directly from an aligned LLM? We present a self-synthesis method for generating large-scale alignment data named Magpie. Our key observation is that aligned LLMs like Llama-3-Instruct can generate a user query when we input only the left-side templates up to the position reserved for user messages, thanks to their auto-regressive nature. We use this method to prompt Llama-3-Instruct and generate 4 million instructions along with their corresponding responses. We perform a comprehensive analysis of the extracted data and select 300K high-quality instances. To compare Magpie data with other public instruction datasets, we fine-tune Llama-3-8B-Base with each dataset and evaluate the performance of the fine-tuned models. Our results indicate that in some tasks, models fine-tuned with Magpie perform comparably to the official Llama-3-8B-Instruct, despite the latter being enhanced with 10 million data points through supervised fine-tuning (SFT) and subsequent feedback learning. We also show that using Magpie solely for SFT can surpass the performance of previous public datasets utilized for both SFT and preference optimization, such as direct preference optimization with UltraFeedback. This advantage is evident on alignment benchmarks such as AlpacaEval, ArenaHard, and WildBench.

## 03-014 | LoRA+: Efficient Low Rank Adaptation of Large Models
- arXiv: 2402.12354  first public: 2024-02-19  latest: 2024-07-04  primary cat: cs.LG
- authors (3): Soufiane Hayou; Nikhil Ghosh; Bin Yu
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: 27 pages
- pages: 24

ABSTRACT: In this paper, we show that Low Rank Adaptation (LoRA) as originally introduced in Hu et al. (2021) leads to suboptimal finetuning of models with large width (embedding dimension). This is due to the fact that adapter matrices A and B in LoRA are updated with the same learning rate. Using scaling arguments for large width networks, we demonstrate that using the same learning rate for A and B does not allow efficient feature learning. We then show that this suboptimality of LoRA can be corrected simply by setting different learning rates for the LoRA adapter matrices A and B with a well-chosen ratio. We call this proposed algorithm LoRA$+$. In our extensive experiments, LoRA$+$ improves performance (1-2 $\%$ improvements) and finetuning speed (up to $\sim$ 2X SpeedUp), at the same computational cost as LoRA.

## 03-015 | SimPO: Simple Preference Optimization with a Reference-Free Reward
- arXiv: 2405.14734  first public: 2024-05-23  latest: 2024-11-01  primary cat: cs.CL
- authors (3): Yu Meng; Mengzhou Xia; Danqi Chen
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024. Code & models: https://github.com/princeton-nlp/SimPO. v3 updates: Gemma 2 results (Appendix J); more discussions about length normalization (Section 2.2) and KL regularization (Section 2.3)
- URLs on first pages of PDF: https://github.com/princeton-nlp/SimPO
- pages: 32

ABSTRACT: Direct Preference Optimization (DPO) is a widely used offline preference optimization algorithm that reparameterizes reward functions in reinforcement learning from human feedback (RLHF) to enhance simplicity and training stability. In this work, we propose SimPO, a simpler yet more effective approach. The effectiveness of SimPO is attributed to a key design: using the average log probability of a sequence as the implicit reward. This reward formulation better aligns with model generation and eliminates the need for a reference model, making it more compute and memory efficient. Additionally, we introduce a target reward margin to the Bradley-Terry objective to encourage a larger margin between the winning and losing responses, further improving the algorithm's performance. We compare SimPO to DPO and its latest variants across various state-of-the-art training setups, including both base and instruction-tuned models such as Mistral, Llama 3, and Gemma 2. We evaluate on extensive chat-based evaluation benchmarks, including AlpacaEval 2, MT-Bench, and Arena-Hard. Our results demonstrate that SimPO consistently and significantly outperforms existing approaches without substantially increasing response length. Specifically, SimPO outperforms DPO by up to 6.4 points on AlpacaEval 2 and by up to 7.5 points on Arena-Hard. Our top-performing model, built on Gemma-2-9B-it, achieves a 72.4% length-controlled win rate on AlpacaEval 2, a 59.1% win rate on Arena-Hard, and ranks 1st on Chatbot Arena among <10B models with real user votes.

## 03-016 | Self-Taught Evaluators
- arXiv: 2408.02666  first public: 2024-08-05  latest: 2024-08-08  primary cat: cs.CL
- authors (10): Tianlu Wang; Ilia Kulikov; Olga Golovneva; Ping Yu; Weizhe Yuan; Jane Dwivedi-Yu ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- pages: 16

ABSTRACT: Model-based evaluation is at the heart of successful model development -- as a reward model for training, and as a replacement for human evaluation. To train such evaluators, the standard approach is to collect a large amount of human preference judgments over model responses, which is costly and the data becomes stale as models improve. In this work, we present an approach that aims to im-prove evaluators without human annotations, using synthetic training data only. Starting from unlabeled instructions, our iterative self-improvement scheme generates contrasting model outputs and trains an LLM-as-a-Judge to produce reasoning traces and final judgments, repeating this training at each new iteration using the improved predictions. Without any labeled preference data, our Self-Taught Evaluator can improve a strong LLM (Llama3-70B-Instruct) from 75.4 to 88.3 (88.7 with majority vote) on RewardBench. This outperforms commonly used LLM judges such as GPT-4 and matches the performance of the top-performing reward models trained with labeled examples.

## 03-017 | The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning
- arXiv: 2312.01552  first public: 2023-12-04  latest: 2023-12-04  primary cat: cs.CL
- authors (8): Bill Yuchen Lin; Abhilasha Ravichander; Ximing Lu; Nouha Dziri; Melanie Sclar; Khyathi Chandu ...
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: 26 pages, 8 figures. Project website: https://allenai.github.io/re-align/
- URLs on first pages of PDF: https://allenai.github.io/re-align
- pages: 26

ABSTRACT: The alignment tuning process of large language models (LLMs) typically involves instruction learning through supervised fine-tuning (SFT) and preference tuning via reinforcement learning from human feedback (RLHF). A recent study, LIMA (Zhou et al. 2023), shows that using merely 1K examples for SFT can achieve significant alignment performance as well, suggesting that the effect of alignment tuning might be "superficial." This raises questions about how exactly the alignment tuning transforms a base LLM. We analyze the effect of alignment tuning by examining the token distribution shift between base LLMs and their aligned counterpart. Our findings reveal that base LLMs and their alignment-tuned versions perform nearly identically in decoding on the majority of token positions. Most distribution shifts occur with stylistic tokens. These direct evidence strongly supports the Superficial Alignment Hypothesis suggested by LIMA. Based on these findings, we rethink the alignment of LLMs by posing the research question: how effectively can we align base LLMs without SFT or RLHF? To address this, we introduce a simple, tuning-free alignment method, URIAL. URIAL achieves effective alignment purely through in-context learning (ICL) with base LLMs, requiring as few as three constant stylistic examples and a system prompt. We conduct a fine-grained and interpretable evaluation on a diverse set of examples, named JUST-EVAL-INSTRUCT. Results demonstrate that base LLMs with URIAL can match or even surpass the performance of LLMs aligned with SFT or SFT+RLHF. We show that the gap between tuning-free and tuning-based alignment methods can be significantly reduced through strategic prompting and ICL. Our findings on the superficial nature of alignment tuning and results with URIAL suggest that deeper analysis and theoretical understanding of alignment is crucial to future LLM research.

## 03-018 | GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection
- arXiv: 2403.03507  first public: 2024-03-06  latest: 2024-06-02  primary cat: cs.LG
- authors (6): Jiawei Zhao; Zhenyu Zhang; Beidi Chen; Zhangyang Wang; Anima Anandkumar; Yuandong Tian
- seed subtopic: 参数高效微调; type: 原始研究; cross: ['11']
- arXiv comment: ICML 2024 (Oral)
- pages: 23

ABSTRACT: Training Large Language Models (LLMs) presents significant memory challenges, predominantly due to the growing size of weights and optimizer states. Common memory-reduction approaches, such as low-rank adaptation (LoRA), add a trainable low-rank matrix to the frozen pre-trained weight in each layer, reducing trainable parameters and optimizer states. However, such approaches typically underperform training with full-rank weights in both pre-training and fine-tuning stages since they limit the parameter search to a low-rank subspace and alter the training dynamics, and further, may require full-rank warm start. In this work, we propose Gradient Low-Rank Projection (GaLore), a training strategy that allows full-parameter learning but is more memory-efficient than common low-rank adaptation methods such as LoRA. Our approach reduces memory usage by up to 65.5% in optimizer states while maintaining both efficiency and performance for pre-training on LLaMA 1B and 7B architectures with C4 dataset with up to 19.7B tokens, and on fine-tuning RoBERTa on GLUE tasks. Our 8-bit GaLore further reduces optimizer memory by up to 82.5% and total training memory by 63.3%, compared to a BF16 baseline. Notably, we demonstrate, for the first time, the feasibility of pre-training a 7B model on consumer GPUs with 24GB memory (e.g., NVIDIA RTX 4090) without model parallel, checkpointing, or offloading strategies.

## 03-019 | Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models
- arXiv: 2401.01335  first public: 2024-01-02  latest: 2024-06-14  primary cat: cs.LG
- authors (5): Zixiang Chen; Yihe Deng; Huizhuo Yuan; Kaixuan Ji; Quanquan Gu
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: 22 pages, 6 figures, 7 tables. In ICML 2024
- URLs on first pages of PDF: https://github.com/uclaml/SPIN
- pages: 22

ABSTRACT: Harnessing the power of human-annotated data through Supervised Fine-Tuning (SFT) is pivotal for advancing Large Language Models (LLMs). In this paper, we delve into the prospect of growing a strong LLM out of a weak one without the need for acquiring additional human-annotated data. We propose a new fine-tuning method called Self-Play fIne-tuNing (SPIN), which starts from a supervised fine-tuned model. At the heart of SPIN lies a self-play mechanism, where the LLM refines its capability by playing against instances of itself. More specifically, the LLM generates its own training data from its previous iterations, refining its policy by discerning these self-generated responses from those obtained from human-annotated data. Our method progressively elevates the LLM from a nascent model to a formidable one, unlocking the full potential of human-annotated demonstration data for SFT. Theoretically, we prove that the global optimum to the training objective function of our method is achieved only when the LLM policy aligns with the target data distribution. Empirically, we evaluate our method on several benchmark datasets including the HuggingFace Open LLM Leaderboard, MT-Bench, and datasets from Big-Bench. Our results show that SPIN can significantly improve the LLM's performance across a variety of benchmarks and even outperform models trained through direct preference optimization (DPO) supplemented with extra GPT-4 preference data. This sheds light on the promise of self-play, enabling the achievement of human-level performance in LLMs without the need for expert opponents. Codes are available at https://github.com/uclaml/SPIN.

## 03-020 | RewardBench: Evaluating Reward Models for Language Modeling
- arXiv: 2403.13787  first public: 2024-03-20  latest: 2024-06-08  primary cat: cs.LG
- authors (12): Nathan Lambert; Valentina Pyatkin; Jacob Morrison; LJ Miranda; Bill Yuchen Lin; Khyathi Chandu ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: ['12']
- arXiv comment: 44 pages, 19 figures, 12 tables
- URLs on first pages of PDF: https://github.com/allenai/reward-bench https://huggingface.co/datasets/allenai/reward-bench-results
- pages: 44

ABSTRACT: Reward models (RMs) are at the crux of successfully using RLHF to align pretrained models to human preferences, yet there has been relatively little study that focuses on evaluation of those models. Evaluating reward models presents an opportunity to understand the opaque technologies used for alignment of language models and which values are embedded in them. Resources for reward model training and understanding are sparse in the nascent open-source community around them. To enhance scientific understanding of reward models, we present RewardBench, a benchmark dataset and code-base for evaluation. The RewardBench dataset is a collection of prompt-chosen-rejected trios spanning chat, reasoning, and safety, to benchmark how reward models perform on challenging, structured and out-of-distribution queries. We create specific comparison datasets for RMs that have subtle, but verifiable reasons (e.g. bugs, incorrect facts) why one answer should be preferred to another. On the RewardBench leaderboard, we evaluate reward models trained with a variety of methods, such as the direct MLE training of classifiers and the implicit reward modeling of Direct Preference Optimization (DPO). We present many findings on propensity for refusals, reasoning limitations, and instruction following shortcomings of various reward models towards a better understanding of the RLHF process.

## 03-021 | Tulu 3: Pushing Frontiers in Open Language Model Post-Training
- arXiv: 2411.15124  first public: 2024-11-22  latest: 2025-04-14  primary cat: cs.CL
- authors (23): Nathan Lambert; Jacob Morrison; Valentina Pyatkin; Shengyi Huang; Hamish Ivison; Faeze Brahman ...
- seed subtopic: 指令微调; type: 技术报告; cross: ['04']
- arXiv comment: Added Tulu 3 405B results and additional analyses
- pages: 82

ABSTRACT: Language model post-training is applied to refine behaviors and unlock new skills across a wide range of recent language models, but open recipes for applying these techniques lag behind proprietary ones. The underlying training data and recipes for post-training are simultaneously the most important pieces of the puzzle and the portion with the least transparency. To bridge this gap, we introduce Tulu 3, a family of fully-open state-of-the-art post-trained models, alongside its data, code, and training recipes, serving as a comprehensive guide for modern post-training techniques. Tulu 3, which builds on Llama 3.1 base models, achieves results surpassing the instruct versions of Llama 3.1, Qwen 2.5, Mistral, and even closed models such as GPT-4o-mini and Claude 3.5-Haiku. The training algorithms for our models include supervised finetuning (SFT), Direct Preference Optimization (DPO), and a novel method we call Reinforcement Learning with Verifiable Rewards (RLVR). With Tulu 3, we introduce a multi-task evaluation scheme for post-training recipes with development and unseen evaluations, standard benchmark implementations, and substantial decontamination of existing open datasets on said benchmarks. We conclude with analysis and discussion of training methods that did not reliably improve performance. In addition to the Tulu 3 model weights and demo, we release the complete recipe -- including datasets for diverse core skills, a robust toolkit for data curation and evaluation, the training code and infrastructure, and, most importantly, a detailed report for reproducing and further adapting the Tulu 3 approach to more domains.

## 03-022 | PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models
- arXiv: 2404.02948  first public: 2024-04-03  latest: 2025-04-09  primary cat: cs.LG
- authors (3): Fanxu Meng; Zhaohui Wang; Muhan Zhang
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024 spotlight
- URLs on first pages of PDF: https://github.com/GraphPKU/PiSSA
- pages: 34

ABSTRACT: To parameter-efficiently fine-tune (PEFT) large language models (LLMs), the low-rank adaptation (LoRA) method approximates the model changes $ΔW \in \mathbb{R}^{m \times n}$ through the product of two matrices $A \in \mathbb{R}^{m \times r}$ and $B \in \mathbb{R}^{r \times n}$, where $r \ll \min(m, n)$, $A$ is initialized with Gaussian noise, and $B$ with zeros. LoRA freezes the original model $W$ and updates the "Noise & Zero" adapter, which may lead to slow convergence. To overcome this limitation, we introduce Principal Singular values and Singular vectors Adaptation (PiSSA). PiSSA shares the same architecture as LoRA, but initializes the adaptor matrices $A$ and $B$ with the principal components of the original matrix $W$, and put the remaining components into a residual matrix $W^{res} \in \mathbb{R}^{m \times n}$ which is frozen during fine-tuning. Compared to LoRA, PiSSA updates the principal components while freezing the "residual" parts, allowing faster convergence and enhanced performance. Comparative experiments of PiSSA and LoRA across 12 different models, ranging from 184M to 70B, encompassing 5 NLG and 8 NLU tasks, reveal that PiSSA consistently outperforms LoRA under identical experimental setups. On the GSM8K benchmark, Mistral-7B fine-tuned with PiSSA achieves an accuracy of 72.86%, surpassing LoRA's 67.7% by 5.16%. Due to the same architecture, PiSSA is also compatible with quantization to further reduce the memory requirement of fine-tuning. Compared to QLoRA, QPiSSA exhibits smaller quantization errors in the initial stages. Fine-tuning LLaMA-3-70B on GSM8K, QPiSSA attains an accuracy of 86.05%, exceeding the performances of QLoRA at 81.73%. Leveraging a fast SVD technique, PiSSA can be initialized in only a few seconds, presenting a negligible cost for transitioning from LoRA to PiSSA. Code is available at https://github.com/GraphPKU/PiSSA.

## 03-023 | Nash Learning from Human Feedback
- arXiv: 2312.00886  first public: 2023-12-01  latest: 2024-06-11  primary cat: stat.ML
- authors (17): Rémi Munos; Michal Valko; Daniele Calandriello; Mohammad Gheshlaghi Azar; Mark Rowland; Zhaohan Daniel Guo ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- pages: 26

ABSTRACT: Reinforcement learning from human feedback (RLHF) has emerged as the main paradigm for aligning large language models (LLMs) with human preferences. Typically, RLHF involves the initial step of learning a reward model from human feedback, often expressed as preferences between pairs of text generations produced by a pre-trained LLM. Subsequently, the LLM's policy is fine-tuned by optimizing it to maximize the reward model through a reinforcement learning algorithm. However, an inherent limitation of current reward models is their inability to fully represent the richness of human preferences and their dependency on the sampling distribution. In this study, we introduce an alternative pipeline for the fine-tuning of LLMs using pairwise human feedback. Our approach entails the initial learning of a preference model, which is conditioned on two inputs given a prompt, followed by the pursuit of a policy that consistently generates responses preferred over those generated by any competing policy, thus defining the Nash equilibrium of this preference model. We term this approach Nash learning from human feedback (NLHF). In the context of a tabular policy representation, we present a novel algorithmic solution, Nash-MD, founded on the principles of mirror descent. This algorithm produces a sequence of policies, with the last iteration converging to the regularized Nash equilibrium. Additionally, we explore parametric representations of policies and introduce gradient descent algorithms for deep-learning architectures. To demonstrate the effectiveness of our approach, we present experimental results involving the fine-tuning of a LLM for a text summarization task. We believe NLHF offers a compelling avenue for preference learning and policy optimization with the potential of advancing the field of aligning LLMs with human preferences.

## 03-024 | Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy
- arXiv: 2507.01352  first public: 2025-07-02  latest: 2026-03-02  primary cat: cs.CL
- authors (12): Chris Yuhao Liu; Liang Zeng; Yuzhen Xiao; Jujie He; Jiacai Liu; Chaojie Wang ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: ICLR 2026 Poster
- URLs on first pages of PDF: https://github.com/Skywork/Skywork-Reward-V2 https://huggingface.co/Skywork
- pages: 33

ABSTRACT: Despite the critical role of reward models (RMs) in Reinforcement Learning from Human Feedback (RLHF), current state-of-the-art open RMs perform poorly on most existing evaluation benchmarks, failing to capture nuanced human preferences. We hypothesize that this brittleness stems primarily from limitations in preference datasets, which are often narrowly scoped, synthetically labeled, or lack rigorous quality control. To address these challenges, we present SynPref-40M, a large-scale preference dataset comprising 40 million preference pairs. To enable data curation at scale, we design a human-AI synergistic two-stage pipeline that leverages the complementary strengths of human annotation quality and AI scalability. In this pipeline, humans provide verified annotations, while LLMs perform automatic curation based on human guidance. Training on this preference mixture, we introduce Skywork-Reward-V2, a suite of eight reward models ranging from 0.6B to 8B parameters, trained on a carefully curated subset of 26 million preference pairs from SynPref-40M. We demonstrate that Skywork-Reward-V2 is versatile across a wide range of capabilities, including alignment with human preferences, objective correctness, safety, resistance to stylistic biases, and best-of-N scaling. These reward models achieve state-of-the-art performance across seven major reward model benchmarks, outperform generative reward models, and demonstrate strong downstream performance. Ablation studies confirm that effectiveness stems not only from data scale but also from high-quality curation. The Skywork-Reward-V2 series represents substantial progress in open reward models, demonstrating how human-AI curation synergy can unlock significantly higher data quality.

## 03-025 | Scaling Synthetic Data Creation with 1,000,000,000 Personas
- arXiv: 2406.20094  first public: 2024-06-28  latest: 2025-05-08  primary cat: cs.CL
- authors (6): Tao Ge; Xin Chan; Xiaoyang Wang; Dian Yu; Haitao Mi; Dong Yu
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: Work in progress
- URLs on first pages of PDF: https://github.com/tencent-ailab/persona-hub
- pages: 20

ABSTRACT: We propose a novel persona-driven data synthesis methodology that leverages various perspectives within a large language model (LLM) to create diverse synthetic data. To fully exploit this methodology at scale, we introduce Persona Hub -- a collection of 1 billion diverse personas automatically curated from web data. These 1 billion personas (~13% of the world's total population), acting as distributed carriers of world knowledge, can tap into almost every perspective encapsulated within the LLM, thereby facilitating the creation of diverse synthetic data at scale for various scenarios. By showcasing Persona Hub's use cases in synthesizing high-quality mathematical and logical reasoning problems, instructions (i.e., user prompts), knowledge-rich texts, game NPCs and tools (functions) at scale, we demonstrate persona-driven data synthesis is versatile, scalable, flexible, and easy to use, potentially driving a paradigm shift in synthetic data creation and applications in practice, which may have a profound impact on LLM research and development.

## 03-026 | LoRA Learns Less and Forgets Less
- arXiv: 2405.09673  first public: 2024-05-15  latest: 2024-09-20  primary cat: cs.LG
- authors (12): Dan Biderman; Jacob Portes; Jose Javier Gonzalez Ortiz; Mansheej Paul; Philip Greengard; Connor Jennings ...
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: Final version with new experiments and analyses, as accepted to Transactions on Machine Learning Research, August 2024 (Featured Certification). https://openreview.net/forum?id=aloEru2qCG&noteId=Jb3PQNQDI2
- URLs on first pages of PDF: https://github.com/danbider/lora-tradeoffs https://github.com/mosaicml/composer https://github.com/mosaicml/llm-foundry https://github.com/mosaicml/streaming https://huggingface.co/datasets/open-web-math/open-web-math
- pages: 39

ABSTRACT: Low-Rank Adaptation (LoRA) is a widely-used parameter-efficient finetuning method for large language models. LoRA saves memory by training only low rank perturbations to selected weight matrices. In this work, we compare the performance of LoRA and full finetuning on two target domains, programming and mathematics. We consider both the instruction finetuning (approximately 100K prompt-response pairs) and continued pretraining (20B unstructured tokens) data regimes. Our results show that, in the standard low-rank settings, LoRA substantially underperforms full finetuning. Nevertheless, LoRA better maintains the base model's performance on tasks outside the target domain. We show that LoRA mitigates forgetting more than common regularization techniques such as weight decay and dropout; it also helps maintain more diverse generations. Finally, we show that full finetuning learns perturbations with a rank that is 10-100X greater than typical LoRA configurations, possibly explaining some of the reported gaps. We conclude by proposing best practices for finetuning with LoRA.

## 03-027 | Direct Nash Optimization: Teaching Language Models to Self-Improve with General Preferences
- arXiv: 2404.03715  first public: 2024-04-04  latest: 2024-04-04  primary cat: cs.LG
- authors (6): Corby Rosset; Ching-An Cheng; Arindam Mitra; Michael Santacroce; Ahmed Awadallah; Tengyang Xie
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- pages: 36

ABSTRACT: This paper studies post-training large language models (LLMs) using preference feedback from a powerful oracle to help a model iteratively improve over itself. The typical approach for post-training LLMs involves Reinforcement Learning from Human Feedback (RLHF), which traditionally separates reward learning and subsequent policy optimization. However, such a reward maximization approach is limited by the nature of "point-wise" rewards (such as Bradley-Terry model), which fails to express complex intransitive or cyclic preference relations. While advances on RLHF show reward learning and policy optimization can be merged into a single contrastive objective for stability, they yet still remain tethered to the reward maximization framework. Recently, a new wave of research sidesteps the reward maximization presumptions in favor of directly optimizing over "pair-wise" or general preferences. In this paper, we introduce Direct Nash Optimization (DNO), a provable and scalable algorithm that marries the simplicity and stability of contrastive learning with theoretical generality from optimizing general preferences. Because DNO is a batched on-policy algorithm using a regression-based objective, its implementation is straightforward and efficient. Moreover, DNO enjoys monotonic improvement across iterations that help it improve even over a strong teacher (such as GPT-4). In our experiments, a resulting 7B parameter Orca-2.5 model aligned by DNO achieves the state-of-the-art win-rate against GPT-4-Turbo of 33% on AlpacaEval 2.0 (even after controlling for response length), an absolute gain of 26% (7% to 33%) over the initializing model. It outperforms models with far more parameters, including Mistral Large, Self-Rewarding LM (70B parameters), and older versions of GPT-4.

## 03-028 | HelpSteer2: Open-source dataset for training top-performing reward models
- arXiv: 2406.08673  first public: 2024-06-12  latest: 2024-06-12  primary cat: cs.CL
- authors (9): Zhilin Wang; Yi Dong; Olivier Delalleau; Jiaqi Zeng; Gerald Shen; Daniel Egert ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/NVIDIA/NeMo-Aligner https://huggingface.co/datasets/nvidia/HelpSteer2
- pages: 27

ABSTRACT: High-quality preference datasets are essential for training reward models that can effectively guide large language models (LLMs) in generating high-quality responses aligned with human preferences. As LLMs become stronger and better aligned, permissively licensed preference datasets, such as Open Assistant, HH-RLHF, and HelpSteer need to be updated to remain effective for reward modeling. Methods that distil preference data from proprietary LLMs such as GPT-4 have restrictions on commercial usage imposed by model providers. To improve upon both generated responses and attribute labeling quality, we release HelpSteer2, a permissively licensed preference dataset (CC-BY-4.0). Using a powerful internal base model trained on HelpSteer2, we are able to achieve the SOTA score (92.0%) on Reward-Bench's primary dataset, outperforming currently listed open and proprietary models, as of June 12th, 2024. Notably, HelpSteer2 consists of only ten thousand response pairs, an order of magnitude fewer than existing preference datasets (e.g., HH-RLHF), which makes it highly efficient for training reward models. Our extensive experiments demonstrate that reward models trained with HelpSteer2 are effective in aligning LLMs. In particular, we propose SteerLM 2.0, a model alignment approach that can effectively make use of the rich multi-attribute score predicted by our reward models. HelpSteer2 is available at https://huggingface.co/datasets/nvidia/HelpSteer2 and code is available at https://github.com/NVIDIA/NeMo-Aligner

## 03-029 | Learning Dynamics of LLM Finetuning
- arXiv: 2407.10490  first public: 2024-07-15  latest: 2025-06-29  primary cat: cs.LG
- authors (2): Yi Ren; Danica J. Sutherland
- seed subtopic: 指令微调; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/Joshua-Ren/Learning_dynamics_LLM
- pages: 41

ABSTRACT: Learning dynamics, which describes how the learning of specific training examples influences the model's predictions on other examples, gives us a powerful tool for understanding the behavior of deep learning systems. We study the learning dynamics of large language models during different types of finetuning, by analyzing the step-wise decomposition of how influence accumulates among different potential responses. Our framework allows a uniform interpretation of many interesting observations about the training of popular algorithms for both instruction tuning and preference tuning. In particular, we propose a hypothetical explanation of why specific types of hallucination are strengthened after finetuning, e.g., the model might use phrases or facts in the response for question B to answer question A, or the model might keep repeating similar simple phrases when generating responses. We also extend our framework and highlight a unique "squeezing effect" to explain a previously observed phenomenon in off-policy direct preference optimization (DPO), where running DPO for too long makes even the desired outputs less likely. This framework also provides insights into where the benefits of on-policy DPO and other variants come from. The analysis not only provides a novel perspective of understanding LLM's finetuning but also inspires a simple, effective method to improve alignment performance.

## 03-030 | ReFT: Representation Finetuning for Language Models
- arXiv: 2404.03592  first public: 2024-04-04  latest: 2024-05-22  primary cat: cs.CL
- authors (7): Zhengxuan Wu; Aryaman Arora; Zheng Wang; Atticus Geiger; Dan Jurafsky; Christopher D. Manning ...
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: preprint
- URLs on first pages of PDF: https://github.com/stanfordnlp/pyreft
- pages: 49

ABSTRACT: Parameter-efficient finetuning (PEFT) methods seek to adapt large neural models via updates to a small number of weights. However, much prior interpretability work has shown that representations encode rich semantic information, suggesting that editing representations might be a more powerful alternative. We pursue this hypothesis by developing a family of Representation Finetuning (ReFT) methods. ReFT methods operate on a frozen base model and learn task-specific interventions on hidden representations. We define a strong instance of the ReFT family, Low-rank Linear Subspace ReFT (LoReFT), and we identify an ablation of this method that trades some performance for increased efficiency. Both are drop-in replacements for existing PEFTs and learn interventions that are 15x--65x more parameter-efficient than LoRA. We showcase LoReFT on eight commonsense reasoning tasks, four arithmetic reasoning tasks, instruction-tuning, and GLUE. In all these evaluations, our ReFTs deliver the best balance of efficiency and performance, and almost always outperform state-of-the-art PEFTs. We release a generic ReFT training library publicly at https://github.com/stanfordnlp/pyreft.

## 03-031 | Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs
- arXiv: 2402.14740  first public: 2024-02-22  latest: 2024-02-26  primary cat: cs.LG
- authors (8): Arash Ahmadian; Chris Cremer; Matthias Gallé; Marzieh Fadaee; Julia Kreutzer; Olivier Pietquin ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: 27 pages, 7 figures, 2 tables
- pages: 28

ABSTRACT: AI alignment in the shape of Reinforcement Learning from Human Feedback (RLHF) is increasingly treated as a crucial ingredient for high performance large language models. Proximal Policy Optimization (PPO) has been positioned by recent literature as the canonical method for the RL part of RLHF. However, it involves both high computational cost and sensitive hyperparameter tuning. We posit that most of the motivational principles that led to the development of PPO are less of a practical concern in RLHF and advocate for a less computationally expensive method that preserves and even increases performance. We revisit the formulation of alignment from human preferences in the context of RL. Keeping simplicity as a guiding principle, we show that many components of PPO are unnecessary in an RLHF context and that far simpler REINFORCE-style optimization variants outperform both PPO and newly proposed "RL-free" methods such as DPO and RAFT. Our work suggests that careful adaptation to LLMs alignment characteristics enables benefiting from online RL optimization at low cost.

## 03-032 | Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts
- arXiv: 2406.12845  first public: 2024-06-18  latest: 2024-06-18  primary cat: cs.LG
- authors (5): Haoxiang Wang; Wei Xiong; Tengyang Xie; Han Zhao; Tong Zhang
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: Technical report v1. Code and model are released at https://github.com/RLHFlow/RLHF-Reward-Modeling/
- URLs on first pages of PDF: https://github.com/RLHFlow/RLHF-Rewar
- pages: 14

ABSTRACT: Reinforcement learning from human feedback (RLHF) has emerged as the primary method for aligning large language models (LLMs) with human preferences. The RLHF process typically starts by training a reward model (RM) using human preference data. Conventional RMs are trained on pairwise responses to the same user request, with relative ratings indicating which response humans prefer. The trained RM serves as a proxy for human preferences. However, due to the black-box nature of RMs, their outputs lack interpretability, as humans cannot intuitively understand why an RM thinks a response is good or not. As RMs act as human preference proxies, we believe they should be human-interpretable to ensure that their internal decision processes are consistent with human preferences and to prevent reward hacking in LLM alignment. To build RMs with interpretable preferences, we propose a two-stage approach: i) train an Absolute-Rating Multi-Objective Reward Model (ArmoRM) with multi-dimensional absolute-rating data, each dimension corresponding to a human-interpretable objective (e.g., honesty, verbosity, safety); ii) employ a Mixture-of-Experts (MoE) strategy with a gating network that automatically selects the most suitable reward objectives based on the context. We efficiently trained an ArmoRM with Llama-3 8B and a gating network consisting of a shallow MLP on top of the ArmoRM. Our trained model, ArmoRM-Llama3-8B, obtains state-of-the-art performance on RewardBench, a benchmark evaluating RMs for language modeling. Notably, the performance of our model surpasses the LLM-as-a-judge method with GPT-4 judges by a margin, and approaches the performance of the much larger Nemotron-4 340B reward model.

## 03-033 | SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training
- arXiv: 2501.17161  first public: 2025-01-28  latest: 2025-05-26  primary cat: cs.AI
- authors (9): Tianzhe Chu; Yuexiang Zhai; Jihan Yang; Shengbang Tong; Saining Xie; Dale Schuurmans ...
- seed subtopic: 指令微调; type: 原始研究; cross: ['04']
- arXiv comment: Website at https://tianzhechu.com/SFTvsRL
- pages: 21

ABSTRACT: Supervised fine-tuning (SFT) and reinforcement learning (RL) are widely used post-training techniques for foundation models. However, their roles in enhancing model generalization capabilities remain unclear. This paper studies the difference between SFT and RL on generalization and memorization, focusing on text-based rule variants and visual variants. We introduce GeneralPoints, an arithmetic reasoning card game, and adopt V-IRL, a real-world navigation environment, to assess how models trained with SFT and RL generalize to unseen variants in both textual and visual domains. We show that RL, especially when trained with an outcome-based reward, generalizes across both rule-based textual and visual variants. SFT, in contrast, tends to memorize training data and struggles to generalize out-of-distribution scenarios. Further analysis reveals that RL improves the model's underlying visual recognition capabilities, contributing to its enhanced generalization in the visual domain. Despite RL's superior generalization, we show that SFT remains essential for effective RL training; SFT stabilizes the model's output format, enabling subsequent RL to achieve its performance gains. These findings demonstrates the capability of RL for acquiring generalizable knowledge in complex, multi-modal tasks.

## 03-034 | Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey
- arXiv: 2403.14608  first public: 2024-03-21  latest: 2024-09-16  primary cat: cs.LG
- authors (5): Zeyu Han; Chao Gao; Jinyang Liu; Jeff Zhang; Sai Qian Zhang
- seed subtopic: 参数高效微调; type: 综述; cross: []
- arXiv comment: 25 pages, 12 figures. Due to word limit, the abstract here is truncated. The full abstract is available in the PDF
- pages: 25

ABSTRACT: Large models represent a groundbreaking advancement in multiple application fields, enabling remarkable achievements across various tasks. However, their unprecedented scale comes with significant computational costs. These models, often consisting of billions of parameters, require vast amounts of computational resources for execution. Especially, the expansive scale and computational demands pose considerable challenges when customizing them for particular downstream tasks, particularly over the hardware platforms constrained by computational capabilities. Parameter Efficient Fine-Tuning (PEFT) provides a practical solution by efficiently adjusting the large models over the various downstream tasks. In particular, PEFT refers to the process of adjusting the parameters of a pre-trained large model to adapt it to a specific task or domain while minimizing the number of additional parameters introduced or computational resources required. This approach is particularly important when dealing with large-scale language models with high parameter counts, as fine-tuning these models from scratch can be computationally expensive and resource-intensive, posing considerable challenges in the supporting system platform design. In this survey, we present comprehensive studies of various PEFT algorithms, examining their performance and computational overhead. Moreover, we provide an overview of applications developed using different PEFT algorithms and discuss common techniques employed to mitigate computation costs for PEFT. In addition to providing an extensive survey from an algorithmic standpoint, we also examine various real-world system designs to investigate the implementation costs associated with different PEFT approaches. This survey serves as a valuable resource for researchers aiming to understand both the PEFT algorithm and its system implementation, offering detailed ......

## 03-035 | Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study
- arXiv: 2404.10719  first public: 2024-04-16  latest: 2024-10-10  primary cat: cs.CL
- authors (9): Shusheng Xu; Wei Fu; Jiaxuan Gao; Wenjie Ye; Weilin Liu; Zhiyu Mei ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: 16 pages, 2 figures, 14 tables
- journal_ref: ICML 2024
- pages: 16

ABSTRACT: Reinforcement Learning from Human Feedback (RLHF) is currently the most widely used method to align large language models (LLMs) with human preferences. Existing RLHF methods can be roughly categorized as either reward-based or reward-free. Novel applications such as ChatGPT and Claude leverage reward-based methods that first learn a reward model and apply actor-critic algorithms, such as Proximal Policy Optimization (PPO). However, in academic benchmarks, state-of-the-art results are often achieved via reward-free methods, such as Direct Preference Optimization (DPO). Is DPO truly superior to PPO? Why does PPO perform poorly on these benchmarks? In this paper, we first conduct both theoretical and empirical studies on the algorithmic properties of DPO and show that DPO may have fundamental limitations. Moreover, we also comprehensively examine PPO and reveal the key factors for the best performances of PPO in fine-tuning LLMs. Finally, we benchmark DPO and PPO across a collection of RLHF testbeds, ranging from dialogue to code generation. Experiment results demonstrate that PPO is able to surpass other alignment methods in all cases and achieve state-of-the-art results in challenging code competitions. Our code is publicly available at https://github.com/openpsi-project/ReaLHF.

## 03-036 | WARM: On the Benefits of Weight Averaged Reward Models
- arXiv: 2401.12187  first public: 2024-01-22  latest: 2024-01-22  primary cat: cs.LG
- authors (7): Alexandre Ramé; Nino Vieillard; Léonard Hussenot; Robert Dadashi; Geoffrey Cideron; Olivier Bachem ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: 14 pages, 9 figures
- pages: 33

ABSTRACT: Aligning large language models (LLMs) with human preferences through reinforcement learning (RLHF) can lead to reward hacking, where LLMs exploit failures in the reward model (RM) to achieve seemingly high rewards without meeting the underlying objectives. We identify two primary challenges when designing RMs to mitigate reward hacking: distribution shifts during the RL process and inconsistencies in human preferences. As a solution, we propose Weight Averaged Reward Models (WARM), first fine-tuning multiple RMs, then averaging them in the weight space. This strategy follows the observation that fine-tuned weights remain linearly mode connected when sharing the same pre-training. By averaging weights, WARM improves efficiency compared to the traditional ensembling of predictions, while improving reliability under distribution shifts and robustness to preference inconsistencies. Our experiments on summarization tasks, using best-of-N and RL methods, shows that WARM improves the overall quality and alignment of LLM predictions; for example, a policy RL fine-tuned with WARM has a 79.4% win rate against a policy RL fine-tuned with a single RM.

## 03-037 | On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification
- arXiv: 2508.05629  first public: 2025-08-07  latest: 2026-02-27  primary cat: cs.LG
- authors (10): Yongliang Wu; Yizhou Zhou; Zhou Ziheng; Yingzhe Peng; Xinyu Ye; Xinting Hu ...
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: ICLR 2026
- pages: 22

ABSTRACT: In this work, we present a simple yet theoretically motivated improvement to Supervised Fine-Tuning (SFT) for the Large Language Model (LLM), addressing its limited generalization compared to reinforcement learning (RL). Through mathematical analysis, we reveal that standard SFT gradients implicitly encode a problematic reward structure that may severely restrict the generalization capabilities of model compared to RL. To rectify this, we propose Dynamic Fine-Tuning (\model), stabilizing gradient updates for each token by dynamically rescaling the objective function with the probability of this token. With just a single-line change, the method outperforms standard SFT on multiple difficult benchmarks and base models, from math reasoning to code generation and multi-modal tasks, demonstrating improved generalization. Additionally, \model~achieves competitive results in offline RL settings, providing an effective yet streamlined alternative. By bridging theoretical insights with practical solutions, this work advances the state of SFT. The source code will be available at https://github.com/yongliang-wu/DFT.

## 03-038 | LoRA vs Full Fine-tuning: An Illusion of Equivalence
- arXiv: 2410.21228  first public: 2024-10-28  latest: 2025-10-22  primary cat: cs.LG
- authors (4): Reece Shuttleworth; Jacob Andreas; Antonio Torralba; Pratyusha Sharma
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- pages: 29

ABSTRACT: Fine-tuning is a crucial paradigm for adapting pre-trained large language models to downstream tasks. Recently, methods like Low-Rank Adaptation (LoRA) have been shown to effectively fine-tune LLMs with an extreme reduction in trainable parameters. But, \emph{are their learned solutions really equivalent?} We study how LoRA and full-finetuning change pre-trained models by analyzing the model's weight matrices through the lens of their spectral properties. We find that LoRA and full fine-tuning yield weight matrices whose singular value decompositions exhibit very different structure: weight matrices trained with LoRA have new, high-ranking singular vectors, which we call \emph{intruder dimensions}, while those trained with full fine-tuning do not. Further, we extend the finding that LoRA forgets less than full fine-tuning and find its forgetting is vastly localized to the intruder dimension -- by causally intervening on the intruder dimensions by changing their associated singular values post-fine-tuning, we show that they cause forgetting. Moreover, scaling them down significantly improves modeling of the pre-training distribution with a minimal drop in downstream task performance. Given this, we should expect accumulating intruder dimensions to be harmful and lead to more forgetting. This will be amplified during continual learning because of sequentially fine-tuning, and we show that LoRA models do accumulate intruder dimensions here tend to perform worse in this setting, emphasizing the practicality of our findings.

## 03-039 | Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data
- arXiv: 2404.14367  first public: 2024-04-22  latest: 2024-06-02  primary cat: cs.LG
- authors (9): Fahim Tajwar; Anikait Singh; Archit Sharma; Rafael Rafailov; Jeff Schneider; Tengyang Xie ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: International Conference on Machine Learning (ICML), 2024
- pages: 41

ABSTRACT: Learning from preference labels plays a crucial role in fine-tuning large language models. There are several distinct approaches for preference fine-tuning, including supervised learning, on-policy reinforcement learning (RL), and contrastive learning. Different methods come with different implementation tradeoffs and performance differences, and existing empirical findings present different conclusions, for instance, some results show that online RL is quite important to attain good fine-tuning results, while others find (offline) contrastive or even purely supervised methods sufficient. This raises a natural question: what kind of approaches are important for fine-tuning with preference data and why? In this paper, we answer this question by performing a rigorous analysis of a number of fine-tuning techniques on didactic and full-scale LLM problems. Our main finding is that, in general, approaches that use on-policy sampling or attempt to push down the likelihood on certain responses (i.e., employ a "negative gradient") outperform offline and maximum likelihood objectives. We conceptualize our insights and unify methods that use on-policy sampling or negative gradient under a notion of mode-seeking objectives for categorical distributions. Mode-seeking objectives are able to alter probability mass on specific bins of a categorical distribution at a fast rate compared to maximum likelihood, allowing them to relocate masses across bins more effectively. Our analysis prescribes actionable insights for preference fine-tuning of LLMs and informs how data should be collected for maximal improvement.

## 03-040 | The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models
- arXiv: 2404.16019  first public: 2024-04-24  latest: 2024-12-03  primary cat: cs.CL
- authors (12): Hannah Rose Kirk; Alexander Whitefield; Paul Röttger; Andrew Bean; Katerina Margatina; Juan Ciro ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- journal_ref: The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track (2024)
- pages: 107

ABSTRACT: Human feedback is central to the alignment of Large Language Models (LLMs). However, open questions remain about methods (how), domains (where), people (who) and objectives (to what end) of feedback processes. To navigate these questions, we introduce PRISM, a dataset that maps the sociodemographics and stated preferences of 1,500 diverse participants from 75 countries, to their contextual preferences and fine-grained feedback in 8,011 live conversations with 21 LLMs. With PRISM, we contribute (i) wider geographic and demographic participation in feedback; (ii) census-representative samples for two countries (UK, US); and (iii) individualised ratings that link to detailed participant profiles, permitting personalisation and attribution of sample artefacts. We target subjective and multicultural perspectives on value-laden and controversial issues, where we expect interpersonal and cross-cultural disagreement. We use PRISM in three case studies to demonstrate the need for careful consideration of which humans provide what alignment data.

## 03-041 | Instruction-Following Evaluation for Large Language Models
- arXiv: 2311.07911  first public: 2023-11-14  latest: 2023-11-14  primary cat: cs.CL
- authors (8): Jeffrey Zhou; Tianjian Lu; Swaroop Mishra; Siddhartha Brahma; Sujoy Basu; Yi Luan ...
- seed subtopic: 指令微调; type: 原始研究; cross: ['12']
- URLs on first pages of PDF: https://github.com/google-research/ https://github.com/google-research/google-research/tree/master/
- pages: 43

ABSTRACT: One core capability of Large Language Models (LLMs) is to follow natural language instructions. However, the evaluation of such abilities is not standardized: Human evaluations are expensive, slow, and not objectively reproducible, while LLM-based auto-evaluation is potentially biased or limited by the ability of the evaluator LLM. To overcome these issues, we introduce Instruction-Following Eval (IFEval) for large language models. IFEval is a straightforward and easy-to-reproduce evaluation benchmark. It focuses on a set of "verifiable instructions" such as "write in more than 400 words" and "mention the keyword of AI at least 3 times". We identified 25 types of those verifiable instructions and constructed around 500 prompts, with each prompt containing one or more verifiable instructions. We show evaluation results of two widely available LLMs on the market. Our code and data can be found at https://github.com/google-research/google-research/tree/master/instruction_following_eval

## 03-042 | Text-to-LoRA: Instant Transformer Adaption
- arXiv: 2506.06105  first public: 2025-06-06  latest: 2025-06-09  primary cat: cs.LG
- authors (4): Rujikorn Charakorn; Edoardo Cetin; Yujin Tang; Robert Tjarko Lange
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2025
- URLs on first pages of PDF: https://github.com/SakanaAI/
- pages: 30

ABSTRACT: While Foundation Models provide a general tool for rapid content creation, they regularly require task-specific adaptation. Traditionally, this exercise involves careful curation of datasets and repeated fine-tuning of the underlying model. Fine-tuning techniques enable practitioners to adapt foundation models for many new applications but require expensive and lengthy training while being notably sensitive to hyperparameter choices. To overcome these limitations, we introduce Text-to-LoRA (T2L), a model capable of adapting large language models (LLMs) on the fly solely based on a natural language description of the target task. T2L is a hypernetwork trained to construct LoRAs in a single inexpensive forward pass. After training T2L on a suite of 9 pre-trained LoRA adapters (GSM8K, Arc, etc.), we show that the ad-hoc reconstructed LoRA instances match the performance of task-specific adapters across the corresponding test sets. Furthermore, T2L can compress hundreds of LoRA instances and zero-shot generalize to entirely unseen tasks. This approach provides a significant step towards democratizing the specialization of foundation models and enables language-based adaptation with minimal compute requirements. Our code is available at https://github.com/SakanaAI/text-to-lora

## 03-043 | From $r$ to $Q^*$: Your Language Model is Secretly a Q-Function
- arXiv: 2404.12358  first public: 2024-04-18  latest: 2024-08-12  primary cat: cs.LG
- authors (4): Rafael Rafailov; Joey Hejna; Ryan Park; Chelsea Finn
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: COLM 2024
- pages: 32

ABSTRACT: Reinforcement Learning From Human Feedback (RLHF) has been critical to the success of the latest generation of generative AI models. In response to the complex nature of the classical RLHF pipeline, direct alignment algorithms such as Direct Preference Optimization (DPO) have emerged as an alternative approach. Although DPO solves the same objective as the standard RLHF setup, there is a mismatch between the two approaches. Standard RLHF deploys reinforcement learning in a specific token-level MDP, while DPO is derived as a bandit problem in which the whole response of the model is treated as a single arm. In this work we rectify this difference. We theoretically show that we can derive DPO in the token-level MDP as a general inverse Q-learning algorithm, which satisfies the Bellman equation. Using our theoretical results, we provide three concrete empirical insights. First, we show that because of its token level interpretation, DPO is able to perform some type of credit assignment. Next, we prove that under the token level formulation, classical search-based algorithms, such as MCTS, which have recently been applied to the language generation space, are equivalent to likelihood-based search on a DPO policy. Empirically we show that a simple beam search yields meaningful improvement over the base DPO policy. Finally, we show how the choice of reference policy causes implicit rewards to decline during training. We conclude by discussing applications of our work, including information elicitation in multi-turn dialogue, reasoning, agentic applications and end-to-end training of multi-model systems.

## 03-044 | Inference-Time Scaling for Generalist Reward Modeling
- arXiv: 2504.02495  first public: 2025-04-03  latest: 2025-09-25  primary cat: cs.CL
- authors (8): Zijun Liu; Peiyi Wang; Runxin Xu; Shirong Ma; Chong Ruan; Peng Li ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: ['04']
- arXiv comment: Preprint, under review. 44 pages. Models are available at https://huggingface.co/collections/BBQGOD/deepseek-grm-68b4681169dbb97fd30614b5 and https://www.modelscope.cn/collections/DeepSeek-GRM-ff6a2d8babdd4a
- pages: 44

ABSTRACT: Reinforcement learning (RL) has been widely adopted in post-training for large language models (LLMs) at scale. Recently, the incentivization of reasoning capabilities in LLMs from RL indicates that $\textit{proper learning methods could enable effective inference-time scalability}$. A key challenge of RL is to obtain accurate reward signals for LLMs in various domains beyond verifiable questions or artificial rules. In this work, we investigate how to improve reward modeling (RM) with more inference compute for general queries, i.e. the $\textbf{inference-time scalability of generalist RM}$, and further, how to improve the effectiveness of performance-compute scaling with proper learning methods. For the RM approach, we adopt pointwise generative reward modeling (GRM) to enable flexibility for different input types and potential for inference-time scaling. For the learning method, we propose Self-Principled Critique Tuning (SPCT) to foster scalable reward generation behaviors in GRMs through online RL, to generate principles adaptively and critiques accurately, resulting in $\textbf{DeepSeek-GRM}$ models. Furthermore, for effective inference-time scaling, we use parallel sampling to expand compute usage, and introduce a meta RM to guide voting process for better scaling performance. Empirically, we show that SPCT significantly improves the quality and scalability of GRMs, outperforming existing methods and models in various RM benchmarks without severe biases, and could achieve better performance compared to training-time scaling. DeepSeek-GRM still meets challenges in some tasks, which we believe can be addressed by future efforts in generalist reward systems. The models are released at Hugging Face and ModelScope.

## 03-045 | Generalizing Verifiable Instruction Following
- arXiv: 2507.02833  first public: 2025-07-03  latest: 2025-11-11  primary cat: cs.CL
- authors (8): Valentina Pyatkin; Saumya Malik; Victoria Graf; Hamish Ivison; Shengyi Huang; Pradeep Dasigi ...
- seed subtopic: 指令微调; type: 原始研究; cross: []
- arXiv comment: 11 pages, accepted to NeurIPS 2025, Datasets & Benchmarks
- URLs on first pages of PDF: https://github.com/allenai/IFBench
- pages: 21

ABSTRACT: A crucial factor for successful human and AI interaction is the ability of language models or chatbots to follow human instructions precisely. A common feature of instructions are output constraints like ``only answer with yes or no" or ``mention the word `abrakadabra' at least 3 times" that the user adds to craft a more useful answer. Even today's strongest models struggle with fulfilling such constraints. We find that most models strongly overfit on a small set of verifiable constraints from the benchmarks that test these abilities, a skill called precise instruction following, and are not able to generalize well to unseen output constraints. We introduce a new benchmark, IFBench, to evaluate precise instruction following generalization on 58 new, diverse, and challenging verifiable out-of-domain constraints. In addition, we perform an extensive analysis of how and on what data models can be trained to improve precise instruction following generalization. Specifically, we carefully design constraint verification modules and show that reinforcement learning with verifiable rewards (RLVR) significantly improves instruction following. In addition to IFBench, we release 29 additional new hand-annotated training constraints and verification functions, RLVR training prompts, and code.

## 03-046 | Direct Language Model Alignment from Online AI Feedback
- arXiv: 2402.04792  first public: 2024-02-07  latest: 2024-02-29  primary cat: cs.AI
- authors (12): Shangmin Guo; Biao Zhang; Tianlin Liu; Tianqi Liu; Misha Khalman; Felipe Llinares ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: 18 pages, 9 figures, 4 tables
- pages: 18

ABSTRACT: Direct alignment from preferences (DAP) methods, such as DPO, have recently emerged as efficient alternatives to reinforcement learning from human feedback (RLHF), that do not require a separate reward model. However, the preference datasets used in DAP methods are usually collected ahead of training and never updated, thus the feedback is purely offline. Moreover, responses in these datasets are often sampled from a language model distinct from the one being aligned, and since the model evolves over training, the alignment phase is inevitably off-policy. In this study, we posit that online feedback is key and improves DAP methods. Our method, online AI feedback (OAIF), uses an LLM as annotator: on each training iteration, we sample two responses from the current model and prompt the LLM annotator to choose which one is preferred, thus providing online feedback. Despite its simplicity, we demonstrate via human evaluation in several tasks that OAIF outperforms both offline DAP and RLHF methods. We further show that the feedback leveraged in OAIF is easily controllable, via instruction prompts to the LLM annotator.

## 03-047 | RM-R1: Reward Modeling as Reasoning
- arXiv: 2505.02387  first public: 2025-05-05  latest: 2026-03-06  primary cat: cs.CL
- authors (12): Xiusi Chen; Gaotang Li; Ziqi Wang; Bowen Jin; Cheng Qian; Yu Wang ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: ['04']
- arXiv comment: ICLR 2026
- URLs on first pages of PDF: https://github.com/RM-R1-UIUC/RM-R1
- pages: 30

ABSTRACT: Reward modeling is essential for aligning large language models with human preferences through reinforcement learning. To provide accurate reward signals, a reward model (RM) should stimulate deep thinking and conduct interpretable reasoning before assigning a score or a judgment. Inspired by recent advances of long chain-of-thought on reasoning-intensive tasks, we hypothesize and validate that integrating reasoning into reward modeling significantly enhances RM's interpretability and performance. We introduce a new class of generative reward models, Reasoning Reward Models (ReasRMs), which formulate reward modeling as a reasoning task. We propose a reasoning-oriented training pipeline and train a family of ReasRMs, RM-R1. RM-R1 features a chain-of-rubrics (CoR) mechanism -- self-generating sample-level chat rubrics or math/code solutions, and evaluating candidate responses against them. The training of RM-R1 consists of two key stages: (1) distillation of high-quality reasoning chains and (2) reinforcement learning with verifiable rewards. Empirically, our models achieve superior performance across three reward model benchmarks on average, outperforming much larger open-weight models (e.g., INF-ORM-Llama3.1-70B) and proprietary ones (e.g., GPT-4o) by up to 4.9%. Beyond final performance, we perform thorough analyses to understand the key ingredients of successful ReasRM training.

## 03-048 | Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms
- arXiv: 2406.02900  first public: 2024-06-05  latest: 2024-11-05  primary cat: cs.LG
- authors (8): Rafael Rafailov; Yaswanth Chittepu; Ryan Park; Harshit Sikchi; Joey Hejna; Bradley Knox ...
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- arXiv comment: 30 pages, 38th Conference on Neural Information Processing Systems (NeurIPS 2024)
- pages: 36

ABSTRACT: Reinforcement Learning from Human Feedback (RLHF) has been crucial to the recent success of Large Language Models (LLMs), however, it is often a complex and brittle process. In the classical RLHF framework, a reward model is first trained to represent human preferences, which is in turn used by an online reinforcement learning (RL) algorithm to optimize the LLM. A prominent issue with such methods is reward over-optimization or reward hacking, where performance as measured by the learned proxy reward model increases, but true quality plateaus or even deteriorates. Direct Alignment Algorithms (DDAs) like Direct Preference Optimization have emerged as alternatives to the classical RLHF pipeline by circumventing the reward modeling phase. However, although DAAs do not use a separate proxy reward model, they still commonly deteriorate from over-optimization. While the so-called reward hacking phenomenon is not well-defined for DAAs, we still uncover similar trends: at higher KL budgets, DAA algorithms exhibit similar degradation patterns to their classic RLHF counterparts. In particular, we find that DAA methods deteriorate not only across a wide range of KL budgets but also often before even a single epoch of the dataset is completed. Through extensive empirical experimentation, this work formulates and formalizes the reward over-optimization or hacking problem for DAAs and explores its consequences across objectives, training regimes, and model scales.

## 03-049 | Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains
- arXiv: 2507.17746  first public: 2025-07-23  latest: 2025-10-03  primary cat: cs.LG
- authors (7): Anisha Gunjal; Anthony Wang; Elaine Lau; Vaskar Nath; Yunzhong He; Bing Liu ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: preprint
- URLs on first pages of PDF: https://huggingface.co/datasets/anisha2102/RaR-Medicine https://huggingface.co/datasets/anisha2102/RaR-Science
- pages: 20

ABSTRACT: Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective for complex reasoning tasks with clear correctness signals such as math and coding. However, extending it to real-world reasoning tasks is challenging, as evaluation depends on nuanced, multi-criteria judgments rather than binary correctness. Instance-specific rubrics have recently been used in evaluation benchmarks to capture such judgments, but their potential as reward signals for on-policy post-training remains underexplored. We introduce $\textbf{Rubrics as Rewards}$ (RaR), an on-policy reinforcement learning method that extends RLVR beyond verifiable domains by using rubric-based feedback. Across both medical and science domains, we evaluate multiple strategies for aggregating rubric feedback into rewards. The best RaR variant achieves relative improvements of up to $31\%$ on HealthBench and $7\%$ on GPQA-Diamond over popular LLM-as-judge baselines that rely on direct Likert-based rewards. These results demonstrate that RaR-trained policies adapt well to diverse evaluation formats, performing strongly on both rubric-based and multiple-choice tasks. Moreover, we find that using rubrics as structured reward signals yields better alignment for smaller judges and reduces performance variance across judge scales.

## 03-050 | Towards a Unified View of Preference Learning for Large Language Models: A Survey
- arXiv: 2409.02795  first public: 2024-09-04  latest: 2024-10-31  primary cat: cs.CL
- authors (25): Bofei Gao; Feifan Song; Yibo Miao; Zefan Cai; Zhe Yang; Liang Chen ...
- seed subtopic: 偏好优化; type: 综述; cross: []
- arXiv comment: 23 pages, 6 figures
- pages: 32

ABSTRACT: Large Language Models (LLMs) exhibit remarkably powerful capabilities. One of the crucial factors to achieve success is aligning the LLM's output with human preferences. This alignment process often requires only a small amount of data to efficiently enhance the LLM's performance. While effective, research in this area spans multiple domains, and the methods involved are relatively complex to understand. The relationships between different methods have been under-explored, limiting the development of the preference alignment. In light of this, we break down the existing popular alignment strategies into different components and provide a unified framework to study the current alignment strategies, thereby establishing connections among them. In this survey, we decompose all the strategies in preference learning into four components: model, data, feedback, and algorithm. This unified view offers an in-depth understanding of existing alignment algorithms and also opens up possibilities to synergize the strengths of different strategies. Furthermore, we present detailed working examples of prevalent existing algorithms to facilitate a comprehensive understanding for the readers. Finally, based on our unified perspective, we explore the challenges and future research directions for aligning large language models with human preferences.

## 03-051 | LLM Critics Help Catch LLM Bugs
- arXiv: 2407.00215  first public: 2024-06-28  latest: 2024-06-28  primary cat: cs.SE
- authors (6): Nat McAleese; Rai Michael Pokorny; Juan Felipe Ceron Uribe; Evgenia Nitishinskaya; Maja Trebacz; Jan Leike
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- pages: 23

ABSTRACT: Reinforcement learning from human feedback (RLHF) is fundamentally limited by the capacity of humans to correctly evaluate model output. To improve human evaluation ability and overcome that limitation this work trains "critic" models that help humans to more accurately evaluate model-written code. These critics are themselves LLMs trained with RLHF to write natural language feedback highlighting problems in code from real-world assistant tasks. On code containing naturally occurring LLM errors model-written critiques are preferred over human critiques in 63% of cases, and human evaluation finds that models catch more bugs than human contractors paid for code review. We further confirm that our fine-tuned LLM critics can successfully identify hundreds of errors in ChatGPT training data rated as "flawless", even though the majority of those tasks are non-code tasks and thus out-of-distribution for the critic model. Critics can have limitations of their own, including hallucinated bugs that could mislead humans into making mistakes they might have otherwise avoided, but human-machine teams of critics and contractors catch similar numbers of bugs to LLM critics while hallucinating less than LLMs alone.

## 03-052 | Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision
- arXiv: 2312.09390  first public: 2023-12-14  latest: 2023-12-14  primary cat: cs.CL
- authors (12): Collin Burns; Pavel Izmailov; Jan Hendrik Kirchner; Bowen Baker; Leo Gao; Leopold Aschenbrenner ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: ['12']
- pages: 49

ABSTRACT: Widely used alignment techniques, such as reinforcement learning from human feedback (RLHF), rely on the ability of humans to supervise model behavior - for example, to evaluate whether a model faithfully followed instructions or generated safe outputs. However, future superhuman models will behave in complex ways too difficult for humans to reliably evaluate; humans will only be able to weakly supervise superhuman models. We study an analogy to this problem: can weak model supervision elicit the full capabilities of a much stronger model? We test this using a range of pretrained language models in the GPT-4 family on natural language processing (NLP), chess, and reward modeling tasks. We find that when we naively finetune strong pretrained models on labels generated by a weak model, they consistently perform better than their weak supervisors, a phenomenon we call weak-to-strong generalization. However, we are still far from recovering the full capabilities of strong models with naive finetuning alone, suggesting that techniques like RLHF may scale poorly to superhuman models without further work. We find that simple methods can often significantly improve weak-to-strong generalization: for example, when finetuning GPT-4 with a GPT-2-level supervisor and an auxiliary confidence loss, we can recover close to GPT-3.5-level performance on NLP tasks. Our results suggest that it is feasible to make empirical progress today on a fundamental challenge of aligning superhuman models.

## 03-054 | A Survey of Reinforcement Learning from Human Feedback
- arXiv: 2312.14925  first public: 2023-12-22  latest: 2025-12-28  primary cat: cs.LG
- authors (4): Timo Kaufmann; Paul Weng; Viktor Bengs; Eyke Hüllermeier
- seed subtopic: 人类反馈与模型反馈; type: 综述; cross: []
- arXiv comment: Published version (TMLR): https://openreview.net/pdf?id=f7OkIurx4b
- journal_ref: Transactions on Machine Learning Research, 2025
- pages: 91

ABSTRACT: Reinforcement learning from human feedback (RLHF) is a variant of reinforcement learning (RL) that learns from human feedback instead of relying on an engineered reward function. Building on prior work on the related setting of preference-based reinforcement learning (PbRL), it stands at the intersection of artificial intelligence and human-computer interaction. This positioning provides a promising approach to enhance the performance and adaptability of intelligent systems while also improving the alignment of their objectives with human values. The success in training large language models (LLMs) has impressively demonstrated this potential in recent years, where RLHF has played a decisive role in directing the model's capabilities towards human objectives. This article provides an overview of the fundamentals of RLHF, exploring how RL agents interact with human feedback. While recent focus has been on RLHF for LLMs, our survey covers the technique across multiple domains. We provide our most comprehensive coverage in control and robotics, where many fundamental techniques originate, alongside a dedicated LLM section. We examine the core principles that underpin RLHF, how algorithms and human feedback work together, and the main research trends in the field. Our goal is to give researchers and practitioners a clear understanding of this rapidly growing field.

## 03-055 | Checklists Are Better Than Reward Models For Aligning Language Models
- arXiv: 2507.18624  first public: 2025-07-24  latest: 2025-12-01  primary cat: cs.CL
- authors (7): Vijay Viswanathan; Yanchao Sun; Shuang Ma; Xiang Kong; Meng Cao; Graham Neubig ...
- seed subtopic: 人类反馈与模型反馈; type: 原始研究; cross: []
- arXiv comment: Presented at NeurIPS 2025
- pages: 20

ABSTRACT: Language models must be adapted to understand and follow user instructions. Reinforcement learning is widely used to facilitate this -- typically using fixed criteria such as "helpfulness" and "harmfulness". In our work, we instead propose using flexible, instruction-specific criteria as a means of broadening the impact that reinforcement learning can have in eliciting instruction following. We propose "Reinforcement Learning from Checklist Feedback" (RLCF). From instructions, we extract checklists and evaluate how well responses satisfy each item - using both AI judges and specialized verifier programs - then combine these scores to compute rewards for RL. We compare RLCF with other alignment methods applied to a strong instruction following model (Qwen2.5-7B-Instruct) on five widely-studied benchmarks -- RLCF is the only method to improve performance on every benchmark, including a 4-point boost in hard satisfaction rate on FollowBench, a 6-point increase on InFoBench, and a 3-point rise in win rate on Arena-Hard. These results establish checklist feedback as a key tool for improving language models' support of queries that express a multitude of needs.

## 03-079 | RL's Razor: Why Online Reinforcement Learning Forgets Less
- arXiv: 2509.04259  first public: 2025-09-04  latest: 2025-09-04  primary cat: cs.LG
- authors (3): Idan Shenfeld; Jyothish Pari; Pulkit Agrawal
- seed subtopic: 指令微调; type: 原始研究; cross: []
- URLs on first pages of PDF: http://jyopari.github.io/posts/rl_razor
- pages: 23

ABSTRACT: Comparison of fine-tuning models with reinforcement learning (RL) and supervised fine-tuning (SFT) reveals that, despite similar performance at a new task, RL preserves prior knowledge and capabilities significantly better. We find that the degree of forgetting is determined by the distributional shift, measured as the KL-divergence between the fine-tuned and base policy evaluated on the new task. Our analysis reveals that on-policy RL is implicitly biased towards KL-minimal solutions among the many that solve the new task, whereas SFT can converge to distributions arbitrarily far from the base model. We validate these findings through experiments with large language models and robotic foundation models and further provide theoretical justification for why on-policy RL updates lead to a smaller KL change. We term this principle $\textit{RL's Razor}$: among all ways to solve a new task, RL prefers those closest in KL to the original model.

## 03-080 | How Sampling Shapes LLM Alignment: From One-Shot Optima to Iterative Dynamics
- arXiv: 2602.12180  first public: 2026-02-12  latest: 2026-02-12  primary cat: cs.LG
- authors (4): Yurong Chen; Yu He; Michael I. Jordan; Fan Yao
- seed subtopic: 偏好优化; type: 原始研究; cross: []
- pages: 61

ABSTRACT: Standard methods for aligning large language models with human preferences learn from pairwise comparisons among sampled candidate responses and regularize toward a reference policy. Despite their effectiveness, the effects of sampling and reference choices are poorly understood theoretically. We investigate these effects through Identity Preference Optimization, a widely used preference alignment framework, and show that proper instance-dependent sampling can yield stronger ranking guarantees, while skewed on-policy sampling can induce excessive concentration under structured preferences. We then analyze iterative alignment dynamics in which the learned policy feeds back into future sampling and reference policies, reflecting a common practice of model-generated preference data. We prove that these dynamics can exhibit persistent oscillations or entropy collapse for certain parameter choices, and characterize regimes that guarantee stability. Our theoretical insights extend to Direct Preference Optimization, indicating the phenomena we captured are common to a broader class of preference-alignment methods. Experiments on real-world preference data validate our findings.

## 03-081 | LoFT: Low-Rank Adaptation That Behaves Like Full Fine-Tuning
- arXiv: 2505.21289  first public: 2025-05-27  latest: 2026-03-09  primary cat: cs.LG
- authors (5): Nurbek Tastan; Stefanos Laskaridis; Martin Takac; Karthik Nandakumar; Samuel Horvath
- seed subtopic: 参数高效微调; type: 原始研究; cross: []
- arXiv comment: Accepted to ICLR 2026
- URLs on first pages of PDF: https://github.com/tnurbek/loft
- pages: 31

ABSTRACT: Large pre-trained models are commonly adapted to downstream tasks using parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA), which injects small trainable low-rank matrices instead of updating all weights. While LoRA dramatically reduces trainable parameters with little overhead, it can still underperform full fine-tuning in accuracy and often converges more slowly. We introduce LoFT, a novel low-rank adaptation method that behaves like full fine-tuning by aligning the optimizer's internal dynamics with those of updating all model weights. LoFT not only learns weight updates in a low-rank subspace (like LoRA) but also properly projects the optimizer's first and second moments (Adam's momentum and variance) into the same subspace, mirroring full-model updates. By aligning the low-rank update itself with the full update, LoFT eliminates the need for tuning extra hyperparameters, e.g., the LoRA scaling factor $α$. Empirically, this approach substantially narrows the performance gap between adapter-based tuning and full fine-tuning and consistently outperforms standard LoRA-style methods, all without increasing inference cost.
