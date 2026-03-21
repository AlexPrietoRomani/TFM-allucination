---
id: arxiv-2505.02441
title: MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection
year: 2025
country: Internacional
source: ArXiv (cs.AI)
doc_type: Artículo científico
language: en
tags:
  - detección de plagas
  - deep learning
  - cultivos
  - artículo científico
  - ArXiv
---

## MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection

Jiaqi Zhang 1* , Zhuodong Liu 2* , Kejian Yu 3 †

1 College of Computer and Information Science, Southwest University, Chongqing 400700, China

2 School of Economics and Management, Beijing Jiaotong University, Beijing 100044, China

3 School of Computer Science and Technology, Donghua University, Shanghai 201620, China

Abstract -Accurate identification of agricultural pests is essential for crop protection but remains challenging due to the large intra-class variance and fine-grained differences among pest species. While deep learning has advanced pest detection, most existing approaches rely solely on low-level visual features and lack effective multi-modal integration, leading to limited accuracy and poor interpretability. Moreover, the scarcity of high-quality multi-modal agricultural datasets further restricts progress in this field. To address these issues, we construct two novel multi-modal benchmarks-CTIP102 and STIP102-based on the widely-used IP102 dataset, and introduce a Multi-scale Cross-Modal Fusion Network (MSFNet-CPD) for robust pest detection. Our approach enhances visual quality via a superresolution reconstruction module, and feeds both the original and reconstructed images into the network to improve clarity and detection performance. To better exploit semantic cues, we propose an Image-Text Fusion (ITF) module for joint modeling of visual and textual features, and an Image-Text Converter (ITC) that reconstructs fine-grained details across multiple scales to handle challenging backgrounds. Furthermore, we introduce an Arbitrary Combination Image Enhancement (ACIE) strategy to generate a more complex and diverse pest detection dataset, MTIP102, improving the model's generalization to real-world scenarios. Extensive experiments demonstrate that MSFNetCPD consistently outperforms state-of-the-art methods on multiple pest detection benchmarks. All code and datasets will be made publicly available at: https://github.com/Healer-ML/ MSFNet-CPD.

Index Terms -Cross-Modal Fusion, Pest Detection, MultiModal

## I. INTRODUCTION

Over the years, crop pests have consistently threatened agricultural yields, product quality, and profitability. Traditional methods of pest identification are slow, costly, and heavily reliant on expert knowledge [1]. However, recent advancements in deep learning and computer vision have led to the development of innovative pest classification techniques, such as Convolutional Neural Networks (CNNs) and Transformers. These techniques provide faster, more accurate, and costeffective solutions to the challenges of pest detection.

In recent years, various deep learning techniques have been applied to crop pest detection to enhance accuracy and efficiency. You et al. [2] developed an offline mobile app that uses a compressed CNN to diagnose citrus pests, which stands out

* These authors contributed equally to this work.

† Corresponding author: Kejian Yu (yukejian2021@outlook.com)

for its low cost, speed, and accuracy. Similarly, Wang et al. [3] designed a CNN with an Inception module to identify multiple crop diseases, achieving over 95% accuracy. Their model is not only faster but also more precise compared to traditional methods. H.T. et al. [4] enhanced CNNs by incorporating attention mechanisms and feature pyramids, achieving 99.78% accuracy on a small pest dataset and yielding respectable results on the larger IP102 dataset. Guo et al. [5] advanced multi-label pest classification by applying the Swin Transformer, which significantly improved accuracy on the IP102 dataset. Wang et al. [6] developed a deep learning ensemble that combines CNNs and Swin Transformers, demonstrating high accuracy across various datasets. Bao et al. [7] employed DenseNet with a Coordinated Attention mechanism to accurately classify the severity of cotton aphid damage. Nigam et al. [8] fine-tuned EfficientNet for identifying wheat diseases, achieving high accuracy. Lastly, Yu et al. [9] combined Transformers with convolutional networks to create the Inception Convolution Visual Transformer (ICVT), which enhances feature extraction for plant disease detection through Dynamic Pattern Decomposition, resulting in improved performance in deep learning classifiers and machine learning models [10].

The challenge of pest image detection arises from the complexity and variability of agricultural backgrounds, coupled with the scarcity of high-quality pest images. Historically, studies have focused on leaf-based pest detection. However, advancements in smart farming have highlighted the importance of integrating deep learning into this field [11], despite the challenges posed by diverse agricultural data sources and the need for semantic interpretation [12]. Rice fusion Multimodal approaches are being explored to fuse different types of data. For instance, Rutuja et al. [13] introduced rice fusion for rice disease diagnosis. In contrast, Zhang et al. [14] developed the MMFGT model, which utilizes self-supervised learning for fine-grained pest detection. Zhou et al. [15] investigated semantic embedding for disease image-text correlation, and Zhang et al. [16] implemented the Multi-ResNet34 method for diagnosing tomato diseases, contributing to pest detection technology advancements.

Although significant progress has been made in crop pest detection, several challenges remain. First, the complexity and diversity of agricultural environments can negatively impact the accuracy of models that primarily rely on low-level image features. Second, many models are designed for single-target detection and struggle to handle images with multiple pests of varying species and sizes. Finally, the performance of these models is often limited by the low quality of images captured in natural settings in the real world. To address these challenges, this study proposes a multi-scale cross-modal fusion network to enhance pest detection performance in the IP102 dataset. We constructed two multi-modal datasets, CTIP102 and STIP102, by creating simple and complex text descriptions for each pest image to combine visual and text features for multi-modal learning. We employ the Enhanced SuperResolution Generative Adversarial Network (ESRGAN) [17] to perform super-resolution reconstruction on low-resolution images, preserving and enriching the pest feature information. Both the original and reconstructed images are used together for model training. Additionally, we introduce the ACIE data augmentation algorithm to improve the model's robustness and adaptability in real-world environments by generating a multitarget detection dataset, MTIP102. Our contributions to this study can be summarized as follows:

- (1) This paper proposes the Multi-Scale Cross-modal Fusion Network (MSFNet-CPD) for crop pest detection. This approach is the first to integrate image high-frequency information with text for pest detection by recovering highfrequency information from low-quality images and combining visual and text features.
- (2) Based on the IP102 dataset, we created two multi-modal datasets, STIP102 and CTIP102. Additionally, we introduced a generalized data enhancement algorithm, ACIE, to create the multi-target detection dataset MTIP102, which enhances the model's practical applicability.
- (3) Extensive experiments on the constructed datasets validate the model's effectiveness, and comparisons with other models demonstrate the advantages of our approach.

## II. METHOD

This section describes each part of the MSFNet-CPD model in detail, as shown in Figure 1.

## A. Low and Super Resolution Generative Adversarial Network (LSRGAN)

The low and super-resolution modules mainly convert lowresolution input data into high-resolution image formats. Lowresolution images may be due to small spatial resolution of image data or distortion such as blurring in the image. In addition, image texture loss, mutation loss, content loss, and pixel loss can be detected and repaired using the superresolution (SR) method [18]. However, since some of the lowresolution information will be changed when reconstruction is performed, in this paper, the original image is used as a supplement to the SR image features and sent to the model for feature extraction, as shown in the upper part of Figure 1.

## B. Text-Image Converter (TIC)

In this paper, we design a multi-scale feature extraction block using a convolutional neural network. It processes the original and super-resolution images to extract features at three scales, which are then concatenated. The TIC aligns these visual features with text dimensions and reduces computational load. TIC consists of three parts ( B 1 , B 2 , B 3 ), corresponding to visual features ( V 1 , V 2 , V 3 ), and each part includes a convolutional layer, ReLU layer, and max pooling layer. Input dimensions for B 1 , B 2 , and B 3 are 19×19×1024, 38×38×512, and 76×76×256, respectively. The output was scaled to 5 × 5 × T and then reshaped to 25 visual feature markers for ITF input, with T representing the text size, as shown in the specific module parameters in Table I.

## C. Multi-Scale Cross-Modal Fusion ITF Module

ITF, based on the Transformer encoding architecture proposed by Vaswani et al. [19], is demonstrated in Figure 2 to illustrate the specific internal process of ITF. Conv Transformer A extracts visual features and transforms them into the Transformer architecture encoding through convolution. This structure includes multi-head self-attention sublayers and fully connected feed-forward sub-layers. Residual connections and layer normalization are applied between the two sub-layers. The Transformer encoder employs scaled dotproduct attention, defined as follows:

<!-- formula-not-decoded -->

Q , K , and V consist of queries, keys, and values, respectively, and d k represents the dimensionality of keys. In our model, we concatenate text and image features into a new sequence G :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

G LR , G SR represent high-resolution image features and low-resolution image features respectively. The reconstructed image features before and after concatenation into G are input into ITF; hence, Q = K = V = G T . Ultimately, ITF outputs multi-scale image features V C 1 , V C 2 and V C 3 , which are encoded through Conv Transformer B for subsequent ITC. Conv Transformer B is the reverse process of Conv Transformer A.

## D. Image-Text Converter (ITC)

The ITC is the inverse process of the TIC. The ITC outputs features of the same size ( V Ni ) as the input features ( V i ) to the TIC, where i ∈ [1,3]. The ITC consists of three parts, denoted as C 1 , C 2 , and C 3 corresponding to B 1 , B 2 , and B 3 in the TIC, with specific architectures and parameters detailed in Table I. Each part comprises transpose convolution (ConvT) [20] ReLU and upsampling operations. ConvT performs the reverse operation of convolution. Since the kernel size, padding size, and stride of ConvT are the same as those used in the Conv layer, ConvT generates image features with the exact dimensions as the input features. Upsampling reverses the pooling operation using the nearest-neighbor interpolation algorithm.

Fig. 1: MSFNet-CPD Model Architecture (A. LSRGAN for super-resolution of low-quality images, B. Picture to ITF Transformer (TIC), C. Multi-scale Cross-modal Fusion ITF Module, D. ITF to Neck Network Converter (ITC), and E. Pest Target Identification (PTI). Numbers represent categories in Original Image and Pre Image, numbers represent class confidence and category).

<!-- image -->

Fig. 2: ITF Specific Process. ( B i , C i , V i stand for different scale image features and T stands for text features).

<!-- image -->

TABLE I: TIC and ITC Structure.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), TIC: B3, B1 B2: [3x3].
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), TIC: ITC, B1 B2: C1 C2 C3, Conv MaxPooling Conv MaxPooling Conv MaxPooling: UpSampling ConvT UpSampling ConvT UpSampling ConvT, [K=3x3, P=1, S=2] [2x2] [K=3x3, P=1, S=2; K=3x3, P=1, S=2] [2x2] [K=5x5, P=2, S=4; K=3x3, P=1, S=2]: [2x2] [K=3x3, P=1, S=2] [2x2] [K=3x3, P=1, S=2; K=3x3, P=1, S=2] [2x2] [K=3x3, P=1, S=2; K=5x5, P=2, S=4].
B 1 , B 2 , B 3 , C 1 , C 2 and C 3 stand for the corresponding module name of Figure 1. K, S, P are the convolution kernel, step size, and padding respectively.

## E. Pest Target Identification (PTI)

This paper primarily compares the advantages and disadvantages of unimodal and multi-modal approaches. Due to its simpler structure and fewer model parameters than YOLOv8 and YOLOv9, we utilize the Neck and Head Networks of YOLOv4 [21] for pest target detection. The multi-scale cross-modal features V N 1 , V N 2 and V N 3 from the image feature extraction network are connected to the neck network, which includes Spatial Pyramid Pooling (SPP) [22] and Path Aggregation Network (PANet) [23]. The SPP consists of three maximum pooling layers, while the PANet comprises convolutional and downsampling components. PANet enhances the receptive field and retains spatial information. The processed information at different scales is then fed into the head network, which predicts three types of bounding boxes at different scales. Detailed calculations for bounding offsets can be found in Redmon and Farhadi [24]. In our model, num class is set to 102 to account for the 102 different pest classes. The PTI objective function includes the bounding box regression loss L B and the target class loss L O :

<!-- formula-not-decoded -->

As with YOLOv4, the bounding box regression loss of L B includes the Mean Squared Error (MSE) of the width and height of the predicted box versus the width and height of the target box. Additionally, L O is the target category loss, which calculates the binary cross-entropy (BCE) of the predictor box

Fig. 3: Partial Presentation of Multi-modal Dataset.

<!-- image -->

category probability with the category information of the target box.

## F. Data Set Construction

In this study, we utilize two types of data: image and text. The image data are mainly from the IP102 [25] public dataset, which contains photos of forest and field pests of variable quality and often affected by noise. To ensure the quality of the data, we manually screened and extracted some high-quality images for model comparison experiments, and this dataset was named HIP102. To compensate for the lack of textual feature information, we constructed two text descriptions, simple and complex, for each pest. These text descriptions are intended to provide information about the pest characteristics and thus increase the source of information for the model.

In the process of text data collection, to ensure the credibility of the data. Our text data were mainly obtained from specialized pest books. In addition, we also applied crawler technology to obtain relevant text data from authoritative websites. These text descriptions mainly cover the main features of pests, such as morphology, size, color, etc., as shown in Figure 3.

## G. Arbitrary Combination Image Enhancement

In real agricultural environments, pests live in sophisticated and diverse conditions, with multiple pests often appearing on the same crop simultaneously. Photos taken at different angles can result in pest size and relative position variations. Most current datasets contain images with only 1 or 2 pests, which are relatively fixed in size and have high overlap, limiting pest diversity in the training data and affecting model prediction accuracy. To address these issues, this study proposes an image data enhancement algorithm. Unlike traditional methods such as image rotation, noise addition, and saturation adjustment, this method fully considers pest diversity and environmental randomness. It reduces labeling costs and better adapts the model to identify pests in real scenarios. The specific steps of the algorithm are as follows:

In the above ACIE, B , T , R , and num in this study are 580, 820, 4, and 10,000, respectively. This innovative data enhancement method effectively increases the pest diversity and randomness in the training dataset, provides more challenging training data for the model, and boosts the model's performance for application in real environments.

## Algorithm ACIE

Input: Target Images( T ); Background Images( B ); The number of targets R on the image and the number of generated images num

Output: num images containing R target images

1: Repeat 2: for in range( num ) 3: Select B 4: for r ← 1 to R 5: Select T Calculate w,h (minimum bounding rectangle width and height). Randomly select a point ( x 1 , y 1 ) , place target T on background B , and calculate the final position based on w,h 6: Obtain image annotations [( x 1 , y 1 ) , ( x 2 , y 2 ) , class id ] 7: If Target overlap 8: Go to step 6

- 9: Until Target does not overlap
- 10: Return Composite image

Fig. 4: Visualization of the semantic correlation analysis of simple and complex text descriptions. (Horizontal and vertical coordinates in the figure indicate the coordinates after mapping the feature vectors into a low-dimensional space).

<!-- image -->

## III. EXPERIMENTATION

## A. Data Setup

In this study, we applied five datasets, IP102, HIP102, STIP102, CTIP102, and MTIP102, dividing the datasets according to 8:1:1. Table II shows the number of images and text characters in the training, validation, and test sets of these datasets. We use these datasets to evaluate the performance of our proposed MSFNet-CPD model.

## B. Experimental Setup

In this experiment, we implemented the algorithm on a Linux Ubuntu 18.04 workstation equipped with 70GB of RAM and an A6000-48G GPU using Pycharm, Python 3.7, and PyTorch 1.7.0+cu110. We used the Adam optimization

TABLE II: Dataset Description and Division.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: IP102, Dataset: Images, Training: 60178, Test: 7522, Validation: 7522, Total: 75222.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: Text.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: HIP102, Dataset: Images, Training: 15180, Test: 1898, Validation: 1898, Total: 18976.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: HIP102, Dataset: Text, Training: 306124, Test: 42513, Validation: 43214, Total: 391851.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: STIP102, Dataset: Images, Training: 60178, Test: 7522, Validation: 7522, Total: 75222.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: STIP102, Dataset: Text, Training: 12626878, Test: 405124, Validation: 405080, Total: 13437082.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: CTIP102, Dataset: Images, Training: 60178, Test: 7522, Validation: 7522, Total: 75222.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: CTIP102, Dataset: Text, Training: 34501251, Test: 951324, Validation: 952652, Total: 36405227.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: MTIP102, Dataset: Images, Training: 8000, Test: 1000, Validation: 1000, Total: 10000.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: MTIP102, Dataset: Text, Training: 665549, Test: 83083, Validation: 83083, Total: 831715.
The IP102 dataset serves as the original baseline collection. HIP102 is a refined subset of hand-screened, high-quality images with detailed text descriptions. CTIP102 combines the original IP102 images with complex text descriptions, while STIP102 pairs the original images with more straightforward, concise text descriptions. MTIP102, constructed using the ACIE algorithm, includes images with complex text descriptions and is designed to enhance multiscale feature diversity for robust model training.

TABLE III: Model Parameter Settings.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Experimental Settings: Training Settings, Hyperparameter: batch size optimizer weight decay learning rate dropout epochs, Optimized Value: 4 Adam 0.0000001 5.00E-05 0.5 30.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Experimental Settings: Image, Hyperparameter: conf thresh nms thresh pretrain model, Optimized Value: 0.5 0.4 yolo.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Experimental Settings: Text, Hyperparameter: sent maxlen hidden size num attention heads pretrain model, Optimized Value: 35 768 16 bert-base-uncased.
TABLE IV: IP102 Advanced Model Target Detection Effects.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: FRCNN [26], Backbone: VGG-16, mAP(%): 21 . 05, mAP 50 (%): 47 . 87, mAP 75 (%): 15 . 23.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: FPN [27], Backbone: ResNet-50, mAP(%): 28 . 10, mAP 50 (%): 54 . 93, mAP 75 (%): 23 . 30.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: SSD300 [28], Backbone: VGG-16, mAP(%): 21 . 49, mAP 50 (%): 47 . 21, mAP 75 (%): 16 . 57.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: RefineDet [29], Backbone: VGG-16, mAP(%): 22 . 84, mAP 50 (%): 49 . 01, mAP 75 (%): 16 . 82.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: YOLOv3 [24], Backbone: DarkNet-53, mAP(%): 25 . 67, mAP 50 (%): 50 . 64, mAP 75 (%): 21 . 79.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: YOLOv8 [30], Backbone: DarkNet, mAP(%): 38 . 41, mAP 50 (%): 73 . 58, mAP 75 (%): 29 . 17.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Method: YOLOv9 [31], Backbone: E-ELAN, mAP(%): 42 . 32, mAP 50 (%): 81 . 10, mAP 75 (%): 39 . 86.
The results for FRCNN, FPN, SSD300, and RefineDet are from [25], while the results for YOLOv8, YOLOv9, and YOLOv4 are from the experiments in this paper, all using the IP102 unimodal dataset.

algorithm for training and applied non-maximal suppression (NMS) for object detection. YOLOv4 and bert-base-uncased pre-trained models were used for image and text processing, with the specific parameter configurations listed in Table III. These settings validated the effectiveness of the MSFNet-CPD model for pest identification and classification.

In this study, we have used Word2Vec [32] and TF-IDF to visualize and analyze the semantic relevance of textual information, as shown in Figure 4. Both methods show a high degree of aggregation of complex text descriptions at the word and sentence level. Thus, compared to STIP102, these results highlight the complexity and richness of text descriptions

TABLE V: Indicator Results from Different Data Sets.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: HIP102, P(%): 90.88, F1(%): 81.23, mAP(%): 52.21, mAP 50 (%): 95.35, mAP 75 (%): 41.8.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: STIP102, P(%): 72.43, F1(%): 69.15, mAP(%): 44.98, mAP 50 (%): 88.22, mAP 75 (%): 42.3.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: CTIP102, P(%): 82.15, F1(%): 78.21, mAP(%): 46.06, mAP 50 (%): 92.18, mAP 75 (%): 40.18.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Dataset: MTIP102, P(%): 45.24, F1(%): 51.23, mAP(%): 22.33, mAP 50 (%): 43.04, mAP 75 (%): 20.78.
Experimental results of the MSFNet-CPD model using different multi-modal datasets in the same setup.

in the CTIP102 dataset, providing valuable insights for data processing and model training.

## C. Model evaluation and analysis

We use several commonly adopted metrics to comprehensively evaluate model performance in object detection tasks: Precision, recall, F1-Score, and Average Precision (AP). Average Precision includes Mean Average Precision (mAP), calculated as the average over a range of Intersection over Union (IoU) values from 0.5 to 0.95, as well as mAP at specific thresholds: mAP 50 (IoU=0.5) and mAP 75 (IoU=0.75). These metrics are crucial for assessing the accuracy of pest classification and detection performance.

In this section, we evaluate the performance of our proposed MSFNet-CPD model using four multi-modal datasets derived from the IP102 dataset. The detailed results are shown in Table V. Additionally, Table IV presents the mAP, mAP 50 , and mAP 75 results from the unimodal IP102 dataset for the target detection task. The results indicate that the CTIP02 and STIP102 datasets outperform the unimodal dataset in detection performance. This suggests that incorporating textual descriptive features corresponding to the images helps overcome the limitations of using single-image features, thus improving the model's extraction, detection, and classification effectiveness. This further demonstrates that the multi-modal dataset developed in this study is more complete and accurate than the unimodal IP102 dataset. We also explore the impact of

AP75

<!-- image -->

ACC

Fig. 5: Comparison of Indicators for Different Data Sets.

text feature complexity on model performance. Experimental results from the STIP102 and CTIP102 datasets show that more complex text descriptions lead to better performance compared to simpler ones, especially during the feature extraction and fusion phases. Specifically, using complex text descriptions improves Precision, mAP, and mAP 50 by 9.72%, 1.08%, and 3.96%, respectively, compared to more straightforward text descriptions. As shown in Table IV, the mAP achieved using YOLOv9 is 42.32%, with mAP 50 at 81.10% and mAP 75 at 39.86%. In comparison, our proposed model significantly outperforms this state-of-the-art model across all metrics-precision, mAP, mAP 50 , and mAP 75 . These results convincingly demonstrate that cross-modal feature learning is more effective than unimodal features in agricultural pest identification tasks, providing valuable insights for future research.

## D. Ablation Experiments

Ablation experiments were performed by removing text (w/o text) and LSRGAN (w/o LSRGAN) from our multimodal model. The results of these experiments are shown in Table VI, where the backbone is CSPDakNet53, and the language model (LM) is BERTbase. When the text component was removed, the mAP decreased by 10.42%, mAP 50 dropped by 10.5%, and mAP 75 decreased by 10.76%. Similarly, when the LSRGAN component was removed, mAP decreased by 11. 24%, mAP 50 decreased by 12. 64%, and mAP 75 decreased by 11.19%. These results highlight the importance of highresolution image and text features for target detection.

## E. Comparison of datasets

To explore the performance of our model, we manually selected high-quality images. To evaluate the performance of our model, we created the HIP102 multi-modal data set

TABLE VI: Ablation Results.

Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Model: Our model, mAP(%): 46 . 06, mAP 50 (%): 92 . 18, mAP 75 (%): 39 . 86.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Model: -w/o text, mAP(%): 35 . 64, mAP 50 (%): 81 . 68, mAP 75 (%): 29 . 10.
Según MSFNet-CPD: Multi-Scale Cross-Modal Fusion Network for Crop Pest Detection (2025), Model: -w/o LSRGAN, mAP(%): 34 . 82, mAP 50 (%): 79 . 54, mAP 75 (%): 28 . 67.
manually, selecting high-quality images. HIP102 surpasses other multi-modal datasets in image resolution, quality, pest variety, and robustness. As demonstrated in Figure 5, our model achieves higher accuracy, mAP, mAP 50 and mAP 75 on HIP102 compared to other datasets. This suggests that the IP102-based multi-modal dataset could still be improved in these areas. Given that pests inhabit diverse environments and vary widely in size and species, we further examined the model's ability to identify multiple targets at various scales within complex scenes. We constructed the MTIP102 multi-modal dataset to simulate these real-world conditions using the ACIE data enhancement method proposed in this study. MTIP102 includes images with multiple pest targets of different types and sizes.

In comparison to other single-target multi-modal datasets, MTIP102 achieves slightly lower scores in terms of accuracy, mAP, mAP 50 , and mAP 75 . However, it still outperforms the original IP102 unimodal dataset in several metrics. The decrease in performance can be attributed to the increased complexity of multi-target images, where the variations in pest types and scales pose greater challenges for feature learning. Nevertheless, MTIP102 closely simulates the natural environments of pests, enhancing the model's robustness under challenging conditions. Other datasets, such as STIP102 and CTIP102, were constructed in addition to HIP102 and MTIP102. While these datasets differ in complexity and target representation, they allow further refinement. This section highlights the need for dataset enhancement to improve model performance, especially in complex, real-world pest identification scenarios.

## F. Visualization of Regions of Interest

In this section, Grad-cam methods [33], [34] are employed to conduct an interpretable study of the model's feature points of interest. The most critical locations in the Gradcam plot correspond to the targets, which also serve as the model's regions of interest (ROI). As depicted in Figure 6, the Grad-cam plot of multi-modal images predominantly focuses on the primary areas of pests, reducing redundant coverage compared to unimodal images. This observation underscores the inadequacy of semantic information in unimodal visual features, highlighting the enhanced robustness of multi-modal features derived from the fusion of text and visual information.

## G. Discussion

Although image-based methods have been widely used for disease or pest detection, there are still limitations in that images may not provide detailed information about pest

Fig. 6: Grad-cam Visualization Results. (Single modal images are generated using w/o text, while multi-modal images are generated using MSFNet-CPD).

<!-- image -->

species and characteristics [7], [34], [35]. The ITF structure proposed in this study solves this problem by processing text description information in images for feature extraction and fusion. The MSFNet-CPD model has an advantage when image and text data are available, enabling more accurate and comprehensive pest classification and detection. Experiments have demonstrated that complex text descriptions can improve the detection rate, and future research should focus on the preprocessing of natural language descriptions and validate the model's performance in practical applications. In addition, this study proposes the ACIE data enhancement method, which can be applied to single-target detection with fewer data and extend the dataset, thus reducing the time for data labeling and collection.

## IV. CONCLUSION

This study addresses the challenges in pest detection, including complex and dynamic backgrounds and the limitations of single-mode detection. We propose a deep learning network, MSFNet-CPD, which utilizes multi-scale cross-modal fusion network of image and text data to detect and classify 102 pest species using the IP102 dataset. Experimental results show that integrating a super-resolution reconstruction algorithm with the multi-scale cross-modal fusion strategy significantly enhances the model's performance. Specifically, MSFNetCPD achieves a detection precision of 82.15% and a mAP score of 46.06% when processing both image and text inputs simultaneously.

Ablation studies demonstrate that our approach not only overcomes the limitations of image-only features but also benefits from higher-quality data, improving network performance. Furthermore, we expect even better performance under real-world conditions by incorporating multi-target datasets with diverse pest species and sizes, enhanced through the ACIE data augmentation algorithm.

Overall, our MSFNet-CPD network for cross-modal, multiscale fusion shows strong potential for pest identification in complex environments, with promising applications for a wide range of agricultural tasks in the future.

## REFERENCES

- [1] G. Dai, J. Fan, Z. Tian, and C. Wang, 'Pplc-net: Neural networkbased plant disease identification model supported by weather data augmentation and multi-level attention mechanism,' Journal of King Saud University-Computer and Information Sciences , vol. 35, no. 5, p. 101555, 2023.
- [2] J. You and J. Lee, 'Offline mobile diagnosis system for citrus pests and diseases using deep compression neural network,' IET Computer Vision , vol. 14, no. 6, pp. 370-377, 2020.
- [3] L. Wang, J. Sun, X. Wu, J. Shen, B. Lu, and W. Tan, 'Identification of crop diseases using improved convolutional neural networks,' IET Computer Vision , vol. 14, no. 7, pp. 538-545, 2020.
- [4] H. T. Ung, H. Q. Ung, and B. T. Nguyen, 'An efficient insect pest classification using multiple convolutional neural network based models,' arXiv preprint arXiv:2107.12189 , 2021.
- [5] Q. Guo, C. Wang, D. Xiao, and Q. Huang, 'A novel multi-label pest image classifier using the modified swin transformer and soft binary cross entropy loss,' Engineering Applications of Artificial Intelligence , vol. 126, p. 107060, 2023.
- [6] C. Wang, J. Zhang, J. He, W. Luo, X. Yuan, and L. Gu, 'A twostream network with complementary feature fusion for pest image classification,' Engineering Applications of Artificial Intelligence , vol. 124, p. 106563, 2023.
- [7] W. Bao, T. Cheng, X.-G. Zhou, W. Guo, Y. Wang, X. Zhang, H. Qiao, and D. Zhang, 'An improved densenet model to classify the damage caused by cotton aphid,' Computers and Electronics in Agriculture , vol. 203, p. 107485, 2022.
- [8] S. Nigam, R. Jain, S. Marwaha, A. Arora, M. A. Haque, A. Dheeraj, and V. K. Singh, 'Deep transfer learning model for disease identification in wheat crop,' Ecological Informatics , vol. 75, p. 102068, 2023.
- [9] S. Yu, L. Xie, and Q. Huang, 'Inception convolutional vision transformers for plant disease identification,' Internet of Things , vol. 21, p. 100650, 2023.
- [10] S. KM, S. V, S. P. Kurian, and O. K. Sikha, 'Ai based rice leaf disease identification enhanced by dynamic mode decomposition,' 2023.
- [11] P. S. Thakur, P. Khanna, T. Sheorey, and A. Ojha, 'Trends in visionbased machine learning techniques for plant disease identification: A systematic review,' Expert Systems with Applications , p. 118117, 2022.
- [12] X. Yang, L. Shu, J. Chen, M. A. Ferrag, J. Wu, E. Nurellari, and K. Huang, 'A survey on smart agriculture: Development modes, technologies, and security and privacy challenges,' IEEE/CAA Journal of Automatica Sinica , vol. 8, no. 2, pp. 273-302, 2021.
- [13] R. R. Patil and S. Kumar, 'Rice-fusion: A multimodality data fusion framework for rice disease diagnosis,' IEEE Access , vol. 10, pp. 52075222, 2022.
- [14] Y. Zhang, L. Chen, and Y. Yuan, 'Multimodal fine-grained transformer model for pest recognition,' Electronics , vol. 12, no. 12, p. 2620, 2023.
- [15] J. Zhou, J. Li, C. Wang, H. Wu, C. Zhao, and G. Teng, 'Crop disease identification and interpretation method based on multimodal deep learning,' Computers and Electronics in Agriculture , vol. 189, p. 106408, 2021.
- [16] N. Zhang, H. Wu, H. Zhu, Y. Deng, and X. Han, 'Tomato disease classification and identification method based on multimodal fusion deep learning,' Agriculture , vol. 12, no. 12, p. 2014, 2022.
- [17] X. Wang, L. Xie, C. Dong, and Y. Shan, 'Real-esrgan: Training realworld blind super-resolution with pure synthetic data,' in Proceedings of the IEEE/CVF International Conference on Computer Vision , 2021, pp. 1905-1914.
- [18] K. Hayat, 'Super-resolution via deep learning,' arXiv preprint arXiv:1706.09077 , 2017.
- [19] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, 'Attention is all you need,' Advances in Neural Information Processing Systems , vol. 30, 2017.
- [20] V. Dumoulin and F. Visin, 'A guide to convolution arithmetic for deep learning,' arXiv preprint arXiv:1603.07285 , 2016.
- [21] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, 'Yolov4: Optimal speed and accuracy of object detection,' arXiv preprint arXiv:2004.10934 , 2020.
- [22] K. He, X. Zhang, S. Ren, and J. Sun, 'Spatial pyramid pooling in deep convolutional networks for visual recognition,' IEEE Transactions on Pattern Analysis and Machine Intelligence , vol. 37, no. 9, pp. 19041916, 2015.
- [23] S. Liu, L. Qi, H. Qin, J. Shi, and J. Jia, 'Path aggregation network for instance segmentation,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , 2018, pp. 8759-8768.
- [24] J. Redmon and A. Farhadi, 'Yolov3: An incremental improvement,' arXiv preprint arXiv:1804.02767 , 2018.
- [25] X. Wu, C. Zhan, Y.-K. Lai, M.-M. Cheng, and J. Yang, 'Ip102: A largescale benchmark dataset for insect pest recognition,' in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2019, pp. 8787-8796.
- [26] S. Ren, K. He, R. Girshick, and J. Sun, 'Faster r-cnn: Towards real-time object detection with region proposal networks,' Advances in Neural Information Processing Systems , vol. 28, 2015.
- [27] T.-Y. Lin, P. Doll´ ar, R. Girshick, K. He, B. Hariharan, and S. Belongie, 'Feature pyramid networks for object detection,' in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , 2017, pp. 2117-2125.
- [28] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu, and A. C. Berg, 'Ssd: Single shot multibox detector,' in Computer VisionECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part I 14 . Springer, 2016, pp. 21-37.
- [29] G. Batchuluun, J. Choi, and K. R. Park, 'Cam-can: Class activation map-based categorical adversarial network,' Expert Systems with Applications , vol. 222, p. 119809, 2023.
- [30] D. Reis, J. Kupec, J. Hong, and A. Daoudi, 'Real-time flying object detection with yolov8,' 2024. [Online]. Available: https: //arxiv.org/abs/2305.09972
- [31] C.-Y. Wang, I.-H. Yeh, and H.-Y. M. Liao, 'Yolov9: Learning what you want to learn using programmable gradient information,' 2024. [Online]. Available: https://arxiv.org/abs/2402.13616
- [32] T. Mikolov, K. Chen, G. Corrado, and J. Dean, 'Efficient estimation of word representations in vector space,' 2013. [Online]. Available: https://arxiv.org/abs/1301.3781
- [33] C. He, Y. Qiao, R. Mao, M. Li, and M. Wang, 'Enhanced litehrnet based sheep weight estimation using rgb-d images,' Computers and Electronics in Agriculture , vol. 206, p. 107667, 2023.
- [34] S. Coulibaly, B. Kamsu-Foguem, D. Kamissoko, and D. Traore, 'Explainable deep convolutional neural networks for insect pest recognition,' Journal of Cleaner Production , vol. 371, p. 133638, 2022.
- [35] M.-L. Huang, T.-C. Chuang, and Y.-C. Liao, 'Application of transfer learning and image augmentation technology for tomato pest identification,' Sustainable Computing: Informatics and Systems , vol. 33, p. 100646, 2022.