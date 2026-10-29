# Brief for annotation: 02 预训练与数据

## 02-001 | Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research
- arXiv: 2402.00159  first public: 2024-01-31  latest: 2024-06-06  primary cat: cs.CL
- authors (36): Luca Soldaini; Rodney Kinney; Akshita Bhagia; Dustin Schwenk; David Atkinson; Russell Authur ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- arXiv comment: Accepted at ACL 2024; Dataset: https://hf.co/datasets/allenai/dolma; Code: https://github.com/allenai/dolma
- pages: 64

ABSTRACT: Information about pretraining corpora used to train the current best-performing language models is seldom discussed: commercial models rarely detail their data, and even open models are often released without accompanying training data or recipes to reproduce them. As a result, it is challenging to conduct and advance scientific research on language modeling, such as understanding how training data impacts model capabilities and limitations. To facilitate scientific research on language model pretraining, we curate and release Dolma, a three-trillion-token English corpus, built from a diverse mixture of web content, scientific papers, code, public-domain books, social media, and encyclopedic materials. We extensively document Dolma, including its design principles, details about its construction, and a summary of its contents. We present analyses and experimental results on intermediate states of Dolma to share what we have learned about important data curation practices. Finally, we open-source our data curation toolkit to enable reproduction of our work as well as support further research in large-scale data curation.

## 02-002 | The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale
- arXiv: 2406.17557  first public: 2024-06-25  latest: 2024-10-31  primary cat: cs.CL
- authors (8): Guilherme Penedo; Hynek Kydlíček; Loubna Ben allal; Anton Lozhkov; Margaret Mitchell; Colin Raffel ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/HuggingFaceFW/fineweb https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
- pages: 38

ABSTRACT: The performance of a large language model (LLM) depends heavily on the quality and size of its pretraining dataset. However, the pretraining datasets for state-of-the-art open LLMs like Llama 3 and Mixtral are not publicly available and very little is known about how they were created. In this work, we introduce FineWeb, a 15-trillion token dataset derived from 96 Common Crawl snapshots that produces better-performing LLMs than other open pretraining datasets. To advance the understanding of how best to curate high-quality pretraining datasets, we carefully document and ablate all of the design choices used in FineWeb, including in-depth investigations of deduplication and filtering strategies. In addition, we introduce FineWeb-Edu, a 1.3-trillion token collection of educational text filtered from FineWeb. LLMs pretrained on FineWeb-Edu exhibit dramatically better performance on knowledge- and reasoning-intensive benchmarks like MMLU and ARC. Along with our datasets, we publicly release our data curation codebase and all of the models trained during our ablation experiments.

## 02-003 | DataComp-LM: In search of the next generation of training sets for language models
- arXiv: 2406.11794  first public: 2024-06-17  latest: 2025-04-21  primary cat: cs.LG
- authors (59): Jeffrey Li; Alex Fang; Georgios Smyrnis; Maor Ivgi; Matt Jordan; Samir Gadre ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: Project page: https://www.datacomp.ai/dclm/
- pages: 89

ABSTRACT: We introduce DataComp for Language Models (DCLM), a testbed for controlled dataset experiments with the goal of improving language models. As part of DCLM, we provide a standardized corpus of 240T tokens extracted from Common Crawl, effective pretraining recipes based on the OpenLM framework, and a broad suite of 53 downstream evaluations. Participants in the DCLM benchmark can experiment with data curation strategies such as deduplication, filtering, and data mixing at model scales ranging from 412M to 7B parameters. As a baseline for DCLM, we conduct extensive experiments and find that model-based filtering is key to assembling a high-quality training set. The resulting dataset, DCLM-Baseline enables training a 7B parameter language model from scratch to 64% 5-shot accuracy on MMLU with 2.6T training tokens. Compared to MAP-Neo, the previous state-of-the-art in open-data language models, DCLM-Baseline represents a 6.6 percentage point improvement on MMLU while being trained with 40% less compute. Our baseline model is also comparable to Mistral-7B-v0.3 and Llama 3 8B on MMLU (63% & 66%), and performs similarly on an average of 53 natural language understanding tasks while being trained with 6.6x less compute than Llama 3 8B. Our results highlight the importance of dataset design for training language models and offer a starting point for further research on data curation.

## 02-004 | RedPajama: an Open Dataset for Training Large Language Models
- arXiv: 2411.12372  first public: 2024-11-19  latest: 2024-11-19  primary cat: cs.CL
- authors (19): Maurice Weber; Daniel Fu; Quentin Anthony; Yonatan Oren; Shane Adams; Anton Alexandrov ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- arXiv comment: 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks
- pages: 30

ABSTRACT: Large language models are increasingly becoming a cornerstone technology in artificial intelligence, the sciences, and society as a whole, yet the optimal strategies for dataset composition and filtering remain largely elusive. Many of the top-performing models lack transparency in their dataset curation and model development processes, posing an obstacle to the development of fully open language models. In this paper, we identify three core data-related challenges that must be addressed to advance open-source language models. These include (1) transparency in model development, including the data curation process, (2) access to large quantities of high-quality data, and (3) availability of artifacts and metadata for dataset curation and analysis. To address these challenges, we release RedPajama-V1, an open reproduction of the LLaMA training dataset. In addition, we release RedPajama-V2, a massive web-only dataset consisting of raw, unfiltered text data together with quality signals and metadata. Together, the RedPajama datasets comprise over 100 trillion tokens spanning multiple domains and with their quality signals facilitate the filtering of data, aiming to inspire the development of numerous new datasets. To date, these datasets have already been used in the training of strong language models used in production, such as Snowflake Arctic, Salesforce's XGen and AI2's OLMo. To provide insight into the quality of RedPajama, we present a series of analyses and ablation studies with decoder-only language models with up to 1.6B parameters. Our findings demonstrate how quality signals for web data can be effectively leveraged to curate high-quality subsets of the dataset, underscoring the potential of RedPajama to advance the development of transparent and high-performing language models at scale.

## 02-005 | Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset
- arXiv: 2412.02595  first public: 2024-12-03  latest: 2025-05-30  primary cat: cs.CL
- authors (9): Dan Su; Kezhi Kong; Ying Lin; Joseph Jennings; Brandon Norick; Markus Kliegl ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: ACL 2025
- URLs on first pages of PDF: https://github.com/NVIDIA/NeMo-Curator https://github.com/google-research/ https://huggingface.co/nvidia/nemocurator-
- pages: 17

ABSTRACT: Recent English Common Crawl datasets like FineWeb-Edu and DCLM achieved significant benchmark gains via aggressive model-based filtering, but at the cost of removing 90% of data. This limits their suitability for long token horizon training, such as 15T tokens for Llama 3.1. In this paper, we show how to achieve better trade-offs between accuracy and data quantity by a combination of classifier ensembling, synthetic data rephrasing, and reduced reliance on heuristic filters. When training 8B parameter models for 1T tokens, using a high-quality subset of our data improves MMLU by 5.6 over DCLM, demonstrating the efficacy of our methods for boosting accuracies over a relatively short token horizon. Furthermore, our full 6.3T token dataset matches DCLM on MMLU, but contains four times more unique real tokens than DCLM. This unlocks state-of-the-art training over a long token horizon: an 8B parameter model trained for 15T tokens, of which 7.2T came from our dataset, is better than the Llama 3.1 8B model: +5 on MMLU, +3.1 on ARC-Challenge, and +0.5 on average across ten diverse tasks. The dataset is available at https://data.commoncrawl.org/contrib/Nemotron/Nemotron-CC/index.html

## 02-006 | FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language
- arXiv: 2506.20920  first public: 2025-06-26  latest: 2025-06-26  primary cat: cs.CL
- authors (10): Guilherme Penedo; Hynek Kydlíček; Vinko Sabolčec; Bettina Messmer; Negar Foroutan; Amir Hossein Kargaran ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/huggingface/fineweb-2
- pages: 59

ABSTRACT: Pre-training state-of-the-art large language models (LLMs) requires vast amounts of clean and diverse text data. While the open development of large high-quality English pre-training datasets has seen substantial recent progress, training performant multilingual LLMs remains a challenge, in large part due to the inherent difficulty of tailoring filtering and deduplication pipelines to a large number of languages. In this work, we introduce a new pre-training dataset curation pipeline based on FineWeb that can be automatically adapted to support any language. We extensively ablate our pipeline design choices on a set of nine diverse languages, guided by a set of meaningful and informative evaluation tasks that were chosen through a novel selection process based on measurable criteria. Ultimately, we show that our pipeline can be used to create non-English corpora that produce more performant models than prior datasets. We additionally introduce a straightforward and principled approach to rebalance datasets that takes into consideration both duplication count and quality, providing an additional performance uplift. Finally, we scale our pipeline to over 1000 languages using almost 100 Common Crawl snapshots to produce FineWeb2, a new 20 terabyte (5 billion document) multilingual dataset which we release along with our pipeline, training, and evaluation codebases.

## 02-007 | The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text
- arXiv: 2506.05209  first public: 2025-06-05  latest: 2025-06-05  primary cat: cs.CL
- authors (27): Nikhil Kandpal; Brian Lester; Colin Raffel; Sebastian Majstorovic; Stella Biderman; Baber Abbasi ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- pages: 55

ABSTRACT: Large language models (LLMs) are typically trained on enormous quantities of unlicensed text, a practice that has led to scrutiny due to possible intellectual property infringement and ethical concerns. Training LLMs on openly licensed text presents a first step towards addressing these issues, but prior data collection efforts have yielded datasets too small or low-quality to produce performant LLMs. To address this gap, we collect, curate, and release the Common Pile v0.1, an eight terabyte collection of openly licensed text designed for LLM pretraining. The Common Pile comprises content from 30 sources that span diverse domains including research papers, code, books, encyclopedias, educational materials, audio transcripts, and more. Crucially, we validate our efforts by training two 7 billion parameter LLMs on text from the Common Pile: Comma v0.1-1T and Comma v0.1-2T, trained on 1 and 2 trillion tokens respectively. Both models attain competitive performance to LLMs trained on unlicensed text with similar computational budgets, such as Llama 1 and 2 7B. In addition to releasing the Common Pile v0.1 itself, we also release the code used in its creation as well as the training mixture and checkpoints for the Comma v0.1 models.

## 02-008 | StarCoder 2 and The Stack v2: The Next Generation
- arXiv: 2402.19173  first public: 2024-02-29  latest: 2024-02-29  primary cat: cs.SE
- authors (66): Anton Lozhkov; Raymond Li; Loubna Ben Allal; Federico Cassano; Joel Lamy-Poirier; Nouamane Tazi ...
- seed subtopic: 数据收集; type: 原始研究; cross: ['04']
- pages: 61

ABSTRACT: The BigCode project, an open-scientific collaboration focused on the responsible development of Large Language Models for Code (Code LLMs), introduces StarCoder2. In partnership with Software Heritage (SWH), we build The Stack v2 on top of the digital commons of their source code archive. Alongside the SWH repositories spanning 619 programming languages, we carefully select other high-quality data sources, such as GitHub pull requests, Kaggle notebooks, and code documentation. This results in a training set that is 4x larger than the first StarCoder dataset. We train StarCoder2 models with 3B, 7B, and 15B parameters on 3.3 to 4.3 trillion tokens and thoroughly evaluate them on a comprehensive set of Code LLM benchmarks. We find that our small model, StarCoder2-3B, outperforms other Code LLMs of similar size on most benchmarks, and also outperforms StarCoderBase-15B. Our large model, StarCoder2- 15B, significantly outperforms other models of comparable size. In addition, it matches or outperforms CodeLlama-34B, a model more than twice its size. Although DeepSeekCoder- 33B is the best-performing model at code completion for high-resource languages, we find that StarCoder2-15B outperforms it on math and code reasoning benchmarks, as well as several low-resource languages. We make the model weights available under an OpenRAIL license and ensure full transparency regarding the training data by releasing the SoftWare Heritage persistent IDentifiers (SWHIDs) of the source code data.

## 02-009 | MegaMath: Pushing the Limits of Open Math Corpora
- arXiv: 2504.02807  first public: 2025-04-03  latest: 2025-04-03  primary cat: cs.CL
- authors (8): Fan Zhou; Zengzhi Wang; Nikhil Ranjan; Zhoujun Cheng; Liping Tang; Guowei He ...
- seed subtopic: 数据收集; type: 原始研究; cross: []
- arXiv comment: 26 pages, 15 figures, 22 tables
- URLs on first pages of PDF: https://github.com/LLM360/MegaMath
- pages: 26

ABSTRACT: Mathematical reasoning is a cornerstone of human intelligence and a key benchmark for advanced capabilities in large language models (LLMs). However, the research community still lacks an open, large-scale, high-quality corpus tailored to the demands of math-centric LLM pre-training. We present MegaMath, an open dataset curated from diverse, math-focused sources through following practices: (1) Revisiting web data: We re-extracted mathematical documents from Common Crawl with math-oriented HTML optimizations, fasttext-based filtering and deduplication, all for acquiring higher-quality data on the Internet. (2) Recalling Math-related code data: We identified high quality math-related code from large code training corpus, Stack-V2, further enhancing data diversity. (3) Exploring Synthetic data: We synthesized QA-style text, math-related code, and interleaved text-code blocks from web data or code data. By integrating these strategies and validating their effectiveness through extensive ablations, MegaMath delivers 371B tokens with the largest quantity and top quality among existing open math pre-training datasets.

## 02-010 | Consent in Crisis: The Rapid Decline of the AI Data Commons
- arXiv: 2407.14933  first public: 2024-07-20  latest: 2024-07-24  primary cat: cs.CL
- authors (49): Shayne Longpre; Robert Mahari; Ariel Lee; Campbell Lund; Hamidah Oderinwale; William Brannon ...
- seed subtopic: 数据收集; type: 原始研究; cross: ['12']
- arXiv comment: 41 pages (13 main), 5 figures, 9 tables
- pages: 41

ABSTRACT: General-purpose artificial intelligence (AI) systems are built on massive swathes of public web data, assembled into corpora such as C4, RefinedWeb, and Dolma. To our knowledge, we conduct the first, large-scale, longitudinal audit of the consent protocols for the web domains underlying AI training corpora. Our audit of 14,000 web domains provides an expansive view of crawlable web data and how codified data use preferences are changing over time. We observe a proliferation of AI-specific clauses to limit use, acute differences in restrictions on AI developers, as well as general inconsistencies between websites' expressed intentions in their Terms of Service and their robots.txt. We diagnose these as symptoms of ineffective web protocols, not designed to cope with the widespread re-purposing of the internet for AI. Our longitudinal analyses show that in a single year (2023-2024) there has been a rapid crescendo of data restrictions from web sources, rendering ~5%+ of all tokens in C4, or 28%+ of the most actively maintained, critical sources in C4, fully restricted from use. For Terms of Service crawling restrictions, a full 45% of C4 is now restricted. If respected or enforced, these restrictions are rapidly biasing the diversity, freshness, and scaling laws for general-purpose AI systems. We hope to illustrate the emerging crises in data consent, for both developers and creators. The foreclosure of much of the open web will impact not only commercial AI, but also non-commercial AI and academic research.

## 02-011 | Craw4LLM: Efficient Web Crawling for LLM Pretraining
- arXiv: 2502.13347  first public: 2025-02-19  latest: 2025-06-23  primary cat: cs.CL
- authors (3): Shi Yu; Zhiyuan Liu; Chenyan Xiong
- seed subtopic: 数据收集; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/cxcscmu/Craw4LLM
- pages: 9

ABSTRACT: Web crawl is a main source of large language models' (LLMs) pretraining data, but the majority of crawled web pages are discarded in pretraining due to low data quality. This paper presents Craw4LLM, an efficient web crawling method that explores the web graph based on the preference of LLM pretraining. Specifically, it leverages the influence of a webpage in LLM pretraining as the priority score of the web crawler's scheduler, replacing the standard graph connectivity based priority. Our experiments on a web graph containing 900 million webpages from a commercial search engine's index demonstrate the efficiency of Craw4LLM in obtaining high-quality pretraining data. With just 21% URLs crawled, LLMs pretrained on Craw4LLM data reach the same downstream performances of previous crawls, significantly reducing the crawling waste and alleviating the burdens on websites. Our code is publicly available at https://github.com/cxcscmu/Craw4LLM.

## 02-012 | SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model
- arXiv: 2502.02737  first public: 2025-02-04  latest: 2025-02-04  primary cat: cs.CL
- authors (22): Loubna Ben Allal; Anton Lozhkov; Elie Bakouch; Gabriel Martín Blázquez; Guilherme Penedo; Lewis Tunstall ...
- seed subtopic: 数据配比; type: 技术报告; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/HuggingFaceTB/finemath
- pages: 24

ABSTRACT: While large language models have facilitated breakthroughs in many applications of artificial intelligence, their inherent largeness makes them computationally expensive and challenging to deploy in resource-constrained settings. In this paper, we document the development of SmolLM2, a state-of-the-art "small" (1.7 billion parameter) language model (LM). To attain strong performance, we overtrain SmolLM2 on ~11 trillion tokens of data using a multi-stage training process that mixes web text with specialized math, code, and instruction-following data. We additionally introduce new specialized datasets (FineMath, Stack-Edu, and SmolTalk) at stages where we found existing datasets to be problematically small or low-quality. To inform our design decisions, we perform both small-scale ablations as well as a manual refinement process that updates the dataset mixing rates at each stage based on the performance at the previous stage. Ultimately, we demonstrate that SmolLM2 outperforms other recent small LMs including Qwen2.5-1.5B and Llama3.2-1B. To facilitate future research on LM development as well as applications of small LMs, we release both SmolLM2 as well as all of the datasets we prepared in the course of this project.

## 02-013 | What's In My Big Data?
- arXiv: 2310.20707  first public: 2023-10-31  latest: 2024-03-05  primary cat: cs.CL
- authors (13): Yanai Elazar; Akshita Bhagia; Ian Magnusson; Abhilasha Ravichander; Dustin Schwenk; Alane Suhr ...
- seed subtopic: 数据收集; type: 原始研究; cross: ['12']
- arXiv comment: Published at ICLR 2024 spotlight
- URLs on first pages of PDF: https://github.com/allenai/wimbd
- pages: 56

ABSTRACT: Large text corpora are the backbone of language models. However, we have a limited understanding of the content of these corpora, including general statistics, quality, social factors, and inclusion of evaluation data (contamination). In this work, we propose What's In My Big Data? (WIMBD), a platform and a set of sixteen analyses that allow us to reveal and compare the contents of large text corpora. WIMBD builds on two basic capabilities -- count and search -- at scale, which allows us to analyze more than 35 terabytes on a standard compute node. We apply WIMBD to ten different corpora used to train popular language models, including C4, The Pile, and RedPajama. Our analysis uncovers several surprising and previously undocumented findings about these corpora, including the high prevalence of duplicate, synthetic, and low-quality content, personally identifiable information, toxic language, and benchmark contamination. For instance, we find that about 50% of the documents in RedPajama and LAION-2B-en are duplicates. In addition, several datasets used for benchmarking models trained on such corpora are contaminated with respect to important benchmarks, including the Winograd Schema Challenge and parts of GLUE and SuperGLUE. We open-source WIMBD's code and artifacts to provide a standard set of evaluations for new text-based corpora and to encourage more analyses and transparency around them.

## 02-014 | Infini-gram: Scaling Unbounded n-gram Language Models to a Trillion Tokens
- arXiv: 2401.17377  first public: 2024-01-30  latest: 2025-04-07  primary cat: cs.CL
- authors (5): Jiacheng Liu; Sewon Min; Luke Zettlemoyer; Yejin Choi; Hannaneh Hajishirzi
- seed subtopic: 数据收集; type: 原始研究; cross: []
- arXiv comment: Published at COLM 2024, spotlight paper
- pages: 26

ABSTRACT: Are $n$-gram language models still relevant in this era of neural large language models (LLMs)? Our answer is yes, and we showcase their values in both text analysis and improving neural LLMs. This was done by modernizing $n$-gram LMs in two aspects. First, we train them at the same data scale as neural LLMs -- 5 trillion tokens. This is the largest $n$-gram LM ever built. Second, existing $n$-gram LMs use small $n$ which hinders their performance; we instead allow $n$ to be arbitrarily large, by introducing a new $\infty$-gram LM with backoff. Instead of pre-computing $n$-gram count tables (which would be very expensive), we develop an engine named infini-gram -- powered by suffix arrays -- that can compute $\infty$-gram (as well as $n$-gram with arbitrary $n$) probabilities with millisecond-level latency. The $\infty$-gram framework and infini-gram engine enable us to conduct many novel and interesting analyses of human-written and machine-generated text: we find that the $\infty$-gram LM has fairly high accuracy for next-token prediction (47%), and can complement neural LLMs to greatly reduce their perplexity. When analyzing machine-generated text, we also observe irregularities in the machine--$\infty$-gram agreement level with respect to the suffix length, which indicates deficiencies in neural LLM pretraining and the positional embeddings of Transformers.

## 02-015 | Programming Every Example: Lifting Pre-training Data Quality Like Experts at Scale
- arXiv: 2409.17115  first public: 2024-09-25  latest: 2025-02-14  primary cat: cs.CL
- authors (5): Fan Zhou; Zengzhi Wang; Qian Liu; Junlong Li; Pengfei Liu
- seed subtopic: 清洗; type: 原始研究; cross: []
- arXiv comment: 47 pages, 13 figures, 34 tables
- URLs on first pages of PDF: https://github.com/GAIR-NLP/ProX https://huggingface.co/gair-prox
- pages: 47

ABSTRACT: Large language model pre-training has traditionally relied on human experts to craft heuristics for improving the corpora quality, resulting in numerous rules developed to date. However, these rules lack the flexibility to address the unique characteristics of individual example effectively. Meanwhile, applying tailored rules to every example is impractical for human experts. In this paper, we demonstrate that even small language models, with as few as 0.3B parameters, can exhibit substantial data refining capabilities comparable to those of human experts. We introduce Programming Every Example (ProX), a novel framework that treats data refinement as a programming task, enabling models to refine corpora by generating and executing fine-grained operations, such as string normalization, for each individual example at scale. Experimental results show that models pre-trained on ProX-curated data outperform either original data or data filtered by other selection methods by more than 2% across various downstream benchmarks. Its effectiveness spans various model sizes and pre-training corpora, including C4, RedPajama-V2, FineWeb, FineWeb-Edu, and DCLM. Furthermore, ProX exhibits significant potential in domain-specific continual pre-training: without domain specific design, models trained on OpenWebMath refined by ProX outperform human-crafted rule-based methods, improving average accuracy by 7.6% over Mistral-7B, with 14.6% for Llama-2-7B and 20.3% for CodeLlama-7B, all within 10B tokens to be comparable to models like Llemma-7B trained on 200B tokens. Further analysis highlights that ProX significantly saves training FLOPs, offering a promising path for efficient LLM pre-training. We are open-sourcing ProX with >500B corpus, models, and sharing all training and implementation details for reproducible research and future innovation. Code: https://github.com/GAIR-NLP/ProX

## 02-016 | Data, Data Everywhere: A Guide for Pretraining Dataset Construction
- arXiv: 2407.06380  first public: 2024-07-08  latest: 2024-10-19  primary cat: cs.CL
- authors (9): Jupinder Parmar; Shrimai Prabhumoye; Joseph Jennings; Bo Liu; Aastha Jhunjhunwala; Zhilin Wang ...
- seed subtopic: 清洗; type: 原始研究; cross: []
- arXiv comment: Accepted as an oral presentation at EMNLP 2024
- pages: 25

ABSTRACT: The impressive capabilities of recent language models can be largely attributed to the multi-trillion token pretraining datasets that they are trained on. However, model developers fail to disclose their construction methodology which has lead to a lack of open information on how to develop effective pretraining sets. To address this issue, we perform the first systematic study across the entire pipeline of pretraining set construction. First, we run ablations on existing techniques for pretraining set development to identify which methods translate to the largest gains in model accuracy on downstream evaluations. Then, we categorize the most widely used data source, web crawl snapshots, across the attributes of toxicity, quality, type of speech, and domain. Finally, we show how such attribute information can be used to further refine and improve the quality of a pretraining set. These findings constitute an actionable set of steps that practitioners can use to develop high quality pretraining sets.

## 02-017 | LSHBloom: Memory-efficient, Extreme-scale Document Deduplication
- arXiv: 2411.04257  first public: 2024-11-06  latest: 2026-01-27  primary cat: cs.LG
- authors (10): Arham Khan; Robert Underwood; Carlo Siebenschuh; Yadu Babuji; Aswathy Ajith; Kyle Hippe ...
- seed subtopic: 去重; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Contemporary large language model (LLM) training pipelines require the assembly of internet-scale databases full of text data from a variety of sources (e.g., web, academic, and publishers). Preprocessing these datasets via deduplication -- detecting and eliminating additional instances of the same content -- is a major focus for assembling and curating training datasets for LLMs. Unrestrained, duplicates in the training dataset increase training costs and lead to undesirable properties such as memorization in trained models or cheating on evaluation. Unfortunately, contemporary approaches to document-level deduplication are either unreliable at accurately identifying duplicate documents or extremely expensive in terms of both runtime and memory. We propose LSHBloom, an extension to MinhashLSH, which replaces the expensive LSHIndex with lightweight Bloom filters. LSHBloom demonstrates the same state-of-the-art deduplication performance as MinhashLSH, with only a marginal increase in false positives (near zero in our experiments), while boasting competitive runtime (12$\times$ faster than MinhashLSH on peS2o) and, crucially, using 18$\times$ less disk space than MinhashLSH (as measured on peS2o). Based on extrapolation, we show that this advantage in space and runtime remains even at the extreme scale of several billion documents. LSHBloom allows practitioners to access the deduplication quality of MinHashLSH at scales that are normally only tractable for less sophisticated, heuristic solutions. As a result, LSHBloom promises to enable scaling high-quality document deduplication to internet-scale text datasets.

## 02-019 | QuRating: Selecting High-Quality Data for Training Language Models
- arXiv: 2402.09739  first public: 2024-02-15  latest: 2024-07-17  primary cat: cs.CL
- authors (4): Alexander Wettig; Aatmik Gupta; Saumya Malik; Danqi Chen
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2024. The results for top-k selection have been corrected. The code, models and data are available at https://github.com/princeton-nlp/QuRating
- URLs on first pages of PDF: https://github.com/princeton-nlp/QuRating
- pages: 57

ABSTRACT: Selecting high-quality pre-training data is important for creating capable language models, but existing methods rely on simple heuristics. We introduce QuRating, a method for selecting pre-training data that can capture human intuitions about data quality. In this paper, we investigate four qualities - writing style, required expertise, facts & trivia, and educational value - and find that LLMs are able to discern these qualities, especially when making pairwise judgments of texts. We train a QuRater model to learn scalar ratings from pairwise judgments, and use it to annotate a 260B training corpus with quality ratings for each of the four criteria. In our experiments, we select 30B tokens according to the different quality ratings and train 1.3B-parameter language models on the selected data. We find that it is important to balance quality and diversity. When we sample using quality ratings as logits over documents, our models obtain lower perplexity and stronger in-context learning performance than baselines. Our best model is based on educational value and performs similarly to a model trained with uniform sampling for 50% more steps. Beyond data selection, we use the quality ratings to construct a training curriculum which improves performance without changing the training dataset. We extensively analyze the quality ratings and discuss their characteristics, biases, and wider implications.

## 02-022 | How to Train Data-Efficient LLMs
- arXiv: 2402.09668  first public: 2024-02-15  latest: 2024-02-15  primary cat: cs.LG
- authors (9): Noveen Sachdeva; Benjamin Coleman; Wang-Cheng Kang; Jianmo Ni; Lichan Hong; Ed H. Chi ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: Under review. 44 pages, 30 figures
- pages: 44

ABSTRACT: The training of large language models (LLMs) is expensive. In this paper, we study data-efficient approaches for pre-training LLMs, i.e., techniques that aim to optimize the Pareto frontier of model quality and training resource/data consumption. We seek to understand the tradeoffs associated with data selection routines based on (i) expensive-to-compute data-quality estimates, and (ii) maximization of coverage and diversity-based measures in the feature space. Our first technique, Ask-LLM, leverages the zero-shot reasoning capabilities of instruction-tuned LLMs to directly assess the quality of a training example. To target coverage, we propose Density sampling, which models the data distribution to select a diverse sample. In our comparison of 19 samplers, involving hundreds of evaluation tasks and pre-training runs, we find that Ask-LLM and Density are the best methods in their respective categories. Coverage sampling can recover the performance of the full data, while models trained on Ask-LLM data consistently outperform full-data training -- even when we reject 90% of the original dataset, while converging up to 70% faster.

## 02-023 | Improving Pretraining Data Using Perplexity Correlations
- arXiv: 2409.05816  first public: 2024-09-09  latest: 2025-03-10  primary cat: cs.CL
- authors (3): Tristan Thrush; Christopher Potts; Tatsunori Hashimoto
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: ICLR 2025
- URLs on first pages of PDF: https://github.com/TristanThrush/perplexity-correlations
- pages: 35

ABSTRACT: Quality pretraining data is often seen as the key to high-performance language models. However, progress in understanding pretraining data has been slow due to the costly pretraining runs required for data selection experiments. We present a framework that avoids these costs and selects high-quality pretraining data without any LLM training of our own. Our work is based on a simple observation: LLM losses on many pretraining texts are correlated with downstream benchmark performance, and selecting high-correlation documents is an effective pretraining data selection method. We build a new statistical framework for data selection centered around estimates of perplexity-benchmark correlations and perform data selection using a sample of 90 LLMs taken from the Open LLM Leaderboard on texts from tens of thousands of web domains. In controlled pretraining experiments at the 160M parameter scale on 8 benchmarks, our approach outperforms DSIR on every benchmark, while matching the best data selector found in DataComp-LM, a hand-engineered bigram classifier. We have now also updated this paper to include results from preregistered experiments with new pretraining data on an aggregation of 22 benchmarks up to the 1.4B scale, showing increasing improvements of our method over others with more scale. A pip package with full documentation can be found here: https://github.com/TristanThrush/perplexity-correlations.

## 02-025 | Organize the Web: Constructing Domains Enhances Pre-Training Data Curation
- arXiv: 2502.10341  first public: 2025-02-14  latest: 2025-07-16  primary cat: cs.CL
- authors (6): Alexander Wettig; Kyle Lo; Sewon Min; Hannaneh Hajishirzi; Danqi Chen; Luca Soldaini
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: Accepted at ICML 2025. Project page: https://weborganizer.allen.ai
- pages: 28

ABSTRACT: Modern language models are trained on large, unstructured datasets consisting of trillions of tokens and obtained by crawling the web. The unstructured nature makes it difficult to reason about their contents and develop systematic approaches to data curation. In this paper, we unpack monolithic web corpora by developing taxonomies of their contents and organizing them into domains. We introduce WebOrganizer, a framework for organizing web pages in terms of both their topic and format. Using these two complementary notions of domains, we automatically annotate pre-training data by distilling annotations from a large language model into efficient classifiers. This allows us to study how data from different domains should be mixed to improve models on downstream tasks, and we show that we can combine insights about effective topics and formats to further boost performance. We demonstrate that our domain mixing also improves existing methods that select data based on quality. Furthermore, we study and compare how quality-based methods will implicitly change the domain mixture. Overall, our work demonstrates that constructing and mixing domains provides a valuable complement to quality-based data curation methods, opening new avenues for effective and insightful pre-training data curation.

## 02-026 | Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models
- arXiv: 2504.14194  first public: 2025-04-19  latest: 2025-08-06  primary cat: cs.CL
- authors (10): Xinlin Zhuang; Jiahui Peng; Ren Ma; Yinfan Wang; Tianyi Bai; Xingjian Wei ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: ACL 2025 Best Theme Paper Award
- pages: 41

ABSTRACT: The composition of pre-training datasets for large language models (LLMs) remains largely undisclosed, hindering transparency and efforts to optimize data quality, a critical driver of model performance. Current data selection methods, such as natural language quality assessments, diversity-based filters, and classifier-based approaches, are limited by single-dimensional evaluation or redundancy-focused strategies. To address these gaps, we propose four dimensions to evaluate data quality: professionalism, readability, reasoning, and cleanliness. We further introduce Meta-rater,a multi-dimensional data selection method that integrates these dimensions with existing quality metrics through learned optimal weightings. Meta-rater employs proxy models to train a regression model that predicts validation loss, enabling the identification of optimal combinations of quality scores. Experiments demonstrate that Meta-rater doubles convergence speed for 1.3B parameter models and improves downstream task performance by 3.23, with advantages that scale to models as large as 7.2B parameters. Our work establishes that holistic, multi-dimensional quality integration significantly outperforms conventional single-dimension approaches, offering a scalable paradigm for enhancing pre-training efficiency and model capability. To advance future research, we release scripts, data, and models at https://github.com/opendatalab/Meta-rater.

## 02-027 | DataDecide: How to Predict Best Pretraining Data with Small Experiments
- arXiv: 2504.11393  first public: 2025-04-15  latest: 2025-07-13  primary cat: cs.LG
- authors (13): Ian Magnusson; Nguyen Tai; Ben Bogin; David Heineman; Jena D. Hwang; Luca Soldaini ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: ICML 2025
- pages: 16

ABSTRACT: Because large language models are expensive to pretrain on different datasets, using smaller-scale experiments to decide on data is crucial for reducing costs. Which benchmarks and methods of making decisions from observed performance at small scale most accurately predict the datasets that yield the best large models? To empower open exploration of this question, we release models, data, and evaluations in DataDecide -- the most extensive open suite of models over differences in data and scale. We conduct controlled pretraining experiments across 25 corpora with differing sources, deduplication, and filtering up to 100B tokens, model sizes up to 1B parameters, and 3 random seeds. We find that the ranking of models at a single, small size (e.g., 150M parameters) is a strong baseline for predicting best models at our larger target scale (1B) (~80% of com parisons correct). No scaling law methods among 8 baselines exceed the compute-decision frontier of single-scale predictions, but DataDecide can measure improvement in future scaling laws. We also identify that using continuous likelihood metrics as proxies in small experiments makes benchmarks including MMLU, ARC, HellaSwag, MBPP, and HumanEval >80% predictable at the target 1B scale with just 0.01% of the compute.

## 02-028 | Ultra-FineWeb: Efficient Data Filtering and Verification for High-Quality LLM Training Data
- arXiv: 2505.05427  first public: 2025-05-08  latest: 2025-05-08  primary cat: cs.CL
- authors (12): Yudong Wang; Zixuan Fu; Jie Cai; Peijun Tang; Hongya Lyu; Yewei Fang ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: The datasets are available on https://huggingface.co/datasets/openbmb/UltraFineWeb
- URLs on first pages of PDF: https://huggingface.co/datasets/openbmb/UltraFineWeb https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1
- pages: 19

ABSTRACT: Data quality has become a key factor in enhancing model performance with the rapid development of large language models (LLMs). Model-driven data filtering has increasingly become a primary approach for acquiring high-quality data. However, it still faces two main challenges: (1) the lack of an efficient data verification strategy makes it difficult to provide timely feedback on data quality; and (2) the selection of seed data for training classifiers lacks clear criteria and relies heavily on human expertise, introducing a degree of subjectivity. To address the first challenge, we introduce an efficient verification strategy that enables rapid evaluation of the impact of data on LLM training with minimal computational cost. To tackle the second challenge, we build upon the assumption that high-quality seed data is beneficial for LLM training, and by integrating the proposed verification strategy, we optimize the selection of positive and negative samples and propose an efficient data filtering pipeline. This pipeline not only improves filtering efficiency, classifier quality, and robustness, but also significantly reduces experimental and inference costs. In addition, to efficiently filter high-quality data, we employ a lightweight classifier based on fastText, and successfully apply the filtering pipeline to two widely-used pre-training corpora, FineWeb and Chinese FineWeb datasets, resulting in the creation of the higher-quality Ultra-FineWeb dataset. Ultra-FineWeb contains approximately 1 trillion English tokens and 120 billion Chinese tokens. Empirical results demonstrate that the LLMs trained on Ultra-FineWeb exhibit significant performance improvements across multiple benchmark tasks, validating the effectiveness of our pipeline in enhancing both data quality and training efficiency.

## 02-030 | Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
- arXiv: 2403.16952  first public: 2024-03-25  latest: 2025-03-20  primary cat: cs.CL
- authors (6): Jiasheng Ye; Peiju Liu; Tianxiang Sun; Jun Zhan; Yunhua Zhou; Xipeng Qiu
- seed subtopic: 数据配比; type: 原始研究; cross: []
- arXiv comment: accepted by ICLR2025, camera ready version
- URLs on first pages of PDF: https://github.com/yegcjs/mixinglaws
- pages: 27

ABSTRACT: Pretraining data of large language models composes multiple domains (e.g., web texts, academic papers, codes), whose mixture proportions crucially impact the competence of outcome models. While existing endeavors rely on heuristics or qualitative strategies to tune the proportions, we discover the quantitative predictability of model performance regarding the mixture proportions in function forms, which we refer to as the data mixing laws. Fitting such functions on sample mixtures unveils model performance on unseen mixtures before actual runs, thus guiding the selection of an ideal data mixture. Furthermore, we propose nested use of the scaling laws of training steps, model sizes, and our data mixing law to enable predicting the performance of large models trained on massive data under various mixtures with only small-scale training. Moreover, experimental results verify that our method effectively optimizes the training mixture of a 1B model trained for 100B tokens in RedPajama, reaching a performance comparable to the one trained for 48% more steps on the default mixture. Extending the application of data mixing laws to continual training accurately predicts the critical mixture proportion that avoids catastrophic forgetting and outlooks the potential for dynamic data schedules

## 02-031 | RegMix: Data Mixture as Regression for Language Model Pre-training
- arXiv: 2407.01492  first public: 2024-07-01  latest: 2025-01-23  primary cat: cs.CL
- authors (8): Qian Liu; Xiaosen Zheng; Niklas Muennighoff; Guangtao Zeng; Longxu Dou; Tianyu Pang ...
- seed subtopic: 数据配比; type: 原始研究; cross: []
- arXiv comment: ICLR 2025
- URLs on first pages of PDF: https://github.com/sail-sg/regmix
- pages: 36

ABSTRACT: The data mixture for large language model pre-training significantly impacts performance, yet how to determine an effective mixture remains unclear. We propose RegMix to automatically identify a high-performing data mixture by formulating it as a regression task. RegMix trains many small models on diverse data mixtures, uses regression to predict performance of unseen mixtures, and applies the best predicted mixture to train a large-scale model with orders of magnitude more compute. To empirically validate RegMix, we train 512 models with 1M parameters for 1B tokens to fit the regression model and predict the best data mixture. Using this mixture we train a 1B parameter model for 25B tokens (i.e. 1000x larger and 25x longer) which we find performs best among 64 candidate 1B parameter models with other mixtures. Furthermore, RegMix consistently outperforms human selection in experiments involving models up to 7B models trained on 100B tokens, while matching or exceeding DoReMi using just 10% of the computational resources. Our experiments also show that (1) Data mixtures significantly impact performance; (2) Web corpora rather than data perceived as high-quality like Wikipedia have the strongest positive correlation with downstream performance; (3) Domains interact in complex ways often contradicting common sense, thus automatic approaches like RegMix are needed; (4) Data mixture effects transcend scaling laws. Our code is available at https://github.com/sail-sg/regmix.

## 02-032 | Aioli: A Unified Optimization Framework for Language Model Data Mixing
- arXiv: 2411.05735  first public: 2024-11-08  latest: 2025-04-21  primary cat: cs.LG
- authors (5): Mayee F. Chen; Michael Y. Hu; Nicholas Lourie; Kyunghyun Cho; Christopher Ré
- seed subtopic: 数据配比; type: 原始研究; cross: []
- arXiv comment: ICLR 2025 Camera Ready
- pages: 40

ABSTRACT: Language model performance depends on identifying the optimal mixture of data groups to train on (e.g., law, code, math). Prior work has proposed a diverse set of methods to efficiently learn mixture proportions, ranging from fitting regression models over training runs to dynamically updating proportions throughout training. Surprisingly, we find that no existing method consistently outperforms a simple stratified sampling baseline in terms of average test perplexity. To understand this inconsistency, we unify existing methods into a standard framework, showing they are equivalent to solving a common optimization problem: minimize average loss subject to a method-specific mixing law -- an implicit assumption on the relationship between loss and mixture proportions. This framework suggests that measuring the fidelity of a method's mixing law can offer insights into its performance. Empirically, we find that existing methods set their mixing law parameters inaccurately, resulting in the inconsistent mixing performance we observe. Using this insight, we derive a new online method named Aioli, which directly estimates the mixing law parameters throughout training and uses them to dynamically adjust proportions. Aioli outperforms stratified sampling on 6 out of 6 datasets by an average of 0.27 test perplexity points, whereas existing methods fail to consistently beat stratified sampling, doing up to 6.9 points worse. Moreover, in a practical setting where proportions are learned on shorter runs due to computational constraints, Aioli can dynamically adjust these proportions over the full training run, consistently improving performance over existing methods by up to 12.012 test perplexity points.

## 02-033 | Nemotron-CLIMB: CLustering-based Iterative Data Mixture Bootstrapping for Language Model Pre-training
- arXiv: 2504.13161  first public: 2025-04-17  latest: 2025-11-30  primary cat: cs.CL
- authors (14): Shizhe Diao; Yu Yang; Yonggan Fu; Xin Dong; Dan Su; Markus Kliegl ...
- seed subtopic: 数据配比; type: 原始研究; cross: []
- arXiv comment: Accepted to NeurIPS 2025
- pages: 29

ABSTRACT: Pre-training datasets are typically collected from web content and lack inherent domain divisions. For instance, widely used datasets like Common Crawl do not include explicit domain labels, while manually curating labeled datasets such as The Pile is labor-intensive. Consequently, identifying an optimal pre-training data mixture remains a challenging problem, despite its significant benefits for pre-training performance. To address these challenges, we propose CLustering-based Iterative Data Mixture Bootstrapping (Nemotron-CLIMB), an automated framework that discovers, evaluates, and refines data mixtures in a pre-training setting. Specifically, Nemotron-CLIMB embeds and clusters large-scale datasets in a semantic space and then iteratively searches for optimal mixtures using a smaller proxy model and a predictor. When continuously trained on 400B tokens with this mixture, our 1B model exceeds the state-of-the-art Llama-3.2-1B by 2.0%. Moreover, we observe that optimizing for a specific domain (e.g., Social Sciences) yields a 5% improvement over random sampling. Finally, we introduce Nemotron-ClimbLab, a filtered 1.2-trillion-token corpus with 20 clusters as a research playground, and Nemotron-ClimbMix, a compact yet powerful 400-billion-token dataset designed for efficient pre-training that delivers superior performance under an equal token budget. We analyze the final data mixture, elucidating the characteristics of an optimal data mixture. Our data is available at: https://research.nvidia.com/labs/lpr/climb/

## 02-034 | Scaling Laws for Optimal Data Mixtures
- arXiv: 2507.09404  first public: 2025-07-12  latest: 2025-10-02  primary cat: cs.LG
- authors (7): Mustafa Shukor; Louis Bethune; Dan Busbridge; David Grangier; Enrico Fini; Alaaeldin El-Nouby ...
- seed subtopic: 数据配比; type: 原始研究; cross: ['01']
- pages: 25

ABSTRACT: Large foundation models are typically trained on data from multiple domains, with the data mixture--the proportion of each domain used--playing a critical role in model performance. The standard approach to selecting this mixture relies on trial and error, which becomes impractical for large-scale pretraining. We propose a systematic method to determine the optimal data mixture for any target domain using scaling laws. Our approach accurately predicts the loss of a model of size $N$ trained with $D$ tokens and a specific domain weight vector $h$. We validate the universality of these scaling laws by demonstrating their predictive power in three distinct and large-scale settings: large language model (LLM), native multimodal model (NMM), and large vision models (LVM) pretraining. We further show that these scaling laws can extrapolate to new data mixtures and across scales: their parameters can be accurately estimated using a few small-scale training runs, and used to estimate the performance at larger scales and unseen domain weights. The scaling laws allow to derive the optimal domain weights for any target domain under a given training budget ($N$,$D$), providing a principled alternative to costly trial-and-error methods.

## 02-038 | Rephrasing the Web: A Recipe for Compute and Data-Efficient Language Modeling
- arXiv: 2401.16380  first public: 2024-01-29  latest: 2024-01-29  primary cat: cs.CL
- authors (6): Pratyush Maini; Skyler Seto; He Bai; David Grangier; Yizhe Zhang; Navdeep Jaitly
- seed subtopic: 合成数据; type: 原始研究; cross: []
- pages: 33

ABSTRACT: Large language models are trained on massive scrapes of the web, which are often unstructured, noisy, and poorly phrased. Current scaling laws show that learning from such data requires an abundance of both compute and data, which grows with the size of the model being trained. This is infeasible both because of the large compute costs and duration associated with pre-training, and the impending scarcity of high-quality data on the web. In this work, we propose Web Rephrase Augmented Pre-training ($\textbf{WRAP}$) that uses an off-the-shelf instruction-tuned model prompted to paraphrase documents on the web in specific styles such as "like Wikipedia" or in "question-answer format" to jointly pre-train LLMs on real and synthetic rephrases. First, we show that using WRAP on the C4 dataset, which is naturally noisy, speeds up pre-training by $\sim3x$. At the same pre-training compute budget, it improves perplexity by more than 10% on average across different subsets of the Pile, and improves zero-shot question answer accuracy across 13 tasks by more than 2%. Second, we investigate the impact of the re-phrasing style on the performance of the model, offering insights into how the composition of the training data can impact the performance of LLMs in OOD settings. Our gains are attributed to the fact that re-phrased synthetic data has higher utility than just real data because it (i) incorporates style diversity that closely reflects downstream evaluation style, and (ii) has higher 'quality' than web-scraped data.

## 02-039 | Synthetic continued pretraining
- arXiv: 2409.07431  first public: 2024-09-11  latest: 2024-10-03  primary cat: cs.LG
- authors (5): Zitong Yang; Neil Band; Shuangping Li; Emmanuel Candès; Tatsunori Hashimoto
- seed subtopic: 合成数据; type: 原始研究; cross: []
- arXiv comment: Updated organization of experimental results and methods introduction. Released the dataset and model weights artifact
- pages: 45

ABSTRACT: Pretraining on large-scale, unstructured internet text enables language models to acquire a significant amount of world knowledge. However, this knowledge acquisition is data-inefficient--to learn a given fact, models must be trained on hundreds to thousands of diverse representations of it. This poses a challenge when adapting a pretrained model to a small corpus of domain-specific documents, where each fact may appear rarely or only once. We propose to bridge this gap with synthetic continued pretraining: using the small domain-specific corpus to synthesize a large corpus more amenable to learning, and then performing continued pretraining on the synthesized corpus. We instantiate this proposal with EntiGraph, a synthetic data augmentation algorithm that extracts salient entities from the source documents and then generates diverse text by drawing connections between the sampled entities. Synthetic continued pretraining with EntiGraph enables a language model to answer questions and follow generic instructions related to the source documents without access to them. If, instead, the source documents are available at inference time, we show that the knowledge acquired through our approach compounds with retrieval-augmented generation. To better understand these results, we build a simple mathematical model of EntiGraph, and show how synthetic data augmentation can "rearrange" knowledge to enable more data-efficient learning.

## 02-041 | Scaling Laws of Synthetic Data for Language Models
- arXiv: 2503.19551  first public: 2025-03-25  latest: 2025-10-05  primary cat: cs.CL
- authors (13): Zeyu Qin; Qingxiu Dong; Xingxing Zhang; Li Dong; Xiaolong Huang; Ziyi Yang ...
- seed subtopic: 合成数据; type: 原始研究; cross: []
- arXiv comment: COLM 2025
- pages: 24

ABSTRACT: Large language models (LLMs) achieve strong performance across diverse tasks, largely driven by high-quality web data used in pre-training. However, recent studies indicate this data source is rapidly depleting. Synthetic data emerges as a promising alternative, but it remains unclear whether synthetic datasets exhibit predictable scalability comparable to raw pre-training data. In this work, we systematically investigate the scaling laws of synthetic data by introducing SynthLLM, a scalable framework that transforms pre-training corpora into diverse, high-quality synthetic datasets. Our approach achieves this by automatically extracting and recombining high-level concepts across multiple documents using a graph algorithm. Key findings from our extensive mathematical experiments on SynthLLM include: (1) SynthLLM generates synthetic data that reliably adheres to the rectified scaling law across various model sizes; (2) Performance improvements plateau near 300B tokens; and (3) Larger models approach optimal performance with fewer training tokens. For instance, an 8B model peaks at 1T tokens, while a 3B model requires 4T. Moreover, comparisons with existing synthetic data generation and augmentation methods demonstrate that SynthLLM achieves superior performance and scalability. Our findings highlight synthetic data as a scalable and reliable alternative to organic pre-training corpora, offering a viable path toward continued improvement in model performance.

## 02-042 | BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining
- arXiv: 2508.10975  first public: 2025-08-14  latest: 2025-08-19  primary cat: cs.LG
- authors (31): DatologyAI; :; Pratyush Maini; Vineeth Dorna; Parth Doshi; Aldo Carranza ...
- seed subtopic: 合成数据; type: 原始研究; cross: []
- arXiv comment: Blog version can be viewed at: http://blog.datologyai.com/beyondweb
- pages: 29

ABSTRACT: Recent advances in large language model (LLM) pretraining have shown that simply scaling data quantity eventually leads to diminishing returns, hitting a data wall. In response, the use of synthetic data for pretraining has emerged as a promising paradigm for pushing the frontier of performance. Despite this, the factors affecting synthetic data quality remain poorly understood. In this work, we introduce BeyondWeb, a synthetic data generation framework that produces high-quality synthetic data for pretraining. BeyondWeb significantly extends the capabilities of traditional web-scale datasets, outperforming state-of-the-art synthetic pretraining datasets such as Cosmopedia and Nemotron-CC's high-quality synthetic subset (Nemotron-Synth) by up to 5.1 percentage points (pp) and 2.6pp, respectively, when averaged across a suite of 14 benchmark evaluations. It delivers up to 7.7x faster training than open web data and 2.7x faster than Nemotron-Synth. Remarkably, a 3B model trained for 180B tokens on BeyondWeb outperforms an 8B model trained for the same token budget on Cosmopedia. We also present several insights from BeyondWeb on synthetic data for pretraining: what drives its benefits, which data to rephrase and how, and the impact of model size and family on data quality. Overall, our work shows that there's no silver bullet for generating high-quality synthetic pretraining data. The best outcomes require jointly optimizing many factors, a challenging task that requires rigorous science and practical expertise. Naive approaches can yield modest improvements, potentially at great cost, while well-executed methods can yield transformative improvements, as exemplified by BeyondWeb.

## 02-043 | Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models
- arXiv: 2506.04689  first public: 2025-06-05  latest: 2025-09-15  primary cat: cs.CL
- authors (7): Thao Nguyen; Yang Li; Olga Golovneva; Luke Zettlemoyer; Sewoong Oh; Ludwig Schmidt ...
- seed subtopic: 合成数据; type: 原始研究; cross: []
- arXiv comment: Accepted to COLM 2025
- URLs on first pages of PDF: https://huggingface.co/datasets/facebook/recycling
- pages: 22

ABSTRACT: Scaling laws predict that the performance of large language models improves with increasing model size and data size. In practice, pre-training has been relying on massive web crawls, using almost all data sources publicly available on the internet so far. However, this pool of natural data does not grow at the same rate as the compute supply. Furthermore, the availability of high-quality texts is even more limited: data filtering pipelines often remove up to 99% of the initial web scrapes to achieve state-of-the-art. To address the "data wall" of pre-training scaling, our work explores ways to transform and recycle data discarded in existing filtering processes. We propose REWIRE, REcycling the Web with guIded REwrite, a method to enrich low-quality documents so that they could become useful for training. This in turn allows us to increase the representation of synthetic data in the final pre-training set. Experiments at 1B, 3B and 7B scales of the DCLM benchmark show that mixing high-quality raw texts and our rewritten texts lead to 1.0, 1.3 and 2.5 percentage points improvement respectively across 22 diverse tasks, compared to training on only filtered web data. Training on the raw-synthetic data mix is also more effective than having access to 2x web data. Through further analysis, we demonstrate that about 82% of the mixed in texts come from transforming lower-quality documents that would otherwise be discarded. REWIRE also outperforms related approaches of generating synthetic data, including Wikipedia-style paraphrasing, question-answer synthesizing and knowledge extraction. These results suggest that recycling web texts holds the potential for being a simple and effective approach for scaling pre-training data. We make our high-quality synthetic data publicly available at https://huggingface.co/datasets/facebook/recycling_the_web.

## 02-045 | Strong Model Collapse
- arXiv: 2410.04840  first public: 2024-10-07  latest: 2024-10-08  primary cat: cs.LG
- authors (4): Elvis Dohmatob; Yunzhen Feng; Arjun Subramonian; Julia Kempe
- seed subtopic: 合成数据; type: 原始研究; cross: []
- pages: 34

ABSTRACT: Within the scaling laws paradigm, which underpins the training of large neural networks like ChatGPT and Llama, we consider a supervised regression setting and establish the existance of a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus. Our results show that even the smallest fraction of synthetic data (e.g., as little as 1\% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance. We further investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse. In a simplified regime where neural networks are approximated via random projections of tunable size, we both theoretically and empirically show that larger models can amplify model collapse. Interestingly, our theory also indicates that, beyond the interpolation threshold (which can be extremely high for very large datasets), larger models may mitigate the collapse, although they do not entirely prevent it. Our theoretical findings are empirically verified through experiments on language models and feed-forward neural networks for images.

## 02-047 | Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models
- arXiv: 2404.02936  first public: 2024-04-03  latest: 2025-02-12  primary cat: cs.CL
- authors (8): Jingyang Zhang; Jingwei Sun; Eric Yeats; Yang Ouyang; Martin Kuo; Jianyi Zhang ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: ICLR'25 Spotlight. Project page and code is available at https://zjysteven.github.io/mink-plus-plus/
- URLs on first pages of PDF: https://zjysteven.github.io/mink-plus-plus/
- pages: 18

ABSTRACT: The problem of pre-training data detection for large language models (LLMs) has received growing attention due to its implications in critical issues like copyright violation and test data contamination. Despite improved performance, existing methods (including the state-of-the-art, Min-K%) are mostly developed upon simple heuristics and lack solid, reasonable foundations. In this work, we propose a novel and theoretically motivated methodology for pre-training data detection, named Min-K%++. Specifically, we present a key insight that training samples tend to be local maxima of the modeled distribution along each input dimension through maximum likelihood training, which in turn allow us to insightfully translate the problem into identification of local maxima. Then, we design our method accordingly that works under the discrete distribution modeled by LLMs, whose core idea is to determine whether the input forms a mode or has relatively high probability under the conditional categorical distribution. Empirically, the proposed method achieves new SOTA performance across multiple settings. On the WikiMIA benchmark, Min-K%++ outperforms the runner-up by 6.2% to 10.5% in detection AUROC averaged over five models. On the more challenging MIMIR benchmark, it consistently improves upon reference-free methods while performing on par with reference-based method that requires an extra reference model.

## 02-048 | Benchmarking Benchmark Leakage in Large Language Models
- arXiv: 2404.18824  first public: 2024-04-29  latest: 2024-04-29  primary cat: cs.CL
- authors (4): Ruijie Xu; Zengzhi Wang; Run-Ze Fan; Pengfei Liu
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: 30 pages; Homepage: https://gair-nlp.github.io/benbench
- URLs on first pages of PDF: https://gair-nlp.github.io/benbench https://github.com/GAIR-NLP/benbench https://huggingface.co/spaces/GAIR/benbench
- pages: 30

ABSTRACT: Amid the expanding use of pre-training data, the phenomenon of benchmark dataset leakage has become increasingly prominent, exacerbated by opaque training processes and the often undisclosed inclusion of supervised data in contemporary Large Language Models (LLMs). This issue skews benchmark effectiveness and fosters potentially unfair comparisons, impeding the field's healthy development. To address this, we introduce a detection pipeline utilizing Perplexity and N-gram accuracy, two simple and scalable metrics that gauge a model's prediction precision on benchmark, to identify potential data leakages. By analyzing 31 LLMs under the context of mathematical reasoning, we reveal substantial instances of training even test set misuse, resulting in potentially unfair comparisons. These findings prompt us to offer several recommendations regarding model documentation, benchmark setup, and future evaluations. Notably, we propose the "Benchmark Transparency Card" to encourage clear documentation of benchmark utilization, promoting transparency and healthy developments of LLMs. we have made our leaderboard, pipeline implementation, and model predictions publicly available, fostering future research.

## 02-049 | A Careful Examination of Large Language Model Performance on Grade School Arithmetic
- arXiv: 2405.00332  first public: 2024-05-01  latest: 2024-11-22  primary cat: cs.CL
- authors (15): Hugh Zhang; Jeff Da; Dean Lee; Vaughn Robinson; Catherine Wu; Will Song ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: 2024 NeurIPS Camera Ready (Datasets and Benchmarks Track)
- pages: 45

ABSTRACT: Large language models (LLMs) have achieved impressive success on many benchmarks for mathematical reasoning. However, there is growing concern that some of this performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability. To investigate this claim rigorously, we commission Grade School Math 1000 (GSM1k). GSM1k is designed to mirror the style and complexity of the established GSM8k benchmark, the gold standard for measuring elementary mathematical reasoning. We ensure that the two benchmarks are comparable across important metrics such as human solve rates, number of steps in solution, answer magnitude, and more. When evaluating leading open- and closed-source LLMs on GSM1k, we observe accuracy drops of up to 8%, with several families of models showing evidence of systematic overfitting across almost all model sizes. Further analysis suggests a positive relationship (Spearman's r^2 = 0.36) between a model's probability of generating an example from GSM8k and its performance gap between GSM8k and GSM1k, suggesting that some models may have partially memorized GSM8k. Nevertheless, many models, especially those on the frontier, show minimal signs of overfitting, and all models broadly demonstrate generalization to novel math problems guaranteed to not be in their training data.

## 02-050 | Rethinking Benchmark and Contamination for Language Models with Rephrased Samples
- arXiv: 2311.04850  first public: 2023-11-08  latest: 2023-11-11  primary cat: cs.CL
- authors (5): Shuo Yang; Wei-Lin Chiang; Lianmin Zheng; Joseph E. Gonzalez; Ion Stoica
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- pages: 16

ABSTRACT: Large language models are increasingly trained on all the data ever produced by humans. Many have raised concerns about the trustworthiness of public benchmarks due to potential contamination in pre-training or fine-tuning datasets. While most data decontamination efforts apply string matching (e.g., n-gram overlap) to remove benchmark data, we show that these methods are insufficient, and simple variations of test data (e.g., paraphrasing, translation) can easily bypass these decontamination measures. Furthermore, we demonstrate that if such variation of test data is not eliminated, a 13B model can easily overfit a test benchmark and achieve drastically high performance, on par with GPT-4. We validate such observations in widely used benchmarks such as MMLU, GSK8k, and HumanEval. To address this growing risk, we propose a stronger LLM-based decontamination method and apply it to widely used pre-training and fine-tuning datasets, revealing significant previously unknown test overlap. For example, in pre-training sets such as RedPajama-Data-1T and StarCoder-Data, we identified that 8-18\% of the HumanEval benchmark overlaps. Interestingly, we also find such contamination in synthetic dataset generated by GPT-3.5/4, suggesting a potential risk of unintentional contamination. We urge the community to adopt stronger decontamination approaches when using public benchmarks. Moreover, we call for the community to actively develop fresh one-time exams to evaluate models accurately. Our decontamination tool is publicly available at https://github.com/lm-sys/llm-decontaminator.

## 02-052 | Do Membership Inference Attacks Work on Large Language Models?
- arXiv: 2402.07841  first public: 2024-02-12  latest: 2024-09-16  primary cat: cs.CL
- authors (10): Michael Duan; Anshuman Suri; Niloofar Mireshghallah; Sewon Min; Weijia Shi; Luke Zettlemoyer ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: Accepted at Conference on Language Modeling (COLM), 2024
- URLs on first pages of PDF: http://github.com/iamgroot42/ http://github.com/iamgroot42/mimir
- pages: 33

ABSTRACT: Membership inference attacks (MIAs) attempt to predict whether a particular datapoint is a member of a target model's training data. Despite extensive research on traditional machine learning models, there has been limited work studying MIA on the pre-training data of large language models (LLMs). We perform a large-scale evaluation of MIAs over a suite of language models (LMs) trained on the Pile, ranging from 160M to 12B parameters. We find that MIAs barely outperform random guessing for most settings across varying LLM sizes and domains. Our further analyses reveal that this poor performance can be attributed to (1) the combination of a large dataset and few training iterations, and (2) an inherently fuzzy boundary between members and non-members. We identify specific settings where LLMs have been shown to be vulnerable to membership inference and show that the apparent success in such settings can be attributed to a distribution shift, such as when members and non-members are drawn from the seemingly identical domain but with different temporal ranges. We release our code and data as a unified benchmark package that includes all existing MIAs, supporting future work.

## 02-053 | Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models
- arXiv: 2402.15938  first public: 2024-02-24  latest: 2024-05-31  primary cat: cs.CL
- authors (7): Yihong Dong; Xue Jiang; Huanyu Liu; Zhi Jin; Bin Gu; Mengfei Yang ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: Accepted to ACL
- URLs on first pages of PDF: https://github.com/YihongDong/CDD-TED4LLMs
- pages: 13

ABSTRACT: Recent statements about the impressive capabilities of large language models (LLMs) are usually supported by evaluating on open-access benchmarks. Considering the vast size and wide-ranging sources of LLMs' training data, it could explicitly or implicitly include test data, leading to LLMs being more susceptible to data contamination. However, due to the opacity of training data, the black-box access of models, and the rapid growth of synthetic training data, detecting and mitigating data contamination for LLMs faces significant challenges. In this paper, we propose CDD, which stands for Contamination Detection via output Distribution for LLMs. CDD necessitates only the sampled texts to detect data contamination, by identifying the peakedness of LLM's output distribution. To mitigate the impact of data contamination in evaluation, we also present TED: Trustworthy Evaluation via output Distribution, based on the correction of LLM's output distribution. To facilitate this study, we introduce two benchmarks, i.e., DetCon and ComiEval, for data contamination detection and contamination mitigation evaluation tasks. Extensive experimental results show that CDD achieves the average relative improvements of 21.8\%-30.2\% over other contamination detection approaches in terms of Accuracy, F1 Score, and AUC metrics, and can effectively detect implicit contamination. TED substantially mitigates performance improvements up to 66.9\% attributed to data contamination across various contamination setups. In real-world applications, we reveal that ChatGPT exhibits a high potential to suffer from data contamination on HumanEval benchmark.

## 02-055 | A Survey on Data Contamination for Large Language Models
- arXiv: 2502.14425  first public: 2025-02-20  latest: 2025-06-05  primary cat: cs.CL
- authors (3): Yuxing Cheng; Yi Chang; Yuan Wu
- seed subtopic: 数据污染; type: 综述; cross: ['12']
- pages: 15

ABSTRACT: Recent advancements in Large Language Models (LLMs) have demonstrated significant progress in various areas, such as text generation and code synthesis. However, the reliability of performance evaluation has come under scrutiny due to data contamination-the unintended overlap between training and test datasets. This overlap has the potential to artificially inflate model performance, as LLMs are typically trained on extensive datasets scraped from publicly available sources. These datasets often inadvertently overlap with the benchmarks used for evaluation, leading to an overestimation of the models' true generalization capabilities. In this paper, we first examine the definition and impacts of data contamination. Secondly, we review methods for contamination-free evaluation, focusing on three strategies: data updating-based methods, data rewriting-based methods, and prevention-based methods. Specifically, we highlight dynamic benchmarks and LLM-driven evaluation methods. Finally, we categorize contamination detecting methods based on model information dependency: white-Box, gray-Box, and black-Box detection approaches. Our survey highlights the requirements for more rigorous evaluation protocols and proposes future directions for addressing data contamination challenges.

## 02-056 | A Survey on Data Selection for Language Models
- arXiv: 2402.16827  first public: 2024-02-26  latest: 2024-08-02  primary cat: cs.CL
- authors (14): Alon Albalak; Yanai Elazar; Sang Michael Xie; Shayne Longpre; Nathan Lambert; Xinyi Wang ...
- seed subtopic: 质量筛选; type: 综述; cross: []
- arXiv comment: Paper list available at https://github.com/alon-albalak/data-selection-survey
- pages: 81

ABSTRACT: A major factor in the recent success of large language models is the use of enormous and ever-growing text datasets for unsupervised pre-training. However, naively training a model on all available data may not be optimal (or feasible), as the quality of available text data can vary. Filtering out data can also decrease the carbon footprint and financial costs of training models by reducing the amount of training required. Data selection methods aim to determine which candidate data points to include in the training dataset and how to appropriately sample from the selected data points. The promise of improved data selection methods has caused the volume of research in the area to rapidly expand. However, because deep learning is mostly driven by empirical evidence and experimentation on large-scale data is expensive, few organizations have the resources for extensive data selection research. Consequently, knowledge of effective data selection practices has become concentrated within a few organizations, many of which do not openly share their findings and methodologies. To narrow this gap in knowledge, we present a comprehensive review of existing literature on data selection methods and related research areas, providing a taxonomy of existing approaches. By describing the current landscape of research, this work aims to accelerate progress in data selection by establishing an entry point for new and established researchers. Additionally, throughout this review we draw attention to noticeable holes in the literature and conclude the paper by proposing promising avenues for future research.

## 02-058 | Deduplicating Training Data Makes Language Models Better
- arXiv: 2107.06499  first public: 2021-07-14  latest: 2022-03-24  primary cat: cs.CL
- authors (7): Katherine Lee; Daphne Ippolito; Andrew Nystrom; Chiyuan Zhang; Douglas Eck; Chris Callison-Burch ...
- seed subtopic: 去重; type: 原始研究; cross: []
- arXiv comment: Accepted to ACL 2022
- URLs on first pages of PDF: https://github.com/goog/l.Vare-research/
- pages: 22

ABSTRACT: We find that existing language modeling datasets contain many near-duplicate examples and long repetitive substrings. As a result, over 1% of the unprompted output of language models trained on these datasets is copied verbatim from the training data. We develop two tools that allow us to deduplicate training datasets -- for example removing from C4 a single 61 word English sentence that is repeated over 60,000 times. Deduplication allows us to train models that emit memorized text ten times less frequently and require fewer train steps to achieve the same or better accuracy. We can also reduce train-test overlap, which affects over 4% of the validation set of standard datasets, thus allowing for more accurate evaluation. We release code for reproducing our work and performing dataset deduplication at https://github.com/google-research/deduplicate-text-datasets.

## 02-059 | The RefinedWeb Dataset for Falcon LLM: Outperforming Curated Corpora with Web Data, and Web Data Only
- arXiv: 2306.01116  first public: 2023-06-01  latest: 2023-06-01  primary cat: cs.CL
- authors (9): Guilherme Penedo; Quentin Malartic; Daniel Hesslow; Ruxandra Cojocaru; Alessandro Cappelli; Hamza Alobeidli ...
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/datasets/tiiuae/falcon-refinedweb
- pages: 32

ABSTRACT: Large language models are commonly trained on a mixture of filtered web data and curated high-quality corpora, such as social media conversations, books, or technical papers. This curation process is believed to be necessary to produce performant models with broad zero-shot generalization abilities. However, as larger models requiring pretraining on trillions of tokens are considered, it is unclear how scalable is curation and whether we will run out of unique high-quality data soon. At variance with previous beliefs, we show that properly filtered and deduplicated web data alone can lead to powerful models; even significantly outperforming models from the state-of-the-art trained on The Pile. Despite extensive filtering, the high-quality data we extract from the web is still plentiful, and we are able to obtain five trillion tokens from CommonCrawl. We publicly release an extract of 600 billion tokens from our RefinedWeb dataset, and 1.3/7.5B parameters language models trained on it.

## 02-060 | DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining
- arXiv: 2305.10429  first public: 2023-05-17  latest: 2023-11-21  primary cat: cs.CL
- authors (10): Sang Michael Xie; Hieu Pham; Xuanyi Dong; Nan Du; Hanxiao Liu; Yifeng Lu ...
- seed subtopic: 数据配比; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2023
- pages: 27

ABSTRACT: The mixture proportions of pretraining data domains (e.g., Wikipedia, books, web text) greatly affect language model (LM) performance. In this paper, we propose Domain Reweighting with Minimax Optimization (DoReMi), which first trains a small proxy model using group distributionally robust optimization (Group DRO) over domains to produce domain weights (mixture proportions) without knowledge of downstream tasks. We then resample a dataset with these domain weights and train a larger, full-sized model. In our experiments, we use DoReMi on a 280M-parameter proxy model to set the domain weights for training an 8B-parameter model (30x larger) more efficiently. On The Pile, DoReMi improves perplexity across all domains, even when it downweights a domain. DoReMi improves average few-shot downstream accuracy by 6.5% points over a baseline model trained using The Pile's default domain weights and reaches the baseline accuracy with 2.6x fewer training steps. On the GLaM dataset, DoReMi, which has no knowledge of downstream tasks, even matches the performance of using domain weights tuned on downstream tasks.

## 02-061 | Detecting Pretraining Data from Large Language Models
- arXiv: 2310.16789  first public: 2023-10-25  latest: 2024-03-09  primary cat: cs.CL
- authors (8): Weijia Shi; Anirudh Ajith; Mengzhou Xia; Yangsibo Huang; Daogao Liu; Terra Blevins ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- pages: 23

ABSTRACT: Although large language models (LLMs) are widely deployed, the data used to train them is rarely disclosed. Given the incredible scale of this data, up to trillions of tokens, it is all but certain that it includes potentially problematic text such as copyrighted materials, personally identifiable information, and test data for widely reported reference benchmarks. However, we currently have no way to know which data of these types is included or in what proportions. In this paper, we study the pretraining data detection problem: given a piece of text and black-box access to an LLM without knowing the pretraining data, can we determine if the model was trained on the provided text? To facilitate this study, we introduce a dynamic benchmark WIKIMIA that uses data created before and after model training to support gold truth detection. We also introduce a new detection method Min-K% Prob based on a simple hypothesis: an unseen example is likely to contain a few outlier words with low probabilities under the LLM, while a seen example is less likely to have words with such low probabilities. Min-K% Prob can be applied without any knowledge about the pretraining corpus or any additional training, departing from previous detection methods that require training a reference model on data that is similar to the pretraining data. Moreover, our experiments demonstrate that Min-K% Prob achieves a 7.4% improvement on WIKIMIA over these previous methods. We apply Min-K% Prob to three real-world scenarios, copyrighted book detection, contaminated downstream example detection and privacy auditing of machine unlearning, and find it a consistently effective solution.

## 02-070 | How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Prompt Design, Generator Model, and Source Data
- arXiv: 2604.13977  first public: 2026-04-15  latest: 2026-07-30  primary cat: cs.CL
- authors (12): Joel Niklaus; Atsuki Yamaguchi; Michal Štefánik; Guilherme Penedo; Hynek Kydlíček; Elie Bakouch ...
- seed subtopic: 合成数据; type: 原始研究; cross: []
- arXiv comment: Accepted to COLM 2026
- URLs on first pages of PDF: https://github.com/huggingface/finephrase
- pages: 35

ABSTRACT: Synthetic data is a standard component in training large language models, yet systematic comparisons across design dimensions, including rephrasing strategy, generator model, and source data, remain absent. We conduct extensive controlled experiments, generating over one trillion tokens, to identify critical factors in rephrasing web text into synthetic pretraining data. Our results reveal that structured output formats, such as tables, math problems, FAQs, and tutorials, consistently outperform both curated web baselines and prior synthetic methods. Notably, increasing the size of the generator model beyond 1B parameters provides no additional benefit. Our analysis also demonstrates that the selection of the original data used for mixing substantially influences performance. By applying our findings, we develop \textbf{\textsc{FinePhrase}}, a 486-billion-token open dataset of rephrased web text. We show that \textsc{FinePhrase} outperforms all existing synthetic data baselines while reducing generation costs by up to 30 times. We provide the dataset, all prompts, and the generation framework to the research community.

## 02-071 | Soft Contamination Means Benchmarks Test Shallow Generalization
- arXiv: 2602.12413  first public: 2026-02-12  latest: 2026-02-12  primary cat: cs.LG
- authors (7): Ari Spiesberger; Juan J. Vazquez; Nicky Pochinkov; Tomáš Gavenčiak; Peli Grietzer; Gavin Leech ...
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- URLs on first pages of PDF: https://github.com/AriSpiesberger/
- pages: 26

ABSTRACT: If LLM training data is polluted with benchmark test data, then benchmark performance gives biased estimates of out-of-distribution (OOD) generalization. Typical decontamination filters use n-gram matching which fail to detect semantic duplicates: sentences with equivalent (or near-equivalent) content that are not close in string space. We study this soft contamination of training data by semantic duplicates. Among other experiments, we embed the Olmo3 training corpus and find that: 1) contamination remains widespread, e.g. we find semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems; 2) including semantic duplicates of benchmark data in training does improve benchmark performance; and 3) when finetuning on duplicates of benchmark datapoints, performance also improves on truly-held-out datapoints from the same benchmark. We argue that recent benchmark gains are thus confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data and effective test data in growing training corpora.

## 02-072 | The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection
- arXiv: 2606.03305  first public: 2026-06-02  latest: 2026-07-01  primary cat: cs.AI
- authors (3): Wojciech Zarzecki; Jan Dubiński; Sebastian Cygert
- seed subtopic: 数据污染; type: 原始研究; cross: ['12']
- arXiv comment: accepted to ECML PKDD 2026
- pages: 24

ABSTRACT: Benchmark contamination, where evaluation examples appear in a model's training data, threatens the validity of LLM assessment. Statistical tools for detecting training-data membership exist, but have been validated almost exclusively in controlled academic regimes: large, homogeneous pre-training corpora and transparent, single-stage training pipelines. Whether these methods remain reliable in realistic auditing scenarios remains unclear. We identify two under-studied failure modes: distribution shift, which arises when suspect and validation sets violate the IID assumption, and scale constraints, which arise because benchmarks are orders of magnitude smaller than pre-training corpora. We systematically evaluate three leading paradigms, LLM Dataset Inference, Post-Hoc Dataset Inference, and CoDeC, across 25 models from multiple families (including Pythia, OLMo 2, and specialised cultural and medical LLMs) and scales (up to 27B). We then further extend our analysis to frontier industry models. Across 335 evaluations, only 201 yield correct outcomes. LLM Dataset Inference results in false positives under distribution shift, Post-Hoc Dataset Inference is underpowered at benchmark scale, and CoDeC provides only coarse provenance signals that are insufficient to verify individual benchmark splits. Our results reveal a systematic reliability gap between controlled validation and practical benchmark auditing, and show that statistical detection cannot yet replace transparent data provenance. We open-source our benchmark for further research.

## 02-073 | Hubs or Fringes: Pretraining Data Selection via Web Graph Centrality
- arXiv: 2606.11499  first public: 2026-06-09  latest: 2026-06-09  primary cat: cs.CL
- authors (3): Vedant Badoni; Danqi Chen; Xinyi Wang
- seed subtopic: 质量筛选; type: 原始研究; cross: []
- arXiv comment: 10 pages
- pages: 23

ABSTRACT: The performance of modern language models depends critically on pretraining data composition. Yet existing data selection methods rely on auxiliary classifiers for document scoring or mixture optimization, adding computational overhead and dependence on labeled data. We propose WebGraphMix, a lightweight data selection framework that computes structural centrality scores over the Common Crawl host-level web graph and uses them to vary the proportion of central versus peripheral documents in the pretraining mixture. We hypothesize that central hosts expose models to reusable abstractions, while peripheral hosts encode specialized, long-tail knowledge. WebGraphMix computes centrality scores efficiently at web scale, requiring no model training, labeled data, or downstream supervision. We integrate WebGraphMix into the DataComp-LM pipeline and train models at 400M and 1B parameter scales with 8B and 28B tokens respectively, evaluating on 23 tasks ranging from factual knowledge to symbolic reasoning. Our experiments show that central and peripheral web regions encode complementary capabilities. Mixture combining both at a ratio of 1:1 achieves 41.4% on average, compared to 39.8% for uniform sampling. Combining structural scores with document-level quality classifier scores further improves performance to 43.8%. These findings demonstrate that web graph topology is a meaningful axis for pretraining data curation, capturing information that is largely orthogonal to existing content-based approaches.

## 02-074 | Olmix: A Framework for Data Mixing Throughout LM Development
- arXiv: 2602.12237  first public: 2026-02-12  latest: 2026-02-12  primary cat: cs.LG
- authors (8): Mayee F. Chen; Tyler Murray; David Heineman; Matt Jordan; Hannaneh Hajishirzi; Christopher Ré ...
- seed subtopic: 数据配比; type: 原始研究; cross: []
- pages: 58

ABSTRACT: Data mixing -- determining the ratios of data from different domains -- is a first-order concern for training language models (LMs). While existing mixing methods show promise, they fall short when applied during real-world LM development. We present Olmix, a framework that addresses two such challenges. First, the configuration space for developing a mixing method is not well understood -- design choices across existing methods lack justification or consensus and overlook practical issues like data constraints. We conduct a comprehensive empirical study of this space, identifying which design choices lead to a strong mixing method. Second, in practice, the domain set evolves throughout LM development as datasets are added, removed, partitioned, and revised -- a problem setting largely unaddressed by existing works, which assume fixed domains. We study how to efficiently recompute the mixture after the domain set is updated, leveraging information from past mixtures. We introduce mixture reuse, a mechanism that reuses existing ratios and recomputes ratios only for domains affected by the update. Over a sequence of five domain-set updates mirroring real-world LM development, mixture reuse matches the performance of fully recomputing the mix after each update with 74% less compute and improves over training without mixing by 11.6% on downstream tasks.

## 02-075 | Data Mixing for Large Language Models Pretraining: A Survey and Outlook
- arXiv: 2604.16380  first public: 2026-03-25  latest: 2026-03-25  primary cat: cs.CL
- authors (4): Zhuo Chen; Yuxuan Miao; Supryadi; Deyi Xiong
- seed subtopic: 数据配比; type: 综述; cross: []
- arXiv comment: 41 pages, 4 figures, 1 table
- journal_ref: Data Intelligence 8 (2026), Art. No. 2026r01
- doi: 10.3724/2096-7004.di.2026.0055
- pages: 41

ABSTRACT: Large language models (LLMs) rely on pretraining on massive and heterogeneous corpora, where training data composition has a decisive impact on training efficiency and downstream generalization under realistic compute and data budget constraints. Unlike sample-level data selection, data mixing optimizes domain-level sampling weights to allocate limited budgets more effectively. In recent years, a growing body of work has proposed principled data mixing methods for LLM pretraining; however, the literature remains fragmented and lacks a dedicated, systematic survey. This paper provides a comprehensive review of data mixing for LLM pretraining. We first formalize data mixture optimization as a bilevel problem on the probability simplex and clarify the role of data mixing in the pretraining pipeline, and briefly explain how existing methods make this formulation tractable in practice. We then introduce a fine-grained taxonomy that organizes existing methods along two dimensions: static versus dynamic mixing. Static mixing is further categorized into rule-based and learning-based methods, while dynamic mixing is grouped into adaptive and externally guided families. For each class, we summarize representative approaches and analyze their strengths and limitations from a performance-cost trade-off perspective. Building on this analysis, we highlight challenges that cut across methods, including limited transferability across data domains, optimization objectives, models, and validation sets, as well as unstandardized evaluation protocols and benchmarks, and the inherent tension between performance gains and cost control in learning-based methods. Finally, we outline several exploratory directions, including finer-grained domain partitioning and inverse data mixing, as well as pipeline-aware designs, aiming to provide conceptual and methodological insights for future research.

## 02-076 | Mix, MinHash, and Match: Cross-Source Agreement for Multilingual Pretraining Datasets
- arXiv: 2512.18834  first public: 2025-12-21  latest: 2026-01-29  primary cat: cs.CL
- authors (2): Sultan Alrashed; Francesco Orabona
- seed subtopic: 去重; type: 原始研究; cross: []
- arXiv comment: Multilingual LLM pretraining dataset curation
- URLs on first pages of PDF: https://huggingface.co/collections/AdaMLLab/mixminmatch
- pages: 26

ABSTRACT: Multilingual data from the web is essential for LLM pretraining. Yet, scraping it is expensive, and research groups repeatedly crawl the same content. For example, we found that over 40\% of tokens across major Arabic web corpora are duplicated between sources. In this work, we propose to use this wasteful redundancy as a quality signal to create high-quality pretraining datasets. Our key insight is that cross-source agreement functions as a free, model-free quality filter: content retained by multiple independent pipelines is more likely to represent high-quality text. Crucially, this signal requires no additional computation beyond standard deduplication, which is already performed at scale when pretraining language models. So, we propose MixMinMatch, a method that combines multiple existing web corpora, performs cross-dataset MinHash deduplication, and identifies documents independently recovered by multiple sources. We apply MixMinMatch to Arabic, Turkish, and Hindi, producing corpora that match or exceed the quality of the best single-source baselines, while providing up to 4$\times$ more unique tokens. On Arabic, our matched subset achieves a 4.5\% relative improvement over ArabicWeb24, while on Turkish, we improve over FineWeb-2 by 5.5\%. We release the datasets at: https://huggingface.co/collections/AdaMLLab/mixminmatch

## 02-079 | SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training
- arXiv: 2407.06654  first public: 2024-07-09  latest: 2024-07-09  primary cat: cs.CL
- authors (9): Nan He; Weichen Xiong; Hanwen Liu; Yi Liao; Lei Ding; Kai Zhang ...
- seed subtopic: 去重; type: 原始研究; cross: []
- arXiv comment: 12 pages, 7 figures
- pages: 12

ABSTRACT: The effectiveness of large language models (LLMs) is often hindered by duplicated data in their extensive pre-training datasets. Current approaches primarily focus on detecting and removing duplicates, which risks the loss of valuable information and neglects the varying degrees of duplication. To address this, we propose a soft deduplication method that maintains dataset integrity while selectively reducing the sampling weight of data with high commonness. Central to our approach is the concept of "data commonness", a metric we introduce to quantify the degree of duplication by measuring the occurrence probabilities of samples using an n-gram model. Empirical analysis shows that this method significantly improves training efficiency, achieving comparable perplexity scores with at least a 26% reduction in required training steps. Additionally, it enhances average few-shot downstream accuracy by 1.77% when trained for an equivalent duration. Importantly, this approach consistently improves performance, even on rigorously deduplicated datasets, indicating its potential to complement existing methods and become a standard pre-training process for LLMs.
