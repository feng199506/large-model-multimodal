# Brief for annotation: 05 检索增强与知识

## 05-001 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- arXiv: 2310.11511  first public: 2023-10-17  latest: 2023-10-17  primary cat: cs.CL
- authors (5): Akari Asai; Zeqiu Wu; Yizhong Wang; Avirup Sil; Hannaneh Hajishirzi
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: 30 pages, 2 figures, 12 tables
- URLs on first pages of PDF: https://selfrag.github.io/
- pages: 30

ABSTRACT: Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation. We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (Self-RAG) that enhances an LM's quality and factuality through retrieval and self-reflection. Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks. Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models.

## 05-002 | Corrective Retrieval Augmented Generation
- arXiv: 2401.15884  first public: 2024-01-29  latest: 2024-10-07  primary cat: cs.CL
- authors (4): Shi-Qi Yan; Jia-Chen Gu; Yun Zhu; Zhen-Hua Ling
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: Update results, add more analysis, and fix typos
- pages: 16

ABSTRACT: Large language models (LLMs) inevitably exhibit hallucinations since the accuracy of generated texts cannot be secured solely by the parametric knowledge they encapsulate. Although retrieval-augmented generation (RAG) is a practicable complement to LLMs, it relies heavily on the relevance of retrieved documents, raising concerns about how the model behaves if retrieval goes wrong. To this end, we propose the Corrective Retrieval Augmented Generation (CRAG) to improve the robustness of generation. Specifically, a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query, returning a confidence degree based on which different knowledge retrieval actions can be triggered. Since retrieval from static and limited corpora can only return sub-optimal documents, large-scale web searches are utilized as an extension for augmenting the retrieval results. Besides, a decompose-then-recompose algorithm is designed for retrieved documents to selectively focus on key information and filter out irrelevant information in them. CRAG is plug-and-play and can be seamlessly coupled with various RAG-based approaches. Experiments on four datasets covering short- and long-form generation tasks show that CRAG can significantly improve the performance of RAG-based approaches.

## 05-003 | Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs
- arXiv: 2312.05934  first public: 2023-12-10  latest: 2024-01-30  primary cat: cs.AI
- authors (4): Oded Ovadia; Menachem Brief; Moshik Mishaeli; Oren Elisha
- seed subtopic: 知识更新; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Large language models (LLMs) encapsulate a vast amount of factual information within their pre-trained weights, as evidenced by their ability to answer diverse questions across different domains. However, this knowledge is inherently limited, relying heavily on the characteristics of the training data. Consequently, using external datasets to incorporate new information or refine the capabilities of LLMs on previously seen information poses a significant challenge. In this study, we compare two common approaches: unsupervised fine-tuning and retrieval-augmented generation (RAG). We evaluate both approaches on a variety of knowledge-intensive tasks across different topics. Our findings reveal that while unsupervised fine-tuning offers some improvement, RAG consistently outperforms it, both for existing knowledge encountered during training and entirely new knowledge. Moreover, we find that LLMs struggle to learn new factual information through unsupervised fine-tuning, and that exposing them to numerous variations of the same fact during training could alleviate this problem.

## 05-005 | Enabling Large Language Models to Generate Text with Citations
- arXiv: 2305.14627  first public: 2023-05-24  latest: 2023-10-31  primary cat: cs.CL
- authors (4): Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen
- seed subtopic: 引用; type: 原始研究; cross: []
- arXiv comment: Accepted by EMNLP 2023. Code and data are available at https://github.com/princeton-nlp/ALCE
- pages: 24

ABSTRACT: Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. Existing work mainly relies on commercial search engines and human evaluation, making it challenging to reproduce and compare different modeling approaches. We propose ALCE, the first benchmark for Automatic LLMs' Citation Evaluation. ALCE collects a diverse set of questions and retrieval corpora and requires building end-to-end systems to retrieve supporting evidence and generate answers with citations. We develop automatic metrics along three dimensions -- fluency, correctness, and citation quality -- and demonstrate their strong correlation with human judgements. Our experiments with state-of-the-art LLMs and novel prompting strategies show that current systems have considerable room for improvement -- For example, on the ELI5 dataset, even the best models lack complete citation support 50% of the time. Our analyses further highlight promising future directions, including developing better retrievers, advancing long-context LLMs, and improving the ability to synthesize information from multiple sources.

## 05-006 | Locating and Editing Factual Associations in GPT
- arXiv: 2202.05262  first public: 2022-02-10  latest: 2023-01-13  primary cat: cs.CL
- authors (4): Kevin Meng; David Bau; Alex Andonian; Yonatan Belinkov
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2022. 35 pages, 30 figures. Code and data at https://rome.baulab.info/
- pages: 35

ABSTRACT: We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/

## 05-007 | Lost in the Middle: How Language Models Use Long Contexts
- arXiv: 2307.03172  first public: 2023-07-06  latest: 2023-11-20  primary cat: cs.CL
- authors (7): Nelson F. Liu; Kevin Lin; John Hewitt; Ashwin Paranjape; Michele Bevilacqua; Fabio Petroni ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: 18 pages, 16 figures. Accepted for publication in Transactions of the Association for Computational Linguistics (TACL), 2023
- pages: 18

ABSTRACT: While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models.

## 05-008 | From Local to Global: A Graph RAG Approach to Query-Focused Summarization
- arXiv: 2404.16130  first public: 2024-04-24  latest: 2025-02-19  primary cat: cs.CL
- authors (10): Darren Edge; Ha Trinh; Newman Cheng; Joshua Bradley; Alex Chao; Apurva Mody ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- pages: 26

ABSTRACT: The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections. However, RAG fails on global questions directed at an entire text corpus, such as "What are the main themes in the dataset?", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task. Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems. To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text. Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities. Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user. For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

## 05-009 | LightRAG: Simple and Fast Retrieval-Augmented Generation
- arXiv: 2410.05779  first public: 2024-10-08  latest: 2025-04-28  primary cat: cs.IR
- authors (5): Zirui Guo; Lianghao Xia; Yanhua Yu; Tu Ao; Chao Huang
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/HKUDS/LightRAG
- pages: 16

ABSTRACT: Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex inter-dependencies. To address these challenges, we propose LightRAG, which incorporates graph structures into text indexing and retrieval processes. This innovative framework employs a dual-level retrieval system that enhances comprehensive information retrieval from both low-level and high-level knowledge discovery. Additionally, the integration of graph structures with vector representations facilitates efficient retrieval of related entities and their relationships, significantly improving response times while maintaining contextual relevance. This capability is further enhanced by an incremental update algorithm that ensures the timely integration of new data, allowing the system to remain effective and responsive in rapidly changing data environments. Extensive experimental validation demonstrates considerable improvements in retrieval accuracy and efficiency compared to existing approaches. We have made our LightRAG open-source and available at the link: https://github.com/HKUDS/LightRAG

## 05-010 | Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?
- arXiv: 2405.05904  first public: 2024-05-09  latest: 2024-10-01  primary cat: cs.CL
- authors (7): Zorik Gekhman; Gal Yona; Roee Aharoni; Matan Eyal; Amir Feder; Roi Reichart ...
- seed subtopic: 知识更新; type: 原始研究; cross: ['12']
- arXiv comment: Accepted as a long paper at EMNLP 2024
- pages: 20

ABSTRACT: When large language models are aligned via supervised fine-tuning, they may encounter new factual information that was not acquired through pre-training. It is often conjectured that this can teach the model the behavior of hallucinating factually incorrect responses, as the model is trained to generate facts that are not grounded in its pre-existing knowledge. In this work, we study the impact of such exposure to new knowledge on the capability of the fine-tuned model to utilize its pre-existing knowledge. To this end, we design a controlled setup, focused on closed-book QA, where we vary the proportion of the fine-tuning examples that introduce new knowledge. We demonstrate that large language models struggle to acquire new factual knowledge through fine-tuning, as fine-tuning examples that introduce new knowledge are learned significantly slower than those consistent with the model's knowledge. However, we also find that as the examples with new knowledge are eventually learned, they linearly increase the model's tendency to hallucinate. Taken together, our results highlight the risk in introducing new factual knowledge through fine-tuning, and support the view that large language models mostly acquire factual knowledge through pre-training, whereas fine-tuning teaches them to use it more efficiently.

## 05-011 | Fine-tuning Language Models for Factuality
- arXiv: 2311.08401  first public: 2023-11-14  latest: 2023-11-14  primary cat: cs.CL
- authors (5): Katherine Tian; Eric Mitchell; Huaxiu Yao; Christopher D. Manning; Chelsea Finn
- seed subtopic: 事实性; type: 原始研究; cross: ['03']
- pages: 16

ABSTRACT: The fluency and creativity of large pre-trained language models (LLMs) have led to their widespread use, sometimes even as a replacement for traditional search engines. Yet language models are prone to making convincing but factually inaccurate claims, often referred to as 'hallucinations.' These errors can inadvertently spread misinformation or harmfully perpetuate misconceptions. Further, manual fact-checking of model responses is a time-consuming process, making human factuality labels expensive to acquire. In this work, we fine-tune language models to be more factual, without human labeling and targeting more open-ended generation settings than past work. We leverage two key recent innovations in NLP to do so. First, several recent works have proposed methods for judging the factuality of open-ended text by measuring consistency with an external knowledge base or simply a large model's confidence scores. Second, the direct preference optimization algorithm enables straightforward fine-tuning of language models on objectives other than supervised imitation, using a preference ranking over possible model responses. We show that learning from automatically generated factuality preference rankings, generated either through existing retrieval systems or our novel retrieval-free approach, significantly improves the factuality (percent of generated claims that are correct) of Llama-2 on held-out topics compared with RLHF or decoding strategies targeted at factuality. At 7B scale, compared to Llama-2-chat, we observe 58% and 40% reduction in factual error rate when generating biographies and answering medical questions, respectively.

## 05-012 | Training Language Models to Generate Text with Citations via Fine-grained Rewards
- arXiv: 2402.04315  first public: 2024-02-06  latest: 2024-08-30  primary cat: cs.CL
- authors (4): Chengyu Huang; Zeqiu Wu; Yushi Hu; Wenya Wang
- seed subtopic: 引用; type: 原始研究; cross: []
- arXiv comment: Accepted by ACL 2024
- pages: 24

ABSTRACT: While recent Large Language Models (LLMs) have proven useful in answering user queries, they are prone to hallucination, and their responses often lack credibility due to missing references to reliable sources. An intuitive solution to these issues would be to include in-text citations referring to external documents as evidence. While previous works have directly prompted LLMs to generate in-text citations, their performances are far from satisfactory, especially when it comes to smaller LLMs. In this work, we propose an effective training framework using fine-grained rewards to teach LLMs to generate highly supportive and relevant citations, while ensuring the correctness of their responses. We also conduct a systematic analysis of applying these fine-grained rewards to common LLM training strategies, demonstrating its advantage over conventional practices. We conduct extensive experiments on Question Answering (QA) datasets taken from the ALCE benchmark and validate the model's generalizability using EXPERTQA. On LLaMA-2-7B, the incorporation of fine-grained rewards achieves the best performance among the baselines, even surpassing that of GPT-3.5-turbo.

## 05-013 | A Comprehensive Study of Knowledge Editing for Large Language Models
- arXiv: 2401.01286  first public: 2024-01-02  latest: 2024-11-17  primary cat: cs.CL
- authors (22): Ningyu Zhang; Yunzhi Yao; Bozhong Tian; Peng Wang; Shumin Deng; Mengru Wang ...
- seed subtopic: 知识编辑; type: 综述; cross: []
- arXiv comment: Ongoing work (v5): we have updated the Table 4 results after optimizing certain methods (related to AdaLoRA) and fixing computational bugs (related to ROME and MEMIT) in the EasyEdit. These improvements have led to better results than before. We will continue updating this paper and welcome everyone to discuss and exchange ideas
- URLs on first pages of PDF: https://github.com/zjunlp/EasyEdit https://zjunlp.github.io/project/KnowEdit
- pages: 52

ABSTRACT: Large Language Models (LLMs) have shown extraordinary capabilities in understanding and generating text that closely mirrors human communication. However, a primary limitation lies in the significant computational demands during training, arising from their extensive parameterization. This challenge is further intensified by the dynamic nature of the world, necessitating frequent updates to LLMs to correct outdated information or integrate new knowledge, thereby ensuring their continued relevance. Note that many applications demand continual model adjustments post-training to address deficiencies or undesirable behaviors. There is an increasing interest in efficient, lightweight methods for on-the-fly model modifications. To this end, recent years have seen a burgeoning in the techniques of knowledge editing for LLMs, which aim to efficiently modify LLMs' behaviors within specific domains while preserving overall performance across various inputs. In this paper, we first define the knowledge editing problem and then provide a comprehensive review of cutting-edge approaches. Drawing inspiration from educational and cognitive research theories, we propose a unified categorization criterion that classifies knowledge editing methods into three groups: resorting to external knowledge, merging knowledge into the model, and editing intrinsic knowledge. Furthermore, we introduce a new benchmark, KnowEdit, for a comprehensive empirical evaluation of representative knowledge editing approaches. Additionally, we provide an in-depth analysis of knowledge location, which can give a deeper understanding of the knowledge structures inherent within LLMs. Finally, we discuss several potential applications of knowledge editing, outlining its broad and impactful implications.

## 05-014 | RULER: What's the Real Context Size of Your Long-Context Language Models?
- arXiv: 2404.06654  first public: 2024-04-09  latest: 2024-08-06  primary cat: cs.CL
- authors (8): Cheng-Ping Hsieh; Simeng Sun; Samuel Kriman; Shantanu Acharya; Dima Rekesh; Fei Jia ...
- seed subtopic: 长上下文; type: 原始研究; cross: ['12']
- arXiv comment: COLM 2024; Code is available at https://github.com/hsiehjackson/RULER
- URLs on first pages of PDF: https://github.com/hsiehjackson/RULER
- pages: 27

ABSTRACT: The needle-in-a-haystack (NIAH) test, which examines the ability to retrieve a piece of information (the "needle") from long distractor texts (the "haystack"), has been widely adopted to evaluate long-context language models (LMs). However, this simple retrieval-based test is indicative of only a superficial form of long-context understanding. To provide a more comprehensive evaluation of long-context LMs, we create a new synthetic benchmark RULER with flexible configurations for customized sequence length and task complexity. RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER. Despite achieving nearly perfect accuracy in the vanilla NIAH test, almost all models exhibit large performance drops as the context length increases. While these models all claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of 32K. Our analysis of Yi-34B, which supports context length of 200K, reveals large room for improvement as we increase input length and task complexity. We open source RULER to spur comprehensive evaluation of long-context LMs.

## 05-015 | HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models
- arXiv: 2405.14831  first public: 2024-05-23  latest: 2025-01-14  primary cat: cs.CL
- authors (5): Bernal Jiménez Gutiérrez; Yiheng Shu; Yu Gu; Michihiro Yasunaga; Yu Su
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024. Code and data: https://github.com/OSU-NLP-Group/HippoRAG
- URLs on first pages of PDF: https://github.com/OSU-NLP-Group/HippoRAG
- pages: 31

ABSTRACT: In order to thrive in hostile and ever-changing natural environments, mammalian brains evolved to store large amounts of knowledge about the world and continually integrate new information while avoiding catastrophic forgetting. Despite the impressive accomplishments, large language models (LLMs), even with retrieval-augmented generation (RAG), still struggle to efficiently and effectively integrate a large amount of new experiences after pre-training. In this work, we introduce HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory to enable deeper and more efficient knowledge integration over new experiences. HippoRAG synergistically orchestrates LLMs, knowledge graphs, and the Personalized PageRank algorithm to mimic the different roles of neocortex and hippocampus in human memory. We compare HippoRAG with existing RAG methods on multi-hop question answering and show that our method outperforms the state-of-the-art methods remarkably, by up to 20%. Single-step retrieval with HippoRAG achieves comparable or better performance than iterative retrieval like IRCoT while being 10-30 times cheaper and 6-13 times faster, and integrating HippoRAG into IRCoT brings further substantial gains. Finally, we show that our method can tackle new types of scenarios that are out of reach of existing methods. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

## 05-016 | Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity
- arXiv: 2403.14403  first public: 2024-03-21  latest: 2024-03-28  primary cat: cs.CL
- authors (5): Soyeong Jeong; Jinheon Baek; Sukmin Cho; Sung Ju Hwang; Jong C. Park
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: NAACL 2024
- pages: 15

ABSTRACT: Retrieval-Augmented Large Language Models (LLMs), which incorporate the non-parametric knowledge from external knowledge bases into LLMs, have emerged as a promising approach to enhancing response accuracy in several tasks, such as Question-Answering (QA). However, even though there are various approaches dealing with queries of different complexities, they either handle simple queries with unnecessary computational overhead or fail to adequately address complex multi-step queries; yet, not all user requests fall into only one of the simple or complex categories. In this work, we propose a novel adaptive QA framework, that can dynamically select the most suitable strategy for (retrieval-augmented) LLMs from the simplest to the most sophisticated ones based on the query complexity. Also, this selection process is operationalized with a classifier, which is a smaller LM trained to predict the complexity level of incoming queries with automatically collected labels, obtained from actual predicted outcomes of models and inherent inductive biases in datasets. This approach offers a balanced strategy, seamlessly adapting between the iterative and single-step retrieval-augmented LLMs, as well as the no-retrieval methods, in response to a range of query complexities. We validate our model on a set of open-domain QA datasets, covering multiple query complexities, and show that ours enhances the overall efficiency and accuracy of QA systems, compared to relevant baselines including the adaptive retrieval approaches. Code is available at: https://github.com/starsuzi/Adaptive-RAG.

## 05-017 | How Do Large Language Models Acquire Factual Knowledge During Pretraining?
- arXiv: 2406.11813  first public: 2024-06-17  latest: 2024-11-12  primary cat: cs.CL
- authors (7): Hoyeon Chang; Jinho Park; Seonghyeon Ye; Sohee Yang; Youngkyung Seo; Du-Seong Chang ...
- seed subtopic: 知识更新; type: 原始研究; cross: ['02']
- arXiv comment: Accepted at NeurIPS 2024
- URLs on first pages of PDF: https://github.com/kaistAI/factual-knowledge-acquisition/
- pages: 36

ABSTRACT: Despite the recent observation that large language models (LLMs) can store substantial factual knowledge, there is a limited understanding of the mechanisms of how they acquire factual knowledge through pretraining. This work addresses this gap by studying how LLMs acquire factual knowledge during pretraining. The findings reveal several important insights into the dynamics of factual knowledge acquisition during pretraining. First, counterintuitively, we observe that pretraining on more data shows no significant improvement in the model's capability to acquire and maintain factual knowledge. Next, there is a power-law relationship between training steps and forgetting of memorization and generalization of factual knowledge, and LLMs trained with duplicated training data exhibit faster forgetting. Third, training LLMs with larger batch sizes can enhance the models' robustness to forgetting. Overall, our observations suggest that factual knowledge acquisition in LLM pretraining occurs by progressively increasing the probability of factual knowledge presented in the pretraining data at each step. However, this increase is diluted by subsequent forgetting. Based on this interpretation, we demonstrate that we can provide plausible explanations for recently observed behaviors of LLMs, such as the poor performance of LLMs on long-tail knowledge and the benefits of deduplicating the pretraining corpus.

## 05-019 | LongCite: Enabling LLMs to Generate Fine-grained Citations in Long-context QA
- arXiv: 2409.02897  first public: 2024-09-04  latest: 2024-09-10  primary cat: cs.CL
- authors (11): Jiajie Zhang; Yushi Bai; Xin Lv; Wanjun Gu; Danqing Liu; Minhao Zou ...
- seed subtopic: 引用; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/THUDM/LongCite
- pages: 24

ABSTRACT: Though current long-context large language models (LLMs) have demonstrated impressive capacities in answering user questions based on extensive text, the lack of citations in their responses makes user verification difficult, leading to concerns about their trustworthiness due to their potential hallucinations. In this work, we aim to enable long-context LLMs to generate responses with fine-grained sentence-level citations, improving their faithfulness and verifiability. We first introduce LongBench-Cite, an automated benchmark for assessing current LLMs' performance in Long-Context Question Answering with Citations (LQAC), revealing considerable room for improvement. To this end, we propose CoF (Coarse to Fine), a novel pipeline that utilizes off-the-shelf LLMs to automatically generate long-context QA instances with precise sentence-level citations, and leverage this pipeline to construct LongCite-45k, a large-scale SFT dataset for LQAC. Finally, we train LongCite-8B and LongCite-9B using the LongCite-45k dataset, successfully enabling their generation of accurate responses and fine-grained sentence-level citations in a single output. The evaluation results on LongBench-Cite show that our trained models achieve state-of-the-art citation quality, surpassing advanced proprietary models including GPT-4o.

## 05-020 | AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models
- arXiv: 2410.02355  first public: 2024-10-03  latest: 2025-04-22  primary cat: cs.CL
- authors (8): Junfeng Fang; Houcheng Jiang; Kun Wang; Yunshan Ma; Shi Jie; Xiang Wang ...
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- journal_ref: 13th International Conference on Learning Representations (ICLR 2025 Oral)
- pages: 32

ABSTRACT: Large language models (LLMs) often exhibit hallucinations due to incorrect or outdated knowledge. Hence, model editing methods have emerged to enable targeted knowledge updates. To achieve this, a prevailing paradigm is the locating-then-editing approach, which first locates influential parameters and then edits them by introducing a perturbation. While effective, current studies have demonstrated that this perturbation inevitably disrupt the originally preserved knowledge within LLMs, especially in sequential editing scenarios. To address this, we introduce AlphaEdit, a novel solution that projects perturbation onto the null space of the preserved knowledge before applying it to the parameters. We theoretically prove that this projection ensures the output of post-edited LLMs remains unchanged when queried about the preserved knowledge, thereby mitigating the issue of disruption. Extensive experiments on various LLMs, including LLaMA3, GPT2-XL, and GPT-J, show that AlphaEdit boosts the performance of most locating-then-editing methods by an average of 36.7% with a single line of additional code for projection solely. Our code is available at: https://github.com/jianghoucheng/AlphaEdit.

## 05-021 | LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks
- arXiv: 2412.15204  first public: 2024-12-19  latest: 2025-01-03  primary cat: cs.CL
- authors (12): Yushi Bai; Shangqing Tu; Jiajie Zhang; Hao Peng; Xiaozhi Wang; Xin Lv ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: 26 pages, 13 figures
- pages: 26

ABSTRACT: This paper introduces LongBench v2, a benchmark designed to assess the ability of LLMs to handle long-context problems requiring deep understanding and reasoning across real-world multitasks. LongBench v2 consists of 503 challenging multiple-choice questions, with contexts ranging from 8k to 2M words, across six major task categories: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repository understanding, and long structured data understanding. To ensure the breadth and the practicality, we collect data from nearly 100 highly educated individuals with diverse professional backgrounds. We employ both automated and manual review processes to maintain high quality and difficulty, resulting in human experts achieving only 53.7% accuracy under a 15-minute time constraint. Our evaluation reveals that the best-performing model, when directly answers the questions, achieves only 50.1% accuracy. In contrast, the o1-preview model, which includes longer reasoning, achieves 57.7%, surpassing the human baseline by 4%. These results highlight the importance of enhanced reasoning ability and scaling inference-time compute to tackle the long-context challenges in LongBench v2. The project is available at https://longbench2.github.io.

## 05-022 | RAFT: Adapting Language Model to Domain Specific RAG
- arXiv: 2403.10131  first public: 2024-03-15  latest: 2024-06-05  primary cat: cs.CL
- authors (7): Tianjun Zhang; Shishir G. Patil; Naman Jain; Sheng Shen; Matei Zaharia; Ion Stoica ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['03']
- URLs on first pages of PDF: https://github.com/ShishirPatil/gorilla
- pages: 12

ABSTRACT: Pretraining Large Language Models (LLMs) on large corpora of textual data is now a standard paradigm. When using these LLMs for many downstream applications, it is common to additionally bake in new knowledge (e.g., time-critical news, or private domain knowledge) into the pretrained model either through RAG-based-prompting, or fine-tuning. However, the optimal methodology for the model to gain such new knowledge remains an open question. In this paper, we present Retrieval Augmented FineTuning (RAFT), a training recipe that improves the model's ability to answer questions in a "open-book" in-domain settings. In RAFT, given a question, and a set of retrieved documents, we train the model to ignore those documents that don't help in answering the question, which we call, distractor documents. RAFT accomplishes this by citing verbatim the right sequence from the relevant document that would help answer the question. This coupled with RAFT's chain-of-thought-style response helps improve the model's ability to reason. In domain-specific RAG, RAFT consistently improves the model's performance across PubMed, HotpotQA, and Gorilla datasets, presenting a post-training recipe to improve pre-trained LLMs to in-domain RAG. RAFT's code and demo are open-sourced at github.com/ShishirPatil/gorilla.

## 05-023 | Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning
- arXiv: 2503.09516  first public: 2025-03-12  latest: 2025-08-05  primary cat: cs.CL
- authors (8): Bowen Jin; Hansi Zeng; Zhenrui Yue; Jinsung Yoon; Sercan Arik; Dong Wang ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['04', '06']
- arXiv comment: 31 pages
- URLs on first pages of PDF: https://github.com/PeterGriffinJin/Search-R1
- pages: 31

ABSTRACT: Efficiently acquiring external knowledge and up-to-date information is essential for effective reasoning and text generation in large language models (LLMs). Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal, as the LLM might not fully possess the capability on how to interact optimally with the search engine. This paper introduces Search-R1, an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval. Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions, leveraging retrieved token masking for stable RL training and a simple outcome-based reward function. Experiments on seven question-answering datasets show that Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines under the same setting. This paper further provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning. The code and model checkpoints are available at https://github.com/PeterGriffinJin/Search-R1.

## 05-025 | The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input
- arXiv: 2501.03200  first public: 2025-01-06  latest: 2025-01-06  primary cat: cs.CL
- authors (26): Alon Jacovi; Andrew Wang; Chris Alberti; Connie Tao; Jon Lipovetz; Kate Olszewska ...
- seed subtopic: 事实性; type: 原始研究; cross: []
- pages: 16

ABSTRACT: We introduce FACTS Grounding, an online leaderboard and associated benchmark that evaluates language models' ability to generate text that is factually accurate with respect to given context in the user prompt. In our benchmark, each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request. Models are evaluated using automated judge models in two phases: (1) responses are disqualified if they do not fulfill the user request; (2) they are judged as accurate if the response is fully grounded in the provided document. The automated judge models were comprehensively evaluated against a held-out test-set to pick the best prompt template, and the final factuality score is an aggregate of multiple judge models to mitigate evaluation bias. The FACTS Grounding leaderboard will be actively maintained over time, and contains both public and private splits to allow for external participation while guarding the integrity of the leaderboard. It can be found at https://www.kaggle.com/facts-leaderboard.

## 05-026 | Effective Large Language Model Adaptation for Improved Grounding and Citation Generation
- arXiv: 2311.09533  first public: 2023-11-16  latest: 2024-04-02  primary cat: cs.CL
- authors (4): Xi Ye; Ruoxi Sun; Sercan Ö. Arik; Tomas Pfister
- seed subtopic: 引用; type: 原始研究; cross: []
- arXiv comment: NAACL 2024
- pages: 15

ABSTRACT: Large language models (LLMs) have achieved remarkable advancements in natural language understanding and generation. However, one major issue towards their widespread deployment in the real world is that they can generate "hallucinated" answers that are not factual. Towards this end, this paper focuses on improving LLMs by grounding their responses in retrieved passages and by providing citations. We propose a new framework, AGREE, Adaptation for GRounding EnhancEment, that improves the grounding from a holistic perspective. Our framework tunes LLMs to selfground the claims in their responses and provide accurate citations to retrieved documents. This tuning on top of the pre-trained LLMs requires well-grounded responses (with citations) for paired queries, for which we introduce a method that can automatically construct such data from unlabeled queries. The selfgrounding capability of tuned LLMs further grants them a test-time adaptation (TTA) capability that can actively retrieve passages to support the claims that have not been grounded, which iteratively improves the responses of LLMs. Across five datasets and two LLMs, our results show that the proposed tuningbased AGREE framework generates superior grounded responses with more accurate citations compared to prompting-based approaches and post-hoc citing-based approaches

## 05-027 | WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models
- arXiv: 2405.14768  first public: 2024-05-23  latest: 2024-12-19  primary cat: cs.CL
- authors (9): Peng Wang; Zexi Li; Ningyu Zhang; Ziwen Xu; Yunzhi Yao; Yong Jiang ...
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024
- URLs on first pages of PDF: https://github.com/zjunlp/EasyEdit
- pages: 28

ABSTRACT: Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides in memories is a fundamental question for model editing. In this paper, we find that editing either long-term memory (direct model parameters) or working memory (non-parametric knowledge of neural network activations/representations by retrieval) will result in an impossible triangle -- reliability, generalization, and locality can not be realized together in the lifelong editing settings. For long-term memory, directly editing the parameters will cause conflicts with irrelevant pretrained knowledge or previous edits (poor reliability and locality). For working memory, retrieval-based activations can hardly make the model understand the edits and generalize (poor generalization). Therefore, we propose WISE to bridge the gap between memories. In WISE, we design a dual parametric memory scheme, which consists of the main memory for the pretrained knowledge and a side memory for the edited knowledge. We only edit the knowledge in the side memory and train a router to decide which memory to go through when given a query. For continual editing, we devise a knowledge-sharding mechanism where different sets of edits reside in distinct subspaces of parameters, and are subsequently merged into a shared memory without conflicts. Extensive experiments show that WISE can outperform previous model editing methods and overcome the impossible triangle under lifelong model editing of question answering, hallucination, and out-of-distribution settings across trending LLM architectures, e.g., GPT, LLaMA, and Mistral. Code is available at https://github.com/zjunlp/EasyEdit.

## 05-028 | HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly
- arXiv: 2410.02694  first public: 2024-10-03  latest: 2025-03-06  primary cat: cs.CL
- authors (8): Howard Yen; Tianyu Gao; Minmin Hou; Ke Ding; Daniel Fleischer; Peter Izsak ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: ICLR 2025. Project page: https://princeton-nlp.github.io/HELMET/
- URLs on first pages of PDF: https://github.com/princeton-nlp/HELMET https://princeton-nlp.github.io/HELMET
- pages: 52

ABSTRACT: Many benchmarks exist for evaluating long-context language models (LCLMs), yet developers often rely on synthetic tasks such as needle-in-a-haystack (NIAH) or an arbitrary subset of tasks. However, it remains unclear whether these benchmarks reflect the diverse downstream applications of LCLMs, and such inconsistencies further complicate model comparison. We investigate the underlying reasons behind these practices and find that existing benchmarks often provide noisy signals due to limited coverage of applications, insufficient context lengths, unreliable metrics, and incompatibility with base models. In this work, we introduce HELMET (How to Evaluate Long-context Models Effectively and Thoroughly), a comprehensive benchmark encompassing seven diverse, application-centric categories. We also address several issues in previous benchmarks by adding controllable lengths up to 128K tokens, model-based evaluation for reliable metrics, and few-shot prompting for robustly evaluating base models. Consequently, we demonstrate that HELMET offers more reliable and consistent rankings of frontier LCLMs. Through a comprehensive study of 59 LCLMs, we find that (1) synthetic tasks like NIAH do not reliably predict downstream performance; (2) the diverse categories in HELMET exhibit distinct trends and low correlations with each other; and (3) while most LCLMs achieve perfect NIAH scores, open-source models significantly lag behind closed ones when tasks require full-context reasoning or following complex instructions -- the gap widens as length increases. Finally, we recommend using our RAG tasks for fast model development, as they are easy to run and better predict other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.

## 05-029 | Search-o1: Agentic Search-Enhanced Large Reasoning Models
- arXiv: 2501.05366  first public: 2025-01-09  latest: 2025-01-09  primary cat: cs.AI
- authors (8): Xiaoxi Li; Guanting Dong; Jiajie Jin; Yuyao Zhang; Yujia Zhou; Yutao Zhu ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['04']
- URLs on first pages of PDF: https://github.com/sunnynexus/Search-o1
- pages: 23

ABSTRACT: Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. However, their extended reasoning processes often suffer from knowledge insufficiency, leading to frequent uncertainties and potential errors. To address this limitation, we introduce \textbf{Search-o1}, a framework that enhances LRMs with an agentic retrieval-augmented generation (RAG) mechanism and a Reason-in-Documents module for refining retrieved documents. Search-o1 integrates an agentic search workflow into the reasoning process, enabling dynamic retrieval of external knowledge when LRMs encounter uncertain knowledge points. Additionally, due to the verbose nature of retrieved documents, we design a separate Reason-in-Documents module to deeply analyze the retrieved information before injecting it into the reasoning chain, minimizing noise and preserving coherent reasoning flow. Extensive experiments on complex reasoning tasks in science, mathematics, and coding, as well as six open-domain QA benchmarks, demonstrate the strong performance of Search-o1. This approach enhances the trustworthiness and applicability of LRMs in complex reasoning tasks, paving the way for more reliable and versatile intelligent systems. The code is available at \url{https://github.com/sunnynexus/Search-o1}.

## 05-030 | Chain-of-Retrieval Augmented Generation
- arXiv: 2501.14342  first public: 2025-01-24  latest: 2025-10-10  primary cat: cs.IR
- authors (6): Liang Wang; Haonan Chen; Nan Yang; Xiaolong Huang; Zhicheng Dou; Furu Wei
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['04']
- arXiv comment: Accepted by NeurIPS 2025
- URLs on first pages of PDF: https://github.com/microsoft/LMOps/tree/main/corag
- pages: 28

ABSTRACT: This paper introduces an approach for training o1-like RAG models that retrieve and reason over relevant information step by step before generating the final answer. Conventional RAG methods usually perform a single retrieval step before the generation process, which limits their effectiveness in addressing complex queries due to imperfect retrieval results. In contrast, our proposed method, CoRAG (Chain-of-Retrieval Augmented Generation), allows the model to dynamically reformulate the query based on the evolving state. To train CoRAG effectively, we utilize rejection sampling to automatically generate intermediate retrieval chains, thereby augmenting existing RAG datasets that only provide the correct final answer. At test time, we propose various decoding strategies to scale the model's test-time compute by controlling the length and number of sampled retrieval chains. Experimental results across multiple benchmarks validate the efficacy of CoRAG, particularly in multi-hop question answering tasks, where we observe more than 10 points improvement in EM score compared to strong baselines. On the KILT benchmark, CoRAG establishes a new state-of-the-art performance across a diverse range of knowledge-intensive tasks. Furthermore, we offer comprehensive analyses to understand the scaling behavior of CoRAG, laying the groundwork for future research aimed at developing factual and grounded foundation models.

## 05-031 | Self-Adapting Language Models
- arXiv: 2506.10943  first public: 2025-06-12  latest: 2025-09-18  primary cat: cs.LG
- authors (6): Adam Zweiger; Jyothish Pari; Han Guo; Ekin Akyürek; Yoon Kim; Pulkit Agrawal
- seed subtopic: 知识更新; type: 原始研究; cross: ['03']
- URLs on first pages of PDF: https://jyopari.github.io/posts/seal
- pages: 25

ABSTRACT: Large language models (LLMs) are powerful but static; they lack mechanisms to adapt their weights in response to new tasks, knowledge, or examples. We introduce Self-Adapting LLMs (SEAL), a framework that enables LLMs to self-adapt by generating their own finetuning data and update directives. Given a new input, the model produces a self-edit-a generation that may restructure the information in different ways, specify optimization hyperparameters, or invoke tools for data augmentation and gradient-based updates. Through supervised finetuning (SFT), these self-edits result in persistent weight updates, enabling lasting adaptation. To train the model to produce effective self-edits, we use a reinforcement learning loop with the downstream performance of the updated model as the reward signal. Unlike prior approaches that rely on separate adaptation modules or auxiliary networks, SEAL directly uses the model's own generation to control its adaptation process. Experiments on knowledge incorporation and few-shot generalization show that SEAL is a promising step toward language models capable of self-directed adaptation. Our website and code is available at https://jyopari.github.io/posts/seal.

## 05-032 | VERISCORE: Evaluating the factuality of verifiable claims in long-form text generation
- arXiv: 2406.19276  first public: 2024-06-27  latest: 2024-06-27  primary cat: cs.CL
- authors (3): Yixiao Song; Yekyung Kim; Mohit Iyyer
- seed subtopic: 事实性; type: 原始研究; cross: []
- pages: 27

ABSTRACT: Existing metrics for evaluating the factuality of long-form text, such as FACTSCORE (Min et al., 2023) and SAFE (Wei et al., 2024), decompose an input text into "atomic claims" and verify each against a knowledge base like Wikipedia. These metrics are not suitable for most generation tasks because they assume that every claim is verifiable (i.e., can plausibly be proven true or false). We address this issue with VERISCORE, a metric for diverse long-form generation tasks that contain both verifiable and unverifiable content. VERISCORE can be effectively implemented with either closed or fine-tuned open-weight language models, and human evaluation confirms that VERISCORE's extracted claims are more sensible than those from competing methods across eight different long-form tasks. We use VERISCORE to evaluate generations from 16 different models across multiple long-form tasks and find that while GPT-4o is the best-performing model overall, open-weight models such as Mixtral-8x22 are closing the gap. We show that an LM's VERISCORE on one task (e.g., biography generation) does not necessarily correlate to its VERISCORE on a different task (e.g., long-form QA), highlighting the need for expanding factuality evaluation across tasks with varying fact density.

## 05-033 | SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models
- arXiv: 2502.09604  first public: 2025-02-13  latest: 2025-06-15  primary cat: cs.CL
- authors (9): Yung-Sung Chuang; Benjamin Cohen-Wang; Shannon Zejiang Shen; Zhaofeng Wu; Hu Xu; Xi Victoria Lin ...
- seed subtopic: 引用; type: 原始研究; cross: []
- arXiv comment: ICML 2025 main conference paper. The source code is available at https://github.com/facebookresearch/SelfCite
- pages: 20

ABSTRACT: We introduce SelfCite, a novel self-supervised approach that aligns LLMs to generate high-quality, fine-grained, sentence-level citations for the statements in their generated responses. Instead of only relying on costly and labor-intensive annotations, SelfCite leverages a reward signal provided by the LLM itself through context ablation: If a citation is necessary, removing the cited text from the context should prevent the same response; if sufficient, retaining the cited text alone should preserve the same response. This reward can guide the inference-time best-of-N sampling strategy to improve citation quality significantly, as well as be used in preference optimization to directly fine-tune the models for generating better citations. The effectiveness of SelfCite is demonstrated by increasing citation F1 up to 5.3 points on the LongBench-Cite benchmark across five long-form question answering tasks. The source code is available at https://github.com/facebookresearch/SelfCite

## 05-034 | Model Editing at Scale leads to Gradual and Catastrophic Forgetting
- arXiv: 2401.07453  first public: 2024-01-15  latest: 2024-06-10  primary cat: cs.CL
- authors (3): Akshat Gupta; Anurag Rao; Gopala Anumanchipalli
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- arXiv comment: ACL 2024 Findings
- pages: 31

ABSTRACT: Editing knowledge in large language models is an attractive capability to have which allows us to correct incorrectly learnt facts during pre-training, as well as update the model with an ever-growing list of new facts. While existing model editing techniques have shown promise, they are usually evaluated using metrics for reliability, specificity and generalization over one or few edits. We argue that for model editing to have practical utility, we must be able to make multiple edits to the same model. With this in mind, we evaluate the current model editing methods at scale, focusing on two state of the art methods: ROME and MEMIT. We find that as the model is edited sequentially with multiple facts, it continually forgets previously edited facts and the ability to perform downstream tasks. This forgetting happens in two phases -- an initial gradual but progressive forgetting phase followed by abrupt or catastrophic forgetting phase. Both gradual and catastrophic forgetting limit the usefulness of model editing methods at scale -- the former making model editing less effective as multiple edits are made to the model while the latter caps the scalability of such model editing methods. Our analysis also highlights other key limitations of ROME and MEMIT at scale. With our work, we push for the development and evaluation of model editing methods keeping scalability in mind.

## 05-035 | NoLiMa: Long-Context Evaluation Beyond Literal Matching
- arXiv: 2502.05167  first public: 2025-02-07  latest: 2025-07-09  primary cat: cs.CL
- authors (7): Ali Modarressi; Hanieh Deilamsalehy; Franck Dernoncourt; Trung Bui; Ryan A. Rossi; Seunghyun Yoon ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2025
- URLs on first pages of PDF: https://github.com/adobe-
- pages: 17

ABSTRACT: Recent large language models (LLMs) support long contexts ranging from 128K to 1M tokens. A popular method for evaluating these capabilities is the needle-in-a-haystack (NIAH) test, which involves retrieving a "needle" (relevant information) from a "haystack" (long irrelevant context). Extensions of this approach include increasing distractors, fact chaining, and in-context reasoning. However, in these benchmarks, models can exploit existing literal matches between the needle and haystack to simplify the task. To address this, we introduce NoLiMa, a benchmark extending NIAH with a carefully designed needle set, where questions and needles have minimal lexical overlap, requiring models to infer latent associations to locate the needle within the haystack. We evaluate 13 popular LLMs that claim to support contexts of at least 128K tokens. While they perform well in short contexts (<1K), performance degrades significantly as context length increases. At 32K, for instance, 11 models drop below 50% of their strong short-length baselines. Even GPT-4o, one of the top-performing exceptions, experiences a reduction from an almost-perfect baseline of 99.3% to 69.7%. Our analysis suggests these declines stem from the increased difficulty the attention mechanism faces in longer contexts when literal matches are absent, making it harder to retrieve relevant information. Even models enhanced with reasoning capabilities or CoT prompting struggle to maintain performance in long contexts. We publicly release the dataset and evaluation code at https://github.com/adobe-research/NoLiMa.

## 05-036 | Retrieval-Augmented Generation for Large Language Models: A Survey
- arXiv: 2312.10997  first public: 2023-12-18  latest: 2024-03-27  primary cat: cs.CL
- authors (10): Yunfan Gao; Yun Xiong; Xinyu Gao; Kangxiang Jia; Jinliu Pan; Yuxi Bi ...
- seed subtopic: 检索增强生成; type: 综述; cross: []
- arXiv comment: Ongoing Work
- URLs on first pages of PDF: https://github.com/Tongji-KGLLM/
- pages: 21

ABSTRACT: Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

## 05-037 | Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG
- arXiv: 2501.09136  first public: 2025-01-15  latest: 2026-04-01  primary cat: cs.AI
- authors (5): Aditi Singh; Abul Ehtesham; Saket Kumar; Tala Talaei Khoei; Athanasios V. Vasilakos
- seed subtopic: 检索增强生成; type: 综述; cross: ['06']
- URLs on first pages of PDF: https://github.com/asinghcsu/AgenticRAG-Survey
- pages: 42

ABSTRACT: Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding. However, their reliance on static training data limits their ability to respond to dynamic, real-time queries, resulting in outdated or inaccurate outputs. Retrieval-Augmented Generation (RAG) has emerged as a solution, enhancing LLMs by integrating real-time data retrieval to provide contextually relevant and up-to-date responses. Despite its promise, traditional RAG systems are constrained by static workflows and lack the adaptability required for multi-step reasoning and complex task management. Agentic Retrieval-Augmented Generation (Agentic RAG) transcends these limitations by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns reflection, planning, tool use, and multi-agent collaboration to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows through operational structures ranging from sequential steps to adaptive collaboration. This integration enables Agentic RAG systems to deliver flexibility, scalability, and context-awareness across diverse applications. This paper presents an analytical survey of Agentic RAG systems. It traces the evolution of RAG paradigms, introduces a principled taxonomy of Agentic RAG architectures based on agent cardinality, control structure, autonomy, and knowledge representation, and provides a comparative analysis of design trade-offs across existing frameworks. The survey examines applications in healthcare, finance, education, and enterprise document processing, and distills practical lessons for system designers and practitioners. Finally, it identifies key open research challenges related to evaluation, coordination, memory management, efficiency, and governance, outlining directions for future research.

## 05-038 | How new data permeates LLM knowledge and how to dilute it
- arXiv: 2504.09522  first public: 2025-04-13  latest: 2025-04-13  primary cat: cs.CL
- authors (8): Chen Sun; Renat Aksitov; Andrey Zhmoginov; Nolan Andrew Miller; Max Vladymyrov; Ulrich Rueckert ...
- seed subtopic: 知识更新; type: 原始研究; cross: []
- URLs on first pages of PDF: https://sunchipsster1.github.io/projects/outlandish/
- pages: 35

ABSTRACT: Large language models learn and continually learn through the accumulation of gradient-based updates, but how individual pieces of new information affect existing knowledge, leading to both beneficial generalization and problematic hallucination, remains poorly understood. We demonstrate that when learning new information, LLMs exhibit a "priming" effect: learning a new fact can cause the model to inappropriately apply that knowledge in unrelated contexts. To systematically study this phenomenon, we introduce "Outlandish," a carefully curated dataset of 1320 diverse text samples designed to probe how new knowledge permeates through an LLM's existing knowledge base. Using this dataset, we show that the degree of priming after learning new information can be predicted by measuring the token probability of key words before learning. This relationship holds robustly across different model architectures (PALM-2, Gemma, Llama), sizes, and training stages. Finally, we develop two novel techniques to modulate how new knowledge affects existing model behavior: (1) a ``stepping-stone'' text augmentation strategy and (2) an ``ignore-k'' update pruning method. These approaches reduce undesirable priming effects by 50-95\% while preserving the model's ability to learn new information. Our findings provide both empirical insights into how LLMs learn and practical tools for improving the specificity of knowledge insertion in language models. Further materials: https://sunchipsster1.github.io/projects/outlandish/

## 05-039 | Factuality of Large Language Models: A Survey
- arXiv: 2402.02420  first public: 2024-02-04  latest: 2024-10-31  primary cat: cs.CL
- authors (7): Yuxia Wang; Minghan Wang; Muhammad Arslan Manzoor; Fei Liu; Georgi Georgiev; Rocktim Jyoti Das ...
- seed subtopic: 事实性; type: 综述; cross: []
- arXiv comment: 11 pages, 1 figure and 2 tables
- pages: 11

ABSTRACT: Large language models (LLMs), especially when instruction-tuned for chat, have become part of our daily lives, freeing people from the process of searching, extracting, and integrating information from multiple sources by offering a straightforward answer to a variety of questions in a single place. Unfortunately, in many cases, LLM responses are factually incorrect, which limits their applicability in real-world scenarios. As a result, research on evaluating and improving the factuality of LLMs has attracted a lot of attention recently. In this survey, we critically analyze existing work with the aim to identify the major challenges and their associated causes, pointing out to potential solutions for improving the factuality of LLMs, and analyzing the obstacles to automated factuality evaluation for open-ended text generation. We further offer an outlook on where future research should go.

## 05-040 | ContextCite: Attributing Model Generation to Context
- arXiv: 2409.00729  first public: 2024-09-01  latest: 2024-09-13  primary cat: cs.LG
- authors (4): Benjamin Cohen-Wang; Harshay Shah; Kristian Georgiev; Aleksander Madry
- seed subtopic: 引用; type: 原始研究; cross: ['12']
- URLs on first pages of PDF: https://github.com/MadryLab/context-cite
- pages: 42

ABSTRACT: How do language models use information provided as context when generating a response? Can we infer whether a particular generated statement is actually grounded in the context, a misinterpretation, or fabricated? To help answer these questions, we introduce the problem of context attribution: pinpointing the parts of the context (if any) that led a model to generate a particular statement. We then present ContextCite, a simple and scalable method for context attribution that can be applied on top of any existing language model. Finally, we showcase the utility of ContextCite through three applications: (1) helping verify generated statements (2) improving response quality by pruning the context and (3) detecting poisoning attacks. We provide code for ContextCite at https://github.com/MadryLab/context-cite.

## 05-041 | AnyEdit: Edit Any Knowledge Encoded in Language Models
- arXiv: 2502.05628  first public: 2025-02-08  latest: 2025-10-10  primary cat: cs.CL
- authors (8): Houcheng Jiang; Junfeng Fang; Ningyu Zhang; Guojun Ma; Mingyang Wan; Xiang Wang ...
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- pages: 24

ABSTRACT: Large language models (LLMs) often produce incorrect or outdated information, necessitating efficient and precise knowledge updates. Current model editing methods, however, struggle with long-form knowledge in diverse formats, such as poetry, code snippets, and mathematical derivations. These limitations arise from their reliance on editing a single token's hidden state, a limitation we term "efficacy barrier". To solve this, we propose AnyEdit, a new autoregressive editing paradigm. It decomposes long-form knowledge into sequential chunks and iteratively edits the key token in each chunk, ensuring consistent and accurate outputs. Theoretically, we ground AnyEdit in the Chain Rule of Mutual Information, showing its ability to update any knowledge within LLMs. Empirically, it outperforms strong baselines by 21.5% on benchmarks including UnKEBench, AKEW, and our new EditEverything dataset for long-form diverse-formatted knowledge. Additionally, AnyEdit serves as a plug-and-play framework, enabling current editing methods to update knowledge with arbitrary length and format, significantly advancing the scope and practicality of LLM knowledge editing.

## 05-042 | Can Long-Context Language Models Subsume Retrieval, RAG, SQL, and More?
- arXiv: 2406.13121  first public: 2024-06-19  latest: 2024-06-19  primary cat: cs.CL
- authors (19): Jinhyuk Lee; Anthony Chen; Zhuyun Dai; Dheeru Dua; Devendra Singh Sachan; Michael Boratko ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: 29 pages. Dataset available at https://github.com/google-deepmind/loft
- URLs on first pages of PDF: https://github.com/google-deepmind/loft
- pages: 29

ABSTRACT: Long-context language models (LCLMs) have the potential to revolutionize our approach to tasks traditionally reliant on external tools like retrieval systems or databases. Leveraging LCLMs' ability to natively ingest and process entire corpora of information offers numerous advantages. It enhances user-friendliness by eliminating the need for specialized knowledge of tools, provides robust end-to-end modeling that minimizes cascading errors in complex pipelines, and allows for the application of sophisticated prompting techniques across the entire system. To assess this paradigm shift, we introduce LOFT, a benchmark of real-world tasks requiring context up to millions of tokens designed to evaluate LCLMs' performance on in-context retrieval and reasoning. Our findings reveal LCLMs' surprising ability to rival state-of-the-art retrieval and RAG systems, despite never having been explicitly trained for these tasks. However, LCLMs still face challenges in areas like compositional reasoning that are required in SQL-like tasks. Notably, prompting strategies significantly influence performance, emphasizing the need for continued research as context lengths grow. Overall, LOFT provides a rigorous testing ground for LCLMs, showcasing their potential to supplant existing paradigms and tackle novel tasks as model capabilities scale.

## 05-043 | Improving Text Embeddings with Large Language Models
- arXiv: 2401.00368  first public: 2023-12-31  latest: 2024-05-31  primary cat: cs.CL
- authors (6): Liang Wang; Nan Yang; Xiaolong Huang; Linjun Yang; Rangan Majumder; Furu Wei
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: Accepted by ACL 2024
- pages: 20

ABSTRACT: In this paper, we introduce a novel and simple method for obtaining high-quality text embeddings using only synthetic data and less than 1k training steps. Unlike existing methods that often depend on multi-stage intermediate pre-training with billions of weakly-supervised text pairs, followed by fine-tuning with a few labeled datasets, our method does not require building complex training pipelines or relying on manually collected datasets that are often constrained by task diversity and language coverage. We leverage proprietary LLMs to generate diverse synthetic data for hundreds of thousands of text embedding tasks across 93 languages. We then fine-tune open-source decoder-only LLMs on the synthetic data using standard contrastive loss. Experiments demonstrate that our method achieves strong performance on highly competitive text embedding benchmarks without using any labeled data. Furthermore, when fine-tuned with a mixture of synthetic and labeled data, our model sets new state-of-the-art results on the BEIR and MTEB benchmarks.

## 05-044 | BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval
- arXiv: 2407.12883  first public: 2024-07-16  latest: 2025-03-26  primary cat: cs.CL
- authors (15): Hongjin Su; Howard Yen; Mengzhou Xia; Weijia Shi; Niklas Muennighoff; Han-yu Wang ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: 51 pages
- URLs on first pages of PDF: https://github.com/xlang-ai/BRIGHT
- pages: 51

ABSTRACT: Existing retrieval benchmarks primarily consist of information-seeking queries (e.g., aggregated questions from search engines) where keyword or semantic-based retrieval is usually sufficient. However, many complex real-world queries require in-depth reasoning to identify relevant documents that go beyond surface form matching. For example, finding documentation for a coding question requires understanding the logic and syntax of the functions involved. To better benchmark retrieval on such challenging queries, we introduce BRIGHT, the first text retrieval benchmark that requires intensive reasoning to retrieve relevant documents. Our dataset consists of 1,384 real-world queries spanning diverse domains, such as economics, psychology, mathematics, and coding. These queries are drawn from naturally occurring and carefully curated human data. Extensive evaluation reveals that even state-of-the-art retrieval models perform poorly on BRIGHT. The leading model on the MTEB leaderboard (Muennighoff et al., 2023) SFR-Embedding-Mistral (Meng et al., 2024), which achieves a score of 59.0 nDCG@10,1 produces a score of nDCG@10 of 18.3 on BRIGHT. We show that incorporating explicit reasoning about the query improves retrieval performance by up to 12.2 points. Moreover, incorporating retrieved documents from the top-performing retriever boosts question-answering performance. We believe that BRIGHT paves the way for future research on retrieval systems in more realistic and challenging settings.

## 05-045 | Knowledge Conflicts for LLMs: A Survey
- arXiv: 2403.08319  first public: 2024-03-13  latest: 2024-06-22  primary cat: cs.CL
- authors (7): Rongwu Xu; Zehan Qi; Zhijiang Guo; Cunxiang Wang; Hongru Wang; Yue Zhang ...
- seed subtopic: 知识更新; type: 综述; cross: []
- arXiv comment: Our GitHub repo is available at https://github.com/pillowsofwind/Knowledge-Conflicts-Survey
- URLs on first pages of PDF: https://github.com/pillowsofwind/
- pages: 27

ABSTRACT: This survey provides an in-depth analysis of knowledge conflicts for large language models (LLMs), highlighting the complex challenges they encounter when blending contextual and parametric knowledge. Our focus is on three categories of knowledge conflicts: context-memory, inter-context, and intra-memory conflict. These conflicts can significantly impact the trustworthiness and performance of LLMs, especially in real-world applications where noise and misinformation are common. By categorizing these conflicts, exploring the causes, examining the behaviors of LLMs under such conflicts, and reviewing available solutions, this survey aims to shed light on strategies for improving the robustness of LLMs, thereby serving as a valuable resource for advancing research in this evolving area.

## 05-046 | Learning to Reason for Factuality
- arXiv: 2508.05618  first public: 2025-08-07  latest: 2026-07-24  primary cat: cs.CL
- authors (8): Xilun Chen; Ilia Kulikov; Vincent-Pierre Berges; Barlas Oğuz; Rulin Shao; Gargi Ghosh ...
- seed subtopic: 事实性; type: 原始研究; cross: ['04']
- arXiv comment: ICML 2026
- URLs on first pages of PDF: https://github.com/facebookresearch/ScalableVeriScore https://github.com/facebookresearch/factual_reasoning https://huggingface.co/datasets/facebook/factual_reasoning
- pages: 21

ABSTRACT: Reasoning Large Language Models (R-LLMs) have significantly advanced complex reasoning tasks but often struggle with factuality, generating substantially more hallucinations than their non-reasoning counterparts on long-form factuality benchmarks. However, extending online Reinforcement Learning (RL), a key component in recent R-LLM advancements, to the long-form factuality setting poses several unique challenges due to the lack of reliable verification methods. Previous work has utilized automatic factuality evaluation frameworks such as FActScore to curate preference data in the offline RL setting, yet we find that directly leveraging such methods as the reward in online RL leads to reward hacking in multiple ways, such as producing less detailed or relevant responses. We propose a novel reward function that simultaneously considers the factual precision, response detail level, and answer relevance, and applies online RL to learn high quality factual reasoning. Evaluated on six long-form factuality benchmarks, our factual reasoning model achieves an average reduction of 23.1 percentage points in hallucination rate, a 23% increase in answer detail level, and no degradation in the overall response helpfulness.

## 05-047 | OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs
- arXiv: 2411.14199  first public: 2024-11-21  latest: 2024-11-21  primary cat: cs.CL
- authors (25): Akari Asai; Jacqueline He; Rulin Shao; Weijia Shi; Amanpreet Singh; Joseph Chee Chang ...
- seed subtopic: 引用; type: 原始研究; cross: []
- pages: 53

ABSTRACT: Scientific progress depends on researchers' ability to synthesize the growing body of literature. Can large language models (LMs) assist scientists in this task? We introduce OpenScholar, a specialized retrieval-augmented LM that answers scientific queries by identifying relevant passages from 45 million open-access papers and synthesizing citation-backed responses. To evaluate OpenScholar, we develop ScholarQABench, the first large-scale multi-domain benchmark for literature search, comprising 2,967 expert-written queries and 208 long-form answers across computer science, physics, neuroscience, and biomedicine. On ScholarQABench, OpenScholar-8B outperforms GPT-4o by 5% and PaperQA2 by 7% in correctness, despite being a smaller, open model. While GPT4o hallucinates citations 78 to 90% of the time, OpenScholar achieves citation accuracy on par with human experts. OpenScholar's datastore, retriever, and self-feedback inference loop also improves off-the-shelf LMs: for instance, OpenScholar-GPT4o improves GPT-4o's correctness by 12%. In human evaluations, experts preferred OpenScholar-8B and OpenScholar-GPT4o responses over expert-written ones 51% and 70% of the time, respectively, compared to GPT4o's 32%. We open-source all of our code, models, datastore, data and a public demo.

## 05-048 | The Mirage of Model Editing: Revisiting Evaluation in the Wild
- arXiv: 2502.11177  first public: 2025-02-16  latest: 2025-05-31  primary cat: cs.CL
- authors (8): Wanli Yang; Fei Sun; Jiajun Tan; Xinyu Ma; Qi Cao; Dawei Yin ...
- seed subtopic: 知识编辑; type: 原始研究; cross: ['12']
- arXiv comment: Accepted to ACL 2025 Main Conference (Camera Ready Version)
- URLs on first pages of PDF: https://github.com/W
- pages: 19

ABSTRACT: Despite near-perfect results reported in the literature, the effectiveness of model editing in real-world applications remains unclear. To bridge this gap, we introduce QAEdit, a new benchmark aligned with widely used question answering (QA) datasets, and WILD, a task-agnostic evaluation framework designed to better reflect real-world usage of model editing. Our single editing experiments show that current editing methods perform substantially worse than previously reported (38.5% vs. 96.8%). We demonstrate that it stems from issues in the synthetic evaluation practices of prior work. Among them, the most severe is the use of teacher forcing during testing, which leaks both content and length of the ground truth, leading to overestimated performance. Furthermore, we simulate practical deployment by sequential editing, revealing that current approaches fail drastically with only 1000 edits. This work calls for a shift in model editing research toward rigorous evaluation and the development of robust, scalable methods that can reliably update knowledge in LLMs for real-world use.

## 05-049 | Retrieval Head Mechanistically Explains Long-Context Factuality
- arXiv: 2404.15574  first public: 2024-04-24  latest: 2024-04-24  primary cat: cs.CL
- authors (5): Wenhao Wu; Yizhong Wang; Guangxuan Xiao; Hao Peng; Yao Fu
- seed subtopic: 长上下文; type: 原始研究; cross: ['12']
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/nightdessert/Retrieval_Head
- pages: 10

ABSTRACT: Despite the recent progress in long-context language models, it remains elusive how transformer-based models exhibit the capability to retrieve relevant information from arbitrary locations within the long context. This paper aims to address this question. Our systematic investigation across a wide spectrum of models reveals that a special type of attention heads are largely responsible for retrieving information, which we dub retrieval heads. We identify intriguing properties of retrieval heads:(1) universal: all the explored models with long-context capability have a set of retrieval heads; (2) sparse: only a small portion (less than 5\%) of the attention heads are retrieval. (3) intrinsic: retrieval heads already exist in models pretrained with short context. When extending the context length by continual pretraining, it is still the same set of heads that perform information retrieval. (4) dynamically activated: take Llama-2 7B for example, 12 retrieval heads always attend to the required information no matter how the context is changed. The rest of the retrieval heads are activated in different contexts. (5) causal: completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model's retrieval ability. We further show that retrieval heads strongly influence chain-of-thought (CoT) reasoning, where the model needs to frequently refer back the question and previously-generated context. Conversely, tasks where the model directly generates the answer using its intrinsic knowledge are less impacted by masking out retrieval heads. These observations collectively explain which internal part of the model seeks information from the input tokens. We believe our insights will foster future research on reducing hallucination, improving reasoning, and compressing the KV cache.

## 05-050 | ReasonIR: Training Retrievers for Reasoning Tasks
- arXiv: 2504.20595  first public: 2025-04-29  latest: 2025-04-29  primary cat: cs.AI
- authors (11): Rulin Shao; Rui Qiao; Varsha Kishore; Niklas Muennighoff; Xi Victoria Lin; Daniela Rus ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: Our code is released at \url{https://github.com/facebookresearch/ReasonIR}
- URLs on first pages of PDF: https://github.com/facebookresearch/ReasonIR https://huggingface.co/reasonir/ReasonIR-8B
- pages: 36

ABSTRACT: We present ReasonIR-8B, the first retriever specifically trained for general reasoning tasks. Existing retrievers have shown limited gains on reasoning tasks, in part because existing training datasets focus on short factual queries tied to documents that straightforwardly answer them. We develop a synthetic data generation pipeline that, for each document, our pipeline creates a challenging and relevant query, along with a plausibly related but ultimately unhelpful hard negative. By training on a mixture of our synthetic data and existing public data, ReasonIR-8B achieves a new state-of-the-art of 29.9 nDCG@10 without reranker and 36.9 nDCG@10 with reranker on BRIGHT, a widely-used reasoning-intensive information retrieval (IR) benchmark. When applied to RAG tasks, ReasonIR-8B improves MMLU and GPQA performance by 6.4% and 22.6% respectively, relative to the closed-book baseline, outperforming other retrievers and search engines. In addition, ReasonIR-8B uses test-time compute more effectively: on BRIGHT, its performance consistently increases with longer and more information-rich rewritten queries; it continues to outperform other retrievers when combined with an LLM reranker. Our training recipe is general and can be easily extended to future LLMs; to this end, we open-source our code, data, and model.

## 05-051 | ColPali: Efficient Document Retrieval with Vision Language Models
- arXiv: 2407.01449  first public: 2024-06-27  latest: 2025-02-28  primary cat: cs.IR
- authors (7): Manuel Faysse; Hugues Sibille; Tony Wu; Bilel Omrani; Gautier Viaud; Céline Hudelot ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['07']
- arXiv comment: Published as a conference paper at ICLR 2025
- URLs on first pages of PDF: https://huggingface.co/spaces/vidore/
- pages: 26

ABSTRACT: Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents -often through lengthy and brittle processes-, they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG). To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. We release models, data, code and benchmarks under open licenses at https://hf.co/vidore.

## 05-052 | ClashEval: Quantifying the tug-of-war between an LLM's internal prior and external evidence
- arXiv: 2404.10198  first public: 2024-04-16  latest: 2025-02-07  primary cat: cs.CL
- authors (3): Kevin Wu; Eric Wu; James Zou
- seed subtopic: 知识更新; type: 原始研究; cross: []
- arXiv comment: Revised June 9 2024
- URLs on first pages of PDF: https://github.com/kevinwu23/StanfordClashEval
- pages: 15

ABSTRACT: Retrieval augmented generation (RAG) is frequently used to mitigate hallucinations and provide up-to-date knowledge for large language models (LLMs). However, given that document retrieval is an imprecise task and sometimes results in erroneous or even harmful content being presented in context, this raises the question of how LLMs handle retrieved information: If the provided content is incorrect, does the model know to ignore it, or does it recapitulate the error? Conversely, when the model's initial response is incorrect, does it always know to use the retrieved information to correct itself, or does it insist on its wrong prior response? To answer this, we curate a dataset of over 1200 questions across six domains (e.g., drug dosages, Olympic records, locations) along with content relevant to answering each question. We further apply precise perturbations to the answers in the content that range from subtle to blatant errors. We benchmark six top-performing LLMs, including GPT-4o, on this dataset and find that LLMs are susceptible to adopting incorrect retrieved content, overriding their own correct prior knowledge over 60% of the time. However, the more unrealistic the retrieved content is (i.e. more deviated from truth), the less likely the model is to adopt it. Also, the less confident a model is in its initial response (via measuring token probabilities), the more likely it is to adopt the information in the retrieved content. We exploit this finding and demonstrate simple methods for improving model accuracy where there is conflicting retrieved content. Our results highlight a difficult task and benchmark for LLMs -- namely, their ability to correctly discern when it is wrong in light of correct retrieved content and to reject cases when the provided content is incorrect.

## 05-053 | Knowledge Updating? No More Model Editing! Just Selective Contextual Reasoning
- arXiv: 2503.05212  first public: 2025-03-07  latest: 2025-03-07  primary cat: cs.CL
- authors (3): Guoxiu He; Xin Song; Aixin Sun
- seed subtopic: 知识编辑; type: 原始研究; cross: []
- pages: 30

ABSTRACT: As real-world knowledge evolves, the information embedded within large language models (LLMs) can become outdated, inadequate, or erroneous. Model editing has emerged as a prominent approach for updating LLMs' knowledge with minimal computational costs and parameter changes. This approach typically identifies and adjusts specific model parameters associated with newly acquired knowledge. However, existing methods often underestimate the adverse effects that parameter modifications can have on broadly distributed knowledge. More critically, post-edit LLMs frequently struggle with multi-hop reasoning and continuous knowledge updates. Although various studies have discussed these shortcomings, there is a lack of comprehensive evaluation. In this paper, we provide an evaluation of ten model editing methods along four dimensions: reliability, generalization, locality, and portability. Results confirm that all ten popular model editing methods show significant shortcomings across multiple dimensions, suggesting model editing is less promising. We then propose a straightforward method called Selective Contextual Reasoning (SCR), for knowledge updating. SCR does not modify model parameters but harnesses LLM's inherent contextual reasoning capabilities utilizing the updated knowledge pieces. Under SCR, an LLM first assesses whether an incoming query falls within the scope of an external knowledge base. If it does, the relevant external knowledge texts are contextualized to enhance reasoning; otherwise, the query is answered directly. We evaluate SCR against the ten model editing methods on two counterfactual datasets with three backbone LLMs. Empirical results confirm the effectiveness and efficiency of contextual reasoning for knowledge updating.

## 05-054 | Make Your LLM Fully Utilize the Context
- arXiv: 2404.16811  first public: 2024-04-25  latest: 2024-04-26  primary cat: cs.CL
- authors (5): Shengnan An; Zexiong Ma; Zeqi Lin; Nanning Zheng; Jian-Guang Lou
- seed subtopic: 长上下文; type: 原始研究; cross: ['03']
- arXiv comment: 19 pages, 7 figures, 3 tables, 9 examples
- pages: 19

ABSTRACT: While many contemporary large language models (LLMs) can process lengthy input, they still struggle to fully utilize information within the long context, known as the lost-in-the-middle challenge. We hypothesize that it stems from insufficient explicit supervision during the long-context training, which fails to emphasize that any position in a long context can hold crucial information. Based on this intuition, our study presents information-intensive (IN2) training, a purely data-driven solution to overcome lost-in-the-middle. Specifically, IN2 training leverages a synthesized long-context question-answer dataset, where the answer requires (1) fine-grained information awareness on a short segment (~128 tokens) within a synthesized long context (4K-32K tokens), and (2) the integration and reasoning of information from two or more short segments. Through applying this information-intensive training on Mistral-7B, we present FILM-7B (FILl-in-the-Middle). To thoroughly assess the ability of FILM-7B for utilizing long contexts, we design three probing tasks that encompass various context styles (document, code, and structured-data context) and information retrieval patterns (forward, backward, and bi-directional retrieval). The probing results demonstrate that FILM-7B can robustly retrieve information from different positions in its 32K context window. Beyond these probing tasks, FILM-7B significantly improves the performance on real-world long-context tasks (e.g., 23.5->26.9 F1 score on NarrativeQA), while maintaining a comparable performance on short-context tasks (e.g., 59.3->59.2 accuracy on MMLU). Github Link: https://github.com/microsoft/FILM.

## 05-056 | Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation
- arXiv: 2409.12941  first public: 2024-09-19  latest: 2025-01-24  primary cat: cs.CL
- authors (7): Satyapriya Krishna; Kalpesh Krishna; Anhad Mohananey; Steven Schwarcz; Adam Stambler; Shyam Upadhyay ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: []
- arXiv comment: Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL), 2025
- URLs on first pages of PDF: https://huggingface.co/datasets/go
- pages: 15

ABSTRACT: Large Language Models (LLMs) have demonstrated significant performance improvements across various cognitive tasks. An emerging application is using LLMs to enhance retrieval-augmented generation (RAG) capabilities. These systems require LLMs to understand user queries, retrieve relevant information, and synthesize coherent and accurate responses. Given the increasing real-world deployment of such systems, comprehensive evaluation becomes crucial. To this end, we propose FRAMES (Factuality, Retrieval, And reasoning MEasurement Set), a high-quality evaluation dataset designed to test LLMs' ability to provide factual responses, assess retrieval capabilities, and evaluate the reasoning required to generate final answers. While previous work has provided datasets and benchmarks to evaluate these abilities in isolation, FRAMES offers a unified framework that provides a clearer picture of LLM performance in end-to-end RAG scenarios. Our dataset comprises challenging multi-hop questions that require the integration of information from multiple sources. We present baseline results demonstrating that even state-of-the-art LLMs struggle with this task, achieving 0.40 accuracy with no retrieval. The accuracy is significantly improved with our proposed multi-step retrieval pipeline, achieving an accuracy of 0.66 (>50% improvement). We hope our work will help bridge evaluation gaps and assist in developing more robust and capable RAG systems.

## 05-058 | Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG
- arXiv: 2410.05983  first public: 2024-10-08  latest: 2024-10-08  primary cat: cs.CL
- authors (4): Bowen Jin; Jinsung Yoon; Jiawei Han; Sercan O. Arik
- seed subtopic: 长上下文; type: 原始研究; cross: []
- arXiv comment: 34 pages
- pages: 34

ABSTRACT: Retrieval-augmented generation (RAG) empowers large language models (LLMs) to utilize external knowledge sources. The increasing capacity of LLMs to process longer input sequences opens up avenues for providing more retrieved information, to potentially enhance the quality of generated outputs. It is plausible to assume that a larger retrieval set would contain more relevant information (higher recall), that might result in improved performance. However, our empirical findings demonstrate that for many long-context LLMs, the quality of generated output initially improves first, but then subsequently declines as the number of retrieved passages increases. This paper investigates this phenomenon, identifying the detrimental impact of retrieved "hard negatives" as a key contributor. To mitigate this and enhance the robustness of long-context LLM-based RAG, we propose both training-free and training-based approaches. We first showcase the effectiveness of retrieval reordering as a simple yet powerful training-free optimization. Furthermore, we explore training-based methods, specifically RAG-specific implicit LLM fine-tuning and RAG-oriented fine-tuning with intermediate reasoning, demonstrating their capacity for substantial performance gains. Finally, we conduct a systematic analysis of design choices for these training-based methods, including data distribution, retriever selection, and training context length.

## 05-060 | Agentic-R: Learning to Retrieve for Agentic Search
- arXiv: 2601.11888  first public: 2026-01-17  latest: 2026-01-17  primary cat: cs.IR
- authors (7): Wenhan Liu; Xinyu Ma; Yutao Zhu; Yuchen Li; Daiting Shi; Dawei Yin ...
- seed subtopic: 检索增强生成; type: 原始研究; cross: ['06']
- URLs on first pages of PDF: https://huggingface.co/Qwen/Qwen2
- pages: 19

ABSTRACT: Agentic search has recently emerged as a powerful paradigm, where an agent interleaves multi-step reasoning with on-demand retrieval to solve complex questions. Despite its success, how to design a retriever for agentic search remains largely underexplored. Existing search agents typically rely on similarity-based retrievers, while similar passages are not always useful for final answer generation. In this paper, we propose a novel retriever training framework tailored for agentic search. Unlike retrievers designed for single-turn retrieval-augmented generation (RAG) that only rely on local passage utility, we propose to use both local query-passage relevance and global answer correctness to measure passage utility in a multi-turn agentic search. We further introduce an iterative training strategy, where the search agent and the retriever are optimized bidirectionally and iteratively. Different from RAG retrievers that are only trained once with fixed questions, our retriever is continuously improved using evolving and higher-quality queries from the agent. Extensive experiments on seven single-hop and multi-hop QA benchmarks demonstrate that our retriever, termed \ours{}, consistently outperforms strong baselines across different search agents. Our codes are available at: https://github.com/8421BCD/Agentic-R.

## 05-061 | LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark
- arXiv: 2601.02872  first public: 2026-01-06  latest: 2026-01-06  primary cat: cs.CL
- authors (7): Ziyang Chen; Xing Wu; Junlong Jia; Chaochen Gao; Qi Fu; Debing Zhang ...
- seed subtopic: 长上下文; type: 原始研究; cross: []
- pages: 28

ABSTRACT: The rapid expansion of context length in large language models (LLMs) has outpaced existing evaluation benchmarks. Current long-context benchmarks often trade off scalability and realism: synthetic tasks underrepresent real-world complexity, while fully manual annotation is costly to scale to extreme lengths and diverse scenarios. We present LongBench Pro, a more realistic and comprehensive bilingual benchmark of 1,500 naturally occurring long-context samples in English and Chinese spanning 11 primary tasks and 25 secondary tasks, with input lengths from 8k to 256k tokens. LongBench Pro supports fine-grained analysis with task-specific metrics and a multi-dimensional taxonomy of context requirement (full vs. partial dependency), length (six levels), and difficulty (four levels calibrated by model performance). To balance quality with scalability, we propose a Human-Model Collaborative Construction pipeline: frontier LLMs draft challenging questions and reference answers, along with design rationales and solution processes, to reduce the cost of expert verification. Experts then rigorously validate correctness and refine problematic cases. Evaluating 46 widely used long-context LLMs on LongBench Pro yields three findings: (1) long-context optimization contributes more to long-context comprehension than parameter scaling; (2) effective context length is typically shorter than the claimed context length, with pronounced cross-lingual misalignment; and (3) the "thinking" paradigm helps primarily models trained with native reasoning, while mixed-thinking designs offer a promising Pareto trade-off. In summary, LongBench Pro provides a robust testbed for advancing long-context understanding.

## 05-066 | FLAME: Factuality-Aware Alignment for Large Language Models
- arXiv: 2405.01525  first public: 2024-05-02  latest: 2024-05-02  primary cat: cs.CL
- authors (7): Sheng-Chieh Lin; Luyu Gao; Barlas Oguz; Wenhan Xiong; Jimmy Lin; Wen-tau Yih ...
- seed subtopic: 事实性; type: 原始研究; cross: ['03']
- pages: 17

ABSTRACT: Alignment is a standard procedure to fine-tune pre-trained large language models (LLMs) to follow natural language instructions and serve as helpful AI assistants. We have observed, however, that the conventional alignment process fails to enhance the factual accuracy of LLMs, and often leads to the generation of more false facts (i.e. hallucination). In this paper, we study how to make the LLM alignment process more factual, by first identifying factors that lead to hallucination in both alignment steps:\ supervised fine-tuning (SFT) and reinforcement learning (RL). In particular, we find that training the LLM on new knowledge or unfamiliar texts can encourage hallucination. This makes SFT less factual as it trains on human labeled data that may be novel to the LLM. Furthermore, reward functions used in standard RL can also encourage hallucination, because it guides the LLM to provide more helpful responses on a diverse set of instructions, often preferring longer and more detailed responses. Based on these observations, we propose factuality-aware alignment, comprised of factuality-aware SFT and factuality-aware RL through direct preference optimization. Experiments show that our proposed factuality-aware alignment guides LLMs to output more factual responses while maintaining instruction-following capability.

## 05-073 | Knowledge-Level Consistency Reinforcement Learning: Dual-Fact Alignment for Long-Form Factuality
- arXiv: 2509.23765  first public: 2025-09-28  latest: 2026-05-07  primary cat: cs.CL
- authors (8): Junliang Li; Yucheng Wang; Yan Chen; Yu Ran; Ruiqing Zhang; Jing Liu ...
- seed subtopic: 事实性; type: 原始研究; cross: ['04']
- arXiv comment: 32 pages
- URLs on first pages of PDF: https://github.com/ki-ljl/KLCF https://huggingface.co/collections/JunliangLi/klcf
- pages: 32

ABSTRACT: Hallucination in large language models (LLMs) during long-form generation remains difficult to address under existing reinforcement learning from human feedback (RLHF) frameworks, as their preference rewards often overlook the model's own knowledge boundaries. In this paper, we propose the $\textbf{K}$nowledge-$\textbf{L}$evel $\textbf{C}$onsistency Reinforcement Learning $\textbf{F}$ramework ($\textbf{KLCF}$), which re-examines this problem from a distribution alignment perspective. KLCF formalizes long-form factuality as a bidirectional distribution matching objective between the policy model's expressed knowledge distribution and the base model's parametric knowledge distribution: under the constraint that generation must not exceed the support set of the base knowledge, the objective maximizes coverage of high-probability facts, thereby jointly optimizing precision and recall. To achieve this, we design a Dual-Fact Alignment mechanism that approximates the recall term using a factual checklist constructed by sampling from the base model, and constrains hallucinations with a lightweight truthfulness reward model. Both components are jointly optimized and require no external retrieval throughout training. Experimental results demonstrate that KLCF consistently improves factuality metrics across multiple long-form benchmarks and model scales, effectively alleviating hallucination and over-conservatism while maintaining efficiency and scalability.
