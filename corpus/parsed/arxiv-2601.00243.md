---
id: arxiv-2601.00243
title: Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture
year: 2026
country: Internacional
source: ArXiv (cs.CV)
doc_type: Artículo científico
language: en
tags:
  - detección de plagas
  - manejo de plagas
  - agricultura de precisión
  - cultivos
  - plaguicidas
  - artículo científico
  - ArXiv
---

## Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture

Anirudha Ghosh 1 , Ritam Sarkar 2 , and Debaditya Barman 1 ,⋆

1 Department of Computer and System Sciences, Visva-Bharati, Santiniketan, India

2 Faculty of Technology, Uttar Banga Krishi Viswavidyalaya, Cooch Behar, India

<!-- image -->

Fig. 1: Overview of our proposed framework integrating a lightweight prototypical network for few-shot pest detection with the rule-based Decision Support System (integrates pest detection results with environmental factors) to recommend context-aware pesticides.

Abstract. Effective pest management is crucial for enhancing agricultural productivity, especially for crops such as sugarcane and wheat that are highly vulnerable to pest infestations. Traditional pest management methods depend heavily on manual field inspections and the use of chemical pesticides. These approaches are often costly, time-consuming, laborintensive, and can have a negative impact on the environment. To overcome these challenges, this study presents a lightweight framework for pest detection and pesticide recommendation, designed for low-resource devices such as smartphones and drones, making it suitable for use by small and marginal farmers.

⋆ Corresponding author. Email: debaditya.barman@visva-bharati.ac.in

## 2 A. Ghosh et al.

The proposed framework includes two main components. The first is a Pest Detection Module that uses a compact, lightweight convolutional neural network (CNN) combined with prototypical meta-learning to accurately identify pests even when only a few training samples are available. The second is a Pesticide Recommendation Module that incorporates environmental factors like crop type and growth stage to suggest safe and eco-friendly pesticide recommendations. To train and evaluate our framework, a comprehensive pest image dataset was developed by combining multiple publicly available datasets. The final dataset contains samples with different viewing angles, pest sizes, and background conditions to ensure strong generalization.

Experimental results show that the proposed lightweight CNN achieves high accuracy, comparable to state-of-the-art models, while significantly reducing computational complexity. The Decision Support System additionally improves pest management by reducing dependence on traditional chemical pesticides and encouraging sustainable practices, demonstrating its potential for real-time applications in precision agriculture.

Keywords: Pest Detection · Pesticide Recommendation · Deep Learning · Pest Management · Prototypical Meta-Learning · Few-Shot Classification · Edge Computing · Sustainable Agriculture · Precision Farming.

## 1 Introduction

Pests cause substantial economic losses by damaging crops, with sugarcane [18] and wheat [16] particularly vulnerable due to their across-the-board cultivation and economic significance. Pest infestations like cutting weevils, termites, and leafcutter ants in sugarcane, or wheat rust and cutworms in wheat, can drastically decrease outcomes. These losses not only affect farmers but also disrupt supply chains and threaten food availability for millions of people worldwide. So, effective pest management is vital for maintaining agricultural productivity with protecting global food security [14].

Traditional pest management practices, though adequate to some extent, face multiple challenges. Manual assessment for pest detection requires significant time investment and skilled labor, making it impractical for large-scale agriculture functions. Moreover, the overreliance on chemical pesticides, although delivering quick results, has led to long-term health and environmental damage [4]. These include water pollution, soil degradation [6], pest pesticide antagonism, and biodiversity loss [10]. Therefore, there is a need for efficient, sustainable, and scalable pest management solutions to manage these growing challenges.

To overcome the above challenges, this study focuses on developing a lightweight framework for pest detection and pesticide recommendations explicitly for sugarcane and wheat crops. The framework is designed to operate effectively with limited data (few training samples) by leveraging prototypical meta-learning [19] combined with a few-shot learning [13] strategy. This strategy allows quick

model adaptation to different pest types while maintaining good accuracy. Furthermore, combining a decision support system enables context-aware pesticide recommendations, promotes eco-friendly practices, and minimizes the chemical usage.

The key contributions of this work comprise the creation of a comprehensive pest dataset for sugarcane and wheat, a robust lightweight deep neural network for pest detection, and a rule-based recommendation system for pesticide recommendation. The framework highlights practicality, being compatible with low-resourced edge devices like drones and smartphones, allowing farmers to aid from real-time pest management tools. This study highlights the prospect of combining machine learning techniques with sustainable agricultural techniques to tackle demanding pest management challenges.

## 2 Related Work

Traditional pest management strategies depend on manual inspections and chemical pesticide applications. While useful in some situations, these methods are time-consuming, labor-intensive, and unsuited for large-scale agriculture operations. The overreliance on chemical pesticides has resulted in environmental degradation, pesticide resistance, and health risks [4, 6]. Recent advancements in deep learning have revolutionized pest classification to address these challenges, providing accurate and scalable solutions for precision agriculture.

Convolutional Neural Networks (CNNs) have appeared as the dominant approach for this pest detection and classification problem. The work in [9], developed a hybrid global and local feature-based pest monitoring system, acquiring high accuracy in multi-class pest detection. Similarly, the study at [11], integrated CNN models such as AlexNet and DenseNet201 with saliency-based methods to classify pest images, documenting an accuracy of 92.43% on a smaller dataset and 61.93% on the IP102 dataset. The study done by [7] used Region Proposal Networks (RPNs) and data augmentation strategies for pest localization, gaining a mean Average Precision (mAP) of 83.23%. In [15], authors presented a fine-grained detection model based on YOLOv4, acquiring a mAP of 96.29%, showcasing the robustness of CNN-based methods in agricultural pest detection.

Recently, lightweight CNNs have been presented to address the computational constraints of deploying models on resource-low devices like drones and smartphones. For instance, [17] optimized MobileNetV2 using dynamic learning rates with proper augmentation, achieving 71.32% accuracy on the IP102 dataset. The study done by [21], used DenseNet169 with transfer learning, reaching 88.83% accuracy for tomato pest classification. These lightweight models significantly reduce computational overhead, making them suitable for real-time applications. But their dependence on large datasets restricts their ability to generalize to rarely collected pests with unstructured environments.

Few-shot learning (FSL) has recently emerged as a solution to overcome training data scarcity. FSL allows models to generalize to unknown classes with limited labeled data. In the study by [2], the authors showed improved accu-

racy in one-shot scenarios by using fine-tuning techniques. In the survey [20], the authors employed lightweight architectures such as MobileNet for few-shot pest detection, achieving considerable performance advancements. The work of [12] explored metric learning strategies for few-shot pest classification, acquiring results in detecting cotton pests under several real-world scenarios.

Despite advancements in pest detection, integrating pest detection systems with actionable pesticide suggestions still needs to be investigated. The work by [8] showed multi-class pest detection utilizing ResNet152 but lacked contextaware pesticide suggestions. Likewise, [12] earned high detection accuracy utilizing Faster R-CNN but still required integrating a decision support system. This study presents a lightweight CNN integrated with a Decision Support System (DSS) to address these gaps.

## 3 Methodology

## 3.1 Framework Overview

Our proposed framework consists of two primary modules developed to enable efficient and real-time pest management for sugarcane and wheat crops:

- Pest Detection Module: This module employs a lightweight Convolutional Neural Network (CNN) for real-time pest detection. The model analyzes images captured from fields and accurately classifies pests into predefined categories using minimal data by leveraging prototypical meta-learning with a few-shot strategy. This lightweight design ensures compatibility with resource-constrained devices like smartphones and drones, enabling on-thego pest identification.
- Pesticide Recommendation Module: A rule-based Decision Support System (DSS) complements the pest detection module by combining pest classification results with environmental aspects such as crop type, growth stage, and pest severity. The DSS uses a knowledge mapping table to recommend suitable pesticides while emphasizing eco-friendly and decreased chemical usage procedures. This integration ensures context-aware, sustainable pest management solutions.

## 3.2 Dataset Creation

The dataset for sugarcane and wheat pests was created using a structured process to ensure balance and quality, with 30 samples per pest class from copyright-free repositories. Images were collected for pests such as Cutting Weevil, Leafcutter Ants, Red Palm Weevil, Sugarcane Woolly Aphids, and Termites for sugarcane, and Cutworms, Wheat Stem Sawfly, Termites, Wheat Thrips, and Wheat Leaf Rust for wheat. Pre-processing included resizing images to 100 × 100 pixels and ensuring quality and uniformity across all samples. A research team processed the dataset manually to eliminate irrelevant samples and maintain quality. Organized hierarchically by crop and pest categories, the final dataset includes 300

images, with 30 samples per class, ensuring sufficient diversity and readiness for testing through lightweight CNNs.

## 3.3 Model Architecture

The pest detection module employs a lightweight CNN architecture optimized for edge devices, utilizing prototypical meta-learning to enable effective pest identification with minimal data in few-shot settings. This design ensures compatibility with resource-constrained environments.

Fig. 2: Architecture of propose Lightweight Prototype Network Backbone.

<!-- image -->

The Lightweight Prototype Network Backbone (LPN-Backbone) architecture, illustrated in Figure 2, is developed with significantly fewer learnable parameters compared to ResNet18 and DenseNet169. While ResNet18 and DenseNet169 have approximately 12 million and 14 million parameters, the LPN consists of roughly 10 million. The LPN is structured into three stages for hierarchical feature extraction. It comprises four Feature Extraction Building Blocks (FEBBs) and four Reduction Blocks (RBs). The first stage includes two FEBBs, each followed by an RB, while the second and third stages feature one FEBB and one RB each. At the end of each stage, a Fully Connected module (FC) with three densely connected layers combines extracted features into the final feature embedding.

Each FEBB, shown in Figure 3, is made up of three Targeted Learning Blocks (TLBs) with a residual connection linking the input of the second Targeted Learning Block to the output of the third Targeted Learning Block, addressing vanishing gradient issues and improving stability dur-

Fig. 3: Architecture of FEBB

<!-- image -->

ing training. Following each FEBB, the RB reduces feature dimensions using a (3Œ3) convolutional layer combined with batch normalization (BN) and ReLU activation.

The core of each FEBB is the TLB, which extracts diverse features using three independent branches, each using unique convolutional operations:

- Branch A: Uses a ( 3 × 3 ) depthwise separable convolution to extract spatial features, followed by a (1 × 1) convolution to combine information across channels. Batch normalization (BN) and ReLU activation are applied to outputs consistent.
- Branch B: Inspired by ResNet, this branch starts with a (1 × 1) convolution to reduce input size, followed by a (3 × 3) grouped convolution to focus on essential features. A residual connection adds the input back to the output, ensuring feature preservation. BN and ReLU activation are applied to generate the final features with consistent shapes.
- Branch C: Combines a (1 × 1) pointwise convolution to simplify channel dimensions with a (3 × 3) dilated convolution to cover a wider input area. This design allows capturing more context without extra computations. BN and ReLU activation are applied to maintain stable outputs.

## 3.4 Decision Support System (DSS)

The DSS takes pest detection results along with environmental and growthspecific factors as input to recommend pesticide solutions for sugarcane and wheat. It relies on a rule-based knowledge to map pest types to optimal pesticide choices, as shown in Tables 1 and 2. As detailed in those tables, the DSS recommendations specify the kind of suitable pesticide for each pest, its corresponding crop, and environmental and growth stage conditions. However, dosage and timing are not explicitly listed in the tables and must be determined based on specific infestation severity and local guidelines.

Table 1: Knowledge Base for Pests Affecting Sugarcane

Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Cutting Weevil ( Apion spp. ), Growth Stage: Early growth, Environmental Condition: High humidity, Pesticide Recom- mended: Mild insecticide (e.g., Chlorpyrifos).
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Leafcutter Ants ( Atta spp. ), Growth Stage: Vegetative, Environmental Condition: Warm and dry, Pesticide Recom- mended: Bait-based pesti- cides (e.g., Hydram- ethylnon).
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Red Palm Weevil ( Rhynchophorus fer- rugineus ), Growth Stage: Any stage, Environmental Condition: High humidity, Pesticide Recom- mended: Pheromone-based lures and traps.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Sugarcane Woolly Aphid ( Siphunculus spp. ), Growth Stage: Vegetative, Environmental Condition: Moderate tempera- ture, high humidity, Pesticide Recom- mended: Natural predators (lady beetles) or Imidacloprid.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Termites (various species), Growth Stage: Any stage, Environmental Condition: Dry soil conditions, Pesticide Recom- mended: Soil treatment (e.g., Fipronil).
Table 2: Knowledge Base for Pests Affecting Wheat

Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Cutworms ( Agrotis spp. ), Growth Stage: Early growth, Environmental Condition: Cool, moist, Pesticide Recom- mended: Biological pesti- cide (e.g., Bacillus thuringiensis).
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Wheat Stem Sawfly ( Cephus cinctus ), Growth Stage: Vegetative, Environmental Condition: Dry, Pesticide Recom- mended: Pheromone traps or mild insecticides.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Wheat Thrips ( Thrips tabaci ), Growth Stage: Vegetative, Environmental Condition: Warm and dry, Pesticide Recom- mended: Sticky traps or Lambda-cyhalothrin.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Wheat Leaf Rust ( Puccinia triticina ), Growth Stage: Vegetative, Environmental Condition: High humidity, Pesticide Recom- mended: Fungicide (e.g., Propiconazole).
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Pest: Termites (various species), Growth Stage: Any stage, Environmental Condition: Dry soil conditions, Pesticide Recom- mended: Soil-applied insecti- cides (e.g., Chlor- pyrifos).
## 4 Experimental Setup

## 4.1 Training

Training Dataset Our framework utilizes prototypical meta-learning for fewshot classification, which demands a large collection of training with mini-tasks to simulate diverse scenarios effectively. To meet this requirement, we combined three publicly available datasets from Kaggle to form a comprehensive training dataset. The first dataset, the Dangerous Farm Insects Dataset [1], includes images of 15 harmful insects commonly found in agricultural environments. The second dataset, the Agricultural Pests Image Dataset [5], includes 12 pest classes: ants, bees, beetles, caterpillars, and weevils. Lastly, the Crop Pest Dataset [3] contains images of four pest types: rice stem borer, green leafhopper, rice bug, and rice leaf roller. This diverse collection of images enables the creation of varied training tasks, providing the foundation for model learning and generalization with a few-shot learning strategy.

Preprocessing and Augmentation The preprocessing and augmentation pipeline involved resizing images to 100Œ100 pixels, applying random color jitter (brightness, contrast, saturation, and hue), and performing affine transformations with random zoom up to 15%. Then, we apply random horizontal and vertical flips (with 50% probability each), and finally, we perform a grayscale conversion with three channels and normalization using ImageNet statistics.

Training Procedure The training process involves the meta-training of two base networks, ResNet18 and DenseNet169, along the proposed LPN, using the previously described training dataset. The models were trained over 200 metatasks (episodes), with each episode comprising separate mini-tasks. Each minitask was trained for 40 epochs to complete the meta-training phase. During

training, the k-way, n-shot protocol was used, where k (number of classes) and n (number of support samples per class) were randomly chosen between 5 to 10 and 1 to 15, respectively. The Adam optimizer minimizes the training loss, with a learning rate (LR) of 0.002 for all the networks. A dropout rate of 30% was applied to regularize all models and prevent overfitting. This training strategy enhanced the models ability to generalize effectively to new, unseen tasks.

Fig. 4: Training loss of ResNet18.

<!-- image -->

TrainingLoss over Mini-EpochsforEpisodes 0 to49

Fig. 5: Training loss of DensNet169.

<!-- image -->

Figure 4 illustrates the training loss for ResNet18, while Figure 5 presents the training loss for DenseNet169. Similarly, Figure 6 depicts the training loss for the proposed LPN model, highlighting its convergence behavior during the meta-training phase.

Fig. 6: Training loss of our proposed LPN.

<!-- image -->

Testing Procedure The testing procedure utilize a few-shot strategy for both the sugarcane and wheat testing datasets, each comprising five classes. Testing was conducted under 5-way 1-shot, 3-shot, and 5-shot scenarios. For the 1-shot setting, one support image per class was randomly selected. The 3-shot scenario expanded this by including the 1-shot support image along with two additional random images per class. Similarly, the 5-shot setting built upon the 3-shot scenario by adding two more random support images per class.

<!-- image -->

- (a) Recall Plot for Pest Detection Across 1-Shot, 3-Shot, and 5-Shot Configurations in Sugarcane
- (b) Recall Plot for Pest Detection Across 1-Shot, 3-Shot, and 5-Shot Configurations in Wheat

Fig. 7: Comparison of Recall and Precision for Pest Detection Across Different Shot Configurations in Sugarcane and Wheat.

## 5 Results and Discussion

## 5.1 Performance Metrics

The performance of all models for pest detection was evaluated using 1-shot, 3-shot, and 5-shot arrangements for wheat and sugarcane pests. The results, detailed in Tables 3 and 4, highlight the preeminent performance of our proposed LPN model compared to the baseline models (ResNet18 and DenseNet169). Each data point in those tables is generated based on the results of ten independent testing assignments. For wheat pests (Table 3), the LPN consistently exceeded the baselines in all configurations. In the 1-shot setting, the LPN achieved 72.00% accuracy for Cutworms and 69.71% for Wheat Leaf Rust, notably exceeding ResNet18 and DenseNet169. In the 5-shot configuration, the LPN further improved, showcasing its capability to leverage extra support images effectively.

Similarly, the LPN model displayed superior performance in sugarcane pest detection (Table 4). In the 3-shot configuration, it achieved 69.44% accuracy for Cutting Weevil and 77.62% for Sugarcane Woolly Aphids, surpassing both ResNet18 and DenseNet169. In the 5-shot setting, the LPN model maintained its lead with 74.81% accuracy for Red Palm Weevil and 68.43% for Termites.

Additionally, the pest detection recall plot (Figure 7a) for sugarcane pest and (Figure 7b) for wheat pest further validate our models effectiveness, demonstrating consistent improvement in recall across various shot scenarios. These results highlight the robustness and adaptability of the LPN model, particularly in few-shot learning scenarios.

Table 3: Performance Metrics (% Accuracy) for Sugarcane Pest Detection

Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: ResNet18, Shot Configu- ration: 1-Shot 3-Shot 5-Shot, Cutting Wee- vil: 55.11 ś 0.05 60.23 ś 0.06 64.78 ś 0.07, Leafcutter Ants: 50.21 ś 0.03 55.37 ś 0.04 59.84 ś 0.05, Red Weevil: 61.23 ś 0.04 66.01 ś 0.05 67.54 ś 0.06, Palm Sugarcane Woolly Aphids: 67.48 ś 0.03 71.15 ś 0.04 73.89 ś 0.05, Termites: 53.21 ś 0.07 58.47 ś 0.06 61.95 ś 0.08.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: DenseNet169, Shot Configu- ration: 1-Shot 3-Shot 5-Shot, Cutting Wee- vil: 49.92 ś 0.06 55.12 ś 0.07 60.87 ś 0.08, Leafcutter Ants: 47.04 ś 0.04 52.09 ś 0.05 56.47 ś 0.06, Red Weevil: 58.17 ś 0.05 62.43 ś 0.06 66.09 ś 0.07, Palm Sugarcane Woolly Aphids: 64.93 ś 0.04 68.31 ś 0.05 71.56 ś 0.06, Termites: 49.92 ś 0.08 54.35 ś 0.09 58.74 ś 0.10.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: LPN, Shot Configu- ration: 1-Shot 3-Shot 5-Shot, Cutting Wee- vil: 58.51 ś 0.05 64.87 ś 0.06 69.44 ś 0.07, Leafcutter Ants: 55.68 ś 0.03 61.22 ś 0.04 66.71 ś 0.05, Red Weevil: 66.11 ś 0.04 72.35 ś 0.05 74.81 ś 0.06, Palm Sugarcane Woolly Aphids: 71.21 ś 0.03 74.97 ś 0.04 77.62 ś 0.05, Termites: 57.38 ś 0.07 63.19 ś 0.06 68.43 ś 0.08.
Table 4: Performance Metrics (% Accuracy) for Wheat Pest Detection

Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: ResNet18, Shot Configu- ration: 1-Shot 3-Shot 5-Shot, Cutworms: 69.92 ś 0.05 75.03 ś 0.06 78.56 ś 0.07, Wheat Stem Sawfly: 54.75 ś 0.06 58.89 ś 0.07 63.21 ś 0.08, Termites: 48.69 ś 0.04 53.42 ś 0.05 57.98 ś 0.06, Wheat Thrips: 64.16 ś 0.07 68.72 ś 0.08 72.93 ś 0.09, Wheat Leaf Rust: 63.14 ś 0.05 67.39 ś 0.06 71.64 ś 0.07.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: DenseNet169, Shot Configu- ration: 1-Shot 3-Shot 5-Shot, Cutworms: 65.92 ś 0.05 70.14 ś 0.06 73.56 ś 0.07, Wheat Stem Sawfly: 49.76 ś 0.06 53.88 ś 0.07 58.14 ś 0.08, Termites: 45.73 ś 0.04 50.21 ś 0.05 54.13 ś 0.06, Wheat Thrips: 60.56 ś 0.07 64.98 ś 0.08 69.82 ś 0.09, Wheat Leaf Rust: 59.51 ś 0.05 63.18 ś 0.06 67.92 ś 0.07.
Según Context-Aware Pesticide Recommendation via Few-Shot Pest Recognition for Precision Agriculture (2026), Model: LPN, Shot Configu- ration: 1-Shot 5-Shot 5-Shot, Cutworms: 72.00 ś 0.05 76.58 ś 0.06 80.12 ś 0.07, Wheat Stem Sawfly: 59.01 ś 0.06 63.87 ś 0.07 68.52 ś 0.08, Termites: 53.15 ś 0.04 57.61 ś 0.05 61.19 ś 0.06, Wheat Thrips: 68.15 ś 0.07 72.48 ś 0.08 76.98 ś 0.09, Wheat Leaf Rust: 69.71 ś 0.05 73.23 ś 0.06 75.96 ś 0.07.
## 5.2 Analysis and Discussion

The experimental results highlight the superior performance of the lightweight LPN model, which consistently outperforms ResNet18 and DenseNet169, especially in the 3-shot and 5-shot settings, showing its ability to utilize additional support samples to improve classification accuracy. A paired t-test confirms that these performance gains are statistically significant (p &lt; 0.05) across both sugarcane and wheat pest datasets, establishing the reliability of the proposed approach. Its low computational needs make it ideal for real-time deployment on resource-constrained devices. Further, the Integration of the Decision Support System (DSS) improves the framework by offering actionable pesticide recommendations, prioritizing eco-friendly solutions with reducing chemical pesticide usage. The LPN model and DSS provide a robust, efficient, and sustainable solution for precision agriculture.

## 6 Conclusion and Future Work

This study delivered a lightweight model capable of proper pest detection and a decision support system for advising targeted pesticide solutions. The framework effectively balanced high performance in few-shot scenarios with low computational needs, making it practical for real-time use in resource-limited settings. By combining environmental and crop-specific elements, it encouraged sustainable pest management practices. Future measures will aim to enhance the dataset with more pest species, incorporate real-time environmental data via IoT devices, and extend the framework to support a broader variety of crops and agricultural conditions.

## Acknowledgement

The first author sincerely acknowledges the financial support received from the DST-INSPIRE Fellowship, which has helped him conduct this research.

## References

1. Dalal, T.: Dangerous insects dataset (2023), https://www.kaggle.com/datasets/tarundalal/dangerous-insects-dataset, accessed: 2024-08-20
2. Dhillon, G.S., Chaudhari, P., Ravichandran, A., Soatto, S.: A baseline for few-shot image classification. arXiv preprint arXiv:1909.02729 (2019)
3. Ghosh, P.: Crop pest dataset (2023), https://www.kaggle.com/datasets/pialghosh/croppest-dataset, accessed: 2024-08-20
4. Kandalkar, G., Deorankar, A., Chatur, P.: Classification of agricultural pests using dwt and back propagation neural networks. Int. J. Comput. Sci. Inf. Technol 5 (3), 4034-4037 (2014)

5. Lanz, V.: Agricultural pests image dataset (2023), https://www.kaggle.com/datasets/vencerlanz09/agricultural-pests-image-dataset, accessed: 2024-08-20
6. Larios, N., Deng, H., Zhang, W., Sarpola, M., Yuen, J., Paasch, R., Moldenke, A., Lytle, D.A., Correa, S.R., Mortensen, E.N., et al.: Automated insect identification through concatenated histograms of local appearance features: feature vector generation and region detection for deformable objects. Machine Vision and Applications 19 , 105-123 (2008)
7. Li, R., Wang, R., Zhang, J., Xie, C., Liu, L., Wang, F., Chen, H., Chen, T., Hu, H., Jia, X., et al.: An effective data augmentation strategy for cnn-based pest localization and recognition in the field. IEEE access 7 , 160274-160283 (2019)
8. Li, Z., Jiang, X., Jia, X., Duan, X., Wang, Y., Mu, J.: Classification method of significant rice pests based on deep learning. Agronomy 12 (9), 2096 (2022)
9. Liu, L., Xie, C., Wang, R., Yang, P., Sudirman, S., Zhang, J., Li, R., Wang, F.: Deep learning based automatic multiclass wild pest monitoring approach using hybrid global and local activated features. IEEE Transactions on Industrial Informatics 17 (11), 7589-7598 (2020)
10. Messelink, G.J., Lambion, J., Janssen, A., van Rijn, P.C.: Biodiversity in and around greenhouses: Benefits and potential risks for pest management. Insects 12 (10), 933 (2021)
11. Nanni, L., Maguolo, G., Pancino, F.: Insect pest image detection and recognition based on bio-inspired methods. Ecological Informatics 57 , 101089 (2020)
12. Nieuwenhuizen, A., Hemming, J., Suh, H.K.: Detection and classification of insects on stick-traps in a tomato crop using faster r-cnn (2018)
13. Parnami, A., Lee, M.: Learning from few examples: A summary of approaches to few-shot learning. arXiv preprint arXiv:2203.04291 (2022)
14. Pedigo, L.P., Rice, M.E., Krell, R.K.: Entomology and pest management. Waveland Press (2021)
15. Roy, A.M., Bose, R., Bhaduri, J.: A fast accurate fine-grain object detection model based on yolov4 deep neural network. Neural Computing and Applications 34 (5), 3895-3921 (2022)
16. Sehgal, M., Jeswani, M., Kalra, N.: Management of insect, disease, and nematode pests of rice and wheat in the indo-gangetic plains. The Rice-Wheat Cropping System of South Asia pp. 167-226 (2021)
17. Setiawan, A., Yudistira, N., Wihandika, R.C.: Large scale pest classification using efficient convolutional neural network with augmentation and regularizers. Computers and Electronics in Agriculture 200 , 107204 (2022)
18. Usman, M., Akram, N., Imtiaz, S., Haider, S.M.: Sugarcane: Diseases due to pests, pest management strategies and factors influencing the production of sugarcane. American Scientific Research Journal for Engineering, Technology, and Sciences (ASRJETS) 65 (1), 126-139 (2020)
19. Wang, R.Q., Zhang, X.Y., Liu, C.L.: Meta-prototypical learning for domainagnostic few-shot recognition. IEEE Transactions on neural networks and learning systems 33 (11), 6990-6996 (2021)
20. Wang, X., Huang, T.E., Darrell, T., Gonzalez, J.E., Yu, F.: Frustratingly simple few-shot object detection. arXiv preprint arXiv:2003.06957 (2020)
21. Xia, D., Chen, P., Wang, B., Zhang, J., Xie, C.: Insect detection and classification based on an improved convolutional neural network. Sensors 18 (12), 4169 (2018)