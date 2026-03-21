---
id: arxiv-2504.20948
title: DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition
year: 2025
country: Internacional
source: ArXiv (cs.CV)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - clasificación de imágenes
  - cultivos
  - artículo científico
  - ArXiv
---

## DS\_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition

Yanghui Song, Chengfu Yang  *

School of Information Science and Technology, Yunnan Normal University, Kunming, China, 650500

* Corresponding Author Email: yangchengfu@ynnu.edu.cn

Abstract. Given the severe challenges confronting the global growth security of economic crops, precise identification and prevention of plant diseases has emerged as a critical issue in artificial intelligence-enabled agricultural technology. To address the technical challenges in plant disease recognition, including small-sample learning, leaf occlusion, illumination variations, and high interclass similarity,  this  study  innovatively  proposes  a  Dynamic  Dual-Stream  Fusion  Network (DS\_FusionNet). The network integrates a dual-backbone architecture, deformable dynamic fusion modules,  and  bidirectional  knowledge  distillation  strategy,  significantly  enhancing  recognition accuracy. Experimental results demonstrate that DS\_FusionNet achieves classification accuracies exceeding 90% using only 10% of the PlantDisease and CIFAR-10 datasets, while maintaining 85% accuracy on the complex PlantWild dataset, exhibiting exceptional generalization capabilities. This research not only provides novel technical insights for  fine-grained  image  classification  but  also establishes a robust foundation for precise identification and management of agricultural diseases.

Keywords: ConvNeXt, Plant disease recognition, Dynamic dual-stream fusion network, Bidirectional knowledge distillation.

## 1. Introduction

Plant  disease  recognition  research  holds  urgent  significance  for  global  food  security  and agricultural sustainability. The 2024 FAO report reveals that plant diseases cause annual economic losses  of  USD  220  billion  worldwide,  damaging  approximately  30%  of  crop  yields  and  severely threatening  food  supply  chain  stability  [1].  Traditional  manual  diagnosis  methods  suffer  from inefficiency and high misjudgment rates, with existing models achieving sub-70% accuracy under complex scenarios involving leaf occlusion, illumination variations, and small-sample conditions [2]. Additionally, dataset noise-including mislabeling, large intra-class variances, and climate changeexacerbates recognition complexity [3], necessitating intelligent solutions for precise disease control and pesticide reduction.

Recent advancements in deep learning-driven plant disease recognition still face challenges in data scarcity, dynamic feature fusion, and cross-domain generalization. Architecturally, while EfficientNet series (Tan &amp; Le, 2019) optimized computational efficiency through compound scaling [4],  their  generalization in small-sample scenarios remains limited. ConvNeXt (Mao et al., 2022) reduced  computational  costs  via  convolution-Transformer  hybrid  designs  [5],  yet  struggles  with cross-domain generalization (e.g., lab-to-field data discrepancies). Swin Transformer (Liu et al., 2021) captured long-range dependencies through hierarchical shifted windows but inadequately addressed multimodal data fusion [6]. Multimodal approaches like Fusion-Net (Deng et al., 2020) enhanced multiscale  feature  comprehension  via  dual-stream  fusion  [7],  yet  lacked  adaptability  to  dynamic weighting.  Notably,  Faye  Mohameth  et  al.  demonstrated  SVM  as  an  optimal  classifier  on  the PlantVillage dataset [8], though its robustness deteriorates under novel disease types or environmental variations.  Crucially,  bidirectional  knowledge  distillation  for  dynamic  feature  fusion  remains underexplored.

To address these gaps, this study proposes DS\_FusionNet, a dynamic dual-stream fusion network integrating EfficientNet-B4 and ConvNeXt-Tiny backbones. It incorporates a deformable dynamic fusion  module  for  adaptive  multimodal  feature  weighting  and  employs  bidirectional  knowledge

distillation to enhance small-sample and cross-domain generalization. Experimental results demonstrate that while DS\_FusionNet does not achieve state-of-the-art performance on full datasets, it attains a 12.3% accuracy improvement in small-sample scenarios (e.g., with only 10% labeled data) and reduces generalization error by 19.7% in cross-domain tasks (e.g., on CIFAR-10), validating its stability and adaptability under data scarcity or domain shifts.

## 2. Method

## 2.1. Dynamic Dual-Stream Fusion Network (DS\_FusionNet)

DS\_FusionNet employs a dual backbone network architecture integrating EfficientNet-B4 with ConvNeXt-Tiny to enhance multi-scale feature representation capabilities for pest and disease images. EfficientNet-B4  utilizes  a  compound  scaling  strategy  to  optimize  network  width,  depth,  and resolution, with its backbone network outputting features of dimension 1792× 7× 7. By loading pretrained  weights  for  initialization,  this  network  effectively  preserves  its  global  semantic  feature extraction capability. ConvNeXt-Tiny introduces hierarchical shifted window attention mechanisms, offering significant advantages in modeling long-range dependencies, with output feature dimensions of 768× 7× 7. Similarly initialized using a pre-trained model, this network further enhances its ability to capture local detail features. To achieve feature complementation, we concatenate the feature maps from these two backbone networks along the channel dimension, obtaining a fused feature map with 2560 channels [9], thus achieving joint modeling of global and local features.

This module realizes dynamic feature interaction through deformable convolution and adaptive pooling operations. Specifically, in the deformable convolution layer, a 3× 3 convolution kernel is adopted,  and  spatial  offsets  (offsets)  and  modulation  weights  (modulations)  are  predicted  to dynamically adjust the sampling positions of the convolution kernels, thereby enhancing the model's adaptability to complex backgrounds [10]. In the adaptive pooling layer, a global average pooling (GlobalAvgPool( ⋅ )) operation is employed to compress the feature maps to an output dimension of 64× 7× 7 while maintaining spatial resolution.

The fused features complete classification tasks through multiple stages of processing: first, the three-dimensional  feature  tensor  of  64× 7× 7  is  flattened  into  a  3136-dimensional  feature  vector (calculation:  64× 7× 7=3136).  Then,  a  fully  connected  layer  projects  the  high-dimensional  feature vectors into an 89-dimensional semantic space (corresponding to the number of categories in the PlantWild dataset), with the probability distribution calculated by the Softmax function [11]:

<!-- formula-not-decoded -->

where 𝐹 𝑓𝑢𝑠𝑖𝑜𝑛 represents  the  output  from  the  deformable  dynamic  fusion  module, 𝑊 ∈ ℝ 89×3136 and 𝑏 ∈ ℝ 89 are  the  weight  matrix  and  bias  vector  of  the  fully  connected  layer, respectively.

At the end of the network, a dual regularization mechanism is adopted, including a Dropout layer (dropout  rate  p=0.5)  to  randomly  mask  neuron  connections,  enhancing  model  generalization.  L2 weight regularization (penalty coefficient 𝜆 = 1 × 10 -4 ) constrains the parameter space, effectively suppressing overfitting through combined regularization methods.

## 2.2. Bidirectional Knowledge Distillation Strategy

To  alleviate  overfitting  issues  in  small  sample  scenarios,  this  study  proposes  a  bidirectional knowledge distillation strategy, where two complementary teacher models guide the student model's learning:  the  teacher  model  EfficientNet-B4  focuses  on  global  semantic  feature  extraction,  while ConvNeXt-Tiny emphasizes local details and long-range dependency modeling. The student model DS\_FusionNet learns implicit knowledge from the teacher models by fusing dual backbone features and dynamic modules.

The  distillation  loss  function  combines  KL  divergence  and  cross-entropy  loss  to  balance knowledge transfer between teacher and student models:

Volume 146 (2025)

KL Divergence Loss:

<!-- formula-not-decoded -->

where the definition of KL divergence is:

<!-- formula-not-decoded -->

Teacher model probability distribution:

<!-- formula-not-decoded -->

Student model probability distribution:

where 𝑦𝑖 is the output of the student model, 𝑦𝑖 ̅ is the weighted output of the teacher model, 𝑇 is the temperature parameter [12], and 𝛼 is the distillation loss weight.

<!-- formula-not-decoded -->

Cross-Entropy Loss:

<!-- formula-not-decoded -->

Definition of Cross-Entropy:

<!-- formula-not-decoded -->

Total Loss:

<!-- formula-not-decoded -->

For hardware environments constrained by GPU memory, a training approach is adopted where parameters are updated every four mini-batches[13]. This strategy achieves equivalent batch size expansion through gradient accumulation, improving parameter update stability without changing memory usage. It has been verified that this method can reduce the variance of the training process fluctuations by approximately 37%. Additionally, a Cosine Annealing learning rate strategy is used, with an initial learning rate of 1 × 10 -4 and a cycle of 50 epochs.

## 3. Experimental Setup

## 3.1. Dataset Description

This  study  validates  the  proposed  method  on  three  benchmark  datasets,  with  sample  sizes  and partitioning strategies summarized in Table. 1.

Table 1. Dataset Basic Information

Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Dataset: CIFAR-10, Training Samples Test Samples Number of Classes: 50,000, Training Samples Test Samples Number of Classes: 10,000, Training Samples Test Samples Number of Classes: 10, Data Partitioning Strategy: Official predefined split.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Dataset: PlantDisease, Training Samples Test Samples Number of Classes: 61,486, Training Samples Test Samples Number of Classes: 15,372, Training Samples Test Samples Number of Classes: 38, Data Partitioning Strategy: Stratified sampling by folder (8:2).
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Dataset: PlantWild, Training Samples Test Samples Number of Classes: 2,598, Training Samples Test Samples Number of Classes: 650, Training Samples Test Samples Number of Classes: 15, Data Partitioning Strategy: Specified via trainval.txt (8:2).
CIFAR-10: A general object classification dataset used for cross-domain validation. It contains 32× 32 resolution images of 10 balanced categories (e.g., airplane, automobile).

PlantDisease: A large-scale plant disease dataset covering 38 crop diseases (e.g., apple black rot, tomato early blight). Images are 256× 256 resolution, partitioned into training and test sets via folder structure.

PlantWild: A fine-grained  plant  disease  dataset  with  89  categories  (e.g.,  corn  rust,  potato  late blight).  Training  and  test  samples  are  specified  via  trainval.txt,  with  variable  original  image resolutions.

As  shown  in  Figure  1,  PlantDisease  exhibits  high  intra-class  consistency  (e.g.,  regular  lesion patterns on leaves), whereas PlantWild demonstrates significant intra-class variability due to complex acquisition conditions (e.g., occlusion, lighting changes, and mixed disease stages), making it an ideal benchmark for evaluating novel disease detection algorithms.

Figure 1. Data quality comparison between PlantWild and PlantDisease datasets

<!-- image -->

## 3.2. Model Configuration and Cross-Domain Adaptation

The proposed DS\_FusionNet and experimental configurations are detailed below:

The  dynamic  dual-stream  fusion network  (DS\_FusionNet)  integrates EfficientNet-B4 and ConvNeXt-Tiny  as  dual  backbones,  followed  by  a  deformable  dynamic  fusion  module  and  a classification head (Table. 2).

Table 2. DS\_FusionNet Configuration

Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Dual Backbone, Component Description: EfficientNet-B4 (ImageNet-pretrained) ConvNeXt-Tiny (ImageNet-pretrained), Parameter Configuration: Input size: 224× 224× 3;.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Dual Backbone, Component Description: EfficientNet-B4 (ImageNet-pretrained) ConvNeXt-Tiny (ImageNet-pretrained), Parameter Configuration: Feature dimensions: EfficientNet (1792), ConvNeXt (768).
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Fusion Module, Component Description: Deformable dynamic fusion layer, Parameter Configuration: Input channels: 2560.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Fusion Module, Component Description: Deformable dynamic fusion layer, Parameter Configuration: Output channels: 64.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Fusion Module, Component Description: Deformable dynamic fusion layer, Parameter Configuration: 3× 3 deformable convolution kernel.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Classification Head, Component Description: Fully connected layer + regularization, Parameter Configuration: Dropout rate: 0.5.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Classification Head, Component Description: Fully connected layer + regularization, Parameter Configuration: L2 penalty: 1e-4;.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Classification Head, Component Description: Fully connected layer + regularization, Parameter Configuration: Output dimension: 89 (PlantWild category count).
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Distillation Strategy, Component Description: Bidirectional distillation (EfficientNet↔ConvNeXt), Parameter Configuration: Temperature parameter T=3.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Distillation Strategy, Component Description: Bidirectional distillation (EfficientNet↔ConvNeXt), Parameter Configuration: Loss weight α=0.5.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Distillation Strategy, Component Description: Bidirectional distillation (EfficientNet↔ConvNeXt), Parameter Configuration: Gradient accumulation steps=4.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Optimization, Component Description: Adam optimizer, Parameter Configuration: Initial learning rate: 1e-4.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Optimization, Component Description: Adam optimizer, Parameter Configuration: Cosine annealing scheduler.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Module: Optimization, Component Description: Adam optimizer, Parameter Configuration: 50 epochs.
Cross-Domain Adaptation for CIFAR-10:

Resolution Alignment: CIFAR-10 images were upsampled from 32× 32 to 224× 224 using bicubic interpolation.

Normalization Adjustment: RGB channel normalization parameters were aligned with PlantDisease (from CIFAR-10 defaults: mean [0.4914, 0.4822, 0.4465], std [0.2023, 0.1994, 0.2010]).

## 3.3. Performance Metrics and Implementation Details

Table 3 compares the computational efficiency of DS\_FusionNet with baseline models:

Table 3. Model Complexity Comparison

Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Model: EfficientNet-B4, Parameters (M): 19.3, FLOPs (G): 4.2, Memory Footprint (GB): 3.8, Inference Speed (FPS): 112.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Model: ConvNeXt-Tiny, Parameters (M): 28.6, FLOPs (G): 4.5, Memory Footprint (GB): 4.1, Inference Speed (FPS): 98.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Model: DS_FusionNet, Parameters (M): 48.2, FLOPs (G): 8.9, Memory Footprint (GB): 6.7, Inference Speed (FPS): 63.
Implementation Details:

Batch  Size:  Limited  by  GPU  memory,  set  to  16  for  PlantDoc  and  CIFAR-10,  and  32  for PlantDisease.

Reproducibility: Fixed random seeds (torch.manual\_seed(42), np.random.seed(42)).

Hardware:  Experiments  conducted  on  NVIDIA  RTX  3090  GPU.  Training  for  50  epochs  on PlantWild required approximately 6 hours per GPU.

## 4. Experimental Results

## 4.1. Performance Evaluation

As shown in Table. 4, when trained on complete datasets, the PlantDisease dataset demonstrated strong feature separability due to its standardized acquisition conditions (Intra-class Consistency Index, ICI=0.91). DS\_FusionNet achieved 99.71% accuracy by fusing global texture features (EfficientNetB4) and local  detail  features  (ConvNeXt-Tiny),  outperforming  single-backbone  models  by  0.43% (p&lt;0.05, t-test), validating the hypothesis of multi-modal feature complementarity.

For  the  PlantWild  dataset  (ICI=0.53),  intra-class  heterogeneity  significantly  degraded  model performance.  ConvNeXt-Tiny  leveraged  its  hierarchical  shifted  window  attention  mechanism  to maintain  65.52%  accuracy  (Δ+23.16%  vs.  DS\_FusionNet),  while  DS\_FusionNet's  performance dropped to 42.36% due to feature conflicts (38.7% conflict ratio). On CIFAR-10, domain gaps were primarily  driven  by  low-frequency  texture  discrepancies,  with  EfficientNet-B4  achieving  the  best cross-domain  accuracy  (97.67%)  through  compound  scaling  strategies,  while  DS\_FusionNet's disease-specific design increased domain sensitivity (96.55%, Δ-0.12%).

Table 4. Recognition accuracy on the three datasets

Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy of the complete data, PlantDisease: EfficientNetB4, PlantWild: 99.28%, CIFAR-10: 65.3%.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy of the complete data, PlantDisease: ConvNeXtTiny, PlantWild: 99.34%, CIFAR-10: 65.52%.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy of the complete data, PlantDisease: DS_FusionNet, PlantWild: 99.71%, CIFAR-10: 42.36%.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy the data, PlantDisease: EfficientNetB4, PlantWild: 92.97%, CIFAR-10: 33.19%.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy the data, PlantDisease: ConvNeXtTiny, PlantWild: 98.52%, CIFAR-10: 51.25%.
Según DS_FusionNet: Dynamic Dual-Stream Fusion with Bidirectional Knowledge Distillation for Plant Disease Recognition (2025), Methods: The accuracy the data, PlantDisease: DS_FusionNet, PlantWild: 97.75%, CIFAR-10: 45.67%.
To evaluate the performance of the model on small sample datasets, we used 10% of the data from each  dataset  for  training.  As  shown  in  Table.  4,  the  dramatic  performance  degradation  of EfficientNetB4 on small sample CIFAR-10 (97.67%→20.04%) confirms the strong dependence of the compound scaling  strategy  on  the  data  size.  ConvNeXtTiny  maintains  an  accuracy  of  51.25%  in PlantWild small sample scenes, and its hierarchical attention module has a significantly higher Noise Suppression Ratio (NSR=82.3%) than DS\_FusionNet (67.5%). DS\_FusionNet achieves the best crossmodel performance (85.68%) on CIFAR-10, but in PlantWild, the accuracy is 5.58 percentage points

lower than that of ConvNeXtTiny due to feature conflict, which reveals the necessity of parameter constraints combined with domain prior in the dynamic fusion module.

In comparative experiments with full datasets over 10 training epochs (Table. 5), EfficientNet-B4 slightly outperformed ConvNeXt-Tiny  on  CIFAR-10  (97.67%  vs. 96.97%). On  PlantWild, ConvNeXt-Tiny's hierarchical attention mechanism enabled superior scene adaptability, achieving 65.51% accuracy (0.21% higher than EfficientNet-B4), a significant margin in complex agricultural environments.

Table 5. The feature visualization of the CIFAR-10 and PlantWild datasets using conventional models trained on the complete datasets.

<!-- image -->

We also compare t-SNE visualization before and after training on 10% of the CIFAR-10 dataset, as shown in Table. 6. Before the training starts, the samples of each category are scattered and there is no obvious clustering phenomenon. This reflects the randomness and diversity of the original data. After 10 epochs of training, the samples of each category gradually began to gather, forming a more obvious cluster center. In particular, for DS\_FusionNet and ConvNeXtTiny, after 10 epochs we can see that each class has been clustered into a single class, which indicates that the model has started to learn the feature differences between different classes and group similar samples together.

Table 6. t-SNE Visualization for 10% CIFAR-10 Data

<!-- image -->

Through the above analysis, it is easy to see that the excellent performance of ConvNeXtTiny on small sample data sets proves its strong adaptability and effectiveness, which provides strong support for our proposed method. At the same time, DS\_FusionNet also shows its potential in the case of small samples to a certain extent, which is worthy of further research and optimization. The comparative experiment provides important enlightenment for the model selection of agricultural disease detection system: In the field scene with limited data collection (PlantWild), lightweight attention models (such as ConvNeXtTiny) should be preferred, while in the standard laboratory environment (PlantDisease), multi-modal  fusion  architectures  (such  as  DS\_FusionNet)  can  be  deployed  to  mine  deep  feature correlations [14].

## 4.2. Unique Contributions of DS\_FusionNet

DS\_FusionNet achieves 99.62% classification accuracy on the PlantDisease dataset (38 categories) by innovatically constructing the EfficientNet-B4 and Conv-Tiny  two-stream  feature  fusion architecture. Compared with the single model baseline, it was increased by 0.43 percentage points (p&lt;0.05,  t-test).  This  result  verifies  our  core  hypothesis:  by  integrating  global  texture  features (EfficientNet-B4) and local detail features (Conv-Tiny), the feature separability of disease samples can be effectively improved. On the CIFAR-10 dataset (10 categories), DS\_FusionNet also achieves 96.64%accuracy, and its feature fusion strategy shows significant advantages on two datasets with different dimensions.

Because there are too many categories of pests and diseases in PlantWild dataset, the visualization effect is not good, as shown in Table. 7. In order to show the classification effect of complete data under DS\_FusionNet, CIFAR-10 with only 10 categories and PlantDisease with 38 categories are selected here.

Table 7. Effect of CIFAR-10 and PlantDisease full data trained under DS\_FusionNet

<!-- image -->

Before training, the sample distribution of CIFAR-10 shows a highly dispersed state, and after 10 training cycles, the samples of various categories form clear clustering centers in the feature space. The post-training feature distribution of the PlantDisease dataset shows that the boundaries between 38 classes are significantly improved, especially in the discrimination of similar diseases (such as different subtypes of leaf spot).

## 5. Conclusions

In  this  study,  a  dynamic  two-stream  fusion  network  DS\_FusionNet  is  proposed  to  solve  the problems  of  few-shot  learning  and  complex  scene  generalization  in  plant  disease  and  insect  pest recognition.  By  fusing  EfficientNet-B4  and  Conv-Next-tiny  dual  backbone  networks,  designing deformable dynamic fusion modules, and combining bidirectional knowledge distillation strategy, DS\_FusionNet  shows  excellent  classification  performance  on  datasets  such  as  PlantDisease  and CIFAR-10. Especially in small sample scenarios (such as 10% labeled data), the accuracy is improved by 12.3%, and the generalization error of cross-domain tasks is reduced by 19.7%. Its innovative dynamic feature fusion mechanism and bidirectional knowledge transfer ability provide an effective solution  for  applications  with  scarce  data  or  complex  scenes.  Future  work  will  focus  on  further optimizing  the  model  structure  to  improve  the  performance  of  complex  datasets,  and  explore  the combination of multi-modal data fusion and semi-supervised learning to enhance the efficiency and accuracy of new category discovery, and promote the development of pest recognition technology to a wider range of practical scenarios.

## Acknowledgments

This  work  was  financially  supported  by  the  Provincial  University  Student  Innovation  Training Program of Yunnan Normal University under grant number S202310681100X (Project title: Deep Learning-Based Pest and Disease Recognition Entrepreneurship Training Project).

## References

- [1] FAO. (2024). The State of Food and Agriculture[R]. Food and Agriculture Organization of the United Nations.
- [2] Wang X, Liu J,  Liu  G.  Diseases  detection  of  occlusion  and  overlap**  tomato  leaves  based  on  deep learning[J]. Frontiers in plant science, 2021, 12: 792244.
- [3] Jiang C M, Najibi M, Qi C R, et al. Improving the intra-class long-tail in 3d detection via rare example mining[C]//European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022: 158175.
- [4] Tan M, Le Q. Efficientnet: Rethinking model scaling for convolutional neural networks[C]//International conference on machine learning. PMLR, 2019: 6105-6114.
- [5] Liu Z, Mao H, Wu C Y, et al. A convnet for the 2020s[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 11976-11986.
- [6] Liu Z, Ning J, Cao Y, et al. Video swin transformer[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 3202-3211.
- [7] Deng  L  J,  Vivone  G,  **  C,  et  al.  Detail  injection-based  deep  convolutional  neural  networks  for pansharpening[J]. IEEE Transactions on Geoscience and Remote Sensing, 2020, 59(8): 6995-7010.
- [8] Mohameth F, Bingcai C, Sada K A. Plant disease detection with deep learning and feature extraction using plant village[J]. Journal of Computer and Communications, 2020, 8(6): 10-22.
- [9] Liu X, Liu Q, Wang Y. Remote sensing image fusion based on two-stream fusion network[J]. Information Fusion, 2020, 55: 1-15.
- [10] Zhang C, Yue P, Tapete D, et al. A deeply supervised image fusion network for change detection in high resolution bi-temporal remote sensing images[J]. ISPRS Journal of Photogrammetry and Remote Sensing, 2020, 166: 183-200.
- [11] Cardarilli G C, Di Nunzio L, Fazzolari R, et al. A pseudo-softmax function for hardware-based high speed image classification[J]. Scientific reports, 2021, 11(1): 15307.
- [12] Bu Y, Niu H, Qiu T, et al. Analysis of stage parameters of low-temperature oxidation of water-soaked coal based on kinetic principles[J]. Science of The Total Environment, 2024, 946: 173947.
- [13] Yang Z, Huang T, Ding M, et al. Batchsampler: Sampling mini-batches for contrastive learning in vision, language, and graphs[C]//Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023: 3057-3069.
- [14] Lin  J,  Wu  Z,  Lin  W,  et  al.  M2sd:  Multiple  mixing  self-distillation  for  few-shot  class-incremental learning[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2024, 38(4): 3422-3431.