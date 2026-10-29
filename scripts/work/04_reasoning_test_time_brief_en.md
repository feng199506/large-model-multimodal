# Brief for annotation: 04 推理与测试时计算

## 04-001 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- arXiv: 2201.11903  first public: 2022-01-28  latest: 2023-01-10  primary cat: cs.CL
- authors (9): Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia ...
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- pages: 43

ABSTRACT: We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

## 04-002 | Self-Consistency Improves Chain of Thought Reasoning in Language Models
- arXiv: 2203.11171  first public: 2022-03-21  latest: 2023-03-07  primary cat: cs.CL
- authors (8): Xuezhi Wang; Jason Wei; Dale Schuurmans; Quoc Le; Ed Chi; Sharan Narang ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- arXiv comment: Published at ICLR 2023. V2: added PaLM results; V3: added UL2 results; V4: camera ready version at ICLR 2023
- pages: 24

ABSTRACT: Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

## 04-003 | Let's Verify Step by Step
- arXiv: 2305.20050  first public: 2023-05-31  latest: 2023-05-31  primary cat: cs.LG
- authors (10): Hunter Lightman; Vineet Kosaraju; Yura Burda; Harri Edwards; Bowen Baker; Teddy Lee ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- pages: 29

ABSTRACT: In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

## 04-004 | Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- arXiv: 2305.10601  first public: 2023-05-17  latest: 2023-12-03  primary cat: cs.CL
- authors (7): Shunyu Yao; Dian Yu; Jeffrey Zhao; Izhak Shafran; Thomas L. Griffiths; Yuan Cao ...
- seed subtopic: 搜索; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2023 camera ready version. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm
- URLs on first pages of PDF: https://github.com/princeton-nlp/tree-of-thought-llm
- pages: 14

ABSTRACT: Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, Tree of Thoughts (ToT), which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices. Our experiments show that ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords. For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm.

## 04-005 | Training Verifiers to Solve Math Word Problems
- arXiv: 2110.14168  first public: 2021-10-27  latest: 2021-11-18  primary cat: cs.LG
- authors (12): Karl Cobbe; Vineet Kosaraju; Mohammad Bavarian; Mark Chen; Heewoo Jun; Lukasz Kaiser ...
- seed subtopic: 验证器; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/openai/grade-
- pages: 22

ABSTRACT: State-of-the-art language models can match human performance on many tasks, but they still struggle to robustly perform multi-step mathematical reasoning. To diagnose the failures of current models and support research, we introduce GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems. We find that even the largest transformer models fail to achieve high test performance, despite the conceptual simplicity of this problem distribution. To increase performance, we propose training verifiers to judge the correctness of model completions. At test time, we generate many candidate solutions and select the one ranked highest by the verifier. We demonstrate that verification significantly improves performance on GSM8K, and we provide strong empirical evidence that verification scales more effectively with increased data than a finetuning baseline.

## 04-006 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- arXiv: 2501.12948  first public: 2025-01-22  latest: 2026-01-04  primary cat: cs.CL
- authors (200): DeepSeek-AI; Daya Guo; Dejian Yang; Haowei Zhang; Junxiao Song; Peiyi Wang ...
- seed subtopic: 推理强化学习; type: 技术报告; cross: []
- journal_ref: Nature volume 645, pages 633-638 (2025)
- doi: 10.1038/s41586-025-09422-z
- URLs on first pages of PDF: https://huggingface.co/deepseek-ai
- pages: 86

ABSTRACT: General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.

## 04-007 | DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition
- arXiv: 2504.21801  first public: 2025-04-30  latest: 2025-07-18  primary cat: cs.CL
- authors (18): Z. Z. Ren; Zhihong Shao; Junxiao Song; Huajian Xin; Haocheng Wang; Wanjia Zhao ...
- seed subtopic: 数学推理; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/deepseek-ai/DeepSeek-Prover-V2
- pages: 39

ABSTRACT: We introduce DeepSeek-Prover-V2, an open-source large language model designed for formal theorem proving in Lean 4, with initialization data collected through a recursive theorem proving pipeline powered by DeepSeek-V3. The cold-start training procedure begins by prompting DeepSeek-V3 to decompose complex problems into a series of subgoals. The proofs of resolved subgoals are synthesized into a chain-of-thought process, combined with DeepSeek-V3's step-by-step reasoning, to create an initial cold start for reinforcement learning. This process enables us to integrate both informal and formal mathematical reasoning into a unified model. The resulting model, DeepSeek-Prover-V2-671B, achieves state-of-the-art performance in neural theorem proving, reaching 88.9% pass ratio on the MiniF2F-test and solving 49 out of 658 problems from PutnamBench. In addition to standard benchmarks, we introduce ProverBench, a collection of 325 formalized problems, to enrich our evaluation, including 15 selected problems from the recent AIME competitions (years 24-25). Further evaluation on these 15 AIME problems shows that the model successfully solves 6 of them. In comparison, DeepSeek-V3 solves 8 of these problems using majority voting, highlighting that the gap between formal and informal mathematical reasoning in large language models is substantially narrowing.

## 04-008 | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code
- arXiv: 2403.07974  first public: 2024-03-12  latest: 2024-06-06  primary cat: cs.SE
- authors (10): Naman Jain; King Han; Alex Gu; Wen-Ding Li; Fanjia Yan; Tianjun Zhang ...
- seed subtopic: 代码推理; type: 原始研究; cross: ['12']
- arXiv comment: Website - https://livecodebench.github.io/
- pages: 46

ABSTRACT: Large Language Models (LLMs) applied to code-related applications have emerged as a prominent field, attracting significant interest from both academia and industry. However, as new and improved LLMs are developed, existing evaluation benchmarks (e.g., HumanEval, MBPP) are no longer sufficient for assessing their capabilities. In this work, we propose LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which continuously collects new problems over time from contests across three competition platforms, namely LeetCode, AtCoder, and CodeForces. Notably, our benchmark also focuses on a broader range of code related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation. Currently, LiveCodeBench hosts four hundred high-quality coding problems that were published between May 2023 and May 2024. We have evaluated 18 base LLMs and 34 instruction-tuned LLMs on LiveCodeBench. We present empirical findings on contamination, holistic performance comparisons, potential overfitting in existing benchmarks as well as individual model comparisons. We will release all prompts and model completions for further community analysis, along with a general toolkit for adding new scenarios and model

## 04-009 | ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning
- arXiv: 2502.01100  first public: 2025-02-03  latest: 2025-07-15  primary cat: cs.AI
- authors (7): Bill Yuchen Lin; Ronan Le Bras; Kyle Richardson; Ashish Sabharwal; Radha Poovendran; Peter Clark ...
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- arXiv comment: Accepted to ICML 2025
- pages: 17

ABSTRACT: We investigate the logical reasoning capabilities of large language models (LLMs) and their scalability in complex non-monotonic reasoning. To this end, we introduce ZebraLogic, a comprehensive evaluation framework for assessing LLM reasoning performance on logic grid puzzles derived from constraint satisfaction problems (CSPs). ZebraLogic enables the generation of puzzles with controllable and quantifiable complexity, facilitating a systematic study of the scaling limits of models such as Llama, o1 models, and DeepSeek-R1. By encompassing a broad range of search space complexities and diverse logical constraints, ZebraLogic provides a structured environment to evaluate reasoning under increasing difficulty. Our results reveal a significant decline in accuracy as problem complexity grows -- a phenomenon we term the curse of complexity. This limitation persists even with larger models and increased inference-time computation, suggesting inherent constraints in current LLM reasoning capabilities. Additionally, we explore strategies to enhance logical reasoning, including Best-of-N sampling, backtracking mechanisms, and self-verification prompts. Our findings offer critical insights into the scalability of LLM reasoning, highlight fundamental limitations, and outline potential directions for improvement.

## 04-010 | Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
- arXiv: 2408.03314  first public: 2024-08-06  latest: 2024-08-06  primary cat: cs.LG
- authors (4): Charlie Snell; Jaehoon Lee; Kelvin Xu; Aviral Kumar
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- pages: 37

ABSTRACT: Enabling LLMs to improve their outputs by using more test-time computation is a critical step towards building generally self-improving agents that can operate on open-ended natural language. In this paper, we study the scaling of inference-time computation in LLMs, with a focus on answering the question: if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt? Answering this question has implications not only on the achievable performance of LLMs, but also on the future of LLM pretraining and how one should tradeoff inference-time and pre-training compute. Despite its importance, little research attempted to understand the scaling behaviors of various test-time inference methods. Moreover, current work largely provides negative results for a number of these strategies. In this work, we analyze two primary mechanisms to scale test-time computation: (1) searching against dense, process-based verifier reward models; and (2) updating the model's distribution over a response adaptively, given the prompt at test time. We find that in both cases, the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt. This observation motivates applying a "compute-optimal" scaling strategy, which acts to most effectively allocate test-time compute adaptively per prompt. Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.

## 04-011 | Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- arXiv: 2312.08935  first public: 2023-12-14  latest: 2024-02-19  primary cat: cs.AI
- authors (9): Peiyi Wang; Lei Li; Zhihong Shao; R. X. Xu; Damai Dai; Yifei Li ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- arXiv comment: Add Step-by-Step reinforcement learning results
- pages: 15

ABSTRACT: In this paper, we present an innovative process-oriented math process reward model called \textbf{Math-Shepherd}, which assigns a reward score to each step of math problem solutions. The training of Math-Shepherd is achieved using automatically constructed process-wise supervision data, breaking the bottleneck of heavy reliance on manual annotation in existing work. We explore the effectiveness of Math-Shepherd in two scenarios: 1) \textit{Verification}: Math-Shepherd is utilized for reranking multiple outputs generated by Large Language Models (LLMs); 2) \textit{Reinforcement Learning}: Math-Shepherd is employed to reinforce LLMs with step-by-step Proximal Policy Optimization (PPO). With Math-Shepherd, a series of open-source LLMs demonstrates exceptional performance. For instance, the step-by-step PPO with Math-Shepherd significantly improves the accuracy of Mistral-7B (77.9\%$\to$84.1\% on GSM8K and 28.6\%$\to$33.0\% on MATH). The accuracy can be further enhanced to 89.1\% and 43.5\% on GSM8K and MATH with the verification of Math-Shepherd, respectively. We believe that automatic process supervision holds significant potential for the future evolution of LLMs.

## 04-012 | rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking
- arXiv: 2501.04519  first public: 2025-01-08  latest: 2025-01-08  primary cat: cs.CL
- authors (8): Xinyu Guan; Li Lyna Zhang; Yifei Liu; Ning Shang; Youran Sun; Yi Zhu ...
- seed subtopic: 搜索; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/microsoft/rStar
- pages: 26

ABSTRACT: We present rStar-Math to demonstrate that small language models (SLMs) can rival or even surpass the math reasoning capability of OpenAI o1, without distillation from superior models. rStar-Math achieves this by exercising "deep thinking" through Monte Carlo Tree Search (MCTS), where a math policy SLM performs test-time search guided by an SLM-based process reward model. rStar-Math introduces three innovations to tackle the challenges in training the two SLMs: (1) a novel code-augmented CoT data sythesis method, which performs extensive MCTS rollouts to generate step-by-step verified reasoning trajectories used to train the policy SLM; (2) a novel process reward model training method that avoids naïve step-level score annotation, yielding a more effective process preference model (PPM); (3) a self-evolution recipe in which the policy SLM and PPM are built from scratch and iteratively evolved to improve reasoning capabilities. Through 4 rounds of self-evolution with millions of synthesized solutions for 747k math problems, rStar-Math boosts SLMs' math reasoning to state-of-the-art levels. On the MATH benchmark, it improves Qwen2.5-Math-7B from 58.8% to 90.0% and Phi3-mini-3.8B from 41.4% to 86.4%, surpassing o1-preview by +4.5% and +0.9%. On the USA Math Olympiad (AIME), rStar-Math solves an average of 53.3% (8/15) of problems, ranking among the top 20% the brightest high school math students. Code and data will be available at https://github.com/microsoft/rStar.

## 04-013 | Generative Verifiers: Reward Modeling as Next-Token Prediction
- arXiv: 2408.15240  first public: 2024-08-27  latest: 2025-02-22  primary cat: cs.LG
- authors (6): Lunjun Zhang; Arian Hosseini; Hritik Bansal; Mehran Kazemi; Aviral Kumar; Rishabh Agarwal
- seed subtopic: 验证器; type: 原始研究; cross: []
- arXiv comment: ICLR 2025
- pages: 39

ABSTRACT: Verifiers or reward models are often used to enhance the reasoning performance of large language models (LLMs). A common approach is the Best-of-N method, where N candidate solutions generated by the LLM are ranked by a verifier, and the best one is selected. While LLM-based verifiers are typically trained as discriminative classifiers to score solutions, they do not utilize the text generation capabilities of pretrained LLMs. To overcome this limitation, we instead propose training verifiers using the ubiquitous next-token prediction objective, jointly on verification and solution generation. Compared to standard verifiers, such generative verifiers (GenRM) can benefit from several advantages of LLMs: they integrate seamlessly with instruction tuning, enable chain-of-thought reasoning, and can utilize additional test-time compute via majority voting for better verification. We demonstrate that GenRM outperforms discriminative, DPO verifiers, and LLM-as-a-Judge, resulting in large performance gains with Best-of-N, namely 5% $\rightarrow$ 45.3% on algorithmic tasks and 73% $\rightarrow$ 93.4% on GSM8K. In easy-to-hard generalization settings, we observe improvements of 28% $\rightarrow$ 44.6% on MATH, and 37.9% $\rightarrow$ 53.5% on MMLU abstract algebra. Furthermore, we find that training GenRM with synthetic verification rationales is sufficient to pick out subtle errors on math problems. Finally, we demonstrate that GenRM scales favorably with model size and test-time compute.

## 04-014 | Kimi k1.5: Scaling Reinforcement Learning with LLMs
- arXiv: 2501.12599  first public: 2025-01-22  latest: 2025-06-03  primary cat: cs.AI
- authors (96): Kimi Team; Angang Du; Bofei Gao; Bowei Xing; Changjiu Jiang; Cheng Chen ...
- seed subtopic: 推理强化学习; type: 技术报告; cross: ['07']
- arXiv comment: 25 pages
- pages: 25

ABSTRACT: Language model pretraining with next token prediction has proved effective for scaling compute but is limited to the amount of available training data. Scaling reinforcement learning (RL) unlocks a new axis for the continued improvement of artificial intelligence, with the promise that large language models (LLMs) can scale their training data by learning to explore with rewards. However, prior published work has not produced competitive results. In light of this, we report on the training practice of Kimi k1.5, our latest multi-modal LLM trained with RL, including its RL training techniques, multi-modal data recipes, and infrastructure optimization. Long context scaling and improved policy optimization methods are key ingredients of our approach, which establishes a simplistic, effective RL framework without relying on more complex techniques such as Monte Carlo tree search, value functions, and process reward models. Notably, our system achieves state-of-the-art reasoning performance across multiple benchmarks and modalities -- e.g., 77.5 on AIME, 96.2 on MATH 500, 94-th percentile on Codeforces, 74.9 on MathVista -- matching OpenAI's o1. Moreover, we present effective long2short methods that use long-CoT techniques to improve short-CoT models, yielding state-of-the-art short-CoT reasoning results -- e.g., 60.8 on AIME, 94.6 on MATH500, 47.3 on LiveCodeBench -- outperforming existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%).

## 04-015 | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- arXiv: 2402.03300  first public: 2024-02-05  latest: 2024-04-27  primary cat: cs.CL
- authors (11): Zhihong Shao; Peiyi Wang; Qihao Zhu; Runxin Xu; Junxiao Song; Xiao Bi ...
- seed subtopic: 数学推理; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/deepseek-ai/DeepSeek-Math
- pages: 30

ABSTRACT: Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

## 04-016 | Competitive Programming with Large Reasoning Models
- arXiv: 2502.06807  first public: 2025-02-03  latest: 2025-02-18  primary cat: cs.LG
- authors (26): OpenAI; :; Ahmed El-Kishky; Alexander Wei; Andre Saraiva; Borys Minaiev ...
- seed subtopic: 代码推理; type: 原始研究; cross: []
- pages: 48

ABSTRACT: We show that reinforcement learning applied to large language models (LLMs) significantly boosts performance on complex coding and reasoning tasks. Additionally, we compare two general-purpose reasoning models - OpenAI o1 and an early checkpoint of o3 - with a domain-specific system, o1-ioi, which uses hand-engineered inference strategies designed for competing in the 2024 International Olympiad in Informatics (IOI). We competed live at IOI 2024 with o1-ioi and, using hand-crafted test-time strategies, placed in the 49th percentile. Under relaxed competition constraints, o1-ioi achieved a gold medal. However, when evaluating later models such as o3, we find that o3 achieves gold without hand-crafted domain-specific strategies or relaxed constraints. Our findings show that although specialized pipelines such as o1-ioi yield solid improvements, the scaled-up, general-purpose o3 model surpasses those results without relying on hand-crafted inference heuristics. Notably, o3 achieves a gold medal at the 2024 IOI and obtains a Codeforces rating on par with elite human competitors. Overall, these results indicate that scaling general-purpose reinforcement learning, rather than relying on domain-specific techniques, offers a robust path toward state-of-the-art AI in reasoning domains, such as competitive programming.

## 04-017 | Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning
- arXiv: 2502.14768  first public: 2025-02-20  latest: 2025-02-20  primary cat: cs.CL
- authors (10): Tian Xie; Zitian Gao; Qingnan Ren; Haoming Luo; Yuqian Hong; Bryan Dai ...
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- pages: 17

ABSTRACT: Inspired by the success of DeepSeek-R1, we explore the potential of rule-based reinforcement learning (RL) in large reasoning models. To analyze reasoning dynamics, we use synthetic logic puzzles as training data due to their controllable complexity and straightforward answer verification. We make some key technical contributions that lead to effective and stable RL training: a system prompt that emphasizes the thinking and answering process, a stringent format reward function that penalizes outputs for taking shortcuts, and a straightforward training recipe that achieves stable convergence. Our 7B model develops advanced reasoning skills-such as reflection, verification, and summarization-that are absent from the logic corpus. Remarkably, after training on just 5K logic problems, it demonstrates generalization abilities to the challenging math benchmarks AIME and AMC.

## 04-018 | s1: Simple test-time scaling
- arXiv: 2501.19393  first public: 2025-01-31  latest: 2025-03-01  primary cat: cs.CL
- authors (10): Niklas Muennighoff; Zitong Yang; Weijia Shi; Xiang Lisa Li; Li Fei-Fei; Hannaneh Hajishirzi ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- arXiv comment: 46 pages (9 main), 10 figures, 15 tables
- URLs on first pages of PDF: https://github.com/simplescaling/s1
- pages: 46

ABSTRACT: Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI's o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria we validate through ablations: difficulty, diversity, and quality. Second, we develop budget forcing to control test-time compute by forcefully terminating the model's thinking process or lengthening it by appending "Wait" multiple times to the model's generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps. After supervised finetuning the Qwen2.5-32B-Instruct language model on s1K and equipping it with budget forcing, our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24). Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% on AIME24. Our model, data, and code are open-source at https://github.com/simplescaling/s1

## 04-019 | Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- arXiv: 2410.08146  first public: 2024-10-10  latest: 2024-10-10  primary cat: cs.LG
- authors (9): Amrith Setlur; Chirag Nagpal; Adam Fisch; Xinyang Geng; Jacob Eisenstein; Rishabh Agarwal ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- pages: 31

ABSTRACT: A promising approach for improving reasoning in large language models is to use process reward models (PRMs). PRMs provide feedback at each step of a multi-step reasoning trace, potentially improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains. To improve a base policy by running search against a PRM or using it as dense rewards for reinforcement learning (RL), we ask: "How should we design process rewards?". Our key insight is that, to be effective, the process reward for a step should measure progress: a change in the likelihood of producing a correct response in the future, before and after taking the step, corresponding to the notion of step-level advantages in RL. Crucially, this progress should be measured under a prover policy distinct from the base policy. We theoretically characterize the set of good provers and our results show that optimizing process rewards from such provers improves exploration during test-time search and online RL. In fact, our characterization shows that weak prover policies can substantially improve a stronger base policy, which we also observe empirically. We validate our claims by training process advantage verifiers (PAVs) to predict progress under such provers, and show that compared to ORMs, test-time search against PAVs is $>8\%$ more accurate, and $1.5-5\times$ more compute-efficient. Online RL with dense rewards from PAVs enables one of the first results with $5-6\times$ gain in sample efficiency, and $>6\%$ gain in accuracy, over ORMs.

## 04-020 | ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- arXiv: 2406.03816  first public: 2024-06-06  latest: 2024-11-18  primary cat: cs.CL
- authors (6): Dan Zhang; Sining Zhoubian; Ziniu Hu; Yisong Yue; Yuxiao Dong; Jie Tang
- seed subtopic: 搜索; type: 原始研究; cross: []
- arXiv comment: Accepted to NeurIPS 2024
- URLs on first pages of PDF: https://github.com/THUDM/ReST-MCTS
- pages: 38

ABSTRACT: Recent methodologies in LLM self-training mostly rely on LLM generating responses and filtering those with correct output answers as training data. This approach often yields a low-quality fine-tuning training set (e.g., incorrect plans or intermediate reasoning). In this paper, we develop a reinforced self-training approach, called ReST-MCTS*, based on integrating process reward guidance with tree search MCTS* for collecting higher-quality reasoning traces as well as per-step value to train policy and reward models. ReST-MCTS* circumvents the per-step manual annotation typically used to train process rewards by tree-search-based reinforcement learning: Given oracle final correct answers, ReST-MCTS* is able to infer the correct process rewards by estimating the probability this step can help lead to the correct answer. These inferred rewards serve dual purposes: they act as value targets for further refining the process reward model and also facilitate the selection of high-quality traces for policy model self-training. We first show that the tree-search policy in ReST-MCTS* achieves higher accuracy compared with prior LLM reasoning baselines such as Best-of-N and Tree-of-Thought, within the same search budget. We then show that by using traces searched by this tree-search policy as training data, we can continuously enhance the three language models for multiple iterations, and outperform other self-training algorithms such as ReST$^\text{EM}$ and Self-Rewarding LM. We release all code at https://github.com/THUDM/ReST-MCTS.

## 04-021 | V-STaR: Training Verifiers for Self-Taught Reasoners
- arXiv: 2402.06457  first public: 2024-02-09  latest: 2024-08-14  primary cat: cs.LG
- authors (6): Arian Hosseini; Xingdi Yuan; Nikolay Malkin; Aaron Courville; Alessandro Sordoni; Rishabh Agarwal
- seed subtopic: 验证器; type: 原始研究; cross: []
- pages: 16

ABSTRACT: Common self-improvement approaches for large language models (LLMs), such as STaR, iteratively fine-tune LLMs on self-generated solutions to improve their problem-solving ability. However, these approaches discard the large amounts of incorrect solutions generated during this process, potentially neglecting valuable information in such solutions. To address this shortcoming, we propose V-STaR that utilizes both the correct and incorrect solutions generated during the self-improvement process to train a verifier using DPO that judges correctness of model-generated solutions. This verifier is used at inference time to select one solution among many candidate solutions. Running V-STaR for multiple iterations results in progressively better reasoners and verifiers, delivering a 4% to 17% test accuracy improvement over existing self-improvement and verification approaches on common code generation and math reasoning benchmarks with LLaMA2 models.

## 04-022 | DAPO: An Open-Source LLM Reinforcement Learning System at Scale
- arXiv: 2503.14476  first public: 2025-03-18  latest: 2025-05-20  primary cat: cs.LG
- authors (35): Qiying Yu; Zheng Zhang; Ruofei Zhu; Yufeng Yuan; Xiaochen Zuo; Yu Yue ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- arXiv comment: Project Page: https://dapo-sia.github.io/
- URLs on first pages of PDF: https://github.com/volcengine/verl
- pages: 16

ABSTRACT: Inference scaling empowers LLMs with unprecedented reasoning ability, with reinforcement learning as the core technique to elicit complex reasoning. However, key technical details of state-of-the-art reasoning LLMs are concealed (such as in OpenAI o1 blog and DeepSeek R1 technical report), thus the community still struggles to reproduce their RL training results. We propose the $\textbf{D}$ecoupled Clip and $\textbf{D}$ynamic s$\textbf{A}$mpling $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{DAPO}$) algorithm, and fully open-source a state-of-the-art large-scale RL system that achieves 50 points on AIME 2024 using Qwen2.5-32B base model. Unlike previous works that withhold training details, we introduce four key techniques of our algorithm that make large-scale LLM RL a success. In addition, we open-source our training code, which is built on the verl framework, along with a carefully curated and processed dataset. These components of our open-source system enhance reproducibility and support future research in large-scale LLM RL.

## 04-023 | Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement
- arXiv: 2409.12122  first public: 2024-09-18  latest: 2024-09-18  primary cat: cs.CL
- authors (16): An Yang; Beichen Zhang; Binyuan Hui; Bofei Gao; Bowen Yu; Chengpeng Li ...
- seed subtopic: 数学推理; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen-Agent https://github.com/QwenLM/Qwen2-Math https://huggingface.co/Qwen
- pages: 39

ABSTRACT: In this report, we present a series of math-specific large language models: Qwen2.5-Math and Qwen2.5-Math-Instruct-1.5B/7B/72B. The core innovation of the Qwen2.5 series lies in integrating the philosophy of self-improvement throughout the entire pipeline, from pre-training and post-training to inference: (1) During the pre-training phase, Qwen2-Math-Instruct is utilized to generate large-scale, high-quality mathematical data. (2) In the post-training phase, we develop a reward model (RM) by conducting massive sampling from Qwen2-Math-Instruct. This RM is then applied to the iterative evolution of data in supervised fine-tuning (SFT). With a stronger SFT model, it's possible to iteratively train and update the RM, which in turn guides the next round of SFT data iteration. On the final SFT model, we employ the ultimate RM for reinforcement learning, resulting in the Qwen2.5-Math-Instruct. (3) Furthermore, during the inference stage, the RM is used to guide sampling, optimizing the model's performance. Qwen2.5-Math-Instruct supports both Chinese and English, and possess advanced mathematical reasoning capabilities, including Chain-of-Thought (CoT) and Tool-Integrated Reasoning (TIR). We evaluate our models on 10 mathematics datasets in both English and Chinese, such as GSM8K, MATH, GaoKao, AMC23, and AIME24, covering a range of difficulties from grade school level to math competition problems.

## 04-024 | OpenCodeReasoning: Advancing Data Distillation for Competitive Coding
- arXiv: 2504.01943  first public: 2025-04-02  latest: 2025-08-07  primary cat: cs.CL
- authors (8): Wasi Uddin Ahmad; Sean Narenthiran; Somshubra Majumdar; Aleksander Ficek; Siddhartha Jain; Jocelyn Huang ...
- seed subtopic: 代码推理; type: 原始研究; cross: []
- arXiv comment: Published at COLM 2025
- URLs on first pages of PDF: https://huggingface.co/datasets/nvidia/OpenCodeReasoning
- pages: 15

ABSTRACT: Since the advent of reasoning-based large language models, many have found great success from distilling reasoning capabilities into student models. Such techniques have significantly bridged the gap between reasoning and standard LLMs on coding tasks. Despite this, much of the progress on distilling reasoning models remains locked behind proprietary datasets or lacks details on data curation, filtering and subsequent training. To address this, we construct a superior supervised fine-tuning (SFT) dataset that we use to achieve state-of-the-art coding capability results in models of various sizes. Our distilled models use only SFT to achieve 61.8% on LiveCodeBench and 24.6% on CodeContests, surpassing alternatives trained with reinforcement learning. We then perform analysis on the data sources used to construct our dataset, the impact of code execution filtering, and the importance of instruction/solution diversity. We observe that execution filtering negatively affected benchmark accuracy, leading us to prioritize instruction diversity over solution correctness. Finally, we also analyze the token efficiency and reasoning patterns utilized by these models. We will open-source these datasets and distilled models to the community.

## 04-025 | GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models
- arXiv: 2410.05229  first public: 2024-10-07  latest: 2025-08-27  primary cat: cs.LG
- authors (6): Iman Mirzadeh; Keivan Alizadeh; Hooman Shahrokhi; Oncel Tuzel; Samy Bengio; Mehrdad Farajtabar
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- arXiv comment: ICLR camera ready + additional discussion in the appendix
- URLs on first pages of PDF: https://github.com/apple/ml-gsm-symbolic
- pages: 24

ABSTRACT: Recent advancements in Large Language Models (LLMs) have sparked interest in their formal reasoning capabilities, particularly in mathematics. The GSM8K benchmark is widely used to assess the mathematical reasoning of models on grade-school-level questions. While the performance of LLMs on GSM8K has significantly improved in recent years, it remains unclear whether their mathematical reasoning capabilities have genuinely advanced, raising questions about the reliability of the reported metrics. To address these concerns, we conduct a large-scale study on several SOTA open and closed models. To overcome the limitations of existing evaluations, we introduce GSM-Symbolic, an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions. GSM-Symbolic enables more controllable evaluations, providing key insights and more reliable metrics for measuring the reasoning capabilities of models.Our findings reveal that LLMs exhibit noticeable variance when responding to different instantiations of the same question. Specifically, the performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark. Furthermore, we investigate the fragility of mathematical reasoning in these models and show that their performance significantly deteriorates as the number of clauses in a question increases. We hypothesize that this decline is because current LLMs cannot perform genuine logical reasoning; they replicate reasoning steps from their training data. Adding a single clause that seems relevant to the question causes significant performance drops (up to 65%) across all state-of-the-art models, even though the clause doesn't contribute to the reasoning chain needed for the final answer. Overall, our work offers a more nuanced understanding of LLMs' capabilities and limitations in mathematical reasoning.

## 04-026 | Large Language Monkeys: Scaling Inference Compute with Repeated Sampling
- arXiv: 2407.21787  first public: 2024-07-31  latest: 2024-12-30  primary cat: cs.LG
- authors (7): Bradley Brown; Jordan Juravsky; Ryan Ehrlich; Ronald Clark; Quoc V. Le; Christopher Ré ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/ScalingIntelligence/large_language_monkeys https://huggingface.co/datasets/ScalingIntelligence/monkey_business
- pages: 27

ABSTRACT: Scaling the amount of compute used to train language models has dramatically improved their capabilities. However, when it comes to inference, we often limit models to making only one attempt at a problem. Here, we explore inference compute as another axis for scaling, using the simple technique of repeatedly sampling candidate solutions from a model. Across multiple tasks and models, we observe that coverage -- the fraction of problems that are solved by any generated sample -- scales with the number of samples over four orders of magnitude. Interestingly, the relationship between coverage and the number of samples is often log-linear and can be modelled with an exponentiated power law, suggesting the existence of inference-time scaling laws. In domains like coding and formal proofs, where answers can be automatically verified, these increases in coverage directly translate into improved performance. When we apply repeated sampling to SWE-bench Lite, the fraction of issues solved with DeepSeek-Coder-V2-Instruct increases from 15.9% with one sample to 56% with 250 samples, outperforming the single-sample state-of-the-art of 43%. In domains without automatic verifiers, we find that common methods for picking from a sample collection (majority voting and reward models) plateau beyond several hundred samples and fail to fully scale with the sample budget.

## 04-027 | The Lessons of Developing Process Reward Models in Mathematical Reasoning
- arXiv: 2501.07301  first public: 2025-01-13  latest: 2025-06-05  primary cat: cs.CL
- authors (9): Zhenru Zhang; Chujie Zheng; Yangzhen Wu; Beichen Zhang; Runji Lin; Bowen Yu ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- pages: 21

ABSTRACT: Process Reward Models (PRMs) emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), which aim to identify and mitigate intermediate errors in the reasoning processes. However, the development of effective PRMs faces significant challenges, particularly in data annotation and evaluation methodologies. In this paper, through extensive experiments, we demonstrate that commonly used Monte Carlo (MC) estimation-based data synthesis for PRMs typically yields inferior performance and generalization compared to LLM-as-a-judge and human annotation methods. MC estimation relies on completion models to evaluate current-step correctness, leading to inaccurate step verification. Furthermore, we identify potential biases in conventional Best-of-N (BoN) evaluation strategies for PRMs: (1) The unreliable policy models generate responses with correct answers but flawed processes, leading to a misalignment between the evaluation criteria of BoN and the PRM objectives of process verification. (2) The tolerance of PRMs of such responses leads to inflated BoN scores. (3) Existing PRMs have a significant proportion of minimum scores concentrated on the final answer steps, revealing the shift from process to outcome-based assessment in BoN Optimized PRMs. To address these challenges, we develop a consensus filtering mechanism that effectively integrates MC estimation with LLM-as-a-judge and advocates a more comprehensive evaluation framework that combines response-level and step-level metrics. Based on the mechanisms, we significantly improve both model performance and data efficiency in the BoN evaluation and the step-wise error identification task. Finally, we release a new state-of-the-art PRM that outperforms existing open-source alternatives and provides practical guidelines for future research in building process supervision models.

## 04-028 | Stream of Search (SoS): Learning to Search in Language
- arXiv: 2404.03683  first public: 2024-04-01  latest: 2024-04-01  primary cat: cs.LG
- authors (7): Kanishk Gandhi; Denise Lee; Gabriel Grand; Muxin Liu; Winson Cheng; Archit Sharma ...
- seed subtopic: 搜索; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/kanishkg/stream-of-search
- pages: 16

ABSTRACT: Language models are rarely shown fruitful mistakes while training. They then struggle to look beyond the next token, suffering from a snowballing of errors and struggling to predict the consequence of their actions several steps ahead. In this paper, we show how language models can be taught to search by representing the process of search in language, as a flattened string -- a stream of search (SoS). We propose a unified language for search that captures an array of different symbolic search strategies. We demonstrate our approach using the simple yet difficult game of Countdown, where the goal is to combine input numbers with arithmetic operations to reach a target number. We pretrain a transformer-based language model from scratch on a dataset of streams of search generated by heuristic solvers. We find that SoS pretraining increases search accuracy by 25% over models trained to predict only the optimal search trajectory. We further finetune this model with two policy improvement methods: Advantage-Induced Policy Alignment (APA) and Self-Taught Reasoner (STaR). The finetuned SoS models solve 36% of previously unsolved problems, including problems that cannot be solved by any of the heuristic solvers. Our results indicate that language models can learn to solve problems via search, self-improve to flexibly use different search strategies, and potentially discover new ones.

## 04-029 | Sample, Scrutinize and Scale: Effective Inference-Time Search by Scaling Verification
- arXiv: 2502.01839  first public: 2025-02-03  latest: 2025-02-20  primary cat: cs.LG
- authors (3): Eric Zhao; Pranjal Awasthi; Sreenivas Gollapudi
- seed subtopic: 验证器; type: 原始研究; cross: []
- pages: 48

ABSTRACT: Sampling-based search, a simple paradigm for utilizing test-time compute, involves generating multiple candidate responses and selecting the best one -- typically by having models self-verify each response for correctness. In this paper, we study the scaling trends governing sampling-based search. Among our findings is that simply scaling up a minimalist implementation of sampling-based search, using only random sampling and direct self-verification, provides a practical inference method that, for example, elevates the reasoning capabilities of Gemini v1.5 Pro above that of o1-Preview on popular benchmarks. We partially attribute the scalability of sampling-based search to a phenomenon of implicit scaling, where sampling a larger pool of responses in turn improves self-verification accuracy. We further identify two useful principles for improving self-verification capabilities with test-time compute: (1) comparing across responses provides helpful signals about the locations of errors and hallucinations, and (2) different model output styles are useful for different contexts -- chains of thought are useful for reasoning but harder to verify. We also find that, though accurate verification can be elicited, frontier models demonstrate remarkably weak out-of-box verification capabilities and introduce a benchmark to measure progress on these deficiencies.

## 04-030 | Understanding R1-Zero-Like Training: A Critical Perspective
- arXiv: 2503.20783  first public: 2025-03-26  latest: 2025-10-06  primary cat: cs.LG
- authors (8): Zichen Liu; Changyu Chen; Wenjun Li; Penghui Qi; Tianyu Pang; Chao Du ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/sail-sg/oat https://github.com/sail-sg/understand-r1-zero1
- pages: 20

ABSTRACT: DeepSeek-R1-Zero has shown that reinforcement learning (RL) at scale can directly enhance the reasoning capabilities of LLMs without supervised fine-tuning. In this work, we critically examine R1-Zero-like training by analyzing its two core components: base models and RL. We investigate a wide range of base models, including DeepSeek-V3-Base, to understand how pretraining characteristics influence RL performance. Our analysis reveals that DeepSeek-V3-Base already exhibit ''Aha moment'', while Qwen2.5 base models demonstrate strong reasoning capabilities even without prompt templates, suggesting potential pretraining biases. Additionally, we identify an optimization bias in Group Relative Policy Optimization (GRPO), which artificially increases response length (especially for incorrect outputs) during training. To address this, we introduce Dr. GRPO, an unbiased optimization method that improves token efficiency while maintaining reasoning performance. Leveraging these insights, we present a minimalist R1-Zero recipe that achieves 43.3% accuracy on AIME 2024 with a 7B base model, establishing a new state-of-the-art. Our code is available at https://github.com/sail-sg/understand-r1-zero.

## 04-031 | LIMO: Less is More for Reasoning
- arXiv: 2502.03387  first public: 2025-02-05  latest: 2025-07-29  primary cat: cs.CL
- authors (6): Yixin Ye; Zhen Huang; Yang Xiao; Ethan Chern; Shijie Xia; Pengfei Liu
- seed subtopic: 数学推理; type: 原始研究; cross: []
- arXiv comment: COLM 2025
- URLs on first pages of PDF: https://github.com/GAIR-NLP/LIMO
- pages: 16

ABSTRACT: We challenge the prevailing assumption that complex reasoning in large language models (LLMs) necessitates massive training data. We demonstrate that sophisticated mathematical reasoning can emerge with only a few examples. Specifically, through simple supervised fine-tuning, our model, LIMO, achieves 63.3\% accuracy on AIME24 and 95.6\% on MATH500, surpassing previous fine-tuned models (6.5\% on AIME24, 59.2\% on MATH500) while using only 1\% of the training data required by prior approaches. Furthermore, LIMO exhibits strong out-of-distribution generalization, achieving a 45.8\% absolute improvement across diverse benchmarks, outperforming models trained on 100x more data. Synthesizing these findings, we propose the Less-Is-More Reasoning Hypothesis (LIMO Hypothesis): In foundation models where domain knowledge has been comprehensively encoded during pre-training, sophisticated reasoning can emerge through minimal but strategically designed demonstrations of cognitive processes. This hypothesis suggests that the threshold for eliciting complex reasoning is not dictated by task complexity but rather by two key factors: (1) the completeness of the model's pre-trained knowledge base and (2) the effectiveness of post-training examples in serving as "cognitive templates" that guide reasoning.

## 04-032 | AceReason-Nemotron: Advancing Math and Code Reasoning through Reinforcement Learning
- arXiv: 2505.16400  first public: 2025-05-22  latest: 2025-06-05  primary cat: cs.LG
- authors (8): Yang Chen; Zhuolin Yang; Zihan Liu; Chankyu Lee; Peng Xu; Mohammad Shoeybi ...
- seed subtopic: 代码推理; type: 原始研究; cross: []
- arXiv comment: Add pass@1024 evaluation results for LiveCodeBench v6. We release the models at: https://huggingface.co/collections/nvidia/acereason-682f4e1261dc22f697fd1485
- URLs on first pages of PDF: https://huggingface.co/nvidia/AceReason-Nemotron-14B
- pages: 23

ABSTRACT: Despite recent progress in large-scale reinforcement learning (RL) for reasoning, the training recipe for building high-performing reasoning models remains elusive. Key implementation details of frontier models, such as DeepSeek-R1, including data curation strategies and RL training recipe, are often omitted. Moreover, recent research indicates distillation remains more effective than RL for smaller models. In this work, we demonstrate that large-scale RL can significantly enhance the reasoning capabilities of strong, small- and mid-sized models, achieving results that surpass those of state-of-the-art distillation-based models. We systematically study the RL training process through extensive ablations and propose a simple yet effective approach: first training on math-only prompts, then on code-only prompts. Notably, we find that math-only RL not only significantly enhances the performance of strong distilled models on math benchmarks (e.g., +14.6% / +17.2% on AIME 2025 for the 7B / 14B models), but also code reasoning tasks (e.g., +6.8% / +5.8% on LiveCodeBench for the 7B / 14B models). In addition, extended code-only RL iterations further improve performance on code benchmarks with minimal or no degradation in math results. We develop a robust data curation pipeline to collect challenging prompts with high-quality, verifiable answers and test cases to enable verification-based RL across both domains. Finally, we identify key experimental insights, including curriculum learning with progressively increasing response lengths and the stabilizing effect of on-policy parameter updates. We find that RL not only elicits the foundational reasoning capabilities acquired during pretraining and supervised fine-tuning (e.g., distillation), but also pushes the limits of the model's reasoning ability, enabling it to solve problems that were previously unsolvable.

## 04-033 | The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity
- arXiv: 2506.06941  first public: 2025-06-07  latest: 2025-11-20  primary cat: cs.AI
- authors (6): Parshin Shojaee; Iman Mirzadeh; Keivan Alizadeh; Maxwell Horton; Samy Bengio; Mehrdad Farajtabar
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2025. camera-ready version + additional discussion in the appendix
- pages: 39

ABSTRACT: Recent generations of language models have introduced Large Reasoning Models (LRMs) that generate detailed thinking processes before providing answers. While these models demonstrate improved performance on reasoning benchmarks, their fundamental capabilities, scaling properties, and limitations remain insufficiently understood. Current evaluations primarily focus on established math and coding benchmarks, emphasizing final answer accuracy. However, this evaluation paradigm often suffers from contamination and does not provide insights into the reasoning traces. In this work, we systematically investigate these gaps with the help of controllable puzzle environments that allow precise manipulation of complexity while maintaining consistent logical structures. This setup enables the analysis of not only final answers but also the internal reasoning traces, offering insights into how LRMs think. Through extensive experiments, we show that LRMs face a complete accuracy collapse beyond certain complexities. Moreover, they exhibit a counterintuitive scaling limit: their reasoning effort increases with problem complexity up to a point, then declines despite having remaining token budget. By comparing LRMs with their standard LLM counterparts under same inference compute, we identify three performance regimes: (1) low-complexity tasks where standard models outperform LRMs, (2) medium-complexity tasks where LRMs demonstrates advantage, and (3) high-complexity tasks where both models face complete collapse. We found that LRMs have limitations in exact computation: they fail to use explicit algorithms and reason inconsistently across scales. We also investigate the reasoning traces in more depth, studying the patterns of explored solutions and analyzing the models' computational behavior, shedding light on their strengths, limitations, and raising questions about their reasoning capabilities.

## 04-034 | Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs
- arXiv: 2412.21187  first public: 2024-12-30  latest: 2025-02-01  primary cat: cs.CL
- authors (14): Xingyu Chen; Jiahao Xu; Tian Liang; Zhiwei He; Jianhui Pang; Dian Yu ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- arXiv comment: We have updated the results of DeepSeek-R1, and all conclusions still hold
- pages: 17

ABSTRACT: The remarkable performance of models like the OpenAI o1 can be attributed to their ability to emulate human-like long-time thinking during inference. These models employ extended chain-of-thought (CoT) processes, exploring multiple strategies to enhance problem-solving capabilities. However, a critical question remains: How to intelligently and efficiently scale computational resources during testing. This paper presents the first comprehensive study on the prevalent issue of overthinking in these models, where excessive computational resources are allocated for simple problems with minimal benefit. We introduce novel efficiency metrics from both outcome and process perspectives to evaluate the rational use of computational resources by o1-like models. Using a self-training paradigm, we propose strategies to mitigate overthinking, streamlining reasoning processes without compromising accuracy. Experimental results show that our approach successfully reduces computational overhead while preserving model performance across a range of testsets with varying difficulty levels, such as GSM8K, MATH500, GPQA, and AIME.

## 04-035 | ProcessBench: Identifying Process Errors in Mathematical Reasoning
- arXiv: 2412.06559  first public: 2024-12-09  latest: 2025-05-26  primary cat: cs.AI
- authors (9): Chujie Zheng; Zhenru Zhang; Beichen Zhang; Runji Lin; Keming Lu; Bowen Yu ...
- seed subtopic: 过程监督; type: 原始研究; cross: ['12']
- arXiv comment: ACL 2025
- URLs on first pages of PDF: https://github.com/QwenLM/ProcessBench https://huggingface.co/datasets/Qwen/ProcessBench
- pages: 16

ABSTRACT: As language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce ProcessBench for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on ProcessBench, involving two types of models: process reward models (PRMs) and critic models, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope ProcessBench can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.

## 04-036 | Planning In Natural Language Improves LLM Search For Code Generation
- arXiv: 2409.03733  first public: 2024-09-05  latest: 2024-10-18  primary cat: cs.LG
- authors (10): Evan Wang; Federico Cassano; Catherine Wu; Yunfeng Bai; Will Song; Vaskar Nath ...
- seed subtopic: 搜索; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/scaleapi/plansearch
- pages: 52

ABSTRACT: While scaling training compute has led to remarkable improvements in large language models (LLMs), scaling inference compute has not yet yielded analogous gains. We hypothesize that a core missing component is a lack of diverse LLM outputs, leading to inefficient search due to models repeatedly sampling highly similar, yet incorrect generations. We empirically demonstrate that this lack of diversity can be mitigated by searching over candidate plans for solving a problem in natural language. Based on this insight, we propose PlanSearch, a novel search algorithm which shows strong results across HumanEval+, MBPP+, and LiveCodeBench (a contamination-free benchmark for competitive coding). PlanSearch generates a diverse set of observations about the problem and then uses these observations to construct plans for solving the problem. By searching over plans in natural language rather than directly over code solutions, PlanSearch explores a significantly more diverse range of potential solutions compared to baseline search methods. Using PlanSearch on top of Claude 3.5 Sonnet achieves a state-of-the-art pass@200 of 77.0% on LiveCodeBench, outperforming both the best score achieved without search (pass@1 = 41.4%) and using standard repeated sampling (pass@200 = 60.6%). Finally, we show that, across all models, search algorithms, and benchmarks analyzed, we can accurately predict performance gains due to search as a direct function of the diversity over generated ideas. Code can be found at https://github.com/scaleapi/plansearch.

## 04-037 | Rethinking Reward Models for Multi-Domain Test-Time Scaling
- arXiv: 2510.00492  first public: 2025-10-01  latest: 2026-07-13  primary cat: cs.AI
- authors (15): Dong Bok Lee; Seanie Lee; Sangwoo Park; Minki Kang; Jinheon Baek; Dongki Kim ...
- seed subtopic: 验证器; type: 原始研究; cross: []
- pages: 41

ABSTRACT: The reliability of large language models (LLMs) during test-time scaling is often assessed with \emph{external verifiers} or \emph{reward models} that distinguish correct reasoning from flawed logic. Prior work has studied both outcome reward models (ORMs), which assess only the final answer, and process reward models (PRMs), which score intermediate reasoning steps. Although PRMs are often viewed as advantageous due to their finer-grained supervision, much of the supporting evidence comes from math-adjacent settings, and their relative benefits across broader domains remain unclear. We present the first unified evaluation of four reward model variants, discriminative ORM and PRM (dORM, dPRM) and generative ORM and PRM (gORM, gPRM), across 14 diverse domains. Contrary to conventional wisdom, we find that (i) dORM performs on par with dPRM, (ii) gPRM is not competitive, and (iii) overall, gORM is the most robust, yielding significant and consistent gains across every tested domain. We attribute the worse performance of gPRM to the stepwise scoring process, which inherits label noise from LLM-based automatic labeling, leading to difficulties in evaluating long reasoning trajectories, including those involving self-correcting reasoning. Both our theoretical analysis and empirical observations indicate that stepwise aggregation compounds errors as reasoning length increases. These findings challenge the common assumption that fine-grained supervision is always better and support generative outcome verification for multi-domain deployment. Our \href{https://github.com/db-Lee/Multi-RM}{\underline{code}} is publicly available to facilitate future research in multi-domain settings.

## 04-038 | Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- arXiv: 2504.13837  first public: 2025-04-18  latest: 2025-11-24  primary cat: cs.AI
- authors (8): Yang Yue; Zhiqi Chen; Rui Lu; Andrew Zhao; Zhaokai Wang; Yang Yue ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- arXiv comment: 31 pages, 27 figures
- journal_ref: NeurIPS 2025 Oral; ICML 2025 AI4MATH workshop best paper
- pages: 31

ABSTRACT: Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated notable success in enhancing the reasoning performance of large language models (LLMs), particularly on mathematics and programming tasks. Similar to how traditional RL helps agents explore and learn new strategies, RLVR is believed to enable LLMs to continuously self-improve, thus acquiring novel reasoning abilities beyond those of the corresponding base models. In this study we critically examine the current state of RLVR by systematically probing the reasoning capability boundaries of RLVR-trained LLMs across various model families, RL algorithms, and math, coding, and visual reasoning benchmarks, using pass@k at large k values as the evaluation metric. Surprisingly, we find that the current training setup does not elicit fundamentally new reasoning patterns. While RLVR-trained models outperform their base models at small k (e.g., k = 1), the base models achieve a higher pass@k score when k is large. Coverage and perplexity analyses show that the observed reasoning abilities originate from and are bounded by the base model. Treating the base model as an upper bound, our quantitative analysis shows that six popular RLVR algorithms perform similarly and remain far from optimal in leveraging the potential of the base model. By contrast, we find that distillation can introduce new reasoning patterns from the teacher and genuinely expand the model's reasoning capabilities. Overall, our findings suggest that current RLVR methods have not yet realized the potential of RL to elicit truly novel reasoning abilities in LLMs. This highlights the need for improved RL paradigms, such as continual scaling and multi-turn agent-environment interaction, to unlock this potential.

## 04-039 | FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI
- arXiv: 2411.04872  first public: 2024-11-07  latest: 2025-12-23  primary cat: cs.AI
- authors (24): Elliot Glazer; Ege Erdil; Tamay Besiroglu; Diego Chicharro; Evan Chen; Alex Gunning ...
- seed subtopic: 数学推理; type: 原始研究; cross: ['12']
- pages: 28

ABSTRACT: We introduce FrontierMath, a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics -- from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of effort from a researcher in the relevant branch of mathematics, and for the upper end questions, multiple days. FrontierMath uses new, unpublished problems and automated verification to reliably evaluate models while minimizing risk of data contamination. Current state-of-the-art AI models solve under 2% of problems, revealing a vast gap between AI capabilities and the prowess of the mathematical community. As AI systems advance toward expert-level mathematical abilities, FrontierMath offers a rigorous testbed that quantifies their progress.

## 04-040 | The Surprising Effectiveness of Test-Time Training for Few-Shot Learning
- arXiv: 2411.07279  first public: 2024-11-11  latest: 2025-03-25  primary cat: cs.AI
- authors (8): Ekin Akyürek; Mehul Damani; Adam Zweiger; Linlu Qiu; Han Guo; Jyothish Pari ...
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/adamzweiger https://github.com/ekina
- pages: 22

ABSTRACT: Language models (LMs) have shown impressive performance on tasks within their training distribution, but often struggle with structurally novel tasks even when given a small number of in-context task examples. We investigate the effectiveness of test-time training (TTT) -- temporarily updating model parameters during inference using a loss derived from input data -- as a mechanism for improving LMs' reasoning and few-shot learning capabilities. On the Abstraction and Reasoning Corpus (ARC), performing TTT with in-context examples yields up to $6\times$ higher accuracy compared to fine-tuned baselines -- reaching $53.0\%$ on the public validation set with an 8B-parameter LM and $61.9\%$ when ensembled with program-synthesis methods, matching average human performance. On BIG-Bench Hard (BBH), TTT on in-context examples surpasses standard few-shot prompting in the $10$-shot setting by $7.3$ percentage points ($50.5\%$ to $57.8\%$). Our findings highlight the limitations of in-context learning for novel tasks and demonstrate the potential of test-time training to enhance language model adaptability.

## 04-041 | L1: Controlling How Long A Reasoning Model Thinks With Reinforcement Learning
- arXiv: 2503.04697  first public: 2025-03-06  latest: 2025-10-03  primary cat: cs.CL
- authors (2): Pranjal Aggarwal; Sean Welleck
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- arXiv comment: Accepted at COLM 2025
- URLs on first pages of PDF: https://cmu-l3.github.io/l1
- pages: 27

ABSTRACT: Reasoning language models have shown an uncanny ability to improve performance at test-time by ``thinking longer''-that is, by generating longer chain-of-thought sequences and hence using more compute. However, the length of their chain-of-thought reasoning is not controllable, making it impossible to allocate test-time compute to achieve a desired level of performance. We introduce Length Controlled Policy Optimization (LCPO), a simple reinforcement learning method that optimizes for accuracy and adherence to user-specified length constraints. We use LCPO to train L1, a reasoning language model that produces outputs satisfying a length constraint given in its prompt. L1's length control allows for smoothly trading off computational cost and accuracy on a wide range of tasks, and outperforms the state-of-the-art S1 method for length control. Furthermore, we uncover an unexpected short chain-of-thought capability in models trained with LCPO. Specifically, using LCPO we derive Short Reasoning Models (SRMs), that exhibit similar reasoning patterns as full-length reasoning models, but can generate CoT lengths comparable to non-reasoning models. They demonstrate significant performance gains, for instance, our 1.5B L1 model surpasses GPT-4o at equal reasoning lengths. Overall, LCPO enables precise control over reasoning length, allowing for fine-grained allocation of test-time compute and accuracy. We release code and models at https://www.cmu-l3.github.io/l1

## 04-042 | Free Process Rewards without Process Labels
- arXiv: 2412.01981  first public: 2024-12-02  latest: 2024-12-02  primary cat: cs.LG
- authors (9): Lifan Yuan; Wendi Li; Huayu Chen; Ganqu Cui; Ning Ding; Kaiyan Zhang ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- arXiv comment: Models and data are available at: https://github.com/lifan-yuan/ImplicitPRM
- URLs on first pages of PDF: https://github.com/lifan-yuan/ImplicitPRM
- pages: 16

ABSTRACT: Different from its counterpart outcome reward models (ORMs), which evaluate the entire responses, a process reward model (PRM) scores a reasoning trajectory step by step, providing denser and more fine grained rewards. However, training a PRM requires labels annotated at every intermediate step, presenting significant challenges for both manual and automatic data collection. This paper aims to address this challenge. Both theoretically and empirically, we show that an \textit{implicit PRM} can be obtained at no additional cost, by simply training an ORM on the cheaper response-level labels. The only assumption is to parameterize the outcome reward as the log-likelihood ratios of the policy and reference models, which can be optimized regardless of the specific choice of loss objectives. In experiments, we instantiate our implicit PRMs with various objectives and evaluate their performance on MATH. We show that our implicit PRM outperforms a strong MCTS-based baseline \textit{á la} Math-Shepherd using less than $1/38$ of the training data. Its performance can be further improved with majority voting. We further find that scaling up instructions and responses benefits our implicit PRM, and the latter brings a larger gain. Particularly, we find that our implicit PRM, when instantiated with the cross-entropy (CE) loss, is more data-efficient and can keep improving generation models even when trained with only one response per instruction, the setup that suffers from extreme data scarcity and imbalance. Further, instructions should be relevant to downstream tasks while the diversity of responses does not bring gains. Surprisingly, training on extra Math-Shepherd step labels brings no further improvements to our implicit PRM trained on only outcome data. We hope that our work will encourage a rethinking of PRM training approaches and contribute to making training PRMs more accessible.

## 04-043 | Spurious Rewards: Rethinking Training Signals in RLVR
- arXiv: 2506.10947  first public: 2025-06-12  latest: 2026-02-25  primary cat: cs.AI
- authors (14): Rulin Shao; Shuyue Stella Li; Rui Xin; Scott Geng; Yiping Wang; Sewoong Oh ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- pages: 41

ABSTRACT: We show that reinforcement learning with verifiable rewards (RLVR) can elicit strong mathematical reasoning in certain language models even with spurious rewards that have little, no, or even negative correlation with the correct answer. For example, RLVR training with GRPO improves MATH-500 performance for Qwen2.5-Math-7B by 21.4 percentage points using randomly assigned rewards, nearly matching the 29.1-point gain from ground-truth rewards. To explain this counterintuitive observation, we show that GRPO exhibits a clipping bias from the clip term, which can amplify high-prior behaviors learned during pretraining even without informative rewards. As a case study, we identify one such behavior in Qwen2.5-Math models, which we call code reasoning -- reasoning in code without actual code execution; code-reasoning frequency increases from 65 percent to over 90 percent with spurious rewards. However, the presence of such amplifiable behaviors is highly model-dependent. In practice, spurious rewards that are effective for Qwen models often fail to produce gains for other model families, such as Llama3 or OLMo2. Our results highlight the importance of validating RL methods across diverse models rather than relying on a single de facto choice: large gains can arise on Qwen models even from random rewards that do not reflect genuine capability improvements.

## 04-044 | Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad
- arXiv: 2503.21934  first public: 2025-03-27  latest: 2025-09-04  primary cat: cs.CL
- authors (8): Ivo Petrov; Jasper Dekoninck; Lyuben Baltadzhiev; Maria Drencheva; Kristian Minchev; Mislav Balunović ...
- seed subtopic: 数学推理; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/eth-sri/matharena
- pages: 14

ABSTRACT: Recent math benchmarks for large language models (LLMs) such as MathArena indicate that state-of-the-art reasoning models achieve impressive performance on mathematical competitions like AIME, with the leading model, Gemini-2.5-Pro, achieving scores comparable to top human competitors. However, these benchmarks evaluate models solely based on final numerical answers, neglecting rigorous reasoning and proof generation which are essential for real-world mathematical tasks. To address this, we introduce a comprehensive evaluation of full-solution reasoning for challenging mathematical problems. Using expert human annotators, we evaluated several state-of-the-art reasoning models on the six problems from the 2025 USAMO within hours of their release. Our results reveal that all tested models struggled significantly: only Gemini-2.5-Pro achieves a non-trivial score of 25%, while all other models achieve less than 5%. Through detailed analysis of reasoning traces, we identify the most common failure modes and find several unwanted artifacts arising from the optimization strategies employed during model training. Overall, our results suggest that current LLMs are inadequate for rigorous mathematical reasoning tasks, highlighting the need for substantial improvements in reasoning and proof generation capabilities.

## 04-045 | Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach
- arXiv: 2502.05171  first public: 2025-02-07  latest: 2025-02-17  primary cat: cs.LG
- authors (9): Jonas Geiping; Sean McLeish; Neel Jain; John Kirchenbauer; Siddharth Singh; Brian R. Bartoldson ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: ['01']
- arXiv comment: The model is available at https://huggingface.co/tomg-group-umd/huginn-0125. Code and data recipe can be found at https://github.com/seal-rg/recurrent-pretraining
- pages: 37

ABSTRACT: We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space. Our model works by iterating a recurrent block, thereby unrolling to arbitrary depth at test-time. This stands in contrast to mainstream reasoning models that scale up compute by producing more tokens. Unlike approaches based on chain-of-thought, our approach does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words. We scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens. We show that the resulting model can improve its performance on reasoning benchmarks, sometimes dramatically, up to a computation load equivalent to 50 billion parameters.

## 04-046 | Process Reinforcement through Implicit Rewards
- arXiv: 2502.01456  first public: 2025-02-03  latest: 2025-09-26  primary cat: cs.LG
- authors (25): Ganqu Cui; Lifan Yuan; Zefan Wang; Hanbin Wang; Yuchen Zhang; Jiacheng Chen ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- arXiv comment: 24 pages. Model&Code&Data available at https://github.com/PRIME-RL/PRIME
- pages: 24

ABSTRACT: Dense process rewards have proven a more effective alternative to the sparse outcome-level rewards in the inference-time scaling of large language models (LLMs), particularly in tasks requiring complex multi-step reasoning. While dense rewards also offer an appealing choice for the reinforcement learning (RL) of LLMs since their fine-grained rewards have the potential to address some inherent issues of outcome rewards, such as training efficiency and credit assignment, this potential remains largely unrealized. This can be primarily attributed to the challenges of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive, making them particularly vulnerable to reward hacking. To address these challenges, we propose PRIME (Process Reinforcement through IMplicit rEwards), which enables online PRM updates using only policy rollouts and outcome labels through implict process rewards. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phrase that existing approaches require, substantially reducing the development overhead. We demonstrate PRIME's effectiveness on competitional math and coding. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across several key reasoning benchmarks over the SFT model. Notably, our resulting model, Eurus-2-7B-PRIME, surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks with 10% of its training data.

## 04-047 | The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models
- arXiv: 2505.22617  first public: 2025-05-28  latest: 2025-05-28  primary cat: cs.LG
- authors (17): Ganqu Cui; Yuchen Zhang; Jiacheng Chen; Lifan Yuan; Zhi Wang; Yuxin Zuo ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/PRIME-RL/Entropy-Mechanism-of-RL
- pages: 22

ABSTRACT: This paper aims to overcome a major obstacle in scaling RL for reasoning with LLMs, namely the collapse of policy entropy. Such phenomenon is consistently observed across vast RL runs without entropy intervention, where the policy entropy dropped sharply at the early training stage, this diminished exploratory ability is always accompanied with the saturation of policy performance. In practice, we establish a transformation equation R=-a*e^H+b between entropy H and downstream performance R. This empirical law strongly indicates that, the policy performance is traded from policy entropy, thus bottlenecked by its exhaustion, and the ceiling is fully predictable H=0, R=-a+b. Our finding necessitates entropy management for continuous exploration toward scaling compute for RL. To this end, we investigate entropy dynamics both theoretically and empirically. Our derivation highlights that, the change in policy entropy is driven by the covariance between action probability and the change in logits, which is proportional to its advantage when using Policy Gradient-like algorithms. Empirical study shows that, the values of covariance term and entropy differences matched exactly, supporting the theoretical conclusion. Moreover, the covariance term stays mostly positive throughout training, further explaining why policy entropy would decrease monotonically. Through understanding the mechanism behind entropy dynamics, we motivate to control entropy by restricting the update of high-covariance tokens. Specifically, we propose two simple yet effective techniques, namely Clip-Cov and KL-Cov, which clip and apply KL penalty to tokens with high covariances respectively. Experiments show that these methods encourage exploration, thus helping policy escape entropy collapse and achieve better downstream performance.

## 04-048 | OpenThoughts: Data Recipes for Reasoning Models
- arXiv: 2506.04178  first public: 2025-06-04  latest: 2025-06-05  primary cat: cs.LG
- authors (50): Etash Guha; Ryan Marten; Sedrick Keh; Negin Raoof; Georgios Smyrnis; Hritik Bansal ...
- seed subtopic: 数学推理; type: 原始研究; cross: []
- arXiv comment: https://www.openthoughts.ai/blog/ot3. arXiv admin note: text overlap with arXiv:2505.23754 by other authors
- pages: 72

ABSTRACT: Reasoning models have made rapid progress on many benchmarks involving math, code, and science. Yet, there are still many open questions about the best training recipes for reasoning since state-of-the-art models often rely on proprietary datasets with little to no public information available. To address this, the goal of the OpenThoughts project is to create open-source datasets for training reasoning models. After initial explorations, our OpenThoughts2-1M dataset led to OpenThinker2-32B, the first model trained on public reasoning data to match DeepSeek-R1-Distill-32B on standard reasoning benchmarks such as AIME and LiveCodeBench. We then improve our dataset further by systematically investigating each step of our data generation pipeline with 1,000+ controlled experiments, which led to OpenThoughts3. Scaling the pipeline to 1.2M examples and using QwQ-32B as teacher yields our OpenThoughts3-7B model, which achieves state-of-the-art results: 53% on AIME 2025, 51% on LiveCodeBench 06/24-01/25, and 54% on GPQA Diamond - improvements of 15.3, 17.2, and 20.5 percentage points compared to the DeepSeek-R1-Distill-Qwen-7B. All of our datasets and models are available on https://openthoughts.ai.

## 04-049 | Training Large Language Models to Reason in a Continuous Latent Space
- arXiv: 2412.06769  first public: 2024-12-09  latest: 2026-08-23  primary cat: cs.CL
- authors (7): Shibo Hao; Sainbayar Sukhbaatar; DiJia Su; Xian Li; Zhiting Hu; Jason Weston ...
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- arXiv comment: Accepted to COLM 2025
- URLs on first pages of PDF: https://github.com/facebookresearch/coconut
- pages: 18

ABSTRACT: Large language models (LLMs) are typically constrained to reason in the language space, where they express the reasoning process through a chain-of-thought (CoT) to solve complex problems. However, the language space may not always be optimal for reasoning. Most word tokens primarily ensure textual coherence and are not essential for reasoning, while some critical tokens require complex planning and pose challenges to LLMs. To explore the potential of reasoning beyond language, we introduce a new paradigm called Coconut (Chain of Continuous Thought). Coconut utilizes the last hidden state of the LLM as a representation of the reasoning state, termed "continuous thought." Instead of decoding this state into words, we feed it back to the model as the next input embedding directly in the continuous space. This latent reasoning paradigm enables an advanced reasoning pattern, where continuous thoughts can encode multiple alternative next steps, allowing the model to perform a breadth-first search (BFS) rather than committing prematurely to a single deterministic path as in CoT. Coconut outperforms CoT on logical reasoning tasks that require substantial search during planning and achieves a better trade-off between accuracy and efficiency.

## 04-050 | Process Reward Models That Think
- arXiv: 2504.16828  first public: 2025-04-23  latest: 2025-12-08  primary cat: cs.LG
- authors (8): Muhammad Khalifa; Rishabh Agarwal; Lajanugen Logeswaran; Jaekyeom Kim; Hao Peng; Moontae Lee ...
- seed subtopic: 过程监督; type: 原始研究; cross: []
- arXiv comment: Add new ablation and minor writing fixes
- URLs on first pages of PDF: https://github.com/mukhal/thinkprm
- pages: 30

ABSTRACT: Step-by-step verifiers -- also known as process reward models (PRMs) -- are a key ingredient for test-time scaling. PRMs require step-level supervision, making them expensive to train. This work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). We propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. Our approach capitalizes on the inherent reasoning abilities of long CoT models, and outperforms LLM-as-a-Judge and discriminative verifiers -- using only 1% of the process labels in PRM800K -- across several challenging benchmarks. Specifically, ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation on a subset of GPQA-Diamond and LiveCodeBench, our PRM surpasses discriminative verifiers trained on the full PRM800K by 8% and 4.5%, respectively. Lastly, under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. Our work highlights the value of generative, long CoT PRMs that can scale test-time compute for verification while requiring minimal supervision for training. Our code, data, and models are released at https://github.com/mukhal/thinkprm.

## 04-051 | Absolute Zero: Reinforced Self-play Reasoning with Zero Data
- arXiv: 2505.03335  first public: 2025-05-06  latest: 2025-10-16  primary cat: cs.LG
- authors (11): Andrew Zhao; Yiran Wu; Yang Yue; Tong Wu; Quentin Xu; Yang Yue ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- pages: 52

ABSTRACT: Reinforcement learning with verifiable rewards (RLVR) has shown promise in enhancing the reasoning capabilities of large language models by learning directly from outcome-based rewards. Recent RLVR works that operate under the zero setting avoid supervision in labeling the reasoning process, but still depend on manually curated collections of questions and answers for training. The scarcity of high-quality, human-produced examples raises concerns about the long-term scalability of relying on human supervision, a challenge already evident in the domain of language model pretraining. Furthermore, in a hypothetical future where AI surpasses human intelligence, tasks provided by humans may offer limited learning potential for a superintelligent system. To address these concerns, we propose a new RLVR paradigm called Absolute Zero, in which a single model learns to propose tasks that maximize its own learning progress and improves reasoning by solving them, without relying on any external data. Under this paradigm, we introduce the Absolute Zero Reasoner (AZR), a system that self-evolves its training curriculum and reasoning ability by using a code executor to both validate proposed code reasoning tasks and verify answers, serving as an unified source of verifiable reward to guide open-ended yet grounded learning. Despite being trained entirely without external data, AZR achieves overall SOTA performance on coding and mathematical reasoning tasks, outperforming existing zero-setting models that rely on tens of thousands of in-domain human-curated examples. Furthermore, we demonstrate that AZR can be effectively applied across different model scales and is compatible with various model classes.

## 04-052 | Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models
- arXiv: 2503.16419  first public: 2025-03-20  latest: 2025-08-21  primary cat: cs.CL
- authors (12): Yang Sui; Yu-Neng Chuang; Guanchu Wang; Jiamu Zhang; Tianyi Zhang; Jiayi Yuan ...
- seed subtopic: 测试时计算分配; type: 综述; cross: []
- arXiv comment: Accepted by TMLR 2025. Project website: https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs
- URLs on first pages of PDF: https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs
- pages: 33

ABSTRACT: Large Language Models (LLMs) have demonstrated remarkable capabilities in complex tasks. Recent advancements in Large Reasoning Models (LRMs), such as OpenAI o1 and DeepSeek-R1, have further improved performance in System-2 reasoning domains like mathematics and programming by harnessing supervised fine-tuning (SFT) and reinforcement learning (RL) techniques to enhance the Chain-of-Thought (CoT) reasoning. However, while longer CoT reasoning sequences improve performance, they also introduce significant computational overhead due to verbose and redundant outputs, known as the "overthinking phenomenon". In this paper, we provide the first structured survey to systematically investigate and explore the current progress toward achieving efficient reasoning in LLMs. Overall, relying on the inherent mechanism of LLMs, we categorize existing works into several key directions: (1) model-based efficient reasoning, which considers optimizing full-length reasoning models into more concise reasoning models or directly training efficient reasoning models; (2) reasoning output-based efficient reasoning, which aims to dynamically reduce reasoning steps and length during inference; (3) input prompts-based efficient reasoning, which seeks to enhance reasoning efficiency based on input prompt properties such as difficulty or length control. Additionally, we introduce the use of efficient data for training reasoning models, explore the reasoning capabilities of small language models, and discuss evaluation methods and benchmarking. Project website: https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs

## 04-053 | TTRL: Test-Time Reinforcement Learning
- arXiv: 2504.16084  first public: 2025-04-22  latest: 2025-06-30  primary cat: cs.CL
- authors (16): Yuxin Zuo; Kaiyan Zhang; Li Sheng; Shang Qu; Ganqu Cui; Xuekai Zhu ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/PRIME-RL/TTRL
- pages: 22

ABSTRACT: This paper investigates Reinforcement Learning (RL) on data without explicit labels for reasoning tasks in Large Language Models (LLMs). The core challenge of the problem is reward estimation during inference while not having access to ground-truth information. While this setting appears elusive, we find that common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training. In this work, we introduce Test-Time Reinforcement Learning (TTRL), a novel method for training LLMs using RL on unlabeled data. TTRL enables self-evolution of LLMs by utilizing the priors in the pre-trained models. Our experiments demonstrate that TTRL consistently improves performance across a variety of tasks and models. Notably, TTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. Furthermore, although TTRL is only supervised by the maj@n metric, TTRL has demonstrated performance to consistently surpass the upper limit of the initial model maj@n, and approach the performance of models trained directly on test data with ground-truth labels. Our experimental findings validate the general effectiveness of TTRL across various tasks and highlight TTRL's potential for broader tasks and domains. GitHub: https://github.com/PRIME-RL/TTRL

## 04-083 | The Art of Scaling Reinforcement Learning Compute for LLMs
- arXiv: 2510.13786  first public: 2025-10-15  latest: 2025-10-15  primary cat: cs.LG
- authors (9): Devvrit Khatri; Lovish Madaan; Rishabh Tiwari; Rachit Bansal; Sai Surya Duvvuri; Manzil Zaheer ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- arXiv comment: 28 pages, 20 figures
- pages: 28

ABSTRACT: Reinforcement learning (RL) has become central to training large language models (LLMs), yet the field lacks predictive scaling methodologies comparable to those established for pre-training. Despite rapidly rising compute budgets, there is no principled understanding of how to evaluate algorithmic improvements for scaling RL compute. We present the first large-scale systematic study, amounting to more than 400,000 GPU-hours, that defines a principled framework for analyzing and predicting RL scaling in LLMs. We fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. We observe: (1) Not all recipes yield similar asymptotic performance, (2) Details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote, and (3) Stable, scalable recipes follow predictable scaling trajectories, enabling extrapolation from smaller-scale runs. Combining these insights, we propose a best-practice recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours. Our work provides both a scientific framework for analyzing scaling in RL and a practical recipe that brings RL training closer to the predictability long achieved in pre-training.

## 04-084 | DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning
- arXiv: 2511.22570  first public: 2025-11-27  latest: 2025-11-27  primary cat: cs.AI
- authors (9): Zhihong Shao; Yuxiang Luo; Chengda Lu; Z. Z. Ren; Jiewen Hu; Tian Ye ...
- seed subtopic: 验证器; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/deepseek-ai/DeepSeek-Math-V2
- pages: 19

ABSTRACT: Large language models have made significant progress in mathematical reasoning, which serves as an important testbed for AI and could impact scientific research if further advanced. By scaling reasoning with reinforcement learning that rewards correct final answers, LLMs have improved from poor performance to saturating quantitative reasoning competitions like AIME and HMMT in one year. However, this approach faces fundamental limitations. Pursuing higher final answer accuracy doesn't address a key issue: correct answers don't guarantee correct reasoning. Moreover, many mathematical tasks like theorem proving require rigorous step-by-step derivation rather than numerical answers, making final answer rewards inapplicable. To push the limits of deep reasoning, we believe it is necessary to verify the comprehensiveness and rigor of mathematical reasoning. Self-verification is particularly important for scaling test-time compute, especially for open problems without known solutions. Towards self-verifiable mathematical reasoning, we investigate how to train an accurate and faithful LLM-based verifier for theorem proving. We then train a proof generator using the verifier as the reward model, and incentivize the generator to identify and resolve as many issues as possible in their own proofs before finalizing them. To maintain the generation-verification gap as the generator becomes stronger, we propose to scale verification compute to automatically label new hard-to-verify proofs, creating training data to further improve the verifier. Our resulting model, DeepSeekMath-V2, demonstrates strong theorem-proving capabilities, achieving gold-level scores on IMO 2025 and CMO 2024 and a near-perfect 118/120 on Putnam 2024 with scaled test-time compute.

## 04-085 | Deep Think with Confidence
- arXiv: 2508.15260  first public: 2025-08-21  latest: 2025-08-21  primary cat: cs.LG
- authors (4): Yichao Fu; Xuewei Wang; Yuandong Tian; Jiawei Zhao
- seed subtopic: 测试时计算分配; type: 原始研究; cross: []
- pages: 27

ABSTRACT: Large Language Models (LLMs) have shown great potential in reasoning tasks through test-time scaling methods like self-consistency with majority voting. However, this approach often leads to diminishing returns in accuracy and high computational overhead. To address these challenges, we introduce Deep Think with Confidence (DeepConf), a simple yet powerful method that enhances both reasoning efficiency and performance at test time. DeepConf leverages model-internal confidence signals to dynamically filter out low-quality reasoning traces during or after generation. It requires no additional model training or hyperparameter tuning and can be seamlessly integrated into existing serving frameworks. We evaluate DeepConf across a variety of reasoning tasks and the latest open-source models, including Qwen 3 and GPT-OSS series. Notably, on challenging benchmarks such as AIME 2025, DeepConf@512 achieves up to 99.9% accuracy and reduces generated tokens by up to 84.7% compared to full parallel thinking.

## 04-086 | Less is More: Recursive Reasoning with Tiny Networks
- arXiv: 2510.04871  first public: 2025-10-06  latest: 2025-10-06  primary cat: cs.LG
- authors (1): Alexia Jolicoeur-Martineau
- seed subtopic: 逻辑推理; type: 原始研究; cross: []
- pages: 12

ABSTRACT: Hierarchical Reasoning Model (HRM) is a novel approach using two small neural networks recursing at different frequencies. This biologically inspired method beats Large Language models (LLMs) on hard puzzle tasks such as Sudoku, Maze, and ARC-AGI while trained with small models (27M parameters) on small data (around 1000 examples). HRM holds great promise for solving hard problems with small networks, but it is not yet well understood and may be suboptimal. We propose Tiny Recursive Model (TRM), a much simpler recursive reasoning approach that achieves significantly higher generalization than HRM, while using a single tiny network with only 2 layers. With only 7M parameters, TRM obtains 45% test-accuracy on ARC-AGI-1 and 8% on ARC-AGI-2, higher than most LLMs (e.g., Deepseek R1, o3-mini, Gemini 2.5 Pro) with less than 0.01% of the parameters.

## 04-087 | Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs
- arXiv: 2506.14245  first public: 2025-06-17  latest: 2025-10-02  primary cat: cs.AI
- authors (12): Xumeng Wen; Zihan Liu; Shun Zheng; Shengyu Ye; Zhirong Wu; Yang Wang ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- arXiv comment: Update with more experiments
- pages: 31

ABSTRACT: Recent advancements in long chain-of-thought (CoT) reasoning, particularly through the Group Relative Policy Optimization algorithm used by DeepSeek-R1, have led to significant interest in the potential of Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs). While RLVR promises to improve reasoning by allowing models to learn from free exploration, there remains debate over whether it truly enhances reasoning abilities or simply boosts sampling efficiency. This paper systematically investigates the impact of RLVR on LLM reasoning. We revisit Pass@K experiments and demonstrate that RLVR can extend the reasoning boundary for both mathematical and coding tasks. This is supported by our introduction of a novel evaluation metric, CoT-Pass@K, which captures reasoning success by accounting for both the final answer and intermediate reasoning steps. Furthermore, we present a theoretical framework explaining RLVR's incentive mechanism, demonstrating how it can encourage correct reasoning even when rewards are based solely on answer correctness. Our analysis of RLVR's training dynamics reveals that it incentivizes correct reasoning early in the process, with substantial improvements in reasoning quality confirmed through extensive evaluations. These findings provide strong evidence of RLVR's potential to enhance LLM reasoning, offering valuable insights into its mechanisms and performance improvements.

## 04-088 | Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning
- arXiv: 2601.17223  first public: 2026-01-23  latest: 2026-01-23  primary cat: cs.CL
- authors (3): Massimiliano Pronesti; Anya Belz; Yufang Hou
- seed subtopic: 过程监督; type: 原始研究; cross: []
- pages: 16

ABSTRACT: Recent work on reinforcement learning with verifiable rewards (RLVR) has shown that large language models (LLMs) can be substantially improved using outcome-level verification signals, such as unit tests for code or exact-match checks for mathematics. In parallel, process supervision has long been explored as a way to shape the intermediate reasoning behaviour of LLMs, but existing approaches rely on neural judges to score chain-of-thought steps, leaving them vulnerable to opacity, bias, and reward hacking. To address this gap, we introduce Verifiable Process Reward Models (VPRMs), a reinforcement-learning framework in which intermediate reasoning steps are checked by deterministic, rule-based verifiers. We apply VPRMs to risk-of-bias assessment for medical evidence synthesis, a domain where guideline-defined criteria and rule-based decision paths enable programmatic verification of reasoning traces. Across multiple datasets, we find that VPRMs generate reasoning that adheres closely to domain rules and achieve substantially higher coherence between step-level decisions and final labels. Results show that VPRMs achieve up to 20% higher F1 than state-of-the-art models and 6.5% higher than verifiable outcome rewards, with substantial gains in evidence grounding and logical coherence.

## 04-091 | On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation
- arXiv: 2603.22117  first public: 2026-03-23  latest: 2026-03-23  primary cat: cs.LG
- authors (13): Kexin Huang; Haoming Meng; Junkang Wu; Jinda Lu; Chiyu Ma; Ziqian Chen ...
- seed subtopic: 推理强化学习; type: 原始研究; cross: []
- pages: 26

ABSTRACT: Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning capabilities of large language models. While existing analyses identify that RLVR-induced changes are sparse, they primarily focus on the \textbf{magnitude} of these updates, largely overlooking their \textbf{direction}. In this work, we argue that the direction of updates is a more critical lens for understanding RLVR's effects, which can be captured by the signed, token-level log probability difference $Δ\log p$ between the base and final RLVR models. Through statistical analysis and token-replacement interventions, we demonstrate that $Δ\log p$ more effectively identifies sparse, yet reasoning-critical updates than magnitude-based metrics (\eg divergence or entropy). Building on this insight, we propose two practical applications: (1) a \textit{test-time extrapolation} method that amplifies the policy along the learned $Δ\log p$ direction to improve reasoning accuracy without further training; (2) a \textit{training-time reweighting} method that focuses learning on low-probability (corresponding to higher $Δ\log p$) tokens, which improves reasoning performance across models and benchmarks. Our work establishes the direction of change as a key principle for analyzing and improving RLVR.

## 04-092 | Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling
- arXiv: 2605.13301  first public: 2026-05-13  latest: 2026-05-13  primary cat: cs.AI
- authors (28): Yafu Li; Runzhe Zhan; Haoran Zhang; Shunkai Zhang; Yizhuo Li; Zhilin Wang ...
- seed subtopic: 数学推理; type: 技术报告; cross: []
- arXiv comment: Technical Report. 77 pages
- pages: 77

ABSTRACT: Recent progress in reasoning models has substantially advanced long-horizon mathematical and scientific problem solving, with several systems now reaching gold-medal-level performance on International Mathematical Olympiad (IMO) and International Physics Olympiad (IPhO) problems. In this paper, we introduce a simple and unified recipe for converting a post-trained reasoning backbone into a rigorous olympiad-level solver. The recipe first uses a reverse-perplexity curriculum for SFT to instill rigorous proof-search and self-checking behaviors, then scales these behaviors through a two-stage RL pipeline that progresses from RL with verifiable rewards to more delicate proof-level RL, and finally boosts solving performance with test-time scaling. Applying this recipe, we train a 30B-A3B backbone with SFT on around 340K sub-8K-token trajectories followed by 200 RL steps. The resulting model, SU-01, supports stable reasoning on difficult problems with trajectories exceeding 100K tokens, while achieving gold-medal-level performance on mathematical and physical olympiad competitions, including IMO 2025/USAMO 2026 and IPhO 2024/2025. It also demonstrates strong generalization of scientific reasoning to domains beyond mathematics and physics.
