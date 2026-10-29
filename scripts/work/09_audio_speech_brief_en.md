# Brief for annotation: 09 音频与语音大模型

## 09-052 | Qwen3-Omni Technical Report
- arXiv: 2509.17765  first public: 2025-09-22  latest: 2025-09-22  primary cat: cs.CL
- authors (38): Jin Xu; Zhifang Guo; Hangrui Hu; Yunfei Chu; Xiong Wang; Jinzheng He ...
- seed subtopic: 实时交互; type: 技术报告; cross: ['07']
- arXiv comment: https://github.com/QwenLM/Qwen3-Omni
- URLs on first pages of PDF: https://github.com/QwenLM/Qwen3-Omni https://huggingface.co/spaces/Qwen/Qwen3-Omni-Demo
- pages: 25

ABSTRACT: We present Qwen3-Omni, a single multimodal model that, for the first time, maintains state-of-the-art performance across text, image, audio, and video without any degradation relative to single-modal counterparts. Qwen3-Omni matches the performance of same-sized single-modal models within the Qwen series and excels particularly on audio tasks. Across 36 audio and audio-visual benchmarks, Qwen3-Omni achieves open-source SOTA on 32 benchmarks and overall SOTA on 22, outperforming strong closed-source models such as Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe. Qwen3-Omni adopts a Thinker-Talker MoE architecture that unifies perception and generation across text, images, audio, and video, yielding fluent text and natural real-time speech. It supports text interaction in 119 languages, speech understanding in 19 languages, and speech generation in 10 languages. To reduce first-packet latency in streaming synthesis, Talker autoregressively predicts discrete speech codecs using a multi-codebook scheme. Leveraging the representational capacity of these codebooks, we replace computationally intensive block-wise diffusion with a lightweight causal ConvNet, enabling streaming from the first codec frame. In cold-start settings, Qwen3-Omni achieves a theoretical end-to-end first-packet latency of 234 ms. To further strengthen multimodal reasoning, we introduce a Thinking model that explicitly reasons over inputs from any modality. Since the research community currently lacks a general-purpose audio captioning model, we fine-tuned Qwen3-Omni-30B-A3B to obtain Qwen3-Omni-30B-A3B-Captioner, which produces detailed, low-hallucination captions for arbitrary audio inputs. Qwen3-Omni-30B-A3B, Qwen3-Omni-30B-A3B-Thinking, and Qwen3-Omni-30B-A3B-Captioner are publicly released under the Apache 2.0 license.

## 09-053 | MMAudio: Taming Multimodal Joint Training for High-Quality Video-to-Audio Synthesis
- arXiv: 2412.15322  first public: 2024-12-19  latest: 2025-04-07  primary cat: cs.CV
- authors (6): Ho Kei Cheng; Masato Ishii; Akio Hayakawa; Takashi Shibuya; Alexander Schwing; Yuki Mitsufuji
- seed subtopic: 语音与音频生成; type: 原始研究; cross: ['08']
- arXiv comment: Accepted to CVPR 2025. Project page: https://hkchengrex.github.io/MMAudio
- pages: 22

ABSTRACT: We propose to synthesize high-quality and synchronized audio, given video and optional text conditions, using a novel multimodal joint training framework MMAudio. In contrast to single-modality training conditioned on (limited) video data only, MMAudio is jointly trained with larger-scale, readily available text-audio data to learn to generate semantically aligned high-quality audio samples. Additionally, we improve audio-visual synchrony with a conditional synchronization module that aligns video conditions with audio latents at the frame level. Trained with a flow matching objective, MMAudio achieves new video-to-audio state-of-the-art among public models in terms of audio quality, semantic alignment, and audio-visual synchronization, while having a low inference time (1.23s to generate an 8s clip) and just 157M parameters. MMAudio also achieves surprisingly competitive performance in text-to-audio generation, showing that joint training does not hinder single-modality performance. Code and demo are available at: https://hkchengrex.github.io/MMAudio

## 09-054 | Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning
- arXiv: 2602.11909  first public: 2026-02-12  latest: 2026-02-28  primary cat: cs.SD
- authors (10): Daiqing Wu; Xuan Zhang; Dongbao Yang; Jiashu Yao; Longfei Chen; Qingsong Liu ...
- seed subtopic: 音频语言模型; type: 原始研究; cross: ['04']
- arXiv comment: Accepted by ICLR 2026
- URLs on first pages of PDF: https://github.com/wdqqdw/Echo
- pages: 30

ABSTRACT: The maturation of Large Audio Language Models (LALMs) has raised growing expectations for them to comprehend complex audio much like humans. Current efforts primarily replicate text-based reasoning by contextualizing audio content through a one-time encoding, which introduces a critical information bottleneck. Drawing inspiration from human cognition, we propose audio-interleaved reasoning to break through this bottleneck. It treats audio as an active reasoning component, enabling sustained audio engagement and perception-grounded analysis. To instantiate it, we introduce a two-stage training framework, first teaching LALMs to localize salient audio segments through supervised fine-tuning, and then incentivizing proficient re-listening via reinforcement learning. In parallel, a structured data generation pipeline is developed to produce high-quality training data. Consequently, we present Echo, a LALM capable of dynamically re-listening to audio in demand during reasoning. On audio comprehension benchmarks, Echo achieves overall superiority in both challenging expert-level and general-purpose tasks. Comprehensive analysis further confirms the efficiency and generalizability of audio-interleaved reasoning, establishing it as a promising direction for advancing audio comprehension. Project page: https://github.com/wdqqdw/Echo.

## 09-055 | F-Actor: Controllable Conversational Behaviour in Full-Duplex Models
- arXiv: 2601.11329  first public: 2026-01-16  latest: 2026-04-15  primary cat: cs.CL
- authors (6): Maike Züfle; Ondrej Klejch; Nicholas Sanders; Jan Niehues; Alexandra Birch; Tsz Kin Lam
- seed subtopic: 实时交互; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/MaikeZuefle/f-actor
- pages: 18

ABSTRACT: Spoken conversational systems require more than accurate speech generation to have human-like conversations: to feel natural and engaging, they must produce conversational behaviour that adapts dynamically to the context. Current spoken conversational systems, however, rarely allow such customization, limiting their naturalness and usability. In this work, we present the first open, instruction-following full-duplex conversational speech model that can be trained efficiently under typical academic resource constraints. By keeping the audio encoder frozen and finetuning only the language model, our model requires just 2,000 hours of data, without relying on large-scale pretraining or multi-stage optimization. The model can follow explicit instructions to control speaker voice, conversation topic, conversational behaviour (e.g., backchanneling and interruptions), and dialogue initiation. We propose a single-stage training protocol and systematically analyze design choices. Both the model and training code is released to enable reproducible research on controllable full-duplex speech systems.

## 09-056 | Fish Audio S2 Technical Report
- arXiv: 2603.08823  first public: 2026-03-09  latest: 2026-03-11  primary cat: cs.SD
- authors (14): Shijia Liao; Yuxuan Wang; Songting Liu; Yifan Cheng; Ruoyi Zhang; Tianyu Li ...
- seed subtopic: 语音与音频生成; type: 技术报告; cross: []
- URLs on first pages of PDF: https://github.com/fishaudio/fish-speech https://huggingface.co/fishaudio/s2-pro
- pages: 19

ABSTRACT: We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-based inference engine. The inference engine is production-ready for streaming, achieving an RTF of 0.195 and a time-to-first-audio below 100 ms.Our code and weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face (https://huggingface.co/fishaudio/s2-pro). We highly encourage readers to visit https://fish.audio to try custom voices.
