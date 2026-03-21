---
id: arxiv-2510.00547
title: Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests
year: 2025
country: Internacional
source: ArXiv (cs.CV, cs.AI)
doc_type: Artículo científico
language: en
tags:
  - artículo científico
  - ArXiv
---

## Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests

Aoduo Li 2 , Peikai Lin 2 , Jiancheng Li 2 , Zhen Zhang 1* , Shiting Wu 3 , Zexiao Liang 1 , and Zhifa Jiang 4

1 School of Computer Science and Engineering, Huizhou University

2 School of Advanced Manufacturing, Guangdong University of Technology 3 Huizhou Boluo Power Supply Bureau Guangdong Power Grid Co.,Ltd. 4 Obstetrics and Gynaecology, Huizhou First Maternal and Child Health Care Hospital

Abstract -Detecting agricultural pests in complex forestry environments using remote sensing imagery is fundamental for ecological preservation, yet it is severely hampered by practical challenges. Targets are often minuscule, heavily occluded, and visually similar to the cluttered background, causing conventional object detection models to falter due to the loss of fine-grained features and an inability to handle extreme data imbalance. To overcome these obstacles, this paper introduces ForestpestYOLO, a detection framework meticulously optimized for the nuances of forestry remote sensing. Building upon the YOLOv8 architecture, our framework introduces a synergistic trio of innovations. We first integrate a lossless downsampling module, SPD-Conv, to ensure that critical high-resolution details of small targets are preserved throughout the network. This is complemented by a novel cross-stage feature fusion block, CSPOK, which dynamically enhances multi-scale feature representation while suppressing background noise. Finally, we employ VarifocalLoss to refine the training objective, compelling the model to focus on high-quality and hard-to-classify samples. Extensive experiments on our challenging, self-constructed ForestPest dataset demonstrate that Forestpest-YOLO achieves state-of-theart performance, showing marked improvements in detecting small, occluded pests and significantly outperforming established baseline models.

Index Terms -Small object detection, remote sensing imagery, YOLO, feature fusion, forestry pest detection.

## I. INTRODUCTION

Automated remote sensing monitoring of forestry pests is a key technology for achieving smart forestry and preventing ecological disasters. High-resolution images acquired using unmanned aerial vehicles (UAVs) enable object detection to identify and locate pest outbreak areas with efficiency and coverage far beyond manual inspection. However, this task remains challenging.

A primary difficulty lies in the extreme scales and low signal-to-noise ratio of targets. Pests such as individual eggs or boreholes are extremely small; in our dataset, over 70% of targets have an area less than 32 × 32 pixels. These weak cues are easily overwhelmed by high-frequency noise such as bark textures and dappled shadows. Severe occlusion and complex forest backgrounds compound the issue: canopy structure means targets are often occluded by leaves and branches. Backgrounds also contain non-target objects

* Corresponding author.

(rocks, fallen leaves) similar in color/shape to pest camouflage, leading to high false detections. Finally, data acquisition and generalization present significant hurdles. Collection varies by season and weather, and pest morphology varies across lifecycle stages, increasing intra-class variance. Existing datasets often lack negative images, causing many false positives in healthy areas and limiting generalization. Similar concerns about imbalance and generalization appear in semi-supervised medical image segmentation and contrastive learning [1], [2].

To address these challenges, we introduce ForestpestYOLO, a multi-pronged detector built on YOLOv8 [3]. First, to avoid feature loss on minute targets, we integrate SPD-Conv [4] to preserve fine detail. Second, we propose the CSPOK module, leveraging Omni-Kernel [5] for robust, efficient multiscale fusion. Finally, we employ VarifocalLoss [6] to handle severe sample imbalance. Given the visual complexity and occlusion in natural scenes, advances in robust visual representation-especially secure, noise-resilient medical image encryption using permutation-diffusion and chaotic dynamics-offer useful design insights [7]-[10]. We validate efficacy via extensive experiments on our custom ForestPest dataset.

## II. RELATED WORK

Our research sits at the intersection of three areas in object detection and computer vision [11]-[33]: small object detection [34]-[43], feature fusion and attention [44]-[54], and loss design for robust training [55]-[67].

## A. Advances in Small Object Detection

Small object detection remains difficult due to scarce distinguishable features [68]. A foundational route is multi-scale representation, popularized by FPN [69], which fuses highlevel semantics with low-level detail. Yet aggressive backbone downsampling can degrade fine information before fusion. Lossless alternatives like SPD-Conv [4] fold spatial information into channel depth, central to our design. PANet [70] adds a bottom-up path, and BiFPN [71] introduces weighted, bi-directional fusion. Data-centric strategies-copy-paste [72], Mosaic, MixUp-enrich tiny-instance exposure; GAN-based super-resolution [73] and context modeling [74] further help.

## B. Feature Fusion and Attention Mechanisms

Attention improves fusion across scales. SE-Net [75] introduced channel attention; CBAM [76] added spatial attention. To capture global context, Non-local Networks [77] model long-range dependencies; ViT [78] and DETR [79] rely on full self-attention but at notable cost. Dynamic, content-aware convolutions-Deformable Convolutions [80] and Dynamic Convolutions [81]-adapt sampling or weights. Our CSPOK follows this trend, leveraging Omni-Kernel [5] for dynamic, efficient fusion tailored to forestry-pest textures and structures.

## C. Loss Functions and Training Strategies for Robust Training

Loss design is critical for imbalanced, hard samples. Focal Loss [82] down-weights easy examples; VarifocalLoss (VFL) [6] treats positives/negatives asymmetrically, prioritizing highquality positives. For localization, Smooth L1 has given way to IoU-based losses (GIoU/DIoU/CIoU [83], [84]) that better match evaluation. GFL [85] learns box distributions, and dynamic assignment (ATSS [86], SimOTA [87]) improves stability. These advances yield more stable, effective training, especially on challenging sets like ForestPest.

## III. METHODOLOGY: THE FORESTPEST-YOLO FRAMEWORK

The architectural design of Forestpest-YOLO is centered on three strategic modifications to the YOLOv8 framework, each targeting a specific challenge in forestry pest detection. We engineered a novel framework that not only preserves critical low-level features but also enhances multi-scale feature interaction and optimizes the learning objective for imbalanced data.

## A. Overall Architecture

The overall architecture of Forestpest-YOLO, illustrated in Fig. 1, is a systematic enhancement of the standard YOLOv8 pipeline. The data flow begins in the backbone, where we strategically replace a conventional strided convolution with our SPD-Conv module after the P2 feature extraction stage. This crucial intervention ensures that high-resolution spatial information, which is vital for small object detection, is preserved rather than discarded during downsampling. The feature maps then proceed to the neck, where we substitute the standard C2f fusion units with our more powerful CSPOK modules. These modules are designed to facilitate a more sophisticated and robust integration of features across different semantic and spatial scales. Finally, the fused feature maps are passed to the detection heads, where the learning process is governed by VarifocalLoss, replacing the original classification loss to better cope with the severe class imbalance typical in pest detection scenarios.

## B. SPD-Conv: Lossless Downsampling Module

To address the degradation of fine-grained features caused by traditional downsampling, we incorporate SPD-Conv, a space-to-depth feature transformer. Given an input feature map X ∈ R S × S × C 1 , SPD-Conv first performs a slicing operation

Fig. 1. The overall network architecture of Forestpest-YOLO, illustrating the main data flow from input to detection. Key modifications include the integration of the SPD-Conv module in the backbone and the CSPOK fusion block in the neck.

<!-- image -->

with a scale factor (e.g., scale=2). This partitions X into scale 2 sub-maps. For scale=2, the four sub-maps are defined by:

<!-- formula-not-decoded -->

These sub-maps are then concatenated along the channel dimension, transforming the spatial information into channel depth and creating an intermediate feature map X ′ :

<!-- formula-not-decoded -->

where X ′ ∈ R S 2 × S 2 × 4 C 1 . Finally, a non-strided convolution is applied to reduce the channel dimension and learn richer feature representations, producing the output X ′′ :

<!-- formula-not-decoded -->

where X ′′ ∈ R S 2 × S 2 × C 2 . This process effectively halves the spatial dimensions while preserving the complete feature set.

## C. CSPOK: Cross-Stage Parallel Omni-Kernel Fusion

The CSPOK module, whose structure is detailed in Fig. 2, is designed for superior multi-scale feature fusion by combining the efficiency of Cross-Stage Partial (CSP) design with the adaptability of Omni-Kernel (OKM). An input feature map F in is first split into two parts:

<!-- formula-not-decoded -->

F 1 serves as a direct, cross-stage connection, preserving the original information flow. The other part, F 2 , is passed through a sophisticated processing block where the OmniKernel mechanism is applied. This is represented as:

<!-- formula-not-decoded -->

The OKM block dynamically adapts its fusion strategy based on the input features. The two pathways are then concatenated and passed through a final convolutional layer to integrate the information:

<!-- formula-not-decoded -->

This parallel design enriches the feature diversity and enhances the model's ability to capture both local details and global context.

Fig. 2. Detailed structure of the improved neck, highlighting the integration of our proposed modules for enhanced feature fusion. The diagram shows SPD-Conv for lossless downsampling and the CSPOK block replacing the original C2f unit.

<!-- image -->

## D. VarifocalLoss (VFL) and Matching Optimization

To address the severe imbalance between easy/hard and positive/negative samples, we adopt VarifocalLoss (VFL) [6] as the classification loss function:

<!-- formula-not-decoded -->

where p is the model's predicted score, and q is the target IoU score. Based on empirical validation, we set the hyperparameters to α = 0 . 75 and γ = 2 . 0 . As conceptually illustrated in Fig. 3, VFL's asymmetric weighting scheme encourages the model to focus on high-quality positive samples, leading to more precise localization and classification.

<!-- image -->

matching loss

Fig. 3. Conceptual visualization of matching quality improvement achieved by using VarifocalLoss. The left side depicts potential poor matching, while the right (green lines) illustrates the precise target association our loss encourages.

## IV. EXPERIMENTS

## A. Dataset: The ForestPest Dataset

To effectively evaluate our proposed model, we constructed a self-built forestry remote sensing pest detection dataset named ForestPest . This dataset is designed to simulate various challenges encountered in real-world forestry monitoring, containing 5,690 high-resolution UAV images of common forestry pests in COCO format. The dataset is characterized by its diversity in scenes, pest species, and life stages, with a significant portion of small, occluded, and camouflaged targets, making it a challenging benchmark. Key statistics are summarized in Table II.

## B. Implementation Details

All models were trained under a unified experimental protocol to ensure a fair comparison. The implementation was based on PyTorch, with YOLOv8s serving as the baseline. The experiments were conducted on a server equipped with four NVIDIA RTX 3090 GPUs. We employed the AdamW optimizer with an initial learning rate of 1 × 10 -3 , which was adjusted using a cosine annealing strategy over 100 training epochs. Input images were uniformly resized to 640x640, and a batch size of 8 was used. To enhance model robustness and prevent overfitting, we applied a suite of data augmentation techniques, including Mosaic, MixUp, random affine transformations (rotation, scaling), and color jitter. The AP small metric is calculated following the COCO standard, defining small objects as those with an area less than 32 2 pixels.

## C. Comparison with State-of-the-Art Models

We conducted a comprehensive performance comparison between Forestpest-YOLO and several mainstream object detectors on the ForestPest test set, with results shown in Table I. Our model demonstrates superior performance across all key accuracy metrics. Notably, Forestpest-YOLO achieves an mAP@.5:.95 of 0.508, surpassing the YOLOv8s baseline. The most significant improvement is observed in the AP small metric, where our model achieves 0.131, a 17.0% relative increase over YOLOv8s. This highlights the efficacy of our framework in addressing the core challenge of small object detection in complex forestry environments. While other models like YOLOv8s show competitive precision, their lower recall suggests a tendency to miss difficult targets, a shortcoming our model effectively addresses. These accuracy gains are achieved with only a marginal increase in computational cost, making it a practical solution for real-world applications.

## D. Ablation Study

To dissect the individual contributions of our proposed components, we performed a systematic ablation study. We began with the YOLOv8s baseline and incrementally added each module: SPD-Conv, CSPOK, and finally VarifocalLoss (VFL). The results, presented in Table III, clearly demonstrate the effectiveness of each enhancement. The introduction of SPD-Conv alone yielded a 6.3% relative improvement in AP small , confirming the benefits of its lossless downsampling

TABLE I PERFORMANCE COMPARISON ON THE FORESTPEST TEST SET

Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Model: YOLOv5s, mAP .5:.95: 0.478, mAP .5: 0.728, AP small: 0.11, Params(M): 7.2, FLOPs(G): 16.5, FPS: 140.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Model: YOLOv8s, mAP .5:.95: 0.482, mAP .5: 0.746, AP small: 0.112, Params(M): 11.2, FLOPs(G): 28.6, FPS: 125.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Model: RT-DETR-R50, mAP .5:.95: 0.501, mAP .5: 0.737, AP small: 0.128, Params(M): 33, FLOPs(G): 109, FPS: 74.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Model: Forestpest-YOLO (Ours), mAP .5:.95: 0.508, mAP .5: 0.762, AP small: 0.131, Params(M): 12.1, FLOPs(G): 30.2, FPS: 118.
TABLE II FORESTPEST DATASET STATISTICS

Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Attribute: Total Images, Value: 5,690.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Attribute: Train/Val Split, Value: 4,800 / 890.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Attribute: Pest Classes, Value: 15.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Attribute: Total Bounding Boxes, Value: 32,450.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Attribute: Small Targets ( < 32 2 pixels) Ratio, Value: bigger than 70%.
TABLE III ABLATION STUDY OF FORESTPEST-YOLO COMPONENTS

Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Configuration: YOLOv8s (Baseline), mAP .5:.95: 0.482, mAP .5: 0.746, AP small: 0.112.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Configuration: + SPD-Conv, mAP .5:.95: 0.491, mAP .5: 0.75, AP small: 0.119.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Configuration: + SPD-Conv + CSPOK, mAP .5:.95: 0.499, mAP .5: 0.753, AP small: 0.126.
Según Forestpest-YOLO: A High-Performance Detection Framework for Small Forestry Pests (2025), Configuration: + VFL (Full Model), mAP .5:.95: 0.508, mAP .5: 0.762, AP small: 0.131.
for small object feature preservation. Building on this, the addition of the CSPOK module further boosted performance, validating its superior multi-scale fusion capabilities. The final integration of VFL provided an additional lift across all metrics, culminating in our full Forestpest-YOLO model, which achieved the highest scores. This step-by-step analysis validates that our modifications work synergistically.

## V. DISCUSSION

## A. Analysis of Method Effectiveness

Our method's success stems from its targeted design for forestry scenarios. SPD-Conv preserves critical high-frequency details. CSPOK simultaneously processes fine-grained local features and broader context. VarifocalLoss ensures training focuses on informative and challenging samples rather than being dominated by easy background examples.

## B. Limitations and Future Work

Despite the significant progress, our model has limitations. Performance may decline under extreme weather. Its reliance on supervised learning requires large annotated datasets. Future work will explore multimodal data fusion, semisupervised learning, and integrating lightweight Transformerbased decoders.

## VI. CONCLUSION

This paper introduced Forestpest-YOLO, a framework specifically engineered to overcome the critical challenges in forestry pest detection. By synergistically integrating SPDConv, the CSPOK module, and VarifocalLoss, our approach achieves a new state-of-the-art on the challenging ForestPest benchmark. These advancements not only provide a powerful and practical tool for solving real-world problems in remote sensing but also offer valuable insights for designing future intelligent and robust visual detection systems.

## ACKNOWLEDGMENT

This research was funded by the Young Innovative Talents Project of Colleges and Universities in Guangdong Province (2021KQNCX092); the Doctoral Program of Huizhou University (2020JB028); and the Outstanding Youth Cultivation Project of Huizhou University (HZU202009).

## REFERENCES

- [1] Q. Li, W. Li, X. Zheng, J. Zhou, W. Zhong, X. Chen, and C. Long, 'Gre 2-mdcl: Graph representation embedding enhanced via multidimensional contrastive learning,' IEEE Access , 2025.
- [2] F. Zheng, Q. Li, W. Li, X. Chen, Y. Dong, G. Huang, C.-M. Pun, and S. Zhou, 'Lagrange duality and compound multi-attention transformer for semi-supervised medical image segmentation,' arXiv preprint arXiv:2409.07793 , 2024.
- [3] G. Jocher, A. Chaurasia, and J. Qiu, 'Yolo by ultralytics,' https://github. com/ultralytics/ultralytics, 2023, online; accessed [Date of access].
- [4] T. L. Raja Sunkara, 'No more strided convolutions or pooling: A new cnn building block for low-resolution images and small objects,' in European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD) , 2022.
- [5] Y. Cui, W. Ren, and A. Knoll, 'Omni-kernel network for image restoration,' in Proceedings of the AAAI conference on artificial intelligence , vol. 38, no. 2, 2024, pp. 1426-1434.
- [6] H. Zhang, Y. Wang, F. Dayoub, and N. S¨ underhauf, 'Varifocalnet: An iou-aware dense object detector,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2021, pp. 8514-8523.
- [7] Z. Le, Q. Li, H. Chen, S. Cai, X. Xiong, and L. Huang, 'Medical image encryption system based on a simultaneous permutation and diffusion framework utilizing a new chaotic map,' Physica Scripta , vol. 99, no. 5, p. 055249, 2024.
- [8] J. Xu, K. Liu, Q. Huang, Q. Li, and L. Huang, 'A plaintext-related and ciphertext feedback mechanism for medical image encryption based on a new one-dimensional chaotic system,' Physica Scripta , vol. 99, no. 12, p. 125220, 2024.
- [9] Q. Li, Q. Li, B. W.-K. Ling, C.-M. Pun, G. Huang, X. Yuan, G. Zhong, S. Ayouni, and J. Chen, 'Dppad-ie: Dynamic polyhedra permutating and arnold diffusing medical image encryption using 2d cross gaussian hyperchaotic map,' IEEE Transactions on Consumer Electronics , 2025.
- [10] G. Zhong, Y. Chu, Q. Li, T. Wang, and S. Xu, 'Image encryption based on 2d-cphm hyperchaotic map using cross-plane grouping permutation and cipher diffusion: G. zhong et al.' Nonlinear Dynamics , pp. 1-36, 2025.
- [11] X. Chen, M. K.-P. Ng, K.-F. Tsang, C.-M. Pun, and S. Wang, 'Connectomediffuser: Generative ai enables brain network construction from diffusion tensor imaging,' arxiv , 2025.
- [12] X. Chen, Z. Li, Y. Shen, M. Mahmud, H. Pham, C.-M. Pun, and S. Wang, 'High-fidelity functional ultrasound reconstruction via a visual autoregressive framework,' arxiv , 2025.
- [13] M. Li, H. Sun, Y. Lei, X. Zhang, Y. Dong, Y. Zhou, Z. Li, and X. Chen, 'High-fidelity document stain removal via a large-scale realworld dataset and a memory-augmented transformer,' in WACV , 2025, pp. 7614-7624.
- [14] Z. Zhou, Y. Lei, X. Chen, S. Luo, W. Zhang, C.-M. Pun, and Z. Wang, 'Docdeshadower: Frequency-aware transformer for document shadow removal,' in SMC , 2024, pp. 2468-2473.
- [15] X. Guo, S. Luo, Y. Dong, Z. Liang, Z. Li, X. Zhang, and X. Chen, 'An asymmetric calibrated transformer network for underwater image restoration,' The Visual Computer , pp. 6465-6477, 2025.
- [16] X. Guo, Y. Dong, X. Chen, W. Chen, Z. Li, F. Zheng, and C.-M. Pun, 'Underwater image restoration via polymorphic large kernel cnns,' in ICASSP , 2025, pp. 1-5.
- [17] X. Guo, X. Chen, S. Wang, and C.-M. Pun, 'Underwater image restoration through a prior guided hybrid sense approach and extensive benchmark analysis,' IEEE Transactions on Circuits and Systems for Video Technology , vol. 35, no. 5, pp. 4784-4800, 2025.
- [18] F. Yi, Z. Zheng, Z. Liang, Y. Dong, X. Fang, W. Wu, and X. Chen, 'Maclookup: Multi-axis conditional lookup model for underwater image enhancement,' arXiv , 2025.
- [19] X. Zhang, F. Chen, C. Wang, M. Tao, and G.-P. Jiang, 'Sienet: Siamese expansion network for image extrapolation,' SPL , vol. 27, pp. 15901594, 2020.
- [20] X. Zhang, Y. Zhao, C. Gu, C. Lu, and S. Zhu, 'Spa-former: An effective and lightweight transformer for image shadow removal,' in IJCNN , 2023, pp. 1-8.
- [21] Z. Xu, X. Zhang, W. Chen, J. Liu, T. Xu, and Z. Wang, 'Muraldiff: Diffusion for ancient murals restoration on large-scale pre-training,' TETCI , 2024.
- [22] X. Zhang, Z. Xu, H. Tang, C. Gu, S. Zhu, and X. Guan, 'Shadclips: When parameter-efficient fine-tuning with multimodal meets shadow removal,' 2024.
- [23] X. Zhang, C. Shen, X. Yuan, S. Yan, L. Xie, W. Wang, C. Gu, H. Tang, and J. Ye, 'From redundancy to relevance: Enhancing explainability in multimodal large language models,' arXiv , 2024.
- [24] J. Wei and X. Zhang, 'Dopra: Decoding over-accumulation penalization and re-allocation in specific weighting layer,' arXiv , 2024.
- [25] X. Yuan, C. Shen, S. Yan, X. Zhang, L. Xie, W. Wang, R. Guan, Y. Wang, and J. Ye, 'Instance-adaptive zero-shot chain-of-thought prompting,' arXiv , 2024.
- [26] X. Zhang, Y. Quan, C. Gu, C. Shen, X. Yuan, S. Yan, H. Cheng, K. Wu, and J. Ye, 'Seeing clearly by layer two: Enhancing attention heads to alleviate hallucination in lvlms,' arXiv , 2024.
- [27] X. Zhang, F. Zeng, and C. Gu, 'Simignore: Exploring and enhancing multimodal large model complex reasoning via similarity computation,' Neural Networks , p. 107059, 2025.
- [28] X. Zhang, F. Zeng, Y. Quan, Z. Hui, and J. Yao, 'Enhancing multimodal large language models complex reason via similarity computation,' AAAI , 2025.
- [29] X. Zhang, Z. Xu, H. Tang, C. Gu, W. Chen, and A. El Saddik, 'Wakeupdarkness: When multimodal meets unsupervised low-light image enhancement,' TOMM , 2025.
- [30] L. Qiu, D. Yu, C. Zhang, and X. Zhang, 'A local-global framework for semantic segmentation of multisource remote sensing images,' Remote Sensing , vol. 15, no. 1, p. 231, 2022.
- [31] L. Qiu, D. Yu, X. Zhang, and C. Zhang, 'Efficient remote-sensing segmentation with generative adversarial transformer,' GRSL , vol. 21, pp. 1-5, 2023.
- [32] H. Li, X. Zhang, and H. Qu, 'Ddfav: Remote sensing large vision language models dataset and evaluation benchmark,' Remote Sensing , vol. 17, no. 4, p. 719, 2025.
- [33] Q. Zhao, X. Zhang, Y. Li, Y. Xing, X. Yuan, F. Tang, S. Fan, X. Chen, X. Zhang, and D. Wang, 'Mca-llava: Manhattan causal attention for reducing hallucination in large vision-language models,' arXiv preprint arXiv:2507.09184 , 2025.
- [34] J. Wang, G. Huang, G. Zhong, X. Yuan, C.-M. Pun, and J. Deng, 'Qgd-net: a lightweight model utilizing pixels of affinity in feature layer for dermoscopic lesion segmentation,' IEEE Journal of Biomedical and Health Informatics , vol. 27, no. 12, pp. 5982-5993, 2023.
- [35] J. Wang, Z. Deng, T. Lin, W. Li, S. Ling, and J. Lin, 'Beyond direct relationships: Exploring multi-order label pair dependencies for

knowledge distillation,' in Proceedings of the 32nd ACM International Conference on Multimedia , 2024, pp. 8527-8535.

- [36] J. Wang, G. Huang, X. Yuan, G. Zhong, T. Lin, C.-M. Pun, and F. Xie, 'The structure-sharing hypergraph reasoning attention module for cnns,' Expert Systems with Applications , vol. 259, p. 125240, 2025.
- [37] F. Wang, N. Luo, and W. Wu, 'Visioncube: 3d-aware vision-language model for multi-step spatial reasoning,' in Proceedings of the Computer Vision and Pattern Recognition Conference , 2025, pp. 3270-3279.
- [38] W. Liu, J. Qian, Z. Yao, X. Jiao, and J. Pan, 'Convolutional two-stream network using multi-facial feature fusion for driver fatigue detection,' Future Internet , vol. 11, no. 5, p. 115, 2019.
- [39] W. Liu, M. Juhas, and Y. Zhang, 'Fine-grained breast cancer classification with bilinear convolutional neural networks (bcnns),' Frontiers in genetics , vol. 11, p. 547327, 2020.
- [40] L. Zhu, W. Liu, X. Chen, Z. Li, X. Chen, Z. Wang, and C.-M. Pun, 'Test-time intensity consistency adaptation for shadow detection,' arXiv , 2024.
- [41] X. Li, G. Huang, L. Cheng, G. Zhong, W. Liu, X. Chen, and M. Cai, 'Cross-domain visual prompting with spatial proximity knowledge distillation for histological image classification,' Journal of Biomedical Informatics , vol. 158, p. 104728, 2024.
- [42] W. Liu, X. Shen, C.-M. Pun, and X. Cun, 'Forgeryttt: Zero-shot image manipulation localization with test-time training,' arXiv , 2024.
- [43] C. Zhang, H. Jiang, W. Liu, J. Li, S. Tang, M. Juhas, and Y. Zhang, 'Correction of out-of-focus microscopic images by deep learning,' Computational and Structural Biotechnology Journal , vol. 20, pp. 19571966, 2022.
- [44] H. Li and C.-M. Pun, 'Monocular robust 3d human localization by global and body-parts depth awareness,' TCSVT , vol. 32, no. 11, pp. 7692-7705, 2022.
- [45] --, 'Cee-net: complementary end-to-end network for 3d human pose generation and estimation,' in AAAI , vol. 37, no. 1, 2023, pp. 13051313.
- [46] H. Li, S. Ge, C. Gao, and H. Gao, 'Few-shot object detection via highand-low resolution representation,' Computers and Electrical Engineering , vol. 104, p. 108438, 2022.
- [47] H. Li, F. Zheng, Y. Liu, J. Xiong, W. Zhang, H. Hu, and H. Gao, 'Adaptive skeleton prompt tuning for cross-dataset 3d human pose estimation,' in ICASSP . IEEE, 2025, pp. 1-5.
- [48] H. Li, C.-M. Pun, F. Xu, L. Pan, R. Zong, H. Gao, and H. Lu, 'A hybrid feature selection algorithm based on a discrete artificial bee colony for parkinson's diagnosis,' ACM Transactions on Internet Technology , vol. 21, no. 3, pp. 1-22, 2021.
- [49] W. Liu, X. Shen, C.-M. Pun, and X. Cun, 'Explicit visual prompting for low-level structure segmentations,' in CVPR , 2023, pp. 19 434-19 445.
- [50] W. Liu, X. Cun, C.-M. Pun, M. Xia, Y. Zhang, and J. Wang, 'Coordfill: Efficient high-resolution image inpainting via parameterized coordinate querying,' in AAAI , vol. 37, no. 2, 2023, pp. 1746-1754.
- [51] F. Zheng, X. Chen, W. Liu, H. Li, Y. Lei, J. He, C.-M. Pun, and S. Zhou, 'Smaformer: Synergistic multi-attention transformer for medical image segmentation,' in BIBM , 2024.
- [52] W. Liu, X. Cun, and C.-M. Pun, 'Dh-gan: Image manipulation localization via a dual homology-aware generative adversarial network,' PR , p. 110658, 2024.
- [53] H. Jiang, S. Li, W. Liu, H. Zheng, J. Liu, and Y. Zhang, 'Geometryaware cell detection with deep learning,' Msystems , vol. 5, no. 1, pp. 10-1128, 2020.
- [54] W. Liu, X. Shen, H. Li, X. Bi, B. Liu, C.-M. Pun, and X. Cun, 'Depthaware test-time training for zero-shot video object segmentation,' in CVPR , 2024, pp. 19 218-19 227.
- [55] H. Cai, W. Wu, B. Chai, and Y. Zhang, 'Relation-fused attention in knowledge graphs for recommendation,' in International Conference on Neural Information Processing . Springer, 2024, pp. 285-299.
- [56] Y. Chen, W. Wu, and J. Li, 'Adaptive attention-enhanced yolo for wall crack detection.' Applied Sciences (2076-3417) , vol. 14, no. 17, 2024.
- [57] W. Wu, X. Qiu, S. Song, Z. Chen, X. Huang, F. Ma, and J. Xiao, 'Image augmentation agent for weakly supervised semantic segmentation,' arXiv preprint arXiv:2412.20439 , 2024.
- [58] W. Wu, Z. Chen, X. Qiu, S. Song, X. Huang, F. Ma, and J. Xiao, 'Llm-enhanced multimodal fusion for cross-domain sequential recommendation,' arXiv preprint arXiv:2506.17966 , 2025.
- [59] W. Wu, S. Song, X. Qiu, X. Huang, F. Ma, and J. Xiao, 'Image fusion for cross-domain sequential recommendation,' in Companion Proceedings of the ACM Web Conference 2025 , 2025.
- [60] W. Wu, X. Qiu, S. Song, Z. Chen, X. Huang, F. Ma, and J. Xiao, 'Prompt categories cluster for weakly supervised semantic segmentation,' in Proceedings of the Computer Vision and Pattern Recognition Conference , 2025, pp. 3198-3207.
- [61] Z. Li, X. Chen, C.-M. Pun, and X. Cun, 'High-resolution document shadow removal via a large-scale real-world dataset and a frequencyaware shadow erasing net,' in ICCV , 2023, pp. 12 449-12 458.
- [62] X. Guo, X. Chen, S. Luo, S. Wang, and C.-M. Pun, 'Dual-hybrid attention network for specular highlight removal,' in ACM MM , 2024, pp. 10 173-10 181.
- [63] X. Chen, B. Lei, C.-M. Pun, and S. Wang, 'Brain diffuser: An end-toend brain image to brain network pipeline,' in PRCV , 2023, pp. 16-26.
- [64] S. Luo, X. Chen, W. Chen, Z. Li, S. Wang, and C.-M. Pun, 'Devignet: High-resolution vignetting removal via a dual aggregated fusion transformer with adaptive channel expansion,' in AAAI , 2024, pp. 40004008.
- [65] Z. Li, X. Chen, S. Wang, and C.-M. Pun, 'A large-scale film style dataset for learning multi-frequency driven film enhancement,' in IJCAI , 2023, pp. 1160-1168.
- [66] X. Chen, C.-M. Pun, and S. Wang, 'Medprompt: Cross-modal prompting for multi-task medical image translation,' in PRCV , 2024, pp. 61-75.
- [67] Z. Li, X. Chen, C.-M. Pun, and X. Cun, 'High-resolution document shadow removal via a large-scale real-world dataset and a frequencyaware shadow erasing net,' in ICCV , 2023, pp. 12 449-12 458.
- [68] K. Tong, Y. Wu, and F. Zhou, 'Recent advances in small object detection based on deep learning: A review,' Image and Vision Computing , vol. 97, p. 103910, 2020.
- [69] T.-Y. Lin, P. Doll´ ar, R. Girshick, K. He, B. Hariharan, and S. Belongie, 'Feature pyramid networks for object detection,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , 2017.
- [70] S. Liu, L. Qi, H. Qin, J. Shi, and J. Jia, 'Path aggregation network for instance segmentation,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , 2018.
- [71] M. Tan, R. Pang, and Q. V. Le, 'Efficientdet: Scalable and efficient object detection,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2020.
- [72] G. Ghiasi, Y. Cui, A. Srinivas, R. Qian, T.-Y. Lin, E. D. Cubuk, Q. V. Le, and B. Zoph, 'Simple copy-paste is a strong data augmentation method for instance segmentation,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2021.
- [73] J. Li, X. Liang, Y. Wei, T. Xu, J. Feng, and S. Yan, 'Perceptual generative adversarial networks for small object detection,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , 2017.
- [74] J.-S. Lim, M. Astrid, H.-J. Yoon, and S.-I. Lee, 'Small object detection using context and attention,' in 2021 international Conference on Artificial intelligence in information and Communication (ICAIIC) . IEEE, 2021, pp. 181-186.
- [75] J. Hu, L. Shen, and G. Sun, 'Squeeze-and-excitation networks,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , 2018.
- [76] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon, 'Cbam: Convolutional block attention module,' in Proceedings of the European Conference on Computer Vision (ECCV) , 2018.
- [77] X. Wang, R. Girshick, A. Gupta, and K. He, 'Non-local neural networks,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , 2018.
- [78] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, 'An image is worth 16x16 words: Transformers for image recognition at scale,' in International Conference on Learning Representations (ICLR) , 2021.
- [79] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kirillov, and S. Zagoruyko, 'End-to-end object detection with transformers,' in Proceedings of the European Conference on Computer Vision (ECCV) , 2020.
- [80] J. Dai, H. Qi, Y . Xiong, Y . Li, G. Zhang, H. Hu, and Y . Wei, 'Deformable convolutional networks,' in Proceedings of the IEEE International Conference on Computer Vision (ICCV) , 2017.
- [81] Y. Chen, X. Dai, M. Liu, D. Chen, L. Yuan, and Z. Liu, 'Dynamic convolution: Attention over convolution kernels,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2020.
- [82] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Doll´ ar, 'Focal loss for dense object detection,' in Proceedings of the IEEE International Conference on Computer Vision (ICCV) , 2017.
- [83] H. Rezatofighi, N. Tsoi, J. Gwak, A. Sadeghian, I. Reid, and S. Savarese, 'Generalized intersection over union: A metric and a loss for bounding box regression,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2019.
- [84] Z. Zheng, P. Wang, W. Liu, J. Li, R. Ye, and D. Ren, 'Distance-iou loss: Faster and better learning for bounding box regression,' in Proceedings of the AAAI Conference on Artificial Intelligence , 2020, pp. 12 99313 000.
- [85] X. Li, W. Wang, L. Wu, S. Chen, X. Hu, J. Li, J. Tang, and J. Yang, 'Generalized focal loss: Learning qualified and distributed bounding boxes for dense object detection,' in Advances in Neural Information Processing Systems (NeurIPS) , 2020, pp. 21 002-21 012.
- [86] S. Zhang, C. Chi, Y. Yao, Z. Lei, and S. Z. Li, 'Bridging the gap between anchor-based and anchor-free detection via adaptive training sample selection,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , 2020.
- [87] Z. Ge, S. Liu, F. Wang, Z. Li, and J. Sun, 'Yolox: Exceeding yolo series in 2021,' arXiv preprint arXiv:2107.08430 , 2021.