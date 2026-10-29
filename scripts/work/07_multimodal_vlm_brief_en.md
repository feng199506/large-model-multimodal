# Brief for annotation: 07 多模态基础与视觉语言模型

## 07-057 | Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing
- arXiv: 2603.24326  first public: 2026-03-25  latest: 2026-04-03  primary cat: cs.CV
- authors (18): Cheng Cui; Ting Sun; Suyin Liang; Tingquan Gao; Zelun Zhang; Jiaxuan Liu ...
- seed subtopic: OCR; type: 原始研究; cross: []
- arXiv comment: Accepted by CVPR2026
- pages: 55

ABSTRACT: Document parsing is a fine-grained task where image resolution significantly impacts performance. While advanced research leveraging vision-language models benefits from high-resolution input to boost model performance, this often leads to a quadratic increase in the number of vision tokens and significantly raises computational costs. We attribute this inefficiency to substantial visual regions redundancy in document images, like background. To tackle this, we propose PaddleOCR-VL, a novel coarse-to-fine architecture that focuses on semantically relevant regions while suppressing redundant ones, thereby improving both efficiency and performance. Specifically, we introduce a lightweight Valid Region Focus Module (VRFM) which leverages localization and contextual relationship prediction capabilities to identify valid vision tokens. Subsequently, we design and train a compact yet powerful 0.9B vision-language model (PaddleOCR-VL-0.9B) to perform detailed recognition, guided by VRFM outputs to avoid direct processing of the entire large image. Extensive experiments demonstrate that PaddleOCR-VL achieves state-of-the-art performance in both page-level parsing and element-level recognition. It significantly outperforms existing solutions, exhibits strong competitiveness against top-tier VLMs, and delivers fast inference while utilizing substantially fewer vision tokens and parameters, highlighting the effectiveness of targeted coarse-to-fine parsing for accurate and efficient document understanding. The source code and models are publicly available at https://github.com/PaddlePaddle/PaddleOCR.

## 07-056 | LLaVA-UHD v3: Progressive Visual Compression for Efficient Native-Resolution Encoding in MLLMs
- arXiv: 2511.21150  first public: 2025-11-26  latest: 2025-11-26  primary cat: cs.CV
- authors (9): Shichu Sun; Yichen Zhang; Haolin Song; Zonghao Guo; Chi Chen; Yidan Zhang ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- pages: 25

ABSTRACT: Visual encoding followed by token condensing has become the standard architectural paradigm in multi-modal large language models (MLLMs). Many recent MLLMs increasingly favor global native- resolution visual encoding over slice-based methods. To investigate this trend, we systematically compare their behavior on vision-language understanding and attention patterns, revealing that global encoding enhances overall capability but at the expense of greater computational overhead. To address this issue, we present LLaVA-UHD v3, an MLLM centered upon our proposed Progressive Visual Compression (PVC) method, which can be seamlessly integrated into standard Vision Transformer (ViT) to enable efficient native-resolution encoding. The PVC approach consists of two key modules: (i) refined patch embedding, which supports flexible patch-size scaling for fine-grained visual model- ing, (ii) windowed token compression, hierarchically deployed across ViT layers to progressively aggregate local token representations. Jointly modulated by these two modules, a widely pretrained ViT can be reconfigured into an efficient architecture while largely preserving generality. Evaluated across extensive benchmarks, the transformed ViT, termed ViT-UHD, demonstrates competitive performance with MoonViT while reducing TTFT (time-to-first-token) by 2.4x, when developed within an identical MLLM architecture. Building upon ViT-UHD, LLaVA-UHD v3 also achieves competitive performance to Qwen2-VL, while further reducing TTFT by 1.9x. We will release all code and checkpoints to support future research on efficient MLLMs.

## 07-001 | Learning Transferable Visual Models From Natural Language Supervision
- arXiv: 2103.00020  first public: 2021-02-26  latest: 2021-02-26  primary cat: cs.CV
- authors (12): Alec Radford; Jong Wook Kim; Chris Hallacy; Aditya Ramesh; Gabriel Goh; Sandhini Agarwal ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/OpenAI/CLIP
- pages: 48

ABSTRACT: State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

## 07-002 | Flamingo: a Visual Language Model for Few-Shot Learning
- arXiv: 2204.14198  first public: 2022-04-29  latest: 2022-11-15  primary cat: cs.CV
- authors (27): Jean-Baptiste Alayrac; Jeff Donahue; Pauline Luc; Antoine Miech; Iain Barr; Yana Hasson ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- arXiv comment: 54 pages. In Proceedings of Neural Information Processing Systems (NeurIPS) 2022
- pages: 54

ABSTRACT: Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research. We introduce Flamingo, a family of Visual Language Models (VLM) with this ability. We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs. Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities. We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks. These include open-ended tasks such as visual question-answering, where the model is prompted with a question which it has to answer; captioning tasks, which evaluate the ability to describe a scene or an event; and close-ended tasks such as multiple-choice visual question-answering. For tasks lying anywhere on this spectrum, a single Flamingo model can achieve a new state of the art with few-shot learning, simply by prompting the model with task-specific examples. On numerous benchmarks, Flamingo outperforms models fine-tuned on thousands of times more task-specific data.

## 07-003 | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
- arXiv: 2301.12597  first public: 2023-01-30  latest: 2023-06-15  primary cat: cs.CV
- authors (4): Junnan Li; Dongxu Li; Silvio Savarese; Steven Hoi
- seed subtopic: 表示融合; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/salesforce/LAVIS/tree/main/projects/blip2
- pages: 13

ABSTRACT: The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models. This paper proposes BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages. The first stage bootstraps vision-language representation learning from a frozen image encoder. The second stage bootstraps vision-to-language generative learning from a frozen language model. BLIP-2 achieves state-of-the-art performance on various vision-language tasks, despite having significantly fewer trainable parameters than existing methods. For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters. We also demonstrate the model's emerging capabilities of zero-shot image-to-text generation that can follow natural language instructions.

## 07-004 | Visual Instruction Tuning
- arXiv: 2304.08485  first public: 2023-04-17  latest: 2023-12-11  primary cat: cs.CV
- authors (4): Haotian Liu; Chunyuan Li; Qingyang Wu; Yong Jae Lee
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2023 Oral; project page: https://llava-vl.github.io/
- pages: 25

ABSTRACT: Instruction tuning large language models (LLMs) using machine-generated instruction-following data has improved zero-shot capabilities on new tasks, but the idea is less explored in the multimodal field. In this paper, we present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.Our early experiments show that LLaVA demonstrates impressive multimodel chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%. We make GPT-4 generated visual instruction tuning data, our model and code base publicly available.

## 07-005 | SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features
- arXiv: 2502.14786  first public: 2025-02-20  latest: 2025-02-20  primary cat: cs.CV
- authors (14): Michael Tschannen; Alexey Gritsenko; Xiao Wang; Muhammad Ferjad Naeem; Ibrahim Alabdulmohsin; Nikhil Parthasarathy ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: Model checkpoints are available at https://github.com/google-research/big_vision/tree/main/big_vision/configs/proj/image_text/README_siglip2.md
- URLs on first pages of PDF: https://github.com/google-research/big_vision/tree/main/
- pages: 20

ABSTRACT: We introduce SigLIP 2, a family of new multilingual vision-language encoders that build on the success of the original SigLIP. In this second iteration, we extend the original image-text training objective with several prior, independently developed techniques into a unified recipe -- this includes captioning-based pretraining, self-supervised losses (self-distillation, masked prediction) and online data curation. With these changes, SigLIP 2 models outperform their SigLIP counterparts at all model scales in core capabilities, including zero-shot classification, image-text retrieval, and transfer performance when extracting visual representations for Vision-Language Models (VLMs). Furthermore, the new training recipe leads to significant improvements on localization and dense prediction tasks. We also train variants which support multiple resolutions and preserve the input's native aspect ratio. Finally, we train on a more diverse data-mixture that includes de-biasing techniques, leading to much better multilingual understanding and improved fairness. To allow users to trade off inference cost with performance, we release model checkpoints at four sizes: ViT-B (86M), L (303M), So400m (400M), and g (1B).

## 07-007 | Perception Encoder: The best visual embeddings are not at the output of the network
- arXiv: 2504.13181  first public: 2025-04-17  latest: 2025-04-28  primary cat: cs.CV
- authors (18): Daniel Bolya; Po-Yao Huang; Peize Sun; Jang Hyun Cho; Andrea Madotto; Chen Wei ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: Updated refs, fixed typos, and added new COCO SotA: 66.0 val mAP! Code, models, and data at https://github.com/facebookresearch/perception_models
- URLs on first pages of PDF: https://github.com/facebookresearch/perception_models
- pages: 44

ABSTRACT: We introduce Perception Encoder (PE), a state-of-the-art vision encoder for image and video understanding trained via simple vision-language learning. Traditionally, vision encoders have relied on a variety of pretraining objectives, each tailored to specific downstream tasks such as classification, captioning, or localization. Surprisingly, after scaling our carefully tuned image pretraining recipe and refining with our robust video data engine, we find that contrastive vision-language training alone can produce strong, general embeddings for all of these downstream tasks. There is only one caveat: these embeddings are hidden within the intermediate layers of the network. To draw them out, we introduce two alignment methods: language alignment for multimodal language modeling, and spatial alignment for dense prediction. Together, our PE family of models achieves best-in-class results on a wide variety of tasks, including (1) zero-shot image and video classification and retrieval, simultaneously obtaining 86.6 average zero-shot ImageNet robustness and 76.9 zero-shot Kinetics-400 video classification; (2) document, image, and video Q&A, enabling 94.6 DocVQA, 80.9 InfographicVQA, and 82.7 PerceptionTest with an 8B LLM; and (3) spatial tasks such as detection, tracking, and depth estimation, setting a new COCO state-of-the-art of 66.0 box mAP. To foster further research, we release our models, code, and novel dataset of synthetically and human-annotated videos: https://github.com/facebookresearch/perception_models

## 07-011 | The Platonic Representation Hypothesis
- arXiv: 2405.07987  first public: 2024-05-13  latest: 2024-07-25  primary cat: cs.LG
- authors (4): Minyoung Huh; Brian Cheung; Tongzhou Wang; Phillip Isola
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: Equal contributions. Project: https://phillipi.github.io/prh/ Code: https://github.com/minyoungg/platonic-rep
- pages: 27

ABSTRACT: We argue that representations in AI models, particularly deep networks, are converging. First, we survey many examples of convergence in the literature: over time and across multiple domains, the ways by which different neural networks represent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato's concept of an ideal reality. We term such a representation the platonic representation and discuss several possible selective pressures toward it. Finally, we discuss the implications of these trends, their limitations, and counterexamples to our analysis.

## 07-012 | Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs
- arXiv: 2401.06209  first public: 2024-01-11  latest: 2024-04-25  primary cat: cs.CV
- authors (6): Shengbang Tong; Zhuang Liu; Yuexiang Zhai; Yi Ma; Yann LeCun; Saining Xie
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: Project page: https://tsb0601.github.io/mmvp_blog/
- pages: 18

ABSTRACT: Is vision good enough for language? Recent advancements in multimodal models primarily stem from the powerful reasoning abilities of large language models (LLMs). However, the visual component typically depends only on the instance-level contrastive language-image pre-training (CLIP). Our research reveals that the visual capabilities in recent multimodal LLMs (MLLMs) still exhibit systematic shortcomings. To understand the roots of these errors, we explore the gap between the visual embedding space of CLIP and vision-only self-supervised learning. We identify ''CLIP-blind pairs'' - images that CLIP perceives as similar despite their clear visual differences. With these pairs, we construct the Multimodal Visual Patterns (MMVP) benchmark. MMVP exposes areas where state-of-the-art systems, including GPT-4V, struggle with straightforward questions across nine basic visual patterns, often providing incorrect answers and hallucinated explanations. We further evaluate various CLIP-based vision-and-language models and found a notable correlation between visual patterns that challenge CLIP models and those problematic for multimodal LLMs. As an initial effort to address these issues, we propose a Mixture of Features (MoF) approach, demonstrating that integrating vision self-supervised learning features with MLLMs can significantly enhance their visual grounding capabilities. Together, our research suggests visual representation learning remains an open challenge, and accurate visual grounding is crucial for future successful multimodal systems.

## 07-013 | Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs
- arXiv: 2406.16860  first public: 2024-06-24  latest: 2024-12-04  primary cat: cs.CV
- authors (14): Shengbang Tong; Ellis Brown; Penghao Wu; Sanghyun Woo; Manoj Middepogu; Sai Charitha Akula ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024 (Oral). Website at https://cambrian-mllm.github.io
- URLs on first pages of PDF: https://github.com/cambrian-mllm/cambrian https://github.com/cambrian-mllm/cambrian#evaluation https://huggingface.co/datasets/nyu-visionx/CV-Bench https://huggingface.co/datasets/nyu-visionx/Cambrian-10M https://huggingface.co/nyu-visionx/
- pages: 51

ABSTRACT: We introduce Cambrian-1, a family of multimodal LLMs (MLLMs) designed with a vision-centric approach. While stronger language models can enhance multimodal capabilities, the design choices for vision components are often insufficiently explored and disconnected from visual representation learning research. This gap hinders accurate sensory grounding in real-world scenarios. Our study uses LLMs and visual instruction tuning as an interface to evaluate various visual representations, offering new insights into different models and architectures -- self-supervised, strongly supervised, or combinations thereof -- based on experiments with over 20 vision encoders. We critically examine existing MLLM benchmarks, address the difficulties involved in consolidating and interpreting results from various tasks, and introduce a new vision-centric benchmark, CV-Bench. To further improve visual grounding, we propose the Spatial Vision Aggregator (SVA), a dynamic and spatially-aware connector that integrates high-resolution vision features with LLMs while reducing the number of tokens. Additionally, we discuss the curation of high-quality visual instruction-tuning data from publicly available sources, emphasizing the importance of data source balancing and distribution ratio. Collectively, Cambrian-1 not only achieves state-of-the-art performance but also serves as a comprehensive, open cookbook for instruction-tuned MLLMs. We provide model weights, code, supporting tools, datasets, and detailed instruction-tuning and evaluation recipes. We hope our release will inspire and accelerate advancements in multimodal systems and visual representation learning.

## 07-014 | MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training
- arXiv: 2403.09611  first public: 2024-03-14  latest: 2024-04-18  primary cat: cs.CV
- authors (32): Brandon McKinzie; Zhe Gan; Jean-Philippe Fauconnier; Sam Dodge; Bowen Zhang; Philipp Dufter ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- pages: 41

ABSTRACT: In this work, we discuss building performant Multimodal Large Language Models (MLLMs). In particular, we study the importance of various architecture components and data choices. Through careful and comprehensive ablations of the image encoder, the vision language connector, and various pre-training data choices, we identified several crucial design lessons. For example, we demonstrate that for large-scale multimodal pre-training using a careful mix of image-caption, interleaved image-text, and text-only data is crucial for achieving state-of-the-art (SOTA) few-shot results across multiple benchmarks, compared to other published pre-training results. Further, we show that the image encoder together with image resolution and the image token count has substantial impact, while the vision-language connector design is of comparatively negligible importance. By scaling up the presented recipe, we build MM1, a family of multimodal models up to 30B parameters, including both dense models and mixture-of-experts (MoE) variants, that are SOTA in pre-training metrics and achieve competitive performance after supervised fine-tuning on a range of established multimodal benchmarks. Thanks to large-scale pre-training, MM1 enjoys appealing properties such as enhanced in-context learning, and multi-image reasoning, enabling few-shot chain-of-thought prompting.

## 07-015 | What matters when building vision-language models?
- arXiv: 2405.02246  first public: 2024-05-03  latest: 2024-05-03  primary cat: cs.CV
- authors (4): Hugo Laurençon; Léo Tronchon; Matthieu Cord; Victor Sanh
- seed subtopic: 表示融合; type: 原始研究; cross: []
- URLs on first pages of PDF: https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe
- pages: 26

ABSTRACT: The growing interest in vision-language models (VLMs) has been driven by improvements in large language models and vision transformers. Despite the abundance of literature on this subject, we observe that critical decisions regarding the design of VLMs are often not justified. We argue that these unsupported decisions impede progress in the field by making it difficult to identify which choices improve model performance. To address this issue, we conduct extensive experiments around pre-trained models, architecture choice, data, and training methods. Our consolidation of findings includes the development of Idefics2, an efficient foundational VLM of 8 billion parameters. Idefics2 achieves state-of-the-art performance within its size category across various multimodal benchmarks, and is often on par with models four times its size. We release the model (base, instructed, and chat) along with the datasets created for its training.

## 07-017 | Chameleon: Mixed-Modal Early-Fusion Foundation Models
- arXiv: 2405.09818  first public: 2024-05-16  latest: 2025-03-21  primary cat: cs.CL
- authors (1): Chameleon Team
- seed subtopic: 表示融合; type: 原始研究; cross: ['08']
- pages: 27

ABSTRACT: We present Chameleon, a family of early-fusion token-based mixed-modal models capable of understanding and generating images and text in any arbitrary sequence. We outline a stable training approach from inception, an alignment recipe, and an architectural parameterization tailored for the early-fusion, token-based, mixed-modal setting. The models are evaluated on a comprehensive range of tasks, including visual question answering, image captioning, text generation, image generation, and long-form mixed modal generation. Chameleon demonstrates broad and general capabilities, including state-of-the-art performance in image captioning tasks, outperforms Llama-2 in text-only tasks while being competitive with models such as Mixtral 8x7B and Gemini-Pro, and performs non-trivial image generation, all in a single model. It also matches or exceeds the performance of much larger models, including Gemini Pro and GPT-4V, according to human judgments on a new long-form mixed-modal generation evaluation, where either the prompt or outputs contain mixed sequences of both images and text. Chameleon marks a significant step forward in a unified modeling of full multimodal documents.

## 07-018 | Scaling Laws for Native Multimodal Models
- arXiv: 2504.07951  first public: 2025-04-10  latest: 2025-08-09  primary cat: cs.CV
- authors (6): Mustafa Shukor; Enrico Fini; Victor Guilherme Turrisi da Costa; Matthieu Cord; Joshua Susskind; Alaaeldin El-Nouby
- seed subtopic: 表示融合; type: 原始研究; cross: ['01']
- arXiv comment: ICCV 2025 (Oral). 28 figures, 13 tables
- pages: 22

ABSTRACT: Building general-purpose models that can effectively perceive the world through multimodal signals has been a long-standing goal. Current approaches involve integrating separately pre-trained components, such as connecting vision encoders to LLMs and continuing multimodal training. While such approaches exhibit remarkable sample efficiency, it remains an open question whether such late-fusion architectures are inherently superior. In this work, we revisit the architectural design of native multimodal models (NMMs)-those trained from the ground up on all modalities-and conduct an extensive scaling laws study, spanning 457 trained models with different architectures and training mixtures. Our investigation reveals no inherent advantage to late-fusion architectures over early-fusion ones, which do not rely on image encoders or tokenizers. On the contrary, early-fusion exhibits stronger performance at lower parameter counts, is more efficient to train, and is easier to deploy. Motivated by the strong performance of the early-fusion architectures, we show that incorporating Mixture of Experts (MoEs) allows models to learn modality-specific weights, significantly benefiting performance.

## 07-022 | Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution
- arXiv: 2409.12191  first public: 2024-09-18  latest: 2024-10-03  primary cat: cs.CV
- authors (19): Peng Wang; Shuai Bai; Sinan Tan; Shijie Wang; Zhihao Fan; Jinze Bai ...
- seed subtopic: 表示融合; type: 技术报告; cross: []
- arXiv comment: Code is available at https://github.com/QwenLM/Qwen2-VL. arXiv admin note: text overlap with arXiv:2408.15262 by other authors
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen2-VL
- pages: 52

ABSTRACT: We present the Qwen2-VL Series, an advanced upgrade of the previous Qwen-VL models that redefines the conventional predetermined-resolution approach in visual processing. Qwen2-VL introduces the Naive Dynamic Resolution mechanism, which enables the model to dynamically process images of varying resolutions into different numbers of visual tokens. This approach allows the model to generate more efficient and accurate visual representations, closely aligning with human perceptual processes. The model also integrates Multimodal Rotary Position Embedding (M-RoPE), facilitating the effective fusion of positional information across text, images, and videos. We employ a unified paradigm for processing both images and videos, enhancing the model's visual perception capabilities. To explore the potential of large multimodal models, Qwen2-VL investigates the scaling laws for large vision-language models (LVLMs). By scaling both the model size-with versions at 2B, 8B, and 72B parameters-and the amount of training data, the Qwen2-VL Series achieves highly competitive performance. Notably, the Qwen2-VL-72B model achieves results comparable to leading models such as GPT-4o and Claude3.5-Sonnet across various multimodal benchmarks, outperforming other generalist models. Code is available at https://github.com/QwenLM/Qwen2-VL .

## 07-023 | Qwen3-VL Technical Report
- arXiv: 2511.21631  first public: 2025-11-26  latest: 2025-11-27  primary cat: cs.CV
- authors (64): Shuai Bai; Yuxuan Cai; Ruizhe Chen; Keqin Chen; Xionghui Chen; Zesen Cheng ...
- seed subtopic: 表示融合; type: 技术报告; cross: []
- arXiv comment: 42 pages
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen3-VL https://huggingface.co/Qwen
- pages: 42

ABSTRACT: We introduce Qwen3-VL, the most capable vision-language model in the Qwen series to date, achieving superior performance across a broad range of multimodal benchmarks. It natively supports interleaved contexts of up to 256K tokens, seamlessly integrating text, images, and video. The model family includes both dense (2B/4B/8B/32B) and mixture-of-experts (30B-A3B/235B-A22B) variants to accommodate diverse latency-quality trade-offs. Qwen3-VL delivers three core pillars: (i) markedly stronger pure-text understanding, surpassing comparable text-only backbones in several cases; (ii) robust long-context comprehension with a native 256K-token window for both text and interleaved multimodal inputs, enabling faithful retention, retrieval, and cross-referencing across long documents and videos; and (iii) advanced multimodal reasoning across single-image, multi-image, and video tasks, demonstrating leading performance on comprehensive evaluations such as MMMU and visual-math benchmarks (e.g., MathVista and MathVision). Architecturally, we introduce three key upgrades: (i) an enhanced interleaved-MRoPE for stronger spatial-temporal modeling across images and video; (ii) DeepStack integration, which effectively leverages multi-level ViT features to tighten vision-language alignment; and (iii) text-based time alignment for video, evolving from T-RoPE to explicit textual timestamp alignment for more precise temporal grounding. Under comparable token budgets and latency constraints, Qwen3-VL achieves superior performance in both dense and Mixture-of-Experts (MoE) architectures. We envision Qwen3-VL serving as a foundational engine for image-grounded reasoning, agentic decision-making, and multimodal code intelligence in real-world workflows.

## 07-025 | Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models
- arXiv: 2409.17146  first public: 2024-09-25  latest: 2024-12-05  primary cat: cs.CV
- authors (50): Matt Deitke; Christopher Clark; Sangho Lee; Rohun Tripathi; Yue Yang; Jae Sung Park ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: Updated with ablations and more technical details
- pages: 30

ABSTRACT: Today's most advanced vision-language models (VLMs) remain proprietary. The strongest open-weight models rely heavily on synthetic data from proprietary VLMs to achieve good performance, effectively distilling these closed VLMs into open ones. As a result, the community has been missing foundational knowledge about how to build performant VLMs from scratch. We present Molmo, a new family of VLMs that are state-of-the-art in their class of openness. Our key contribution is a collection of new datasets called PixMo, including a dataset of highly detailed image captions for pre-training, a free-form image Q&A dataset for fine-tuning, and an innovative 2D pointing dataset, all collected without the use of external VLMs. The success of our approach relies on careful modeling choices, a well-tuned training pipeline, and, most critically, the quality of our newly collected datasets. Our best-in-class 72B model not only outperforms others in the class of open weight and data models, but also outperforms larger proprietary models including Claude 3.5 Sonnet, and Gemini 1.5 Pro and Flash, second only to GPT-4o based on both academic benchmarks and on a large human evaluation. Our model weights, new datasets, and source code are available at https://molmo.allenai.org/blog.

## 07-038 | DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning
- arXiv: 2505.14362  first public: 2025-05-20  latest: 2026-03-01  primary cat: cs.CV
- authors (8): Ziwei Zheng; Michael Yang; Jack Hong; Chenxiao Zhao; Guohai Xu; Le Yang ...
- seed subtopic: 视觉问答; type: 原始研究; cross: ['04']
- arXiv comment: Accepted by ICLR2026. Ziwei, Michael, Jack, and Chenxiao are equal-contribution. The list order is random
- URLs on first pages of PDF: https://github.com/Visual-Agent/DeepEyes
- pages: 25

ABSTRACT: Large Vision-Language Models excel at multimodal understanding but struggle to deeply integrate visual information into their predominantly text-based reasoning processes, a key challenge in mirroring human cognition. To address this, we introduce DeepEyes, a model that learns to "think with images", trained end-to-end with reinforcement learning without requiring pre-collected reasoning data for cold-start supervised fine-tuning (SFT). Notably, this ability emerges natively, leveraging the model's own grounding capability as an intrinsic function rather than relying on external specialized models or APIs. We enable this capability through active perception, where the model learns to strategically ground its reasoning in visual information, guided by a tailored data selection and reward strategy. DeepEyes achieves significant performance gains on general perception and reasoning benchmarks and also demonstrates improvement in grounding, hallucination, and mathematical reasoning tasks. Interestingly, we observe the distinct evolution of active perception from initial exploration to efficient and accurate exploitation, and diverse thinking patterns that closely mirror human visual reasoning processes. Code is available at https://github.com/Visual-Agent/DeepEyes.

## 07-040 | General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model
- arXiv: 2409.01704  first public: 2024-09-03  latest: 2024-09-03  primary cat: cs.CV
- authors (12): Haoran Wei; Chenglong Liu; Jinyue Chen; Jia Wang; Lingyu Kong; Yanming Xu ...
- seed subtopic: OCR; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/Ucas-HaoranWei/GOT-OCR2.0
- pages: 19

ABSTRACT: Traditional OCR systems (OCR-1.0) are increasingly unable to meet people's usage due to the growing demand for intelligent processing of man-made optical characters. In this paper, we collectively refer to all artificial optical signals (e.g., plain texts, math/molecular formulas, tables, charts, sheet music, and even geometric shapes) as "characters" and propose the General OCR Theory along with an excellent model, namely GOT, to promote the arrival of OCR-2.0. The GOT, with 580M parameters, is a unified, elegant, and end-to-end model, consisting of a high-compression encoder and a long-contexts decoder. As an OCR-2.0 model, GOT can handle all the above "characters" under various OCR tasks. On the input side, the model supports commonly used scene- and document-style images in slice and whole-page styles. On the output side, GOT can generate plain or formatted results (markdown/tikz/smiles/kern) via an easy prompt. Besides, the model enjoys interactive OCR features, i.e., region-level recognition guided by coordinates or colors. Furthermore, we also adapt dynamic resolution and multi-page OCR technologies to GOT for better practicality. In experiments, we provide sufficient results to prove the superiority of our model.

## 07-041 | DeepSeek-OCR: Contexts Optical Compression
- arXiv: 2510.18234  first public: 2025-10-21  latest: 2025-10-21  primary cat: cs.CV
- authors (3): Haoran Wei; Yaofeng Sun; Yukun Li
- seed subtopic: OCR; type: 原始研究; cross: []
- URLs on first pages of PDF: http://github.com/deepseek-ai/DeepSeek-OCR
- pages: 22

ABSTRACT: We present DeepSeek-OCR as an initial investigation into the feasibility of compressing long contexts via optical 2D mapping. DeepSeek-OCR consists of two components: DeepEncoder and DeepSeek3B-MoE-A570M as the decoder. Specifically, DeepEncoder serves as the core engine, designed to maintain low activations under high-resolution input while achieving high compression ratios to ensure an optimal and manageable number of vision tokens. Experiments show that when the number of text tokens is within 10 times that of vision tokens (i.e., a compression ratio < 10x), the model can achieve decoding (OCR) precision of 97%. Even at a compression ratio of 20x, the OCR accuracy still remains at about 60%. This shows considerable promise for research areas such as historical long-context compression and memory forgetting mechanisms in LLMs. Beyond this, DeepSeek-OCR also demonstrates high practical value. On OmniDocBench, it surpasses GOT-OCR2.0 (256 tokens/page) using only 100 vision tokens, and outperforms MinerU2.0 (6000+ tokens per page on average) while utilizing fewer than 800 vision tokens. In production, DeepSeek-OCR can generate training data for LLMs/VLMs at a scale of 200k+ pages per day (a single A100-40G). Codes and model weights are publicly accessible at http://github.com/deepseek-ai/DeepSeek-OCR.

## 07-047 | OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations
- arXiv: 2412.07626  first public: 2024-12-10  latest: 2025-03-25  primary cat: cs.CV
- authors (20): Linke Ouyang; Yuan Qu; Hongbin Zhou; Jiawei Zhu; Rui Zhang; Qunshu Lin ...
- seed subtopic: 文档理解; type: 原始研究; cross: []
- arXiv comment: Accepted by CVPR2025
- pages: 32

ABSTRACT: Document content extraction is a critical task in computer vision, underpinning the data needs of large language models (LLMs) and retrieval-augmented generation (RAG) systems. Despite recent progress, current document parsing methods have not been fairly and comprehensively evaluated due to the narrow coverage of document types and the simplified, unrealistic evaluation procedures in existing benchmarks. To address these gaps, we introduce OmniDocBench, a novel benchmark featuring high-quality annotations across nine document sources, including academic papers, textbooks, and more challenging cases such as handwritten notes and densely typeset newspapers. OmniDocBench supports flexible, multi-level evaluations--ranging from an end-to-end assessment to the task-specific and attribute--based analysis using 19 layout categories and 15 attribute labels. We conduct a thorough evaluation of both pipeline-based methods and end-to-end vision-language models, revealing their strengths and weaknesses across different document types. OmniDocBench sets a new standard for the fair, diverse, and fine-grained evaluation in document parsing. Dataset and code are available at https://github.com/opendatalab/OmniDocBench.

## 07-049 | MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI
- arXiv: 2311.16502  first public: 2023-11-27  latest: 2024-06-13  primary cat: cs.CL
- authors (22): Xiang Yue; Yuansheng Ni; Kai Zhang; Tianyu Zheng; Ruoqi Liu; Ge Zhang ...
- seed subtopic: 视觉问答; type: 原始研究; cross: []
- arXiv comment: CVPR 2024 Oral
- pages: 119

ABSTRACT: We introduce MMMU: a new benchmark designed to evaluate multimodal models on massive multi-discipline tasks demanding college-level subject knowledge and deliberate reasoning. MMMU includes 11.5K meticulously collected multimodal questions from college exams, quizzes, and textbooks, covering six core disciplines: Art & Design, Business, Science, Health & Medicine, Humanities & Social Science, and Tech & Engineering. These questions span 30 subjects and 183 subfields, comprising 30 highly heterogeneous image types, such as charts, diagrams, maps, tables, music sheets, and chemical structures. Unlike existing benchmarks, MMMU focuses on advanced perception and reasoning with domain-specific knowledge, challenging models to perform tasks akin to those faced by experts. The evaluation of 14 open-source LMMs as well as the proprietary GPT-4V(ision) and Gemini highlights the substantial challenges posed by MMMU. Even the advanced GPT-4V and Gemini Ultra only achieve accuracies of 56% and 59% respectively, indicating significant room for improvement. We believe MMMU will stimulate the community to build next-generation multimodal foundation models towards expert artificial general intelligence.

## 07-050 | Are We on the Right Way for Evaluating Large Vision-Language Models?
- arXiv: 2403.20330  first public: 2024-03-29  latest: 2024-04-09  primary cat: cs.CV
- authors (11): Lin Chen; Jinsong Li; Xiaoyi Dong; Pan Zhang; Yuhang Zang; Zehui Chen ...
- seed subtopic: 视觉问答; type: 原始研究; cross: ['12']
- arXiv comment: Project page: https://mmstar-benchmark.github.io/
- pages: 20

ABSTRACT: Large vision-language models (LVLMs) have recently achieved rapid progress, sparking numerous studies to evaluate their multi-modal capabilities. However, we dig into current evaluation works and identify two primary issues: 1) Visual content is unnecessary for many samples. The answers can be directly inferred from the questions and options, or the world knowledge embedded in LLMs. This phenomenon is prevalent across current benchmarks. For instance, GeminiPro achieves 42.9% on the MMMU benchmark without any visual input, and outperforms the random choice baseline across six benchmarks over 24% on average. 2) Unintentional data leakage exists in LLM and LVLM training. LLM and LVLM could still answer some visual-necessary questions without visual content, indicating the memorizing of these samples within large-scale training data. For example, Sphinx-X-MoE gets 43.6% on MMMU without accessing images, surpassing its LLM backbone with 17.9%. Both problems lead to misjudgments of actual multi-modal gains and potentially misguide the study of LVLM. To this end, we present MMStar, an elite vision-indispensable multi-modal benchmark comprising 1,500 samples meticulously selected by humans. MMStar benchmarks 6 core capabilities and 18 detailed axes, aiming to evaluate LVLMs' multi-modal capacities with carefully balanced and purified samples. These samples are first roughly selected from current benchmarks with an automated pipeline, human review is then involved to ensure each curated sample exhibits visual dependency, minimal data leakage, and requires advanced multi-modal capabilities. Moreover, two metrics are developed to measure data leakage and actual performance gain in multi-modal training. We evaluate 16 leading LVLMs on MMStar to assess their multi-modal capabilities, and on 7 benchmarks with the proposed metrics to investigate their data leakage and actual multi-modal gain.

## 07-055 | An Introduction to Vision-Language Modeling
- arXiv: 2405.17247  first public: 2024-05-27  latest: 2024-05-27  primary cat: cs.LG
- authors (41): Florian Bordes; Richard Yuanzhe Pang; Anurag Ajay; Alexander C. Li; Adrien Bardes; Suzanne Petryk ...
- seed subtopic: 跨模态对齐; type: 学术教程; cross: []
- pages: 76

ABSTRACT: Following the recent popularity of Large Language Models (LLMs), several attempts have been made to extend them to the visual domain. From having a visual assistant that could guide us through unfamiliar environments to generative models that produce images using only a high-level text description, the vision-language model (VLM) applications will significantly impact our relationship with technology. However, there are many challenges that need to be addressed to improve the reliability of those models. While language is discrete, vision evolves in a much higher dimensional space in which concepts cannot always be easily discretized. To better understand the mechanics behind mapping vision to language, we present this introduction to VLMs which we hope will help anyone who would like to enter the field. First, we introduce what VLMs are, how they work, and how to train them. Then, we present and discuss approaches to evaluate VLMs. Although this work primarily focuses on mapping images to language, we also discuss extending VLMs to videos.

## 07-080 | Dolphin-v2: Universal Document Parsing via Scalable Anchor Prompting
- arXiv: 2602.05384  first public: 2026-02-05  latest: 2026-02-05  primary cat: cs.CV
- authors (12): Hao Feng; Wei Shi; Ke Zhang; Xiang Fei; Lei Liao; Dingkang Yang ...
- seed subtopic: 文档理解; type: 原始研究; cross: []
- pages: 14

ABSTRACT: Document parsing has garnered widespread attention as vision-language models (VLMs) advance OCR capabilities. However, the field remains fragmented across dozens of specialized models with varying strengths, forcing users to navigate complex model selection and limiting system scalability. Moreover, existing two-stage approaches depend on axis-aligned bounding boxes for layout detection, failing to handle distorted or photographed documents effectively. To this end, we present Dolphin-v2, a two-stage document image parsing model that substantially improves upon the original Dolphin. In the first stage, Dolphin-v2 jointly performs document type classification (digital-born versus photographed) alongside layout analysis. For digital-born documents, it conducts finer-grained element detection with reading order prediction. In the second stage, we employ a hybrid parsing strategy: photographed documents are parsed holistically as complete pages to handle geometric distortions, while digital-born documents undergo element-wise parallel parsing guided by the detected layout anchors, enabling efficient content extraction. Compared with the original Dolphin, Dolphin-v2 introduces several crucial enhancements: (1) robust parsing of photographed documents via holistic page-level understanding, (2) finer-grained element detection (21 categories) with semantic attribute extraction such as author information and document metadata, and (3) code block recognition with indentation preservation, which existing systems typically lack. Comprehensive evaluations are conducted on DocPTBench, OmniDocBench, and our self-constructed RealDoc-160 benchmark. The results demonstrate substantial improvements: +14.78 points overall on the challenging OmniDocBench and 91% error reduction on photographed documents, while maintaining efficient inference through parallel processing.

## 07-081 | CC-OCR V2: Fine-Grained Attribution of LMM Failures in Real-World Visual Document Understanding
- arXiv: 2605.03903  first public: 2026-05-05  latest: 2026-08-10  primary cat: cs.CL
- authors (15): Chunyi Peng; Zhipeng Xu; Yuqi Xiong; Zulong Chen; Junhao Ji; Qing Liu ...
- seed subtopic: OCR; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/eioss/CC-OCR-V2
- pages: 30

ABSTRACT: Recent Large Multimodal Models (LMMs) have achieved remarkable progress on OCR-centric document understanding and processing tasks. Existing benchmarks primarily evaluate LMMs across diverse tasks to reflect practical document-processing workflows or analyze how document characteristics influence model performance. However, they provide limited insight into the reliability of LMMs under real-world document acquisition conditions, where factors such as lighting, screen displays, imaging quality, and capture methods can substantially affect performance. To bridge this gap, we present CC-OCR v2, a comprehensive benchmark for attributing LMM failures in real-world document processing. CC-OCR v2 provides a unified evaluation framework covering five core document-processing capabilities through 16 subtasks, 74 application scenarios, and 7,093 samples. The benchmark spans five evaluation tracks, ten document categories, and 32 languages in the recognition suite. Beyond task-level evaluation, each sample is annotated with ten fine-grained document factors, enabling systematic attribution of model failures across document types and acquisition conditions. Extensive experiments on 17 representative LMMs reveal substantial performance variation across tasks, document categories, and real-world conditions. Moreover, models with comparable overall accuracy often exhibit fundamentally different failure patterns under specific document factors, highlighting a significant gap between benchmark-level performance and reliable deployment in practical applications. The dataset and evaluation toolkit are publicly available at https://github.com/eioss/CC-OCR-V2.

## 07-082 | How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining
- arXiv: 2609.35457  first public: 2026-09-28  latest: 2026-09-28  primary cat: cs.CV
- authors (9): Lin Chen; Bolin Ni; Qi Yang; Lan Jiang; Kun Ding; Xiaoran Fan ...
- seed subtopic: 表示融合; type: 原始研究; cross: ['01']
- pages: 27

ABSTRACT: Most modern multimodal large language models (MLLMs) build on a pretrained visual encoder that provides a strong visual prior. Encoder-free MLLMs instead learn visual representations directly from raw pixels, offering a simple and unified architecture, but their scaling behavior has not been systematically characterized. To fill this gap, we compare scaling laws for encoder-free and encoder-based MLLMs and report three main findings: (1) Removing the visual encoder shifts the compute-optimal allocation for the multimodal objective toward larger models, while leaving that for text nearly unchanged. (2) The two architectures exhibit nearly overlapping loss--compute frontiers on the text objective, but diverge on the multimodal objective: encoder-free models underperform at small scales yet are predicted to catch up at around $10^{22}$ FLOPs, well within practical pretraining budgets. (3) Without a visual encoder, the language model learns to take over its role via vision-specific adaptation: bidirectional interactions among visual tokens become increasingly beneficial as training compute grows, visual processing shifts toward earlier layers, and expert routing for visual tokens becomes more concentrated. Overall, our results indicate that the advantage of the visual prior provided by a pretrained encoder diminishes with scale, positioning encoder-free architectures as a promising direction for multimodal pretraining.

## 07-083 | Can MLLMs Reason Beyond Language? VisReason: A Comprehensive Benchmark for Vision-Centric Reasoning
- arXiv: 2605.25364  first public: 2026-05-25  latest: 2026-05-25  primary cat: cs.CV
- authors (7): Longteng Guo; Yifan Wang; Pengkang Huo; Tailai Chen; Yuze Wu; Jing Liu ...
- seed subtopic: 视觉问答; type: 原始研究; cross: []
- arXiv comment: Accepted by ACL 2026 Findings, resources released at https://github.com/CASIA-IVA-Lab/VisReason
- pages: 44

ABSTRACT: Recent multimodal large language models (MLLMs) achieve strong performance on visual reasoning benchmarks, yet it remains unclear to what extent such performance reflects reasoning directly grounded in visual evidence. We introduce VisReason, a benchmark for vision-centric reasoning in everyday scenarios where perception and inference are tightly coupled. VisReason contains 1,505 questions across 10 categories spanning perceptual, structural, and conceptual reasoning. Our evaluation shows that VisReason poses a qualitatively different challenge from existing benchmarks, exposing substantial gaps between humans and current MLLMs and revealing limited benefits from test-time reasoning strategies. VisReason offers a focused diagnostic for evaluating vision-centric reasoning beyond language.

## 07-006 | EVA-CLIP-18B: Scaling CLIP to 18 Billion Parameters
- arXiv: 2402.04252  first public: 2024-02-06  latest: 2024-02-06  primary cat: cs.CV
- authors (7): Quan Sun; Jinsheng Wang; Qiying Yu; Yufeng Cui; Fan Zhang; Xiaosong Zhang ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- pages: 10

ABSTRACT: Scaling up contrastive language-image pretraining (CLIP) is critical for empowering both vision and multimodal models. We present EVA-CLIP-18B, the largest and most powerful open-source CLIP model to date, with 18-billion parameters. With only 6-billion training samples seen, EVA-CLIP-18B achieves an exceptional 80.7% zero-shot top-1 accuracy averaged across 27 widely recognized image classification benchmarks, outperforming its forerunner EVA-CLIP (5-billion parameters) and other open-source CLIP models by a large margin. Remarkably, we observe a consistent performance improvement with the model size scaling of EVA-CLIP, despite maintaining a constant training dataset of 2-billion image-text pairs from LAION-2B and COYO-700M. This dataset is openly available and much smaller than the in-house datasets (e.g., DFN-5B, WebLI-10B) employed in other state-of-the-art CLIP models. EVA-CLIP-18B demonstrates the potential of EVA-style weak-to-strong visual model scaling. With our model weights made publicly available, we hope to facilitate future research in vision and multimodal foundation models.

## 07-008 | Multimodal Autoregressive Pre-training of Large Vision Encoders
- arXiv: 2411.14402  first public: 2024-11-21  latest: 2024-11-21  primary cat: cs.CV
- authors (16): Enrico Fini; Mustafa Shukor; Xiujun Li; Philipp Dufter; Michal Klein; David Haldimann ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: https://github.com/apple/ml-aim
- URLs on first pages of PDF: https://github.com/apple/ml-aim
- pages: 18

ABSTRACT: We introduce a novel method for pre-training of large-scale vision encoders. Building on recent advancements in autoregressive pre-training of vision models, we extend this framework to a multimodal setting, i.e., images and text. In this paper, we present AIMV2, a family of generalist vision encoders characterized by a straightforward pre-training process, scalability, and remarkable performance across a range of downstream tasks. This is achieved by pairing the vision encoder with a multimodal decoder that autoregressively generates raw image patches and text tokens. Our encoders excel not only in multimodal evaluations but also in vision benchmarks such as localization, grounding, and classification. Notably, our AIMV2-3B encoder achieves 89.5% accuracy on ImageNet-1k with a frozen trunk. Furthermore, AIMV2 consistently outperforms state-of-the-art contrastive models (e.g., CLIP, SigLIP) in multimodal image understanding across diverse settings.

## 07-009 | Scaling Language-Free Visual Representation Learning
- arXiv: 2504.01017  first public: 2025-04-01  latest: 2025-04-01  primary cat: cs.CV
- authors (11): David Fan; Shengbang Tong; Jiachen Zhu; Koustuv Sinha; Zhuang Liu; Xinlei Chen ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: Project page at https://davidfan.io/webssl/
- pages: 21

ABSTRACT: Visual Self-Supervised Learning (SSL) currently underperforms Contrastive Language-Image Pretraining (CLIP) in multimodal settings such as Visual Question Answering (VQA). This multimodal gap is often attributed to the semantics introduced by language supervision, even though visual SSL and CLIP models are often trained on different data. In this work, we ask the question: "Do visual self-supervised approaches lag behind CLIP due to the lack of language supervision, or differences in the training data?" We study this question by training both visual SSL and CLIP models on the same MetaCLIP data, and leveraging VQA as a diverse testbed for vision encoders. In this controlled setup, visual SSL models scale better than CLIP models in terms of data and model capacity, and visual SSL performance does not saturate even after scaling up to 7B parameters. Consequently, we observe visual SSL methods achieve CLIP-level performance on a wide range of VQA and classic vision benchmarks. These findings demonstrate that pure visual SSL can match language-supervised visual pretraining at scale, opening new opportunities for vision-centric representation learning.

## 07-010 | Meta CLIP 2: A Worldwide Scaling Recipe
- arXiv: 2507.22062  first public: 2025-07-29  latest: 2025-08-01  primary cat: cs.CV
- authors (16): Yung-Sung Chuang; Yang Li; Dong Wang; Ching-Feng Yeh; Kehan Lyu; Ramya Raghavendra ...
- seed subtopic: 跨模态对齐; type: 原始研究; cross: []
- arXiv comment: 10 pages
- URLs on first pages of PDF: https://github.com/facebookresearch/MetaCLIP
- pages: 16

ABSTRACT: Contrastive Language-Image Pretraining (CLIP) is a popular foundation model, supporting from zero-shot classification, retrieval to encoders for multimodal large language models (MLLMs). Although CLIP is successfully trained on billion-scale image-text pairs from the English world, scaling CLIP's training further to learning from the worldwide web data is still challenging: (1) no curation method is available to handle data points from non-English world; (2) the English performance from existing multilingual CLIP is worse than its English-only counterpart, i.e., "curse of multilinguality" that is common in LLMs. Here, we present Meta CLIP 2, the first recipe training CLIP from scratch on worldwide web-scale image-text pairs. To generalize our findings, we conduct rigorous ablations with minimal changes that are necessary to address the above challenges and present a recipe enabling mutual benefits from English and non-English world data. In zero-shot ImageNet classification, Meta CLIP 2 ViT-H/14 surpasses its English-only counterpart by 0.8% and mSigLIP by 0.7%, and surprisingly sets new state-of-the-art without system-level confounding factors (e.g., translation, bespoke architecture changes) on multilingual benchmarks, such as CVQA with 57.4%, Babel-ImageNet with 50.2% and XM3600 with 64.3% on image-to-text retrieval.

## 07-019 | CogVLM: Visual Expert for Pretrained Language Models
- arXiv: 2311.03079  first public: 2023-11-06  latest: 2024-02-04  primary cat: cs.CV
- authors (16): Weihan Wang; Qingsong Lv; Wenmeng Yu; Wenyi Hong; Ji Qi; Yan Wang ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/THUDM/CogVLM
- pages: 17

ABSTRACT: We introduce CogVLM, a powerful open-source visual language foundation model. Different from the popular shallow alignment method which maps image features into the input space of language model, CogVLM bridges the gap between the frozen pretrained language model and image encoder by a trainable visual expert module in the attention and FFN layers. As a result, CogVLM enables deep fusion of vision language features without sacrificing any performance on NLP tasks. CogVLM-17B achieves state-of-the-art performance on 10 classic cross-modal benchmarks, including NoCaps, Flicker30k captioning, RefCOCO, RefCOCO+, RefCOCOg, Visual7W, GQA, ScienceQA, VizWiz VQA and TDIUC, and ranks the 2nd on VQAv2, OKVQA, TextVQA, COCO captioning, etc., surpassing or matching PaLI-X 55B. Codes and checkpoints are available at https://github.com/THUDM/CogVLM.

## 07-020 | InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks
- arXiv: 2312.14238  first public: 2023-12-21  latest: 2024-01-15  primary cat: cs.CV
- authors (15): Zhe Chen; Jiannan Wu; Wenhai Wang; Weijie Su; Guo Chen; Sen Xing ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- arXiv comment: 25 pages, 5 figures, 28 tables
- URLs on first pages of PDF: https://github.com/OpenGVLab/InternVL
- pages: 25

ABSTRACT: The exponential growth of large language models (LLMs) has opened up numerous possibilities for multimodal AGI systems. However, the progress in vision and vision-language foundation models, which are also critical elements of multi-modal AGI, has not kept pace with LLMs. In this work, we design a large-scale vision-language foundation model (InternVL), which scales up the vision foundation model to 6 billion parameters and progressively aligns it with the LLM, using web-scale image-text data from various sources. This model can be broadly applied to and achieve state-of-the-art performance on 32 generic visual-linguistic benchmarks including visual perception tasks such as image-level or pixel-level recognition, vision-language tasks such as zero-shot image/video classification, zero-shot image/video-text retrieval, and link with LLMs to create multi-modal dialogue systems. It has powerful visual capabilities and can be a good alternative to the ViT-22B. We hope that our research could contribute to the development of multi-modal large models. Code and models are available at https://github.com/OpenGVLab/InternVL.

## 07-021 | InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models
- arXiv: 2504.10479  first public: 2025-04-14  latest: 2025-04-19  primary cat: cs.CV
- authors (51): Jinguo Zhu; Weiyun Wang; Zhe Chen; Zhaoyang Liu; Shenglong Ye; Lixin Gu ...
- seed subtopic: 表示融合; type: 技术报告; cross: []
- arXiv comment: Technical Report
- URLs on first pages of PDF: https://github.com/OpenGVLab/InternVL https://huggingface.co/OpenGVLab/InternVL3-78B https://huggingface.co/datasets/OpenGVLab/InternVL-Data
- pages: 27

ABSTRACT: We introduce InternVL3, a significant advancement in the InternVL series featuring a native multimodal pre-training paradigm. Rather than adapting a text-only large language model (LLM) into a multimodal large language model (MLLM) that supports visual inputs, InternVL3 jointly acquires multimodal and linguistic capabilities from both diverse multimodal data and pure-text corpora during a single pre-training stage. This unified training paradigm effectively addresses the complexities and alignment challenges commonly encountered in conventional post-hoc training pipelines for MLLMs. To further improve performance and scalability, InternVL3 incorporates variable visual position encoding (V2PE) to support extended multimodal contexts, employs advanced post-training techniques such as supervised fine-tuning (SFT) and mixed preference optimization (MPO), and adopts test-time scaling strategies alongside an optimized training infrastructure. Extensive empirical evaluations demonstrate that InternVL3 delivers superior performance across a wide range of multi-modal tasks. In particular, InternVL3-78B achieves a score of 72.2 on the MMMU benchmark, setting a new state-of-the-art among open-source MLLMs. Its capabilities remain highly competitive with leading proprietary models, including ChatGPT-4o, Claude 3.5 Sonnet, and Gemini 2.5 Pro, while also maintaining strong pure-language proficiency. In pursuit of open-science principles, we will publicly release both the training data and model weights to foster further research and development in next-generation MLLMs.

## 07-024 | LLaVA-OneVision: Easy Visual Task Transfer
- arXiv: 2408.03326  first public: 2024-08-06  latest: 2024-10-26  primary cat: cs.CV
- authors (11): Bo Li; Yuanhan Zhang; Dong Guo; Renrui Zhang; Feng Li; Hao Zhang ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: Project Homepage: https://llava-vl.github.io/blog/2024-08-05-llava-onevision/
- URLs on first pages of PDF: https://llava-vl.github.io/blog/ https://llava-vl.github.io/blog/llava-onevision
- pages: 43

ABSTRACT: We present LLaVA-OneVision, a family of open large multimodal models (LMMs) developed by consolidating our insights into data, models, and visual representations in the LLaVA-NeXT blog series. Our experimental results demonstrate that LLaVA-OneVision is the first single model that can simultaneously push the performance boundaries of open LMMs in three important computer vision scenarios: single-image, multi-image, and video scenarios. Importantly, the design of LLaVA-OneVision allows strong transfer learning across different modalities/scenarios, yielding new emerging capabilities. In particular, strong video understanding and cross-scenario capabilities are demonstrated through task transfer from images to videos.

## 07-026 | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding
- arXiv: 2412.10302  first public: 2024-12-13  latest: 2024-12-13  primary cat: cs.CV
- authors (27): Zhiyu Wu; Xiaokang Chen; Zizheng Pan; Xingchao Liu; Wen Liu; Damai Dai ...
- seed subtopic: 表示融合; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/deepseek-ai/DeepSeek-VL2
- pages: 28

ABSTRACT: We present DeepSeek-VL2, an advanced series of large Mixture-of-Experts (MoE) Vision-Language Models that significantly improves upon its predecessor, DeepSeek-VL, through two key major upgrades. For the vision component, we incorporate a dynamic tiling vision encoding strategy designed for processing high-resolution images with different aspect ratios. For the language component, we leverage DeepSeekMoE models with the Multi-head Latent Attention mechanism, which compresses Key-Value cache into latent vectors, to enable efficient inference and high throughput. Trained on an improved vision-language dataset, DeepSeek-VL2 demonstrates superior capabilities across various tasks, including but not limited to visual question answering, optical character recognition, document/table/chart understanding, and visual grounding. Our model series is composed of three variants: DeepSeek-VL2-Tiny, DeepSeek-VL2-Small and DeepSeek-VL2, with 1.0B, 2.8B and 4.5B activated parameters respectively. DeepSeek-VL2 achieves competitive or state-of-the-art performance with similar or fewer activated parameters compared to existing open-source dense and MoE-based models. Codes and pre-trained models are publicly accessible at https://github.com/deepseek-ai/DeepSeek-VL2.

## 07-027 | NVLM: Open Frontier-Class Multimodal LLMs
- arXiv: 2409.11402  first public: 2024-09-17  latest: 2024-10-22  primary cat: cs.CL
- authors (10): Wenliang Dai; Nayeon Lee; Boxin Wang; Zhuolin Yang; Zihan Liu; Jon Barker ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- arXiv comment: Fixed the typos. For more information, please visit our project page at: https://research.nvidia.com/labs/adlr/NVLM-1
- pages: 33

ABSTRACT: We introduce NVLM 1.0, a family of frontier-class multimodal large language models (LLMs) that achieve state-of-the-art results on vision-language tasks, rivaling the leading proprietary models (e.g., GPT-4o) and open-access models (e.g., Llama 3-V 405B and InternVL 2). Remarkably, NVLM 1.0 shows improved text-only performance over its LLM backbone after multimodal training. In terms of model design, we perform a comprehensive comparison between decoder-only multimodal LLMs (e.g., LLaVA) and cross-attention-based models (e.g., Flamingo). Based on the strengths and weaknesses of both approaches, we propose a novel architecture that enhances both training efficiency and multimodal reasoning capabilities. Furthermore, we introduce a 1-D tile-tagging design for tile-based dynamic high-resolution images, which significantly boosts performance on multimodal reasoning and OCR-related tasks. Regarding training data, we meticulously curate and provide detailed information on our multimodal pretraining and supervised fine-tuning datasets. Our findings indicate that dataset quality and task diversity are more important than scale, even during the pretraining phase, across all architectures. Notably, we develop production-grade multimodality for the NVLM-1.0 models, enabling them to excel in vision-language tasks while maintaining and even improving text-only performance compared to their LLM backbones. To achieve this, we craft and integrate a high-quality text-only dataset into multimodal training, alongside a substantial amount of multimodal math and reasoning data, leading to enhanced math and coding capabilities across modalities. To advance research in the field, we release the model weights at https://huggingface.co/nvidia/NVLM-D-72B and will open-source the training code for the community soon.

## 07-028 | PaliGemma: A versatile 3B VLM for transfer
- arXiv: 2407.07726  first public: 2024-07-10  latest: 2024-10-10  primary cat: cs.CV
- authors (35): Lucas Beyer; Andreas Steiner; André Susano Pinto; Alexander Kolesnikov; Xiao Wang; Daniel Salz ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: v2 adds Appendix H and I and a few citations
- pages: 59

ABSTRACT: PaliGemma is an open Vision-Language Model (VLM) that is based on the SigLIP-So400m vision encoder and the Gemma-2B language model. It is trained to be a versatile and broadly knowledgeable base model that is effective to transfer. It achieves strong performance on a wide variety of open-world tasks. We evaluate PaliGemma on almost 40 diverse tasks including standard VLM benchmarks, but also more specialized tasks such as remote-sensing and segmentation.

## 07-029 | MiniCPM-V: A GPT-4V Level MLLM on Your Phone
- arXiv: 2408.01800  first public: 2024-08-03  latest: 2024-08-03  primary cat: cs.CV
- authors (23): Yuan Yao; Tianyu Yu; Ao Zhang; Chongyi Wang; Junbo Cui; Hongji Zhu ...
- seed subtopic: 图文理解; type: 原始研究; cross: ['11']
- arXiv comment: preprint
- URLs on first pages of PDF: https://github.com/OpenBMB/MiniCPM-V
- pages: 26

ABSTRACT: The recent surge of Multimodal Large Language Models (MLLMs) has fundamentally reshaped the landscape of AI research and industry, shedding light on a promising path toward the next AI milestone. However, significant challenges remain preventing MLLMs from being practical in real-world applications. The most notable challenge comes from the huge cost of running an MLLM with a massive number of parameters and extensive computation. As a result, most MLLMs need to be deployed on high-performing cloud servers, which greatly limits their application scopes such as mobile, offline, energy-sensitive, and privacy-protective scenarios. In this work, we present MiniCPM-V, a series of efficient MLLMs deployable on end-side devices. By integrating the latest MLLM techniques in architecture, pretraining and alignment, the latest MiniCPM-Llama3-V 2.5 has several notable features: (1) Strong performance, outperforming GPT-4V-1106, Gemini Pro and Claude 3 on OpenCompass, a comprehensive evaluation over 11 popular benchmarks, (2) strong OCR capability and 1.8M pixel high-resolution image perception at any aspect ratio, (3) trustworthy behavior with low hallucination rates, (4) multilingual support for 30+ languages, and (5) efficient deployment on mobile phones. More importantly, MiniCPM-V can be viewed as a representative example of a promising trend: The model sizes for achieving usable (e.g., GPT-4V) level performance are rapidly decreasing, along with the fast growth of end-side computation capacity. This jointly shows that GPT-4V level MLLMs deployed on end devices are becoming increasingly possible, unlocking a wider spectrum of real-world AI applications in the near future.

## 07-031 | Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders
- arXiv: 2408.15998  first public: 2024-08-28  latest: 2025-03-02  primary cat: cs.CV
- authors (16): Min Shi; Fuxiao Liu; Shihao Wang; Shijia Liao; Subhashree Radhakrishnan; Yilin Zhao ...
- seed subtopic: 表示融合; type: 原始研究; cross: []
- arXiv comment: Github: https://github.com/NVlabs/Eagle, HuggingFace: https://huggingface.co/NVEagle
- URLs on first pages of PDF: https://github.com/NVlabs/Eagle
- pages: 19

ABSTRACT: The ability to accurately interpret complex visual information is a crucial topic of multimodal large language models (MLLMs). Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. A number of recent MLLMs achieve this goal using a mixture of vision encoders. Despite their success, there is a lack of systematic comparisons and detailed ablation studies addressing critical aspects, such as expert selection and the integration of multiple vision experts. This study provides an extensive exploration of the design space for MLLMs using a mixture of vision encoders and resolutions. Our findings reveal several underlying principles common to various existing strategies, leading to a streamlined yet effective design approach. We discover that simply concatenating visual tokens from a set of complementary vision encoders is as effective as more complex mixing architectures or strategies. We additionally introduce Pre-Alignment to bridge the gap between vision-focused encoders and language tokens, enhancing model coherence. The resulting family of MLLMs, Eagle, surpasses other leading open-source models on major MLLM benchmarks.

## 07-033 | LLaVA-UHD: an LMM Perceiving Any Aspect Ratio and High-Resolution Images
- arXiv: 2403.11703  first public: 2024-03-18  latest: 2024-03-18  primary cat: cs.CV
- authors (10): Ruyi Xu; Yuan Yao; Zonghao Guo; Junbo Cui; Zanlin Ni; Chunjiang Ge ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: Preprint
- URLs on first pages of PDF: https://github.com/thunlp/LLaVA-UHD
- pages: 16

ABSTRACT: Visual encoding constitutes the basis of large multimodal models (LMMs) in understanding the visual world. Conventional LMMs process images in fixed sizes and limited resolutions, while recent explorations in this direction are limited in adaptivity, efficiency, and even correctness. In this work, we first take GPT-4V and LLaVA-1.5 as representative examples and expose systematic flaws rooted in their visual encoding strategy. To address the challenges, we present LLaVA-UHD, a large multimodal model that can efficiently perceive images in any aspect ratio and high resolution. LLaVA-UHD includes three key components: (1) An image modularization strategy that divides native-resolution images into smaller variable-sized slices for efficient and extensible encoding, (2) a compression module that further condenses image tokens from visual encoders, and (3) a spatial schema to organize slice tokens for LLMs. Comprehensive experiments show that LLaVA-UHD outperforms established LMMs trained with 2-3 orders of magnitude more data on 9 benchmarks. Notably, our model built on LLaVA-1.5 336x336 supports 6 times larger (i.e., 672x1088) resolution images using only 94% inference computation, and achieves 6.4 accuracy improvement on TextVQA. Moreover, the model can be efficiently trained in academic settings, within 23 hours on 8 A100 GPUs (vs. 26 hours of LLaVA-1.5). We make the data and code publicly available at https://github.com/thunlp/LLaVA-UHD.

## 07-036 | GLaMM: Pixel Grounding Large Multimodal Model
- arXiv: 2311.03356  first public: 2023-11-06  latest: 2024-06-02  primary cat: cs.CV
- authors (10): Hanoona Rasheed; Muhammad Maaz; Sahal Shaji Mullappilly; Abdelrahman Shaker; Salman Khan; Hisham Cholakkal ...
- seed subtopic: 图文理解; type: 原始研究; cross: []
- arXiv comment: CVPR 2024
- URLs on first pages of PDF: https://github.com/mbzuai-oryx/groundingLMM
- pages: 20

ABSTRACT: Large Multimodal Models (LMMs) extend Large Language Models to the vision domain. Initial LMMs used holistic images and text prompts to generate ungrounded textual responses. Recently, region-level LMMs have been used to generate visually grounded responses. However, they are limited to only referring to a single object category at a time, require users to specify the regions, or cannot offer dense pixel-wise object grounding. In this work, we present Grounding LMM (GLaMM), the first model that can generate natural language responses seamlessly intertwined with corresponding object segmentation masks. GLaMM not only grounds objects appearing in the conversations but is flexible enough to accept both textual and optional visual prompts (region of interest) as input. This empowers users to interact with the model at various levels of granularity, both in textual and visual domains. Due to the lack of standard benchmarks for the novel setting of visually Grounded Conversation Generation (GCG), we introduce a comprehensive evaluation protocol with our curated grounded conversations. Our proposed GCG task requires densely grounded concepts in natural scenes at a large-scale. To this end, we propose a densely annotated Grounding-anything Dataset (GranD) using our proposed automated annotation pipeline that encompasses 7.5M unique concepts grounded in a total of 810M regions available with segmentation masks. Besides GCG, GLaMM also performs effectively on several downstream tasks, e.g., referring expression segmentation, image and region-level captioning and vision-language conversations.

## 07-039 | V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs
- arXiv: 2312.14135  first public: 2023-12-21  latest: 2023-12-26  primary cat: cs.CV
- authors (2): Penghao Wu; Saining Xie
- seed subtopic: 视觉问答; type: 原始研究; cross: []
- arXiv comment: Project page with code: https://vstar-seal.github.io/
- pages: 18

ABSTRACT: When we look around and perform complex tasks, how we see and selectively process what we see is crucial. However, the lack of this visual search mechanism in current multimodal LLMs (MLLMs) hinders their ability to focus on important visual details, especially when handling high-resolution and visually crowded images. To address this, we introduce V*, an LLM-guided visual search mechanism that employs the world knowledge in LLMs for efficient visual querying. When combined with an MLLM, this mechanism enhances collaborative reasoning, contextual understanding, and precise targeting of specific visual elements. This integration results in a new MLLM meta-architecture, named Show, sEArch, and TelL (SEAL). We further create V*Bench, a benchmark specifically designed to evaluate MLLMs in their ability to process high-resolution images and focus on visual details. Our study highlights the necessity of incorporating visual search capabilities into multimodal systems. The code is available https://github.com/penghao-wu/vstar.

## 07-042 | olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models
- arXiv: 2502.18443  first public: 2025-02-25  latest: 2025-07-02  primary cat: cs.CL
- authors (10): Jake Poznanski; Aman Rangapur; Jon Borchardt; Jason Dunkelberger; Regan Huff; Daniel Lin ...
- seed subtopic: OCR; type: 原始研究; cross: []
- pages: 33

ABSTRACT: PDF documents have the potential to provide trillions of novel, high-quality tokens for training language models. However, these documents come in a diversity of types with differing formats and visual layouts that pose a challenge when attempting to extract and faithfully represent the underlying content for language model use. Traditional open source tools often produce lower quality extractions compared to vision language models (VLMs), but reliance on the best VLMs can be prohibitively costly (e.g., over 6,240 USD per million PDF pages for GPT-4o) or infeasible if the PDFs cannot be sent to proprietary APIs. We present olmOCR, an open-source toolkit for processing PDFs into clean, linearized plain text in natural reading order while preserving structured content like sections, tables, lists, equations, and more. Our toolkit runs a fine-tuned 7B vision language model (VLM) trained on olmOCR-mix-0225, a sample of 260,000 pages from over 100,000 crawled PDFs with diverse properties, including graphics, handwritten text and poor quality scans. olmOCR is optimized for large-scale batch processing, able to scale flexibly to different hardware setups and can convert a million PDF pages for only 176 USD. To aid comparison with existing systems, we also introduce olmOCR-Bench, a curated set of 1,400 PDFs capturing many content types that remain challenging even for the best tools and VLMs, including formulas, tables, tiny fonts, old scans, and more. We find olmOCR outperforms even top VLMs including GPT-4o, Gemini Flash 2 and Qwen-2.5-VL. We openly release all components of olmOCR: our fine-tuned VLM model, training code and data, an efficient inference pipeline that supports vLLM and SGLang backends, and benchmark olmOCR-Bench.

## 07-043 | OCRBench v2: An Improved Benchmark for Evaluating Large Multimodal Models on Visual Text Localization and Reasoning
- arXiv: 2501.00321  first public: 2024-12-31  latest: 2025-06-05  primary cat: cs.CV
- authors (24): Ling Fu; Zhebin Kuang; Jiajun Song; Mingxin Huang; Biao Yang; Yuzhe Li ...
- seed subtopic: OCR; type: 原始研究; cross: []
- URLs on first pages of PDF: https://99franklin.github.io/ocrbench_v2
- pages: 45

ABSTRACT: Scoring the Optical Character Recognition (OCR) capabilities of Large Multimodal Models (LMMs) has witnessed growing interest. Existing benchmarks have highlighted the impressive performance of LMMs in text recognition; however, their abilities in certain challenging tasks, such as text localization, handwritten content extraction, and logical reasoning, remain underexplored. To bridge this gap, we introduce OCRBench v2, a large-scale bilingual text-centric benchmark with currently the most comprehensive set of tasks (4x more tasks than the previous multi-scene benchmark OCRBench), the widest coverage of scenarios (31 diverse scenarios), and thorough evaluation metrics, with 10,000 human-verified question-answering pairs and a high proportion of difficult samples. Moreover, we construct a private test set with 1,500 manually annotated images. The consistent evaluation trends observed across both public and private test sets validate the OCRBench v2's reliability. After carefully benchmarking state-of-the-art LMMs, we find that most LMMs score below 50 (100 in total) and suffer from five-type limitations, including less frequently encountered text recognition, fine-grained perception, layout perception, complex element parsing, and logical reasoning. The project website is at: https://99franklin.github.io/ocrbench_v2/

## 07-044 | mPLUG-DocOwl 1.5: Unified Structure Learning for OCR-free Document Understanding
- arXiv: 2403.12895  first public: 2024-03-19  latest: 2024-03-19  primary cat: cs.CV
- authors (11): Anwen Hu; Haiyang Xu; Jiabo Ye; Ming Yan; Liang Zhang; Bo Zhang ...
- seed subtopic: 文档理解; type: 原始研究; cross: []
- arXiv comment: 21 pages, 15 figures
- URLs on first pages of PDF: https://github.com/X-PLUG/mPLUG-DocOwl/tree/main/DocOwl1.5
- pages: 26

ABSTRACT: Structure information is critical for understanding the semantics of text-rich images, such as documents, tables, and charts. Existing Multimodal Large Language Models (MLLMs) for Visual Document Understanding are equipped with text recognition ability but lack general structure understanding abilities for text-rich document images. In this work, we emphasize the importance of structure information in Visual Document Understanding and propose the Unified Structure Learning to boost the performance of MLLMs. Our Unified Structure Learning comprises structure-aware parsing tasks and multi-grained text localization tasks across 5 domains: document, webpage, table, chart, and natural image. To better encode structure information, we design a simple and effective vision-to-text module H-Reducer, which can not only maintain the layout information but also reduce the length of visual features by merging horizontal adjacent patches through convolution, enabling the LLM to understand high-resolution images more efficiently. Furthermore, by constructing structure-aware text sequences and multi-grained pairs of texts and bounding boxes for publicly available text-rich images, we build a comprehensive training set DocStruct4M to support structure learning. Finally, we construct a small but high-quality reasoning tuning dataset DocReason25K to trigger the detailed explanation ability in the document domain. Our model DocOwl 1.5 achieves state-of-the-art performance on 10 visual document understanding benchmarks, improving the SOTA performance of MLLMs with a 7B LLM by more than 10 points in 5/10 benchmarks. Our codes, models, and datasets are publicly available at https://github.com/X-PLUG/mPLUG-DocOwl/tree/main/DocOwl1.5.

## 07-046 | MinerU: An Open-Source Solution for Precise Document Content Extraction
- arXiv: 2409.18839  first public: 2024-09-27  latest: 2024-09-27  primary cat: cs.CV
- authors (18): Bin Wang; Chao Xu; Xiaomeng Zhao; Linke Ouyang; Fan Wu; Zhiyuan Zhao ...
- seed subtopic: 文档理解; type: 技术报告; cross: []
- arXiv comment: MinerU Technical Report
- URLs on first pages of PDF: https://github.com/opendatalab/MinerU https://github.com/opendatalab/PDF-Extract-Kit https://github.com/pymupdf/PyMuPDF
- pages: 14

ABSTRACT: Document content analysis has been a crucial research area in computer vision. Despite significant advancements in methods such as OCR, layout detection, and formula recognition, existing open-source solutions struggle to consistently deliver high-quality content extraction due to the diversity in document types and content. To address these challenges, we present MinerU, an open-source solution for high-precision document content extraction. MinerU leverages the sophisticated PDF-Extract-Kit models to extract content from diverse documents effectively and employs finely-tuned preprocessing and postprocessing rules to ensure the accuracy of the final results. Experimental results demonstrate that MinerU consistently achieves high performance across various document types, significantly enhancing the quality and consistency of content extraction. The MinerU open-source project is available at https://github.com/opendatalab/MinerU.

## 07-048 | CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs
- arXiv: 2406.18521  first public: 2024-06-26  latest: 2024-06-26  primary cat: cs.CL
- authors (13): Zirui Wang; Mengzhou Xia; Luxi He; Howard Chen; Yitao Liu; Richard Zhu ...
- seed subtopic: 文档理解; type: 原始研究; cross: []
- arXiv comment: 121 pages, 90 figures
- pages: 121

ABSTRACT: Chart understanding plays a pivotal role when applying Multimodal Large Language Models (MLLMs) to real-world tasks such as analyzing scientific papers or financial reports. However, existing datasets often focus on oversimplified and homogeneous charts with template-based questions, leading to an over-optimistic measure of progress. We demonstrate that although open-source models can appear to outperform strong proprietary models on these benchmarks, a simple stress test with slightly different charts or questions can deteriorate performance by up to 34.5%. In this work, we propose CharXiv, a comprehensive evaluation suite involving 2,323 natural, challenging, and diverse charts from arXiv papers. CharXiv includes two types of questions: 1) descriptive questions about examining basic chart elements and 2) reasoning questions that require synthesizing information across complex visual elements in the chart. To ensure quality, all charts and questions are handpicked, curated, and verified by human experts. Our results reveal a substantial, previously underestimated gap between the reasoning skills of the strongest proprietary model (i.e., GPT-4o), which achieves 47.1% accuracy, and the strongest open-source model (i.e., InternVL Chat V1.5), which achieves 29.2%. All models lag far behind human performance of 80.5%, underscoring weaknesses in the chart understanding capabilities of existing MLLMs. We hope CharXiv facilitates future research on MLLM chart understanding by providing a more realistic and faithful measure of progress. Project page and leaderboard: https://charxiv.github.io/

## 07-051 | BLINK: Multimodal Large Language Models Can See but Not Perceive
- arXiv: 2404.12390  first public: 2024-04-18  latest: 2024-07-03  primary cat: cs.CV
- authors (10): Xingyu Fu; Yushi Hu; Bangzheng Li; Yu Feng; Haoyu Wang; Xudong Lin ...
- seed subtopic: 视觉问答; type: 原始研究; cross: []
- arXiv comment: Multimodal Benchmark, Project Url: https://zeyofu.github.io/blink/, ECCV 2024
- URLs on first pages of PDF: https://zeyofu.github.io/blink/
- pages: 37

ABSTRACT: We introduce Blink, a new benchmark for multimodal language models (LLMs) that focuses on core visual perception abilities not found in other evaluations. Most of the Blink tasks can be solved by humans "within a blink" (e.g., relative depth estimation, visual correspondence, forensics detection, and multi-view reasoning). However, we find these perception-demanding tasks cast significant challenges for current multimodal LLMs because they resist mediation through natural language. Blink reformats 14 classic computer vision tasks into 3,807 multiple-choice questions, paired with single or multiple images and visual prompting. While humans get 95.70% accuracy on average, Blink is surprisingly challenging for existing multimodal LLMs: even the best-performing GPT-4V and Gemini achieve accuracies of 51.26% and 45.72%, only 13.17% and 7.63% higher than random guessing, indicating that such perception abilities have not "emerged" yet in recent multimodal LLMs. Our analysis also highlights that specialist CV models could solve these problems much better, suggesting potential pathways for future improvements. We believe Blink will stimulate the community to help multimodal LLMs catch up with human-level visual perception.

## 07-052 | MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?
- arXiv: 2403.14624  first public: 2024-03-21  latest: 2024-08-18  primary cat: cs.CV
- authors (11): Renrui Zhang; Dongzhi Jiang; Yichi Zhang; Haokun Lin; Ziyu Guo; Pengshuo Qiu ...
- seed subtopic: 视觉问答; type: 原始研究; cross: []
- arXiv comment: Accepted by ECCV 2024, 46 Pages, Benchmark Project Page: https://mathverse-cuhk.github.io
- pages: 46

ABSTRACT: The remarkable progress of Multi-modal Large Language Models (MLLMs) has garnered unparalleled attention, due to their superior performance in visual contexts. However, their capabilities in visual math problem-solving remain insufficiently evaluated and understood. We investigate current benchmarks to incorporate excessive visual content within textual questions, which potentially assist MLLMs in deducing answers without truly interpreting the input diagrams. To this end, we introduce MathVerse, an all-around visual math benchmark designed for an equitable and in-depth evaluation of MLLMs. We meticulously collect 2,612 high-quality, multi-subject math problems with diagrams from publicly available sources. Each problem is then transformed by human annotators into six distinct versions, each offering varying degrees of information content in multi-modality, contributing to 15K test samples in total. This approach allows MathVerse to comprehensively assess whether and how much MLLMs can truly understand the visual diagrams for mathematical reasoning. In addition, we propose a Chain-of-Thought (CoT) evaluation strategy for a fine-grained assessment of the output answers. Rather than naively judging True or False, we employ GPT-4(V) to adaptively extract crucial reasoning steps, and then score each step with detailed error analysis, which can reveal the intermediate CoT reasoning quality by MLLMs. We hope the MathVerse benchmark may provide unique insights to guide the future development of MLLMs. Project page: https://mathverse-cuhk.github.io
