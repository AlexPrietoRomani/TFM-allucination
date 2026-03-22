---
id: arxiv-2111.00298
title: A fast accurate fine-grain object detection model based on YOLOv4 deep neural network
year: 2021
country: Internacional
source: ArXiv (cs.CV, cs.LG)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - agricultura de precisión
  - cultivos
  - frutales
  - artículo científico
  - ArXiv
---

## A fast accurate fine-grain object detection model based on YOLOv4 deep neural network

Arunabha M. Roy ∗ · Rikhi Bose · Jayabrata Bhaduri

Received: date / Accepted: date

Abstract Early identification and prevention of various plant diseases in commercial farms and orchards is a key feature of precision agriculture technology. This paper presents a highperformance real-time fine -grain object detection framework that addresses several obstacles in plant disease detection that hinder the performance of traditional methods, such as, dense distribution, irregular morphology, multi-scale object classes, textural similarity, etc. The proposed model is built on an improved version of the You Only Look Once (YOLOv4) algorithm. The modified network architecture maximizes both detection accuracy and speed by including the DenseNet in the back-bone to optimize feature transfer and reuse, two new residual blocks in backbone and neck enhance feature extraction and reduce computing cost; the Spatial Pyramid Pooling (SPP) enhances receptive field, and a modified Path Aggregation Network (PANet) preserves fine-grain localized information and improve feature fusion. Additionally, use of the Hard-Swish function as the primary activation improved the model's accuracy due to better nonlinear feature extraction. The proposed model is tested in detecting four different diseases in tomato plants under various challenging environments. The model outperforms the existing state-of-the-art detection models in detection accuracy and speed. At a detection rate of 70.19 FPS, the proposed model obtained a precision value of 90 . 33%, F1-score of 93 . 64%, and a mean average precision ( mAP ) value of 96 . 29%. Current work provides an effective and efficient method for detecting different plant diseases in complex scenarios that can be extended to different fruit and crop detection, generic disease detection, and various automated agricultural detection processes.

Keywords Real-time object detection · plant disease detection · deep neural network · improved YOLOV4 · computer vision

Arunabha M. Roy ( ∗ Corresponding author)

University of Michigan, Aerospace Engineering, Ann Arbor, MI 48109, U.S.A. E-mail: arunabhr.umich@gmail.com

Rikhi Bose

Mechanical Engineering, Johns Hopkins University, Baltimore, MD 21218, U.S.A.

Jayabrata Bhaduri

Capacloud AI, Deep Learning &amp; Data Science Division, Kolkata, WB 711103, India.

## 1 Introduction

In recent advancements in autonomous agricultural production, informatics is widely utilized commercially to enhance and estimate agricultural yields [1]. Early and accurate disease detection is critical for their prevention and cure, activation of intelligent sprayer systems, and in controlling autonomous pesticide spraying robots in large commercial farms and orchards. Exercising such measures result in the reduction of any growth disorders, minimizing pesticide application for pollution-free crop production [2], and consequently, large gains in production. With recent advancements of computer vision in precision agriculture technology, crop imaging, and disease detection protocol have become an integral part of collecting crop growth and health monitoring information [3]. The deep learning techniques have been utilized as an effective tool in agriculture [4] in a wide range of applications, such as but not limited to, crop and fruit classification [5], image segmentation in crops [6], crop detection [7] etc.

Presently, the majority of studies in crop informatics are geared towards deep learningbased image classification of crop diseases and pests [8,9]. Only a few studies [10,11] focus on plant diseases detection utilizing region suggestion. Compared to traditional machine learning, these models provide superior accuracy, however, due to slow detection speed, these approaches are not suitable for real-time detection in complex environment. In that regard, existing disease detection models have limited capability in detecting multi-scale disease distribution, in particular, fine-grain early diseases due to insufficient deep feature extraction. In the present work, a novel detection model is proposed based on an advanced computer vision algorithm that demonstrates superior performance in real-time accurate multi-scale plant disease detection in tomatoes.

Compared to the traditional machine learning models, deep learning algorithms have demonstrated higher accuracy in object detection [12]. The main drawback of these models is that they induce significant error in detecting densely distributed objects with occlusion and overlapping. Convolutional neural network (CNN) -based object detection models were developed to address these limitations. These models may be classified as two-stage or onestage detectors [13]. One of the well-known two-stage detectors is the Region Convolution Neural Network (RCNN) which includes fast/ faster-RCNN [14,15] and mask-RCNN [16]. These models are useful in crop and fruit detection, yield, growth evaluation, and automated agricultural management [17]. Although faster R-CNN composed of region proposal (RPN) and classification networks leads to a significant drop in detection time, these models can not perform real-time detection with high-resolution images.

More recently, the You Only Look Once (YOLO) algorithm [18,19,20,21] was proposed which unifies target classification and localization into a regression problem. Since the YOLO does not use RPN, it can directly perform regression to detect targets in an image which significantly increases detection speed. The YOLO model have been utilized in various complex detection tasks under challenging scenarios [22,23,24]. The more recent YOLOv4 has higher detection speed and performs with better precision and accuracy compared to YOLOv3 in different real-time object detection applications [25,26] including its application in improving autonomous detection [27,28]. However, the original YOLOv4 can provide low detection accuracy with a high number of missed detection and false object predictions due to its insufficient fine-grain feature extraction properties which is essential for early disease detection. Additionally, the YOLOv4 incurs high computational cost and longer training time that may not be suitable for in-field mobile computing devices.

To address the aforementioned shortcomings, in the present study, an improved version of the YOLOv4 algorithm [21] has been developed for real-time multi-scale disease detec-

tion. The YOLOv4 algorithm was modified to optimize both detection speed and accuracy. The model performance is verified by detecting objects under various challenging environments. The contributions of this paper are as follows: in order to improve feature transfer and reuse for small-target detection, CSPDarkNet53 [21] is modified by introducing DenseNet [29] in the last two feature layers. To reduce redundancy and computing cost, the number of network layers is reduced by modifying the convolution blocks. We propose a new residual CSP1n block in the backbone for the improvement of the feature extraction network. Moreover, an additional residual CSP2n block is integrated into modified path aggregation network (PANet) [30] to preserve fine-grain localized information, feature fusion of multi-scale semantic information, and further reduction of computing cost. In addition, the integration of spatial pyramid pooling (SPP) [31] block with the backbone of the proposed model enhances receptive field. Lastly, the novel Hard-Swish activation [32] has been used to enhance the nonlinear feature learning ability of the network model. This was found to increase the accuracy of the model substantially. The proposed detection model is tested in detecting four different diseases in tomato plants in various challenging conditions.

Four diseases are prevalent in tomato plants- early blight, late blight, Septoria spot, and leaf mold. In early phases, due to differences in size, color, cluster density, and other morphological characteristics for these diseases, real-time accurate detection is challenging for traditional methods. Moreover, erratic growth pattern, frequent high aspect ratio of the lesions, coexistence of multi-scale object classes, visual similarities and low distinguishable interface between infected areas and its surroundings, densely populated discreet form of patches, different characteristics in different stages of disease growth, and other critical factors offer additional challenges and difficulties for the object detection models. Also, most of the existing models are designed to detect diseases in higher length scales and are not efficient/ applicable in real-time detection. The model proposed herein outperforms the original YOLOv4 and existing state-of-the-art detection models in terms of both accuracy and speed in detecting all four disease classes. Apart from detecting large-scale diseases of different classes in complex scenarios, the modified model performs exceptionally well in detecting diseases at finer grain/ in very small patches. Therefore, current work provides an effective method for early detection of different plant diseases in complex scenarios which may be used in real-time detection of diseases in fields from portable mobile computing devices.

The paper is organized as follows: Section 2 introduces the YOLO framework; Section 3 describes the proposed network algorithm; object detection preliminaries including performance metrics, bounding box regression, and loss functions have been described in Section 4; Section 5 demonstrates the proposed model's superiority comparing its performance with state-of-the-art object detection models, specifically, original YOLOv3 and YOLOv4 models in tomato plane disease detection problem under various complex scenarios. The model's real-time detection performance in detecting four diseases in tomato plants is shown in Section 6. Several performance measures defined in Section 4 were utilized in sections 5 and 6. Finally, the conclusions and prospects of the current work have been discussed in section 7.

## 2 YOLOv4 network structure

In the present work, an improved YOLOV4 algorithm [21] is implemented for the purpose of plant disease detection. The YOLOv4 is a high-precision single-stage object detection model which transforms the object detection task into a regression problem by generating bounding box coordinates and assigning probabilities to each class. The YOLOv4 is an improved version of the original YOLO algorithm [18] and it's offsprings, YOLOv2 [19], and

Fig. 1 Schematic of the YOLOv4 network architecture consisting of CSPDarknet53 as the backbone, PANet as the neck with a regular YOLOv3 head.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de flujo de datos con una serie de bloques y lías de “ ” “ ”



YOLOv3 [20] in terms of detection speed and accuracy. As shown in Fig. 1, the complete network structure consists of three parts : a backbone for feature extraction, the neck for semantic representation of extracted features, and the head for prediction.

In the network architecture, the residual module is integrated into ResNet network structure [33] to obtain Darknet53. For further improvement of the network performance, crossstage partial network (CSPNet) [34] is combined considering its superior learning capability to form CSPDarkNet53 [21]. Different feature layer's information is inputted into the residual module which provides the higher-level feature maps as the output. This results in a significant decrease in network parameters, at the same time improving the residual feature information, and enhancing feature learning capability compared to the ResNet network. In the original YOLOv4 backbone, the SPP block [31] was integrated with CSPDarknet53 linked to the PANet [30], replacing the feature pyramid networks (FPN) [35] used in other variants of the YOLO. This resulted in a significant increase of the receptive field. The SPP applies an effective strategy for detecting objects of different scales. At first, the inputted feature layer is convoluted in SPP. Afterward, a maximum pool can be applied by pooling cores of a maximum of four different sizes. Pooled feature information obtained from the SPP is then concatenated and further convoluted which significantly increases the receptive field of the detection network. Obtained feature information fields from the backbone and the SPP is convoluted and then up-sampled in PANet resulting in twice the size of the inputted feature layer. To extract additional semantic features, the feature layers obtained from

Fig. 2 Schematic of YOLOv4 object detection algorithm for disease detection.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un **Flu [ ] [ ] [ ] [



the CSPDarknet53 are concatenated after convolution, then up-sampled followed by downsampling which is stacked with the remaining feature layers for enhancing the feature fusion process, as shown in Fig. 1. Thus, the neck is leveraged in backbones for the extraction of rich semantic features that are used for accurate predictions. Finally, for the specific inputted image size, the YOLOv4 model can predict bounding boxes at the detection head at three different scales. In the first step, the inputted image is discretized into N × N equally spaced grids. The model generates B predictive bounding boxes and a corresponding confidence score if the target belongs within a grid-cell. The best bounding box prediction from each of these scales is filtered by non-maximum suppression (NMS) [15] algorithm before the final bounding box can be obtained. The prediction process is shown in Fig. 2. In order to help the model learn various types of distribution of a given image in challenging circumstances, in particular, noise, complex backgrounds etc., YOLOv4 introduces CutMix [36], mosaic augmentations [21], and self-adversarial training (SAT) [21] methods to expand the dataset. Additionally, drop block regularization [37] for learning spatially discriminating features and class label smoothing [21] for better generalization of a dataset can be employed.

Although the aforementioned techniques can effectively improve the detection accuracy of the model, the plant disease detection task faces several specific challenges due to complex environments, in particular, densely populated fine-grain disease, irregular geometric morphology of infected areas, coexistence of multi-scale infected lesions, similarity of texture of affected areas and surroundings, varying lightening conditions, overlapping and occlusion, etc. Thus original YOLOv4 can provide low detection accuracy that may lead to a high number of missed detection as well as false object prediction due to insufficient fine-grain feature extraction for the multi-scale disease detection problem. Additionally, the YOLOv4 incurs high computational cost and longer training time that may not be suitable for on-field mobile devices.

## 3 The proposed model network structure

In order to resolve the aforementioned issues related to real-time disease detection procedure, in the present study, the state-of-the-art YOLOv4 algorithm is improved and optimized for accurate predictions of fine-grain image multi-attribute detection in complex background environments. In the later sections, efficacy of the model is demonstrated by detecting different tomato plant diseases at real-time detection speeds in complex backgrounds. The complete schematic of the improved YOLOv4 network architecture is shown in Fig. 3 and each modification is briefly discussed in this section. The proposed modifications include the proper selection of activation functions for the backbone and the neck for better accuracy, inclusion of the DenseNet [29] transitional block in front of the residual blocks of the original CSPDarknet53, two new residual blocks in the backbone and the neck to enhance feature extraction network and to reduce the computing cost, integration of the SPP [31] block, and the implantation of the modified PANet [30] in the neck part of the network to preserve fine-grain localized information. The original YOLOv3 head is used as the detection head. With an inputted image size of 416 × 416 × 3, the proposed model can predict bounding boxes at the detection head at three different scales, 52 × 52 × 24, 26 × 26 × 24, and 13 × 13 × 24. It is found that with the aforementioned modifications, the model outperforms other state-of-the-art detection models, specifically at detecting fine-grain tomato plant diseases.

## 3.1 Improvement of feature extraction network in the backbone

The residual model in the CSPDarknet53 helps the network to learn more expressive features at the same time reducing the number of trainable parameters to make it faster for real-time detection. In the original YOLOv4 model, the residual unit (Res-unit) carries out 1 × 1 convolutions, followed by 3 × 3 convolutions, and then weights the two outputs containing extracted feature information at the end. In the CSPDarknet53 network, feature layers of the inputted images are continuously down-sampled via the convolution operations to extract fine-grained rich semantic information. As the last three layers contain relatively higher semantic information, these are passed to the SPP and the PANet. The last feature layers contain the finest feature information, and is connected to the SPP. The other two layers are integrated into the PANet as shown in Fig. 3. Although the residual module in the YOLOv4 reduces computational cost, this further reduces computational memory requirement for high-resolution real-time detection. Therefore, a new residual block, CSP1n [25] ( n is the number of residual weighting operations) is proposed in the CSPDarkNet53 network structure (see Fig. 3) to improve detection speed and performance. In the proposed CSP1n residual block, the input features are divided into two parts. The first part of the residual block acts as the trunk which performs 1 × 1 convolution followed by another 1 × 1 convolution to adjust the channel after entering the main residual unit as in Fig. 3(c). To enhance feature extraction even further, it then performs 3 × 3 convolution, whereas, the second part acts as a residual edge for the convolution. At the end of the CSP1n block, these two parts are concatenated resulting in additional feature layer information. In the present study, CSP1n modules replace the CSP8 and CSP4 in an improved backbone. Finally, 1 × 1 convolution performed to integrate the channel after stacking. Implementation of the CSP1n modules in the modified CSPDarknet53 significantly improves the detection accuracy for the feature dataset used herein.

Fig. 3 Schematic of (a) the proposed network architecture for plant disease detection consisting of DenseCSPDarknet53 integrating SPP as the backbone, modified PANet as a neck with a regular YOLOv3 head; (b) CSPn ; (c) CSP1n ; (d) CSP2n blocks.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de flujo de datos con una serie de bloques y lías de “ ” “ ”



## 3.2 Implementation of the Hard-swish activation for better accuracy

One of the important aspects of developing an object detection model is to select appropriate activation function for better accuracy and performance [38]. Activation functions can be characterized by properties such as, derivative, monotonic behavior, etc [39]. In this regard, Leaky Rectified Linear Unit (Leaky-ReLU) [40], Mish [41] are widely used activations in dense object detection models. However, using the Swish function [38] as a drop-in replacement for ReLU demonstrates significant improvement of the neural network performance [38,42,43]. The Swish function is expressed as, swish ( x ) = x . s ( x ) . Due to presence of sigmoid function s ( x ) , it increases computational cost. Therefore, the Hard-swish activation function [32], where s ( x ) in the Swish function is replaced with its piece-wise linear hard analog, ReLU 6 ( x + 3 ) , is used instead. The function is,

$$H - s w i s h ( x ) = x . \frac { R e L U ( x + 3 ) } { 6 }$$

Due to H-swish's unique property of non-monotonicity, it can improve the performance of the detection model for different datasets. Additionally, due to H-swish is bounded below and its property of unboundedness, it helps remove the saturation problem of the output neurons and improve network regularization. Moreover, it is computationally faster than Swish and beneficial for training as it helps to learn more expressive features that are more robust to noise [32]. Hard-swish activation is used in different object detection algorithms which substantially reduces the number of memory accesses by the model [44,45]. HardSwish function is used herein as the primary activation in both the backbone and the neck with significant accuracy gain on the dataset under consideration. Moreover, the detection speed is increased and computational cost is substantially reduced (see Section 5.1.1).

## 3.3 Implementation of the DenseNet for better feature transfer and reuse

During object detection, the YOLOv4 algorithm reduces the feature maps during training. Due to several steps of convolution and down-sampling procedures, important feature information of the training sample can get lost during transmission. To preserve important feature maps and to reuse critical feature information more efficiently, the DenseNet framework [29] is proposed where each layer is connected to other layers feeding forward. The main advantage of this framework is that the n -th layer is able to receive required feature information Xn from all previous layers as inputs.

$$X _ { n } = H _ { n } [ X _ { 0 } , X _ { 1 } , \dots , X _ { n - 1 } ]$$

Here, Hn is the spliced feature map function for layer n ; [ X 0 , X 1 , ..., Xn -1 ] is the feature map of layers X 0 , X 1 , ..., Xn -1. Such formulation allows the DenseNet to reduce the number of parameters, enhance feature propagation and facilitate feature reuse. Due to the complexity of the image dataset, in particular, densely populated distribution and coexistence of multiscale disease classes, it is critical to use the dense block to facilitate better feature transfer and gradient propagation throughout the network. Additionally, it may mitigate over-fitting to some degree. In the proposed model, the last two residual blocks, CSP8 and CSP4 in the original CSPDarknet53 are modified to Dense-CSP1-4 and Dense-CSP1-2 by adding dense connection blocks to enhance feature propagation. Additionally, the redundant feature operations is reduced and the calculation speed is increased by removing the CSPn blocks. The schematic of the proposed dense blocks and corresponding network parameters are shown in Fig. 4(a, b). It is evident that the network structure is improved by replacing 26 × 26 and 13 × 13 down-sampling layers by the DenseNet structure. In the dense block-1, transfer feature map function H 1 nonlinearly transforms the X 0 , X 1 , ..., Xn -1 layers, where each layer Xi is comprised of 64 feature layers each with resolution 26 × 26 pixels as shown in Fig. 4(a). The first dense block before the CSP1-4 performs feature propagation and layer splicing on the layers with 26 × 26 resolution which results in the final forward propagating feature layer of size 26 × 26 × 512. Similarly, feature propagation and layer splicing are performed on the layers with 13 × 13 resolution which result in the final forward propagating feature layer of resolution 13 × 13 × 1024 by the second dense block before the CSP1-2 as shown in Fig. 4-(b). The Dense-CSPDarknet53 configuration ensures that later feature layers obtain features from the previous layers during training when inputted images are transferred to the lower resolution layers of the network reducing the feature loss. Moreover, different low-resolution convolution layers can reuse the feature between them which increases the feature usage rate.

Fig. 4 Schematic of (a) dense block-1; (b) dense block-2 in Dense-CSPDarknet53; (c) SPP block and corresponding network parameters of the proposed disease detection model.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de flujo de “ ” ” ” ”



## 3.4 Enhancement of the receptive field

To enhance the receptive field and separate important context features during object detection, an SPP block [31] is tightly integrated with the last residual block (CSP1-2) of the Dense-CSPDarknet53 backbone structure as shown in Fig. 3. The SPP applies an effective strategy in detecting objects at different length scales. It replaces the pooling layer (after the last convolutional layer) with a spatial pyramid-type pooling layer. In the proposed modification, the SPP retains the spatial dimension of the output, as a maximum pooling is applied to a sliding kernel of sizes 5 × 5, 9 × 9, and 13 × 13 with a stride of 1 as shown in Fig. 4-(c). A relatively large 13 × 13 max-pooling effectively increases the receptive field of the backbone.

## 3.5 Modified PANet to preserve fine-grain localized information

In the object detection neural network model developed herein, earlier layers extract localized texture and pattern information to build up the semantic information needed in the later layers. However, with increasing layers of the residual blocks, interconnectivity among layers become more complex, especially due to the dense connection block where each layer

Fig. 5 Different image augmentation methods: (a) original image, (b) 90 o ACW rotation, (c) 180 o ACW rotation, (d) 270 o ACWrotation, (e) horizontal mirror projection, (f) colour balancing, (g-i) brightness transformation, and (j) blur processing.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



is connected to all previous layers. This requires fine-tuning of the localized information. In order to address this issue, the PANet [30] is used in the neck part of the proposed model which shortens the path of high and low fusion for the multi-scale feature pyramid map. The PANet fuses information from all layers using element-wise max operation and has more flexible ROI pooling compared to the FPN [35]. To disseminate information at lower levels, a bottom-up path augmentation is used in the PANet as shown in Fig. 3. The CSP2n module [25] is added to the PANet which divides the basic feature layer into two parts and reduces the use of repeated gradient information through cross-stage operation as shown in Fig. 3-(d). This further improves multi-scale local feature fusion with global feature information. The introduction of the CSP2n improves the feature extraction flow which leads to a notable increase in detection accuracy and speed (see Section 5.1.2).

Apart from the above mentioned modifications of the model architecture, dropout in the feature map [46], CIoU loss function [47], Cross mini Batch Normalization [48], cosine annealing scheduler [49], and dropblock regularization [50], are utilized to improve the performance of the proposed model. Additionally, data augmentation procedures, such as, rotation, mirror projection, color balancing, brightness transformation, blur processing are employed to increase the variability of inputted images obtained from different environments to augment robustness of the detection model as depicted in Fig. 5.

## 4 Preliminaries of an object detection problem

In this section, some relevant detail associated with the object detection problem formulation, such as, the objective of the model, preliminaries of implementation including the loss functions relevant to the object detection problem, and model performance metrics are briefly described.

## 4.1 Bounding box regression

In dense object detection models, bounding box regression is a widely applied approach to predict the localization boxes on input images. In this regard, a scale-invariant evaluation metric called intersection over union (IoU) was proposed to evaluate the accuracy of target object detection,

$$I o U = \frac { \mathbb { B } \cap \mathbb { B } _ { g t } } { \mathbb { B } \cup \mathbb { B } _ { g t } }$$

where, B ∩ B gt and B ∪ B gt are defined as the intersection and union between areas of the predicted box B and the ground truth bounding box B gt of the object, respectively. However, IoU loss only considers the overlapping bounding boxes. The non-overlapping cases are not taken into account. Additionally, traditional IoU loss has the limitation on gradient disappearance in case of an absence of intersection between target and prediction boxes. To circumvent these issues, generalized IoU ( GIoU ) [51] was proposed which considers the shape, area, and orientation of the overlapping bounding boxes. The GIoU loss is expressed as,

$$L _ { G I o U } = 1 - I o U + \frac { | C - \mathbf B \cup \mathbf B _ { g t } | } { C }$$

Where C is the smallest convex hull between B and B gt . However, GIoU is not computationally cost effective. For better performance, distanceIoU ( DIoU ) [47] loss was introduced which measures the proximity of the target and prediction boxes by introducing a metric parameter in predicting boundary box regression. The expression for the DIoU loss is,

$$L _ { D I o U } = 1 - I o U + \frac { \rho ^ { 2 } ( \mathbf b , \mathbf b _ { \mathbf g } ) } { c ^ { 2 } } .$$

Here, b and bgt are the centroids of B and B gt , respectively; d : = r ( b , bgt ) is the distance between central points of B and B gt , and c is the length of the diagonal of the smallest enclosing box covering the two boxes as shown in Fig. 6-(b). The penalty term r 2 ( b , bgt ) c 2 in Eq. 5 minimizes the normalized distance between central points of the two bounding boxes, leading to faster convergence than the GIoU loss. Subsequently, complete IoU ( CIoU ) [47], an extension of the DIoU loss, was introduced in YOLOv4 to better the accuracy and convergence speed for the target bounding box prediction process. CIoU loss simultaneously considers three geometric metrics that are typically ignored: overlapping area, the distance between centers, and the aspect ratio in the bounding box regression in object detection [47]. CIoU loss was formulated incorporating consistency of the aspect ratio parameter, v , and a positive trade off parameter, a based on DIoU loss which is expressed as,

$$L _ { C l o U } = 1 - I o U + \frac { \rho ^ { 2 } ( \mathbf b , \mathbf b _ { \mathbf g } ) } { c ^ { 2 } } + \alpha v .$$

$$v = \frac { 4 } { \pi ^ { 2 } } \left ( t a n ^ { - 1 } \, \frac { w _ { g t } } { h _ { g t } } - t a n ^ { - 1 } \, \frac { w } { h } \right ) ^ { 2 } ; \quad \alpha = \frac { v } { ( 1 - I o U ) + v ^ { \prime } }$$

Here, wgt , w and hgt , h are the widths and heights of the ground truth and prediction bounding boxes, respectively as shown in Fig. 6 -(b). In Eq. 7, v → 0 with increase in w / h . For consistent predictions, w / h is a chosen parameter for a specific YOLOv4 object detection model.

h

Fig. 6 (a) Schematic of offset regression for target bounding box prediction process; (b) schematic of CIoU loss for bounding box regression in YOLOv4 object detection algorithm.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un [ ] [ ] [



## 4.2 Confidence score

During object detection, when the center of the target-class ground truth falls within a specified grid-cell, it detects the target as an object of a particular class. Each grid predicts B bounding boxes with confidence scores and corresponding C class conditional probabilities for each target class. The confidence scores can be expressed as,

$$c o n f i d e n c e = p _ { r } ( o b j e c t ) \times I o U _ { p r e d } ^ { t r u t h } \wedge \vee _ { r } ( o b j e c t ) \in [ 0 , 1 ]$$

During the object detection process, pr ( object ) = 1 is prescribed in the framework when the target class falls within the YOLO grid-cell, or otherwise, pr ( object ) = 0. Coalescing between the reference and the predicted bounding box is quantified by IoU truth pred . The value of pr ( object ) indicates the accuracy of the bounding-box prediction when the target class is detected within the cell.

The prediction process for the target bounding box is shown in Fig. 6. The dashed box in Fig. 6-(a) is the initial bounding box. The relationship between the initial bounding box to the predicted bounding box can be expressed as,

$$b _ { x } = \sigma ( t _ { x } ) + c _ { x } ; \quad b _ { y } = \sigma ( t _ { y } ) + c _ { y } .$$

$$b _ { w } = p _ { w } e ^ { t _ { w } s _ { w } } ; \quad b _ { h } = p _ { h } e ^ { t _ { h } } .$$

where, ( bx , by ) and ( bw , bh ) are the centroid and size of the predicted bounding box; ( cx , cy ) and ( pw , ph ) are the centroid and size of the bounding box on the feature map; ( tx , ty ) and ( tw , th ) represent the center offset of the bounding box from the network prediction and corresponding scaling size.

## 4.3 Loss function

The loss or cost function ( x ) is important as it dictates the performance of the trained model. The loss function D l for an object detection task such as in YOLO can be defined as,

$$\Delta _ { l } = \Theta _ { c o r } + \Theta _ { l o U } + \Theta _ { c l } .$$

D l consists of mainly three types of error components. The coordinate prediction error, Q cor is defined as:

$$\Theta _ { c o r } = \kappa _ { c o r } \sum _ { i = 1 } ^ { N ^ { 2 } } \sum _ { j = 1 } ^ { B } \delta _ { i j } ^ { o b j } [ ( x _ { i } - \bar { x } _ { i } ) ^ { 2 } + ( y _ { i } - \bar { y } _ { i } ) ^ { 2 } ] + \kappa _ { c o r } \sum _ { i = 1 } ^ { N ^ { 2 } } \sum _ { j = 1 } ^ { B } \delta _ { i j } ^ { o b j } [ ( w _ { i } - \bar { w } _ { i } ) ^ { 2 } + ( h _ { i } - \bar { h } _ { i } ) ^ { 2 } ] \ ]$$

Here, N 2 is the total number of grid points in the inputted image, k cor corresponds to the weight associated with Q cor , B is the total number of bounding boxes associated with each grid, ( xi , yi ) are the true center coordinates of the object, ( ¯ xi , ¯ yi ) are the center coordinates of the predicted bounding box; ( wi , hi ) and ( ¯ wi , ¯ hi ) are the width and height of the truth and the predicted bounding boxes, respectively. The function d obj i j = 1 if the target class lies in the bounding box j generated by grid i , else d obj i j = 0. The IoU error term, Q IoU is given as follows.

$$\Theta _ { I o U } = \sum _ { i = 1 } ^ { N ^ { 2 } } \sum _ { j = 1 } ^ { B } \delta _ { i j } ^ { o b j } ( C _ { i } - \bar { C } _ { i } ) ^ { 2 } + \kappa _ { n b } \sum _ { i = 1 , j = 1 } ^ { N ^ { 2 } } \delta _ { i j } ^ { o b j } ( C _ { i } - \bar { C } _ { i } ) ^ { 2 }$$

Here, k nb is a parameter corresponding to weight associated with Q IoU , Ci is the true confidence in object detection, and ¯ Ci is the confidence score of the prediction. Lastly, the classification error term Q cl is given by,

$$\Theta _ { c l } = \sum _ { i = 1 } ^ { N ^ { 2 } } \sum _ { j = 1 } ^ { B } \delta _ { i j } ^ { o b j } \sum _ { c \in c l a s s e s } ( p _ { i } ( c ) - \bar { p } _ { i } ( c ) ) ^ { 2 }$$

In Eq. 14, c is the class associated with target detection; pi ( c ) is the true probability of detecting the object of class c in grid i ; ¯ pi ( c ) is the probability score from the prediction. Q cl for a particular grid i is obtained from the sum of classification errors due to all classified objects residing in that grid-cell.

## 4.4 Evaluation metrics

Some traditional evaluation parameters, such as, precision-recall ( PR ) curve, F-1 score, average precision (AP), or mean average precision (mAP) can be used [52] to measure the performance of an object detection model.

For binary classification, sample data can be classified into four different categories: true positive (TP), false positive (FP), true negative (TN), and false negative (FN), based on the true class and the model predicted class of the target object. From the quantities defined above, Precision ( P ) and Recall ( R ) can be defined as

$$P = \frac { T P } { ( T P + F P ) } ; \quad R = \frac { T P } { ( T P + F N ) }$$

From Eq. 8, one can infer that P represents prediction results of relevant instances. R refers to correctly classified results out of the total relevant instances. Both higher P and R indicate lower FN value. For a particular set of training sample, the precision-recall curve ( P -R curve) can be constructed from the precision (in the ordinate) and recall data (in the abscissa) for a particular classifier. From the relation between P and R , F1-score is defined which indicates the degree of precision of the object detection model. From Eq. 8, the F1score can be obtained as,

$$F _ { 1 } = \frac { 2 P R } { ( P + R ) } .$$

AP is equal to the area under the P -R curve.

$$A P = \int _ { 0 } ^ { 1 } P ( R ) \, d R .$$

High AP corresponding to a large area under the PR curve indicates accurate prediction of an object class by a detection model. Additionally, AP 50:95 is the average precision over the range of IoU=0 . 50 : 0 . 05 : 0 . 95; AP 50 and AP 75 are AP s at IoU thresholds 50% and 75%, respectively; APS , APM , and APL correspond to the detection accuracy of small, medium, and large objects, respectively, for the presently studied detection problem. The mAP is the average of all APs for a particular class which can be expressed as,

$$m A P = \frac { 1 } { N } \sum ^ { N } A P$$

## 5 Results &amp; Discussion

The state-of-the-art YOLOv4 algorithm is utilized to develop an accurate real-time highperformance image detection model on a single GPU. In this section the proposed model is tested on the tomato plant disease detection problem. A flowchart of the detection model workflow methodology is shown in Fig. 7. At first, 300 images from each of the four different tomato plant diseases (i.e., early blight, late blight, Septoria leaf spot, and leaf mold) are collected from the publicly available popular Kaggle PlantVillage Dataset [53] to construct a dataset consisting of 1200 images. To improve robustness and avoid over-fitting during training, the dataset is expanded ten folds using different image augmentation procedures to obtain the custom dataset of 12,000 images. For image annotation of the target classes in the custom dataset, a Python-based open-source script, LabelImg [54] is used which saves the annotations as XML files and organizes them into PASCAL VOC format. Each XML file contains information of the target class and corresponding bounding box coordinates for the training image dataset. From the custom dataset, a total of 8,400, 1,800, and 1,800 are randomly chosen as training, validation, and test images, respectively. The model is trained through a transfer learning method initialized from a pre-trained weights-file [55]. Training and testing are performed on the local system utilizing a single NVIDIA GeForce RTX 2080 GPU. Computing resources and DNN environment specifications used for these purposes are listed in Table 1.

Configuration parameters, such as, number of channels, momentum value, decay regularization, etc. are same as in the original YOLOV4 model. Primary hyperparameters used for training are summarized in Table 2.

Fig. 7 Flowchart of the overall workflow methodology for the proposed detection model.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de flujo de datos, que representa el proceso de **E I



Table 1 Local computing resources and DNN environments

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: OS, Configuration Parameter: Windows 10 Pro 64.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: CPU, Configuration Parameter: Intel Core i5.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: RAM, Configuration Parameter: 8 GB DDR4.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: GPU, Configuration Parameter: NVIDIA GeForce RTX 2080.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: GPU acceleration env., Configuration Parameter: CUDA 10.2.89.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: GPU accelerated DNN lib., Configuration Parameter: cuDNN 10.2 v7.6.5.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: Python distrib., Configuration Parameter: Anaconda 3 2019.10.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: ML lib., Configuration Parameter: Keras, Tensorflow, PyTorch.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: Int. development env., Configuration Parameter: Visual Studio comm. v15.9 (2017).
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Testing Environment: Comp. Vision lib., Configuration Parameter: OpenCV 4.5.1-vc14.
Table 2 Initial configuration parameters of the proposed detection model

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Input size of image: 416 × 416, Batch: 16, Subdivision: 4, Channels: 3, Momentum: 0.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Input size of image: Class coeff., Batch: Obj coeff., Subdivision: Shear, Channels: Mosaic, Momentum: Mix-up.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Input size of image: 0.5, Batch: 1, Subdivision: 0, Channels: 1, Momentum: 0.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Input size of image: Initial learning rate, Batch: Decay, Subdivision: Classes, Channels: Filters, Momentum: Training steps.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Input size of image: 0.001, Batch: 0.005, Subdivision: 4, Channels: 27, Momentum: 85,000.
Table 3 Comparison of network performance considering different activation functions in YOLO backboneneck combinations with integrated SPP plugin for anchors of 416 × 416 input resolution tested in NVIDIA GeForce RTX 2080 GPU. All APs are in %.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: CSPDarknet53+L-ReLU, Neck+ Activation: PANet+L-ReLU, AP: 60.3, AP 50: 87.6, AP 75: 74.9, AP S: 43.5, AP M: 67.3, AP L: 66.6, FPS: 67.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: CSPDarknet53+Mish, Neck+ Activation: PANet+L-ReLU, AP: 64.2, AP 50: 92.8, AP 75: 78.2, AP S: 48.3, AP M: 63.7, AP L: 70.5, FPS: 63.6.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: CSPDarknet53+H-swish, Neck+ Activation: PANet+H-swish, AP: 65.8, AP 50: 93.1, AP 75: 77.5, AP S: 49.9, AP M: 61.2, AP L: 65.9, FPS: 78.2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: D-CSPDarknet53+L-ReLU, Neck+ Activation: PANet+L-ReLU, AP: 67.3, AP 50: 94.5, AP 75: 76.7, AP S: 46.5, AP M: 69.8, AP L: 64.6, FPS: 61.2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: D-CSPDarknet53+Mish, Neck+ Activation: PANet+L-ReLU, AP: 70.1, AP 50: 94.9, AP 75: 78.8, AP S: 51.5, AP M: 71.5, AP L: 66.7, FPS: 59.7.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: D-CSPDarknet53+Mish, Neck+ Activation: PANet+Mish, AP: 71.5, AP 50: 95.7, AP 75: 79.2, AP S: 52.8, AP M: 69.9, AP L: 68.2, FPS: 58.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: D-CSPDarknet53+H-swish, Neck+ Activation: PANet+Mish, AP: 74.8, AP 50: 96.1, AP 75: 82.2, AP S: 71.8, AP M: 76.9, AP L: 51.7, FPS: 67.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + Activation: D-CSPDarknet53+H-swish, Neck+ Activation: PANet+H-swish, AP: 79.6, AP 50: 96.3, AP 75: 91.6, AP S: 73.6, AP M: 82.9, AP L: 89.5, FPS: 70.2.
## 5.1 Detection accuracy of the proposed model

Several issues can hinder the performance of the YOLOv4 model in detecting diseases in tomato plants, such as, densely populated fine-grain diseases, irregular geometric morphology of infected areas, coexistence of multi-scale disease spots, similarity of color textures of infected areas and leaves, and varying lightening conditions resulting in low detection accuracy, a high number of missed detections, and false object prediction. In order to overcome such issues, modifications of the detection model proposed in Section 3 yields improved feature map in complex zones increasing the accuracy of the bounding boxes.

## 5.1.1 Influence of different activation functions

To obtain the best detection model, the accuracy and detection speed for different combinations of the backbone structure and the neck configuration are tested. Three activation functions ( Leaky-ReLU, Mish, H-swish) are chosen for the backbone and neck parts of the model and all possible combinations are considered in comparing different precision parameters (i.e., AP, AP50, AP75, AP S , AP M , and AP L ) and corresponding detection speed. Results are presented in Table .3. The target confidence and IoU threshold were prescribed as 0.3 and 0.5, respectively. The Leaky-ReLU as the primary activation function in both backbone and neck parts of the detection model provides the least accurate model among all the variants. Compared to Leaky-ReLU, implementation of the Mish activation function increases the AP values at the expense of detection speed. The accuracy is further improved upon implementation of dense blocks in the backbone for both Leaky-ReLU and Mish activation functions. The dense block provides significant improvement in detection accuracy of the model for both cases while the detection speed is slightly compromised. However, together with dense blocks, implementation of the H-swish as the primary activation function in both backbone and neck provides the best results in terms of detection accuracy and speed as shown in Fig. 8-(a). Upon using the H-swish function instead of the Leaky-ReLU as the activation, a significant gain in accuracy is obtained on the custom dataset as AP increases from 60.3% to 79.6%, AP50 increases from 87.6% to 96.3%, AP75 increases from 74.9% to 91.6%, AP S increases from 43.5% to 73.6% and AP M increases from 67.3% to 82.9%; AP L increases

Table 4 Influence of CSP1n and CSP2n blocks on the network performance for the combinations of YOLO backbone-neck add-in considering H-swish as primary activation function with integrated SPP plugin for anchors of 416 × 416.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + add-in: CSPDarknet53, Neck +add-in: PANet, AP: 65.8, AP 50: 93.1, AP 75: 77.5, AP S: 49.9, AP M: 61.2, AP L: 65.9, FPS: 78.2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + add-in: D-CSPDarknet53, Neck +add-in: PANet, AP: 74.8, AP 50: 96.1, AP 75: 78.2, AP S: 51.3, AP M: 66.7, AP L: 65.7, FPS: 54.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + add-in: D-CSPDarknet53+CSP1- n, Neck +add-in: PANet, AP: 77.5, AP 50: 96.2, AP 75: 81.5, AP S: 63.9, AP M: 68.2, AP L: 70.9, FPS: 66.2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + add-in: CSPDarknet53, Neck +add-in: PANet+CSP2- n, AP: 73.8, AP 50: 95.6, AP 75: 71.2, AP S: 54.8, AP M: 67.9, AP L: 74.7, FPS: 78.9.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Backbone + add-in: D-CSPDarknet53+CSP1- n, Neck +add-in: PANet+CSP2- n, AP: 79.6, AP 50: 96.3, AP 75: 91.6, AP S: 73.6, AP M: 82.9, AP L: 89.5, FPS: 70.2.
Fig. 8 Comparison barchart of different precision parameters and detection speed (in FPS) for (a) different activation functions; (b) different combinations of CSP1n in backbone and CSP2n in neck of the detection model.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de barra que compara la **P [ ] [ ] [ ]



from 66.6% to 89.5% as shown in Table 3. Improvement of different AP values also indicates a stronger nonlinear feature learning capability with the H-swish function compared to Leaky-ReLU and Mish functions. Moreover, with the introduction of dense blocks, integration of the SPP module, and modification of the PANet in the proposed model, the fine-grain feature transfer and reuse improve. This leads to improved detection accuracy for small and medium object detection (i.e., AP S and AP M ) on the feature data set. Regarding detection speed, using the Mish activation for both backbone and neck adversely affects the detection speed compared to the Leaky-ReLU. However, H-swish activation provides the fastest detection as the detection speed increases by 14.7% compared to the Leaky-ReLU activation. Evidently, the H-swish activation function provides superior performance (both detection accuracy and speed) on the disease dataset.

## 5.1.2 Influence of residual blocks

The influence of inclusions of the CSP1n in the backbone and the CSP2n in the modified PANet on the network performance is reflected in the accuracy measures reported in Table.4. For comparison, five different combinations of backbone and neck are considered

Table 5 Comparison of precision, recall, F1-score, mAP, and detection speed (in FPS) between proposed model (improved YOLOv4) and other state-of-the-art models: Faster R-CNN, RetinaNet, SSD, Mask R-CNN, Cascade R-CNN, YOLOv3, and YOLOv4 tested in NVIDIA GeForce RTX 2080 GPU. Bold highlights the best result obtained from corresponding model performances.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Faster R-CNN, P (%): 26.27, R (%): 42.39, F1-score (%): 55.73, mAP (%): 59.17, Dect. time (ms): 44.42, FPS: 22.51.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: RetinaNet, P (%): 43.28, R (%): 51.77, F1-score (%): 60.42, mAP (%): 63.78, Dect. time (ms): 30.52, FPS: 32.82.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: SSD, P (%): 65.45, R (%): 76.34, F1-score (%): 80.97, mAP (%): 82.52, Dect. time (ms): 25.71, FPS: 38.39.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Mask R-CNN, P (%): 63.52, R (%): 75.35, F1-score (%): 80.23, mAP (%): 83.61, Dect. time (ms): 55.82, FPS: 19.75.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Cascade R-CNN, P (%): 70.42, R (%): 79.25, F1-score (%): 84.13, mAP (%): 86.61, Dect. time (ms): 35.32, FPS: 28.13.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv3, P (%): 73.98, R (%): 88.01, F1-score (%): 80.38, mAP (%): 89.19, Dect. time (ms): 16.52, FPS: 60.57.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4, P (%): 81.39, R (%): 92.14, F1-score (%): 86.44, mAP (%): 92.84, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model, P (%): 90.33, R (%): 97.2, F1-score (%): 93.64, mAP (%): 96.29, Dect. time (ms): 14.29, FPS: 70.19.
with or without the additional residual blocks. Without the use of the CSP1n and CSP2n , the detection model provides the worst results in terms of accuracy among all variants. Introducing dense and CSP1n blocks in backbone increases all accuracy parameters, in particular, the AP50 and AP S as shown in Fig. 9-(b). Such a combination though reduces the detection speed compared to the other variants. However, implementation of the CSP2n in addition to the CSP1n and dense blocks, both detection accuracy and speed increase; AP, AP75, AP S , AP M and AP L increase by 2.1%, 14.8%, 9.7%, 14.7% and 18.6%, respectively. Also, 6.3% increase in detection speed is obtained as shown in Fig. 9-(b). Evidently, use of the CSP1n block in the backbone enhances feature extraction and use of the CSP2n block in the PANet enhances the learning capability of semantic features increasing AP values and detection speed. The comparisons demonstrate the effectiveness of the CSP1n and CSP2n modules in the proposed model.

## 5.2 Comparison with existing state-of-the-art models

Detection performance of the proposed model is evaluated by comparing different metrics for accuracy ( P , R , F 1 -score, mAP at IoU ≥ 0 . 5, and detection speed as in section 4.2) with existing state-of-the-art models for object detection [56]. YOLOv3, YOLOv4, and the proposed model (improved YOLOv4) along with five additional detection models: Faster RCNN [15], RetinaNet [57], single shot multi-box detector (SSD) [58], Cascade R-CNN [59], and the Mask R-CNN [16] are trained and tested on the custom disease dataset in an open-source OpenMMLab object detection toolbox (MMDetection) [60] based on PyTorch. The hyperparameters were kept as consistent as possible while comparing other models with our proposed model. The performance metrics for the 8 models considered herein are tabulated in Table 5. The bar chart plotted in Fig. 9 shows that the performance of the Faster R-CNN and the RetinaNet is inferior to other models on the custom disease dataset for all metrics with precision values of 26 . 27% and 43 . 28%, respectively. The SSD and the Mask R-CNN demonstrate better performance compared to the RetinaNet with 20 . 55% and 19 . 81% increase in F 1 -score and 18 . 74% and 19 . 83% increase in mAP , respectively. Additionally, the detection speed recorded for Faster R-CNN, RetinaNet, SSD, Mask R-CNN,

Fig. 9 Comparison bar chart of precision, recall, F1-score, mAP, and detection speed (in FPS) between proposed model (improved YOLOv4) and other state-of-the-art models: Faster R-CNN, RetinaNet, SSD, Mask R-CNN, Cascade R-CNN, YOLOv3, and YOLOv4.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de barra que compara el rendo de diferentes modelos de “ ” ” ” ”



Table 6 Comparison of IoU, F1 Score, final loss, detection speed and average detection time between YOLOv3, YOLOv4, and proposed model.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Detection model: YOLOv3, IoU: 0.767, F1-score: 0.803, Validation loss: 13.31, Detection time (ms): 16.52, Detection speed (FPS): 60.57, Training time: 7.35h.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Detection model: YOLOv4, IoU: 0.872, F1-score: 0.864, Validation loss: 8.92, Detection time (ms): 15.72, Detection speed (FPS): 63.61, Training time: 6.14h.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Detection model: Proposed model, IoU: 0.935, F1-score: 0.936, Validation loss: 2.29, Detection time (ms): 14.29, Detection speed (FPS): 70.19, Training time: 3.98h.
and Cascade R-CNN are relatively low indicating limitation of these models for real-time on-field object detection tasks at high resolution. Although the Cascade R-CNN shows some improvement in detection accuracy compared to the previous four models, performance parameters obtained from these models are significantly lower compared to the versions of the original YOLO (i.e., YOLOv3 and YOLOv4) and the proposed detection model for the custom disease dataset used herein. For example, YOLOv4 yields 10 . 97% and 12 . 89% increase in precision and recall values compared to the Cascade R-CNN. However, our proposed model is superior to YOLOv4 with 8 . 94%, 5 . 06%, 7 . 20%, and 3 . 45% increase in precision, recall, F 1 -score, and mAP , respectively as shown in Fig.9. Moreover, the proposed model is faster at detection at 70.19 FPS which is 10 . 34% higher than the original YOLOv4 model. Region based detection model such as Faster RCNN, RetinaNet, SSD perform classification and bounding box regression with its two step architecture. Whereas, YOLO makes classification and bounding box regression at the same time making the detection model significantly faster. Summarizing, the proposed detection model outperforms other stateof-the-art models in both detection accuracy and speed making it a promising model for high-performance real-time disease detection for precision agriculture and automation.

Fig. 10 Comparison of (a) P-R curves during testing ; (b) training loss curves between YOLOv3, YOLOv4, and proposed detection model.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de dos líneas con dos curvas de tendencia: una de color azul y otra de color verde. La curv



## 5.3 Overall performance of the proposed detection model

From the previous section, we identify the YOLOv3 and YOLOv4 models as comparable to the proposed model in detection accuracy and speed. These three models are extensively tested and compared in this section on the disease dataset. The values of IoU , F 1 scores, final loss, and average detection time for these three models are compared in Table 6 for the test images. YOLOv3 yields the lowest IoU value of 0.767 between the three models, whereas, the IoU obtained for the proposed model is the maximum at 0.935, which is 10.4% higher than the original YOLOv4. The IoU values suggest that the proposed detection model is the most accurate at detecting bounding boxes. The original YOLOv4 with an F 1 -score of 0.861 is more efficient in disease detection than the YOLOv3 ( F 1 -score of 0.803). However, the proposed model also yields the highest F 1 score of 0.936 which is an improvement of 7 . 20% from the original YOLOv4. The proposed model also provides the best precision and recall performance compared to the other two models (see Table 7). Furthermore, comparison of the average detection time reveals that the proposed model has the lowest detection time of 14.29 ms resulting in the fastest detection speed of 70.19 FPS as listed in Table 6. Besides, the proposed model is comparatively easy to train (training time s 3.98 h which is the lowest). Therefore, it is evident that the proposed object detection model outperforms the YOLOv3 and YOLOv4 in all performance measures. Comparison of the precision-recall ( PR ) curves for these three models are shown in Fig. 10-(a). Comparing the characteristics of the P -R curves, the precision for the proposed model is higher than YOLOv3and YOLOv4 models for any recall. The area under the P -R curve (i.e., AP value) is the maximum for the proposed model (see Table 5 for comparison of mAP at IoU ≥ 0 . 5) which suggests that the proposed model exhibited better accuracy and precision at detection compared to the YOLOv3 and YOLOv4.

Figure 10-(b) compares the training loss plotted for the YOLOv3, YOLOv4, and modified YOLOv4 models. In the initial phase, the loss curves corresponding to the YOLOv3 and YOLOv4 begin to reduce significantly after approximately 16,000 and 11,000 training steps. For the proposed model, loss reduction is much faster up to at least 5,000 training steps. After exhibiting several cycles of fluctuation, training loss in the proposed model tends to saturate after approximately 55,000 training steps. The final training loss for the proposed model is 2.98 which is approximately 34 . 7% lower than the original YOLOv4.

Fig. 11 (a) Comparison of validation loss curves between YOLOv3, YOLOv4, and improved YOLOv4 detection models; (b) P-R curves for different disease class from the proposed model.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de líneas que compara el rendo de dos modelos de “ ” ” ” ”



Usually, a lower training loss yields a more accurate model. Similarly characteristics are obtained for the validation loss curve plotted in Fig. 11-(a); validation loss for the proposed model decreases rapidly up to 3,000 training steps. The loss curve saturates as the model gradually converges after about 65,000 steps. After 85,000 training steps, both training and validation losses are observed to saturate. The obtained model is therefore assumed to be optimal. The final validation loss value for the proposed model is 2.29 compared to 13.31 and 8.92 for the YOLOv3 and YOLOv4, respectively as shown in Table 6. The proposed model is evidently easier to train, converging faster to a more accurate model.

How do the model perform in detecting individual classes? TP , FP , and FN for each class and corresponding precision, recall and F 1 -score are tabulated in Table 7. For comparison, P -R curves for different disease classes for the proposed model are plotted in Fig. 11-(b) which indicate that the model detects leaf mold better (as the precision-recall values are higher) than the other classes. The proposed model has relatively higher precision for late blight (91 . 76%) and Septoria (94 . 89%). The proposed model yields 90 . 33% precision, 97 . 20% recall, and 93 . 64% F 1 -score. In comparison to other models, the model maximizes the TP value minimizing FP and FN for all classes compared to YOLOv3 and YOLOv4. For example, TP increases from 9575 to 10780; FP and FN reduce from 2188 to 1153 and 816 to 310, respectively, in Table 7. This results in 8 . 94%, 5 . 06%, 7 . 20%, and 3 . 45% increase in precision, recall, F 1 -score, and mAP , respectively, compared to the original YOLOv4.

Influence of using different loss functions, namely, GIoU , DIoU , and CIoU losses on detection performance and speed is compared for YOLOv4 and the proposed model in Table 8. Choosing appropriate loss function can improve the detection accuracy at the same time maintaining high detection speed during disease detection. Among the three loss functions, employing the CIoU loss results in obtaining the best network. For example, precision, recall, F 1, and mAP increase by 2 . 78%, 3 . 81%, 2 . 73%, and 1 . 5%, respectively compared to the model obtained using the GIoU loss. However, using the CIoU slightly compromises the detection speed while the detection time increases by only 1.03 ms compared to the GIoU loss. Overall, a slight improvement in performance is obtained for all disease classes when the CIoU loss function is used for both YOLOv4 and the proposed model. Although the use of an appropriate loss function has some influence, it is relatively less compared to the use of appropriate activation function, addition of the residual module and dense block.

Table 7 Comparison of detection results between YOLOv3, YOLOv4, and proposed model on the test dataset.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv3, Class: All, Objects: 11952, TP: 8508, FP: 2991, FN: 1160, P (%): 73.98, R (%): 88.01, F1-score: 80.38.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Early Blight, Class: 5085, Objects: 3658, TP: 1412, FP: 510, FN: 72.14, P (%): 87.76, R (%): 79.19.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Late Blight, Class: 2304, Objects: 1701, TP: 511, FP: 209, FN: 76.92, P (%): 89.05, R (%): 82.54.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Septoria, Class: 2799, Objects: 1789, TP: 818, FP: 343, FN: 68.62, P (%): 83.91, R (%): 75.5.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Leaf Mold, Class: 1764, Objects: 1361, TP: 251, FP: 98, FN: 84.42, P (%): 93.28, R (%): 88.63.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4, Class: All, Objects: 11952, TP: 9575, FP: 2188, FN: 816, P (%): 81.39, R (%): 92.14, F1-score: 86.44.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Early Blight, Class: 5085, Objects: 4058, TP: 1002, FP: 375, FN: 80.19, P (%): 91.54, R (%): 85.49.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Late Blight, Class: 2304, Objects: 2007, TP: 396, FP: 141, FN: 83.52, P (%): 93.43, R (%): 88.2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Septoria, Class: 2799, Objects: 2041, TP: 593, FP: 255, FN: 77.48, P (%): 88.89, R (%): 82.79.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Leaf Mold, Class: 1764, Objects: 1469, TP: 197, FP: 45, FN: 88.17, P (%): 97.02, R (%): 92.38.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed Model, Class: All, Objects: 11952, TP: 10780, FP: 1153, FN: 310, P (%): 90.33, R (%): 97.2, F1-score: 93.64.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Early Blight, Class: 5085, Objects: 4578, TP: 476, FP: 157, FN: 90.58, P (%): 96.68, R (%): 93.53.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Late Blight, Class: 2304, Objects: 2196, TP: 197, FP: 41, FN: 91.76, P (%): 98.16, R (%): 94.85.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Septoria, Class: 2799, Objects: 2334, TP: 390, FP: 96, FN: 85.68, P (%): 96.04, R (%): 90.57.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Leaf Mold, Class: 1764, Objects: 1672, TP: 91, FP: 16, FN: 94.89, P (%): 99.05, R (%): 96.92.
Nevertheless, appropriate selection of both activation and loss functions lead to maximizing overall network accuracy and speed for tomato plant disease detection.

## 6 Real-time detection results

In this section, real-time detection results for the four different disease classes are presented in detail. Results include detection of different disease classes, detection in greyscale and in low-resolution images, and at various illumination intensities.

## 6.1 Detection of different plant disease classes

Results from the proposed model for four different diseases are compared with predictions from the YOLOv3 and YOLOv4 models. Each of these classes are detected in three different leaves. Visual representations of the results are presented in Figs. 12-15. Four diseases: early blight, late blight, Septoria leaf spot, and leaf mold are marked with bounding-boxclass identifiers: 1, 2, 3, and 4, respectively. The arrows identify undetected objects or false detections by the model. Detection performance of the three models in detecting each class is compared by reporting detected (detec.) and undetected (undetec.) cases for each leaf in Tables 9-12. Superiority of the proposed model over the original models for the detection task at hand is evident from these results.

The area of leaves infected by early blight can be identified as mostly dark brown (or black) spots generally distributed discretely as shown in Fig. 12. After their genesis, early blight lesions grow erratically. It is challenging to detect the high-aspect-ratio patches, specifically at the edges of the leaves. While YOLOv3 and YOLOV4 miss several early blight spots, the proposed model shows superior performance as shown in Fig. 12-(g,h). Due to similarity of their textures with the surroundings, these are difficult to detect. Even in such tasks, the proposed model provides significant improvement in detection accuracy

Table 8 Comparison of detection performance and detection speed between YOLOv4 and the proposed model for GIoU, DIoU, and CIoU loss functions.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (GIoU), Class: All, P (%): 78.71, R (%): 89.56, F1: 83.79, mAP (%): 90.34, Dect. time (ms): 14.34.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (GIoU), Class: Early Blight, P (%): 74.9, R (%): 87.82, F1: 80.84, mAP (%): 90.68, Dect. time (ms): 14.34.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (GIoU), Class: Late Blight, P (%): 78.45, R (%): 90.28, F1: 83.95, mAP (%): 89.93, Dect. time (ms): 14.34, FPS: 69.7.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (GIoU), Class: Septoria, P (%): 77.53, R (%): 87.3, F1: 82.12, mAP (%): 88.98, Dect. time (ms): 14.34.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (GIoU), Class: Leaf Mold, P (%): 83.98, R (%): 92.87, F1: 88.2, mAP (%): 91.79, Dect. time (ms): 14.34.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (GIoU), Class: All, P (%): 88.55, R (%): 93.39, F1: 90.91, mAP (%): 94.16, Dect. time (ms): 13.26, FPS: 75.43.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (GIoU), Class: Early Blight, P (%): 87.35, R (%): 93.12, F1: 90.14, mAP (%): 94.79, Dect. time (ms): 13.26, FPS: 75.43.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (GIoU), Class: Late Blight, P (%): 91.47, R (%): 93.27, F1: 92.36, mAP (%): 97.01, Dect. time (ms): 13.26, FPS: 75.43.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (GIoU), Class: Septoria, P (%): 82.73, R (%): 91.89, F1: 87.07, mAP (%): 88.97, Dect. time (ms): 13.26, FPS: 75.43.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (GIoU), Class: Leaf Mold, P (%): 92.67, R (%): 95.31, F1: 93.97, mAP (%): 95.89, Dect. time (ms): 13.26, FPS: 75.43.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (DIoU), Class: All, P (%): 80.96, R (%): 91.82, F1: 86.05, mAP (%): 92.41, Dect. time (ms): 14.59, FPS: 68.52.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (DIoU), Class: Early Blight, P (%): 78.54, R (%): 90.45, F1: 84.07, mAP (%): 92.76, Dect. time (ms): 14.59, FPS: 68.52.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (DIoU), Class: Late Blight, P (%): 81.24, R (%): 91.07, F1: 85.87, mAP (%): 92.98, Dect. time (ms): 14.59, FPS: 68.52.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (DIoU), Class: Septoria, P (%): 78.21, R (%): 89.89, F1: 83.64, mAP (%): 91.03, Dect. time (ms): 14.59, FPS: 68.52.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (DIoU), Class: Leaf Mold, P (%): 85.87, R (%): 95.87, F1: 90.59, mAP (%): 92.87, Dect. time (ms): 14.59, FPS: 68.52.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (DIoU), Class: All, P (%): 89.43, R (%): 94.83, F1: 92.05, mAP (%): 94.76, Dect. time (ms): 13.66, FPS: 73.21.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (DIoU), Class: Early Blight, P (%): 90.12, R (%): 94.53, F1: 92.27, mAP (%): 95.32, Dect. time (ms): 13.66, FPS: 73.21.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (DIoU), Class: Late Blight, P (%): 90.92, R (%): 92.86, F1: 91.88, mAP (%): 96.56, Dect. time (ms): 13.66, FPS: 73.21.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (DIoU), Class: Septoria, P (%): 84.13, R (%): 94.37, F1: 88.95, mAP (%): 90.87, Dect. time (ms): 13.66, FPS: 73.21.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (DIoU), Class: Leaf Mold, P (%): 92.56, R (%): 97.59, F1: 95.01, mAP (%): 96.32, Dect. time (ms): 13.66, FPS: 73.21.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (CIoU), Class: All, P (%): 81.39, R (%): 92.14, F1: 86.44, mAP (%): 92.84, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (CIoU), Class: Early Blight, P (%): 80.19, R (%): 91.54, F1: 85.49, mAP (%): 93.05, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (CIoU), Class: Late Blight, P (%): 83.52, R (%): 93.43, F1: 88.2, mAP (%): 94.14, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (CIoU), Class: Septoria, P (%): 77.48, R (%): 88.89, F1: 82.79, mAP (%): 87.41, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: YOLOv4 (CIoU), Class: Leaf Mold, P (%): 88.17, R (%): 97.02, F1: 92.38, mAP (%): 96.76, Dect. time (ms): 15.72, FPS: 63.61.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (CIoU), Class: All, P (%): 90.33, R (%): 97.2, F1: 93.64, mAP (%): 96.29, Dect. time (ms): 14.29, FPS: 70.19.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (CIoU), Class: Early Blight, P (%): 90.58, R (%): 96.68, F1: 93.53, mAP (%): 96.01, Dect. time (ms): 14.29, FPS: 70.19.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (CIoU), Class: Late Blight, P (%): 91.76, R (%): 98.16, F1: 94.85, mAP (%): 97.98, Dect. time (ms): 14.29, FPS: 70.19.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (CIoU), Class: Septoria, P (%): 85.68, R (%): 96.04, F1: 90.57, mAP (%): 92.45, Dect. time (ms): 14.29, FPS: 70.19.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Model: Proposed model (CIoU), Class: Leaf Mold, P (%): 94.89, R (%): 99.05, F1: 96.92, mAP (%): 98.72, Dect. time (ms): 14.29, FPS: 70.19.
reflected in reduced number of undetected spots compared to the other two models, visually illustrated in Figs. 12 -(b), (e) and (h), and also in results tabulated in Table 9.

The late blight infections usually show up as larger dark brown lesions in an arbitrary area of a tomato plant which can rapidly spread. Due to irregular shapes and similarity of their texture with surrounding leaves, it is often hard to detect precisely. While the detection results from the YOLOv3 and YOLOv4 show several missed detections when the interface between infected zones and leaves are not prominent as shown in Fig.13 -(a-f), the proposed model yields much better performance in such challenging scenarios by identifying coalescent infected zones between multiple infected spots in Fig.13 -(g-i). Again the proposed model is able to reduce missed detections. Moreover, it provides higher confidence scores in bounding box predictions compared to the other two models as shown in Table 10.

Septoria leaf spots have visual similarities to the early blight (Fig. 14). However, these spots are darker and more rounded. For relatively less dense discrete distribution of Septoria spots, all three models perform reasonably well as shown in Fig. 14 -(a, d, g). Several missed

Fig. 12 Detection result for early blight on three distinct tomato leaves from three models: (a-c) YOLOv3; (d-f) YOLOv4; (g-i) proposed model. The white arrow indicates undetected or false detection from the corresponding model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un [ ] [ ] [



detections for relatively densely distributed spots are obtained for YOLOv3 and YOLOv4 in Fig. 14 -(c,f). On the other hand, the proposed model reduces missed detections significantly as shown in Fig. 14 -(i). In more challenging scenarios such as densely populated distribution of infected areas, as in Fig. 14 -(h), the proposed model illustrates its superiority, correctly predicting higher confidence scores for bounding boxes along with significant reduction in missed detections as listed in Table 11.

Lastly, detection results for leaf-mold-infected leaves are presented in Fig. 15. Leaf molds are generally pale greenish-yellow or olive-green spots. The associated difficulty in detection is due to color similarity and also indistinguishable margins with surrounding leaves. Varying lightening conditions in the image dataset is an additional difficulty for the object detection models to detect each of the lesions precisely. The proposed model is again superior to the YOLOv3 and YOLOv4 as shown in Fig. 15-(h,i), in particular, closely

Table 9 Comparison of detection results between YOLOv3, YOLOv4, and proposed model for early blight detection as shown in Fig 12. Bold highlights the best result obtained from the corresponding model prediction.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(a), Model: YOLOv3, Detc.: 5, Undetc.: 7, Confidence Scores: 0.96, 0.92, 0.84, 0.93, 0.89.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(d), Model: YOLOv4, Detc.: 8, Undetc.: 4, Confidence Scores: 0.72, 0.90, 0.87, 0.76, 0.86, 1.00, 0.83, 0.95.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(g), Model: Proposed model, Detc.: 10, Undetc.: 2, Confidence Scores: 0.97, 0.94, 0.88, 0.96, 1.00, 0.86, 1.00, 0.93, 0.98, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(b), Model: YOLOv3, Detc.: 10, Undetc.: 12, Confidence Scores: 0.82, 0.93, 0.81, 0.78, 1.00, 1.00, 0.83, 0.95, 0.94, 0.99.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(e), Model: YOLOv4, Detc.: 12, Undetc.: 10, Confidence Scores: 0.88, 0.97, 1.00, 1.00, 0.75, 0.86, 0.89, 0.91, 1.00, 1.00, 1.00, 0.96.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(h), Model: Proposed model, Detc.: 19, Undetc.: 3, Confidence Scores: 0.98, 0.87, 1.0, 1.0, 1.0, 0.86,1.0, 0.97, 0.95, 1.0 0.99, 0.87, 0.92, 1.0, 1.0, 0.91, 0.98, 0.92, 0.99.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig.12-(c), Model: YOLOv3, Detc.: 4, Undetc.: 6, Confidence Scores: 0.79, 0.88, 0.93, 0.89.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(f), Model: YOLOv4, Detc.: 4, Undetc.: 6, Confidence Scores: 0.94, 0.98, 1.00, 0.96.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 12-(i), Model: Proposed model, Detc.: 9, Undetc.: 1, Confidence Scores: 0.98, 0.99, 0.98, 0.97, 1.00, 0.96, 1.00, 0.93, 0.98.
Table 10 Comparison of detection results between YOLOv3, YOLOv4, and proposed model for late blight detection as shown in Fig 13. Bold highlights the best result obtained from corresponding model prediction.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(a), Model: YOLOv3, Detc.: 2, Undetc.: 3, Confidence Scores: 0.84, 0.93.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(d), Model: YOLOv4, Detc.: 2, Undetc.: 3, Confidence Scores: 0.94, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(g), Model: Proposed model, Detc.: 4, Undetc.: 1, Confidence Scores: 0.98, 1.00, 1.00, 0.97.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(b), Model: YOLOv3, Detc.: 2, Undetc.: 2, Confidence Scores: 0.91, 0.94.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(e), Model: YOLOv4, Detc.: 3, Undetc.: 1, Confidence Scores: 0.97, 1.00, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(h), Model: Proposed model, Detc.: 4, Undetc.: 0, Confidence Scores: 1.00, 0.96, 1.00, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig.13-(c), Model: YOLOv3, Detc.: 2, Undetc.: 4, Confidence Scores: 0.89, 0.87.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(f), Model: YOLOv4, Detc.: 3, Undetc.: 3, Confidence Scores: 0.91, 1.00, 1.00,.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 13-(i), Model: Proposed model, Detc.: 6, Undetc.: 0, Confidence Scores: 0.92, 0.98, 1.00, 1.00, 1.00, 0.97.
distributed Septoria lesions. For the proposed model, miss detections are reduced the confidence scores are improved, is evident from Table 12.

Based on the detection results for the four classes, overall, the proposed model illustrates superior detection ability, in particular, in detecting densely populated fine-grain diseases, irregular geometric morphology of the infected areas, the coexistence of multi-scale infection lesions, similarity of textures of affected areas and surroundings, varying lightening conditions, etc. compared to the original YOLO models.

Fig. 13 Detection result for late blight on three distinct tomato leaves from three models: (a-c) YOLOv3; (d-f) YOLOv4; (g-i) proposed model. The white arrow indicates undetected or false detection from the corresponding model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un conjunto de 9 sub-imagines de hoas de plantas con manas de “ ” “ ”



## 6.2 Detection under greyscale and low-resolution images

The proposed model is used to predict greyscale and pixelated low-resolution ( 100 × 100 ) images. The predictions are then compared to the original red, green, and blue (RGB) images to analyze the detection accuracy of the bounding boxes for all four disease classes in Fig 16.

The proposed model is highly accurate in predicting greyscale images, for early blight and leaf mold classes in particular, with zero missed detections. However, the model misses one spot for late blight and two spots for Septoria as shown in Fig 16 -(b-ii, c-ii). These results indicate that the accuracy of the detection model can reduce for low-resolution greyscale images with some undetected disease spots in densely populated areas and similar textural colored backgrounds. Nevertheless, detection accuracy of the proposed model for low-resolution images is higher than the YOLOv3 and YOLOv4 models (see Tables 9- 12

Fig. 14 Detection result for Septoria leaf spot on three distinct tomato leaves from three models: (a-c) YOLOv3; (d-f) YOLOv4; (g-i) proposed model. The white arrow indicates undetected or false detection from the corresponding model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un “ ” ” ” ”



and Table 13). It can be concluded from the test results that the proposed model is more adaptive in more challenging environments compared to the original models.

## 6.3 Detection under different illumination intensities

In Fig. 17, prediction results from the proposed model under different illumination intensities are analyzed. Detection results for three different brightness conditions: 80%, 60% , and 40% are compared to the original detection results under normal brightness conditions. Here, white arrow indicates undetected spots or false detections compared to the original images. One can see that the model can accurately detect disease spots in different brightness conditions, in particular, 80% and 60% brightness conditions. However, missed and false detections are obtained for early blight, Septoria, and leaf mold in 40% brightness intensity

Table 11 Comparison of detection results between YOLOv3, YOLOv4, and proposed model for Septoria leaf spot detection as shown in Fig 14. Bold highlights the best result obtained from corresponding model prediction.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(a), Model: YOLOv3, Detc.: 6, Undetc.: 3, Confidence Scores: 0.96, 0.92, 1.00, 0.84, 0.93, 0.89.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(d), Model: YOLOv4, Detc.: 6, Undetc.: 3, Confidence Scores: 0.94, 1.00, 0.97, 0.86, 1.00, 0.87.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(g), Model: Proposed model, Detc.: 9, Undetc.: 0, Confidence Scores: 1.00, 1.00, 1.00, 0.99, 0.87 1.00, 0.91, 0.92, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(b), Model: YOLOv3, Detc.: 8, Undetc.: 13, Confidence Scores: 1.00, 1.00, 1.00, 0.86 0.99, 0.97, 0.87, 0.91.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(e), Model: YOLOv4, Detc.: 10, Undetc.: 11, Confidence Scores: 0.99, 0.87, 1.00, 1.00, 1.00, 0.97, 0.99, 0.84, 0.91, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(h), Model: Proposed model, Detc.: 17, Undetc.: 4, Confidence Scores: 0.94, 0.97, 1.00, 1.00, 1.00, 0.86 1.00, 0.94, 0.99, 0.99, 0.97, 0.94 1.00, 1.00, 0.91, 0.98, 0.99.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig.14-(c), Model: YOLOv3, Detc.: 7, Undetc.: 6, Confidence Scores: 0.79, 0.87, 0.91, 0.83, 1.00, 1.00, 0.94.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(f), Model: YOLOv4, Detc.: 7, Undetc.: 6, Confidence Scores: 0.89, 0.91, 1.00, 1.00, 1.00, 0.96.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 14-(i), Model: Proposed model, Detc.: 12, Undetc.: 1, Confidence Scores: 0.94, 0.97, 1.00, 1.00, 1.00, 0.99, 1.00, 1.00, 0.91, 0.92, 0.99, 1.00.
Table 12 Comparison of detection results between YOLOv3, YOLOv4, and proposed model for leaf mold detection as shown in Fig 15. Bold highlights the best result obtained from corresponding model prediction.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(a), Model: YOLOv3, Detc.: 1, Undetc.: 3, Confidence Scores: 0.96.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(d), Model: YOLOv4, Detc.: 3, Undetc.: 1, Confidence Scores: 0.94, 1.00, 0.97.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(g), Model: Proposed model, Detc.: 4, Undetc.: 0, Confidence Scores: 0.91, 1.00, 1.00, 0.94.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(b), Model: YOLOv3, Detc.: 2, Undetc.: 4, Confidence Scores: 0.94, 0.96.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(e), Model: YOLOv4, Detc.: 2, Undetc.: 4, Confidence Scores: 0.97, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(h), Model: Proposed model, Detc.: 6, Undetc.: 0, Confidence Scores: 0.91, 1.00, 0.96, 0.89, 1.00, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig.15-(c), Model: YOLOv3, Detc.: 3, Undetc.: 3, Confidence Scores: 0.93, 0.89, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(f), Model: YOLOv4, Detc.: 4, Undetc.: 2, Confidence Scores: 0.89, 0.91, 1.00, 1.00.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Fig. 15-(i), Model: Proposed model, Detc.: 6, Undetc.: 0, Confidence Scores: 0.89, 0.91, 1.00, 1.00, 1.00, 0.96.
as shown in Fig. 17-(a, c, d). Nevertheless, predictions of boundary boxes and corresponding confidence scores (see Table 14) for the proposed model are of reasonable accuracy under dimming conditions which justifies the use of the model in practical on-field disease detection tasks.

Despite its efficacy for the tomato plant disease detection task, there is scope for improvement in the proposed model's feature extraction process to further minimize missed and false detections under challenging backgrounds. Future work will focus on further op-

Fig. 15 Detection result for leaf mold on three distinct tomato leaves from three models: (a-c) YOLOv3; (d-f) YOLOv4; (g-i) proposed model. The white arrow indicates undetected or false detection from the corresponding model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un [ ] [ ] [



Table 13 Comparison of detection results on the original RGB, corresponding greyscale, and pixelated low resolution images from the proposed model as shown in Fig. 16.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Detec., Disease class: Undetec., Original: Detec., Original: Undetec., Grey scale: Detec., Grey scale: Undetec..
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 16-(a)-i, ii, iii, Disease class: Early blight, Original: 10, Original: 2, Grey scale: 10, Grey scale: 2, Low resolution: 8, Low resolution: 4.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 16-(b)-i, ii, iii, Disease class: Late blight, Original: 4, Original: 0, Grey scale: 4, Grey scale: 0, Low resolution: 2, Low resolution: 2.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 16-(c)-i, ii, iii, Disease class: Septoria, Original: 12, Original: 1, Grey scale: 10, Grey scale: 3, Low resolution: 7, Low resolution: 6.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 16-(d)-i, ii, iii, Disease class: Leaf mold, Original: 6, Original: 0, Grey scale: 6, Grey scale: 0, Low resolution: 5, Low resolution: 1.
(a)-i                                   (a)-ii                              (a)-iii

(b)-i                                   (b)-ii                              (b)-iii

(c)-i                                   (c)-ii                              (c)-iii

(d)-i                                   (d)-ii                              (d)-iii

Fig. 16 Detection results on original RGB, corresponding greyscale, and pixelated low-resolution images for [(a)-i, ii, iii] early blight; [(b)-i, ii, iii] late blight; [(c)-i, ii, iii] Septoria; and [(d)-i, ii, iii] leaf mold from the proposed model. White arrow indicates undetected or false detection from the model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de unión de “ ” “ ”



timization of detection speed and accuracy of the model for use in a mobile computing platform for portable on-field detection.

## 7 Conclusion

In this work, a real-time object detection model is developed based on the YOLOv4 algorithm. Several modifications are proposed to optimize both detection accuracy and speed of

Fig. 17 Detection results obtained from the original RGB and different illumination conditions including 90%, 80%, and 60% brightness intensity for [(a)-i, ii, iii, iv] early blight; [(b)-i, ii, iii, iv] late blight; [(c)-i, ii, iii, iv] Septoria; and [(d)-i, ii, iii, iv] leaf mold from the proposed model. White arrow indicates undetected or false detection from the model prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de líneas que representa la evolución de la “ ” ” ” ” ”



Table 14 Comparison of detection results obtained from the original RGB and different illumination conditions including 90%, 80%, and 60% brightness intensities as shown in Fig. 17.

Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Det., Disease class: Undet., Original: Det., Original: Undet., 90%: Det., 90%: Undet., 80%: Det., 80%: Undet..
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 17-(a)i-iv, Disease class: Early blight, Original: 10, Original: 2, 90%: 10, 90%: 2, 80%: 10, 80%: 2, 60%: 8, 60%: 4.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 17-(b)i-iv, Disease class: Late blight, Original: 4, Original: 0, 90%: 4, 90%: 0, 80%: 4, 80%: 0, 60%: 3, 60%: 1.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 17-(c)i-iv, Disease class: Septoria, Original: 12, Original: 1, 90%: 12, 90%: 1, 80%: 10, 80%: 3, 60%: 9, 60%: 4.
Según A fast accurate fine-grain object detection model based on YOLOv4 deep neural network (2021), Figs. No: Figs. 17-(d)i-iv, Disease class: Leaf mold, Original: 6, Original: 0, 90%: 6, 90%: 0, 80%: 5, 80%: 1, 60%: 5, 60%: 1.
the model which are then verified in various complex detection tasks in noisy environments utilizing traditional performance measures for detecting objects. Accuracy, efficiency and robustness of the model are enhanced due to introduction of the CSP1n block in the backbone that improved feature extraction and the CSP2n module in the neck that preserved fine-grain local information. Moreover, a DenseNet block is implemented in the backbone bettering feature transfer and reuse. Despite use of these additional components, the model is demonstratively easier to train than the original YOLO models. Additionally, use of the Hard-Swish as the primary activation function ameliorates the model's learning capability of nonlinear characteristics in image features. All these modifications are able to increase the accuracy of the model substantially. The current algorithm achieves the highest detection accuracy and speed compared to some existing state-of-the-art detection models. At a detection rate of 70.19 FPS , the proposed model yielded a precision value of 90 . 33%, F 1 -score of 93 . 64%, mAP of 96 . 29%. Compared to the original YOLOv4, the proposed model acquires 8 . 94% increase in precision, 7 . 20% increase in the F 1 -score, and provides 10 . 34% faster detection illustrating the superior potential of the model in real-time in-field applications. Current work provides an efficient method for accurate fine-grain detection of different object classes in complex scenarios. Although the model is only applied for plant disease detection herein, it can be extended to different fruit and crop detection tasks, generic disease detection problems, and various automated agricultural detection processes [61,62].

## References

1. S.G. Vougioukas, Annual Review of Control, Robotics, and Autonomous Systems 2 , 365 (2019)
2. F. Martinelli, R. Scalenghe, S. Davino, S. Panno, G. Scuderi, P. Ruisi, P. Villa, D. Stroppiana, M. Boschetti, L.R. Goulart, et al., Agronomy for Sustainable Development 35 (1), 1 (2015)
3. X. Ling, Y. Zhao, L. Gong, C. Liu, T. Wang, Robotics and Autonomous Systems 114 , 134 (2019)
4. A. Kamilaris, F.X. Prenafeta-Bold´ u, Computers and electronics in agriculture 147 , 70 (2018)
5. S.H. Lee, C.S. Chan, S.J. Mayo, P. Remagnino, Pattern Recognition 71 , 1 (2017)
6. P.A. Dias, A. Tabb, H. Medeiros, Computers in Industry 99 , 17 (2018)
7. K. Yamamoto, W. Guo, Y. Yoshioka, S. Ninomiya, Sensors 14 (7), 12191 (2014)
8. Y.Y. Zheng, J.L. Kong, X.B. Jin, X.Y. Wang, T.L. Su, M. Zuo, Sensors 19 (5), 1058 (2019)
9. A. Banan, A. Nasiri, A. Taheri-Garavand, Aquacultural Engineering 89 , 102053 (2020)
10. M. Arsenovic, M. Karanovic, S. Sladojevic, A. Anderla, D. Stefanovic, Symmetry 11 (7), 939 (2019)
11. Y. Zhang, C. Song, D. Zhang, IEEE Access 8 , 56607 (2020)
12. J. Han, D. Zhang, G. Cheng, N. Liu, D. Xu, IEEE Signal Processing Magazine 35 (1), 84 (2018)
13. T.Y. Lin, P. Goyal, R. Girshick, K. He, P. Doll´ ar, in Proceedings of the IEEE international conference on computer vision (2017), pp. 2980-2988
14. R. Girshick, Piscataway, NJ: IEEE.[Google Scholar] (2015)
15. S. Ren, K. He, R. Girshick, J. Sun, IEEE transactions on pattern analysis and machine intelligence 39 (6), 1137 (2016)
16. K. He, G. Gkioxari, P. Doll´ ar, R. Girshick. Mask r-cnn. in proceedings of the ieee international conference on computer vision (2017)
17. S. Bargoti, J. Underwood, in 2017 IEEE International Conference on Robotics and Automation (ICRA) (IEEE, 2017), pp. 3626-3633
18. J. Redmon, S. Divvala, R. Girshick, A. Farhadi, in Proceedings of the IEEE conference on computer vision and pattern recognition (2016), pp. 779-788
19. J. Redmon, A. Farhadi, in Proceedings of the IEEE conference on computer vision and pattern recognition (2017), pp. 7263-7271
20. J. Redmon, A. Farhadi. Yolov3: An incremental improvement (2018)
21. A. Bochkovskiy, C.Y. Wang, H.Y.M. Liao. Yolov4: Optimal speed and accuracy of object detection (2020)
22. J. Wang, N. Wang, L. Li, Z. Ren, Neural Computing and Applications 32 (10), 5471 (2020)
23. I. Martinez-Alpiste, G. Golcarenarenji, Q. Wang, J.M. Alcaraz-Calero, Neural Computing and Applications pp. 1-13 (2021)
24. M. Choudhary, V. Tiwari, V. Uduthalapally, Neural Computing and Applications 33 (11), 5609 (2021)

25. Q. Zhu, H. Zheng, Y. Wang, Y. Cao, S. Guo, Sensors 20 (15), 4314 (2020)
26. J. Yu, W. Zhang, Sensors 21 (9), 3263 (2021)
27. R. Gai, N. Chen, H. Yuan, Neural Computing and Applications pp. 1-12 (2021)
28. A.M. Roy, J. Bhaduri, AI 2 (3), 413 (2021)
29. G. Huang, Z. Liu, L. Van Der Maaten, K.Q. Weinberger, in Proceedings of the IEEE conference on computer vision and pattern recognition (2017), pp. 4700-4708
30. S. Liu, L. Qi, H. Qin, J. Shi, J. Jia, in Proceedings of the IEEE conference on computer vision and pattern recognition (2018), pp. 8759-8768
31. K. He, X. Zhang, S. Ren, J. Sun, IEEE transactions on pattern analysis and machine intelligence 37 (9), 1904 (2015)
32. R. Avenash, P. Viswanath, in VISIGRAPP (4: VISAPP) (2019), pp. 413-420
33. Z. Wu, C. Shen, A. Van Den Hengel, Pattern Recognition 90 , 119 (2019)
34. C.Y. Wang, H.Y.M. Liao, Y.H. Wu, P.Y. Chen, J.W. Hsieh, I.H. Yeh, in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition workshops (2020), pp. 390-391
35. T.Y. Lin, P. Doll´ ar, R. Girshick, K. He, B. Hariharan, S. Belongie, in Proceedings of the IEEE conference on computer vision and pattern recognition (2017), pp. 2117-2125
36. S. Yun, D. Han, S.J. Oh, S. Chun, J. Choe, Y. Yoo, in Proceedings of the IEEE/CVF International Conference on Computer Vision (2019), pp. 6023-6032
37. G. Ghiasi, T.Y. Lin, Q.V. Le. Dropblock: A regularization method for convolutional networks (2018)
38. P. Ramachandran, B. Zoph, Q.V. Le. Searching for activation functions (2017)
39. S. Eger, P. Youssef, I. Gurevych. Is it time to swish? comparing deep learning activation functions across nlp tasks (2019)
40. A.L. Maas, A.Y. Hannun, A.Y. Ng, in Proc. icml , vol. 30 (Citeseer, 2013), vol. 30, p. 3
41. D. Misra. Mish: A self regularized non-monotonic activation function (2020)
42. S. Elfwing, E. Uchibe, K. Doya, Neural Networks 107 , 3 (2018)
43. D. Hendrycks, K. Gimpel, (2016)
44. A. Howard, M. Sandler, G. Chu, L.C. Chen, B. Chen, M. Tan, W. Wang, Y. Zhu, R. Pang, V. Vasudevan, et al., in Proceedings of the IEEE/CVF International Conference on Computer Vision (2019), pp. 13141324
45. J. Yu, W. Zhang, Sensors 21 (9), 3263 (2021)
46. N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, R. Salakhutdinov, The journal of machine learning research 15 (1), 1929 (2014)
47. Z. Zheng, P. Wang, W. Liu, J. Li, R. Ye, D. Ren, in Proceedings of the AAAI Conference on Artificial Intelligence , vol. 34 (2020), vol. 34, pp. 12,993-13,000
48. Z. Yao, Y. Cao, S. Zheng, G. Huang, S. Lin. Cross-iteration batch normalization (2021)
49. I. Loshchilov, F. Hutter. Sgdr: Stochastic gradient descent with warm restarts (2017)
50. G. Ghiasi, T.Y. Lin, Q.V. Le. Dropblock: A regularization method for convolutional networks (2018)
51. H. Rezatofighi, N. Tsoi, J. Gwak, A. Sadeghian, I. Reid, S. Savarese, in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (2019), pp. 658-666
52. C. Goutte, E. Gaussier, in European conference on information retrieval (Springer, 2005), pp. 345-359
53. A. Ali. Plantvillage dataset (2019). URL https://www.kaggle.com/abdallahalidev/ plantvillage-dataset
54. Tzutalin. Labelimg (2015). URL https://github.com/tzutalin/labelImg
55. AlexeyAB. Pre-trained weights-file (2021). URL https://github.com/AlexeyAB/darknet
56. Z.Q. Zhao, P. Zheng, S.t. Xu, X. Wu, IEEE transactions on neural networks and learning systems 30 (11), 3212 (2019)
57. T.Y. Lin, P. Goyal, R. Girshick, K. He, P. Doll´ ar, in Proceedings of the IEEE international conference on computer vision (2017), pp. 2980-2988
58. W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C. Fu, A. Berg, (2016)
59. Z. Cai, N. Vasconcelos, IEEE transactions on pattern analysis and machine intelligence (2019)
60. K. Chen, J. Wang, J. Pang, Y. Cao, Y. Xiong, X. Li, S. Sun, W. Feng, Z. Liu, J. Xu, Z. Zhang, D. Cheng, C. Zhu, T. Cheng, Q. Zhao, B. Li, X. Lu, R. Zhu, Y. Wu, J. Dai, J. Wang, J. Shi, W. Ouyang, C.C. Loy, D. Lin, arXiv preprint arXiv:1906.07155 (2019)
61. S. Shamshirband, T. Rabczuk, K.W. Chau, IEEE Access 7 , 164650 (2019)
62. Y. Fan, K. Xu, H. Wu, Y. Zheng, B. Tao, IEEE Access 8 , 25111 (2020)