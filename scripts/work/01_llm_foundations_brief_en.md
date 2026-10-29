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
