---
id: arxiv-2207.07919
title: Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT
year: 2022
country: Internacional
source: ArXiv (cs.CV)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - deep learning
  - clasificación de imágenes
  - cultivos
  - transformer
  - artículo científico
  - ArXiv
---

## EXPLAINABLE VISION TRANSFORMER ENABLED CONVOLUTIONAL NEURAL NETWORK FOR PLANT DISEASE IDENTIFICATION: PLANTXVIT

## Poornima Singh Thakur, Pritee Khanna, Tanuja Sheorey, Aparajita Ojha

PDPM Indian Institute of Information Technology, Design and Manufacturing

Jabalpur, India 482005

{poornima, pkhanna, tanush, aojha}@iiitdmj.ac.in

## ABSTRACT

Plant diseases are the primary cause of crop losses globally, with an impact on the world economy. To deal with these issues, smart agriculture solutions are evolving that combine the Internet of Things and machine learning for early disease detection and control. Many such systems use vision-based machine learning methods for real-time disease detection and diagnosis. With the advancement in deep learning techniques, new methods have emerged that employ convolutional neural networks for plant disease detection and identification. Another trend in vision-based deep learning is the use of vision transformers, which have proved to be powerful models for classification and other problems. However, vision transformers have rarely been investigated for plant pathology applications. In this study, a Vision Transformer enabled Convolutional Neural Network model called "PlantXViT" is proposed for plant disease identification. The proposed model combines the capabilities of traditional convolutional neural networks with the Vision Transformers to efficiently identify a large number of plant diseases for several crops. The proposed model has a lightweight structure with only 0.8 million trainable parameters, which makes it suitable for IoT-based smart agriculture services. The performance of PlantXViT is evaluated on five publicly available datasets. The proposed PlantXViT network performs better than five state-of-the-art methods on all five datasets. The average accuracy for recognising plant diseases is shown to exceed 93.55%, 92.59%, and 98.33% on Apple, Maize, and Rice datasets, respectively, even under challenging background conditions. The efficiency in terms of explainability of the proposed model is evaluated using gradient-weighted class activation maps and Local Interpretable Model Agnostic Explanation.

K eywords Plant Disease Identification · Vision Transformer · Convolutional Neural Network · Deep Learning · Grad-CAM · LIME

Human population will surpass 10 billion in the next 30 years, which indicates a higher food demand [1] in coming decades. To meet the future requirements and for the sustainable agriculture, methods to prevent the crops from pests and diseases are of utmost importance, as plant diseases have a considerable impact on crop production quality and quantity worldwide. Plant diseases alone are responsible for 20-40% of crop yield losses, [2] which affects the agriculture industry on a large scale. To deal with these issues, smart agriculture solutions are being explored worldwide that combine the Internet of Things (IoT) and machine learning (ML) based methods for early disease detection and control. This has led to significant advancements in the area of vision-based plant disease detection methods for real-time disease detection and diagnosis.

Several ML approaches have been suggested by researchers over the years. Amongst them, support vector machines [3-7], artificial neural network (ANN) [7, 8], Naive Bayes [7, 9, 10], k-means clustering [8, 9], and simple linear iterative clustering [4, 6, 9] are some of the most extensively used methods. In recent years, the focus is shifted towards deep learning (DL) algorithms due to the availability of large amounts of data, computing power, and efficient training approaches. The powerful feature learning capabilities of convolutional neural network (CNN) architectures have produced prominent results in plant disease detection. Apart from standard architectures such as AlexNet, GoogleNet, VGG16, ResNet with transfer learning approaches [11, 12], customized CNN architectures have also been introduced

for plant disease detection tasks [13, 14]. More recently, CNN models with attention mechanisms have been proposed that exhibit excellent performance in plant disease detection [15-20].

Despite these developments, plant disease detection remains a challenge due to the variety of disease types for different crops, evolution of new diseases, and unavailability of in-field data for most of the crops. While DL models are data-hungry, lightweight CNN models do not generalize well for all types of crops. There are two main challenges that keep the research community busy; (1) interpretability of decisions made by ML systems to understand when the system may fail and (2) developing efficient lightweight CNN models that can generalize well for a large variety of plants and their disease types.

The concept of transformers in natural language processing [21] has opened new vistas in image processing and compute vision as its analogue Vision Transformers (ViT) has been recently introduced by Dosovitskiy et al. [22] and has achieved exceptional classification performance with a significantly lower memory footprint on benchmark datasets of ImageNet, CIFAR-10, CIFAR-100, Oxford-IIIT Pets, Oxford Flowers-102, and VTAB. But the main issue with the ViT model is that it cannot converge well on small datasets when compared with CNN models. The reason could be that the ViT mainly focuses on the extraction of long-distance feature dependencies but lacks in efficiently capturing local features of the images [23]. But the local feature extraction capability of CNN combined with the powerful self-attention modules of ViT may help in simultaneously extracting local and global features from images. Further, ViT networks alongwith with CNN can help in enhancing the explainability of plant disease detection models. Keeping this in view, a lightweight, explainable ViT-based plant disease detection model is introduced in the present paper that combines the feature extraction capabilities of CNN and ViT. The model consists of the initial two blocks of the pre-trained VGG16 network, followed by an inception block and four stacks of transformer encoders. The proposed model not only outperforms some of the recently introduced DL models [15, 16, 18-20] on five publicly available datasets, but also improves the explainability of its prediction. The main contributions of the present work are summarised as follows.

- A ViT enabled CNN model, PlantXViT is proposed for plant disease identification that significantly improves the classification performance over a broad range of crop varieties and their diseases.
- PlantXViT exhibits better explainability of its prediction through an analysis of gradient-weighted class activation maps and local interpretable model-agnostic explanations.
- The model is lightweight with only 850,500 trainable parameters, that makes it suitable for smart agriculture devices.
- The proposed model outperforms some of the recently introduced deep CNN models, as demonstrated through extensive experiments on five public datasets with images under different capturing conditions.

The rest of the paper is organized as follows: Section 1 provides a brief overview of the existing schemes for crop disease identification. Section 2 is devoted to the proposed method. Section 3 deals with experiments and results. Here we present the performance of the proposed model on five different datasets. Section 4 provides the concluding remarks and the future scope of the work.

## 1 Related works

With the impressive performance of CNN in computer vision, researchers are increasingly interested in developing DL models for automatic plant disease detection and identification. A brief overview of the state-of-the-art CNN models for plant disease detection is presented in this section. Table 1 shows these techniques using various CNN architectures.

The initial work on plant disease detection using CNN was carried out by Mohanty et al. [11] on a large-scale dataset, by comparing the performances of AlexNet and GoogleNet models. They identified that the GoogleNet model with a transfer learning approach achieved a remarkable accuracy of 99.35% on PlantVillage dataset with 54,305 images in 38 classes. In another work by Barbedo [12] analyzed the impact of dataset size and diversity on plant disease detection using a transfer learning approach with the base model as the GoogleNet model. He showed that the model achieved the highest accuracy of 87% on 1383 images in 56 classes with no background.He concluded that the limitation of the datasets in the area was the main bottleneck in practical deployment of CNN models. Too et al. [24] studied the performance of standard architectures VGG16, Inception v4, ResNet with 50, 101, and 152 layers, and DenseNet with 121 layers on the same dataset using the fine tuning technique. As per their results, the highest accuracy of 99.75% was achieved by the DenseNet121 model among all.

In a work by Chen et al. [25], the initial two blocks of pre-trained VGG16 and two Inception v3 blocks were combined to build a plant disease detection model. They evaluated the model's performance on three different datasets. Their model achieved 84.25%, 92% and 80.38% accuracy on Maize species from PlantVillage, Maize dataset, and their own

Maize dataset respectively. Thakur et al. [26] also developed a CNN model with the initial two pre-trained layers of VGG16 and Inception v7 blocks. They evaluated the performance of their model on five publicly available datasets and reported 99.16%, 93.66%, 94.24%, 91.36% and 96.67% accuracy scores on PlantVillage, Embrapa, Apple, Maize and Maize datasets respectively.

Table 1: An overview of related works on crop disease identification

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Mohanty et al. [11], Technique: AlexNet and GoogleNet, Dataset: 54,305 leaf images in 38 classes from PlantVillage dataset.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Barbedo [12], Technique: GoogleNet GoogleNet, Dataset: 1383 images in 56 classes, Acc%: 99.35 87, Pre%: 99.35 -, Re%: 99.35 -, F1%: 99.34 -, Other: - -.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Too et al. [24], Technique: VGG16, Inception v4, ResNet with 50, 101 and 152 layers and DenseNet with 121 layers, Dataset: 54,305 leaf images in 38 classes from PlantVillage dataset.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Chen et al. [25], Technique: VGG19, Incption v3, Dataset: 466 maize leaf images in 4 classes 500 rice leaf images in 5 classes, Acc%: 80.38 92, Pre%: - -, Re%: 60.76 80, F1%: - -, Other: Specificity 86.92 Specificity 95.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Karthik et al. [15], Technique: Residual CNN, attention mechanism, Dataset: 95,999 tomato leaf im- ages in 10 classes from PlantVillage dataset, Acc%: 98.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Zeng and Li [27], Technique: Self-Attention CNN, Dataset: 9214 leaf images in 6 classes from AES- CD9214 988 leaf images from, Acc%: 95.33 98, Pre%: - -, Re%: - -, F1%: - -, Other: - -.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Chen et al. [16], Technique: Mobile-DANet, DenseNet, transi- tion layer, depthwise separable convolution, attention module, Dataset: MK-D2 dataset 3852 maize leaf images 4 classes from PlantVillage dataset, Acc%: 98.5, Pre%: 97, Re%: 97, F1%: 97, Other: Specificity 99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Chen et al. [18], Technique: MobileNet-V2, attention mechanism, Dataset: 133 maize leaf images in 8 classes 1045 leaf images in 10, Acc%: 95.86 99.67, Pre%: 83.45, Re%: 83.45, F1%: 83.45, Other: Specificity 97.63 Specificity.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Chen et al. [28], Technique: MobileNet, SE, Dataset: classes from PlantVillage dataset 1107 rice leaf images in 12 classes, Acc%: 98.48, Pre%: 98.37 90.56, Re%: 98.37 90.56, F1%: 99.81 90.56, Other: 99.81 Specificity 99.17.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: 1645 images in 11 classes from PlantVillage dataset 444 images in 25 classes, Technique: 99.78 99.33, Dataset: - -, Acc%: 98.83 87.87, Pre%: - -, Re%: Specificity 99.88 Specificity.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Chen et al. [19], Technique: MobileNet v2, Depth- wise separable convolu- tion, channel and spatial attention module, Dataset: 1045 leaf images in 10 classes from PlantVillage dataset 405 images in 20 classes, Acc%: 99.71 99.13, Pre%: - -, Re%: 98.56 91.37, F1%: 98.56 91.37, Other: - -.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Thakur et al. [26], Technique: VGG16, Inception v7, Dataset: 54,305 leaf images in 38 classes from PlantVillage dataset 560 Rice leaf images in 4 classes, Acc%: 99.16 96.67, Pre%: - -, Re%: - -, F1%: - -, Other: Loss: 0.05 Loss: 0.05.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Zhao et al. [20], Technique: Inception, residual, mod- ified channelwise atten-, Dataset: 38,466 images of corn, potato and tomato from PlantVillage dataset in 17, Acc%: 99.55, Other: Loss.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: tion module, Technique: categories, Dataset: 0.0175.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Author: Lu et al. [29], Technique: GhostNet, ViT, Dataset: GLDP12k dataset with 12,615 vine leaf images in 11 classes, Acc%: 98.14.
Recent trends have been on the use of attention mechanisms to boost the performance of plant disease detection models. In the attention mechanism, high priority is assigned to pixel locations with relevant information. Researchers have effectively used the attention mechanism to improve the classification performance of CNNs. Karthik et al. [15] have developed a residual CNN with an attention mechanism for tomato disease detection. Their model attains 98% accuracy on a dataset containing 95,999 tomato leaf images labelled into 10 classes. The dataset is created using the images from PlantVillage dataset and applying augmentation on selected images. Zeng and Li [27] have also experimented with residual CNN and self-attention modules. Their model is shown to achieve 98.0% and 95.33% accuracy on the MK-D2 and AES-CD9214 datasets, respectively.

Chen et al. [16] have employed spatial and channel-wise attention modules with depth-wise separable convolution in DenseNet. Their model performs well on maize species of PlantVillage dataset, with 98.50%. On their own collected Maize dataset, 95.86% accuracy is reported by the authors. In another work by Chen et al. [18], spatial and channel-wise attention mechanisms are applied to the MobileNet model. Their model also performs well, with 98.48% accuracy on Rice dataset. In the continuation with this work, Chen et al. [28] have also applied the squeeze-and-excitation (SE) block on MobileNet v2 to achieve 99.33% accuracy on a custom Rice dataset. In yet another paper, the MobileNet v2 model is used with depthwise separable convolution and spatial and channel-wise attention, and this model also shows excellent performance with 99.71% accuracy on a subset of PlantVillage [19]. In another custom dataset containing disease images from paddy, corn, and cucumber plants, their model achieves 99.13% accuracy [19]. In a more recent work by Zhao et al. [20], a CNN model with inception modules and residual blocks has been developed with the attention mechanism. In their model, a modified convolutional block attention module is used that helps in achieving 99.55% accuracy on corn, tomato, and potato datasets. With the introduction of ViT as a powerful image classification model, Lu et al. [29] have devised a plant disease detection model using the GhostNet and ViT blocks. The model has been evaluated on the GLDP12k dataset with 12,615 vine leaf images in 11 classes and achieves 98.14% accuracy.

A review of existing works indicates that CNN models with attention mechanisms have demonstrated higher accuracy for specific types of crops and their diseases. However, these models have not been analysed for the cases when they may fail. The confusion matrix only gives an idea of the number of miss-classifications for a particular class. But the model's behavior on miss-classified samples has not been explored enough. In other words, despite the high accuracy achieved by several recent models, the interpretability of those models has not been explored. With advances in explainable AI, it is crucial to develop methods that not only perform well on a variety of plant diseases, but also aid scientists in analyzing the reasons for high accuracy and possible failures in certain cases. In the present paper, a ViT-enabled CNN model is proposed that significantly improves the disease classification performance on a wide variety of plant diseases. Furthermore, prediction results are shown to be explainable, and are compared with those of existing CNN models.

## 2 Explainable vision transformer enabled convolutional neural network: PlantXViT

This section is devoted to the proposed model PlantXViT that uses ViT for plant disease detection and identification. The model consists of a CNN followed by the ViT. For the sake of completeness, a brief introduction to the ViT is presented first.

## 2.1 Vision Transformer

With the widespread success of transformer networks in natural language processing problems [21], Dosovitskiy et al. [22] developed the ViT model based on the architecture of the original transformer. The ViT is composed of self attention blocks and multilayer perceptron (MLP) networks with a linear projection and positional embedding mechanism for an input image. The organization of a typical ViT is presented in Fig. 1. As presented, the input image is divided into fixed size non-overlapping patches. Further, patches are flattened and positional embedding is performed with linear projection. The positional embedding is basically used to retain the positional information of patches with respect to the original image. The output vector is then passed to a stack of N number of transformer blocks. The main components of a typical transformer block are multi-head self-attention (MHA) and MLP. Each one is preceded by a normalisation layer and residual connection at the end. MHA includes self-attention, which is applied to each patch individually. In MHA, the input vector is transformed into three separate vectors: query (Q), key (K), and value (V). They are computed as Q = XW Q , K = XW K , and V = V W Q ; where W Q , W K , and W V are the weight matrices. A dot-product of Q and K is taken to generate a score matrix based on the saliency of the embedded patch. Then, the SoftMax activation function is applied to the score matrix. Further, the output is multiplied into V to generate the self-attention result as shown in Eq. 1 where d k represents the dimension of the vector K .

$$S A ( Q , K , V ) = S o f t M a x ( \frac { Q K ^ { T } } { \sqrt { d _ { k } } } ) * V$$

Figure 1: ViT block with multi-head self-attention block and self-attention



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un modelo de inteligencia [**_**_**_**



Finally, self-attention matrices are combined and passed onto a linear layer followed by a regression head. Self-attention enables the selection of relevant semantic features at image locations for classification. There can be any number of self-attentions present in the transformer encoder, known as MHA. Output of the MHA block can be calculated using Eq. 2. MLP is stacked in the transformer block after the MHA layer. MLP includes ANN layers with a GeLU activation function. The GELU activation is calculated by multiplying the input by its Bernoulli distribution. It has skip connections from the output of MHA, as presented in Fig. 1. The output of the transformer block can be calculated using Eq. 3.

$$M H A _ { o u t } = M H A ( N O R M ( x _ { i n } ) ) + x _ { i n }$$

Where x in is the input to transformer block NORM is the normalization layer, MHA is multi-head self-attention, and MHA out is the output of multi-head self attention layer.

$$T F _ { o u t } = M L P ( N O R M ( M H A _ { o u t } ) ) + M H A _ { o u t }$$

Where MLP is the multi layer perceptron block, and TF out is the output of the transformer block.

## 2.2 PlantXViT architecture

The main objective of this work is to create a hybrid model for plant disease identification that combines the capabilities of ViT [22] and CNN for plant disease detection and identification. Convolution ( Conv) blocks are used to efficiently extract local-level features while the transformer blocks are appended for global feature extraction. The overall pipeline of the PlantXViT is shown in Fig. 2. The key components of the proposed PlanxViT are Conv blocks of VGG16 and Inception v7, and ViT components - MHA, MLP with linear projections.

The PlantXViT model takes an input of size 224 × 224 × 3 as shown in Fig. 2. The model consists of two Conv blocks of VGG16 network pre-trained on the Imagenet dataset. Each block consists of two Conv layers and a max pooling layer. The output of second Conv block is 56 × 56 × 128 . This output is fed to a multi-level feature extraction block similar to Inception v7 Conv blocks as shown in Fig. 2. The multi-level feature extraction block is added for enhancing the local feature learnability of the model. The inception block generates an output of size 56 × 56 × 512 after concatenating the feature maps generated by different Conv layers.

Figure 2: Block diagram of proposed PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un modelo de inteligencia artificial (IA) que se utiliza para la [**_**_**_



The feature map is then converted into patches, each of size 5 × 5 . The flattened patches are then passed through linear projection and generate feature vector of size 121 × 16 . These vectors are fed to a stack of four transformer blocks for features extraction. Finally, the global average pooling layer is added to convert the output of the transformer block into a 1-dimensional vector. At the end, a fully connected layer with softmax activation is added, with the number of neurons equal to the number of classes in the dataset. The layer-wise parameter count is presented in Table 2. For a dataset with 4 class labels, the model contains 850 , 500 total trainable parameters. The model is trained, validated and tested on a variety of datasets. The experimental results on all the datasets are presented in Section 3.

Table 2: Total number of parameters of PlantXViT

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Input Layer, Output Shape: 224 × 224 × 3, Parameters: 0.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Conv2D, Output Shape: 224 × 224 × 64, Parameters: 1792.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Conv2D, Output Shape: 224 × 224 × 64, Parameters: 36,928.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: MaxPooling2D, Output Shape: 112 × 112 × 64, Parameters: 0.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Conv2D, Output Shape: 112 × 112 × 128, Parameters: 73,856.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Conv2D, Output Shape: 112 × 112 × 128, Parameters: 147,584.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: MaxPooling2D, Output Shape: 56 × 56 × 128, Parameters: 0.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Inception v7, Output Shape: 56 × 56 × 512, Parameters: 361,728.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: PatchEncoder, Output Shape: 121 × 16, Parameters: 206,752.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Transformer block 1, Output Shape: 121 × 16, Parameters: 5440.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Transformer block 2, Output Shape: 121 × 16, Parameters: 5440.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Transformer block 2, Output Shape: 121 × 16, Parameters: 5440.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Transformer block 4, Output Shape: 121 × 16, Parameters: 5440.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Normalization Layer, Output Shape: 121 × 16, Parameters: 32.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Global Average Pooling 1D, Output Shape: 16, Parameters: 0.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Output, Output Shape: 4, Parameters: 68.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Layer/Block: Total, Parameters: 850,500.
Thakur et al.

PlantXViT model is enriched by pre-trained VGG16 that helps in better parameter initialization; and an Inception v7 block that generates a rich pool of multi-scale features. The transformer blocks with MHA provide an efficient mechanism for image patch processing and help extract saliency in the patches. Fusion of CNN and transformer network makes a powerful feature extractor with a combination of global and local information and enhances the explainability of the model. The model is evaluated on five public datasets and the results are presented in the next section.

## 3 Results and discussion

The plant disease detection model PlantXViT was developed using five publicly available datasets. Comprehensive experiments were carried out to finalize the model architecture and to evaluate its performance. Further, the model's performance was also compared with five recent CNN models [15, 16, 18-20]. These include some of the recent lightweight CNN models and models that have used different attention mechanisms. In the following sections, details of the datasets, evaluation metrics, experimental setup, and performance results are presented. The results of the comparative performance of the model with other state-of-the-art CNN models are also analyzed. Further, the proposed model is evaluated in terms of its explainability using two standard methods- gradient-weighted class activation maps (Grad-CAMs) and Local Interpretable Model Agnostic Explanation (LIME).

After resizing all of the images in each dataset to 224 × 224 × 3 , the PlantXViT model was trained using training subsets from the datasets. For training the model, categorical cross-entropy loss with the Adam optimizer was used. The cross-entropy loss is defined in Eq. 4. The learning rate was set to 0.0001 and the batch size to 16. The validation dataset was used for the evaluation of the model's performance after each epoch. Once the model performed with the desired level of classification accuracy on the training and validation subsets, it was evaluated on the test dataset.

$$L o s s = - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } y _ { i } \log \hat { y } _ { i }$$

Here the loss for all the n samples in a batch was calculated using y i as the actual label and ˆ y i as the predicted value of the i-th sample.

## 3.1 Datasets

In the following experiments, five publicly available datasets are employed that have originated from different geographical locations and include a wide range of crops. The datasets are selected from different categories, ranging from small, balanced datasets with 400-500 images to large, imbalanced datasets with over 40K images. The goal of using these datasets from various contexts is to train the proposed model for a wide range of crops and their diseases and to evaluate its performance under various test scenarios. Out of the five publicly available datasets, PlantVillage dataset [30] contains 54,305 images in 38 classes, and Embrapa dataset [31] contains 46,376 images in 93 classes. These datasets contain multiple species with a variety of diseases affecting the plant's leaves. On the other hand, Apple [32], Maize [25] and Rice [33] datasets are single-species datasets selected for the experiments. The details of each dataset with the number of classes and size are presented in Table 3. Sample images from each of the datasets are shown in Fig. 3.

Table 3: Datasets used in the experiments

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Dataset: Apple [32], # of classes: 4, # of images: 1821.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Dataset: Embrapa [31], # of classes: 93, # of images: 46,376.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Dataset: Maize [25], # of classes: 4, # of images: 481.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Dataset: PlantVillage [30], # of classes: 38, # of images: 54,305.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Dataset: Rice [25], # of classes: 5, # of images: 560.
## 3.2 Evaluation Metrics

The model evaluation is done using standard classification performance measures. These include accuracy, precision, recall, F1-score, area under the receiver operating curve, and Cohen's kappa score.

Accuracy : Accuracy is a widely used performance metric for the image classification task. It defines the relationship between the actual class value and the predicted class value. The higher the accuracy value achieved by the algorithm,

Figure 3: Sample images from all the datasets: (a) rust (Apple), (b) citrus canker (Embrapa) (c) northern leaf blight (Maize) (d) potato late blight (PlantVillage) (e) leaf scald (Rice)



> **[💡 Descripción de Imagen VLM]:** La imagen es una serie de cinco fotos de hoas de plantas con manas de “ ” ” ” ”



the better performance is attained. Accuracy is defined as follows in Eq. 5.

$$A c c u r a c y = \frac { ( T P + T N ) } { ( T P + T N + F P + F N ) }$$

A true positive (TP) is the count of the samples belonging to a particular class A and predicted correctly in class A. Class true negative (TN) is the count of the samples that belong to class B and are predicted as class B. False-positive (FP) is the count of the samples that belong to class B but are predicted as A, and false-negative (FN) is the count of the samples that belong to class A but are predicted as class B.

Precision : It is the ratio of true positives to all predicted positives. It is in between the range of 0 and 1. The precision value should be as high as possible to define the preciseness of the algorithm. The formula of the precision is presented in Eq. 6.

$$P r e c i s i o n = \frac { T P } { ( T P + F P ) }$$

Recall : It defined the ratio between the true positive labels to all the actual positive labels. The value of recall lies in between 0 to 1. It is calculated as shown in Eq. 7.

$$R e c a l l = \frac { T P } { ( T P + F N ) }$$

F1-Score : It relates Precision and Recall by calculating the harmonic mean between them. The formula for F1-score is depicted in Eq. 8.

$$F 1 - S c o r e = 2 * \frac { ( P r e c i s i o n * R e c a l l ) } { ( P r e c i s i o n + R e c a l l ) }$$

Area Under the Curve (AUC) : AUC is the area covered by the receiver characteristic operator (ROC) curve. The ROC is calculated using the plot of true positive rate (TPR) (refer Eq. 9) and false positive rate (FPR) (refer Eq. 10).

$$T P R = \frac { T P } { ( T P + F N ) }$$

$$F P R = \frac { F P } { ( F P + T N ) }$$

Cohen's Kappa Score : Cohen's kappa coefficient or score is a probability based measure where the outcome is the level of agreement parties for classification problem. The formula of kappa score calculation is shown below in Eq. 11.

$$K a p p a = \frac { p _ { o } - p _ { e } } { ( 1 - p _ { e } ) }$$

Where p o is the relative agreement probability and p e is the hypothetical agreement probability between the parties.

In addition, confusion matrix, receiver-operating characteristic (ROC) curve analysis, t-distributed stochastic neighbor embedding (t-SNE) plots are used for evaluating the performance of the model. The confusion matrix and ROC curve

indicate the credibility of the model. The higher the ROC curve in the upper left corner, the better is the model's performance. The t-SNE plots demonstrated how good the model is in terms of distinctive feature extraction for different categories in a dataset [34]. Further, the model's explainability is evaluated using two standard methods, namely Grad-CAMs and LIME.

## 3.3 Experimental setup

All the experiments were performed on an Nvidia DGX A100 160GB station with four GPU A100 cards, each with 40 GB of memory. It has the Ubuntu 18.04 LTS operating system on the machine, with an AMD 7742 processor at 2.25-3.4 GHz and 512 GB of RAM. The proposed model and other selected models for comparison were implemented using the Keras framework with NVIDIA CUDA v11.5 and the cuDNN v8.3 library.

## 3.4 Results and analysis

A series of comparative experiments were carried out using CNNs and attention models on the test sets in order to show the effectiveness of the PlantXViT model in the plant disease detection task. One of the experiments is evaluated to select the patch size to feed it into the ViT part of the PlantXViT model. The size of each patch is a hyper-parameter which needs to be selected carefully to generate the best results. In the work, we experimented different patch sizes and came up with the best among them. The patch sizes of 1, 3, 5, 7, and 9 were selected in the experiment. The results for all the patch sizes are presented in Table 4. As per the results, patch size of 5 generated the best results in terms of accuracy, precision, recall and f1-score for all the datasets. However, AUC for patch size 1 and patch size 7 are better in Apple and Rice datasets, respectively.

Table 4: PlantXViT's performance with different patch size

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: Apple, Loss: Apple, Accuracy: Apple, Precision: Apple, Recall: Apple, F1 score: Apple, AUC: Apple, kappa score: Apple.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 1, Loss: 0.31, Accuracy: 92.47, Precision: 92.47, Recall: 92.47, F1 score: 92.47, AUC: 97.61, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 3, Loss: 0.58, Accuracy: 81.72, Precision: 81.52, Recall: 80.65, F1 score: 81.08, AUC: 95.21, kappa score: 0.73.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 5, Loss: 0.3, Accuracy: 93.55, Precision: 93.55, Recall: 93.55, F1 score: 93.55, AUC: 97.01, kappa score: 0.91.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 7, Loss: 0.44, Accuracy: 89.25, Precision: 89.73, Recall: 89.25, F1 score: 89.49, AUC: 96.91, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 9, Loss: 0.43, Accuracy: 88.17, Precision: 88.11, Recall: 87.63, F1 score: 87.87, AUC: 96.83, kappa score: 0.83.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: Embrapa, Loss: Embrapa, Accuracy: Embrapa, Precision: Embrapa, Recall: Embrapa, F1 score: Embrapa, AUC: Embrapa, kappa score: Embrapa.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 1, Loss: 0.53, Accuracy: 87.25, Precision: 89.59, Recall: 85.85, F1 score: 87.68, AUC: 98.52, kappa score: 0.87.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 3, Loss: 0.54, Accuracy: 86.61, Precision: 88.64, Recall: 85.11, F1 score: 86.84, AUC: 98.44, kappa score: 0.86.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 5, Loss: 0.46, Accuracy: 89.24, Precision: 91.17, Recall: 88.27, F1 score: 89.7, AUC: 98.73, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 7, Loss: 0.52, Accuracy: 87.63, Precision: 89.49, Recall: 86.68, F1 score: 88.06, AUC: 98.25, kappa score: 0.87.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 9, Loss: 0.68, Accuracy: 84.73, Precision: 86.81, Recall: 83.5, F1 score: 85.12, AUC: 97.72, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: Maize, Loss: Maize, Accuracy: Maize, Precision: Maize, Recall: Maize, F1 score: Maize, AUC: Maize, kappa score: Maize.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 1, Loss: 0.42, Accuracy: 86.42, Precision: 88.61, Recall: 86.42, F1 score: 87.5, AUC: 96.74, kappa score: 0.82.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 3, Loss: 0.44, Accuracy: 90.12, Precision: 91.03, Recall: 87.65, F1 score: 89.3, AUC: 95.48, kappa score: 0.87.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 5, Loss: 0.35, Accuracy: 92.59, Precision: 92.5, Recall: 91.36, F1 score: 91.93, AUC: 96.8, kappa score: 0.9.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 7, Loss: 0.44, Accuracy: 88.89, Precision: 92.31, Recall: 88.89, F1 score: 90.57, AUC: 95.43, kappa score: 0.85.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 9, Loss: 0.42, Accuracy: 87.65, Precision: 88.75, Recall: 87.65, F1 score: 88.2, AUC: 96.76, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: PlantVillage, Loss: PlantVillage, Accuracy: PlantVillage, Precision: PlantVillage, Recall: PlantVillage, F1 score: PlantVillage, AUC: PlantVillage, kappa score: PlantVillage.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 1, Loss: 0.11, Accuracy: 97.06, Precision: 97.38, Recall: 96.86, F1 score: 97.12, AUC: 99.76, kappa score: 0.97.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 3, Loss: 0.05, Accuracy: 98.66, Precision: 98.71, Recall: 98.62, F1 score: 98.66, AUC: 99.87, kappa score: 0.99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 5, Loss: 0.04, Accuracy: 98.86, Precision: 98.9, Recall: 98.81, F1 score: 98.85, AUC: 99.92, kappa score: 0.99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 7, Loss: 0.09, Accuracy: 97.3, Precision: 97.58, Recall: 97.08, F1 score: 97.33, AUC: 99.82, kappa score: 0.97.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 9, Loss: 0.08, Accuracy: 97.85, Precision: 98.01, Recall: 97.82, F1 score: 97.91, AUC: 99.78, kappa score: 0.98.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: Rice, Loss: Rice, Accuracy: Rice, Precision: Rice, Recall: Rice, F1 score: Rice, AUC: Rice, kappa score: Rice.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 1, Loss: 0.25, Accuracy: 93.33, Precision: 94.92, Recall: 93.33, F1 score: 94.12, AUC: 99.41, kappa score: 0.91.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 3, Loss: 0.27, Accuracy: 91.67, Precision: 94.74, Recall: 90, F1 score: 92.31, AUC: 99.38, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 5, Loss: 0.24, Accuracy: 95, Precision: 98.25, Recall: 93.33, F1 score: 95.73, AUC: 99.39, kappa score: 0.94.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 7, Loss: 0.21, Accuracy: 93.33, Precision: 94.83, Recall: 91.67, F1 score: 93.22, AUC: 99.73, kappa score: 0.91.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Patch size: 9, Loss: 0.21, Accuracy: 95, Precision: 94.92, Recall: 93.33, F1 score: 94.12, AUC: 99.51, kappa score: 0.94.
Performances of several optimizers were also evaluted for PlantXViT model to select the best among all for improved training. In the experiments, SGD, RMSProp, Adamax, Adam, and Nadam optimizers were compared to ensure the

effectiveness of the model. According to the results in Table 5, the PlantXViT model with the SGD optimizer showed a substantial decrease in the model results, while Adam was able to maintain the accuracy across all the datasets. Further, the Nadam optimizer performed well on PlantVillage dataset. However, the Adam optimizer's performance was found to be consistent across all the five datasets, irrespective of their sizes.

Table 5: Comparison of the various optimizer

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Apple, Loss: Apple, Accuracy: Apple, Precision: Apple, Recall: Apple, F1 score: Apple, AUC: Apple, kappa score: Apple.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: SGD, Loss: 0.95, Accuracy: 60.22, Precision: 68.25, Recall: 46.24, F1 score: 55.13, AUC: 84.36, kappa score: 0.42.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: RMSProp, Loss: 0.35, Accuracy: 93.55, Precision: 93.55, Recall: 93.55, F1 score: 93.55, AUC: 97.34, kappa score: 0.91.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adamax, Loss: 0.81, Accuracy: 68.28, Precision: 73.86, Recall: 60.75, F1 score: 66.67, AUC: 88.66, kappa score: 0.54.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adam, Loss: 0.3, Accuracy: 93.55, Precision: 93.55, Recall: 93.55, F1 score: 93.55, AUC: 97.01, kappa score: 0.1.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Nadam, Loss: 0.28, Accuracy: 93.01, Precision: 93.51, Recall: 93.01, F1 score: 93.26, AUC: 97.89, kappa score: 0.9.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Embrapa, Loss: Embrapa, Accuracy: Embrapa, Precision: Embrapa, Recall: Embrapa, F1 score: Embrapa, AUC: Embrapa, kappa score: Embrapa.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: SGD, Loss: 0.72, Accuracy: 81.31, Precision: 91.72, Recall: 72.42, F1 score: 80.94, AUC: 98.99, kappa score: 0.81.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: RMSProp, Loss: 0.71, Accuracy: 83.33, Precision: 83.33, Recall: 80.59, F1 score: 81.94, AUC: 97.83, kappa score: 0.83.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adamax, Loss: 0.56, Accuracy: 86, Precision: 92.28, Recall: 81.16, F1 score: 86.36, AUC: 98.99, kappa score: 0.85.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adam, Loss: 0.46, Accuracy: 89.24, Precision: 91.17, Recall: 88.27, F1 score: 89.7, AUC: 98.73, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Nadam, Loss: 0.53, Accuracy: 87.04, Precision: 88.72, Recall: 85.77, F1 score: 87.22, AUC: 98.41, kappa score: 0.87.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Maize, Loss: Maize, Accuracy: Maize, Precision: Maize, Recall: Maize, F1 score: Maize, AUC: Maize, kappa score: Maize.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: SGD, Loss: 0.75, Accuracy: 70.37, Precision: 73.68, Recall: 69.14, F1 score: 71.34, AUC: 90.32, kappa score: 0.61.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: RMSProp, Loss: 0.44, Accuracy: 87.65, Precision: 88.31, Recall: 83.95, F1 score: 86.07, AUC: 96.04, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adamax, Loss: 0.44, Accuracy: 90.12, Precision: 92.11, Recall: 86.42, F1 score: 89.17, AUC: 96.1, kappa score: 0.87.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adam, Loss: 0.35, Accuracy: 92.59, Precision: 92.5, Recall: 91.36, F1 score: 91.93, AUC: 96.8, kappa score: 0.9.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Nadam, Loss: 0.47, Accuracy: 87.65, Precision: 90.79, Recall: 85.19, F1 score: 87.9, AUC: 94.99, kappa score: .83.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: PlantVillage, Loss: PlantVillage, Accuracy: PlantVillage, Precision: PlantVillage, Recall: PlantVillage, F1 score: PlantVillage, AUC: PlantVillage, kappa score: PlantVillage.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: SGD, Loss: 0.09, Accuracy: 97.5, Precision: 98.07, Recall: 96.79, F1 score: 97.43, AUC: 99.95, kappa score: 0.97.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: RMSProp, Loss: 0.08, Accuracy: 97.72, Precision: 97.94, Recall: 97.52, F1 score: 97.73, AUC: 99.80, kappa score: 0.98.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adamax, Loss: 0.06, Accuracy: 98.49, Precision: 98.58, Recall: 98.33, F1 score: 98.45, AUC: 99.91, kappa score: 0.98.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adam, Loss: 0.04, Accuracy: 98.86, Precision: 98.9, Recall: 98.81, F1 score: 98.85, AUC: 99.92, kappa score: 0.99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Nadam, Loss: 0.03, Accuracy: 99.06, Precision: 99.14, Recall: 98.99, F1 score: 99.06, AUC: 99.92, kappa score: 0.99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Rice, Loss: Rice, Accuracy: Rice, Precision: Rice, Recall: Rice, F1 score: Rice, AUC: Rice, kappa score: Rice.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: SGD, Loss: 0.98, Accuracy: 70, Precision: 83.78, Recall: 51.67, F1 score: 63.92, AUC: 88.8, kappa score: 0.63.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: RMSProp, Loss: 0.36, Accuracy: 91.67, Precision: 94.55, Recall: 86.67, F1 score: 90.44, AUC: 98.38, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adamax, Loss: 0.55, Accuracy: 85, Precision: 94, Recall: 78.33, F1 score: 85.45, AUC: 96.6, kappa score: 0.81.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Adam, Loss: 0.24, Accuracy: 95, Precision: 98.25, Recall: 93.33, F1 score: 95.73, AUC: 99.39, kappa score: 0.94.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Optimizer: Nadam, Loss: 0.66, Accuracy: 76.67, Precision: 80.36, Recall: 75, F1 score: 77.59, AUC: 94.31, kappa score: 0.71.
The training and validation epoch-wise graph of accuracy and loss is presented in Fig. 4 for all the five datasets. The graphs converge perfectly for Maize, PlantVillage, and Rice datasets, whereas there is more difference in the training and validation data results for Apple and Embrapa datasets. For Embrapa dataset, the reason for this difference could be high imbalance and very few samples in case of some classes. In Apple dataset, samples with multiple diseases get misclassified due to textural similarity between different type of diseases.

The confusion matrices of the test set of Apple, Maize, and Rice datasets using PlantXViT are shown in Fig. 5. As the other two datasets, PlantVillage and Embrapa, have a large number of classes, it is not possible to plot the confusion matrix for the same. It can be observed that PlantXViT has a higher classification accuracy in all the three datasets. In the confusion matrix Fig. 5 (a), we can see that the classifications of healthy, rust, and scab are very accurate for Apple dataset. However, multiple diseases are highly misclassified, with only 30% of them correctly classified. Similarly, in Maize dataset (Fig. 5 (b)), Goss's bacterial wilt and phaeosphaeria spot are classified correctly. However, 10% of the test images in the eyespot class are misclassified as gray leaf spot and phaeosphaeria spot. On the other hand, 20% of the gray leaf images are misclassified as eye spots and phaeosphaeria spots. In Rice (see Fig. 5 (c)) dataset, the model correctly classifies images of bacterial leaf streak, leaf smut, stackburn, and white tip. Only 6.67% of the leaf scald images are misclassified as bacterial leaf streaks. It can be observed that leaves having more than one disease are highly misclassified in Apple dataset. On the other hand, diseases having similar structural elements, i.e., spots, are misclassified. The ROC curve for all five datasets is shown in Fig.6. The aforementioned figure demonstrates that the PlantXViT has achieved a good performance in all the five datasets.

Thakur et al.

Figure 4: Accuracy and loss graph for (a) Apple, (b) Embrapa, (c) Maize, (d) PlantVillage, and (e) Rice datasets.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



Figure 5: Normalized confusion matrix for (a) Apple, (b) maize, and (c) Rice datasets.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de barra de dos subgrá



PlantXViT is compared with five recently introduced CNN-based plant disease classification models [15, 16, 18-20]. The models chosen for comparison in this work are mainly recent models with attention mechanisms and lightweight structures. Each model represents a unique technique for disease detection, which makes the comparative results instructive. The parameters of the models are set to the same as the PlantXViT parameters for training. Table 6 shows the quantitative results of the different CNN models on all the five datasets. The PlantXViT model has an accuracy of 93.55%, 89.24%, 92.59%, 98.86%, and 98.33% on Apple, Embrapa, Maize, PlantVillage, and Rice datasets, respectively. Table 6 illustrates that the CNN models [15, 16, 18-20] designed on the basis of the attention mechanism are less effective than PlantXViT. It is able to achieve the best performance in all metrics for all five datasets.

In order to explain the effectiveness of PlantXViT in extracting right features for plant disease detection, the t-SNE method is used that shows the feature similarity and dissimilarity for samples of the same and different classes in a dataset [34]. The learned features of different datasets are projected onto the 2D-plane using t-SNE algorithm, an unsupervised nonlinear dimensionality reduction technique [34]. The visualisation results for all five datasets using 2-D vector scatter plots obtained with the t-SNE method are shown in Figures 7, 8, and 9. The results are also compared with the t-SNE plots of other state-of-the-art techniques. Output of the global average pooling layer is used to visualise feature maps for the proposed model. In Apple dataset (refer Fig. 7 (a)), red color denotes the healthy class, lemon green denotes multiple diseases in a single image, blue denotes the rust disease, and green denotes the scab disease. The

0.200

Figure 6: ROC for (a) Apple, (b) Maize, (c) Rice, (d) Embrapa, and (e) PlantVillage datasets.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



t-SNE features for all state-of-the-art methods have been compared to analyze distinctive feature extraction capabilities of different methods. Fig. 7 (a)(6) shows that the features are easily distinguishable and are the best among all other

Thakur et al.

Table 6: Comparison of the work with other state-of-the-art methods

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Apple, Loss: Apple, Accuracy: Apple, Precision: Apple, Recall: Apple, F1 score: Apple, AUC: Apple, kappa score: Apple.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Loss: 1.56, Accuracy: 62.37, Precision: 62.84, Recall: 61.83, F1 score: 62.35, AUC: 83.53, kappa score: 0.45.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Loss: 1.96, Accuracy: 55.91, Precision: 56.35, Recall: 54.84, F1 score: 55.58, AUC: 78.32, kappa score: 0.36.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Loss: 0.79, Accuracy: 83.33, Precision: 83.7, Recall: 82.8, F1 score: 83.25, AUC: 94.1, kappa score: 0.76.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Loss: 0.63, Accuracy: 83.33, Precision: 85.47, Recall: 82.26, F1 score: 83.83, AUC: 95.59, kappa score: 0.76.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Loss: 0.58, Accuracy: 88.71, Precision: 89.62, Recall: 88.17, F1 score: 88.89, AUC: 95.81, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Loss: 0.3, Accuracy: 93.55, Precision: 93.55, Recall: 93.55, F1 score: 93.55, AUC: 97.01, kappa score: 0.91.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Embrapa, Loss: Embrapa, Accuracy: Embrapa, Precision: Embrapa, Recall: Embrapa, F1 score: Embrapa, AUC: Embrapa, kappa score: Embrapa.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Loss: 0.77, Accuracy: 80.29, Precision: 83.07, Recall: 78.38, F1 score: 80.6, AUC: 97.8, kappa score: 0.82.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Loss: 0.6, Accuracy: 80.95, Precision: 85.08, Recall: 76.02, F1 score: 80.3, AUC: 98.02, kappa score: 0.78.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Loss: 1.11, Accuracy: 73.63, Precision: 80.12, Recall: 67.86, F1 score: 73.48, AUC: 98.02, kappa score: 0.73.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Loss: 1.12, Accuracy: 74.88, Precision: 82.93, Recall: 66.06, F1 score: 73.18, AUC: 98.2, kappa score: 0.75.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Loss: 0.36, Accuracy: 88.48, Precision: 89.13, Recall: 87.44, F1 score: 88.28, AUC: 98.23, kappa score: 0.88.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Loss: 0.46, Accuracy: 89.24, Precision: 91.17, Recall: 88.27, F1 score: 89.7, AUC: 98.73, kappa score: 0.89.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Maize, Loss: Maize, Accuracy: Maize, Precision: Maize, Recall: Maize, F1 score: Maize, AUC: Maize, kappa score: Maize.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Loss: 1.17, Accuracy: 54.32, Precision: 59.72, Recall: 53.09, F1 score: 56.21, AUC: 83.19, kappa score: 0.39.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Loss: 1.26, Accuracy: 49.38, Precision: 50.85, Recall: 37.04, F1 score: 42.86, AUC: 76.16, kappa score: 0.33.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Loss: 0.6, Accuracy: 87.65, Precision: 87.65, Recall: 87.65, F1 score: 87.65, AUC: 96.03, kappa score: 0.84.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Loss: 0.5, Accuracy: 88.89, Precision: 91.03, Recall: 87.65, F1 score: 89.31, AUC: 96.78, kappa score: 0.85.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Loss: 1.4, Accuracy: 77.78, Precision: 78.75, Recall: 77.78, F1 score: 78.26, AUC: 94.55, kappa score: 0.7.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Loss: 0.34, Accuracy: 92.59, Precision: 93.67, Recall: 91.36, F1 score: 92.5, AUC: 97.21, kappa score: 0.9.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantVillage, Loss: PlantVillage, Accuracy: PlantVillage, Precision: PlantVillage, Recall: PlantVillage, F1 score: PlantVillage, AUC: PlantVillage, kappa score: PlantVillage.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Loss: 0.16, Accuracy: 95.83, Precision: 96.2, Recall: 95.6, F1 score: 95.89, AUC: 99.7, kappa score: 0.96.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Loss: 0.4, Accuracy: 87.94, Precision: 89.59, Recall: 86.71, F1 score: 88.07, AUC: 99.14, kappa score: 0.85.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Loss: 1.07, Accuracy: 74.63, Precision: 80.92, Recall: 69.64, F1 score: 75.03, AUC: 98.18, kappa score: 0.74.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Loss: 0.17, Accuracy: 96.68, Precision: 97.49, Recall: 95.83, F1 score: 96.64, AUC: 99.26, kappa score: 0.97.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Loss: 0.12, Accuracy: 97.28, Precision: 97.49, Recall: 97.06, F1 score: 97.27, AUC: 99.78, kappa score: 97.15.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Loss: 0.04, Accuracy: 98.86, Precision: 98.90, Recall: 98.81, F1 score: 98.85, AUC: 99.92, kappa score: 0.99.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Rice, Loss: Rice, Accuracy: Rice, Precision: Rice, Recall: Rice, F1 score: Rice, AUC: Rice, kappa score: Rice.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Loss: 0.99, Accuracy: 71.67, Precision: 79.55, Recall: 58.33, F1 score: 69.31, AUC: 88.26, kappa score: 0.64.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Loss: 0.75, Accuracy: 76.67, Precision: 83.02, Recall: 73.33, F1 score: 77.87, AUC: 92.93, kappa score: 0.71.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Loss: 0.3, Accuracy: 96.67, Precision: 96.67, Recall: 96.67, F1 score: 96.67, AUC: 98.97, kappa score: 0.95.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Loss: 0.25, Accuracy: 95, Precision: 96.61, Recall: 96.61, F1 score: 96.61, AUC: 99.72, kappa score: 0.94.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Loss: 0.41, Accuracy: 91.67, Precision: 91.67, Recall: 91.67, F1 score: 91.67, AUC: 98.55, kappa score: 89.27.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Loss: 0.08, Accuracy: 98.33, Precision: 98.33, Recall: 98.33, F1 score: 98.33, AUC: 99.94, kappa score: 0.98.
methods for three disease classes, while categorization is difficult for multiple disease classes. Similarly, from Fig. 7 (b)(6) it can be observed that the proposed method can generate better clusters than all other approaches for Embrapa dataset. In Fig. 8 (c)(6), it is visible that all the four clusters are more separable than those for the other five methods for Maize dataset. Similarly, Fig. 8 (d)(6) demonstrates that the proposed method produces feature clusters comparable to all other methods. Fig. 9 (e) shows the clustering capabilities of the proposed method on Rice dataset. Thus, it can be concluded that the proposed model PlantXViT is quite efficient in understanding the salient features of different classes in a dataset.

Grad-CAM [35] results for the PlantXViT model and other competing models are shown in Fig. 10 using a sample of each of the five datasets. It is worth noting that the model developed by Karthik et al. [15] not so incapable in identifying the correct disease portion for all the five datasets, while other models identify the portion from the entire leaf with greater precision in Apple, Maize, and Rice datasets ([16, 18, 19]. Further, the model by Zhao et al. [20] is able to generate the structure of the disease portion in Apple and Maize datasets. However, it is unable to produce good results for Embrapa, PlantVillage, and Rice datasets. The PlantXViT is able to focus on the disease portion with better understanding of the disease texture and shape. These results have been verified for a large number of samples from the test datasets. For brevity, only one sample is chosen from each dataset to show representative results.

LIME is another interpretability method that uses model-agnostic features for analyzing the interpretability of results for a classifier [36]. It is based on the local linear approximation of the model. The LIME results for the PlantXViT model and other comparative models are presented in Fig. 11. The first row (a) shows the input image from each dataset.

Figure 7: t-SNE plots for (a) Apple and (b) Embrapa datasets. (1) Karthik et al. [15] (2) Chen et al. [16] (3) Chen et al. [19] (4) Chen et al. [18] (5) Zhao et al. [20] (6) PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



Figure 8: t-SNE plots for (c) Maize and (d) PlantVillage datasets. (1) Karthik et al. [15] (2) Chen et al. [16] (3) Chen et al. [19] (4) Chen et al. [18] (5) Zhao et al. [20] (6) PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



Figure 9: t-SNE plots for (e) Rice dataset. (1) Karthik et al. [15] (2) Chen et al. [16] (3) Chen et al. [19] (4) Chen et al. [18] (5) Zhao et al. [20] (6) PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de 6 subgrá



It may be noted that the model by Karthik et al. [15] is not able to identify the disease area correctly for the sample from PlantVillage dataset. Similarly, the model by Chen et al. [19] is not able to identify the disease correctly. The model by Chen et al. [16] generates comparatively better results. Further, the model by Chen et al. [18] generates good results for apple and Rice datasets, but not for other samples. However, the LIME results for Zhao et al. [20] indicate that the results are not much explainable for all the five datasets. It is indeed remarkable that the proposed PlantXViT model is able to capture the disease portion with better precision in the case of all the five datasets. These samples are just representative of how the methods are interpreting different types of diseases. These results have been verified for a large number of samples from the test datasets.

The PlantXViT model is designed with a lower number of trainable parameters to make the model compatible with mobile/handheld devices like drones and smartphones. A model's suitability for IoT devices does only depends on its low memory footprint, but also heavily depends on the computational needs, like the floating point operations (FLOPs). Table 7 shows the total number of parameters, trainable parameters, and GegaFLOPs ( GFLPOs). It may be noted that the proposed model has reasonably lower number of trainable and total parameters as compared to other models except for the case of the model developed by Karthik et al. [15]. But the downside of PlantXViT is that it is not able to maintain a lower count of GFLOPs due to the operations involved in the inception block. The approach by Chen et al. [19] has the least GFLOPs. However, it is at the cost of model's classification efficiency on all the parameters. A good balance is needed between the model's memory requirement, computational demands and the desired level of efficiency.

## 4 Conclusion

In the present work, a ViT enabled CNN model is proposed for plant disease detection and identification. The model combines the benefits of the transformer and CNN in achieving higher precision and accuracy in terms of its feature extraction capability and classification performance. The experimental results demonstrate that the model's performance is impressive on five publicly available datasets of different sizes with images captured under varying background conditions. In the experiment for plant disease detection, PlantXViT achieves 93.55%, 89.24%, 92.59%, 98.86%, and 98.33% overall accuracy on Apple, Embrapa, Maize, PlantVillage, and Rice datasets, respectively. It is remarkable to

## Thakur et al.

Figure 10: Grad-CAMs for (1) Apple, (2) Embrapa, (3) Maize, (4) PlantVillage, and (5) Rice datasets. (a) input image (b) Karthik et al. [15] (c) Chen et al. [16] (d) Chen et al. [19] (e) Chen et al. [18] (f) Zhao et al. [20] (g) PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



## Thakur et al.

Figure 11: LIME for (1) Apple, (2) Embrapa, (3) Maize, (4) PlantVillage, and (5) Rice datasets. (a) input image (b) Karthik et al. [15] (c) Chen et al. [16] (d) Chen et al. [19] (e) Chen et al. [18] (f) Zhao et al. [20] (g) PlantXViT



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de [**C **] ** **



Thakur et al.

Table 7: Comparison of the trainable parameters and FLOPs

Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Karthik et al. [15], Total params(M): 0.72, Trainable params(M): 0.72, GFLOPs: 3.59, Memory (MB): 2.8.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [16], Total params(M): 0.82, Trainable params(M): 0.82, GFLOPs: 3.4, Memory (MB): 0.76.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [19], Total params(M): 4.32, Trainable params(M): 2.06, GFLOPs: 0.78, Memory (MB): 16.8.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Chen et al. [18], Total params(M): 4.32, Trainable params(M): 2.06, GFLOPs: 0.83, Memory (MB): 16.9.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: Zhao et al. [20], Total params(M): 6.71, Trainable params(M): 6.71, GFLOPs: 11.9, Memory (MB): 25.8.
Según Explainable vision transformer enabled convolutional neural network for plant disease identification: PlantXViT (2022), Approach: PlantXViT, Total params(M): 0.85, Trainable params(M): 0.85, GFLOPs: 11.8, Memory (MB): 3.4.
note that the model outperforms other state-of-the-art models in efficiently identifying plant diseases. The model is also evaluated for the interpretability of its prediction results using Grad-CAM and LIME methods and the results show that the model's results are reasonably interpretable. The only hindrance in the applicability of PlantXViT is its higher computational requirement. In future, it is planned to work on reducing the FLOPs count while maintaining the model's efficiency and explainability.

## References

- [1] DESA. World population prospects 2019. https://www.un.org/development/desa/publications/ world-population-prospects-2019-highlights.html , 2019. Online; accessed 30-05-2020.
- [2] FAO. New standards to curb the global spread of plant pests and diseases. http://www.fao.org/news/story/ en/item/1187738/icode/ , 2021. Accessed: 2021-09-04.
- [3] Shanwen Zhang and Zhen Wang. Cucumber disease recognition based on global-local singular value decomposition. Neurocomputing , 205:341-348, 2016.
- [4] Yunyun Sun, Zhaohui Jiang, Liping Zhang, Wei Dong, and Yuan Rao. Slic\_svm based leaf diseases saliency map extraction of tea plant. Computers and electronics in agriculture , 157:102-109, 2019.
- [5] Sandeep Kumar, Basudev Sharma, Vivek Kumar Sharma, Harish Sharma, and Jagdish Chand Bansal. Plant leaf disease identification using exponential spider monkey optimization. Sustainable computing: Informatics and systems , 28:100283, 2020.
- [6] Chaojun Hou, Jiajun Zhuang, Yu Tang, Yong He, Aimin Miao, Huasheng Huang, and Shaoming Luo. Recognition of early blight and late blight diseases on potato leaves based on graph cut segmentation. Journal of Agriculture and Food Research , 5:100154, 2021.
- [7] Hamdani Hamdani, Anindita Septiarini, Andi Sunyoto, Suyanto Suyanto, and Fitri Utaminingrum. Detection of oil palm leaf disease based on color histogram and supervised classifier. Optik , 245:167753, 2021.
- [8] S Ramesh and D Vydeki. Recognition and classification of paddy leaf diseases using optimized deep neural network with jaya algorithm. Information processing in agriculture , 7(2):249-260, 2020.
- [9] Alexander Johannes, Artzai Picon, Aitor Alvarez-Gila, Jone Echazarra, Sergio Rodriguez-Vaamonde, Ana Díez Navajas, and Amaia Ortiz-Barredo. Automatic plant disease diagnosis using mobile capture devices, applied on a wheat use case. Computers and electronics in agriculture , 138:200-209, 2017.
- [10] Aliyu Muhammad Abdu, Musa Mohd Mokji, and Usman Ullah Sheikh. Automatic vegetable disease identification approach using individual lesion features. Computers and Electronics in Agriculture , 176:105660, 2020.
- [11] Sharada P Mohanty, David P Hughes, and Marcel Salathé. Using deep learning for image-based plant disease detection. Frontiers in plant science , 7:1419, 2016.
- [12] Jayme Garcia Arnal Barbedo. Impact of dataset size and variety on the effectiveness of deep learning and transfer learning for plant disease classification. Computers and electronics in agriculture , 153:46-53, 2018.
- [13] Shuangjie Huang, Guoxiong Zhou, Mingfang He, Aibin Chen, Wenzhuo Zhang, and Yahui Hu. Detection of peach disease image based on asymptotic non-local means and pcnn-ipelm. IEEE Access , 8:136421-136433, 2020.
- [14] Saumya Yadav, Neha Sengar, Akriti Singh, Anushikha Singh, and Malay Kishore Dutta. Identification of disease using deep learning and evaluation of bacteriosis in peach leaf. Ecological Informatics , page 101247, 2021.
- [15] R Karthik, M Hariharan, Sundar Anand, Priyanka Mathikshara, Annie Johnson, and R Menaka. Attention embedded residual cnn for disease detection in tomato leaves. Applied Soft Computing , 86:105933, 2020.

- [16] Junde Chen, Wenhua Wang, Defu Zhang, Adnan Zeb, and Yaser Ahangari Nanehkaran. Attention embedded lightweight network for maize disease recognition. Plant Pathology , 2020.
- [17] Xiao Chen, Guoxiong Zhou, Aibin Chen, Jizheng Yi, Wenzhuo Zhang, and Yahui Hu. Identification of tomato leaf diseases based on combination of abck-bwtr and b-arnet. Computers and Electronics in Agriculture , 178: 105730, 2020.
- [18] Junde Chen, Defu Zhang, Adnan Zeb, and Yaser A Nanehkaran. Identification of rice plant diseases using lightweight attention networks. Expert Systems with Applications , 169:114514, 2021.
- [19] Junde Chen, Defu Zhang, Md Suzauddola, and Adnan Zeb. Identifying crop diseases using attention embedded mobilenet-v2 model. Applied Soft Computing , 113:107901, 2021.
- [20] Yun Zhao, Cheng Sun, Xing Xu, and Jiagui Chen. Ric-net: A plant disease classification model based on the fusion of inception and residual structure and embedded attention mechanism. Computers and Electronics in Agriculture , 193:106644, 2022.
- [21] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in neural information processing systems , pages 5998-6008, 2017.
- [22] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 , 2020.
- [23] Behnam Neyshabur. Towards learning convolutions from scratch. Advances in Neural Information Processing Systems , 33:8078-8088, 2020.
- [24] Edna Chebet Too, Li Yujian, Sam Njuki, and Liu Yingchun. A comparative study of fine-tuning deep learning models for plant disease identification. Computers and Electronics in Agriculture , 161:272-279, 2019.
- [25] Junde Chen, Jinxiu Chen, Defu Zhang, Yuandong Sun, and Yaser Ahangari Nanehkaran. Using deep transfer learning for image-based plant disease identification. Computers and Electronics in Agriculture , 173:105393, 2020.
- [26] Poornima Singh Thakur, Tanuja Sheorey, and Aparajita Ojha. Vgg-icnn: A lightweight cnn model for crop disease identification. Multimedia Tools and Applications , pages 1-24, 2022.
- [27] Weihui Zeng and Miao Li. Crop leaf disease recognition based on self-attention convolutional neural network. Computers and Electronics in Agriculture , 172:105341, 2020.
- [28] Junde Chen, Defu Zhang, Md Suzauddola, Yaser Ahangari Nanehkaran, and Yuandong Sun. Identification of plant disease images via a squeeze-and-excitation mobilenet model and twice transfer learning. IET Image Processing , 2021.
- [29] Xiangyu Lu, Rui Yang, Jun Zhou, Jie Jiao, Fei Liu, Yufei Liu, Baofeng Su, and Peiwen Gu. A hybrid model of ghost-convolution enlightened transformer for effective diagnosis of grape leaf disease and pest. Journal of King Saud University-Computer and Information Sciences , 34(5):1755-1767, 2022.
- [30] David Hughes, Marcel Salathé, et al. An open access repository of images on plant health to enable the development of mobile disease diagnostics. arXiv preprint arXiv:1511.08060 , 2015.
- [31] Jayme Garcia Arnal Barbedo, Luciano Vieira Koenigkan, Bernardo Almeida Halfeld-Vieira, Rodrigo Veras Costa, Katia Lima Nechet, Claudia Vieira Godoy, Murillo Lobo Junior, Flavia Rodrigues Alves Patricio, Viviane Talamini, Luiz Gonzaga Chitarra, et al. Annotated plant pathology databases for image-based detection and recognition of diseases. IEEE Latin America Transactions , 16(6):1749-1757, 2018.
- [32] Ranjita Thapa, Noah Snavely, Serge Belongie, and Awais Khan. The plant pathology 2020 challenge dataset to classify foliar disease of apples. arXiv preprint arXiv:2004.11958 , 2020.
- [33] Junde Chen, Huayi Yin, and Defu Zhang. A self-adaptive classification method for plant disease detection using gmdh-logistic model. Sustainable Computing: Informatics and Systems , 28:100415, 2020.
- [34] Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. Journal of machine learning research , 9(11), 2008.
- [35] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra. Grad-cam: Visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE international conference on computer vision , pages 618-626, 2017.
- [36] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. " why should i trust you?" explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining , pages 1135-1144, 2016.