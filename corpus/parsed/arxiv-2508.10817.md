---
id: arxiv-2508.10817
title: Mobile-Friendly Deep Learning for Plant Disease Detection: A Lightweight CNN Benchmark Across 101 Classes of 33 Crops
year: 2025
country: Internacional
source: ArXiv (cs.CV, cs.LG)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - deep learning
  - clasificación de imágenes
  - cultivos
  - visión por computadora
  - dispositivos móviles
  - artículo científico
  - ArXiv
---

## Mobile-Friendly Deep Learning for Plant Disease Detection: A Lightweight CNN Benchmark Across 101 Classes of 33 Crops

Anand Kumar¹, Harminder Pal Monga¹, Tapasi Brahma², Satyam Kalra³, Navas Sherif ⁴

¹Indian Institute of Technology Patna, ²Columbia University, ³The George Washington University, ⁴ Amity University anand\_24a03res117@iitp.ac.in, harminder\_24a03res132@iitp.ac.in, tb3001@columbia.edu, skalra@gwu.edu, navassherif@amityonline.com

Abstract : Plant  diseases  are  a  major  threat  to  food  security  globally.  It  is  important  to  develop  early  detection systems which can accurately detect. The advancement in computer vision techniques has the potential to solve this challenge. We have developed a mobile-friendly solution which can accurately classify 101 plant diseases across 33 crops.    We built a comprehensive dataset by combining different datasets, Plant Doc, PlantVillage, and PlantWild, all  of  which  are  for  the  same  purpose.  We  evaluated  performance  across  several  lightweight  architectures  MobileNetV2, MobileNetV3, MobileNetV3-Large, and EfficientNet-B0, B1 - specifically chosen for their efficiency on resource-constrained devices. The results were promising, with EfficientNet-B1 delivering our best performance at  94.7%  classification  accuracy. This architecture struck an optimal balance between accuracy and computational efficiency, making it well-suited for real-world deployment on mobile devices.

## 1 Introduction

The global demand for food is increasing, with estimates that the world will need 50 per cent more food by 2050 to feed  the  increasing  global  population  in  the  context  of  natural  resource  constraints,  environmental  pollution, ecological  degradation  and  climate change.   Reducing crop loss due to disease can significantly help in achieving this target, as the crop loss accounts for roughly 14.1% of annual crop loss worldwide. [1].  Plant diagnosticians are not always available to provide assessment promptly, leading to potentially costly delays. Further, plant pathologists are  often  skilled  at  recognising  a  limited  number  of  plant  diseases  on  a  handful  of  hosts,  thus  multiple  plant pathologists or taxonomists are usually required for a reliable diagnosis. [2].

The advancement in computer vision techniques now offers high-quality object detection systems. It is also noted  92%  of  farmers  in the United States have cellphones, with over 90% of farm operations using smartphones within  field  operations.  [3].  In  developing  countries  like  India,  the  number  is  less,  having  75-80%  of  farmer households having smartphone access, with Gujarat at 90% and Punjab/Haryana at 70% [4].

Farmers  in  the  remote  areas  frequently  face  the  problem  of  low  internet  speed,  and  sometimes it is not available. A Smartphone-based local computer vision model application not only helps farmers it also reduces image processing  cost,  faster  inference  time,  etc.  There  has  been  good  progress  in  mobile-based  vision  models  and previously have been applied in successfully applied in various sectors. Previous studies have used different models for plant disease detection. Sharada Prasanna Mohanty et al [30] used AlexNet and GoogleNet [31] and achieved an accuracy of 99.35% for 14 crops using 60 million parameters. Jun et al achieved 95.94 % accuracy using MobileNet for 64 different classes of 22 different sets of crops. In this study, we are classifying 101 classes for 33 crops, which has not been done by previous studies on this scale.

## 1.1 Mobile Optimised Computer Vision Models

Mobile Convolutional Networks: Key mobile convolution networks include MobileNetV1 [5] with depthwise-separable convolutions for better efficiency, MobileNetV2 [6] introduced linear bottlenecks and inverted residuals, GhostNet [7], increasing the relative frequency of depthwise convolutions, and MobileOne [8], adding and reparameterizes linear branches in inverted bottlenecks at inference time.

Efficient  Hybrid  Networks :  This  research  combines  convolutions  and  attention.  MobileViT [9] merges CNN strengths with ViT [10] through global attention blocks. GhostNetV2 [11] uses FC layers to capture long-range dependencies.  FastViT  [12]  adds  attention  to  the last stage with large convolutional kernels instead of early-stage self-attention.

Efficient Attention: EfficientViT [13] and MobileViTv2 [14] introduce self-attention approximations for linear complexity with minor accuracy impacts. EfficientFormerV2 [15] downsamples Q, K, and V for efficiency..

Hardware-aware  Neural  Architecture  Search  (NAS): Another  common technique  is  to  automate  the model  design  process  using  hardware-aware  Neural  Architecture  Search  (NAS).  NetAdapt  [16]  uses  empirical latency tables to optimise the accuracy of a model under a target latency constraint. MnasNet [17] also uses latency tables, but applies reinforcement learning to do hardware-aware NAS. MobileNetV3 [18] is tuned to mobile phone CPUs  through  a  combination  of  hardware-aware  NAS,  the  NetAdapt  algorithm,  and  architecture  advances. MobileNet MultiHardware [19] optimises  a  single model for multiple hardware targets. EfficientNet[20] (B0-B7) was designed using MnasNet-like hardware-aware NA S to find the optimal baseline network (EfficientNet-B0) for mobile  accelerators.  Then  it  applied  the compound  scaling rule  to  systematically  scale depth,  width,  and resolution for other variants (B1-B7).

Various  comprehensive  studies  have  been  done  to  test  these  mobile-compatible  vision  models  across different hardware phones. [Table 1] shows the comparison of different models and their performance on different phones taken from earlier studies [26], [20].

Table  1: Classification  results  on  ImageNet-1K  [27],  along  with  on-device  benchmarks.  Median  latency  is  reported.  A  indicates that we did not benchmark a model due to a missing corresponding model file for a platform. Failed indicates that the model is not supported by the platform. Dividers denote approximate latency classes.

Según Mobile-Friendly Deep Learning for Plant Disease Detection: A Lightweight CNN Benchmark Across 101 Classes of 33 Crops (2025), Model: MobileNet-V2 [6] MNv4-Conv-S [26] MobileNet-V1 [5] MNv4-Conv-M [26] MNv4-Hybrid-M [26] MNv4-Conv-L [26] FastViT-T8† [45] FastViT-S12† [45] MobileNet-V3S [18] EfficientNet-B0 [20] EfficientNet-B1[20], Top-1: 73.4 73.8 74.0 79.9 80.7 82.9 75.6 79.8 69.2 77.1 79.1, Params (M): 3.5 3.8 4.2 9.2 10.5 31 3.6 8.8 2.7 5.3 7.8, MACs (G): 0.3 0.2 0.6 1.0 1.2 5.9 0.7 1.8 0.1 0.39 0.70, Pixel CPU: 5.0 2.4 6.1 11.4 14.3 59.9 49.3 83.0 2.4 - -, 6: 0.7 0.7 0.8 1.1 1.5 2.4 1.3 1.8 0.8 - -, Pixel 8 EdgeTPU: 0.7 0.6 0.7 1.1 - 3.0 0.7 1.6 0.45 - -, iPhone 13 CoreML Pixel Hexagon: 3.9 2.4 3.2 7.3 Failed 20.8 Failed Failed 3.5 - -, Pixel 7 GPU: 13.6 8.4 13.0 18.1 17.9 37.6 40.7 75.0 9.9 - -, Samsung S23 CPU: 4.1 1.8 4.6 8.6 10.8 43.0 43.6 69.2 2.0 - -, Samsung S23 GPU: 2.5 2.0 2.1 4.1 5.9 13.2 24.7 47.0 2.1 - -.
We  have  done  our  experiment  with  MobileNet-V1[5],  MobileNet-V2  [6],  MobileNet-V3[18]   Large  and  Small, MobileNet-V4[26], and EfficientNet-B0, B1 [20]. These models were chosen because they are specifically designed for  mobile  devices  with  low  computational  requirements.  The  MobileNet  variants  (V1,  V2,  V3,  V4)  and EfficientNet  models  (B0,  B1)  represent  the  most  widely  used  efficient  architectures  that  balance  accuracy  with speed.  They  have  small  parameter  counts  (2.7M-31M)  and  low  computational  costs,  making  them  practical  for real-world mobile applications. These models also demonstrate good compatibility across different mobile platforms and processors.

## 2 Methods

## 2.1 Datasets

We have used three  datasets  which  have  been  widely  used  for  plant  disease  detection tasks. First is the PlantVillage  [21]  dataset,  which  is  the  most  widely  used  plant  disease  dataset.  It  contains  54,309  images  of  38 classes. All the pictures in PlantVillage are captured in laboratory environments, thus lacking complex backgrounds in the wild conditions. In contrast, PlantDoc [22] comprise of 2,598 wild images of 27 categories.  Third is the Plant Wild  dataset  [23],  which  is  a  large-scale  in-the-wild  plant  disease  recognition  dataset  in  the  wild,  covering  89 classes, including 33 healthy plant classes and 56 diseased classes.

As the PlantVillage dataset is mostly taken in laboratory conditions and PlantWild and PlantDoc were taken in  field  conditions,  we  have  created  a  unified  dataset  which  have  both datasets. The final dataset contained 37% laboratory images and 67% wild or images taken in field conditions. [Fig. 4]  shows the relation between PlantDoc [22], PlantVillage [21], and PlantWild [23] datasets.

## 2.2 Class Balancing Strategy

While  merging  the  datasets,  we  faced  class  imbalance  where  some  of  the  plant  disease  classes  had thousands  of  images  and  some  had  fewer  than  100  images  [Fig.  1].  A  balancing  algorithm  was  implemented to address the severe class imbalance inherent in the merged dataset. The balancing strategy was as follows

Large Classes :  Datasets  exceeding  2×  target  threshold  underwent  controlled  downsampling  via random selection to prevent computational bias toward overrepresented categories.

Medium  Classes : Classes within the viable range (50-800 samples) were augmented  using  the albumentations [28] library with controlled generation ratios. The maximum augmentation factor was constrained to 4×  per  original  image  to  preserve  data  distribution  integrity.  The  pipeline  combines  geometric  transformations (horizontal/vertical  flips, 90° rotations, p=0.8), photometric adjustments (brightness-contrast variation ±20%, HSV modulation, CLAHE enhancement, p=0.7), noise injection and blur simulation (Gaussian noise σ² ∈ [10,50], motion blur  kernel≤3,  p=0.4),  and  elastic  deformations  (α=50,  σ=5,  p=0.3)  to  preserve  pathological  morphology  while introducing  realistic  imaging variations. Classes below the minimum threshold (50 samples) were excluded, while medium classes  (50-800  samples)  received  controlled  augmentation up to 4× per original image, with augmented samples distributed proportionally across existing images to reach the target of 800 samples per class. The strategy maintains biological plausibility through moderate transformation parameters and prevents overfitting via controlled synthetic-to-real ratios.

Small  Classes :  Classes  below  the  minimum  viability  threshold  (n&lt;50)  were  systematically  excluded  to eliminate statistical noise and ensure robust model training.

After  performing  the  class  balancing  activity,  we  found  our  datasets  balanced.  [Fig.  2]  represents  the balanced  dataset.  The  final  balanced  datasets  were  used  for  training,  which  comprised  101  classes  and  76,730 images.

<!-- image -->

Classes

Fig. 1 | The figure shows the merged datasets, which had a serious class imbalance problem.

<!-- image -->

Fig. 2 | The figure shows the balanced dataset after downsampling and data augmentation.

<!-- image -->

- Fig. 3 |  The figure shows the data engineering steps for creating a unified dataset. Firstly, images from all datasets were merged and create a unified dataset. The unified dataset has a problem of class imbalance, where some of the classes have thousands of images, but some of the classes have fewer than 50 images. To solve class imbalance, we have dropped images from the majority classes, capping the maximum images, and further augmentation techniques were used to increase the minority classes.

Fig. 4 |  The dataset comprises 115 wild plant samples (Plant Wild) and 28 documented samples (Plant Doc), with a subset of 39 samples further analysed. Classification results reveal high accuracy (93 correct predictions) for dominant classes, while smaller values  (17,  5)  indicate confusion between morphologically similar species. The reference to 'Plant Village' suggests alignment with established benchmarks, though our data includes unique wild variants posing greater variability

## 2.3 Training

## 2.3.1 Dataset Configuration and Partitioning

For  training, the dataset  was  first split  into  a  (80:20  ratio,  seed=42)  partition.  We  have  used  the ImageFolder  dataset  [24]  class,  which  facilitated  automatic  label  encoding  based  on directory structure, ensuring consistent  class  mapping  across  experimental  runs.  A  total  of  61,384  images  were  used  for  training, and 15,346 images were used for validation.

## 2.3.2 Training Transform Pipeline

The training data was designed to use execution time augmentation with following augmentation techniques: initial resizing  to  256×256  pixels  followed  by random resized cropping to 224×224, horizontal flipping with probability p=0.5,  color  jittering  across  brightness  (β=0.2),  contrast  (γ=0.2),  saturation  (σ=0.2),  and  hue  (η=0.1)  channels, random  rotation  within  ±15°,  affine  transformation  with  translation  parameters  (0.1,0.1),  random  perspective distortion (ε=0.2, p=0.5), tensor conversion, and  ImageNet  normalization. Where  as test  data underwent deterministic  preprocessing:  resizing  to  256×256  pixels,  center  cropping  to  224×224,  tensor  conversion,  and ImageNet normalization using μ=[0.485, 0.456, 0.406] and σ=[0.229, 0.224, 0.225].

## 2.3.3 Neural Network Architecture

We have chosen MobileNets and EfficientNets as they are suitable for low-compute devices as per their model size and number of parameters mentioned in the table.

## 3.3.2 Transfer Learning Configuration

All  architectures  were  instantiated with ImageNet-pretrained weights. We had frozen the feature extraction layers, excluding the final four blocks (requires\_grad=False) , to preserve hierarchical feature representations learned from large-scale visual dat . Architecture-specific classifier modifications were implemented:

MobileNetV2 : Final linear layer adapted from 1280 to 101 classes

MobileNetV3-Small/Large : Terminal classifier layer modified from original dimensions to 101 output classes

MobileNet  V4 :  Ultimate  classification  layer  restructured  from  pre-trained  weights  to  accommodate  101  target categories

EfficientNet-B0, B1 : Classification head restructured to accommodate 101 target categories

## 3.3.3 Loss Function

Cross-entropy loss was employed: L(θ) = -1/N ∑ᵢ ₌₁ ᴺ ∑ ₌₁ ᶜ yᵢ  log(pᵢ ), where N represents batch size, C denotes class count, y represents ground truth labels, and p represents predicted probabilities.

## 3.3.4 Optimisation Algorithm

Adam optimiser was configured with learning rate α=1×10 ⁻⁴ , L2 regularisation coefficient λ=1×10 ⁻⁴ , and batch size B=64. Training proceeded for 30 epochs with stochastic gradient descent updates: θ ← θ - α ∇ θ(L(θ) + λ||θ||²).

## 3.3.5 Training Protocol

Each  epoch  involved  forward  propagation  through  randomly  shuffled  mini-batches,  loss  computation,  backward propagation, and parameter updates. Memory-efficient data loading utilised pinned memory allocation for optimised GPU transfer.

## 3.4 Computational Infrastructure and Evaluation

Model training was executed on Apple Silicon hardware utilising Metal Performance Shaders (MPS) [25]  backend for  GPU  acceleration.  The  optimised  data  pipeline  employed  memory-pinned  allocation  and  stochastic  batch sampling  during  the  training  phase.  PyTorch  MPS  integration  enabled  efficient  tensor  operations  and  gradient computations on Apple's unified memory architecture.

Comparative model assessment was conducted on the held-out test partition using classification accuracy A = (TP + TN)/(TP + TN + FP + FN) across all four architectures.

## 3.5 Experimental Reproducibility

Deterministic experimental  conditions  were  maintained  through  fixed  random  seed  initialisation,  consistent transformation  application  across  data  splits,  version-controlled  hyperparameter  configuration,  and  standardised evaluation protocols ensuring reproducible results across experimental runs.

## 4  Results

## 4.1 Accuracy Performance Rankings

The training result of all the trained models is listed in [Table 2]. We have found the EfficientNet B1 performing the best with an overall accuracy of 94.7% percent on all datasets. We have achieved this accuracy in a relatively low number of  epochs.  Smaller  parameter  models  like   MobileNet  V3  small,  MobileNet  V2 have achieved very low accuracy, 90.71, and 90.90 respectively.

Según Mobile-Friendly Deep Learning for Plant Disease Detection: A Lightweight CNN Benchmark Across 101 Classes of 33 Crops (2025), Model: MobileNetV3-Large MobileNetV3-small MobileNetV2 EfficientNet-B0 EfficientNet-B1 MobileNetV4, Parameters (Millions): ~5.4M ~2.9M ~3.4M ~5.3M ~7.7M ~6.2M, Size (FP32): ~21.6MB ~11.6MB ~ 13.6MB ~21.8MB ~31.7MB ~24.8MB, Accuracy Recorded(%): 92.62 90.71 90.90 92.03 94.70 93.66.
Table 2 |  Training accuracy comparison of mobile neural network architectures. Classification accuracy during 30-epoch training on [dataset name]. EfficientNet-B1 achieves superior performance (94.7% final accuracy) compared to MobileNet variants. Data represent  single training runs with standard hyperparameters (learning rate: 0.0001, batch size: 64). [Add sample size n = X if multiple runs averaged].

## Overall Model Performance

<!-- image -->

Accuracy (%)

Fig. 6 | Shows the overall performance of  EfficientNet-B1

Top : The confusion matrix heatmap demonstrates strong diagonal patterns indicating accurate classification across most disease classes. Off-diagonal elements  reveal systematic misclassifications primarily between  morphologically  similar  diseases, particularly  bacterial  and  fungal  spots  affecting  different  plant  species.  The  predominantly  green  diagonal  with  sparse  red off-diagonal elements confirms robust model performance with minimal inter-class confusion.

Bottom  left: The  model  achieved  perfect  classification  (100%)  for  top-performing  classes,  including  Grape  Esca  and  Corn Healthy, while ten classes exceeded 99% accuracy. Conversely, the five lowest-performing classes ranged from 71.7% to 78.5%, with Eggplant Cercospora Leaf Spot and Cabbage Alternaria Spot presenting the greatest classification challenges. All categories got an accuracy above 71%.

Bottom  right: The  accuracy distribution shows a right-skewed pattern with a mean performance of 94.7% ± 6.0%, indicating consistently  high  classification  reliability.  Eighty-six  classes  achieved  ≥90%  accuracy,  while  no  classes  fell  below  70%, demonstrating robust performance across the entire disease spectrum. The distribution pattern suggests the model is suitable for practical deployment with minimal classes requiring additional optimisation.

## 4. 2 Model Performance Overview

The proposed plant disease classification model achieved exceptional performance with a mean accuracy of 94.7% and median accuracy of 97.0% across all disease classes. The model demonstrated high consistency with a standard deviation of only 6.0% , indicating robust performance across diverse plant pathologies.

## 4.2.1 Classification Accuracy Distribution

Performance  analysis  revealed  that 86  classes  achieved  ≥90%  accuracy ,  while 94  classes  exceeded  80%

accuracy .  Notably, no  classes  fell  below  70%  accuracy ,  demonstrating  the model's reliability across all disease categories.  The  performance  distribution  was  heavily  right-skewed,  with  the  majority  of  classes  clustered  in  the 95-100% accuracy range.

## 4.2.2 Top-Performing Classes

Several  disease  classes  achieved  near-perfect  classification  accuracy:  Grape Esca (100%), Corn Healthy (99.9%), Tomato  Mosaic  Virus  (99.8%),  Cherry  Powdery  Mildew  (99.6%),  and  Carrot  Alternaria  Blight  (99.6%).  These results  indicate  the  model's  exceptional  capability  in  distinguishing  healthy  plants  from  diseased  specimens  and identifying visually distinct pathological symptoms.

## 4.2.3 Challenging Disease Categories

The model showed relatively lower performance on certain spot-type diseases, including Eggplant Cercospora Spot (73.7%),  Cauliflower  Alternaria  Spot  (75.6%),  and  Cabbage  Alternaria  Spot  (77.8%).  These  challenging  cases primarily involved diseases with subtle visual symptoms or morphologically similar lesion patterns.

## 4.2.4 Clinical Significance

The  confusion  matrix  heatmap  revealed  strong  diagonal  patterns  with  minimal  off-diagonal  misclassifications, confirming  the  model's  ability  to  accurately  discriminate  between different plant pathologies. The consistent high performance across 94+ disease classes demonstrates the model's potential for practical agricultural applications and automated plant disease diagnosis systems.

## 5 Discussion

Our  deep  learning  model  achieved  94.  %  mean  accuracy  across  94+  plant  disease  classes,  establishing  new performance  benchmarks  for  automated  phytopathological  diagnostics.  The  low  standard  deviation  (6.0%)  and absence of classes below 75%  accuracy  indicate robust feature extraction across taxonomically diverse plant-pathogen interactions.

## 5.1 Performance Analysis and Feature Learning

The  strong  diagonal  patterns  in  confusion matrices demonstrate successful learning of discriminative pathological features.  Superior  performance  on  morphologically  distinct  diseases  (Grape  Esca:  100%,  Tomato  Mosaic  Virus: 99.8%)  versus  subtle  spot-type  pathologies  (Cercospora  species:  73.7-77.8%)  reflects  inherent  challenges  in computer vision-based discrimination of similar lesion morphologies. These results exceed recent  Vision Transformer  implementations  (85-92%)  and  traditional  labour-intensive  methods  that  are  insufficient  for  modern agricultural demands.

The  model's  consistent  accuracy  across  healthy  plant  classification  (&gt;99%)  suggests  robust  baseline morphological learning, while high performance on diverse  disease  states  indicates  successful  capture  of pathogen-specific  symptomatology.  Current  detection  methods'  reliance  on  lab-captured  images  limits  real-world generalizability, highlighting the need for field-condition training data.

## 5.2 Implications and Limitations

AI-driven  precision  agriculture  capabilities  enable  accurate  predictions  and  efficient  resource  management  under climate  change  pressures,  with  our  reliability  metrics  approaching  expert-level  diagnostic  accuracy.  However, systematic  challenges  persist  for  morphologically  similar  pathologies,  reflecting  fundamental  computer  vision limitations in subtle pattern discrimination.

The generalizability across diverse crop species positions this technology for universal precision agriculture deployment,  potentially  democratising  expert-level  plant  pathology  knowledge.  Future  research  should  prioritise multi-temporal disease progression analysis and environmental variability incorporation to enhance field deployment viability.

## 5 Conclusion

The demonstrated performance establishes artificial intelligence approaches as viable alternatives to traditional plant disease diagnostics, with implications for global food security and sustainable agriculture. The robust generalisation across  100+  disease  classes  provides  a  foundation  for  scalable  precision  agriculture  implementation,  though morphologically  challenging  pathologies  require  continued  methodological  advancement.  In  the  future,  we  will work extensively on segmentation techniques. Previous segmentation studies have shown promising results for plant disease classification techniques [29]. We will also extend our work on pest detection for a mobile environment [31].

## 6 References

1. https://www.fao.org/plant-production-protection/about/en
2. PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation Tianqi Wei, Zhi Chen, Xin Yu , Scott Chapman, Paul Melloy, and Zi Huang, https://arxiv.org/pdf/2409.04038
3. https://investigatemidwest.org/2024/10/09/graphic-kansas-farmers-lead-midwest-in-smartphone-computeruse
4. https://qqri.com/2022/11/02/digital-usage-trends-amongst-indian-farmers/
5. Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto,  and  Hartwig  Adam.  Mobilenets:  Efficient  convolutional  neural  networks  for  mobile  vision applications. arXiv preprint arXiv:1704.04861, 2017.
6. Mark  Sandler,  Andrew  G.  Howard,  Menglong  Zhu,  Andrey  Zhmoginov,  and  LiangChieh  Chen. Mobilenetv2: Inverted residuals and linear bottlenecks. CoRR, abs/1801.04381, 2018
7. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, and Chang Xu. Ghostnet: More features from cheap operations. In Proceedings of  the  IEEE/CVF  Conference  on  Computer  Vision  and  Pattern Recognition (CVPR), June 2020.]
8. Pavan Kumar Anasosalu Vasu, James Gabriel, Jeff Zhu, Oncel Tuzel, and Anurag Ranjan. Mobileone: An improved  one-millisecond  mobile  backbone.  In  Proceedings  of  the  IEEE/CVF  Conference on Computer Vision and Pattern Recognition, pages 7907-7917, 2023
9. Sachin  Mehta  and  Mohammad Rastegari.  Mobilevit:  light-weight,  general-purpose,  and  mobile-friendly vision transformer. arXiv preprint arXiv:2110.02178, 2021
10.  Alexey  Dosovitskiy,  Lucas  Beyer,  Alexander  Kolesnikov,  Dirk  Weissenborn,  Xiaohua  Zhai,  Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929, 2020.
11.  Yehui Tang, Kai Han, Jianyuan Guo, Chang Xu, Chao Xu, and Yunhe Wang. Ghostnetv2: Enhance cheap operation  with  long-range attention. Advances in Neural Information Processing Systems, 35:9969-9982, 2022
12.  Pavan  Kumar  Anasosalu Vasu, James Gabriel, Jeff Zhu, Oncel Tuzel, and Anurag Ranjan. Fastvit: A fast hybrid vision transformer using structural reparameterization. arXiv preprint arXiv:2303.14189, 2023.
13.  Han Cai et al. Efficientvit: Lightweight multi-scale attention for high-resolution dense prediction. In ICCV, 2023.
14.  Sachin  Mehta  and  Mohammad  Rastegari.  Separable  self-attention  for  mobile  vision  transformers.  arXiv preprint arXiv:2206.02680, 2022
15.  Yanyu  Li,  Ju  Hu,  Yang Wen, Georgios Evangelidis, Kamyar Salahi, Yanzhi Wang, Sergey Tulyakov, and Jian  Ren.  Rethinking  vision  transformers  for mobilenet size and speed. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 16889-16900, 2023.
16.  Tien-Ju  Yang,  Andrew  G.  Howard,  Bo  Chen,  Xiao  Zhang,  Alec  Go,  Vivienne  Sze,  and Hartwig Adam. Netadapt:  Platform-aware  neural  network  adaptation  for  mobile  applications.  CoRR,  abs/1804.03230, 2018.]
17.  Mingxing  Tan,  Bo  Chen,  Ruoming  Pang,  Vijay  Vasudevan,  and  Quoc  V.  Le.  Mnasnet:  Platform-aware neural architecture search for mobile. CoRR, abs/1807.11626, 2018
18.  Andrew  Howard,  Mark  Sandler,  Grace  Chu,  Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu, Ruoming Pang, Vijay Vasudevan, Quoc V. Le, and Hartwig Adam. Searching for mobilenetv3. CoRR, abs/1905.02244, 2019]
19.  Grace Chu, Okan Arikan, Gabriel Bender, Weijun Wang, Achille Brighton, PieterJan Kindermans, Hanxiao Liu,  Berkin  Akin,  Suyog  Gupta,  and  Andrew  Howard.  Discovering  multi-hardware  mobile  models  via architecture  search. In IEEE Conference on Computer Vision and Pattern Recognition Workshops, CVPR Workshops 2021, virtual, June 19-25, 2021, pages 3022-3031. Computer Vision Foundation / IEEE, 2021.
20.  https://arxiv.org/pdf/2404.10518
21.  David Hughes, Marcel Salathé, et al. 2015. An open-access repository of images on plant health to enable the development of mobile disease diagnostics. arXiv preprint arXiv:1511.08060 (2015).
22.  Davinder  Singh,  Naman  Jain,  Pranjali  Jain,  Pratik  Kayal,  Sudhakar  Kumawat,  and  Nipun  Batra.  2020. PlantDoc:  A  dataset  for  visual  plant disease detection. In Proceedings of the 7th ACM IKDD CoDS and 25th COMAD. 249-253.
23.  Benchmarking  In-the-Wild  Multimodal  Plant  Disease  Recognition  and  A Versatile Baseline, Tianqi Wei, Zhi Chen, Zi Huang, Xin Yu. ACM International Conference of Multimedia 2024, https://arxiv.org/pdf/2408.03120
24.  https://docs.pytorch.org/vision/main/generated/torchvision.datasets.ImageFolder.html
25.  https://developer.apple.com/metal/pytorch
26.  MobileNetV4:  Universal  Models  for  the  Mobile  Ecosystem  Danfeng  Qin†‡,  Chas  Leichner,  Manolis Delakis, Marco Fornoni, Shixin Luo, Fan Yang, Weijun Wang, Colby Banbury, Chengxi Ye, Berkin Akin, Vaibhav Aggarwal, Tenghui Zhu, Daniele Moro, and Andrew Howard,  https://arxiv.org/pdf/2404.10518
27.  J.  Deng,  W.  Dong,  R.  Socher,  L.  Li,  Kai  Li,  and  Li  Fei-Fei. Imagenet: A large-scale hierarchical image database.  In  2009  IEEE  Conference  on  Computer  Vision  and  Pattern  Recognition, pages 248-255, June 2009.
28. https://albumentations.ai/
29.  PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation Tianqi Wei, Zhi Chen, Xin Yu, Scott Chapman, Paul Melloy, and Zi Huang, https://arxiv.org/pdf/2409.04038.
30.  Using  Deep  Learning  for  Image-Based  Plant  Disease  Detection,  Sharada  Prasanna  Mohanty,  David Hughes, and Marcel Salathe, https://arxiv.org/pdf/1604.03169
31.  Plant diseases  and  pests  detection  based  on  deep  learning:  a  review,  Jun  Liu  &amp;  Xuewei  Wang, https://plantmethods.biomedcentral.com/articles/10.1186/s13007-021-00722-9.
32.  Krizhevsky  A,  Sutskever  I,  Hinton  GE  (2012)  Imagenet  classification  with  deep  convolutional  neural networks in Advances in neural information processing systems. pp. 1097-1105
33.  Szegedy  C  et  al.  (2015)  Going  deeper  with  convolutions  in  Proceedings  of  the  IEEE  Conference  on Computer Vision and Pattern Recognition. pp. 1-9.