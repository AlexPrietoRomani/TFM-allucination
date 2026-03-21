---
id: arxiv-2312.10948
title: A Multimodal Approach for Advanced Pest Detection and Classification
year: 2023
country: Internacional
source: ArXiv (cs.CV, cs.AI)
doc_type: Artículo científico
language: en
tags:
  - detección de plagas
  - deep learning
  - clasificación de imágenes
  - artículo científico
  - ArXiv
---

## A Multimodal Approach for Advanced Pest Detection and Classification

Jinli Duan 1 * , Haoyu Ding 1 * , Sung Kim 1 *

1 NYU Tandon jd5374@nyu.edu, haoyu ding@outlook.com, sk9623@nyu.edu

## Abstract

This paper presents a novel multi modal deep learning framework for enhanced agricultural pest detection, combining tiny-BERT's natural language processing with R-CNN and ResNet-18's image processing. Addressing limitations of traditional CNN-based visual methods, this approach integrates textual context for more accurate pest identification. The RCNN and ResNet-18 integration tackles deep CNN issues like vanishing gradients, while tiny-BERT ensures computational efficiency. Employing ensemble learning with linear regression and random forest models, the framework demonstrates superior discriminate ability, as shown in ROC and AUC analyses. This multi modal approach, blending text and image data, significantly boosts pest detection in agriculture. The study highlights the potential of multi modal deep learning in complex real-world scenarios, suggesting future expansions in diversity of datasets, advanced data augmentation, and cross-modal attention mechanisms to enhance model performance.

## Introduction

Pest infestations in agricultural crops are a concern to the world with some far reaching consequences, and it can cause a lower quality of agricultural product or permanent damage and compromise lead to reduction significantly. Which has implications for food security, economic stability. In the rapidly evolving agricultural technology and deep learning techniques could migrate this problem. In order to prevent or migrate the growth of the agricultural pests, detecting pests precisely and timelessly is crucial.

Traditional image detection methods which are also used for the pest detection, particularly relying on single methods such as Convolutions Neural Network (CNN) models to primarily focus on visual data analysis (Alzubaidi et al. 2021). Using R-CNN models have shown efficacy in image recognition tasks Image detection(Bharati and Pramanik 2020); however this reliance on solely visual limits there could be possible improvement through integrating a model from others.

This report introduces a multi-modal deep learning approach, combining the strength of tiny-BERT which and RCNN with ResNet-18 as backbone, which has exceptional

* These authors contributed equally to this work.

Copyright © 2023, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

performance in natural language processing. The combination of visual data processing and natural language processing can increase the possible positive differences (Jiao et al. 2019).

The R-CNN with ResNet-18(Residual Network-18) is used instead of traditional CNN architectures due to innovative use of residual network learning (Targ, Almeida, and Lyman 2016). This effectively addresses the vanishing gradient problems, and over fitting issues can be occurred in deep CNN. thereby allowing the construction of a much deeper, yet more accurate and efficient model for this project. Tiny-Bert is employed over the standard Transformer and regular BERT models due to its optimized architecture. It allows while maintaining a performance analogous to its predecessors in natural language processing tasks, markedly reduces computational and consumption of the resources. Therefore, it can reduce the size significantly while maintaining much of the performance by giving slight trade off in accuracy.

Notwithstanding the potential for yielding favorable outcomes, there remains consideration of its applicability and effectiveness. The process of collecting image-labeled data presents a certain degree of tedious; however it is relatively more straightforward contrasted with language input data sets. The data-sets for fine tuning tiny-BERT dominantly derived from LLAVA which necessitated the use of a high performance graphics processing unit and considerable investment in time for data-sets (Liu et al. 2023a). Despite these challenges, the result of both combinations of tinyBERT and RCNN augmented by ResNet-18 as backbone, yielded satisfying outcomes, and demonstrably distinctions of integrative approach.

## Related Work

The domain of image detection has significant advancement with CNNs. Prominent among these developments are models as ResNet, VGG, GoogleNet, Alexnet and other CNN methods are used as backbone. According to Nyarko The models AlexNet, ResNet-50, and Inception-V3 were employed, with ResNet-50 achieving the highest accuracy in facial recognition via mouth detection, recording 100 percent accuracy in training and 97.5 percent in testing. This performance notably surpassed that of the other models (Nyarko et al. 2022). The ResNet-50 demonstrated notably superior performance compared to the other models; therefore, this model is suited for the backbone of the R-CNN image classification model. Even Though there is a slight trade off for ResNet-18 because of the efficiency this model suits for the method. Zhang Claimed that CNN models with large data-sets and retraining with smaller data-set is effective to solve large and diverse data sets in the pest recognition field (Zhang, Chen, and Yuan 2023). the MSR-RCNN method demonstrates significant improvements in pest detection by addressing the specific challenges of pest object characteristics, such as small size, varied scales, and high similarity (Teng et al. 2022). Employing the R-CNN framework demonstrates considerable efficacy in the identification and localization of pests within image data sets.

The transformer model revolutionized Natural Language Processing due to its unique structure and efficiency because the attention mechanism word of sequence does not matter to process step by step (Vaswani et al. 2017). And this parallel processing significantly speeds up training to improve. (Redmon et al. 2016). It is used as an actual object detection model with a CNN. unlike these 2 stage model. In our proposed model, we integrate Tiny-BERT as the linguistic processing component to analyze textual data extracted from images. This integration is designed to synergize with our RCNN framework, which is fortified with a ResNet-18 backbone, thereby enhancing the overall accuracy of the system.

multi modal enhancing their analytical robustness and accuracy in complex tasks. introduce MMCNN-MIML, a deep multi-modal CNN for MIML image classification, which outperforms on benchmarks due to its unique approach: it groups related class labels for better feature learning, represents images as bags of visual instances rather than single entities, and uses group descriptions to enhance discrimination of visually similar objects in different groups (Song et al. 2018). However, rather than directly integrating the Multi-Modal approach within the CNN model, our methodology entails independently scoring the Tiny-BERT model and subsequently amalgamating these scores in the final stage to achieve enhanced accuracy.

## Related Methods

In this section, we discuss several important metrics, loss functions, regularization techniques, and model fusion methods commonly used in our project.

## Metrics

1. F1 Score : The F1 Score is a widely used metric for evaluating classification models. In our case, we used F1 scores in CNN-Resnet scores by balancing the precision and recall to provides a more comprehensive performance assessment. The F1 score combines precision and recall and is defined as:

<!-- formula-not-decoded -->

2. Accuracy : Accuracy measures the ratio of correct predictions to the total number of predictions. This has been

used as Metrics for both CNN-Resnet model and Finetuned Tiny-BERT and is defined as:

<!-- formula-not-decoded -->

3. AUC (Area Under the ROC Curve) : The Area Under the Curve (AUC) metric measures a model's ranking ability, making it particularly suitable for rankingoriented tasks. AUC is insensitive to the balance of positive and negative samples, allowing for reasonable evaluation even in imbalanced scenarios. In contrast, other metrics like precision, recall, and F1 score can vary based on the threshold set for distinguishing between positive and negative samples. Since AUC doesn't require a manual threshold setting, it offers a holistic measurement approach. In our dataset, where the number of pest samples is approximately 1/2 higher than that of non-pest samples, AUC proves to be a more appropriate metric.

## Loss Functions

- Cross-entropy Loss : Cross-entropy loss is frequently employed in classification tasks(Zhang and Sabuncu 2018). For our case, we used Cross entropy loss in the process of both CNN-resnet and Fine-tuning Tiny-Bert for a binary classification purpose. It measures the dissimilarity between the predicted probabilities ( q ( x ) ) and the true probabilities ( p ( x ) ) and is defined as:

<!-- formula-not-decoded -->

## Regularization Techniques

- Dropout : Dropout is a widely adopted regularization technique in neural networks, pioneered by Srivastava et al. (Hinton et al. 2012). This method involves randomly deactivating individual neurons during the training phase with a probability 'p', while keeping them active with a probability of '1-p'. This stochastic process aids in mitigating the risk of overfitting, which is particularly crucial in complex models. In the context of our CNN-ResNet architectures, we observed a major issue of overfitting. This was evident from the disparity in performance metrics: the model achieved a remarkable accuracy of 99% on the training set, yet this accuracy has been dropped to 82% on the test set. To address this challenge, we employed the dropout strategy, experimenting with different probabilities. We found that setting the dropout rate to 0.2 yielded the most favorable outcome, striking a balance between learning efficiency and generalization capability. The following table provides a comparative analysis of various dropout rates and their corresponding impacts on the model's performance.

Table 1: Effects of Dropout on Model Accuracy

Según A Multimodal Approach for Advanced Pest Detection and Classification (2023), Methods: Trainset Accuracy, without dropout: 99, P=0.1: 94, P=0.2: 86, P=0.5: 54.
Según A Multimodal Approach for Advanced Pest Detection and Classification (2023), Methods: Testset Accuracy, without dropout: 82, P=0.1: 88, P=0.2: 90, P=0.5: 86.
## Experiment

Our approach leverages a hybrid model combining the powerful feature extraction capabilities of CNN-ResNet with the advanced language understanding of a fine-tuned Tiny BERT.

## CNN-ResNet Backbone model

The foundation of our visual recognition part is predicated on the CNN-ResNet architecture, a convolutional neural network renowned for its deep structure and residual connections.

Model Architecture We employ the ResNet50d model, obtained through the timm library, renowned for its pretrained weights that facilitate the extraction of generic visual features from a vast corpus of image data. To tailor the model to our classification task, the original fully connected layer is replaced with a new linear layer. This layer's output features are equivalent to the number of classes in our dataset, thus adapting the model to the specificities of our task.

Data Preprocessing Our preprocessing pipeline transforms the input images to a uniform size, enhancing the model's ability to learn scale-invariant features. Further data augmentation is applied to improve model robustness and generalization. This includes random horizontal flips, slight rotations, and automatic contrast adjustments implemented using the transforms and albumentations libraries.

Training and Validation The model is fine-tuned using custom training and validation functions, which involve computing the loss and accuracy metrics while monitoring performance through the MetricMonitor class. We use cross-entropy loss for training and an AdamW optimizer for weight adjustment. A cosine annealing strategy is applied to the learning rate after each epoch, aiding in the stabilization of the training process over successive iterations.

Performance Evaluation To assess the model's capability in handling multi-class classification, we utilize macroaveraged F1 scores, accuracy and recall rates as our primary performance metrics. In essence, the CNN-ResNet component of our model is integral to capturing the nuanced patterns and textures present in pest image data.

## Fine-Tuned TinyBERT Model

In parallel with the visual recognition provided by the CNNResNet architecture, our framework incorporates the TinyBERT model for text classification. This choice is motivated by TinyBERT's smaller size and fewer parameters, making it ideal for fine-tuning on our dataset with a limited number of text descriptions generated using LLAVA(Liu et al. 2023b).

Model Architecture TinyBERT is a compact version of the larger BERT model(Jiao et al. 2020), renowned for its effectiveness in natural language processing tasks. Weutilize the pre-trained TinyBERT General 4L 312D model from the Hugging Face transformers library. The model is adapted to our specific task by adjusting the number of output labels to correspond to the categories in our dataset.

Dataset preprocess In the context of our dataset, which primarily consists of about 5500 images of insects , a critical aspect of classification is identifying whether an insect belongs to a pest species. This determination hinges not only on the species of the insect but also significantly on its interaction with the image background, particularly in agricultural settings. LLA V A generates comprehensive text descriptions that encapsulate these crucial details based on image set.

When LLAVA analyzes each image, it goes beyond mere species recognition. It delves into the contextual relationship between the insect and its surroundings and the generated textual descriptions, therefore, contain nuanced information that describes not just the insect but also its activities and surroundings. For example, a description might include details such as '...a bee standing on a purple flower...' or '...a blue blanket with a small hole in it, possibly caused by a bug...' providing critical insights into the potential impact of the insect on the environment.

Figure 1: LLAVA prompt

<!-- image -->

This enriched data, once preprocessed and tokenized using TinyBERT's tokenizer, offers a detailed and contextual basis for training our model. By incorporating both the identification of the insect species and the contextual understanding of its role in the environment, our model is better equipped to differentiate pests from non-pests, leading to more effective and practical applications in agricultural and ecological settings.

Training Procedure The fine-tuning of TinyBERT is carried out over a small number of epochs, considering the model's efficiency and our dataset's size. We employ the AdamW optimizer with a learning rate of 5 × 10 -5 and cross-entropy loss to guide the training process. The model is trained using a custom DataLoader, ensuring efficient batch processing and shuffling of the training data. Below is a loss/accurate rate vs Epoch for a 10 epochs training for Finetuned TinyBert:

Figure 2: Loss/Accurate-Epoch

<!-- image -->

Performance Metrics Model performance is evaluated using accuracy, a crucial metric given our task's classification nature. The accuracy is calculated on a separate test set, providing an objective measure of the model's ability to generalize to new data. This metric, along with qualitative analysis of model predictions, guides our assessment of the fine-tuning process's effectiveness.

In summary, the integration of TinyBERT allows our system to process and classify textual descriptions effectively, complementing the visual features extracted by the CNNResNet model. This dual approach, leveraging both image and text data, enhances the overall performance and applicability of our framework in multimodal classification tasks.

## Model Fusion Strategy

Our ensemble learning framework is designed to leverage the distinct predictive strengths of different models, aiming to enhance overall accuracy. We integrate a CNN+ResNet model with a fine-tuned Tiny Bert for NLP tasks, applying a weighted average, linear regression, and random forest models for fusion.

Weighted Average We calculate ensemble weights based on the accuracy metrics of the NLP and CV models to form a weighted average. The weights, w NLP for the NLP model and w CV for the CV model, are computed as follows:

<!-- image -->

Linear Regression Model A linear regression model is employed to process the outputs of the CNN+ResNet and Tiny Bert models. It is trained on the scores generated from these models and aims to predict the probability of the positive class:

- The model is trained using scores as features and ground truth labels as the target.
- It predicts continuous scores on the test data, which are then thresholded at 0.5 to generate binary classifications.
- The accuracy of the binary predictions is assessed by comparison with the test labels.

Random Forest Model We further employ a random forest classifier as part of our ensemble:

- The classifier is trained on the same scores from the CNN+ResNet and Tiny Bert models' trainset.
- It predicts class probabilities for the test data.
- Probabilities are thresholded at 0.5 to create binary predictions.
- Model accuracy is determined by how well these predictions match the ground truth labels.

## Main Result

Following the experimentation methods demonstrated above, as a result, we successfully integrated the linguistic and visual modalities to enhance pest detection: we processed textual data using the cutting-edge BERT model to capture contextual dependencies within pest description; concurrently, the ResNet model aided in the extraction of more complicated patterns from the visual input. And the merger of these elements was accomplished using multiple different concatenation methods that were specially tuned to capitalize on the particular strengths of each modality. In this section, we are going to take a glance at the final outcomes of our integrated model and analyze them using a visualized ROC &amp; AUC diagram.

Performance Metrics In the field of pest identification, where the cost of false negatives can be significant (e.g., a single species of unidentified pest could leave thousands acres of field in threat from their erosion). Therefore, a predictive model's ability to distinguish between classes accurately is critical, and how to measure such ability is worth consideration. In our study, we used the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) to evaluate model performance.

The ROC curve is a graphical representation of a binary classifier system's diagnostic capacity by comparing the True Positive Rate (TPR) versus the False Positive Rate (FPR) at various threshold values. The TPR, also known as sensitivity or recall, calculates the percentage of true positives that are correctly identified as such. The FPR, on the other hand, is the percentage of true negatives that are misidentified as positives. A model with a TPR of 1 and an FPR of 0 is ideal, but in practice, a trade-off will always be made.

As for the AUC. by measuring the area under the ROC curve, it gives a single, aggregate measure of performance across all categorization criteria. AUC of 1 indicates a flawless model; AUC of 0.5 indicates no discriminative capacity, which is similar to random guessing. Following is our outcome, demonstrated in a Figure 4, including the ROC curve and AUC value of our two original models and several different model using various integrating approach.

Figure 3: ROC and AUC for different models

<!-- image -->

Linear Regression (LR) Score Analysis The linear regression model produced a ROC curve with an AUC of 0.977 when trained using the combined feature set acquired from the NLP and CV scores. This displays a high level of discriminative ability, showing that the model can distinguish between the two classes reliably. The coefficients in the regression equation linked with the NLP and CV features highlighted the relative importance of each modality in predicting the outcome.

Weighted Average (WA) Score Analysis The WA method provides a nuanced approach to prediction by combining accuracy-weighted ratings from both NLP and CV models. The estimated weights were directly proportionate to the NLP and CV models' individual accuracies. This approach generated a ROC curve with an impressive AUC of 0.994, indicating its superior performance in test set assessments.

Random Forest (RF) Score Analysis We also used the RF model to , which operates by constructing multiple decision trees during training and outputting the class that is the majority vote of the individual trees (Belgiu and Dr˘ agut ¸ 2016). And it indeed had a significant discriminative capacity with an AUC of 0.985. The ROC curve linked with this model proved its robustness in accurately identifying the test data.

Model Comparison A comparison found that, while all models performed admirably, the WA model had the greatest AUC, closely followed by the RF model. We were able to analyze the trade-offs between model complexity and performance using this comparison, with the WA model appearing as a promising method due to its balance of simplicity and high accuracy.

According to the comparative ROC analysis, the combination of NLP and CV modalities via a weighted average technique produced the greatest performance among all these tested methodologies. And such a fact implies that, while each modality has qualities of its own, their combina- tion in various approaches can often lead to greater prediction capabilities. The constant AUC ratings above 0.97 for all models imply that each model can distinguish between the presence and absence of pests. The modest differences in AUC values among the models emphasize the impact of alternative feature representations and model topologies on the overall performance of the classifier.

## Conclusion

According to the experiment outcomes illustrated above, conducted following the fine-tuning and fusion strategies, we now have confidence to conclude that using text-image multimodal models could enhance the performance of pest detection.

The improved performance of multimodal models that integrate textual and visual data can be attributed to synergistic augmentation of data representation, a phenomenon in which each modality contributes unique and complementary information that would otherwise be absent or overlooked if considered separately (Gaonkar et al. 2021). On the one hand, textual descriptions elucidate behavioral patterns (such as granivorous or frugivorous tendencies), environmental contexts (such as the presence of leaves indicated by nibbled leaves), and temporal markers (denoting seasonal or diurnal cycles relevant to the observation), allowing for the differentiation of species with similar appearance and divergent ethological traits.

Visual data, on the other hand, provides important morphological subtleties and conspicuous pattern recognition elements required for emphasizing fine-grained details. The intersection of various modalities results in a more comprehensive and nuanced data interpretation framework, which improves the model's capacity to distinguish and categorize with more accuracy and precision.

What's more, the convergence of textual and visual information serves not only as a means of broadening data representation, but also as a strategic approach to mitigating the impact of unimodal noise - extraneous or non-informative elements inherent in each individual modality. Each data type, whether text or image, is vulnerable to informational noise or extraneous aspects, which can obscure the underlying patterns required for accurate classification. By crossreferencing and correlating these disparate data streams, the multimodal paradigm intrinsically favors the intersection of consistent and prominent elements present in both modalities. This methodological synergy successfully filters out unimodal noise, improving signal-to-noise ratio. As a result, because it capitalizes on the inherent strengths of each data source while limiting their unique limitations, this integrated approach develops a more robust and precise prediction model.

Future Improvement Our model's exceptional performance, as evidenced by an AUC close to 0.98, can be due in part to the deliberate use of dropout layers, a strategy used to reduce overfitting. Overfitting is a common problem in which a model becomes overly reliant on the training data, limiting its capacity to generalize. Dropout layers aid in model generalizability by randomly deactivating neu- rons during training. Furthermore, the dataset's small size and good quality are likely to have aided this level of performance. While a smaller, cleaner dataset helps to simplify the learning process and achieve unambiguous class distinctions, it's vital to note that it may not fully represent the model's performance in more complicated, real-world circumstances.

And in the foreseeable future, there are quite a lot of promising aspects for improvements. For example, we should increase the dataset size, which is critical for improving the model's accuracy and generalizability. A larger dataset with a broader range of pest species, environmental circumstances, and geographic locations can give the model with a deeper and more thorough training ground. This growth should not just focus on quantity but also on data diversity, including unusual and atypical insect infestation situations. A more diversified dataset would let the model to learn more complicated patterns while reducing the risk of overfitting, enhancing its performance in real-world circumstances.

Besides, using advanced data augmentation techniques can improve the model's robustness greatly. The reason why we argue so is that Advanced techniques for picture data, including as geometric modifications, photometric augmentations, and generative adversarial networks (GANs), can generate a variety of tough scenarios for the model to learn from (Mariani et al. 2018). And natural language processing techniques such as paraphrase, synonym replacement, and even producing synthetic text descriptions can provide a richer and more varied linguistic dataset for textual data. Overall, these enriched datasets can help the model better understand the complexities of pest detection and make it more resilient to changes in real-world data.

And finally, we could utilize integrating cross-modal attention mechanisms. As far as we're concerned, such utlization can improve the model's capacity to focus on relevant features of both text and visual input and such methods allow the model to recognize and prioritize the most informative information from each modality in real time, resulting in more accurate and contextually relevant predictions. This method is especially useful in complex settings where some textual properties may strongly correspond with specific visual patterns, necessitating the use of a model that can intelligently explore and integrate these multimodal inputs.

After all, you could access our project repository via: github.com/shirou10086/Deeplearning-NYU-2023

## References

Alzubaidi, L.; Zhang, J.; Humaidi, A. J.; Al-Dujaili, A.; Duan, Y.; Al-Shamma, O.; Santamar´ ıa, J.; Fadhel, M. A.; Al-Amidie, M.; and Farhan, L. 2021. Review of deep learning: Concepts, CNN architectures, challenges, applications, future directions. Journal of big Data , 8: 1-74.

Belgiu, M.; and Dr˘ agut ¸, L. 2016. Random forest in remote sensing: A review of applications and future directions. ISPRS Journal of Photogrammetry and Remote Sensing , 114: 24-31.

Bharati, P.; and Pramanik, A. 2020. Deep learning techniques-R-CNN to mask R-CNN: a survey. Computational Intelligence in Pattern Recognition: Proceedings of CIPR 2019 , 657-668.

Gaonkar, A.; Chukkapalli, Y.; Raman, P. J.; Srikanth, S.; and Gurugopinath, S. 2021. A Comprehensive Survey on Multimodal Data Representation and Information Fusion Algorithms. In 2021 International Conference on Intelligent Technologies (CONIT) , 1-8.

Hinton, G. E.; Srivastava, N.; Krizhevsky, A.; Sutskever, I.; and Salakhutdinov, R. R. 2012. Improving neural networks by preventing co-adaptation of feature detectors. arXiv:1207.0580.

Jiao, X.; Yin, Y.; Shang, L.; Jiang, X.; Chen, X.; Li, L.; Wang, F.; and Liu, Q. 2019. Tinybert: Distilling bert for natural language understanding. arXiv preprint arXiv:1909.10351 .

Jiao, X.; Yin, Y.; Shang, L.; Jiang, X.; Chen, X.; Li, L.; Wang, F.; and Liu, Q. 2020. TinyBERT: Distilling BERT for Natural Language Understanding. arXiv:1909.10351.

Liu, H.; Li, C.; Li, Y.; and Lee, Y. J. 2023a. Improved baselines with visual instruction tuning. arXiv preprint arXiv:2310.03744 .

Liu, H.; Li, C.; Wu, Q.; and Lee, Y. J. 2023b. Visual Instruction Tuning. arXiv:2304.08485.

Mariani, G.; Scheidegger, F.; Istrate, R.; Bekas, C.; and Malossi, C. 2018. BAGAN: Data Augmentation with Balancing GAN. arXiv:1803.09655.

Nyarko, B. N. E.; Bin, W.; Zhou, J.; Agordzo, G. K.; Odoom, J.; and Koukoyi, E. 2022. Comparative analysis of Alexnet, resnet-50, and inception-V3 models on masked face recognition. In 2022 IEEE World AI IoT Congress (AIIoT) , 337343. IEEE.

Redmon, J.; Divvala, S.; Girshick, R.; and Farhadi, A. 2016. You only look once: Unified, real-time object detection. In Proceedings of the IEEE conference on computer vision and pattern recognition , 779-788.

Song, L.; Liu, J.; Qian, B.; Sun, M.; Yang, K.; Sun, M.; and Abbas, S. 2018. A deep multi-modal CNN for multiinstance multi-label image classification. IEEE Transactions on Image Processing , 27(12): 6025-6038.

Targ, S.; Almeida, D.; and Lyman, K. 2016. Resnet in resnet: Generalizing residual architectures. arXiv preprint arXiv:1603.08029 .

Teng, Y.; Zhang, J.; Dong, S.; Zheng, S.; and Liu, L. 2022. MSR-RCNN: A multi-class crop pest detection network based on a multi-scale super-resolution feature enhancement module. Frontiers in Plant Science , 13: 810546.

Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A. N.; Kaiser, Ł.; and Polosukhin, I. 2017. Attention is all you need. Advances in neural information processing systems , 30.

Zhang, Y.; Chen, L.; and Yuan, Y. 2023. Multimodal FineGrained Transformer Model for Pest Recognition. Electronics , 12(12): 2620.

Zhang, Z.; and Sabuncu, M. R. 2018. Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels. arXiv:1805.07836.