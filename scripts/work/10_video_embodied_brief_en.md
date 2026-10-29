# Brief for annotation: 10 视频理解与具身多模态

## 10-051 | Navigation World Models
- arXiv: 2412.03572  first public: 2024-12-04  latest: 2025-04-11  primary cat: cs.CV
- authors (5): Amir Bar; Gaoyue Zhou; Danny Tran; Trevor Darrell; Yann LeCun
- seed subtopic: 世界模型; type: 原始研究; cross: []
- arXiv comment: CVPR 2025. Project page: https://www.amirbar.net/nwm/
- pages: 17

ABSTRACT: Navigation is a fundamental skill of agents with visual-motor capabilities. We introduce a Navigation World Model (NWM), a controllable video generation model that predicts future visual observations based on past observations and navigation actions. To capture complex environment dynamics, NWM employs a Conditional Diffusion Transformer (CDiT), trained on a diverse collection of egocentric videos of both human and robotic agents, and scaled up to 1 billion parameters. In familiar environments, NWM can plan navigation trajectories by simulating them and evaluating whether they achieve the desired goal. Unlike supervised navigation policies with fixed behavior, NWM can dynamically incorporate constraints during planning. Experiments demonstrate its effectiveness in planning trajectories from scratch or by ranking trajectories sampled from an external policy. Furthermore, NWM leverages its learned visual priors to imagine trajectories in unfamiliar environments from a single input image, making it a flexible and powerful tool for next-generation navigation systems.

## 10-049 | Diffusion for World Modeling: Visual Details Matter in Atari
- arXiv: 2405.12399  first public: 2024-05-20  latest: 2024-10-30  primary cat: cs.LG
- authors (7): Eloi Alonso; Adam Jelley; Vincent Micheli; Anssi Kanervisto; Amos Storkey; Tim Pearce ...
- seed subtopic: 世界模型; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024 (Spotlight)
- pages: 28

ABSTRACT: World models constitute a promising approach for training reinforcement learning agents in a safe and sample-efficient manner. Recent world models predominantly operate on sequences of discrete latent variables to model environment dynamics. However, this compression into a compact discrete representation may ignore visual details that are important for reinforcement learning. Concurrently, diffusion models have become a dominant approach for image generation, challenging well-established methods modeling discrete latents. Motivated by this paradigm shift, we introduce DIAMOND (DIffusion As a Model Of eNvironment Dreams), a reinforcement learning agent trained in a diffusion world model. We analyze the key design choices that are required to make diffusion suitable for world modeling, and demonstrate how improved visual details can lead to improved agent performance. DIAMOND achieves a mean human normalized score of 1.46 on the competitive Atari 100k benchmark; a new best for agents trained entirely within a world model. We further demonstrate that DIAMOND's diffusion world model can stand alone as an interactive neural game engine by training on static Counter-Strike: Global Offensive gameplay. To foster future research on diffusion for world modeling, we release our code, agents, videos and playable world models at https://diamond-wm.github.io.

## 10-053 | Latent Action Pretraining from Videos
- arXiv: 2410.11758  first public: 2024-10-15  latest: 2025-05-15  primary cat: cs.RO
- authors (16): Seonghyeon Ye; Joel Jang; Byeongguk Jeon; Sejune Joo; Jianwei Yang; Baolin Peng ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: ICLR 2025 Website: https://latentactionpretraining.github.io
- pages: 27

ABSTRACT: We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model.

## 10-061 | SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- arXiv: 2509.09674  first public: 2025-09-11  latest: 2025-09-11  primary cat: cs.RO
- authors (21): Haozhan Li; Yuxin Zuo; Jiale Yu; Yuhao Zhang; Zhaohui Yang; Kaiyan Zhang ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/volcengine/verl
- pages: 24

ABSTRACT: Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 10-079 | LLaVAction: evaluating and training multi-modal large language models for action understanding
- arXiv: 2503.18712  first public: 2025-03-24  latest: 2026-01-12  primary cat: cs.CV
- authors (4): Haozhe Qi; Shaokai Ye; Alexander Mathis; Mackenzie W. Mathis
- seed subtopic: 动作理解; type: 原始研究; cross: []
- arXiv comment: https://github.com/AdaptiveMotorControlLab/LLaVAction
- journal_ref: International Conference on Learning Representations (ICLR) 2026
- URLs on first pages of PDF: https://github.com/AdaptiveMotorControlLab/LLaV
- pages: 25

ABSTRACT: Understanding human behavior requires measuring behavioral actions. Due to its complexity, behavior is best mapped onto a rich, semantic structure such as language. Emerging multimodal large language models (MLLMs) are promising candidates, but their fine-grained action understanding ability has not been fully examined. In this work, we reformulate EPIC-KITCHENS-100, one of the largest and most challenging egocentric action recognition datasets, into a MLLM benchmark (EPIC-KITCHENS-100-MQA). We demonstrate that when we sample difficult answers based on specialist models as distractors, leading MLLMs struggle to recognize the correct actions. How can we increase the performance of MLLMs? We curated a supervised finetuning dataset that includes `hard' action recognition, temporal detection, captioning, and free-form question answering to improve models' diverse action understanding capabilities. We introduce a new model called LLaVAction that adds an action token to boost models' attention on visual tokens and a two-stage pipeline to obtain structured actions. LLaVAction greatly improves the MLLMs' ability of action understanding, achieving strong improvements on both MLLM benchmarks (21 points in accuracy over GPT-4o on EPIC-KITCHENS-100-MQA) and established action recognition benchmarks, suggesting that our methods prepare MLLMs to be a promising path forward for complex action tasks. Code, data, the benchmark, and models are available at https://github.com/AdaptiveMotorControlLab/LLaVAction.

## 10-001 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- arXiv: 2307.15818  first public: 2023-07-28  latest: 2023-07-28  primary cat: cs.RO
- authors (54): Anthony Brohan; Noah Brown; Justice Carbajal; Yevgen Chebotar; Xi Chen; Krzysztof Choromanski ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Website: https://robotics-transformer.github.io/
- pages: 26

ABSTRACT: We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## 10-002 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- arXiv: 2310.08864  first public: 2023-10-13  latest: 2025-05-14  primary cat: cs.RO
- authors (294): Open X-Embodiment Collaboration; Abby O'Neill; Abdul Rehman; Abhinav Gupta; Abhiram Maddukuri; Abhishek Gupta ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: Project website: https://robotics-transformer-x.github.io
- pages: 12

ABSTRACT: Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 10-003 | PaLM-E: An Embodied Multimodal Language Model
- arXiv: 2303.03378  first public: 2023-03-06  latest: 2023-03-06  primary cat: cs.LG
- authors (22): Danny Driess; Fei Xia; Mehdi S. M. Sajjadi; Corey Lynch; Aakanksha Chowdhery; Brian Ichter ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- pages: 18

ABSTRACT: Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains. Our largest model, PaLM-E-562B with 562B parameters, in addition to being trained on robotics tasks, is a visual-language generalist with state-of-the-art performance on OK-VQA, and retains generalist language capabilities with increasing scale.

## 10-007 | MVBench: A Comprehensive Multi-modal Video Understanding Benchmark
- arXiv: 2311.17005  first public: 2023-11-28  latest: 2024-05-23  primary cat: cs.CV
- authors (12): Kunchang Li; Yali Wang; Yinan He; Yizhuo Li; Yi Wang; Yi Liu ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: CVPR 2024 highlight: updated version with Mistral and better performances for MVBench/NExT-QA/STAR/TVQA/EgoSchema/IntentQA
- pages: 19

ABSTRACT: With the rapid development of Multi-modal Large Language Models (MLLMs), a number of diagnostic benchmarks have recently emerged to evaluate the comprehension capabilities of these models. However, most benchmarks predominantly assess spatial understanding in the static image tasks, while overlooking temporal understanding in the dynamic video tasks. To alleviate this issue, we introduce a comprehensive Multi-modal Video understanding Benchmark, namely MVBench, which covers 20 challenging video tasks that cannot be effectively solved with a single frame. Specifically, we first introduce a novel static-to-dynamic method to define these temporal-related tasks. By transforming various static tasks into dynamic ones, we enable the systematic generation of video tasks that require a broad spectrum of temporal skills, ranging from perception to cognition. Then, guided by the task definition, we automatically convert public video annotations into multiple-choice QA to evaluate each task. On one hand, such a distinct paradigm allows us to build MVBench efficiently, without much manual intervention. On the other hand, it guarantees evaluation fairness with ground-truth video annotations, avoiding the biased scoring of LLMs. Moreover, we further develop a robust video MLLM baseline, i.e., VideoChat2, by progressive multi-modal training with diverse instruction-tuning data. The extensive results on our MVBench reveal that, the existing MLLMs are far from satisfactory in temporal understanding, while our VideoChat2 largely surpasses these leading models by over 15% on MVBench. All models and data are available at https://github.com/OpenGVLab/Ask-Anything.

## 10-008 | Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis
- arXiv: 2405.21075  first public: 2024-05-31  latest: 2025-05-30  primary cat: cs.CV
- authors (21): Chaoyou Fu; Yuhan Dai; Yongdong Luo; Lei Li; Shuhuai Ren; Renrui Zhang ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: Project Page: https://video-mme.github.io
- pages: 13

ABSTRACT: In the quest for artificial general intelligence, Multi-modal Large Language Models (MLLMs) have emerged as a focal point in recent advancements. However, the predominant focus remains on developing their capabilities in static image understanding. The potential of MLLMs in processing sequential visual data is still insufficiently explored, highlighting the absence of a comprehensive, high-quality assessment of their performance. In this paper, we introduce Video-MME, the first-ever full-spectrum, Multi-Modal Evaluation benchmark of MLLMs in Video analysis. Our work distinguishes from existing benchmarks through four key features: 1) Diversity in video types, spanning 6 primary visual domains with 30 subfields to ensure broad scenario generalizability; 2) Duration in temporal dimension, encompassing both short-, medium-, and long-term videos, ranging from 11 seconds to 1 hour, for robust contextual dynamics; 3) Breadth in data modalities, integrating multi-modal inputs besides video frames, including subtitles and audios, to unveil the all-round capabilities of MLLMs; 4) Quality in annotations, utilizing rigorous manual labeling by expert annotators to facilitate precise and reliable model assessment. 900 videos with a total of 254 hours are manually selected and annotated by repeatedly viewing all the video content, resulting in 2,700 question-answer pairs. With Video-MME, we extensively evaluate various state-of-the-art MLLMs, including GPT-4 series and Gemini 1.5 Pro, as well as open-source image models like InternVL-Chat-V1.5 and video models like LLaVA-NeXT-Video. Our experiments reveal that Gemini 1.5 Pro is the best-performing commercial model, significantly outperforming the open-source models. Our dataset along with these findings underscores the need for further improvements in handling longer sequences and multi-modal data. Project Page: https://video-mme.github.io

## 10-015 | Apollo: An Exploration of Video Understanding in Large Multimodal Models
- arXiv: 2412.10360  first public: 2024-12-13  latest: 2024-12-13  primary cat: cs.CV
- authors (12): Orr Zohar; Xiaohan Wang; Yann Dubois; Nikhil Mehta; Tong Xiao; Philippe Hansen-Estruch ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: https://apollo-lmms.github.io
- pages: 33

ABSTRACT: Despite the rapid integration of video perception capabilities into Large Multimodal Models (LMMs), the underlying mechanisms driving their video understanding remain poorly understood. Consequently, many design decisions in this domain are made without proper justification or analysis. The high computational cost of training and evaluating such models, coupled with limited open research, hinders the development of video-LMMs. To address this, we present a comprehensive study that helps uncover what effectively drives video understanding in LMMs. We begin by critically examining the primary contributors to the high computational requirements associated with video-LMM research and discover Scaling Consistency, wherein design and training decisions made on smaller models and datasets (up to a critical size) effectively transfer to larger models. Leveraging these insights, we explored many video-specific aspects of video-LMMs, including video sampling, architectures, data composition, training schedules, and more. For example, we demonstrated that fps sampling during training is vastly preferable to uniform frame sampling and which vision encoders are the best for video representation. Guided by these findings, we introduce Apollo, a state-of-the-art family of LMMs that achieve superior performance across different model sizes. Our models can perceive hour-long videos efficiently, with Apollo-3B outperforming most existing $7$B models with an impressive 55.1 on LongVideoBench. Apollo-7B is state-of-the-art compared to 7B LMMs with a 70.9 on MLVU, and 63.3 on Video-MME.

## 10-021 | Revisiting Feature Prediction for Learning Visual Representations from Video
- arXiv: 2404.08471  first public: 2024-02-15  latest: 2024-02-15  primary cat: cs.CV
- authors (8): Adrien Bardes; Quentin Garrido; Jean Ponce; Xinlei Chen; Michael Rabbat; Yann LeCun ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/facebookresearch/jepa
- pages: 23

ABSTRACT: This paper explores feature prediction as a stand-alone objective for unsupervised learning from video and introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective, without the use of pretrained image encoders, text, negative examples, reconstruction, or other sources of supervision. The models are trained on 2 million videos collected from public datasets and are evaluated on downstream image and video tasks. Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model's parameters; e.g., using a frozen backbone. Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K.

## 10-022 | V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning
- arXiv: 2506.09985  first public: 2025-06-11  latest: 2025-06-11  primary cat: cs.AI
- authors (30): Mido Assran; Adrien Bardes; David Fan; Quentin Garrido; Russell Howes; Mojtaba ...
- seed subtopic: 世界模型; type: 原始研究; cross: []
- arXiv comment: 48 pages, 19 figures
- URLs on first pages of PDF: https://github.com/facebookresearch/vjepa2
- pages: 48

ABSTRACT: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass). Finally, we show how self-supervised learning can be applied to robotic planning tasks by post-training a latent action-conditioned world model, V-JEPA 2-AC, using less than 62 hours of unlabeled robot videos from the Droid dataset. We deploy V-JEPA 2-AC zero-shot on Franka arms in two different labs and enable picking and placing of objects using planning with image goals. Notably, this is achieved without collecting any data from the robots in these environments, and without any task-specific training or reward. This work demonstrates how self-supervised learning from web-scale data and a small amount of robot interaction data can yield a world model capable of planning in the physical world.

## 10-024 | Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces
- arXiv: 2412.14171  first public: 2024-12-18  latest: 2025-07-02  primary cat: cs.CV
- authors (6): Jihan Yang; Shusheng Yang; Anjali W. Gupta; Rilyn Han; Li Fei-Fei; Saining Xie
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: Project page: https://vision-x-nyu.github.io/thinking-in-space.github.io/
- pages: 28

ABSTRACT: Humans possess the visual-spatial intelligence to remember spaces from sequential visual observations. However, can Multimodal Large Language Models (MLLMs) trained on million-scale video datasets also ``think in space'' from videos? We present a novel video-based visual-spatial intelligence benchmark (VSI-Bench) of over 5,000 question-answer pairs, and find that MLLMs exhibit competitive - though subhuman - visual-spatial intelligence. We probe models to express how they think in space both linguistically and visually and find that while spatial reasoning capabilities remain the primary bottleneck for MLLMs to reach higher benchmark performance, local world models and spatial awareness do emerge within these models. Notably, prevailing linguistic reasoning techniques (e.g., chain-of-thought, self-consistency, tree-of-thoughts) fail to improve performance, whereas explicitly generating cognitive maps during question-answering enhances MLLMs' spatial distance ability.

## 10-025 | Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives
- arXiv: 2311.18259  first public: 2023-11-30  latest: 2024-09-25  primary cat: cs.CV
- authors (101): Kristen Grauman; Andrew Westbury; Lorenzo Torresani; Kris Kitani; Jitendra Malik; Triantafyllos Afouras ...
- seed subtopic: 动作理解; type: 原始研究; cross: []
- arXiv comment: Expanded manuscript (compared to arxiv v1 from Nov 2023 and CVPR 2024 paper from June 2024) for more comprehensive dataset and benchmark presentation, plus new results on v2 data release
- pages: 99

ABSTRACT: We present Ego-Exo4D, a diverse, large-scale multimodal multiview video dataset and benchmark challenge. Ego-Exo4D centers around simultaneously-captured egocentric and exocentric video of skilled human activities (e.g., sports, music, dance, bike repair). 740 participants from 13 cities worldwide performed these activities in 123 different natural scene contexts, yielding long-form captures from 1 to 42 minutes each and 1,286 hours of video combined. The multimodal nature of the dataset is unprecedented: the video is accompanied by multichannel audio, eye gaze, 3D point clouds, camera poses, IMU, and multiple paired language descriptions -- including a novel "expert commentary" done by coaches and teachers and tailored to the skilled-activity domain. To push the frontier of first-person video understanding of skilled human activity, we also present a suite of benchmark tasks and their annotations, including fine-grained activity understanding, proficiency estimation, cross-view translation, and 3D hand/body pose. All resources are open sourced to fuel new research in the community. Project page: http://ego-exo4d-data.org/

## 10-027 | OpenVLA: An Open-Source Vision-Language-Action Model
- arXiv: 2406.09246  first public: 2024-06-13  latest: 2024-09-05  primary cat: cs.RO
- authors (18): Moo Jin Kim; Karl Pertsch; Siddharth Karamcheti; Ted Xiao; Ashwin Balakrishna; Suraj Nair ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Website: https://openvla.github.io/
- pages: 37

ABSTRACT: Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks, a key component for adoption. Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters. We further show that we can effectively fine-tune OpenVLA for new settings, with especially strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, and outperform expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%. We also explore compute efficiency; as a separate contribution, we show that OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate. Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.

## 10-028 | $π_0$: A Vision-Language-Action Flow Model for General Robot Control
- arXiv: 2410.24164  first public: 2024-10-31  latest: 2026-01-08  primary cat: cs.LG
- authors (24): Kevin Black; Noah Brown; Danny Driess; Adnan Esmail; Michael Equi; Chelsea Finn ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: See project website for videos: https://physicalintelligence.company/blog/pi0 Published in RSS 2025
- pages: 17

ABSTRACT: Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot policies (i.e., robot foundation models) can address these challenges, and how we can design effective generalist robot policies for complex and highly dexterous tasks. We propose a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. We then discuss how this model can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators. We evaluate our model in terms of its ability to perform tasks in zero shot after pre-training, follow language instructions from people and from a high-level VLM policy, and its ability to acquire new skills via fine-tuning. Our results cover a wide variety of tasks, such as laundry folding, table cleaning, and assembling boxes.

## 10-029 | $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization
- arXiv: 2504.16054  first public: 2025-04-22  latest: 2025-04-22  primary cat: cs.LG
- authors (36): Physical Intelligence; Kevin Black; Noah Brown; James Darpinian; Karan Dhabalia; Danny Driess ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- pages: 19

ABSTRACT: In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 10-032 | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
- arXiv: 2503.14734  first public: 2025-03-18  latest: 2025-03-27  primary cat: cs.RO
- authors (43): NVIDIA; :; Johan Bjorck; Fernando Castañeda; Nikita Cherniadev; Xingye Da ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Authors are listed alphabetically. Project leads are Linxi "Jim" Fan and Yuke Zhu. For more information, see https://developer.nvidia.com/isaac/gr00t
- pages: 36

ABSTRACT: General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks. To this end, we introduce GR00T N1, an open foundation model for humanoid robots. GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end. We train GR00T N1 with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets. We show that our generalist robot model GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments. Furthermore, we deploy our model on the Fourier GR-1 humanoid robot for language-conditioned bimanual manipulation tasks, achieving strong performance with high data efficiency.

## 10-033 | Gemini Robotics: Bringing AI into the Physical World
- arXiv: 2503.20020  first public: 2025-03-25  latest: 2025-03-25  primary cat: cs.RO
- authors (118): Gemini Robotics Team; Saminda Abeyruwan; Joshua Ainslie; Jean-Baptiste Alayrac; Montserrat Gonzalez Arenas; Travis Armstrong ...
- seed subtopic: 视觉语言动作模型; type: 技术报告; cross: []
- pages: 64

ABSTRACT: Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## 10-047 | Genie: Generative Interactive Environments
- arXiv: 2402.15391  first public: 2024-02-23  latest: 2024-02-23  primary cat: cs.LG
- authors (25): Jake Bruce; Michael Dennis; Ashley Edwards; Jack Parker-Holder; Yuge Shi; Edward Hughes ...
- seed subtopic: 世界模型; type: 原始研究; cross: ['08']
- arXiv comment: https://sites.google.com/corp/view/genie-2024/
- pages: 27

ABSTRACT: We introduce Genie, the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches. At 11B parameters, Genie can be considered a foundation world model. It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model. Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain-specific requirements typically found in the world model literature. Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.

## 10-048 | Cosmos World Foundation Model Platform for Physical AI
- arXiv: 2501.03575  first public: 2025-01-07  latest: 2025-07-09  primary cat: cs.CV
- authors (79): NVIDIA; :; Niket Agarwal; Arslan Ali; Maciej Bala; Yogesh Balaji ...
- seed subtopic: 世界模型; type: 技术报告; cross: ['08']
- pages: 75

ABSTRACT: Physical AI needs to be trained digitally first. It needs a digital twin of itself, the policy model, and a digital twin of the world, the world model. In this paper, we present the Cosmos World Foundation Model Platform to help developers build customized world models for their Physical AI setups. We position a world foundation model as a general-purpose world model that can be fine-tuned into customized world models for downstream applications. Our platform covers a video curation pipeline, pre-trained world foundation models, examples of post-training of pre-trained world foundation models, and video tokenizers. To help Physical AI builders solve the most critical problems of our society, we make Cosmos open-source and our models open-weight with permissive licenses available via https://github.com/nvidia-cosmos/cosmos-predict1.

## 10-072 | Green-VLA: Staged Vision-Language-Action Model for Generalist Robots
- arXiv: 2602.00919  first public: 2026-01-31  latest: 2026-03-07  primary cat: cs.RO
- authors (28): I. Apanasevich; M. Artemyev; R. Babakyan; P. Fedotova; D. Grankin; E. Kupryashin ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: 22 pages, 14 figures
- URLs on first pages of PDF: https://github.com/greenvla/GreenVLA
- pages: 22

ABSTRACT: We introduce Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments. Green-VLA follows a five stage curriculum: (L0) foundational VLMs, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning (RL) policy alignment. We couple a scalable data-processing pipeline (3,000 hours of demonstrations) with temporal alignment and quality filtering, and use a unified, embodiment-aware action interface enabling a single policy to control humanoids, mobile manipulators, and fixed-base arms. At inference, the VLA controller is enhanced with episode-progress prediction, out-of-distribution detection, and joint-prediction-based guidance to improve safety and precise target selection. Experiments on Simpler BRIDGE WidowX and CALVIN ABC-D, as well as real-robot evaluations, show strong generalization and performance gains from RL alignment in success rate, robustness, and long-horizon efficiency.

## 10-073 | InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation
- arXiv: 2601.02456  first public: 2026-01-05  latest: 2026-02-13  primary cat: cs.RO
- authors (42): Junhao Cai; Zetao Cai; Jiafei Cao; Yilun Chen; Zeyu He; Lei Jiang ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Homepage: https://internrobotics.github.io/internvla-a1.github.io/
- pages: 25

ABSTRACT: Prevalent Vision-Language-Action (VLA) models are typically built upon Multimodal Large Language Models (MLLMs) and demonstrate exceptional proficiency in semantic understanding, but they inherently lack the capability to deduce physical world dynamics. Consequently, recent approaches have shifted toward World Models, typically formulated via video prediction; however, these methods often suffer from a lack of semantic grounding and exhibit brittleness in the presence of video prediction errors. To synergize semantic understanding with dynamic predictive capabilities, we present InternVLA-A1. This model employs a unified Mixture-of-Transformers architecture, coordinating three experts for scene understanding, visual foresight generation, and action execution. These components interact seamlessly through a unified masked self attention mechanism. Building upon InternVL3 and Qwen3-VL, we instantiate InternVLA-A1 at 2B and 3B parameter scales. We pre-train these models on heterogeneous data sources over real-world robot data, synthetic simulation data, and human videos, covering over 692M frames. This hybrid training strategy effectively harnesses the diversity of synthetic simulation data while minimizing the sim-to-real gap. We evaluated InternVLA-A1 on 12 real-world robotic tasks and a simulation benchmark. The results show that InternVLA-A1 consistently outperforms prior leading models: compared with pi0.5, it achieves +4.4\% on static manipulation tasks and +2.6\% on the RoboTwin 2.0 simulation benchmark, and delivers a +26.7\% boost on dynamic manipulation tasks.

## 10-074 | Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism
- arXiv: 2603.29252  first public: 2026-03-31  latest: 2026-03-31  primary cat: cs.CV
- authors (8): Tao Chen; Kun Zhang; Qiong Wu; Xiao Chen; Chao Chang; Xiaoshuai Sun ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: CVPR 2026
- pages: 12

ABSTRACT: Long video understanding is a key challenge that plagues the advancement of \emph{Multimodal Large language Models} (MLLMs). In this paper, we study this problem from the perspective of visual memory mechanism, and proposed a novel and training-free approach, termed \emph{Flexible Memory} (\textbf{FlexMem}). In principle, FlexMem aims to mimic human behavior of video watching, \emph{i.e.}, continually watching video content and recalling the most relevant memory fragments to answer the question. In this way, FlexMem can help MLLMs achieve video understanding of infinite lengths, unlike previous methods that process all video information at once and have input upper-limit. Concretely, FlexMem first consider the visual KV caches as the memory sources, and realize the effective memory transfer and writing via a dual-pathway compression design. Afterwards, FlexMem also explores different memory reading strategies for the diverse video understanding tasks, including the popular streaming one. To validate FlexMem, we apply it to two popular video-MLLMs, and conduct extensive experiments on five long video and one streaming video task. The experimental results show that on \textbf{a single 3090 GPU}, our FlexMem can achieve obvious improvements than existing efficient video understanding methods and process more than \textbf{1k frames}, which also helps the base MLLMs achieve comparable or even better performance than SOTA MLLMs on some benchmarks, \emph{e.g.} , GPT-4o and Gemini-1.5 Pro.

## 10-075 | RoboJEPA: Scaling Robotic Latent World Models
- arXiv: 2610.10515  first public: 2026-10-07  latest: 2026-10-07  primary cat: cs.AI
- authors (12): Artem Zholus; Nicolas Beltran-Velez; Jianhao Yuan; Sarath Chandar; Tushar Nagarajan; Daniel Severo ...
- seed subtopic: 世界模型; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/facebookresearch/robo_jepa
- pages: 73

ABSTRACT: Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring long-horizon planning on real hardware. We release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

## 10-076 | Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?
- arXiv: 2610.09170  first public: 2026-10-06  latest: 2026-10-06  primary cat: cs.RO
- authors (5): Haoran Chen; Jingtian Ji; Samuel Wheeler; Kaylene Caswell Stocking; Matthew Walter
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- pages: 62

ABSTRACT: Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space. Many action tokenizers learn the mapping between tokens and actions via a reconstruction objective. However, as we show through extensive analysis, sufficiently accurate action reconstruction is only one part of what makes a downstream robot policy successful. It is also critical that the policy is able to predict the right tokens for new observations, and that unseen policy token predictions still decode into reasonable actions. These properties are downstream of tokenizer training and are not directly incentivized by a reconstruction objective alone. In this work, we introduce Predictable and Robust Action Tokenization (ProAct), a tokenizer training method that strategically augments reconstruction with the goal of improving downstream predictability and robustness. ProAct is policy-agnostic and uses only action datasets for training. Across the Robomimic, LIBERO, and RoboTwin benchmarks and a diverse set of tokenizer architectures, ProAct improves rollout success by an average of 11.3 percentage points. These improvements also translate to vision-language-action policies and real-world robotic manipulation, yielding average gains of 21.8 and 36.7 percentage points, respectively. These results suggest that effective action tokenization should be designed as a policy interface that balances fidelity, predictability, and robustness, rather than as a reconstruction problem alone.

## 10-077 | Turning Video Models into Generalist Robot Policies
- arXiv: 2605.27817  first public: 2026-05-27  latest: 2026-05-27  primary cat: cs.RO
- authors (7): Sizhe Lester Li; Evan Kim; Xingjian Bai; Tong Zhao; Tao Pang; Max Simchowitz ...
- seed subtopic: 世界模型; type: 原始研究; cross: ['08']
- arXiv comment: project page: https://vera.csail.mit.edu
- pages: 20

ABSTRACT: Video generative models have emerged as a promising robotics backbone, capable of generating videos that depict the completion of complex tasks across embodiments and environments. Recent work proposes robot foundation models that jointly predict future observations and actions by finetuning video models with action-labeled data. In this paper, we test the limits of an alternative approach: leave the video planner as-is while training an embodiment-specific inverse dynamics model (IDM). This decoupling offers several natural benefits: the video planner remains embodiment-agnostic, different video models can be interchanged easily without re-training the IDM, and the IDM can be independently trained with readily available self-play data. We present a closed-loop, video-to-action policy that combines an action-free video world model with a carefully-designed IDM based on the robot embodiment Jacobian. We demonstrate that our IDM design is both data-efficient and scalable to high-dimensional action spaces. Our policy, which we coin the Video-to-Embodied Robot Action Model (VERA), achieves strong performance across simulated and real-world benchmarks, including zero-shot Panda arm manipulation and 16-DoF Allegro-hand dexterous cube re-orientation. The same video planner can be used across multiple embodiments by pairing it with different embodiment-specific IDMs. Our results show that decoupled video planning plus faithful video-to-action translation is a viable alternative route towards zero-shot, cross-embodiment, and generalizable robot control. More results are available on our project website: https://vera.csail.mit.edu.

## 10-078 | World Model for Robot Learning: A Comprehensive Survey
- arXiv: 2605.00080  first public: 2026-04-30  latest: 2026-04-30  primary cat: cs.RO
- authors (18): Bohan Hou; Gen Li; Jindou Jia; Tuo An; Xinying Guo; Sicong Leng ...
- seed subtopic: 世界模型; type: 综述; cross: []
- arXiv comment: 43 pages, 6 figures
- URLs on first pages of PDF: https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy https://ntumars.github.io/wm-robot-survey/
- pages: 43

ABSTRACT: World models, which are predictive representations of how environments evolve under actions, have become a central component of robot learning. They support policy learning, planning, simulation, evaluation, data generation, and have advanced rapidly with the rise of foundation models and large-scale video generation. However, the literature remains fragmented across architectures, functional roles, and embodied application domains. To address this gap, we present a comprehensive review of world models from a robot-learning perspective. We examine how world models are coupled with robot policies, how they serve as learned simulators for reinforcement learning and evaluation, and how robotic video world models have progressed from imagination-based generation to controllable, structured, and foundation-scale formulations. We further connect these ideas to navigation and autonomous driving, and summarize representative datasets, benchmarks, and evaluation protocols. Overall, this survey systematically reviews the rapidly growing literature on world models for robot learning, clarifies key paradigms and applications, and highlights major challenges and future directions for predictive modeling in embodied agents. To facilitate continued access to newly emerging works, benchmarks, and resources, we will maintain and regularly update the accompanying GitHub repository alongside this survey.

## 10-080 | HD-EPIC: A Highly-Detailed Egocentric Video Dataset
- arXiv: 2502.04144  first public: 2025-02-06  latest: 2025-03-25  primary cat: cs.CV
- authors (19): Toby Perrett; Ahmad Darkhalil; Saptarshi Sinha; Omar Emara; Sam Pollard; Kranti Parida ...
- seed subtopic: 动作理解; type: 原始研究; cross: []
- arXiv comment: Accepted at CVPR 2025. Project Webpage and Dataset: http://hd-epic.github.io
- pages: 29

ABSTRACT: We present a validation dataset of newly-collected kitchen-based egocentric videos, manually annotated with highly detailed and interconnected ground-truth labels covering: recipe steps, fine-grained actions, ingredients with nutritional values, moving objects, and audio annotations. Importantly, all annotations are grounded in 3D through digital twinning of the scene, fixtures, object locations, and primed with gaze. Footage is collected from unscripted recordings in diverse home environments, making HDEPIC the first dataset collected in-the-wild but with detailed annotations matching those in controlled lab environments. We show the potential of our highly-detailed annotations through a challenging VQA benchmark of 26K questions assessing the capability to recognise recipes, ingredients, nutrition, fine-grained actions, 3D perception, object motion, and gaze direction. The powerful long-context Gemini Pro only achieves 38.5% on this benchmark, showcasing its difficulty and highlighting shortcomings in current VLMs. We additionally assess action recognition, sound recognition, and long-term video-object segmentation on HD-EPIC. HD-EPIC is 41 hours of video in 9 kitchens with digital twins of 413 kitchen fixtures, capturing 69 recipes, 59K fine-grained actions, 51K audio events, 20K object movements and 37K object masks lifted to 3D. On average, we have 263 annotations per minute of our unscripted videos.

## 10-081 | EgoIntent: A Pre-Outcome Micro-Step Benchmark for Understanding What, Why, and Next
- arXiv: 2603.12147  first public: 2026-03-12  latest: 2026-08-03  primary cat: cs.CV
- authors (11): Ye Pan; Chi Kit Wong; Yuanhuiyi Lyu; Hanqian Li; Chenfei Liao; Jiahao Huo ...
- seed subtopic: 动作理解; type: 原始研究; cross: []
- pages: 47

ABSTRACT: Egocentric video provides a natural modality for studying human behavior, but conventional visual understanding captures mainly observable scenes, objects, and actions rather than the latent goals that organize them. Existing intent benchmarks typically focus on coarse event-level goals and overlook how intent evolves across procedural steps. We introduce EgoIntent, a step-level intent-understanding benchmark comprising 3,014 pre-outcome micro-steps from 32 egocentric videos across 15 indoor and outdoor daily-life scenarios. Each step is manually annotated along three complementary dimensions: Local Intent (What), the immediate goal; Procedural Intent (Why), the role of the step in the broader procedure; and Next-Plan (Next), the action most likely to follow. Multiple rounds of human review refine temporal boundaries and annotation quality. We evaluate 15 multimodal large language models using reference-based scores and complementary reference-free diagnostics. Controlled studies on four representative models show that only one model gains significantly from correct temporal order, while a single boundary frame outperforms the full ordered clip for three models. Step-only input performs best for all four models, and adding 15 seconds of history significantly degrades three. Revealing the current outcome improves Local Intent by 7.81 points, while revealing the following step improves Next-Plan by 13.17 points. These findings indicate that current models can achieve strong intent-prediction scores through static boundary cues without robustly exploiting temporal order or procedural history.

## 10-004 | VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training
- arXiv: 2203.12602  first public: 2022-03-23  latest: 2022-10-18  primary cat: cs.CV
- authors (4): Zhan Tong; Yibing Song; Jue Wang; Limin Wang
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2022 camera-ready version
- URLs on first pages of PDF: https://github.com/MCG-NJU/VideoMAE
- pages: 25

ABSTRACT: Pre-training video transformers on extra large-scale datasets is generally required to achieve premier performance on relatively small datasets. In this paper, we show that video masked autoencoders (VideoMAE) are data-efficient learners for self-supervised video pre-training (SSVP). We are inspired by the recent ImageMAE and propose customized video tube masking with an extremely high ratio. This simple design makes video reconstruction a more challenging self-supervision task, thus encouraging extracting more effective video representations during this pre-training process. We obtain three important findings on SSVP: (1) An extremely high proportion of masking ratio (i.e., 90% to 95%) still yields favorable performance of VideoMAE. The temporally redundant video content enables a higher masking ratio than that of images. (2) VideoMAE achieves impressive results on very small datasets (i.e., around 3k-4k videos) without using any extra data. (3) VideoMAE shows that data quality is more important than data quantity for SSVP. Domain shift between pre-training and target datasets is an important issue. Notably, our VideoMAE with the vanilla ViT can achieve 87.4% on Kinetics-400, 75.4% on Something-Something V2, 91.3% on UCF101, and 62.6% on HMDB51, without using any extra data. Code is available at https://github.com/MCG-NJU/VideoMAE.

## 10-005 | Video-LLaVA: Learning United Visual Representation by Alignment Before Projection
- arXiv: 2311.10122  first public: 2023-11-16  latest: 2024-10-01  primary cat: cs.CV
- authors (7): Bin Lin; Yang Ye; Bin Zhu; Jiaxi Cui; Munan Ning; Peng Jin ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- URLs on first pages of PDF: https://github.com/PKU-YuanGroup/Video-LLaV
- pages: 14

ABSTRACT: The Large Vision-Language Model (LVLM) has enhanced the performance of various downstream tasks in visual-language understanding. Most existing approaches encode images and videos into separate feature spaces, which are then fed as inputs to large language models. However, due to the lack of unified tokenization for images and videos, namely misalignment before projection, it becomes challenging for a Large Language Model (LLM) to learn multi-modal interactions from several poor projection layers. In this work, we unify visual representation into the language feature space to advance the foundational LLM towards a unified LVLM. As a result, we establish a simple but robust LVLM baseline, Video-LLaVA, which learns from a mixed dataset of images and videos, mutually enhancing each other. Video-LLaVA achieves superior performances on a broad range of 9 image benchmarks across 5 image question-answering datasets and 4 image benchmark toolkits. Additionally, our Video-LLaVA also outperforms Video-ChatGPT by 5.8%, 9.9%, 18.6%, and 10.1% on MSRVTT, MSVD, TGIF, and ActivityNet, respectively. Notably, extensive experiments demonstrate that Video-LLaVA mutually benefits images and videos within a unified visual representation, outperforming models designed specifically for images or videos. We aim for this work to provide modest insights into the multi-modal inputs for the LLM. Code address: \href{https://github.com/PKU-YuanGroup/Video-LLaVA}

## 10-006 | LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models
- arXiv: 2311.17043  first public: 2023-11-28  latest: 2023-11-28  primary cat: cs.CV
- authors (3): Yanwei Li; Chengyao Wang; Jiaya Jia
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: Code is available at https://github.com/dvlab-research/LLaMA-VID
- URLs on first pages of PDF: https://github.com/dvlab-research/LLaMA-VID
- pages: 18

ABSTRACT: In this work, we present a novel method to tackle the token generation challenge in Vision Language Models (VLMs) for video and image understanding, called LLaMA-VID. Current VLMs, while proficient in tasks like image captioning and visual question answering, face computational burdens when processing long videos due to the excessive visual tokens. LLaMA-VID addresses this issue by representing each frame with two distinct tokens, namely context token and content token. The context token encodes the overall image context based on user input, whereas the content token encapsulates visual cues in each frame. This dual-token strategy significantly reduces the overload of long videos while preserving critical information. Generally, LLaMA-VID empowers existing frameworks to support hour-long videos and pushes their upper limit with an extra context token. It is proved to surpass previous methods on most of video- or image-based benchmarks. Code is available https://github.com/dvlab-research/LLaMA-VID}{https://github.com/dvlab-research/LLaMA-VID

## 10-009 | LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding
- arXiv: 2407.15754  first public: 2024-07-22  latest: 2024-07-22  primary cat: cs.CV
- authors (4): Haoning Wu; Dongxu Li; Bei Chen; Junnan Li
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: 29 pages
- pages: 29

ABSTRACT: Large multimodal models (LMMs) are processing increasingly longer and richer inputs. Albeit the progress, few public benchmark is available to measure such development. To mitigate this gap, we introduce LongVideoBench, a question-answering benchmark that features video-language interleaved inputs up to an hour long. Our benchmark includes 3,763 varying-length web-collected videos with their subtitles across diverse themes, designed to comprehensively evaluate LMMs on long-term multimodal understanding. To achieve this, we interpret the primary challenge as to accurately retrieve and reason over detailed multimodal information from long inputs. As such, we formulate a novel video question-answering task termed referring reasoning. Specifically, as part of the question, it contains a referring query that references related video contexts, called referred context. The model is then required to reason over relevant video details from the referred context. Following the paradigm of referring reasoning, we curate 6,678 human-annotated multiple-choice questions in 17 fine-grained categories, establishing one of the most comprehensive benchmarks for long-form video understanding. Evaluations suggest that the LongVideoBench presents significant challenges even for the most advanced proprietary models (e.g. GPT-4o, Gemini-1.5-Pro, GPT-4-Turbo), while their open-source counterparts show an even larger performance gap. In addition, our results indicate that model performance on the benchmark improves only when they are capable of processing more frames, positioning LongVideoBench as a valuable benchmark for evaluating future-generation long-context LMMs.

## 10-011 | Long Context Transfer from Language to Vision
- arXiv: 2406.16852  first public: 2024-06-24  latest: 2024-07-01  primary cat: cs.CV
- authors (10): Peiyuan Zhang; Kaichen Zhang; Bo Li; Guangtao Zeng; Jingkang Yang; Yuanhan Zhang ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: Code, demo, and models are available at https://github.com/EvolvingLMMs-Lab/LongVA
- URLs on first pages of PDF: https://github.com/EvolvingLMMs-Lab/LongVA
- pages: 17

ABSTRACT: Video sequences offer valuable temporal information, but existing large multimodal models (LMMs) fall short in understanding extremely long videos. Many works address this by reducing the number of visual tokens using visual resamplers. Alternatively, in this paper, we approach this problem from the perspective of the language model. By simply extrapolating the context length of the language backbone, we enable LMMs to comprehend orders of magnitude more visual tokens without any video training. We call this phenomenon long context transfer and carefully ablate its properties. To effectively measure LMMs' ability to generalize to long contexts in the vision modality, we develop V-NIAH (Visual Needle-In-A-Haystack), a purely synthetic long vision benchmark inspired by the language model's NIAH test. Our proposed Long Video Assistant (LongVA) can process 2000 frames or over 200K visual tokens without additional complexities. With its extended context length, LongVA achieves state-of-the-art performance on Video-MME among 7B-scale models by densely sampling more input frames. Our work is open-sourced at https://github.com/EvolvingLMMs-Lab/LongVA.

## 10-012 | LLaVA-Video: Video Instruction Tuning With Synthetic Data
- arXiv: 2410.02713  first public: 2024-10-03  latest: 2025-08-01  primary cat: cs.CV
- authors (7): Yuanhan Zhang; Jinming Wu; Wei Li; Bo Li; Zejun Ma; Ziwei Liu ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: Project page: https://llava-vl.github.io/blog/2024-09-30-llava-video/; Accepted at TMLR
- pages: 24

ABSTRACT: The development of video large multimodal models (LMMs) has been hindered by the difficulty of curating large amounts of high-quality raw data from the web. To address this, we propose an alternative approach by creating a high-quality synthetic dataset specifically for video instruction-following, namely LLaVA-Video-178K. This dataset includes key tasks such as detailed captioning, open-ended question-answering (QA), and multiple-choice QA. By training on this dataset, in combination with existing visual instruction tuning data, we introduce LLaVA-Video, a new video LMM. Our experiments demonstrate that LLaVA-Video achieves strong performance across various video benchmarks, highlighting the effectiveness of our dataset. We plan to release the dataset, its generation pipeline, and the model checkpoints.

## 10-013 | VideoLLaMA 3: Frontier Multimodal Foundation Models for Image and Video Understanding
- arXiv: 2501.13106  first public: 2025-01-22  latest: 2025-06-03  primary cat: cs.CV
- authors (15): Boqiang Zhang; Kehan Li; Zesen Cheng; Zhiqiang Hu; Yuqian Yuan; Guanzheng Chen ...
- seed subtopic: 视频理解; type: 技术报告; cross: []
- arXiv comment: BZ, KL, ZC, ZH, YY, GC, SL, YJ, HZ, and XL contributed equally to this project. Code: https://github.com/DAMO-NLP-SG/VideoLLaMA3
- URLs on first pages of PDF: https://github.com/DAMO-NLP-SG/VideoLLaMA3
- pages: 34

ABSTRACT: In this paper, we propose VideoLLaMA3, a more advanced multimodal foundation model for image and video understanding. The core design philosophy of VideoLLaMA3 is vision-centric. The meaning of "vision-centric" is two-fold: the vision-centric training paradigm and vision-centric framework design. The key insight of our vision-centric training paradigm is that high-quality image-text data is crucial for both image and video understanding. Instead of preparing massive video-text datasets, we focus on constructing large-scale and high-quality image-text datasets. VideoLLaMA3 has four training stages: 1) Vision Encoder Adaptation, which enables vision encoder to accept images of variable resolutions as input; 2) Vision-Language Alignment, which jointly tunes the vision encoder, projector, and LLM with large-scale image-text data covering multiple types (including scene images, documents, charts) as well as text-only data. 3) Multi-task Fine-tuning, which incorporates image-text SFT data for downstream tasks and video-text data to establish a foundation for video understanding. 4) Video-centric Fine-tuning, which further improves the model's capability in video understanding. As for the framework design, to better capture fine-grained details in images, the pretrained vision encoder is adapted to encode images of varying sizes into vision tokens with corresponding numbers, rather than a fixed number of tokens. For video inputs, we reduce the number of vision tokens according to their similarity so that the representation of videos will be more precise and compact. Benefit from vision-centric designs, VideoLLaMA3 achieves compelling performances in both image and video understanding benchmarks.

## 10-014 | InternVideo2: Scaling Foundation Models for Multimodal Video Understanding
- arXiv: 2403.15377  first public: 2024-03-22  latest: 2024-08-14  primary cat: cs.CV
- authors (20): Yi Wang; Kunchang Li; Xinhao Li; Jiashuo Yu; Yinan He; Chenting Wang ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: a technical report about video understanding (accepted to ECCV2024)
- URLs on first pages of PDF: https://github.com/OpenGVLab/InternVideo/tree/main/InternVideo2
- pages: 27

ABSTRACT: We introduce InternVideo2, a new family of video foundation models (ViFM) that achieve the state-of-the-art results in video recognition, video-text tasks, and video-centric dialogue. Our core design is a progressive training approach that unifies the masked video modeling, crossmodal contrastive learning, and next token prediction, scaling up the video encoder size to 6B parameters. At the data level, we prioritize spatiotemporal consistency by semantically segmenting videos and generating video-audio-speech captions. This improves the alignment between video and text. Through extensive experiments, we validate our designs and demonstrate superior performance on over 60 video and audio tasks. Notably, our model outperforms others on various video-related dialogue and long video understanding benchmarks, highlighting its ability to reason and comprehend longer contexts. Code and models are available at https://github.com/OpenGVLab/InternVideo/tree/main/InternVideo2/.

## 10-016 | TimeChat: A Time-sensitive Multimodal Large Language Model for Long Video Understanding
- arXiv: 2312.02051  first public: 2023-12-04  latest: 2024-03-28  primary cat: cs.CV
- authors (5): Shuhuai Ren; Linli Yao; Shicheng Li; Xu Sun; Lu Hou
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: CVPR 2024 camera-ready version, code is available at https://github.com/RenShuhuai-Andy/TimeChat
- pages: 18

ABSTRACT: This work proposes TimeChat, a time-sensitive multimodal large language model specifically designed for long video understanding. Our model incorporates two key architectural contributions: (1) a timestamp-aware frame encoder that binds visual content with the timestamp of each frame, and (2) a sliding video Q-Former that produces a video token sequence of varying lengths to accommodate videos of various durations. Additionally, we construct an instruction-tuning dataset, encompassing 6 tasks and a total of 125K instances, to further enhance TimeChat's instruction-following performance. Experiment results across various video understanding tasks, such as dense captioning, temporal grounding, and highlight detection, demonstrate TimeChat's strong zero-shot temporal localization and reasoning capabilities. For example, it achieves +9.2 F1 score and +2.8 CIDEr on YouCook2, +5.8 HIT@1 on QVHighlights, and +27.5 R@1 (IoU=0.5) on Charades-STA, compared to state-of-the-art video large language models, holding the potential to serve as a versatile video assistant for long-form video comprehension tasks and satisfy realistic user requirements.

## 10-018 | VideoLLM-online: Online Video Large Language Model for Streaming Video
- arXiv: 2406.11816  first public: 2024-06-17  latest: 2024-06-17  primary cat: cs.CV
- authors (10): Joya Chen; Zhaoyang Lv; Shiwei Wu; Kevin Qinghong Lin; Chenan Song; Difei Gao ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: CVPR 2024. This arxiv version is upgraded with Llama-3
- pages: 19

ABSTRACT: Recent Large Language Models have been enhanced with vision capabilities, enabling them to comprehend images, videos, and interleaved vision-language content. However, the learning methods of these large multimodal models typically treat videos as predetermined clips, making them less effective and efficient at handling streaming video inputs. In this paper, we propose a novel Learning-In-Video-Stream (LIVE) framework, which enables temporally aligned, long-context, and real-time conversation within a continuous video stream. Our LIVE framework comprises comprehensive approaches to achieve video streaming dialogue, encompassing: (1) a training objective designed to perform language modeling for continuous streaming inputs, (2) a data generation scheme that converts offline temporal annotations into a streaming dialogue format, and (3) an optimized inference pipeline to speed up the model responses in real-world video streams. With our LIVE framework, we built VideoLLM-online model upon Llama-2/Llama-3 and demonstrate its significant advantages in processing streaming videos. For instance, on average, our model can support streaming dialogue in a 5-minute video clip at over 10 FPS on an A100 GPU. Moreover, it also showcases state-of-the-art performance on public offline video benchmarks, such as recognition, captioning, and forecasting. The code, model, data, and demo have been made available at https://showlab.github.io/videollm-online.

## 10-020 | Video-R1: Reinforcing Video Reasoning in MLLMs
- arXiv: 2503.21776  first public: 2025-03-27  latest: 2025-10-22  primary cat: cs.CV
- authors (10): Kaituo Feng; Kaixiong Gong; Bohao Li; Zonghao Guo; Yibing Wang; Tianshuo Peng ...
- seed subtopic: 视频理解; type: 原始研究; cross: ['04']
- arXiv comment: NeurIPS 2025, Project page: https://github.com/tulerfeng/Video-R1
- URLs on first pages of PDF: https://github.com/tulerfeng/Video-R1 https://github.com/tulerfeng/Video-R1
- pages: 17

ABSTRACT: Inspired by DeepSeek-R1's success in eliciting reasoning abilities through rule-based reinforcement learning (RL), we introduce Video-R1 as the first attempt to systematically explore the R1 paradigm for incentivizing video reasoning within multimodal large language models (MLLMs). However, directly applying RL training with the GRPO algorithm to video reasoning presents two primary challenges: (i) a lack of temporal modeling for video reasoning, and (ii) the scarcity of high-quality video-reasoning data. To address these issues, we first propose the T-GRPO algorithm, which encourages models to utilize temporal information in videos for reasoning. Additionally, instead of relying solely on video data, we incorporate high-quality image-reasoning data into the training process. We have constructed two datasets: Video-R1-CoT-165k for SFT cold start and Video-R1-260k for RL training, both comprising image and video data. Experimental results demonstrate that Video-R1 achieves significant improvements on video reasoning benchmarks such as VideoMMMU and VSI-Bench, as well as on general video benchmarks including MVBench and TempCompass, etc. Notably, Video-R1-7B attains a 37.1% accuracy on video spatial reasoning benchmark VSI-bench, surpassing the commercial proprietary model GPT-4o. All code, models, and data are released in: https://github.com/tulerfeng/Video-R1.

## 10-023 | VideoPrism: A Foundational Visual Encoder for Video Understanding
- arXiv: 2402.13217  first public: 2024-02-20  latest: 2025-06-07  primary cat: cs.CV
- authors (19): Long Zhao; Nitesh B. Gundavarapu; Liangzhe Yuan; Hao Zhou; Shen Yan; Jennifer J. Sun ...
- seed subtopic: 时间建模; type: 原始研究; cross: []
- arXiv comment: Accepted to ICML 2024. v2: added retrieval results on MSRVTT (1K-A), more data analyses, and ablation studies; v3: released models at https://github.com/google-deepmind/videoprism
- pages: 27

ABSTRACT: We introduce VideoPrism, a general-purpose video encoder that tackles diverse video understanding tasks with a single frozen model. We pretrain VideoPrism on a heterogeneous corpus containing 36M high-quality video-caption pairs and 582M video clips with noisy parallel text (e.g., ASR transcripts). The pretraining approach improves upon masked autoencoding by global-local distillation of semantic video embeddings and a token shuffling scheme, enabling VideoPrism to focus primarily on the video modality while leveraging the invaluable text associated with videos. We extensively test VideoPrism on four broad groups of video understanding tasks, from web video question answering to CV for science, achieving state-of-the-art performance on 31 out of 33 video understanding benchmarks. Our models are released at https://github.com/google-deepmind/videoprism.

## 10-026 | HourVideo: 1-Hour Video-Language Understanding
- arXiv: 2411.04998  first public: 2024-11-07  latest: 2024-11-07  primary cat: cs.CV
- authors (10): Keshigeyan Chandrasegaran; Agrim Gupta; Lea M. Hadzic; Taran Kota; Jimming He; Cristóbal Eyzaguirre ...
- seed subtopic: 视频理解; type: 原始研究; cross: []
- arXiv comment: NeurIPS 2024 Datasets and Benchmarks Track; 28 pages
- pages: 28

ABSTRACT: We present HourVideo, a benchmark dataset for hour-long video-language understanding. Our dataset consists of a novel task suite comprising summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. HourVideo includes 500 manually curated egocentric videos from the Ego4D dataset, spanning durations of 20 to 120 minutes, and features 12,976 high-quality, five-way multiple-choice questions. Benchmarking results reveal that multimodal models, including GPT-4 and LLaVA-NeXT, achieve marginal improvements over random chance. In stark contrast, human experts significantly outperform the state-of-the-art long-context multimodal model, Gemini Pro 1.5 (85.0% vs. 37.3%), highlighting a substantial gap in multimodal capabilities. Our benchmark, evaluation toolkit, prompts, and documentation are available at https://hourvideo.stanford.edu

## 10-030 | Octo: An Open-Source Generalist Robot Policy
- arXiv: 2405.12213  first public: 2024-05-20  latest: 2024-05-26  primary cat: cs.RO
- authors (19): Octo Model Team; Dibya Ghosh; Homer Walke; Karl Pertsch; Kevin Black; Oier Mees ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: Project website: https://octo-models.github.io
- pages: 17

ABSTRACT: Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces. We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## 10-031 | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation
- arXiv: 2410.07864  first public: 2024-10-10  latest: 2025-03-01  primary cat: cs.RO
- authors (9): Songming Liu; Lingxuan Wu; Bangguo Li; Hengkai Tan; Huayu Chen; Zhengyi Wang ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: 10 pages, conference
- pages: 28

ABSTRACT: Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## 10-034 | FAST: Efficient Action Tokenization for Vision-Language-Action Models
- arXiv: 2501.09747  first public: 2025-01-16  latest: 2025-01-16  primary cat: cs.RO
- authors (9): Karl Pertsch; Kyle Stachowicz; Brian Ichter; Danny Driess; Suraj Nair; Quan Vuong ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Website: https://www.pi.website/research/fast
- pages: 19

ABSTRACT: Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 10-035 | Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
- arXiv: 2502.19645  first public: 2025-02-27  latest: 2025-04-28  primary cat: cs.RO
- authors (3): Moo Jin Kim; Chelsea Finn; Percy Liang
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Accepted to Robotics: Science and Systems (RSS) 2025. Project website: https://openvla-oft.github.io/
- pages: 24

ABSTRACT: Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 10-038 | 3D-VLA: A 3D Vision-Language-Action Generative World Model
- arXiv: 2403.09631  first public: 2024-03-14  latest: 2024-03-14  primary cat: cs.CV
- authors (8): Haoyu Zhen; Xiaowen Qiu; Peihao Chen; Jincheng Yang; Xin Yan; Yilun Du ...
- seed subtopic: 世界模型; type: 原始研究; cross: []
- arXiv comment: Project page: https://vis-www.cs.umass.edu/3dvla/
- pages: 15

ABSTRACT: Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 10-039 | Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation
- arXiv: 2401.02117  first public: 2024-01-04  latest: 2024-01-04  primary cat: cs.RO
- authors (3): Zipeng Fu; Tony Z. Zhao; Chelsea Finn
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: Project website: https://mobile-aloha.github.io (Zipeng Fu and Tony Z. Zhao are project co-leads, Chelsea Finn is the advisor)
- pages: 20

ABSTRACT: Imitation learning from human demonstrations has shown impressive performance in robotics. However, most results focus on table-top manipulation, lacking the mobility and dexterity necessary for generally useful tasks. In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control. We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection. It augments the ALOHA system with a mobile base, and a whole-body teleoperation interface. Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile manipulation tasks. With 50 demonstrations for each task, co-training can increase success rates by up to 90%, allowing Mobile ALOHA to autonomously complete complex mobile manipulation tasks such as sauteing and serving a piece of shrimp, opening a two-door wall cabinet to store heavy cooking pots, calling and entering an elevator, and lightly rinsing a used pan using a kitchen faucet. Project website: https://mobile-aloha.github.io

## 10-040 | DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset
- arXiv: 2403.12945  first public: 2024-03-19  latest: 2025-04-22  primary cat: cs.RO
- authors (101): Alexander Khazatsky; Karl Pertsch; Suraj Nair; Ashwin Balakrishna; Sudeep Dasari; Siddharth Karamcheti ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: Project website: https://droid-dataset.github.io/
- pages: 26

ABSTRACT: The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies. However, creating such datasets is challenging: collecting robot manipulation data in diverse environments poses logistical and safety challenges and requires substantial investments in hardware and human labour. As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited scene and task diversity. In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 84 tasks by 50 data collectors in North America, Asia, and Europe over the course of 12 months. We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability. We open source the full dataset, policy learning code, and a detailed guide for reproducing our robot hardware setup.

## 10-041 | Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers
- arXiv: 2409.20537  first public: 2024-09-30  latest: 2024-09-30  primary cat: cs.RO
- authors (4): Lirui Wang; Xinlei Chen; Jialiang Zhao; Kaiming He
- seed subtopic: 机器人; type: 原始研究; cross: []
- arXiv comment: See the project website (https://liruiw.github.io/hpt/) for code and videos
- journal_ref: Neurips 2024
- URLs on first pages of PDF: https://liruiw.github.io/hpt
- pages: 24

ABSTRACT: One of the roadblocks for training generalist robotic models today is heterogeneity. Previous robot learning methods often collect data to train with one specific embodiment for one task, which is expensive and prone to overfitting. This work studies the problem of learning policy representations through heterogeneous pre-training on robot data across different embodiments and tasks at scale. We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared representation. This general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to map to control robots for different tasks. Leveraging the recent large-scale multi-embodiment real-world robotic datasets as well as simulation, deployed robots, and human video datasets, we investigate pre-training policies across heterogeneity. We conduct experiments to investigate the scaling behaviors of training objectives, to the extent of 52 datasets. HPTs outperform several baselines and enhance the fine-tuned policy performance by over 20% on unseen tasks in multiple simulator benchmarks and real-world settings. See the project website (https://liruiw.github.io/hpt/) for code and videos.

## 10-042 | What Matters in Building Vision-Language-Action Models for Generalist Robots
- arXiv: 2412.14058  first public: 2024-12-18  latest: 2026-02-13  primary cat: cs.RO
- authors (13): Xinghang Li; Peiyan Li; Long Qian; Minghuan Liu; Dong Wang; Jirong Liu ...
- seed subtopic: 视觉语言动作模型; type: 原始研究; cross: []
- arXiv comment: Project page: robovlms.github.io. Added limitations and future works. Fix categorization
- pages: 37

ABSTRACT: To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 10-043 | Evaluating Real-World Robot Manipulation Policies in Simulation
- arXiv: 2405.05941  first public: 2024-05-09  latest: 2024-05-09  primary cat: cs.RO
- authors (16): Xuanlin Li; Kyle Hsu; Jiayuan Gu; Karl Pertsch; Oier Mees; Homer Rich Walke ...
- seed subtopic: 机器人; type: 原始研究; cross: []
- pages: 22

ABSTRACT: The field of robotics has made significant advances towards generalist robot manipulation policies. However, real-world evaluation of such policies is not scalable and faces reproducibility challenges, which are likely to worsen as policies broaden the spectrum of tasks they can perform. We identify control and visual disparities between real and simulated environments as key challenges for reliable simulated evaluation and propose approaches for mitigating these gaps without needing to craft full-fidelity digital twins of real-world environments. We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups. Through paired sim-and-real evaluations of manipulation policies, we demonstrate strong correlation between policy performance in SIMPLER environments and in the real world. Additionally, we find that SIMPLER evaluations accurately reflect real-world policy behavior modes such as sensitivity to various distribution shifts. We open-source all SIMPLER environments along with our workflow for creating new environments at https://simpler-env.github.io to facilitate research on general-purpose manipulation policies and simulated evaluation frameworks.
