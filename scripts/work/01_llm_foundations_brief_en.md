# Brief for annotation: 01 大语言模型基础

## 01-001 | The Llama 3 Herd of Models
- arXiv: 2407.21783  first public: 2024-07-31  latest: 2024-11-23  primary cat: cs.AI
- authors (561): Aaron Grattafiori; Abhimanyu Dubey; Abhinav Jauhri; Abhinav Pandey; Abhishek Kadian; Ahmad Al-Dahle ...
- seed subtopic: 模型设计与技术报告; type: 技术报告; cross: []
- pages: 92

ABSTRACT: Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development.

## 01-002 | RoFormer: Enhanced Transformer with Rotary Position Embedding
- arXiv: 2104.09864  first public: 2021-04-20  latest: 2023-11-08  primary cat: cs.CL
- authors (6): Jianlin Su; Yu Lu; Shengfeng Pan; Ahmed Murtadha; Bo Wen; Yunfeng Liu
- seed subtopic: 位置编码; type: 原始研究; cross: []
- arXiv comment: fixed some typos
- URLs on first pages of PDF: https://github.com/ZhuiyiTechnology/roformer https://huggingface.co/docs/transformers/model_doc/roformer
- pages: 14

ABSTRACT: Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: \url{https://huggingface.co/docs/transformers/model_doc/roformer}.

## 01-003 | Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- arXiv: 2312.00752  first public: 2023-12-01  latest: 2024-05-31  primary cat: cs.LG
- authors (2): Albert Gu; Tri Dao
- seed subtopic: 架构; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/state-spaces/mamba
- pages: 36

ABSTRACT: Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5$\times$ higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

## 01-004 | Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality
- arXiv: 2405.21060  first public: 2024-05-31  latest: 2024-05-31  primary cat: cs.LG
- authors (2): Tri Dao; Albert Gu
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: ICML 2024
- URLs on first pages of PDF: https://github.com/state-spaces/mamba
- pages: 52

ABSTRACT: While Transformers have been the main architecture behind deep learning's success in language modeling, state-space models (SSMs) such as Mamba have recently been shown to match or outperform Transformers at small to medium scale. We show that these families of models are actually quite closely related, and develop a rich framework of theoretical connections between SSMs and variants of attention, connected through various decompositions of a well-studied class of structured semiseparable matrices. Our state space duality (SSD) framework allows us to design a new architecture (Mamba-2) whose core layer is an a refinement of Mamba's selective SSM that is 2-8X faster, while continuing to be competitive with Transformers on language modeling.

## 01-005 | Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models
- arXiv: 2402.19427  first public: 2024-02-29  latest: 2024-02-29  primary cat: cs.LG
- authors (17): Soham De; Samuel L. Smith; Anushan Fernando; Aleksandar Botev; George Cristian-Muraru; Albert Gu ...
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: 25 pages, 11 figures
- pages: 25

ABSTRACT: Recurrent neural networks (RNNs) have fast inference and scale efficiently on long sequences, but they are difficult to train and hard to scale. We propose Hawk, an RNN with gated linear recurrences, and Griffin, a hybrid model that mixes gated linear recurrences with local attention. Hawk exceeds the reported performance of Mamba on downstream tasks, while Griffin matches the performance of Llama-2 despite being trained on over 6 times fewer tokens. We also show that Griffin can extrapolate on sequences significantly longer than those seen during training. Our models match the hardware efficiency of Transformers during training, and during inference they have lower latency and significantly higher throughput. We scale Griffin up to 14B parameters, and explain how to shard our models for efficient distributed training.

## 01-007 | Gated Delta Networks: Improving Mamba2 with Delta Rule
- arXiv: 2412.06464  first public: 2024-12-09  latest: 2025-03-06  primary cat: cs.CL
- authors (3): Songlin Yang; Jan Kautz; Ali Hatamizadeh
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: ICLR 2025 camera ready
- URLs on first pages of PDF: https://github.com/NVlabs/GatedDeltaNet
- pages: 22

ABSTRACT: Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited. To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta update rule for precise memory modifications. We observe that these mechanisms are complementary: gating enables rapid memory erasure while the delta rule facilitates targeted updates. Building on this insight, we introduce the gated delta rule and develop a parallel training algorithm optimized for modern hardware. Our proposed architecture, Gated DeltaNet, consistently surpasses existing models like Mamba2 and DeltaNet across multiple benchmarks, including language modeling, common-sense reasoning, in-context retrieval, length extrapolation, and long-context understanding. We further enhance performance by developing hybrid architectures that combine Gated DeltaNet layers with sliding window attention or Mamba2 layers, achieving both improved training efficiency and superior task performance.

## 01-008 | Titans: Learning to Memorize at Test Time
- arXiv: 2501.00663  first public: 2024-12-31  latest: 2024-12-31  primary cat: cs.LG
- authors (3): Ali Behrouz; Peilin Zhong; Vahab Mirrokni
- seed subtopic: 架构; type: 原始研究; cross: []
- pages: 27

ABSTRACT: Over more than a decade there has been an extensive research effort on how to effectively utilize recurrent models and attention. While recurrent models aim to compress the data into a fixed-size memory (called hidden state), attention allows attending to the entire context window, capturing the direct dependencies of all tokens. This more accurate modeling of dependencies, however, comes with a quadratic cost, limiting the model to a fixed-length context. We present a new neural long-term memory module that learns to memorize historical context and helps attention to attend to the current context while utilizing long past information. We show that this neural memory has the advantage of fast parallelizable training while maintaining a fast inference. From a memory perspective, we argue that attention due to its limited context but accurate dependency modeling performs as a short-term memory, while neural memory due to its ability to memorize the data, acts as a long-term, more persistent, memory. Based on these two modules, we introduce a new family of architectures, called Titans, and present three variants to address how one can effectively incorporate memory into this architecture. Our experimental results on language modeling, common-sense reasoning, genomics, and time series tasks show that Titans are more effective than Transformers and recent modern linear recurrent models. They further can effectively scale to larger than 2M context window size with higher accuracy in needle-in-haystack tasks compared to baselines.

## 01-009 | Transformers without Normalization
- arXiv: 2503.10622  first public: 2025-03-13  latest: 2025-06-14  primary cat: cs.LG
- authors (5): Jiachen Zhu; Xinlei Chen; Kaiming He; Yann LeCun; Zhuang Liu
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: CVPR 2025; Project page: https://jiachenzhu.github.io/DyT/
- pages: 19

ABSTRACT: Normalization layers are ubiquitous in modern neural networks and have long been considered essential. This work demonstrates that Transformers without normalization can achieve the same or better performance using a remarkably simple technique. We introduce Dynamic Tanh (DyT), an element-wise operation $DyT($x$) = \tanh(α$x$)$, as a drop-in replacement for normalization layers in Transformers. DyT is inspired by the observation that layer normalization in Transformers often produces tanh-like, $S$-shaped input-output mappings. By incorporating DyT, Transformers without normalization can match or exceed the performance of their normalized counterparts, mostly without hyperparameter tuning. We validate the effectiveness of Transformers with DyT across diverse settings, ranging from recognition to generation, supervised to self-supervised learning, and computer vision to language models. These findings challenge the conventional understanding that normalization layers are indispensable in modern neural networks, and offer new insights into their role in deep networks.

## 01-010 | Gated Linear Attention Transformers with Hardware-Efficient Training
- arXiv: 2312.06635  first public: 2023-12-11  latest: 2024-08-27  primary cat: cs.LG
- authors (5): Songlin Yang; Bailin Wang; Yikang Shen; Rameswar Panda; Yoon Kim
- seed subtopic: 注意力; type: 原始研究; cross: []
- arXiv comment: minor update
- URLs on first pages of PDF: https://github.com/sustcsonglin/fl
- pages: 23

ABSTRACT: Transformers with linear attention allow for efficient parallel training but can simultaneously be formulated as an RNN with 2D (matrix-valued) hidden states, thus enjoying linear-time inference complexity. However, linear attention generally underperforms ordinary softmax attention. Moreover, current implementations of linear attention lack I/O-awareness and are thus slower than highly optimized implementations of softmax attention. This work describes a hardware-efficient algorithm for linear attention that trades off memory movement against parallelizability. The resulting implementation, dubbed FLASHLINEARATTENTION, is faster than FLASHATTENTION-2 (Dao, 2023) as a standalone layer even on short sequence lengths (e.g., 1K). We then generalize this algorithm to a more expressive variant of linear attention with data-dependent gates. When used as a replacement for the standard attention layer in Transformers, the resulting gated linear attention (GLA) Transformer is found to perform competitively against the LLaMA-architecture Transformer (Touvron et al., 2023) as well recent linear-time-inference baselines such as RetNet (Sun et al., 2023a) and Mamba (Gu & Dao, 2023) on moderate-scale language modeling experiments. GLA Transformer is especially effective at length generalization, enabling a model trained on 2K to generalize to sequences longer than 20K without significant perplexity degradations. For training speed, the GLA Transformer has higher throughput than a similarly-sized Mamba model.

## 01-011 | Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention
- arXiv: 2502.11089  first public: 2025-02-16  latest: 2025-02-27  primary cat: cs.CL
- authors (15): Jingyang Yuan; Huazuo Gao; Damai Dai; Junyu Luo; Liang Zhao; Zhengyan Zhang ...
- seed subtopic: 注意力; type: 原始研究; cross: ['11']
- pages: 25

ABSTRACT: Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges. Sparse attention offers a promising direction for improving efficiency while maintaining model capabilities. We present NSA, a Natively trainable Sparse Attention mechanism that integrates algorithmic innovations with hardware-aligned optimizations to achieve efficient long-context modeling. NSA employs a dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection to preserve both global context awareness and local precision. Our approach advances sparse attention design with two key innovations: (1) We achieve substantial speedups through arithmetic intensity-balanced algorithm design, with implementation optimizations for modern hardware. (2) We enable end-to-end training, reducing pretraining computation without sacrificing model performance. As shown in Figure 1, experiments show the model pretrained with NSA maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning. Meanwhile, NSA achieves substantial speedups over Full Attention on 64k-length sequences across decoding, forward propagation, and backward propagation, validating its efficiency throughout the model lifecycle.

## 01-012 | Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- arXiv: 2505.06708  first public: 2025-05-10  latest: 2025-05-10  primary cat: cs.CL
- authors (13): Zihan Qiu; Zekun Wang; Bo Zheng; Zeyu Huang; Kaiyue Wen; Songlin Yang ...
- seed subtopic: 注意力; type: 原始研究; cross: []
- pages: 17

ABSTRACT: Gating mechanisms have been widely utilized, from early models like LSTMs and Highway Networks to recent state space models, linear attention, and also softmax attention. Yet, existing literature rarely examines the specific effects of gating. In this work, we conduct comprehensive experiments to systematically investigate gating-augmented softmax attention variants. Specifically, we perform a comprehensive comparison over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5 trillion token dataset. Our central finding is that a simple modification-applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)-consistently improves performance. This modification also enhances training stability, tolerates larger learning rates, and improves scaling properties. By comparing various gating positions and computational variants, we attribute this effectiveness to two key factors: (1) introducing non-linearity upon the low-rank mapping in the softmax attention, and (2) applying query-dependent sparse gating scores to modulate the SDPA output. Notably, we find this sparse gating mechanism mitigates 'attention sink' and enhances long-context extrapolation performance, and we also release related $\href{https://github.com/qiuzh20/gated_attention}{codes}$ and $\href{https://huggingface.co/QwQZh/gated_attention}{models}$ to facilitate future research.

## 01-014 | Simple linear attention language models balance the recall-throughput tradeoff
- arXiv: 2402.18668  first public: 2024-02-28  latest: 2025-03-07  primary cat: cs.CL
- authors (9): Simran Arora; Sabri Eyuboglu; Michael Zhang; Aman Timalsina; Silas Alberti; Dylan Zinsley ...
- seed subtopic: 注意力; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/HazyResearch/based
- pages: 78

ABSTRACT: Recent work has shown that attention-based language models excel at recall, the ability to ground generations in tokens previously seen in context. However, the efficiency of attention-based models is bottle-necked during inference by the KV-cache's aggressive memory consumption. In this work, we explore whether we can improve language model efficiency (e.g. by reducing memory consumption) without compromising on recall. By applying experiments and theory to a broad set of architectures, we identify a key tradeoff between a model's state size and recall ability. We show that efficient alternatives to attention (e.g. H3, Mamba, RWKV) maintain a fixed-size recurrent state, but struggle at recall. We propose BASED a simple architecture combining linear and sliding window attention. By varying BASED window size and linear attention feature dimension, we can dial the state size and traverse the pareto frontier of the recall-memory tradeoff curve, recovering the full quality of attention on one end and the small state size of attention-alternatives on the other. We train language models up to 1.3b parameters and show that BASED matches the strongest sub-quadratic models (e.g. Mamba) in perplexity and outperforms them on real-world recall-intensive tasks by 6.22 accuracy points. Implementations of linear attention are often less efficient than optimized standard attention implementations. To make BASED competitive, we develop IO-aware algorithms that enable 24x higher throughput on language generation than FlashAttention-2, when generating 1024 tokens using 1.3b parameter models. Code for this work is provided at: https://github.com/HazyResearch/based.

## 01-016 | When Attention Sink Emerges in Language Models: An Empirical View
- arXiv: 2410.10781  first public: 2024-10-14  latest: 2025-03-02  primary cat: cs.CL
- authors (8): Xiangming Gu; Tianyu Pang; Chao Du; Qian Liu; Fengzhuo Zhang; Cunxiao Du ...
- seed subtopic: 注意力; type: 原始研究; cross: []
- arXiv comment: ICLR 2025 (Spotlight)
- URLs on first pages of PDF: https://github.com/sail-sg/Attention-Sink
- pages: 31

ABSTRACT: Language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as attention sink. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others. Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sinks exist universally in LMs with various inputs, even in small models. Furthermore, attention sink is observed to emerge during the LM pre-training, motivating us to investigate how optimization, data distribution, loss function, and model architecture in LM pre-training influence its emergence. We highlight that attention sink emerges after effective optimization on sufficient training data. The sink position is highly correlated with the loss function and data distribution. Most importantly, we find that attention sink acts more like key biases, storing extra attention scores, which could be non-informative and not contribute to the value computation. We also observe that this phenomenon (at least partially) stems from tokens' inner dependence on attention scores as a result of softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, such as sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters. The code is available at https://github.com/sail-sg/Attention-Sink.

## 01-017 | MiniMax-01: Scaling Foundation Models with Lightning Attention
- arXiv: 2501.08313  first public: 2025-01-14  latest: 2025-01-14  primary cat: cs.CL
- authors (90): MiniMax; Aonian Li; Bangwei Gong; Bo Yang; Boji Shan; Chang Liu ...
- seed subtopic: 注意力; type: 技术报告; cross: ['11']
- arXiv comment: A technical report from MiniMax. The authors are listed in alphabetical order. We open-sourced our MiniMax-01 at https://github.com/MiniMax-AI
- URLs on first pages of PDF: https://github.com/MiniMax-AI
- pages: 68

ABSTRACT: We introduce MiniMax-01 series, including MiniMax-Text-01 and MiniMax-VL-01, which are comparable to top-tier models while offering superior capabilities in processing longer contexts. The core lies in lightning attention and its efficient scaling. To maximize computational capacity, we integrate it with Mixture of Experts (MoE), creating a model with 32 experts and 456 billion total parameters, of which 45.9 billion are activated for each token. We develop an optimized parallel strategy and highly efficient computation-communication overlap techniques for MoE and lightning attention. This approach enables us to conduct efficient training and inference on models with hundreds of billions of parameters across contexts spanning millions of tokens. The context window of MiniMax-Text-01 can reach up to 1 million tokens during training and extrapolate to 4 million tokens during inference at an affordable cost. Our vision-language model, MiniMax-VL-01 is built through continued training with 512 billion vision-language tokens. Experiments on both standard and in-house benchmarks show that our models match the performance of state-of-the-art models like GPT-4o and Claude-3.5-Sonnet while offering 20-32 times longer context window. We publicly release MiniMax-01 at https://github.com/MiniMax-AI.

## 01-018 | LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
- arXiv: 2402.13753  first public: 2024-02-21  latest: 2024-02-21  primary cat: cs.CL
- authors (8): Yiran Ding; Li Lyna Zhang; Chengruidong Zhang; Yuanyuan Xu; Ning Shang; Jiahang Xu ...
- seed subtopic: 位置编码; type: 原始研究; cross: []
- pages: 13

ABSTRACT: Large context window is a desirable feature in large language models (LLMs). However, due to high fine-tuning costs, scarcity of long texts, and catastrophic values introduced by new token positions, current extended context windows are limited to around 128k tokens. This paper introduces LongRoPE that, for the first time, extends the context window of pre-trained LLMs to an impressive 2048k tokens, with up to only 1k fine-tuning steps at within 256k training lengths, while maintaining performance at the original short context window. This is achieved by three key innovations: (i) we identify and exploit two forms of non-uniformities in positional interpolation through an efficient search, providing a better initialization for fine-tuning and enabling an 8x extension in non-fine-tuning scenarios; (ii) we introduce a progressive extension strategy that first fine-tunes a 256k length LLM and then conducts a second positional interpolation on the fine-tuned extended LLM to achieve a 2048k context window; (iii) we readjust LongRoPE on 8k length to recover the short context window performance. Extensive experiments on LLaMA2 and Mistral across various tasks demonstrate the effectiveness of our method. Models extended via LongRoPE retain the original architecture with minor modifications to the positional embedding, and can reuse most pre-existing optimizations.

## 01-019 | Round and Round We Go! What makes Rotary Positional Encodings useful?
- arXiv: 2410.06205  first public: 2024-10-08  latest: 2025-05-13  primary cat: cs.CL
- authors (5): Federico Barbero; Alex Vitvitskyi; Christos Perivolaropoulos; Razvan Pascanu; Petar Veličković
- seed subtopic: 位置编码; type: 原始研究; cross: []
- pages: 31

ABSTRACT: Positional Encodings (PEs) are a critical component of Transformer-based Large Language Models (LLMs), providing the attention mechanism with important sequence-position information. One of the most popular types of encoding used today in LLMs are Rotary Positional Encodings (RoPE), that rotate the queries and keys based on their relative distance. A common belief is that RoPE is useful because it helps to decay token dependency as relative distance increases. In this work, we argue that this is unlikely to be the core reason. We study the internals of a trained Gemma 7B model to understand how RoPE is being used at a mechanical level. We find that Gemma learns to use RoPE to construct robust "positional" attention patterns by exploiting the highest frequencies. We also find that, in general, Gemma greatly prefers to use the lowest frequencies of RoPE, which we suspect are used to carry semantic information. We mathematically prove interesting behaviours of RoPE and conduct experiments to verify our findings, proposing a modification of RoPE that fixes some highlighted issues and improves performance. We believe that this work represents an interesting step in better understanding PEs in LLMs, which we believe holds crucial value for scaling LLMs to large sizes and context lengths.

## 01-020 | Contextual Position Encoding: Learning to Count What's Important
- arXiv: 2405.18719  first public: 2024-05-29  latest: 2024-05-30  primary cat: cs.CL
- authors (4): Olga Golovneva; Tianlu Wang; Jason Weston; Sainbayar Sukhbaatar
- seed subtopic: 位置编码; type: 原始研究; cross: []
- pages: 17

ABSTRACT: The attention mechanism is a critical component of Large Language Models (LLMs) that allows tokens in a sequence to interact with each other, but is order-invariant. Incorporating position encoding (PE) makes it possible to address by position, such as attending to the i-th token. However, current PE methods use token counts to derive position, and thus cannot generalize to higher levels of abstraction, such as attending to the i-th sentence. In this paper, we propose a new position encoding method, Contextual Position Encoding (CoPE), that allows positions to be conditioned on context by incrementing position only on certain tokens determined by the model. This allows more general position addressing such as attending to the $i$-th particular word, noun, or sentence. We show that CoPE can solve the selective copy, counting and Flip-Flop tasks where popular position embeddings fail, and improves perplexity on language modeling and coding tasks.

## 01-022 | PaTH Attention: Position Encoding via Accumulating Householder Transformations
- arXiv: 2505.16381  first public: 2025-05-22  latest: 2026-02-03  primary cat: cs.CL
- authors (8): Songlin Yang; Yikang Shen; Kaiyue Wen; Shawn Tan; Mayank Mishra; Liliang Ren ...
- seed subtopic: 位置编码; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2025 camera ready
- URLs on first pages of PDF: https://github.com/fla-org/flash-linear-attention
- pages: 21

ABSTRACT: The attention mechanism is a core primitive in modern large language models (LLMs) and AI more broadly. Since attention by itself is permutation-invariant, position encoding is essential for modeling structured domains such as language. Rotary position encoding (RoPE) has emerged as the de facto standard approach for position encoding and is part of many modern LLMs. However, in RoPE the key/query transformation between two elements in a sequence is only a function of their relative position and otherwise independent of the actual input. This limits the expressivity of RoPE-based transformers. This paper describes PaTH, a flexible data-dependent position encoding scheme based on accumulated products of Householder(like) transformations, where each transformation is data-dependent, i.e., a function of the input. We derive an efficient parallel algorithm for training through exploiting a compact representation of products of Householder matrices, and implement a FlashAttention-style blockwise algorithm. Across both targeted synthetic benchmarks and moderate-scale real-world language modeling experiments, we find that PaTH improves upon RoPE and other recent baselines. Finally, we show that we can convert pretrained RoPE transformers into PaTH with continued pretraining.

## 01-023 | Length Extrapolation of Transformers: A Survey from the Perspective of Positional Encoding
- arXiv: 2312.17044  first public: 2023-12-28  latest: 2024-10-06  primary cat: cs.CL
- authors (9): Liang Zhao; Xiachong Feng; Xiaocheng Feng; Weihong Zhong; Dongliang Xu; Qing Yang ...
- seed subtopic: 位置编码; type: 综述; cross: []
- arXiv comment: Accepted to EMNLP 2024 Findings
- pages: 19

ABSTRACT: Built upon the Transformer, large language models (LLMs) have captured worldwide attention due to their remarkable abilities. Nevertheless, all Transformer-based models including LLMs suffer from a preset length limit and can hardly generalize from short training sequences to longer inference ones, namely, they cannot perform length extrapolation to handle long sequences, which severely hinders their application in scenarios demanding long input sequences such as legal or scientific documents. Thus, numerous methods have emerged to enhance the length extrapolation of Transformers. Despite the great research efforts, a systematic survey is still lacking. To fill this gap, we delve into these advances in a unified notation from the perspective of positional encoding (PE), as it has been considered the primary factor on length extrapolation. Specifically, we begin with extrapolatable PEs that have dominated this research field. Then, we dive into extrapolation methods based on them, covering position interpolation and randomized position methods. Finally, several challenges and future directions in this area are highlighted. Through this survey, we aim to enable the reader to gain a deep understanding of existing methods and provide stimuli for future research.

## 01-024 | Byte Latent Transformer: Patches Scale Better Than Tokens
- arXiv: 2412.09871  first public: 2024-12-13  latest: 2024-12-13  primary cat: cs.CL
- authors (14): Artidoro Pagnoni; Ram Pasunuru; Pedro Rodriguez; John Nguyen; Benjamin Muller; Margaret Li ...
- seed subtopic: 分词; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/facebookresearch/blt https://github.com/facebookresearch/blt
- pages: 27

ABSTRACT: We introduce the Byte Latent Transformer (BLT), a new byte-level LLM architecture that, for the first time, matches tokenization-based LLM performance at scale with significant improvements in inference efficiency and robustness. BLT encodes bytes into dynamically sized patches, which serve as the primary units of computation. Patches are segmented based on the entropy of the next byte, allocating more compute and model capacity where increased data complexity demands it. We present the first FLOP controlled scaling study of byte-level models up to 8B parameters and 4T training bytes. Our results demonstrate the feasibility of scaling models trained on raw bytes without a fixed vocabulary. Both training and inference efficiency improve due to dynamically selecting long patches when data is predictable, along with qualitative improvements on reasoning and long tail generalization. Overall, for fixed inference costs, BLT shows significantly better scaling than tokenization-based models, by simultaneously growing both patch and model size.

## 01-025 | Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies
- arXiv: 2407.13623  first public: 2024-07-18  latest: 2024-11-01  primary cat: cs.CL
- authors (8): Chaofan Tao; Qian Liu; Longxu Dou; Niklas Muennighoff; Zhongwei Wan; Ping Luo ...
- seed subtopic: 分词; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024
- URLs on first pages of PDF: https://github.com/sail-sg/scaling-with-vocab
- pages: 33

ABSTRACT: Research on scaling large language models (LLMs) has primarily focused on model parameters and training data size, overlooking the role of vocabulary size. We investigate how vocabulary size impacts LLM scaling laws by training models ranging from 33M to 3B parameters on up to 500B characters with various vocabulary configurations. We propose three complementary approaches for predicting the compute-optimal vocabulary size: IsoFLOPs analysis, derivative estimation, and parametric fit of the loss function. Our approaches converge on the conclusion that the optimal vocabulary size depends on the compute budget, with larger models requiring larger vocabularies. Most LLMs, however, use insufficient vocabulary sizes. For example, we predict that the optimal vocabulary size of Llama2-70B should have been at least 216K, 7 times larger than its vocabulary of 32K. We validate our predictions empirically by training models with 3B parameters across different FLOPs budgets. Adopting our predicted optimal vocabulary size consistently improves downstream performance over commonly used vocabulary sizes. By increasing the vocabulary size from the conventional 32K to 43K, we improve performance on ARC-Challenge from 29.1 to 32.0 with the same 2.3e21 FLOPs. Our work highlights the importance of jointly considering tokenization and model scaling for efficient pre-training. The code and demo are available at https://github.com/sail-sg/scaling-with-vocab and https://hf.co/spaces/sail/scaling-with-vocab-demo.

## 01-026 | SuperBPE: Space Travel for Language Models
- arXiv: 2503.13423  first public: 2025-03-17  latest: 2025-08-26  primary cat: cs.CL
- authors (6): Alisa Liu; Jonathan Hayase; Valentin Hofmann; Sewoong Oh; Noah A. Smith; Yejin Choi
- seed subtopic: 分词; type: 原始研究; cross: []
- arXiv comment: COLM 2025 camera-ready
- URLs on first pages of PDF: https://superbpe.github.io/
- pages: 30

ABSTRACT: The assumption across nearly all language model (LM) tokenization schemes is that tokens should be subwords, i.e., contained within word boundaries. While providing a seemingly reasonable inductive bias, is this common practice limiting the potential of modern LMs? Whitespace is not a reliable delimiter of meaning, as evidenced by multi-word expressions (e.g., "by the way"), crosslingual variation in the number of words needed to express a concept (e.g., "spacesuit helmet" in German is "raumanzughelm"), and languages that do not use whitespace at all (e.g., Chinese). To explore the potential of tokenization beyond subwords, we introduce a "superword" tokenizer, SuperBPE, which incorporates a simple pretokenization curriculum into the byte-pair encoding (BPE) algorithm to first learn subwords, then superwords that bridge whitespace. This brings dramatic improvements in encoding efficiency: when fixing the vocabulary size to 200k, SuperBPE encodes a fixed piece of text with up to 33% fewer tokens than BPE on average. In experiments, we pretrain 8B transformer LMs from scratch while fixing the model size, vocabulary size, and train compute, varying *only* the algorithm for learning the vocabulary. Our model trained with SuperBPE achieves an average +4.0% absolute improvement over the BPE baseline across 30 downstream tasks (including +8.2% on MMLU), while simultaneously requiring 27% less compute at inference time. In analysis, we find that SuperBPE results in segmentations of text that are more uniform in per-token difficulty. Qualitatively, this may be because SuperBPE tokens often capture common multi-word expressions that function semantically as a single unit. SuperBPE is a straightforward, local modification to tokenization that improves both encoding efficiency and downstream performance, yielding better language models overall.

## 01-027 | Tokenization Is More Than Compression
- arXiv: 2402.18376  first public: 2024-02-28  latest: 2024-10-07  primary cat: cs.CL
- authors (7): Craig W. Schmidt; Varshini Reddy; Haoran Zhang; Alec Alameddine; Omri Uzan; Yuval Pinter ...
- seed subtopic: 分词; type: 原始研究; cross: []
- arXiv comment: EMNLP 2024
- URLs on first pages of PDF: https://github.com/MeLeLBGU/SaGe https://github.com/huggingface/
- pages: 25

ABSTRACT: Tokenization is a foundational step in natural language processing (NLP) tasks, bridging raw text and language models. Existing tokenization approaches like Byte-Pair Encoding (BPE) originate from the field of data compression, and it has been suggested that the effectiveness of BPE stems from its ability to condense text into a relatively small number of tokens. We test the hypothesis that fewer tokens lead to better downstream performance by introducing PathPiece, a new tokenizer that segments a document's text into the minimum number of tokens for a given vocabulary. Through extensive experimentation we find this hypothesis not to be the case, casting doubt on the understanding of the reasons for effective tokenization. To examine which other factors play a role, we evaluate design decisions across all three phases of tokenization: pre-tokenization, vocabulary construction, and segmentation, offering new insights into the design of effective tokenizers. Specifically, we illustrate the importance of pre-tokenization and the benefits of using BPE to initialize vocabulary construction. We train 64 language models with varying tokenization, ranging in size from 350M to 2.4B parameters, all of which are made publicly available.

## 01-028 | Dynamic Chunking for End-to-End Hierarchical Sequence Modeling
- arXiv: 2507.07955  first public: 2025-07-10  latest: 2025-07-15  primary cat: cs.LG
- authors (3): Sukjun Hwang; Brandon Wang; Albert Gu
- seed subtopic: 分词; type: 原始研究; cross: []
- pages: 39

ABSTRACT: Major progress on language models (LMs) in recent years has largely resulted from moving away from specialized models designed for specific tasks, to general models based on powerful architectures (e.g. the Transformer) that learn everything from raw data. Despite this trend, pre-processing steps such as tokenization remain a barrier to true end-to-end foundation models. We introduce a collection of new techniques that enable a dynamic chunking mechanism which automatically learns content- and context- dependent segmentation strategies learned jointly with the rest of the model. Incorporating this into an explicit hierarchical network (H-Net) allows replacing the (implicitly hierarchical) tokenization-LM-detokenization pipeline with a single model learned fully end-to-end. When compute- and data- matched, an H-Net with one stage of hierarchy operating at the byte level outperforms a strong Transformer language model operating over BPE tokens. Iterating the hierarchy to multiple stages further increases its performance by modeling multiple levels of abstraction, demonstrating significantly better scaling with data and matching the token-based Transformer of twice its size. H-Nets pretrained on English show significantly increased character-level robustness, and qualitatively learn meaningful data-dependent chunking strategies without any heuristics or explicit supervision. Finally, the H-Net's improvement over tokenized pipelines is further increased in languages and modalities with weaker tokenization heuristics, such as Chinese and code, or DNA sequences (nearly 4x improvement in data efficiency over baselines), showing the potential of true end-to-end models that learn and scale better from unprocessed data.

## 01-030 | Better & Faster Large Language Models via Multi-token Prediction
- arXiv: 2404.19737  first public: 2024-04-30  latest: 2024-04-30  primary cat: cs.CL
- authors (5): Fabian Gloeckle; Badr Youbi Idrissi; Baptiste Rozière; David Lopez-Paz; Gabriel Synnaeve
- seed subtopic: 训练目标; type: 原始研究; cross: []
- pages: 29

ABSTRACT: Large language models such as GPT and Llama are trained with a next-token prediction loss. In this work, we suggest that training language models to predict multiple future tokens at once results in higher sample efficiency. More specifically, at each position in the training corpus, we ask the model to predict the following n tokens using n independent output heads, operating on top of a shared model trunk. Considering multi-token prediction as an auxiliary training task, we measure improved downstream capabilities with no overhead in training time for both code and natural language models. The method is increasingly useful for larger model sizes, and keeps its appeal when training for multiple epochs. Gains are especially pronounced on generative benchmarks like coding, where our models consistently outperform strong baselines by several percentage points. Our 13B parameter models solves 12 % more problems on HumanEval and 17 % more on MBPP than comparable next-token models. Experiments on small algorithmic tasks demonstrate that multi-token prediction is favorable for the development of induction heads and algorithmic reasoning capabilities. As an additional benefit, models trained with 4-token prediction are up to 3 times faster at inference, even with large batch sizes.

## 01-031 | Rho-1: Not All Tokens Are What You Need
- arXiv: 2404.07965  first public: 2024-04-11  latest: 2025-01-08  primary cat: cs.CL
- authors (11): Zhenghao Lin; Zhibin Gou; Yeyun Gong; Xiao Liu; Yelong Shen; Ruochen Xu ...
- seed subtopic: 训练目标; type: 原始研究; cross: ['02']
- arXiv comment: First two authors equal contribution
- pages: 28

ABSTRACT: Previous language model pre-training methods have uniformly applied a next-token prediction loss to all training tokens. Challenging this norm, we posit that "9l training". Our initial analysis examines token-level training dynamics of language model, revealing distinct loss patterns for different tokens. Leveraging these insights, we introduce a new language model called Rho-1. Unlike traditional LMs that learn to predict every next token in a corpus, Rho-1 employs Selective Language Modeling (SLM), which selectively trains on useful tokens that aligned with the desired distribution. This approach involves scoring pretraining tokens using a reference model, and then training the language model with a focused loss on tokens with higher scores. When continual pretraining on 15B OpenWebMath corpus, Rho-1 yields an absolute improvement in few-shot accuracy of up to 30% in 9 math tasks. After fine-tuning, Rho-1-1B and 7B achieved state-of-the-art results of 40.6% and 51.8% on MATH dataset, respectively - matching DeepSeekMath with only 3% of the pretraining tokens. Furthermore, when continual pretraining on 80B general tokens, Rho-1 achieves 6.8% average enhancement across 15 diverse tasks, increasing both efficiency and performance of the language model pre-training.

## 01-032 | Large Language Diffusion Models
- arXiv: 2502.09992  first public: 2025-02-14  latest: 2025-10-18  primary cat: cs.CL
- authors (10): Shen Nie; Fengqi Zhu; Zebin You; Xiaolu Zhang; Jingyang Ou; Jun Hu ...
- seed subtopic: 训练目标; type: 原始研究; cross: []
- URLs on first pages of PDF: https://ml-gsai.github.io/LLaDA-demo/
- pages: 33

ABSTRACT: The capabilities of large language models (LLMs) are widely regarded as relying on autoregressive models (ARMs). We challenge this notion by introducing LLaDA, a diffusion model trained from scratch under the pre-training and supervised fine-tuning (SFT) paradigm. LLaDA employs a forward data masking process and a reverse generation process, parameterized by a Transformer to predict masked tokens. It provides a principled generative approach for probabilistic inference by optimizing a likelihood lower bound. Across extensive benchmarks on general tasks, math, code, and so on, LLaDA demonstrates strong scalability and performs comparably to our self-constructed ARM baselines. Remarkably, LLaDA 8B is competitive with strong LLMs like LLaMA3 8B in in-context learning and, after SFT, exhibits impressive instruction-following abilities in case studies such as multi-turn dialogue. Moreover, LLaDA addresses the reversal curse, surpassing GPT-4o in a reversal poem completion task. Our findings show the promise of diffusion models for language modeling at scale and challenge the common assumption that core LLM capabilities discussed above inherently depend on ARMs. Project page and codes: https://ml-gsai.github.io/LLaDA-demo/.

## 01-033 | Simple and Effective Masked Diffusion Language Models
- arXiv: 2406.07524  first public: 2024-06-11  latest: 2024-11-10  primary cat: cs.CL
- authors (8): Subham Sekhar Sahoo; Marianne Arriola; Yair Schiff; Aaron Gokaslan; Edgar Marroquin; Justin T Chiu ...
- seed subtopic: 训练目标; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024. We provide the code at https://github.com/kuleshov-group/mdlm
- URLs on first pages of PDF: https://github.com/kuleshov-group/mdlm
- pages: 49

ABSTRACT: While diffusion models excel at generating high-quality images, prior work reports a significant performance gap between diffusion and autoregressive (AR) methods in language modeling. In this work, we show that simple masked discrete diffusion is more performant than previously thought. We apply an effective training recipe that improves the performance of masked diffusion models and derive a simplified, Rao-Blackwellized objective that results in additional improvements. Our objective has a simple form -- it is a mixture of classical masked language modeling losses -- and can be used to train encoder-only language models that admit efficient samplers, including ones that can generate arbitrary lengths of text semi-autoregressively like a traditional language model. On language modeling benchmarks, a range of masked diffusion models trained with modern engineering practices achieves a new state-of-the-art among diffusion models, and approaches AR perplexity. We provide the code, along with a blog post and video tutorial on the project page: https://s-sahoo.com/mdlm

## 01-034 | Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models
- arXiv: 2503.09573  first public: 2025-03-12  latest: 2025-05-17  primary cat: cs.LG
- authors (8): Marianne Arriola; Aaron Gokaslan; Justin T. Chiu; Zhihan Yang; Zhixuan Qi; Jiaqi Han ...
- seed subtopic: 训练目标; type: 原始研究; cross: []
- arXiv comment: ICLR 2025 Oral. We provide the code at https://github.com/kuleshov-group/bd3lms
- URLs on first pages of PDF: https://github.com/kuleshov-group/bd3lms
- pages: 28

ABSTRACT: Diffusion language models offer unique benefits over autoregressive models due to their potential for parallelized generation and controllability, yet they lag in likelihood modeling and are limited to fixed-length generation. In this work, we introduce a class of block diffusion language models that interpolate between discrete denoising diffusion and autoregressive models. Block diffusion overcomes key limitations of both approaches by supporting flexible-length generation and improving inference efficiency with KV caching and parallel token sampling. We propose a recipe for building effective block diffusion models that includes an efficient training algorithm, estimators of gradient variance, and data-driven noise schedules to minimize the variance. Block diffusion sets a new state-of-the-art performance among diffusion models on language modeling benchmarks and enables generation of arbitrary-length sequences. We provide the code, along with the model weights and blog post on the project page: https://m-arriola.com/bd3lms

## 01-036 | Muon is Scalable for LLM Training
- arXiv: 2502.16982  first public: 2025-02-24  latest: 2025-02-24  primary cat: cs.LG
- authors (28): Jingyuan Liu; Jianlin Su; Xingcheng Yao; Zhejun Jiang; Guokun Lai; Yulun Du ...
- seed subtopic: 训练目标; type: 原始研究; cross: ['11']
- pages: 19

ABSTRACT: Recently, the Muon optimizer based on matrix orthogonalization has demonstrated strong results in training small-scale language models, but the scalability to larger models has not been proven. We identify two crucial techniques for scaling up Muon: (1) adding weight decay and (2) carefully adjusting the per-parameter update scale. These techniques allow Muon to work out-of-the-box on large-scale training without the need of hyper-parameter tuning. Scaling law experiments indicate that Muon achieves $\sim\!2\times$ computational efficiency compared to AdamW with compute optimal training. Based on these improvements, we introduce Moonlight, a 3B/16B-parameter Mixture-of-Expert (MoE) model trained with 5.7T tokens using Muon. Our model improves the current Pareto frontier, achieving better performance with much fewer training FLOPs compared to prior models. We open-source our distributed Muon implementation that is memory optimal and communication efficient. We also release the pretrained, instruction-tuned, and intermediate checkpoints to support future research.

## 01-037 | Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws
- arXiv: 2401.00448  first public: 2023-12-31  latest: 2025-04-14  primary cat: cs.LG
- authors (4): Nikhil Sardana; Jacob Portes; Sasha Doubov; Jonathan Frankle
- seed subtopic: 规模规律; type: 原始研究; cross: []
- arXiv comment: 16 pages, 7 figures, In the 41st International Conference on Machine Learning, 2024
- pages: 16

ABSTRACT: Large language model (LLM) scaling laws are empirical formulas that estimate changes in model quality as a result of increasing parameter count and training data. However, these formulas, including the popular Deepmind Chinchilla scaling laws, neglect to include the cost of inference. We modify the Chinchilla scaling laws to calculate the optimal LLM parameter count and pre-training data size to train and deploy a model of a given quality and inference demand. We conduct our analysis both in terms of a compute budget and real-world costs and find that LLM researchers expecting reasonably large inference demand (~1B requests) should train models smaller and longer than Chinchilla-optimal. Furthermore, we train 47 models of varying sizes and parameter counts to validate our formula and find that model quality continues to improve as we scale tokens per parameter to extreme ranges (up to 10,000). Finally, we ablate the procedure used to fit the Chinchilla scaling law coefficients and find that developing scaling laws only from data collected at typical token/parameter ratios overestimates the impact of additional tokens at these extreme ranges.

## 01-038 | Language models scale reliably with over-training and on downstream tasks
- arXiv: 2403.08540  first public: 2024-03-13  latest: 2024-06-14  primary cat: cs.CL
- authors (25): Samir Yitzhak Gadre; Georgios Smyrnis; Vaishaal Shankar; Suchin Gururangan; Mitchell Wortsman; Rulin Shao ...
- seed subtopic: 规模规律; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/mlfoundations/scaling
- pages: 43

ABSTRACT: Scaling laws are useful guides for derisking expensive training runs, as they predict performance of large models using cheaper, small-scale experiments. However, there remain gaps between current scaling studies and how language models are ultimately trained and evaluated. For instance, scaling is usually studied in the compute-optimal training regime (i.e., "Chinchilla optimal" regime). In contrast, models are often over-trained to reduce inference costs. Moreover, scaling laws mostly predict loss on next-token prediction, but models are usually compared on downstream task performance. To address both shortcomings, we create a testbed of 104 models with 0.011B to 6.9B parameters trained with various numbers of tokens on three data distributions. First, we fit scaling laws that extrapolate in both the amount of over-training and the number of model parameters. This enables us to predict the validation loss of a 1.4B parameter, 900B token run (i.e., 32$\times$ over-trained) and a 6.9B parameter, 138B token run (i.e., a compute-optimal run)$\unicode{x2014}$each from experiments that take 300$\times$ less compute. Second, we relate the perplexity of a language model to its downstream task performance by proposing a power law. We use this law to predict top-1 error averaged over downstream tasks for the two aforementioned models, using experiments that take 20$\times$ less compute. Our experiments are available at https://github.com/mlfoundations/scaling.

## 01-039 | Observational Scaling Laws and the Predictability of Language Model Performance
- arXiv: 2405.10938  first public: 2024-05-17  latest: 2024-10-01  primary cat: cs.LG
- authors (3): Yangjun Ruan; Chris J. Maddison; Tatsunori Hashimoto
- seed subtopic: 规模规律; type: 原始研究; cross: []
- arXiv comment: Accepted at NeurIPS 2024 as a spotlight
- pages: 45

ABSTRACT: Understanding how language model performance varies with scale is critical to benchmark and algorithm development. Scaling laws are one approach to building this understanding, but the requirement of training models across many different scales has limited their use. We propose an alternative, observational approach that bypasses model training and instead builds scaling laws from ~100 publically available models. Building a single scaling law from multiple model families is challenging due to large variations in their training compute efficiencies and capabilities. However, we show that these variations are consistent with a simple, generalized scaling law where language model performance is a function of a low-dimensional capability space, and model families only vary in their efficiency in converting training compute to capabilities. Using this approach, we show the surprising predictability of complex scaling phenomena: we show that several emergent phenomena follow a smooth, sigmoidal behavior and are predictable from small models; we show that the agent performance of models such as GPT-4 can be precisely predicted from simpler non-agentic benchmarks; and we show how to predict the impact of post-training interventions like Chain-of-Thought and Self-Consistency as language model capabilities continue to improve.

## 01-041 | Scaling Laws for Precision
- arXiv: 2411.04330  first public: 2024-11-07  latest: 2024-11-30  primary cat: cs.LG
- authors (9): Tanishq Kumar; Zachary Ankner; Benjamin F. Spector; Blake Bordelon; Niklas Muennighoff; Mansheej Paul ...
- seed subtopic: 规模规律; type: 原始研究; cross: ['11']
- pages: 37

ABSTRACT: Low precision training and inference affect both the quality and cost of language models, but current scaling laws do not account for this. In this work, we devise "precision-aware" scaling laws for both training and inference. We propose that training in lower precision reduces the model's "effective parameter count," allowing us to predict the additional loss incurred from training in low precision and post-train quantization. For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful. For training, our scaling laws allow us to predict the loss of a model with different parts in different precisions, and suggest that training larger models in lower precision may be compute optimal. We unify the scaling laws for post and pretraining quantization to arrive at a single functional form that predicts degradation from training and inference in varied precisions. We fit on over 465 pretraining runs and validate our predictions on model sizes up to 1.7B parameters trained on up to 26B tokens.

## 01-042 | Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations
- arXiv: 2405.18392  first public: 2024-05-28  latest: 2024-10-17  primary cat: cs.LG
- authors (6): Alexander Hägele; Elie Bakouch; Atli Kosson; Loubna Ben Allal; Leandro Von Werra; Martin Jaggi
- seed subtopic: 规模规律; type: 原始研究; cross: []
- arXiv comment: Spotlight at NeurIPS 2024
- URLs on first pages of PDF: https://github.com/epfml/schedules-and-scaling/ https://huggingface.co/datasets/DKYoon/SlimPajama-6B
- pages: 26

ABSTRACT: Scale has become a main ingredient in obtaining strong machine learning models. As a result, understanding a model's scaling properties is key to effectively designing both the right training setup as well as future generations of architectures. In this work, we argue that scale and training research has been needlessly complex due to reliance on the cosine schedule, which prevents training across different lengths for the same model size. We investigate the training behavior of a direct alternative -- constant learning rate and cooldowns -- and find that it scales predictably and reliably similar to cosine. Additionally, we show that stochastic weight averaging yields improved performance along the training trajectory, without additional training costs, across different scales. Importantly, with these findings we demonstrate that scaling experiments can be performed with significantly reduced compute and GPU hours by utilizing fewer but reusable training runs. Our code is available at \url{https://github.com/epfml/schedules-and-scaling/}.

## 01-044 | DeepSeek LLM: Scaling Open-Source Language Models with Longtermism
- arXiv: 2401.02954  first public: 2024-01-05  latest: 2024-01-05  primary cat: cs.CL
- authors (88): DeepSeek-AI; :; Xiao Bi; Deli Chen; Guanting Chen; Shanhuang Chen ...
- seed subtopic: 规模规律; type: 技术报告; cross: []
- pages: 48

ABSTRACT: The rapid development of open-source large language models (LLMs) has been truly remarkable. However, the scaling law described in previous literature presents varying conclusions, which casts a dark cloud over scaling LLMs. We delve into the study of scaling laws and present our distinctive findings that facilitate scaling of large scale models in two commonly used open-source configurations, 7B and 67B. Guided by the scaling laws, we introduce DeepSeek LLM, a project dedicated to advancing open-source language models with a long-term perspective. To support the pre-training phase, we have developed a dataset that currently consists of 2 trillion tokens and is continuously expanding. We further conduct supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) on DeepSeek LLM Base models, resulting in the creation of DeepSeek Chat models. Our evaluation results demonstrate that DeepSeek LLM 67B surpasses LLaMA-2 70B on various benchmarks, particularly in the domains of code, mathematics, and reasoning. Furthermore, open-ended evaluations reveal that DeepSeek LLM 67B Chat exhibits superior performance compared to GPT-3.5.

## 01-045 | Kimi Linear: An Expressive, Efficient Attention Architecture
- arXiv: 2510.26692  first public: 2025-10-30  latest: 2025-11-01  primary cat: cs.CL
- authors (60): Kimi Team; Yu Zhang; Zongyu Lin; Xingcheng Yao; Jiaxi Hu; Fanqing Meng ...
- seed subtopic: 注意力; type: 原始研究; cross: ['11']
- arXiv comment: Kimi Linear tech report
- URLs on first pages of PDF: https://github.com/MoonshotAI/Kimi-Linear https://github.com/fla-org/flash-linear-attention/tree/main/fla/ops/kda https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct
- pages: 28

ABSTRACT: We introduce Kimi Linear, a hybrid linear attention architecture that, for the first time, outperforms full attention under fair comparisons across various scenarios -- including short-context, long-context, and reinforcement learning (RL) scaling regimes. At its core lies Kimi Delta Attention (KDA), an expressive linear attention module that extends Gated DeltaNet with a finer-grained gating mechanism, enabling more effective use of limited finite-state RNN memory. Our bespoke chunkwise algorithm achieves high hardware efficiency through a specialized variant of the Diagonal-Plus-Low-Rank (DPLR) transition matrices, which substantially reduces computation compared to the general DPLR formulation while remaining more consistent with the classical delta rule. We pretrain a Kimi Linear model with 3B activated parameters and 48B total parameters, based on a layerwise hybrid of KDA and Multi-Head Latent Attention (MLA). Our experiments show that with an identical training recipe, Kimi Linear outperforms full MLA with a sizeable margin across all evaluated tasks, while reducing KV cache usage by up to 75% and achieving up to 6 times decoding throughput for a 1M context. These results demonstrate that Kimi Linear can be a drop-in replacement for full attention architectures with superior performance and efficiency, including tasks with longer input and output lengths. To support further research, we open-source the KDA kernel and vLLM implementations, and release the pre-trained and instruction-tuned model checkpoints.

## 01-047 | Hybrid Architectures for Language Models: Systematic Analysis and Design Insights
- arXiv: 2510.04800  first public: 2025-10-06  latest: 2026-04-21  primary cat: cs.CL
- authors (8): Sangmin Bae; Bilge Acun; Chien-Yu Lin; Haroun Habeeb; Seungyeon Kim; Liang Luo ...
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: 41 pages, 8 figures, 22 tables;
- pages: 41

ABSTRACT: Recent progress in large language models demonstrates that hybrid architectures--combining self-attention mechanisms with structured state space models like Mamba--can achieve a compelling balance between modeling quality and computational efficiency, particularly for long-context tasks. While these hybrid models show promising performance, systematic comparisons of hybridization strategies and analyses on the key factors behind their effectiveness have not been clearly shared to the community. In this work, we present a holistic evaluation of hybrid architectures based on inter-layer (sequential) or intra-layer (parallel) fusion. We comprehensively evaluate these designs across multiple dimensions: language modeling and downstream task performance, long-context capabilities, scaling analysis, and training and inference efficiency. By investigating the core characteristics of their computational primitive, we identify the most critical elements for each hybridization strategy and further propose optimal design recipes for hybrid models. Our comprehensive analysis provides practical guidance and valuable insights for developing hybrid language models, facilitating the optimization of architectural configurations.

## 01-049 | Diffusion Beats Autoregressive in Data-Constrained Settings
- arXiv: 2507.15857  first public: 2025-07-21  latest: 2025-10-26  primary cat: cs.LG
- authors (5): Mihir Prabhudesai; Mengning Wu; Amir Zadeh; Katerina Fragkiadaki; Deepak Pathak
- seed subtopic: 训练目标; type: 原始研究; cross: []
- arXiv comment: Project Webpage: https://diffusion-scaling.github.io
- pages: 26

ABSTRACT: Autoregressive (AR) models have long dominated the landscape of large language models, driving progress across a wide range of tasks. Recently, diffusion-based language models have emerged as a promising alternative, though their advantages over AR models remain underexplored. In this paper, we systematically study masked diffusion models in data-constrained settings where training involves repeated passes over limited data and find that they significantly outperform AR models when compute is abundant but data is scarce. Diffusion models make better use of repeated data, achieving lower validation loss and superior downstream performance. We find new scaling laws for diffusion models and derive a closed-form expression for the critical compute threshold at which diffusion begins to outperform AR. Finally, we explain why diffusion models excel in this regime: their randomized masking objective implicitly trains over a rich distribution of token orderings, acting as an implicit data augmentation that AR's fixed left-to-right factorization lacks. Our results suggest that when data, not compute, is the bottleneck, diffusion models offer a compelling alternative to the standard AR paradigm. Our code is available at: https://diffusion-scaling.github.io.

## 01-050 | Fantastic Pretraining Optimizers and Where to Find Them
- arXiv: 2509.02046  first public: 2025-09-02  latest: 2026-10-25  primary cat: cs.LG
- authors (4): Kaiyue Wen; David Hall; Tengyu Ma; Percy Liang
- seed subtopic: 训练目标; type: 原始研究; cross: []
- arXiv comment: 108 pages, 8 figures, reproducible runs available at https://wandb.ai/marin-community/optimizer-scaling
- pages: 108

ABSTRACT: AdamW has long been the dominant optimizer in language model pretraining, despite numerous claims that alternative optimizers offer 1.4 to 2x speedup. We posit that two methodological shortcomings have obscured fair comparisons and hindered practical adoption: (i) unequal hyperparameter tuning and (ii) limited or misleading evaluation setups. To address these two issues, we conduct a systematic study of ten deep learning optimizers across four model scales (0.1B-1.2B parameters) and data-to-model ratios (1-8x the Chinchilla optimum). We find that fair and informative comparisons require rigorous hyperparameter tuning and evaluations across a range of model scales and data-to-model ratios, performed at the end of training. First, optimal hyperparameters for one optimizer may be suboptimal for another, making blind hyperparameter transfer unfair. Second, the actual speedup of many proposed optimizers over well-tuned baselines is lower than claimed and decreases with model size to only 1.1x for 1.2B parameter models. Thirdly, comparing intermediate checkpoints before reaching the target training budgets can be misleading, as rankings between two optimizers can flip during training due to learning rate decay. Through our thorough investigation, we find that all the fastest optimizers such as Muon and Soap, use matrices as preconditioners -- multiplying gradients with matrices rather than entry-wise scalars. However, the speedup of matrix-based optimizers is inversely proportional to model scale, decreasing from 1.4x over AdamW for 0.1B parameter models to merely 1.1x for 1.2B parameter models.

## 01-051 | Qwen3 Technical Report
- arXiv: 2505.09388  first public: 2025-05-14  latest: 2025-05-14  primary cat: cs.CL
- authors (60): An Yang; Anfeng Li; Baosong Yang; Beichen Zhang; Binyuan Hui; Bo Zheng ...
- seed subtopic: 模型设计与技术报告; type: 技术报告; cross: ['04']
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen3 https://huggingface.co/Qwen
- pages: 35

ABSTRACT: In this work, we present Qwen3, the latest version of the Qwen model family. Qwen3 comprises a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion. A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework. This eliminates the need to switch between different models--such as chat-optimized models (e.g., GPT-4o) and dedicated reasoning models (e.g., QwQ-32B)--and enables dynamic mode switching based on user queries or chat templates. Meanwhile, Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity. Moreover, by leveraging the knowledge from the flagship models, we significantly reduce the computational resources required to build smaller-scale models, while ensuring their highly competitive performance. Empirical evaluations demonstrate that Qwen3 achieves state-of-the-art results across diverse benchmarks, including tasks in code generation, mathematical reasoning, agent tasks, etc., competitive against larger MoE models and proprietary models. Compared to its predecessor Qwen2.5, Qwen3 expands multilingual support from 29 to 119 languages and dialects, enhancing global accessibility through improved cross-lingual understanding and generation capabilities. To facilitate reproducibility and community-driven research and development, all Qwen3 models are publicly accessible under Apache 2.0.

## 01-052 | Gemma 3 Technical Report
- arXiv: 2503.19786  first public: 2025-03-25  latest: 2025-03-25  primary cat: cs.CL
- authors (216): Gemma Team; Aishwarya Kamath; Johan Ferret; Shreya Pathak; Nino Vieillard; Ramona Merhej ...
- seed subtopic: 模型设计与技术报告; type: 技术报告; cross: []
- pages: 25

ABSTRACT: We introduce Gemma 3, a multimodal addition to the Gemma family of lightweight open models, ranging in scale from 1 to 27 billion parameters. This version introduces vision understanding abilities, a wider coverage of languages and longer context - at least 128K tokens. We also change the architecture of the model to reduce the KV-cache memory that tends to explode with long context. This is achieved by increasing the ratio of local to global attention layers, and keeping the span on local attention short. The Gemma 3 models are trained with distillation and achieve superior performance to Gemma 2 for both pre-trained and instruction finetuned versions. In particular, our novel post-training recipe significantly improves the math, chat, instruction-following and multilingual abilities, making Gemma3-4B-IT competitive with Gemma2-27B-IT and Gemma3-27B-IT comparable to Gemini-1.5-Pro across benchmarks. We release all our models to the community.

## 01-053 | 2 OLMo 2 Furious
- arXiv: 2501.00656  first public: 2024-12-31  latest: 2025-10-08  primary cat: cs.CL
- authors (43): Team OLMo; Pete Walsh; Luca Soldaini; Dirk Groeneveld; Kyle Lo; Shane Arora ...
- seed subtopic: 模型设计与技术报告; type: 技术报告; cross: ['02']
- arXiv comment: Shorter version accepted to COLM 2025. Updated to include 32B results. Model demo available at playground.allenai.org
- pages: 58

ABSTRACT: We present OLMo 2, the next generation of our fully open language models. OLMo 2 includes a family of dense autoregressive language models at 7B, 13B and 32B scales with fully released artifacts -- model weights, full training data, training code and recipes, training logs and thousands of intermediate checkpoints. In this work, we describe our modified model architecture and training recipe, focusing on techniques for achieving better training stability and improved per-token efficiency. Our updated pretraining data mixture introduces a new, specialized data mix called Dolmino Mix 1124, which significantly improves model capabilities across many downstream task benchmarks when introduced via late-stage curriculum training (i.e. specialized data during the annealing phase of pretraining). Finally, we incorporate best practices from Tülu 3 to develop OLMo 2-Instruct, focusing on permissive data and extending our final-stage reinforcement learning with verifiable rewards (RLVR). Our OLMo 2 base models sit at the Pareto frontier of performance to training compute, often matching or outperforming open-weight only models like Llama 3.1, Qwen 2.5, and Gemma 2 while using fewer FLOPs and with fully transparent training data, code, and recipe. Our fully open OLMo 2-Instruct models are competitive with open-weight only models of comparable size and even some proprietary models like GPT-3.5 Turbo and GPT 4o Mini.

## 01-055 | Speed Always Wins: A Survey on Efficient Architectures for Large Language Models
- arXiv: 2508.09834  first public: 2025-08-13  latest: 2025-08-13  primary cat: cs.CL
- authors (15): Weigao Sun; Jiaxi Hu; Yucheng Zhou; Jusen Du; Disen Lan; Kexin Wang ...
- seed subtopic: 架构; type: 综述; cross: ['11']
- arXiv comment: Survey, 82 pages, GitHub: https://github.com/weigao266/Awesome-Efficient-Arch
- URLs on first pages of PDF: https://github.com/weigao266/Awesome-Efficient-Arch
- pages: 82

ABSTRACT: Large Language Models (LLMs) have delivered impressive results in language understanding, generation, reasoning, and pushes the ability boundary of multimodal models. Transformer models, as the foundation of modern LLMs, offer a strong baseline with excellent scaling properties. However, the traditional transformer architecture requires substantial computations and poses significant obstacles for large-scale training and practical deployment. In this survey, we offer a systematic examination of innovative LLM architectures that address the inherent limitations of transformers and boost the efficiency. Starting from language modeling, this survey covers the background and technical details of linear and sparse sequence modeling methods, efficient full attention variants, sparse mixture-of-experts, hybrid model architectures incorporating the above techniques, and emerging diffusion LLMs. Additionally, we discuss applications of these techniques to other modalities and consider their wider implications for developing scalable, resource-aware foundation models. By grouping recent studies into the above category, this survey presents a blueprint of modern efficient LLM architectures, and we hope this could help motivate future research toward more efficient, versatile AI systems.

## 01-056 | A Survey on Diffusion Language Models
- arXiv: 2508.10875  first public: 2025-08-14  latest: 2026-06-04  primary cat: cs.CL
- authors (4): Tianyi Li; Mingda Chen; Bowei Guo; Zhiqiang Shen
- seed subtopic: 训练目标; type: 综述; cross: []
- URLs on first pages of PDF: https://github.com/VILA-Lab/Awesome-DLMs
- pages: 26

ABSTRACT: Diffusion Language Models (DLMs) are rapidly emerging as a powerful and promising alternative to the dominant autoregressive (AR) paradigm. By generating tokens in parallel through an iterative denoising process, DLMs possess inherent advantages in reducing inference latency and capturing bidirectional context, thereby enabling fine-grained control over the generation process. While achieving a several-fold speed-up, recent advancements have allowed DLMs to show performance comparable to their autoregressive counterparts, making them a compelling choice for various natural language processing tasks. In this survey, we provide a holistic overview of the current DLM landscape. We trace its evolution and relationship with other paradigms, such as autoregressive and masked language models, and cover both foundational principles and state-of-the-art models. Our work offers an up-to-date, comprehensive taxonomy and an in-depth analysis of current techniques, from pre-training strategies to advanced post-training methods. Another contribution of this survey is a thorough review of DLM inference strategies and optimizations, including improvements in decoding parallelism, caching mechanisms, and generation quality. We also highlight the latest approaches to multimodal extensions of DLMs and delineate their applications across various practical scenarios. Furthermore, our discussion addresses the limitations and challenges of DLMs, including efficiency, long-sequence handling, and infrastructure requirements, while outlining future research directions to sustain progress in this rapidly evolving field. Project GitHub is available at https://github.com/VILA-Lab/Awesome-DLMs.

## 01-057 | Attention Is All You Need
- arXiv: 1706.03762  first public: 2017-06-12  latest: 2023-08-02  primary cat: cs.CL
- authors (8): Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez ...
- seed subtopic: 架构; type: 原始研究; cross: []
- arXiv comment: 15 pages, 5 figures
- pages: 15

ABSTRACT: The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## 01-058 | Scaling Laws for Neural Language Models
- arXiv: 2001.08361  first public: 2020-01-23  latest: 2020-01-23  primary cat: cs.LG
- authors (10): Jared Kaplan; Sam McCandlish; Tom Henighan; Tom B. Brown; Benjamin Chess; Rewon Child ...
- seed subtopic: 规模规律; type: 原始研究; cross: []
- arXiv comment: 19 pages, 15 figures
- pages: 30

ABSTRACT: We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

## 01-059 | Training Compute-Optimal Large Language Models
- arXiv: 2203.15556  first public: 2022-03-29  latest: 2022-03-29  primary cat: cs.CL
- authors (22): Jordan Hoffmann; Sebastian Borgeaud; Arthur Mensch; Elena Buchatskaya; Trevor Cai; Eliza Rutherford ...
- seed subtopic: 规模规律; type: 原始研究; cross: []
- pages: 36

ABSTRACT: We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4$\times$ more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

## 01-075 | ByteFlow: Language Modeling through Adaptive Byte Compression without a Tokenizer
- arXiv: 2603.03583  first public: 2026-03-03  latest: 2026-03-03  primary cat: cs.CL
- authors (6): Chunyuan Deng; Sanket Lokegaonkar; Colin Lockard; Besnik Fetahu; Nasser Zalmout; Xian Li
- seed subtopic: 分词; type: 原始研究; cross: []
- arXiv comment: ICLR 2026
- pages: 22

ABSTRACT: Modern language models still rely on fixed, pre-defined subword tokenizations. Once a tokenizer is trained, the LM can only operate at this fixed level of granularity, which often leads to brittle and counterintuitive behaviors even in otherwise strong reasoning models. We introduce \textbf{ByteFlow Net}, a new hierarchical architecture that removes tokenizers entirely and instead enables models to learn their own segmentation of raw byte streams into semantically meaningful units. ByteFlow Net performs compression-driven segmentation based on the coding rate of latent representations, yielding adaptive boundaries \emph{while preserving a static computation graph via Top-$K$ selection}. Unlike prior self-tokenizing methods that depend on brittle heuristics with human-designed inductive biases, ByteFlow Net adapts its internal representation granularity to the input itself. Experiments demonstrate that this compression-based chunking strategy yields substantial performance gains, with ByteFlow Net outperforming both BPE-based Transformers and previous byte-level architectures. These results suggest that end-to-end, tokenizer-free modeling is not only feasible but also more effective, opening a path toward more adaptive and information-grounded language models.

## 01-076 | Revisiting the 16x Pretraining Compute Gap between Diffusion and Autoregressive Language Models
- arXiv: 2610.17590  first public: 2026-10-13  latest: 2026-10-13  primary cat: cs.LG
- authors (6): Guanghan Wang; Bing He; Zhan Shi; Benoit Dumoulin; Hanqing Lu; Volodymyr Kuleshov
- seed subtopic: 训练目标; type: 原始研究; cross: []
- arXiv comment: project page: https://guanghanwang.com/dlm-scaling
- pages: 35

ABSTRACT: Diffusion language models (DLMs) have attracted wide attention for their fast, parallel decoding, but they are believed to be far less efficient to train than autoregressive language models (ARMs): a widely cited study reports that a DLM needs roughly 16x the training compute of an ARM to match its likelihood, a figure that has made pretraining DLMs from scratch look prohibitive at scale. We find that the methodology behind this figure has fallen out of step with current DLM practice: it scores the model with its evidence lower bound (ELBO) and trains a full-sequence, decoder-only model. We therefore revisit the scaling laws of DLMs, adopting the exact likelihood under the model's own decoding order, block diffusion training, an encoder-decoder architecture, and a sweep over the block sizes used in practice. Under this new protocol, we study across ten model variants, about 1,700 models in total, and find that pretraining DLMs is far cheaper than previously thought. Concretely, scoring with the exact likelihood reduces the compute multiple to 12.8x; block diffusion training and an encoder-decoder architecture further reduce it to 7.8x at block size 32, and smaller block sizes narrow it to 4.6x at block size 8 and 3.0x at block size 4. We complement these scaling analyses with an empirical rule for the optimal decoder depth of encoder-decoder block diffusion, a held-out compute budget beyond the fitting range at which the gap between variants persists, and downstream benchmark results where likelihood improvements carry over to accuracy. Overall, the 16x figure substantially overstates the pretraining cost gap between DLMs and ARMs, and pretraining DLMs from scratch is far more viable than previously assumed.

## 01-077 | Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts
- arXiv: 2601.22156  first public: 2026-01-29  latest: 2026-01-29  primary cat: cs.CL
- authors (9): Yingfa Chen; Zhen Leng Thai; Zihan Zhou; Zhu Zhang; Xingyu Shen; Shuo Wang ...
- seed subtopic: 注意力; type: 原始研究; cross: []
- arXiv comment: 20 pages, 8 figures
- pages: 20

ABSTRACT: Hybrid Transformer architectures, which combine softmax attention blocks and recurrent neural networks (RNNs), have shown a desirable performance-throughput tradeoff for long-context modeling, but their adoption and studies are hindered by the prohibitive cost of large-scale pre-training from scratch. Some recent studies have shown that pre-trained softmax attention blocks can be converted into RNN blocks through parameter transfer and knowledge distillation. However, these transfer methods require substantial amounts of training data (more than 10B tokens), and the resulting hybrid models also exhibit poor long-context performance, which is the scenario where hybrid models enjoy significant inference speedups over Transformer-based models. In this paper, we present HALO (Hybrid Attention via Layer Optimization), a pipeline for distilling Transformer models into RNN-attention hybrid models. We then present HypeNet, a hybrid architecture with superior length generalization enabled by a novel position encoding scheme (named HyPE) and various architectural modifications. We convert the Qwen3 series into HypeNet using HALO, achieving performance comparable to the original Transformer models while enjoying superior long-context performance and efficiency. The conversion requires just 2.3B tokens, less than 0.01% of their pre-training data

## 01-079 | Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position
- arXiv: 2610.10114  first public: 2026-10-07  latest: 2026-10-07  primary cat: cs.CL
- authors (3): Xiaoran Liu; Ziwei He; Xipeng Qiu
- seed subtopic: 位置编码; type: 原始研究; cross: []
- arXiv comment: 60 pages, 36 figures, 25 tables, under review
- URLs on first pages of PDF: https://github.com/OpenMOSS/Hybrid-Mechanics
- pages: 60

ABSTRACT: The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we begin with hybrids of full attention and either sliding-window attention (SWA) or gated variants of linear attention (LA), represented by GLA and GDN. We first observe a Seesaw Effect in Context Extension: LA hybrids benefit more from long-context continual pretraining, whereas SWA hybrids perform better under length extrapolation. We attribute this behavior to differences in the positional inductive biases induced by these attention mechanisms. We find that SWA hybrids suffer from a Short-Context Learning Trap, Short-Window Weariness, and Long-Window Laziness, and require extended windows to enhance performance in continual long-context pretraining. For LA hybrids, we summarize the Matthew Effect of Hybrid Position Extrapolation and propose Sliding-Window Linear Attention, achieving 16$\times$ training-free length extrapolation while maintaining 100\% accuracy on NIAH-SK1 in 64k context length.

## 01-080 | RoPE is Dead, Long Live RoPE: Towards Scalable Data-aware Positional Encodings
- arXiv: 2609.34556  first public: 2026-09-28  latest: 2026-10-03  primary cat: cs.CL
- authors (6): Jarod Lévy; Mathurin Videau; Jad Yehya; Jean-Rémi King; Stéphane d'Ascoli; Thomas Moreau
- seed subtopic: 位置编码; type: 原始研究; cross: []
- pages: 25

ABSTRACT: Transformers process tokens without any inherent notion of order, making positional encoding a fundamental requirement rather than an architectural refinement. Rotary Position Embedding (RoPE) has become the default positional encoding in modern language models, yet it is heavily biased toward nearby tokens. Existing alternatives have been evaluated under different settings, leaving the literature fragmented and without a clear replacement. We bring structure to this landscape by examining a specific weakness of RoPE: its slow frequency bands, whose wavelengths exceed the training context and expose models to unseen angles during extrapolation. We therefore introduce Data aware RoPE (DaRoPE), which preserves standard RoPE on the fast bands but replaces absolute position on the slow bands with bounded coordinates learned from contextual representations. Therefore, the slow-band geometry depends on the data rather than only on positional distance. We compare representative encodings under matched conditions across synthetic tasks, symbolic music, genomics, neural signals, and language models spanning 124M to 50B parameters. Across these experiments, DaRoPE leads on non-text benchmarks, mitigates recency bias, while remaining best or on par in language modeling and length extrapolation. Moreover, the learned coordinates also make the mechanism interpretable, revealing how attention layers leverage contextual information beyond token distance. Together, these results support DaRoPE as the best overall default among the evaluated methods, when there is no domain-specific reasons to prefer another.

## 01-081 | Sliding-window beats linear attention
- arXiv: 2608.28444  first public: 2026-08-28  latest: 2026-10-04  primary cat: cs.CL
- authors (4): Alexia Jolicoeur-Martineau; Rhea Sanjay Sukthanker; Pashmina Cameron; Emy Gervais
- seed subtopic: 注意力; type: 原始研究; cross: ['11']
- pages: 16

ABSTRACT: Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy: every new token costs more than the previous one, and its keys and values must be stored in memory indefinitely, which is unsustainable. Two main lines of work address this: compressing the KV cache, e.g., by evicting or quantizing keys and values, and retrofitting LLMs to use Linear Attention, which replaces the KV cache with a fixed-size state. Retrofitting has attracted a lot of attention, given its promise to solve the quadratic scaling problem with state-of-the-art performance at low cost. However, it has not been properly compared to the simplest form of KV-cache eviction: Sliding Window Attention (SWA) with attention sinks. In this work, we show that SWA with sinks performs as well or better than most retrofitted Linear Attention models across multiple LLMs and downstream tasks, with the largest gains on long-context and generative tasks. On long-context reasoning tasks (Needle-in-a-Haystack and BABILong), SWA achieves massively higher performance (2 to 10 times higher than linear attention). SWA requires no additional training, is extremely fast, and requires little memory, making it an extremely cheap and reliable solution. When the training budget is limited, switching to SWA is a much more effective way to reduce inference memory cost than retrofitting linear attention. Linear attention models have shown promise, but they require training from scratch or extensive retrofitting to reap their architectural benefits and come close to SWA.
