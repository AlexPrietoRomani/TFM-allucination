---
id: arxiv-2508.17653
title: FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis
year: 2025
country: Internacional
source: ArXiv (cs.CV)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - deep learning
  - artículo científico
  - ArXiv
---

## FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis

Saif Ur Rehman Khan 1,3* , Muhammad Nabeel Asim 1,2* , Sebastian Vollmer 1,2 and Andreas Dengel 1,2,3

1 German Research Center for Artificial Intelligence, Kaiserslautern, 67663, Germany.

2 Intelligentx GmbH (intelligentx.com), Kaiserslautern, Germany.

3 Department of Computer Science, Rhineland-Palatinate Technical University of Kaiserslautern-Landau Kaiserslautern, 67663, Germany.

*Corresponding author(s). E-mail(s): saif ur rehman.khan@dfki.de; muhammad nabeel.asim@dfki.de; Contributing authors: sebastian.vollmer@dfki.de;

andreas.dengel@dfki.de;

## Abstract

Early diagnosis of plant diseases is critical for global food safety, yet most AI solutions lack the generalization required for real-world agricultural diversity. These models are typically constrained to specific species, failing to perform accurately across the broad spectrum of cultivated plants. To address this gap, we first introduce the FloraSyntropy Archive, a large-scale dataset of 178,922 images across 35 plant species, annotated with 97 distinct disease classes. We establish a benchmark by evaluating numerous existing models on this archive, revealing a significant performance gap. We then propose FloraSyntropy-Net, a novel federated learning framework (FL) that integrates a Memetic Algorithm (MAO) for optimal base model selection (DenseNet201), a novel Deep Block for enhanced feature representation, and a client-cloning strategy for scalable, privacy-preserving training. FloraSyntropy-Net achieves a state-of-the-art accuracy of 96.38% on the FloraSyntropy benchmark. Crucially, to validate its generalization capability, we test the model on the unrelated multiclass Pest dataset, where it demonstrates exceptional adaptability, achieving 99.84% accuracy. This work provides not only a valuable new resource but also a robust

and highly generalizable framework that advances the field towards practical, large-scale agricultural AI applications.

Keywords: Large-Scale Plant Disease, Federated Knowledge Collection, Global Learning, Agriculture, Food Safety

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: FL, Detail form: federated learning.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: DL, Detail form: deep learning.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: SOTA, Detail form: state-of-the-art.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: CNN, Detail form: Convolution Neural Network.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: AI, Detail form: Artificial intelligence.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: MAO, Detail form: Memetic Algorithm Optimization.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: FedAvg, Detail form: Federated Averaging.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Abbreviation: TRIPOD, Detail form: Transparent Reporting of a multi prediction model for Individual Prognosis or Diagnosis.
## 1 Introduction

Plant diseases represent a significant threat to global food security and agricultural sustainability by causing significant losses in crop yields and economic damage worldwide [1] . These diseases disrupt essential plant functions by leading to reduced crop production and quality. Plant diseases are typically classified based on the pathogens responsible including fungi, bacteria, and viruses [2]. The timely and accurate diagnosis of these diseases is crucial to control their further spread and minimize their adverse impact on crop yields [3]. The importance of diagnosing plant diseases arises from their significant impact on agricultural productivity and economic stability. These diseases result in considerable yield losses, reduced species diversity, and increased costs for mitigation efforts [4]. Continuous monitoring and time-series analysis can further enhance early detection by facilitating timely intervention before symptoms become severe [5]. Symptoms of plant diseases vary depending on the pathogen and plant species, but common signs include water-soaked lesions, necrotic spots, mottling, necrosis, stunting, leaf curling, distortion, vein chlorosis, and ring spots [6]. These visual cues are often the first signs of infection and are crucial for initial diagnostic assessment. Traditionally, diagnosing plant diseases has relied on manual inspection, serological tests and visual assessment by trained experts, which often lack both in precision and scalability [6, 7]. These methods typically involve observing symptoms that are followed by microscopic examination of plant tissues or pathogen cultures. While these approaches have been widely used but have notable limitations, such as being labor-intensive, health risks, time-consuming, environmental pollution, and often prone to errors [8]. Additionally, the lack of knowledge among local farmers, the high costs of consulting experts, and the inherent inaccuracy of manual assessments further complicate disease

diagnosis [9]. These challenges emphasize the urgent need for automated, efficient, and accurate methods for detecting and classifying plant diseases.

Artificial intelligence (AI) techniques have emerged as powerful tools for automating plant disease diagnosis [10]. Deep learning (DL) models, especially convolutional neural networks (CNNs) have demonstrated remarkable capabilities in image recognition and classification by making them highly suitable for analyzing visual symptoms of plant diseases from images of leaves, stems, and fruits [11, 12]. These models autonomously extract complex features directly from raw image data for enabling accurate and rapid identification of various plant diseases. DL-based systems have shown promising results in differentiating between healthy and multiple diseased plants [13]. However, these systems require large, diverse, high-quality datasets for training that are challenging to acquire and annotate. Additionally, privacy concerns and high computational demands limit the scalability of centralized DL frameworks, especially when dealing with sensitive agricultural data from multiple sources [14].

The aforementioned limitations of traditional DL including its dependence on aggregated data and the associated privacy risks underscore the urgent need for alternative approaches. FL offers a compelling solution by facilitating collaborative model training across distributed datasets without the exchange of raw data [15, 16]. In the field of plant disease diagnosis, FL enables agricultural farms and research institutions to collaboratively develop robust classification models while maintaining the privacy of sensitive local data [17]. This decentralized framework effectively addresses privacy and governance concerns, while promoting the creation of more generalized and accurate models by integrating diverse datasets from various geographical regions and environmental conditions. Ultimately, the ability of FL to enhance data privacy makes it ideal for advancing secure and scalable AI applications in agricultural disease classification.

## 1.1 Study Novelty and Contribution

The performance of a deep learning (DL) model is a function of its architecture (A), its parameters (Parm), and the dataset (DS) on which it is trained. Formally, the expected performance on a real-world distribution P DS can be presented as:

<!-- formula-not-decoded -->

Literature presents [ ? ? ] that research in plant disease detection has been constrained by the use of limited, homogeneous, and often small-scale datasets. Let a typical small-scale dataset be defined as S DS , characterized by a limited number of samples S N .

<!-- formula-not-decoded -->

When a model is trained and evaluated solely on such a dataset, it optimizes for a narrow performance metric, often achieving high accuracy f ( A,Parm,S DS ). However, this leads to a critical generalization gap. The model performance on the true, global data distribution P DS is often significantly low:

<!-- formula-not-decoded -->

This disparity means that reported high accuracies in prior studies [14, 15] were likely optimistic and did not translate to reliable performance in diverse, real-world agricultural scenarios. The primary novelty of this work is to directly bridge this gap by constructing a large-scale, globally representative dataset, G DS , and a novel framework, FloraSyntropy-Net, designed to maximize f ( A,Parm,G DS ) with the explicit goal of ensuring that this performance is maintained on P DS .

This study makes the following contributions to the field of automated plant disease diagnosis:

- Introduction of the FloraSyntropy Archive: We present a large-scale, heterogeneous, and globally representative image dataset for plant disease diagnosis G DS, comprising 178,922 images across 97 distinct classes. Curated from 13 public repositories, this dataset directly addresses the critical research gap of small-scale, non-global evaluation and provides a robust benchmark for assessing true model generalizability.
- Architectural Innovation with the Novel Deep Block: We design and integrate a new learnable module that enhances the feature extraction capabilities of the base model. This block, which incorporates dense transformation, concatenation, and sequential feature restructuring, was empirically proven to boost overall accuracy by 1.64% and deliver substantial performance gains on numerous challenging, underperforming classes.
- A Novel Weighted Federated Optimization: We introduce a robust federated optimization scheme that moves beyond standard FedAvg. Our method incorporates a dynamic weight scaling factor ( n k /n ), which explicitly weights each client contribution to the global model update based on their data volume and class distribution. This ensures the framework is robust to the inherent data heterogeneity and imbalance found in real-world scenarios, leading to more stable and equitable learning.
- Demonstration of Exceptional Cross-Domain Generalization: We rigorously validate the FloraSyntropy-Net framework robustness not only on its primary FloraSyntropy archive but also through cross-domain adaptation on the unrelated multiclass Pest dataset. FloraSyntropy-Net achieved an efficient accuracy of 99.84%, demonstrating an unparalleled ability to generalize to novel visual features and biological concepts, a capability critically lacking in previous studies.

## 2 Related work

DL has become increasingly important in agriculture due to its capacity to process and analyze vast amounts of data [18]. This capability offers numerous benefits, such as enhanced productivity, cost reduction, and the promotion of sustainable farming practices. Yakkundimath et al.[19] employed DL models based on transfer learning for rice plant disease classification, using pre-trained VGG-16 and GoogleNet CNN models. The models were evaluated on a dataset of 12,000 labeled images representing three rice diseases and 24 symptoms, achieving classification accuracies of 92.24% and 91.28%, respectively. Hassan et al.[20] proposed a DL model incorporating inception layers, residual connections, and depthwise separable convolution. Their model

achieved 76.59% accuracy on the cassava dataset by demonstrating improved performance with fewer parameters compared to state-of-the-art models. Haque et al. [21] proposed a DL method for identifying diseases in maize crops using a custom dataset collected. Three architectures based on the Inception-v3 framework were trained on this dataset with the top-performing model achieved 95.99% of accuracy. The robust model was compared with SOTA approaches to assess its performance. DL offers a promising approach for various disease identification through crop images. However, this method raises concerns regarding data privacy, as it often necessitates the sharing of image data from multiple farms. However, the shift towards FL is becoming increasingly relevant due to the growing challenges posed by data heterogeneity. Adaptive federated learning (AFL) [16] methods are gaining significant attention for their potential to enhance model performance in federated settings.

Tripathy et al. [22] propose a novel approach using FL for rice leaf disease classification. Their method involves local training on nodes, followed by model aggregation at the server by utilizing pre-processed images, data augmentation, and feature extraction. The LeNet model optimized with the Spotted Hyena Archimedes Optimizer achieved a precision of 91.30% by showcasing reasonable performance in disease classification. Shrivastava et al.[23] proposed a federated learning-based crop disease classification method using the Vision Transformer model. Their method achieved 92.00% accuracy in disease detection, which was further improved to 97.00% with 20 clients, thus ensuring data privacy while enhancing performance. Chorney et al.[24] proposed a FL-based collaborative classifier for data privacy and efficiency in rice crop disease detection. Their model effectively classified multiple disease types and healthy states by achieving 83.24% accuracy performance. The accuracy can be further improved by using more advanced approaches. Hari et al.[17] propose Federated Deep Learning (FDL) for plant leaf disease detection, where local models trained on regionspecific datasets share knowledge with a parent model for reducing computational costs. Their method uses the Plant Village dataset and employs a lightweight Hierarchical Convolutional Neural Network (H-CNN) for achieving 93.00% testing accuracy. Deng et al. [25] propose a FL-based pest detection technique using an improved faster R-CNN with ResNet-101, multisize feature map fusion, and a soft-non maximum suppression (NMS) algorithm. Their method achieves an average detection accuracy of 90.27% for multiple pests and diseases in apples.

## 3 Methodology

This section details the FloraSyntropy-Net framework, a novel federated learning framework for collaborative model training. We begin by introducing the Novel Dataset FloraSyntropy Archive and the Genetic Algorithm for Global-Net Model Selection used to establish a robust base model. The core of our methodology involves Finetuning the Architecture and Leveraging Federated Collective Knowledge for Client Robustness. We then explain the process of Global FloraSyntropy-Net: Client Cloning and provide a FloraSyntropy-Net Sync: Client Training Guide for implementation. Finally, we present a comprehensive Overview of the framework, followed by its step-by-step Training and Evaluating procedures to validate its performance.

## 3.1 Novel Dataset FloraSyntropy Archive

A large-scale plant disease dataset is essential for enabling the rapid and accurate diagnosis critical to safeguarding global food security. Such a resource allows for the development of robust AI tools capable of identifying a wide spectrum of threats early. This timely detection is the key to implementing effective, targeted interventions, preventing devastating crop losses, minimizing pesticide overuse, and containing outbreaks before they cause widespread damage. From 2018 to 2023, a significant research gap existed, as no previous studies had comprehensively evaluated models on a large-scale, globally representative plant disease dataset. This limitation meant that the reported high accuracy of many models was often achieved on limited, controlled, or homogenous data, making their true real-world performance and generalizability unclear and potentially overstated. To directly address the limitation of small-scale, non-global evaluations, this study introduces the Novel FloraSyntropy Archive, a largescale, heterogeneous dataset compiled from 13 publicly available repositories spanning 2018 to 2023. This archive is meticulously curated to ensure global representation and diversity, culminating in a vast collection of 178,922 images across 97 distinct classes of diseased and healthy plants. The dataset integrates historically significant benchmarks like Plant Village (2018, 20,639 samples) [25] with extensive newer additions such as Cassava (2021, 53,303 samples) [26] and Plant Village V2 (2023, 70,000 samples) [27], while also including crucial specialized datasets for crops like Banana (BananaLSD, 2023) [28], Coffee (2019) [29], Soybean (2021) [30], Tea (2022) [31], and Sugarcane (2022) [32]. This comprehensive aggregation provides an unprecedented benchmark for developing and fairly evaluating robust, generalizable models for global plant disease diagnosis. Fig 1 presents a visual sample from each of the 13 repositories comprising the FloraSyntropy Archive, illustrating the diversity of its 178,242 total images.

## 3.2 Memetic Algorithm for Global-Net Model Selection

Selecting an optimal base model (Global-Net), is a critical step that significantly influences the performance of the entire FloraSyntropy-Net framework. To automate this selection process and identify the most robust and suitable architecture from a vast search space, we employed a Memetic algorithm optimization (MAO) [33]. The MAO is a hybrid metaheuristic that effectively combines the global exploration capabilities of a genetic algorithm with the local refinement efficiency of a local search strategy, making it exceptionally suited for complex optimization problems.

## Utilization and Initialization

The search process was initialized with a diverse population MP 0 of Pr = 11 highlyperforming, pre-trained models. This initial gene pool was carefully curated to ensure genetic diversity:

<!-- formula-not-decoded -->

where each model mp i represents a chromosome defined by its architectural hyperparameters hp arch i and its pre-trained weights W i from ImageNet. The objective

## Novel FloraSyntropy Plant Dataset Archive

DatasetCollection2018-2023

Fig. 1 Visual samples from the 13 constituent datasets of the Novel FloraSyntropy Archive, demonstrating the morphological diversity and scale of the collected 178,922 images across 97 classes.

<!-- image -->

was to find the model that maximizes the validation accuracy after a standardized preprocessing TD train , where F is the fitness function.

<!-- formula-not-decoded -->

## Working Principle of MAO Approach

The Memetic Algorithm iteratively improves a population of candidate solutions over G generations. Each generation t consists of the following steps:

## Fitness Evaluation

Each individual model mp i in the current population P i is evaluated using a fitness function F , defined as the validation accuracy after a rapid fine-tuning cycle. Let D val be the validation dataset with N val samples. For a given model mp i , let ˆ c j be the predicted class for the j -th validation sample, and C j be the true class. The fitness F ( mp i ) is calculated as:

<!-- formula-not-decoded -->

where I ( · ) is the indicator function that returns 1 if the condition is true and 0 otherwise.

## Selection (Tournament Selection)

To select a parent, a random subset T of size k is chosen from the population J t . The individual in T with the highest fitness is selected as a parent:

<!-- formula-not-decoded -->

This process is repeated to select a second parent.

## Crossover (Recombination)

Two parents Pr 1 and Pr 2 produce an offspring Φ by exchanging architectural components. Let the architectural configuration of a model be represented as a vector hp . The offspring architecture hp Φ is derived as:

<!-- formula-not-decoded -->

where M is a binary mask vector (determined by uniform crossover), and Θ denotes element-wise multiplication.

## Mutation

The offspring's architectural parameters are mutated with probability p m . For each parameter hp Φ [ i ] in hp 0 :

<!-- formula-not-decoded -->

where ϵ is a small random value sampled from a normal distribution H (0 , λ ).

The algorithm terminates after G generations, and the model with the highest fitness in the final population P G is selected as the Global-Net:

<!-- formula-not-decoded -->

which was conclusively identified as DenseNet201 for our framework.

## 3.3 Finetune Architecture: FloraSyntropy-Net framework

The baseline model (Global-Net) for Large-Scale Plant Disease Diagnosis is DenseNet201, a powerful CNN from the DenseNet family [34]. Its core innovation is the Dense Block, where each layer receives the feature maps of all preceding layers as input, connected via concatenation. This promotes feature reuse, strengthens gradient flow, and mitigates the vanishing gradient problem in deep networks. DenseNet201 is composed of an initial convolutional and pooling layer, followed by four sequential dense blocks separated by transition layers (which use 1x1 convolutions for compression and average pooling for downsampling). The final component is a global average pooling layer and a classifier, typically a softmax-activated fully connected layer. Figure 2 presents the architecture diagram of selected (Global-Net) model.

The finetuning process involves integrating a novel block, termed the Deep Block, after the feature-extracting layers of the DenseNet201 (i.e., before the flatten layer).

As depicted in the fig 2 diagram, this block is designed to add depth and non-linear representation power to the extracted feature vector before the final classification. The block begins by taking the input vector and passing it through a Dense Layer. The output of this layer is then processed by a ReLU activation function to introduce non-linearity. A key feature of this block is the use of a Concatenate operation, which merges the original input vector with the newly transformed ReLU-activated output. This creates a wider feature vector that preserves original information while incorporating new, higher-level features.

This concatenated output is then fed into a Repeat Vector layer. This layer is crucial as it transforms the 1D feature vector into a 2D sequence by repeating it a fixed number of times, effectively creating a temporal and sequential structure out of the static features. This reshaped data can then be fed into subsequent layers, such as additional 1D layers, for further processing. Finally, the entire Deep Block structure is wrapped in a recursive loop, indicated by the Repeat Vector acting as a loop boundary, meaning this process of dense transformation, concatenation, and repetition is performed multiple times to progressively build deeper and more complex feature representations tailored for the specific finetuning task.

Fig. 2 Overview of the Global-Net (DenseNet201) Architecture and Novel Deep Block Integration Mechanism

<!-- image -->

## 3.4 Leveraging Federated Collective Knowledge for Client Robustness

Federated knowledge [35] provides a foundational framework for advancing collaborative model training in distributed environments. This paradigm is essential for improving client skills, especially when it comes to multiclass plant disease detection. Models can be trained on a variety of datasets from various customers by utilizing dispersed data sources while maintaining anonymity, which enhances generalization

and performance. By this approach, our FloraSyntropy-Net can gain from the federated sharing of collective knowledge from five sequence clients learning, which will ultimately improve diagnosis accuracy across different global plant classes.

In order to guarantee that each client contribution to the model update is proportionate to the quantity of data clients possess, the weight scaling factor in a Federated Learning (FL) arrangement is crucial. This scaling approach enables the equitable aggregation of model updates from multiple clients, each with varying amounts of training data, in the context of multiclass plant diagnosis. The amount of data points possessed by a particular client LocalNet Count and the overall number of data points across all clients GlobalNet Count are the first steps in calculating the weight scaling factor in this study.

The weight scaling factor, which is determined by the ratio of these two variables, guarantees that clients with more data have a correspondingly greater impact on the global model update. By keeping clients with different quantities of data balanced, this method improves the model's capacity to generalize across various datasets for better disease diagnosis results. The following is a mathematical representation of the weight scaling factor:

<!-- formula-not-decoded -->

Here, C LocalNet is a client's total number of data points, as determined by:

<!-- formula-not-decoded -->

In this case, batch size is the number of data points in each batch, and cardi( T client ) is the total number of batches in the client dataset.

Where, the total amount of data points across all clients C GlobalNet is determined by:

<!-- formula-not-decoded -->

The T client is the dataset for the k -th client and n is the total number of clients (in our case, it's five). Therefore, each client model update is scaled based on the percentage of data they contribute to the global dataset using the weight scaling factor.

## 3.5 Global FloraSyntropy-Net: Client Cloning

For multiclass global plant disease diagnosis, cloning the Global FloraSyntropy-Net model offers a scalable and computationally effective method. This method ensures low computational overhead while preserving the integrity of the global model by using the same FloraSyntropy-Net model both globally and by each individual client. This approach eliminates the need for intricate, resource-intensive architectures by replicating the global model at the client level, allowing each client to conduct local training. The system strikes a balance between scalability, efficiency, and high-performance multiclass classification for plant diagnosis by utilizing a common model at the client and global levels. It is efficient for resource-constrained applications since it uses a robust model for both global and client-level tasks, which guarantees quicker training times,

less memory usage, and less energy consumption. Additionally, this approach reduces the frequency of data transfers between clients and the global model, which lessens the computational load and boosts system effectiveness.

FedAvg: Federated Averaging (FedAvg) equation for the global model is updated after each round of training presents as below:

- Let w t be the global model weights at communication round t .
- Let S t be a subset of clients selected for training in round t , with | S t | = m .
- Let K = 5 be the total number of clients.
- Let n k be the number of data samples on client k .
- Let w ( t +1) k be the updated weights from client k after training on its local data.
- Let n = ∑ m k =1 n k be the total number of samples across the selected clients.

The update of the global model is given by:

<!-- formula-not-decoded -->

This equation ensures that each client's contribution to the model update is proportionate to the quantity of data they possess. The term n k n is precisely that scaling factor.

## 3.6 FloraSyntropy-Net Sync: A Client Training Guide

A crucial step in FL is client training and global synchronization, especially for global applications like multiclass plant disease detection. Individual clients (such as agriculture planting and research institutes) use their own datasets, which may vary (Local &amp; Global geographical location) in terms of data and plant disease kinds, to train local models in this framework. The learn parameters are then aggregated while preserving data privacy by regularly synchronizing these local models with a global model. There are multiple steps in the process:

## Individual Training (Clients):

Every trainer (client) uses its own data to train a local model. This model is FloraSyntropy-Net to balance efficiency and performance in the context of plant disease diagnosis. Only model update gradients are transmitted during client-side training, guaranteeing the privacy of sensitive local client (agriculture planting and research institutes) data. Moreover, every trainer (client) Tr i uses its local dataset PlantDB i to train a FloraSyntropy-Net FSyn i . Here, the training goal is to minimize a loss function ρ (FSyn i ; PlantDB i ), and the model is a FloraSyntropy-Net. Following training on client trainer (client) Tr i 's data, the local model parameters ˆ FSyn i are updated as follows:

<!-- formula-not-decoded -->

Where:

- Fyn i is the client model parameters for trainer (client) Tr i .

- η is the rate of learning.
- ∇ ρ (Fyn i ; PlantDB i ) is the gradient of the loss function with respect to the model parameters Fyn i using data from PlantDB i .

## Global-Net Synchronization:

All trainers (clients) Tr i send their model modifications to a central server following local training. The server merges these updates in a process known as global aggregation, typically by averaging (FedAvg) the model parameters. This improves the global model FSyn new i capacity to generalize across many data sources by enabling it to learn from the combined knowledge of all trainers (clients) Tr i . The weighted average of the local models FSyn local from each trainer (client) Tr i is used to update the global model parameters FSyn global following local training. The representation of the global model is:

<!-- formula-not-decoded -->

Where:

- G is the total number of trainers (clients) Tr i . In our case, it is five trainers (clients) Tr 5 .
- FSyn new i are each trainer (client) updated settings.
- gradient i = | Data x | ∑ 5 x =1 | Data x | is the weight allocated to trainer (client) Tr 5 , which is proportional to the number of data points | Data x | the trainer (client) Tr 5 has.
- FSyn new global is the post-aggregation global model parameters.

While preserving anonymity, our averaging procedure guarantees that the global model benefits from the combined knowledge of all the clients.

## Scalable Learning

The procedure needs to be effective for the model to scale across several trainers (clients) Tr i with global plants having different volumes of data. The weight scaling factor equation is as follows:

<!-- formula-not-decoded -->

Where:

- The number of data points in the trainer (client) Tr i dataset is represented by | Data x | .
- ∑ 5 i =1 | Data x | is the sum of the data points for every client.

Trainers (clients) Tr i with more data are guaranteed to contribute more to the global model thanks to this weight scaling.

## 3.7 Overview of proposed FloraSyntropy-Net framework

The FloraSyntropy-Net framework represents a comprehensive FL architecture specifically designed to address the challenges of large-scale plant disease diagnosis across heterogeneous, globally-sourced data. The framework begins with a rigorously curated FloraSyntropy Archive, a novel dataset aggregating and standardizing images from 13 public repositories to ensure diversity and representativeness. A critical preprocessing phase resizes all images to 224 × 224 pixels to maintain dimensional consistency, while advanced augmentation techniques including geometric transformations (balance dataset) are applied to enhance data variety and mitigate class imbalance. This foundational step ensures robust feature extraction and minimizes bias, enabling the model to generalize effectively across varied agricultural contexts. Architecturally, FloraSyntropy-Net incorporates a hybrid optimization approach to maximize performance and adaptability. A MAO is employed for automated base model selection, combining global genetic search with local refinement to identify DenseNet201 as the optimal backbone (Global-Net) for the framework. This base architecture is enhanced with a novel Deep Block, a novel module inserted before the classification layer to augment feature representation. The Deep Block employs dense layers, concatenation operations, and recursive feature restructuring to capture richer spatial hierarchies and nuanced discriminative patterns, significantly improving the model ability to differentiate between visually similar disease phenotypes. For decentralized and privacy-aware training, FloraSyntropy-Net implements a FL structure supported by a weighted aggregation strategy. The Global-Net model is cloned across five multiple clients, each training locally on private data. Model updates are aggregated using a modified Federated Averaging (FedAvg) protocol, where contributions are weighted by client dataset size:

<!-- formula-not-decoded -->

to ensure equitable influence and robustness against data heterogeneity. This design not only facilitates collaborative learning without data sharing but also enhances the framework scalability and applicability to real-world agricultural networks, where data privacy and computational efficiency are paramount. Fig 3 presents the Overview of the proposed FloraSyntropy-Net framework.

## 3.8 Training FloraSyntropy-Net framework procedure

To guarantee effectiveness and consistency, we used a meticulous chosen set of hyperparameters when training the FloraSyntropy-Net. In particular, the model was trained across 30 epochs to allow for adequate learning while avoiding overfitting, and a learning rate of 0.001 was selected to maximize convergence. In order to balance model accuracy and computational performance, a batch size of 32 was chosen. Compared to other optimization methods, the Adam optimizer offered quick convergence and better generalization, which was crucial in obtaining improved performance. It was quite successful because it could adjust the learning rate for each parameter separately, which resulted in more steady training and a lower chance of overshooting. Furthermore, the

Novel FloraSyntropyPlantDatasetArchive

Fig. 3 Overview of the proposed FloraSyntropy-Net framework

<!-- image -->

categorical cross-entropy loss function was utilized, which was crucial for the classification of plant diseases on a broad scale. This loss function effectively guided the optimization process and ensured a proper evaluation of the model accuracy. Overall, the FloraSyntropy-Net performance significantly improved as a result of the combination of these well-chosen hyperparameters and methodologies, demonstrating the effectiveness and resilience of the suggested architecture.

In this study, a structured approach to dataset partitioning was employed to ensure robust model evaluation and prevent overfitting. The available data was initially split into a dedicated hold-out test set comprising 20% of the entire dataset. This test set was completely sequestered and used only for the final, unbiased evaluation of the model's performance on unseen data after all training and tuning was complete. The remaining 80% of the data was designated as the training pool. From this pool, a validation set was then carved out, constituting 10% of the original total dataset (which equates to 70% of the training pool). This validation set is crucial for tuning hyperparameters, making architectural decisions like the Deep Block, and providing

ongoing performance metrics during the training process without leaking information from the test set. This proposed ratio of 70:10:20 (Train: Validation: Test) is highly efficient as it allocates a substantial majority of the data for training the complex model, while still reserving a statistically significant portion for reliable final testing. The explicit separation of the validation set from the training data ensures that the model's generalization is monitored on data it hasn't been directly optimized on, leading to a more accurate and trustworthy assessment of its real-world capability. Fig 4 illustrate the dataset distribution.

Fig. 4 Ensuring Generalizability: A 70:10:20 Dataset Split for the Novel FloraSyntropy Archive

<!-- image -->

## 3.9 Evaluating FloraSyntropy-Net framework procedure

To evaluate the performance of the FloraSyntropy-Net framework, we carried out a thorough analysis using evaluation criteria frequently applied in evaluation assignments. The outcomes supported the validity of our strategy and were in line with findings from earlier research [36, 37]. Four categories TP (True Positive), TN (True Negative), FP (False Positive), and FN (False Negative) were assigned to each plant diagnosis sample. In order to determine performance metrics like accuracy (EQU-18), precision (EQU -19), recall (EQU -20), and F1-score (EQU-21), which offer a numerical understanding of the model effectiveness in differentiating between correct and incorrect diagnoses, the performance evaluation was carried out using these classifications and the corresponding mathematical formulations.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 4 Result and discussion

This section details the methodology and experimental validation of the FloraSyntropy-Net model. We begin by describing the Novel FloraSyntropy Archive: Dataset Preparation and the Running Setup and Hyperparameters. Adherence to the TRIPOD Checklist ensures standardized reporting. The model's performance is then rigorously evaluated through a Large-Scale Plant Disease Classification benchmark and compared against existing CNN and SOTA models. Further analysis includes an Agricultural Application: Interpretable Analysis, a Domain Adaptation Test, and a critical Ablation study to deconstruct the model's architecture.

## 4.1 Novel FloraSyntropy Archive: Dataset Preparation

To guarantee robust performance, preprocessing of the globally gathered plant image is necessary prior to training the FloraSyntropy Framework. In order to improve the accuracy of diverse plant disease identification, this stage combines the various plant images from 13 publicly available agriculture dataset repositories. This enables the model to focus diverse plants on the regions that are irrelevant. All images are standardized to a uniform input size of 224 × 224 pixels in order to prevent bias and distortion brought on by differences in image dimensions. By ensuring uniform feature extraction across the 13 datasets, this standardization enhances FloraSyntropy generalization capabilities. Furthermore, pretreatment contributes to more consistent and dependable FloraSyntropy performance by reducing frequent problems with plant image, such as noise in image intensity.

To increase the diversity of our novel FloraSyntropy archive, we used three different augmentation techniques in this study. The distribution of plant image following dataset balancing, which guarantees fair representation across all categories, is shown in Table 1. An illustration of the augmentation procedures is also provided by Fig 5, which shows the visual comparison between the original and augmented images. This method supports the model capacity to generalize successfully across many categories in addition to exposing it to a wider range of inputs. We reduced the possibility of skewed drawings that could result from class imbalance by maintaining equal class proportions during training, providing a more trustworthy indicator of the model capacity for generalization.

## 4.2 Running Setup

The FloraSyntropy-Net framework was developed and trained using the Python programming. The Global-Net model architecture was built using the adaptable PyCharm framework, and Python offered a productive environment for the implementation and performance of many tasks. All tests were carried out in the Python environment to optimize speed and computational efficiency [38], taking advantage of a GPU capabilities to speed up the training and testing procedures. In particular, an NVIDIA

Fig. 5 An overview of the preprocessed and augmented plant images: Novel FloraSyntropy Archive

<!-- image -->

RTX5040 Tesla GPU and 32 GB of RAM were used, guaranteeing enough hardware resources for the demanding tasks at hand. This configuration was essential for effectively managing the extensive data processing needed for the assessment of the model performance.

## 4.3 TRIPOD Checklist: Ensuring Standardized Reporting in Plant Disease Diagnosis

Verifying our comprehension of disease pathways requires accurate and open reporting of research. When diagnosing agricultural diseases, it is essential to follow established protocols, such as the TRIPOD checklist. Table 2,3 presents the TRIPOD checklist [39] encourages consistency, dependability, and reproducibility in research findings by offering an organized framework for reporting prediction models. In the detection of plant diseases, adherence to reporting guidelines is important. Our study can guarantee that results are reliable and applicable to agricultural practice by increasing the transparency of model construction, validation, and interpretation. This section examines how the TRIPOD checklist is essential for improving decision-making, guaranteeing high-quality reporting, and boosting the dependability of diagnostic models.

## 4.4 Large-Scale Plant Disease Classification Evaluation of Proposed model

The integration of the Novel Deep Block into the FloraSyntropy-Net architecture yielded a clear and significant improvement in overall performance (Table 4,5 (WO Novel Deep Block), and 6,7 (With Novel Deep Block)), as evidenced by the increase in overall accuracy from 94.74% to 96.38%. This 1.64% gain demonstrates that the block efficiently enhanced the model feature extraction capabilities, leading to more

Table 1 Distribution of the training and validation sets of large-scale plant images after dataset balancing

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris-Diseased, Train: 4712, Validation: 524, Class: Olive-AculusOlearius, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris-Healthy, Train: 4710, Validation: 521, Class: Olive-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-BlackRot, Train: 4712, Validation: 524, Class: Olive-PeacockSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-CedarRust, Train: 4712, Validation: 524, Class: Orange-Haunglongbing, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Healthy, Train: 4712, Validation: 524, Class: Peach-BacterialSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Scab, Train: 4709, Validation: 520, Class: Peach-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Diseased, Train: 4712, Validation: 524, Class: Pepper-BacterialSpot, Train: 4707, Validation: 519.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Healthy, Train: 4712, Validation: 524, Class: Pepper-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Bael-Diseased, Train: 4712, Validation: 524, Class: Pomegranate-Diseased, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-Cordana, Train: 4712, Validation: 524, Class: Pomegranate-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-Healthy, Train: 4712, Validation: 524, Class: PongamiaPinnata-Diseased, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-Pestalotiopsis, Train: 4712, Validation: 524, Class: PongamiaPinnata-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-Sigatoka, Train: 4712, Validation: 524, Class: Potato-EarlyBlight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Basil-Healthy, Train: 4712, Validation: 524, Class: Potato-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Diseased, Train: 4712, Validation: 524, Class: Potato-LateBlight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Healthy, Train: 4712, Validation: 524, Class: Raspberry-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Blueberry-healthy, Train: 4712, Validation: 524, Class: Rice-Blast, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Bacterial Blight, Train: 4712, Validation: 524, Class: Rice-BrownSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Brown Streak Disease, Train: 4712, Validation: 524, Class: Rice-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Green Mottle, Train: 4712, Validation: 524, Class: Rice-Hispa, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Healthy, Train: 4712, Validation: 524, Class: Soybean-Caterpillar, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Mosaic Disease, Train: 4712, Validation: 524, Class: Soybean-DiabroticaSpeciosa, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cherry-Healthy, Train: 4712, Validation: 524, Class: Soybean-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cherry-PowderyMildew, Train: 4712, Validation: 524, Class: Squash-PowderyMildew, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar-Diseased, Train: 4712, Validation: 524, Class: Strawberry-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar-Healthy, Train: 4712, Validation: 524, Class: Strawberry-Scorch, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Coffe-Leaf, Train: 4712, Validation: 524, Class: Sugarcane-Diseased, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-Cercospora, Train: 4712, Validation: 524, Class: Sugarcane-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-CommonRust, Train: 4712, Validation: 524, Class: Tea-Algal, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-Healthy, Train: 4712, Validation: 524, Class: Tea-Anthracnose, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-NorthernBlight, Train: 4712, Validation: 524, Class: Tea-BirdEye, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-BacterialBlight, Train: 4712, Validation: 524, Class: Tea-BrownBlight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-CurlVirus, Train: 4712, Validation: 524, Class: Tea-GrayLight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-FussariumWilt, Train: 4712, Validation: 524, Class: Tea-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-Healthy, Train: 4712, Validation: 524, Class: Tea-RedSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Gauva-Diseased, Train: 4712, Validation: 524, Class: Tea-WhiteSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Gauva-Healthy, Train: 4712, Validation: 524, Class: Tomato-BacterialSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-BlackRot, Train: 4712, Validation: 524, Class: Tomato-EarlyBlight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-blight, Train: 4712, Validation: 524, Class: Tomato-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Esca, Train: 4712, Validation: 524, Class: Tomato-LateBlight, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Healthy, Train: 4712, Validation: 524, Class: Tomato-Mold, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jamun-Diseased, Train: 4712, Validation: 524, Class: Tomato-MosaicVirus, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jamun-Healthy, Train: 4712, Validation: 524, Class: Tomato-SeptoriaSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jatropha-Diseased, Train: 4712, Validation: 524, Class: Tomato-SpiderMites, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jatropha-Healthy, Train: 4712, Validation: 524, Class: Tomato-TargetSpot, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Lemon-Diseased, Train: 4712, Validation: 524, Class: Tomato-YellowCurlVirus, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Lemon-Healthy, Train: 4712, Validation: 524, Class: YellowVein-Diseased, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango-Diseased, Train: 4712, Validation: 524, Class: YellowVein-Healthy, Train: 4712, Validation: 524.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango-Healthy, Train: 4712, Validation: 524.
Table 2 TRIPOD Checklist for FloraSyntropy-Net Framework (Part 1)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Title, Description: Identify the study as develop- ing and/or validating a gen- eralize prediction model, the target population, and the out- come to be predicted., Our Mapping: FloraSyntropy-Net: Scalable Deep Learning for Novel Plant Disease Classification identi- fies the model and its purpose., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Abstract, Description: Provide a summary of objec- tives, study design, results, and conclusions., Our Mapping: Paper abstract summarizes the framework objectives, method- ology (federated learning, opti- mization, finetuning), and key results., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Introduction.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 3a. Background, Description: Explain the plant disease con- text and rationale for develop- ing or validating the prediction model., Our Mapping: The Introduction explains the context of large-scale plant dis- ease diagnosis and the limita- tions of existing methods., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 3b. Objectives, Description: Specify the objectives, including whether the study describes the development or validation of the model, or both., Our Mapping: Section 1.1. Study contribution explicitly states the objectives and novel contributions of the FloraSyntropy-Net framework., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Related Work, Description: Review of current models, approaches, and pertinent studies, along with an analysis of their shortcomings., Our Mapping: Highlight the distinctive con- tributions of the work by contrasting FloraSyntropy-Net with earlier federated learning models and their use in plant disease detection., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Methods.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 4. Source of data, Description: Describe the study design or source of data., Our Mapping: Section 3.1. Novel Dataset FloraSyntropy Archive and 4.1. Dataset Preprocessing describe the source, nature, and handling of the data., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 5a. Participants, Description: Specify key elements of the study setting and the inclu- sion/exclusion criteria., Our Mapping: Section 3.1. implies the dataset contains specific plant disease imagery. The criteria would be detailed in the dataset descrip- tion., Checklist: Fair*.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 6a. Outcome, Description: Clearly define the outcome that is predicted., Our Mapping: The outcome is plant dis- ease classification, defined in Section 3.1. and 4.4. Large- Scale Plant Disease Classifica- tion Experiment., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 7a. Predictors, Description: Clearly define all predictors used in developing the final model., Our Mapping: Predictors are the image data from the FloraSyntropy Archive. The feature extrac- tion process is defined in Section 3.2./3.3. (Global-Net selection & finetuning)., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 8. Sample size, Description: Explain how the study size was arrived at., Our Mapping: The dataset size and the 70:10:20 split (Section 3.1./4.1) justify the sample size used for training and eval- uation., Checklist: Pass.
Table 3 TRIPOD Checklist for FloraSyntropy-Net Framework (Part 2)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 10. Model develop- ment, Description: Specify the statistical methods used for model development., Our Mapping: Sections 3.2. (Memetic Algo- rithm), 3.3. (Finetune Archi- tecture), and 3.4./3.5. /3.6. (Federated Learning) detail the machine learning methods for model development., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 16. Model perfor- mance, Description: Report performance measures for the prediction model., Our Mapping: Sections 4.4., 4.5., 4.6., and 4.7.4. are dedicated to report- ing results like accuracy, preci- sion, recall, F1-score, and sta- tistical analysis., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: Results.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 17. Participants, Description: Describe the flow of partici- pants and any deviations from the study plan., Our Mapping: Section 4.1. describes the dataset distribution and preprocessing, effectively describing the flow of data samples., Checklist: Fair*.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 19. Interpretation, Description: Give an overall interpretation of the results., Our Mapping: Sections 4. (Result and discus- sion) and 5. Discussion provide interpretation of the results in the context of existing work and the study objectives., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 20. Implications, Description: Discuss the potential implica- tions of the results., Our Mapping: Section 6. Conclusion and future direction discuss the implications and future work, suggesting the model's value and next steps., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 21. Discussion, Description: Discuss any limitations of the study., Our Mapping: Section 5. Discussion with limi- tation is explicitly dedicated to this purpose., Checklist: Pass.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 22. Data and Code Availability, Description: To ensure transparency and repeatability, make the data and code used in the investiga- tion available., Our Mapping: For reproducibility, make sure that the code is publicly avail- able., Checklist: Fair*.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), TRIPOD Section: 23. Reporting Com- pliance, Description: Adherence to reporting regula- tions, such as TRIPOD., Our Mapping: Our study complies with TRI- POD requirements by using the checklist for transparent reporting., Checklist: Pass.
precise classification across the extensive dataset. A closer look at the per-class metrics reveals that this improvement was not uniform but targeted. Numerous challenging classes, particularly those with previously poor performance, saw substantial gains in F1-scores. For instance, the Arjun-Diseased class improved from 0.8261 to 0.9070, Bael-Diseased from 0.8627 to 0.9200, and Potato-LateBlight from 0.8544 to 0.9879. This pattern suggests the Novel Deep Block specifically improved the model ability to discern complex and subtle features that were previously difficult to classify, effectively addressing specific weaknesses in the base model.

However, the upgrade was not universally beneficial for every single class. A comparative analysis shows slight regressions in a minority of cases, such as Rice-Blast (F1 dropping from 0.9285 to 9169) and Rice-Hispa (from 0.9280 to 0.8770). This indicates that while the new block optimizes the network for the vast majority of features, it may cause minor over-specialization or a shift in decision boundaries that slightly disadvantages a few specific classes. Despite these isolated regressions, the FloraSyntropy-Net effect is positive by implementing a FL approach with five client clones of our finelytuned FloraSyntropy-Net model, which significantly enhance both the robustness and generalization capability of our model. This decentralized approach allows each client to learn specialized features from its unique subset of the data, while periodic aggregation of model weights on a central server synthesizes these diverse learnings into a single, robust global model. This process not only mitigates the risk of overfitting to specific data characteristics that may have caused minor regressions in individual classes during centralized training but also leverages collective learning from varied data distributions.

Performance comparison of FloraSyntropy-Net against baseline models.

Based on the comparative ROC and Precision-Recall curve analysis (Fig 6) conducted on the large-scale novel FloraSyntropy Archive, the FloraSyntropy-Net framework incorporating the novel deep block demonstrates a measurable performance enhancement, achieving a perfect AUC of 1.000 compared to 0.999 without the block, and an efficient Average Precision of 1.000 versus 0.999. This measurable improvement signifies a superior ability to maintain high true positive rates while minimizing false positives across 97 disease classes. The 0.001 gain in both metrics, though numerically small, reflects the elimination of the final marginal errors and confirms the model strengthened capacity for precise feature discrimination, leading to a marked reduction in inter-class confusion. The results validate that the architectural innovation introduced by the deep block is critically effective in enhancing classification robustness and reliability on complex, real-world plant disease imagery.

<!-- image -->

a

b

Fig. 6 A comparison of performance for the FloraSyntropy-Net model (a) ROC Curve (b) PrecisionRecall Curve, demonstrating a significant reduction in misclassifications and an increase in diagonal accuracy with novel deep block.

Table 4 Per Class Performance Comparison - FloraSyntropy-Net (Our) WO Novel Deep Block (Part 1)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris- Diseased, Precision: 0.8679, Recall: 0.902, F1-Score: 0.8846, Class: Olive- AculusOlearius, Precision: 0.8652, Recall: 0.6854, F1-Score: 0.7649, Overall: 94.74.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris- Healthy, Precision: 0.8571, Recall: 0.8333, F1-Score: 0.8451, Class: Olive-Healthy, Precision: 0.5054, Recall: 0.9895, F1-Score: 0.669.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-, Precision: 1, Recall: 0.9914, F1-Score: 0.9957, Class: Olive-, Precision: 0.9742, Recall: 0.5171, F1-Score: 0.6756.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: BlackRot Apple- CedarRust, Precision: 0.9974, Recall: 0.9873, F1-Score: 0.9924, Class: PeacockSpot Orange- Haunglongbing, Precision: 0.9985, Recall: 0.9992, F1-Score: 0.9989.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Healthy, Precision: 0.9896, Recall: 0.9955, F1-Score: 0.9926, Class: Peach- BacterialSpot, Precision: 1, Recall: 0.995, F1-Score: 0.9975.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Scab, Precision: 0.9865, Recall: 0.9981, F1-Score: 0.9923, Class: Peach-Healthy, Precision: 0.9854, Recall: 0.9951, F1-Score: 0.9902.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Diseased, Precision: 0.8261, Recall: 0.8261, F1-Score: 0.8261, Class: Pepper- BacterialSpot, Precision: 1, Recall: 0.9751, F1-Score: 0.9874.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Healthy, Precision: 0.6029, Recall: 0.9318, F1-Score: 0.7321, Class: Pepper- Healthy, Precision: 0.9854, Recall: 0.9951, F1-Score: 0.9902.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Bael-Diseased, Precision: 0.8148, Recall: 0.9167, F1-Score: 0.8627, Class: Pomegranate- Diseased, Precision: 1, Recall: 0.9751, F1-Score: 0.9874.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-, Precision: 0.931, Recall: 0.8438, F1-Score: 0.8852, Class: Pomegranate- Healthy, Precision: 0.9854, Recall: 0.9951, F1-Score: 0.9902.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cordana Banana- Healthy, Precision: 0.7879, Recall: 1, F1-Score: 0.8814, Class: PongamiaPinnata- Diseased, Precision: 1, Recall: 0.9751, F1-Score: 0.9874.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana- Pestalotiopsis, Precision: 0.6531, Recall: 0.9143, F1-Score: 0.7619, Class: PongamiaPinnata- Healthy, Precision: 0.994, Recall: 0.9812, F1-Score: 0.9876.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana- Sigatoka, Precision: 0.8482, Recall: 1, F1-Score: 0.9179, Class: Potato- EarlyBlight, Precision: 0.8548, Recall: 0.9815, F1-Score: 0.9138.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Basil-Healthy, Precision: 1, Recall: 1, F1-Score: 1, Class: Potato- Healthy, Precision: 0.9138, Recall: 0.9298, F1-Score: 0.9217.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Diseased, Precision: 0.9474, Recall: 0.8571, F1-Score: 0.9, Class: Potato- LateBlight, Precision: 0.9167, Recall: 0.8, F1-Score: 0.8544.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Healthy, Precision: 0.7368, Recall: 0.9333, F1-Score: 0.8235, Class: Raspberry- Healthy, Precision: 0.9091, Recall: 0.9375, F1-Score: 0.9231.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Blueberry- healthy, Precision: 0.9913, Recall: 0.98, F1-Score: 0.9856, Class: Rice-Blast, Precision: 0.9903, Recall: 0.9868, F1-Score: 0.9285.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Bacterial Blight, Precision: 0.5781, Recall: 0.3978, F1-Score: 0.4713, Class: Rice- BrownSpot, Precision: 0.9839, Recall: 1, F1-Score: 0.9919.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Brown Streak Disease, Precision: 0.6827, Recall: 0.6339, F1-Score: 0.6574, Class: Rice-Healthy, Precision: 0.9841, Recall: 0.9794, F1-Score: 0.9818.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Green Mottle, Precision: 0.7229, Recall: 0.6383, F1-Score: 0.678, Class: Rice-Hispa, Precision: 0.9959, Recall: 0.9836, F1-Score: 0.928.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Healthy, Precision: 0.5593, Recall: 0.7333, F1-Score: 0.6346, Class: Soybean- Caterpillar, Precision: 0.6875, Recall: 0.3929, F1-Score: 0.5.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Mosaic Disease, Precision: 0.6875, Recall: 0.7765, F1-Score: 0.7293, Class: Soybean- DiabroticaSpeciosa, Precision: 0.7778, Recall: 0.28, F1-Score: 0.4118.
## 4.5 Performance comparison of FloraSyntropy-Net with existing CNN models

Our proposed FloraSyntropy-Net demonstrates a significant and substantial superiority over a suite of SOTA DL models across all key metrics. Established architectures

Table 5 Per Class Performance Comparison - FloraSyntropy-Net (Our) WO Novel Deep Block (Part 2)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cherry-, Precision: 0.9973, Recall: 0.9739, F1-Score: 0.9855, Class: Soybean- Healthy, Precision: 0.5726, Recall: 0.9579, F1-Score: 0.7168.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Healthy Cherry- PowderyMildew, Precision: 0.9972, Recall: 1, F1-Score: 0.9986, Class: Squash- PowderyMildew, Precision: 0.2400, Recall: 0.1463, F1-Score: 0.1818.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar- Diseased, Precision: 0.95, Recall: 0.7917, F1-Score: 0.8636, Class: Strawberry- Healthy, Precision: 0.8149, Recall: 0.4456, F1-Score: 0.5762.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar- Healthy, Precision: 1, Recall: 0.9524, F1-Score: 0.9756, Class: Strawberry- Scorch, Precision: 0.6304, Recall: 0.8549, F1-Score: 0.7257.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Coffe-Leaf, Precision: 0.9872, Recall: 0.9904, F1-Score: 0.9888, Class: Sugarcane- Diseased, Precision: 0.8473, Recall: 0.9920, F1-Score: 0.9139.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-, Precision: 0.8654, Recall: 1, F1-Score: 0.9278, Class: Sugarcane- Healthy, Precision: 1.0000, Recall: 0.9987, F1-Score: 0.9994.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cercospora Corn-, Precision: 0.9975, Recall: 0.9817, F1-Score: 0.9895, Class: Tea-Algal, Precision: 0.9987, Recall: 0.9987, F1-Score: 0.9987.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: CommonRust Corn-Healthy, Precision: 0.9773, Recall: 1, F1-Score: 0.9885, Class: Tea- Anthracnose, Precision: 0.9986, Recall: 1.0000, F1-Score: 0.9993.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-, Precision: 0.988, Recall: 0.8906, F1-Score: 0.9368, Class: Tea-BirdEye, Precision: 0.9875, Recall: 0.9080, F1-Score: 0.9461.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: NorthernBlight Cotton-, Precision: 0.973, Recall: 0.8, F1-Score: 0.878, Class: Tea- BrownBlight, Precision: 0.9286, Recall: 0.5652, F1-Score: 0.7027.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: BacterialBlight Cotton- CurlVirus, Precision: 0.9861, Recall: 0.8452, F1-Score: 0.9103, Class: Tea-GrayLight, Precision: 0.7778, Recall: 0.3500, F1-Score: 0.4828.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton- FussariumWilt, Precision: 0.7835, Recall: 0.9048, F1-Score: 0.8398, Class: Tea-Healthy, Precision: 0.5000, Recall: 0.8000, F1-Score: 0.6154.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-, Precision: 0.9615, Recall: 0.2941, F1-Score: 0.4505, Class: Tea-RedSpot, Precision: 0.8182, Recall: 0.3913, F1-Score: 0.5294.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Healthy Gauva- Diseased, Precision: 1, Recall: 0.4643, F1-Score: 0.6341, Class: Tea-WhiteSpot, Precision: 0.6667, Recall: 0.6000, F1-Score: 0.6316.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Gauva-Healthy, Precision: 0.9487, Recall: 0.6727, F1-Score: 0.7872, Class: Tomato- BacterialSpot, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape- BlackRot, Precision: 0.9925, Recall: 0.9863, F1-Score: 0.9894, Class: Tomato- EarlyBlight, Precision: 0.8235, Recall: 0.9655, F1-Score: 0.8889.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-blight, Precision: 0.9975, Recall: 0.9926, F1-Score: 0.995, Class: Tomato- Healthy, Precision: 0.5400, Recall: 0.9659, F1-Score: 0.9794.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Esca, Precision: 0.9943, Recall: 0.9943, F1-Score: 0.9943, Class: Tomato- LateBlight, Precision: 0.9689, Recall: 0.9177, F1-Score: 0.9426.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Healthy, Precision: 1, Recall: 1, F1-Score: 1, Class: Tomato-Mold, Precision: 0.9988, Recall: 0.9659, F1-Score: 0.9794.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jamun-, Precision: 0.8571, Recall: 0.7826, F1-Score: 0.8182, Class: Tomato-, Precision: 0.9689, Recall: 0.9177, F1-Score: 0.9426.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Diseased Jamun-, Precision: 0.8594, Recall: 0.9821, F1-Score: 0.9167, Class: MosaicVirus Tomato- SeptoriaSpot, Precision: 0.9988, Recall: 0.9952, F1-Score: 0.9970.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Healthy Jatropha-, Precision: 0.9167, Recall: 0.88, F1-Score: 0.898, Class: Tomato- SpiderMites, Precision: 0.9410, Recall: 0.9779, F1-Score: 0.9591.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Diseased Jatropha-, Precision: 0.8929, Recall: 0.9259, F1-Score: 0.9091, Class: Tomato- TargetSpot, Precision: 0.9340, Recall: 0.9925, F1-Score: 0.9624.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Healthy Lemon- Diseased, Precision: 0.7, Recall: 0.4667, F1-Score: 0.56, Class: Tomato- YellowCurlVirus, Precision: 0.8215, Recall: 0.9079, F1-Score: 0.8625.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Lemon- Healthy, Precision: 0.7619, Recall: 1, F1-Score: 0.8649, Class: YellowVein- Diseased, Precision: 0.1404, Recall: 0.0281, F1-Score: 0.0468.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango- Diseased, Precision: 0.9792, Recall: 0.8868, F1-Score: 0.9307, Class: YellowVein- Healthy, Precision: 0.9880, Recall: 0.9973, F1-Score: 0.9927.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango- Healthy, Precision: 0.8684, Recall: 0.9706, F1-Score: 0.9167.
Table 6 Per Class Performance Comparison - FloraSyntropy-Net (Our) With Novel Deep Block (Part 1)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris- Diseased, Precision: 0.8727, Recall: 0.9412, F1-Score: 0.9057, Class: Olive- AculusOlearius, Precision: 0.8365, Recall: 0.7472, F1-Score: 0.7893, Overall: 96.38.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: AlstoniaScholaris- Healthy, Precision: 0.9032, Recall: 0.7778, F1-Score: 0.8358, Class: Olive-Healthy, Precision: 0.5207, Recall: 0.9947, F1-Score: 0.6835.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple- BlackRot, Precision: 1, Recall: 0.9951, F1-Score: 0.9975, Class: Olive- PeacockSpot, Precision: 0.9735, Recall: 0.5034, F1-Score: 0.6637.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple- CedarRust, Precision: 0.9987, Recall: 0.9861, F1-Score: 0.9923, Class: Orange- Haunglongbing, Precision: 1, Recall: 0.9992, F1-Score: 0.9996.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Healthy, Precision: 0.9925, Recall: 0.9925, F1-Score: 0.9925, Class: Peach- BacterialSpot, Precision: 1, Recall: 1, F1-Score: 1.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Apple-Scab, Precision: 0.9942, Recall: 0.9981, F1-Score: 0.9961, Class: Peach-Healthy, Precision: 0.9919, Recall: 0.9951, F1-Score: 0.9935.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Diseased, Precision: 0.975, Recall: 0.8478, F1-Score: 0.907, Class: Pepper- BacterialSpot, Precision: 1, Recall: 0.9876, F1-Score: 0.9937.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Arjun-Healthy, Precision: 0.7451, Recall: 0.8636, F1-Score: 0.8, Class: Pepper- Healthy, Precision: 0.9964, Recall: 0.9753, F1-Score: 0.9857.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Bael-Diseased, Precision: 0.8846, Recall: 0.9583, F1-Score: 0.92, Class: Pomegranate- Diseased, Precision: 0.9464, Recall: 0.9815, F1-Score: 0.9636.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana- Cordana, Precision: 0.9143, Recall: 1, F1-Score: 0.9552, Class: Pomegranate- Healthy, Precision: 0.9032, Recall: 0.9825, F1-Score: 0.9412.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana- Healthy, Precision: 0.963, Recall: 1, F1-Score: 0.9811, Class: PongamiaPinnata- Diseased, Precision: 0.9107, Recall: 0.9273, F1-Score: 0.9189.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Banana-, Precision: 0.8095, Recall: 0.9714, F1-Score: 0.8831, Class: PongamiaPinnata- Healthy, Precision: 0.8986, Recall: 0.9688, F1-Score: 0.9323.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Pestalotiopsis Banana- Sigatoka, Precision: 0.8407, Recall: 1, F1-Score: 0.9135, Class: Potato- EarlyBlight, Precision: 0.9868, Recall: 0.9904, F1-Score: 0.9886.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Basil-Healthy, Precision: 0.9677, Recall: 1, F1-Score: 0.9836, Class: Potato- Healthy, Precision: 0.9761, Recall: 1, F1-Score: 0.9879.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Diseased, Precision: 0.8947, Recall: 0.8095, F1-Score: 0.85, Class: Potato- LateBlight, Precision: 0.9867, Recall: 0.9891, F1-Score: 0.9879.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Betel-Healthy, Precision: 0.8667, Recall: 0.8667, F1-Score: 0.8667, Class: Raspberry- Healthy, Precision: 0.9973, Recall: 1, F1-Score: 0.9986.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Blueberry- healthy, Precision: 0.9899, Recall: 0.9843, F1-Score: 0.9871, Class: Rice-Blast, Precision: 0.897, Recall: 0.8107, F1-Score: 0.9169.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Bacterial Blight, Precision: 0.6119, Recall: 0.4409, F1-Score: 0.5125, Class: Rice- BrownSpot, Precision: 0.9062, Recall: 0.3867, F1-Score: 0.5421.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Brown Streak Disease, Precision: 0.7634, Recall: 0.6339, F1-Score: 0.6927, Class: Rice-Healthy, Precision: 0.6466, Recall: 0.8551, F1-Score: 0.7364.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava-Green Mottle, Precision: 0.6429, Recall: 0.6702, F1-Score: 0.6562, Class: Rice-Hispa, Precision: 0.8303, Recall: 0.839, F1-Score: 0.877.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Healthy, Precision: 0.5676, Recall: 0.7778, F1-Score: 0.6562, Class: Soybean- Caterpillar, Precision: 0.8318, Recall: 0.5529, F1-Score: 0.6642.
like DenseNet201 and ResNet50V2 achieved competitive (Table 8) but lower baseline accuracy (93.73% and 93.48% respectively), with their precision, recall, and F1-scores consistently remaining in the 0.86-0.89 range. This indicates a significant number of misclassifications that balance out in overall accuracy. In unambiguous contrast, FloraSyntropy-Net achieves a significantly higher overall accuracy of 96.38% and delivers a superior balance between precision (0.9525) and recall (0.9409), culminating in an

Table 7 Per Class Performance Comparison - FloraSyntropy-Net (Our) With Novel Deep Block (Part 2)

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cassava- Mosaic Disease, Precision: 0.8056, Recall: 0.6824, F1-Score: 0.7389, Class: Soybean- DiabroticaSpeciosa, Precision: 0.6376, Recall: 0.8617, F1-Score: 0.7329.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cherry- Healthy, Precision: 0.9973, Recall: 0.9739, F1-Score: 0.9855, Class: Soybean- Healthy, Precision: 0.8837, Recall: 0.9940, F1-Score: 0.9356.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cherry- PowderyMildew, Precision: 1, Recall: 1, F1-Score: 1, Class: Squash- PowderyMildew, Precision: 1.0000, Recall: 0.9987, F1-Score: 0.9994.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar- Diseased, Precision: 1, Recall: 0.8333, F1-Score: 0.9091, Class: Strawberry- Healthy, Precision: 0.9987, Recall: 0.9987, F1-Score: 0.9987.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Chinar- Healthy, Precision: 0.9524, Recall: 0.9524, F1-Score: 0.9524, Class: Strawberry- Scorch, Precision: 0.9919, Recall: 1.0000, F1-Score: 0.9960.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Coffe-Leaf, Precision: 0.9841, Recall: 0.9904, F1-Score: 0.9872, Class: Sugarcane- Diseased, Precision: 1.0000, Recall: 0.9195, F1-Score: 0.9581.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-, Precision: 0.9236, Recall: 0.984, F1-Score: 0.9529, Class: Sugarcane- Healthy, Precision: 0.9884, Recall: 1.0000, F1-Score: 0.9942.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cercospora Corn- CommonRust, Precision: 0.9975, Recall: 0.9792, F1-Score: 0.9883, Class: Tea-Algal, Precision: 1.0000, Recall: 0.4783, F1-Score: 0.6471.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn-Healthy, Precision: 0.9974, Recall: 1, F1-Score: 0.9987, Class: Tea- Anthracnose, Precision: 0.7500, Recall: 0.4500, F1-Score: 0.5625.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Corn- NorthernBlight, Precision: 0.9681, Recall: 0.9495, F1-Score: 0.9587, Class: Tea-BirdEye, Precision: 0.4571, Recall: 0.8000, F1-Score: 0.5818.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton-, Precision: 0.9762, Recall: 0.9111, F1-Score: 0.9425, Class: Tea- BrownBlight, Precision: 0.9000, Recall: 0.7826, F1-Score: 0.8372.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: BacterialBlight Cotton- CurlVirus, Precision: 0.9865, Recall: 0.869, F1-Score: 0.9241, Class: Tea-GrayLight, Precision: 0.7692, Recall: 0.5000, F1-Score: 0.6061.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton- FussariumWilt, Precision: 0.828, Recall: 0.9167, F1-Score: 0.8701, Class: Tea-Healthy, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Cotton- Healthy, Precision: 0.96, Recall: 0.2824, F1-Score: 0.4364, Class: Tea-RedSpot, Precision: 0.9032, Recall: 0.9655, F1-Score: 0.9333.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Gauva-, Precision: 0.8696, Recall: 0.7143, F1-Score: 0.7843, Class: Tea-WhiteSpot, Precision: 0.6222, Recall: 1.0000, F1-Score: 0.7671.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Diseased Gauva-Healthy, Precision: 0.9773, Recall: 0.7818, F1-Score: 0.8687, Class: Tomato- BacterialSpot, Precision: 0.9973, Recall: 0.9711, F1-Score: 0.9840.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape- BlackRot, Precision: 0.9962, Recall: 0.985, F1-Score: 0.9906, Class: Tomato- EarlyBlight, Precision: 0.9487, Recall: 0.9533, F1-Score: 0.9510.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-blight, Precision: 0.9988, Recall: 0.9963, F1-Score: 0.9975, Class: Tomato- Healthy, Precision: 0.9952, Recall: 0.9928, F1-Score: 0.9940.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Esca, Precision: 0.9887, Recall: 0.9929, F1-Score: 0.9908, Class: Tomato- LateBlight, Precision: 0.9660, Recall: 0.9767, F1-Score: 0.9713.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grape-Healthy, Precision: 1, Recall: 1, F1-Score: 1, Class: Tomato-Mold, Precision: 0.9555, Recall: 0.9937, F1-Score: 0.9742.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jamun- Diseased, Precision: 0.9474, Recall: 0.7826, F1-Score: 0.8571, Class: Tomato- MosaicVirus, Precision: 0.8188, Recall: 0.8884, F1-Score: 0.8522.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jamun- Healthy, Precision: 0.8615, Recall: 1, F1-Score: 0.9256, Class: Tomato- SeptoriaSpot, Precision: 0.5796, Recall: 0.5316, F1-Score: 0.5452.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jatropha- Diseased, Precision: 0.9167, Recall: 0.88, F1-Score: 0.898, Class: Tomato- SpiderMites, Precision: 0.9920, Recall: 1.0000, F1-Score: 0.9960.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Jatropha-, Precision: 0.8929, Recall: 0.9259, F1-Score: 0.9091, Class: Tomato- TargetSpot, Precision: 0.9831, Recall: 0.9806, F1-Score: 0.9818.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Healthy Lemon- Diseased, Precision: 1, Recall: 0.4, F1-Score: 0.5714, Class: Tomato- YellowCurlVirus, Precision: 0.9908, Recall: 0.9961, F1-Score: 0.9934.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Lemon- Healthy, Precision: 0.7442, Recall: 1, F1-Score: 0.8533, Class: YellowVein- Diseased, Precision: 0.9861, Recall: 0.9953, F1-Score: 0.9907.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango- Diseased, Precision: 0.9444, Recall: 0.9623, F1-Score: 0.9533, Class: YellowVein- Healthy, Precision: 0.9887, Recall: 1.0000, F1-Score: 0.9943.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mango- Healthy, Precision: 0.9189, Recall: 1, F1-Score: 0.9577.
efficient F1-score of 0.9504. This performance gap, particularly in the F1-score which is critical for imbalanced datasets, underscores the efficacy of our novel architectural enhancements and training methodology in achieving more precise and reliable plant disease classification.

Table 8 Performance comparison of FloraSyntropy-Net against baseline models

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: DenseNet121, Precision: 0.8886, Recall: 0.8722, F1-Score: 0.8702, Accuracy: 0.9306.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: DenseNet169, Precision: 0.8958, Recall: 0.8791, F1-Score: 0.8768, Accuracy: 0.9318.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: DenseNet201, Precision: 0.8986, Recall: 0.8864, F1-Score: 0.8838, Accuracy: 0.9373.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: InceptionV3, Precision: 0.8632, Recall: 0.8433, F1-Score: 0.8361, Accuracy: 0.9334.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: MobileNetV1, Precision: 0.889, Recall: 0.8739, F1-Score: 0.8704, Accuracy: 0.9306.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: MobileNetV2, Precision: 0.8881, Recall: 0.8731, F1-Score: 0.8714, Accuracy: 0.9283.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: ResNet50V2, Precision: 0.8904, Recall: 0.8688, F1-Score: 0.87, Accuracy: 0.9348.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: ResNet101V2, Precision: 0.8857, Recall: 0.8673, F1-Score: 0.8681, Accuracy: 0.9248.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: ResNet152V2, Precision: 0.8843, Recall: 0.8618, F1-Score: 0.8638, Accuracy: 0.9255.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: VGG16, Precision: 0.8124, Recall: 0.7917, F1-Score: 0.788, Accuracy: 0.8692.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: VGG19, Precision: 0.7931, Recall: 0.7793, F1-Score: 0.7751, Accuracy: 0.8528.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Model: FloraSyntropy-Net (Our), Precision: 0.9525, Recall: 0.9409, F1-Score: 0.9504, Accuracy: 0.9638.
## 4.6 Performance comparison of FloraSyntropy-Net with existing SOTA models

The comparative analysis of plant disease classification methods, as summarized in the table 9, demonstrates a clear progression in performance and methodological robustness, culminating in the proposed FloraSyntropy-Net framework. While earlier approaches such as SVM-based classifiers (Shrivastava et al.[40], 94.65%; Sharif et al [41], 95.80%) and hybrid autoencoders (Singh et al., 99.35%) achieved high accuracy on smaller, domain-specific datasets like Plant Village or BananaLSD, their evaluations were limited to controlled environments, absent large-scale validation. In contrast, the FloraSyntropy-Net framework, leveraging the novel, globally representative FloraSyntropy Archive, achieves a competitive accuracy of 96.38% while uniquely incorporating rigorous large-scale validation. This ensures not only high performance but also proven generalizability across diverse, real-world agricultural scenarios, addressing a critical gap in prior studies.

## 4.7 Agricultural Application: Interpretable Analysis

To ensure the FloraSyntropy-Net framework is not merely a high-performing black box but a reliable and trustworthy tool for agricultural diagnostics, this section provides an in-depth interpretable analysis. We employ a suite of explainable AI techniques to visually and statistically decipher the model decision-making process. Specifically, GRADCAM visualizations are used to highlight the discriminative image regions that most influenced the model predictions. Together, these methods provide critical insights into the model behavior, validate its focus on biologically relevant features,

Table 9 Comparative analysis of plant disease classification methodologies, highlighting dataset scope, reported accuracy, and the critical presence of large-scale validation

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Harakannanavar et al. [42], Method: ML-Classifier, Dataset Used: Plant Village (Tomato Leaf), Accuracy: 88.00%, Large-Scale: Absent.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Shrivastava et al. [40], Method: SVM-Classifier, Dataset Used: Indira Gandhi, Accuracy: 94.65%, Large-Scale: Absent.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Shah et al. [43], Method: CSVM, Dataset Used: Plant Village, Accuracy: More than 90.00%, Large-Scale: Absent.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Singh et al. [44], Method: HAE, Dataset Used: BananaLSD, Accuracy: 99.35%, Large-Scale: Absent.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Sharif et al. [41], Method: M-SVM, Dataset Used: Cotton Leaf, Accuracy: 95.80%, Large-Scale: Absent.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Reference: Proposed (Our), Method: FloraSyntropy-Net framework, Dataset Used: FloraSyntropy-Net Archive, Accuracy: 96.38%, Large-Scale: Presents.
and ultimately build confidence in its practical deployment for real-world agricultural applications.

## GRADCAM Visualization

The GRADCAM visualizations [35, 39] for FloraSyntropy-Net consistently localize precise disease-specific features, such as lesions and insect damage, within plant imagery. This demonstrates the model ability to focus on diagnostically relevant regions rather than irrelevant background noise. The high-resolution heatmaps align perfectly with expert-agreed areas of infection, validating the model learned representations. This precise visual explainability confirms FloraSyntropy-Net efficacy as an accurate and trustworthy diagnostic tool. Fig 7 presents the GRADCAM visualizations for FloraSyntropy-Net framework.

Fig. 7 Overview of GRADCAM visualizations for FloraSyntropy-Net to highlight the discriminative image regions that most influenced the predictions demonstrating a significant reduction in misclassifications and an increase in diagonal interpretability with novel deep block.

<!-- image -->

## 4.8 Domain Adaptation Test: From Plants to Pests Classification

Conducting a domain adaptation test, where a FloraSyntropy-Net model trained for plant disease classification is evaluated on the distinct task of pest classification, is a critical and rigorous method for validating true model robustness and generalization. This test moves beyond standard evaluation on similar data, intentionally introducing a significant domain shift in features from textural patterns of diseased leaves to the morphological features of insects. Its importance lies in stress-testing the model feature extraction capabilities; a model that performs well under such disparate conditions demonstrates that it has learned fundamental, transferable visual representations rather than merely memorizing dataset-specific artifacts.

In this study, we have used the multiclass Pest [45] dataset, which contains a diverse range of insect categories that pose distinct agricultural threats. This dataset provides an ideal benchmark to evaluate the cross-domain generalization capability of our plant-based model when validate with entirely different visual features and biological contexts. Fig 8 showcases a representative sample of images from the dataset, illustrating the visual diversity and characteristics of the classes, alongside a detailed distribution chart that highlights the composition and balance of the data across categories. The additional dataset test presents that integration of the novel deep

Fig. 8 Representative dataset sample images and class distribution: Additional dataset

<!-- image -->

block into the FloraSyntropy-Net architecture resulted in a substantial performance improvement, as evidenced by the comparative class-wise metrics (Table 10). The most significant impact was observed on the Bollworm class, which saw its F1-score leap from 0.9130 to a perfect 1.0000, indicating the block enhanced ability to capture complex features that were previously challenging. This enhancement also driven the overall accuracy from 0.9778 to an exceptional 0.9984. Furthermore, while the without (deep block) model already performed well on several classes due to collective knowledge, the model (with novel deep block) achieved perfection (1.0000 across precision, recall, and F1) for the majority of classes, including Aphids, Armyworm, and Beetle, demonstrating that the deep block not only improved weaknesses but also boosted the

model consistency and confidence across the entire dataset. Based on the comparative

Table 10 Per class performance comparison of FloraSyntropy-Net Framework O/W Novel Deep block: Pest Dataset

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: FloraSyntropy-Net (Our) WO Novel Deep Block, Precision: FloraSyntropy-Net (Our) WO Novel Deep Block, Recall: FloraSyntropy-Net (Our) WO Novel Deep Block, F1-Score: FloraSyntropy-Net (Our) WO Novel Deep Block, Overall Accuracy: FloraSyntropy-Net (Our) WO Novel Deep Block.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Aphids, Precision: 0.9718, Recall: 0.9857, F1-Score: 0.9787, Overall Accuracy: 0.9778.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Armyworm, Precision: 0.9855, Recall: 0.9714, F1-Score: 0.9784.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Beetle, Precision: 0.9859, Recall: 1.0000, F1-Score: 0.9929.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Bollworm, Precision: 0.9265, Recall: 0.9000, F1-Score: 0.9130.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grasshopper, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mites, Precision: 0.9859, Recall: 1.0000, F1-Score: 0.9929.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mosquito, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Sawfly, Precision: 0.9853, Recall: 0.9571, F1-Score: 0.9710.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Stem borer, Precision: 0.9583, Recall: 0.9857, F1-Score: 0.9718.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: FloraSyntropy-Net (Our) with Novel Deep Block, Precision: FloraSyntropy-Net (Our) with Novel Deep Block, Recall: FloraSyntropy-Net (Our) with Novel Deep Block, F1-Score: FloraSyntropy-Net (Our) with Novel Deep Block, Overall Accuracy: FloraSyntropy-Net (Our) with Novel Deep Block.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Aphids, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000, Overall Accuracy: 0.9984.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Armyworm, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Beetle, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Bollworm, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Grasshopper, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mites, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Mosquito, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Sawfly, Precision: 0.9859, Recall: 1.0000, F1-Score: 0.9929.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Class: Stem borer, Precision: 1.0000, Recall: 0.9857, F1-Score: 0.9928.
analysis of the ROC and Precision-Recall curves in Fig 9, the proposed FloraSyntropyNet model with the novel deep block demonstrates near-perfect discriminative ability and classification reliability, outperforming the model without the deep block. The ROC curve shows an improvement in AUC from an already exceptional 0.9999 to a perfect 1.0000, indicating a perfect ability to distinguish between all classes without error. Similarly, the Precision-Recall curve prove this superior performance, with the Average Precision (AP) score increasing from 0.9991 to 1.0000, signifying that the model with the deep block achieves robust precision across all recall levels. This errorless performance on both metrics underscores that the novel deep block eliminates the remaining marginal errors, resulting in a model with maximum possible diagonal accuracy and zero misclassifications on the additional dataset. A comparative analysis of the two confusion matrices (O/W novel deep block) clearly demonstrates the performance enhancement achieved by integrating the novel deep block into the FloraSyntropy-Net architecture (Fig 10). The baseline model (a), lacking this block, exhibits significant misclassifications, particularly confusing armyworm with other categories such as 2 incorrect class with bollworm and erroneously predicting mice as mosquito or stem borer. In contrast, the enhanced model (b) shows a substantial reduction in off-diagonal entries, with predictions becoming heavily concentrated on the correct diagonal classes. The only incorrect error is a single instance of mosquito being misclassified as mice. This reduction in confusion, especially for previously problematic classes like armyworm, beetle, and grasshopper, underscores the deep block

<!-- image -->

a

b

Fig. 9 A comparison of performance for the FloraSyntropy-Net model (a) ROC Curve (b) PrecisionRecall Curve, demonstrating a significant reduction in misclassifications and an increase in diagonal accuracy with novel deep block: Additional dataset.

efficacy in refining the model feature extraction and discriminatory capabilities. Consequently, the inclusion of the novel deep block yields a marked improvement in overall classification accuracy and model reliability. Based on the GRADCAM visualizations

<!-- image -->

a

b

Fig. 10 A comparison of confusion matrices for the FloraSyntropy-Net model (a) without and (b) with the novel deep block, demonstrating a significant reduction in misclassifications and an increase in diagonal accuracy.

in Fig 11, the proposed FloraSyntropy-Net model equipped with the novel deep block demonstrates an efficient and more precise interpretability analysis. The visualizations shows that the inclusion of the deep block enables the model to more accurately focus its attention on the most discriminative and pathologically relevant regions of the input images, such as specific leaf lesions or insect damage sites. This heightened spatial

precision in activation maps directly correlates with the model significant reduction in misclassifications, as it is leveraging more meaningful visual features for its predictions. Consequently, the novel deep block not only boosts quantitative performance but also substantially increases the model transparency and diagonal interpretability, providing more trustworthy and actionable insights for plant disease diagnosis. Figure

Fig. 11 Overview of GRADCAM visualizations for FloraSyntropy-Net to highlight the discriminative image regions that most influenced the predictions demonstrating a significant reduction in misclassifications and an increase in diagonal interpretability with novel deep block: Additional dataset.

<!-- image -->

12, t-SNE projection [39] reveals well-separated, distinct clusters for each disease class in the latent space learned by FloraSyntropy-Net. This clear separation indicates the model efficient capability to extract and discriminate between highly nuanced pathological features. The minimal overlap between clusters provides statistical evidence of the model's high classification accuracy and generalization power. Thus, the visualization quantitatively proves the superiority of the proposed architecture's feature representation learning. In fig 12, the proposed FloraSyntropy-Net model with the novel deep block (b) demonstrates an improvement in comparative performance over the model without it (a). The incorporation of the deep block results in significantly more distinct and well-separated clusters for each disease class in the latent feature space, indicating that the model learns more discriminative and class-specific representations. This enhanced separation directly correlates with a reduction in misclassifications and an increase in diagonal accuracy, as the model can more effectively distinguish between visually similar conditions such as alpha arrhythmia, benign syndrome, and grasshopper infection. The clear clustering observed in (b) confirms that the novel architectural enhancement successfully addresses feature ambiguity, leading to superior classification robustness and accuracy.

## 4.9 Ablation study

In this section, we present a comprehensive ablation study to rigorously evaluate the individual contributions of our selected Global-Net backbone architecture and the novel Deep Block integrated within the FloraSyntropy-Net framework. The study systematically dissects the model by incrementally adding or removing key components comparing the performance of the baseline Global-Net (DenseNet201) alone, the Global-Net enhanced with our proposed Deep Block, and alternative configurations

<!-- image -->

a

b

Fig. 12 A comparison of distinct clusters for each disease class in the latent space learned by FloraSyntropy-Net model (a) without and (b) with the novel deep block, demonstrating a significant reduction in misclassifications and an increase in diagonal accuracy.

using established architectural blocks such as residual (ResNet), Inception, Na¨ ıve, and other connections in place of our design. This analysis not only quantifies the performance gain attributable solely to the novel Deep Block through metrics such as accuracy, F1-score, and precision but also validates its robustness and superiority over existing structural alternatives. By isolating each element, we demonstrate that the performance improvements are indeed a result of our FL collective knowledge architectural innovations, thereby reinforcing the design choices and providing empirical evidence of the efficacy and necessity of the proposed Deep Block within the overall system.

Fig 13 illustrates a comparative analysis of model performance, evaluating architectures such as DenseNet variants and other convolutional networks based on accuracy. Among all models, DenseNet201 (referred to as Global-Net in this study) achieves superior performance with a value of 0.9373, as definitely denoted by its distinct blue dashed border. The remaining models, while still demonstrating strong and competitive results within the narrow band of 0.8692 to 0.9306, consistently fall short of the benchmark set by Global-Net. This performance gap underscores the efficacy of DenseNet201 as the optimal backbone feature extractor, approved its selection as the Global-Net within the proposed framework. Table 11 presents the ablation study results demonstrate the clear superiority of the proposed Novel Deep Block over other prominent architectural blocks when integrated into the FloraSyntropy-Net framework. While all alternative blocks including Residual, Inception, Squeeze-andExcitation (SE), Convolutional Block Attention Module (CBAM), and Coordinate Attention (CA) delivered highly competitive and comparable performance with accuracy scores range between 94.20% and 94.48%, the model equipped with the Novel Deep Block consistently outperformed them across every single metric. It achieved the highest scores in Precision (0.8925), Recall (0.8709), F1-Score (0.8704), Accuracy (94.74%), and Cohen's Kappa (0.9463). This uniform dominance across all evaluation criteria presents that the Novel Deep Block provides a more effective mechanism

Fig. 13 Comparative performance of various DL architectures. DenseNet201 (denoted as Global-Net and highlighted with a blue dashed border) achieved the highest performance (0.9373), outperforming all other evaluated models.

<!-- image -->

for feature refinement and representation learning, leading to superior discriminatory power and the most robust overall performance.

Table 11 Ablation study comparing the performance of various architectural blocks integrated into the FloraSyntropy-Net framework, demonstrating the superior performance of the proposed Novel Deep Block across all metrics.

Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with Residual Block, Precision: 0.8758, Recall: 0.8593, F1-Score: 0.8559, Accuracy: 94.31%, Cohen's K: 0.9419.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with Inception Block, Precision: 0.8755, Recall: 0.8541, F1-Score: 0.8519, Accuracy: 94.27%, Cohen's K: 0.9414.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with SE, Precision: 0.8864, Recall: 0.8657, F1-Score: 0.8658, Accuracy: 94.20%, Cohen's K: 0.9407.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with CBAM, Precision: 0.8835, Recall: 0.8581, F1-Score: 0.8599, Accuracy: 94.39%, Cohen's K: 0.9427.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with Na¨ ıve Inception, Precision: 0.8841, Recall: 0.8601, F1-Score: 0.8605, Accuracy: 94.48%, Cohen's K: 0.9436.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with CA, Precision: 0.8844, Recall: 0.8574, F1-Score: 0.8593, Accuracy: 94.40%, Cohen's K: 0.9428.
Según FloraSyntropy-Net: Scalable Deep Learning with Novel FloraSyntropy Archive for Large-Scale Plant Disease Diagnosis (2025), Blocks: FloraSyntropy-Net with Novel Deep Block, Precision: 0.8925, Recall: 0.8709, F1-Score: 0.8704, Accuracy: 94.74%, Cohen's K: 0.9463.
## 5 Discussion with limitation

The results of this study demonstrate that the proposed FloraSyntropy-Net framework represents a significant advancement in the development of robust and generalizable AI models for plant disease diagnosis. The integration of the novel Deep Block was contributory in enhancing feature extraction, leading to a measurable performance gain of 1.64% in overall accuracy and resolving specific weaknesses in classifying challenging disease classes. Moreover, the FloraSyntropy-Net framework federated design, supported by a weighted aggregation strategy, successfully leveraged heterogeneous data from multiple clients to build a global model that is inherently more robust than one trained on isolated, small-scale datasets. The most compelling evidence of this robustness is the model exceptional performance (99.84% accuracy) on the cross-domain Pest 2022 dataset. This demonstrates an unprecedented ability to generalize beyond its training domain, effectively learning universal visual features that are applicable to entirely new classification tasks involving different biological subjects. This suggests that FloraSyntropy-Net successfully mitigates the generalization gap that has plagued previous studies [29, 46] reliant on smaller, less diverse data.

Despite its strong performance, this study is not without limitations:

- The FL process, while advantageous for privacy and data diversity, is computationally intensive and requires significant coordination between participating clients (e.g., agriculture research institutes). The synchronization of model updates across a potentially large number of clients with varying computational resources and network speeds presents a practical challenge for real-time deployment in resource-constrained agricultural settings.
- The framework performance, particularly the cross-domain results, depends on the quality and diversity of the client data. While the weighted aggregation helps balance contributions, the presence of systematically poor-quality or mislabeled data across multiple clients could still negatively influence the global model, an issue that our current design does not explicitly resolve.

## 6 Conclusion and future direction

This study efficiently addressed the critical issue of performance generalization in AIbased plant disease diagnosis. By moving beyond small-scale, homogenous datasets, we introduced the large-scale and globally representative FloraSyntropy Archive, providing an essential benchmark for the agriculture community. The proposed FloraSyntropy-Net framework, integrating a novel Deep Block for enhanced feature learning and a weighted federated optimization scheme, demonstrated superior performance, achieving a SOTA accuracy of 96.38%. Its exceptional cross-domain adaptation capability, validated by a 99.84% accuracy on an unrelated insect pest dataset, underscores its robustness and its effectiveness in bridging the generalization gap that has limited previous models. This work provides a comprehensive, privacy-preserving, and scalable solution that is directly applicable to real-world agricultural settings, offering a significant step toward safeguarding global food security through reliable automated diagnosis.

While the results are highly promising, this work opens several avenues for future research. The current framework computational and coordination demands in a federated setting present a practical limitation for real-time use on resource-constrained devices. Our immediate future work will, therefore, focus on developing a lightweight and asynchronous version of the FL protocol to enhance scalability and reduce synchronization overhead. Furthermore, the model performance is inherently tied to the quality of the client data. To address this, we plan to integrate robust data validation and automated quality control mechanisms at the client level to filter out noisy or mislabeled samples before they influence the global model aggregation.

## Declarations

Ethics approval and consent to participate.

Consent for publication. Not applicable

Data availability. Data will be made available on request.

Funding. No funding

Declaration of competing interest. The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

CRediT authorship contribution statement. Saif Ur Rehman Khan &amp; Muhammed Nabeel Asim: Conceptualization, Data curation, Methodology, Software, Validation, Writing original draft &amp; Formal analysis. Sebastian Vollmer: Conceptualization, Funding acquisition, Supervision. Andreas Dengel: review &amp; editing.

## References

- [1] Gai, Y., Wang, H.: Plant disease: A growing threat to global food security. MDPI, 1615 (2024)
- [2] Vijayreddy, D.: Classification of Plant Diseases, Characteristics and Symptoms on Crop Plants, pp. 171-183. Golden Leaf Publishers, Lucknow, India (2024)
- [3] George, R., al.: Past, present and future of deep plant leaf disease recognition: A survey. Computers and Electronics in Agriculture 234 , 110128 (2025)
- [4] Sambana, B., al.: An efficient plant disease detection using transfer learning approach. Scientific Reports 15 (1), 19082 (2025)
- [5] Laxmi, P.N., al.: Advances in plant disease diagnostics and surveillance-a review. Plant Cell Biotechnology and Molecular Biology 25 (11-12), 137-150 (2024)
- [6] Mduma, H.S., al.: Major signs and symptoms caused by biotic and abiotic agents on plants in the tropical africa. Int J Sci Res 6 , 750-759 (2015)

- [7] Pai, P., al.: Deep learning-based automatic diagnosis of rice leaf diseases using ensemble cnn models. Scientific Reports 15 (1), 27690 (2025)
- [8] Akhtar, H., al.: Traditional strategies and cutting-edge technologies used for plant disease management: A comprehensive overview. Agronomy 14 (9), 2175 (2024)
- [9] Upadhyay, A., al.: Deep learning and computer vision in plant disease detection: a comprehensive review of techniques, models, and trends in precision agriculture. Artificial Intelligence Review 58 (3), 92 (2025)
- [10] Naveed, M., al.: Plant disease diagnosis with artificial intelligence (ai). In: Microbial Data Intelligence and Computational Techniques for Sustainable Computing, pp. 217-234. Springer, ??? (2024)
- [11] D.S. Joseph, P.M.P., Pramanik, R.: Intelligent plant disease diagnosis using convolutional neural network: a review. Multimedia Tools and Applications 82 (14), 21415-21481 (2023)
- [12] M.M. Kabir, A.Q.O., Mridha, M.F.: A multi-plant disease diagnosis method using convolutional neural network. In: Computer Vision and Machine Learning in Agriculture, pp. 99-111. Springer, ??? (2021)
- [13] Kheir, A.M., al.: Smart plant disease diagnosis using multiple deep learning and web application integration. Journal of Agriculture and Food Research, 101948 (2025)
- [14] Gavai, A.K., al.: Agricultural data privacy: Emerging platforms &amp; strategies. Food and Humanity, 100542 (2025)
- [15] Fahim-Ul-Islam, M., al.: A comprehensive approach towards wheat leaf disease identification leveraging transformer models and federated learning. IEEE Access (2024)
- [16] Hari, P., Singh, M.P.: Adaptive knowledge transfer using federated deep learning for plant disease detection. Computers and Electronics in Agriculture 229 , 109720 (2025)
- [17] P. Hari, M.P.S., Singh, A.K.: An improved federated deep learning for plant leaf disease detection. Multimedia Tools and Applications 83 (35), 83471-83491 (2024)
- [18] Kowalska, A., Ashraf, H.: Advances in deep learning algorithms for agricultural monitoring and management. Applied Research in Artificial Intelligence and Cloud Computing 6 (1), 68-88 (2023)
- [19] Yakkundimath, R., al.: Classification of rice diseases using convolutional neural network models. Journal of The Institution of Engineers (India): Series B 103 (4),

1047-1059 (2022)

- [20] Hassan, S.M., Maji, A.K.: Plant disease identification using a novel convolutional neural network. IEEE Access 10 , 5390-5401 (2022)
- [21] Haque, M.A., al.: Deep learning-based approach for identification of diseases of maize crop. Scientific Reports 12 (1), 6334 (2022)
- [22] Tripathy, R., al.: Optimization based rice leaf disease classification in federated learning. Multimedia Tools and Applications 83 (29), 72491-72517 (2024)
- [23] Shrivastava, R.K., al.: A generalized federated learning approach for robust crop disease classification across diverse farms. In: 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS). IEEE, ??? (2024)
- [24] Chorney, W., al.: Federated learning for heterogeneous multi-site crop disease diagnosis. Mathematics 13 (9), 1401 (2025)
- [25] Hlaing, C.S., Zaw, S.M.M.: Tomato plant diseases classification using statistical texture feature and color feature. In: 2018 IEEE/ACIS 17th International Conference on Computer and Information Science (ICIS). IEEE, ??? (2018)
- [26] Fathima, A.A., al.: Cassava (manihot esculenta) dual use for food and bioenergy: A review. Food and Energy Security 12 (1), 380 (2023)
- [27] Parez, S., al.: Towards sustainable agricultural systems: A lightweight deep learning model for plant disease detection. Comput. Syst. Sci. Eng. 47 (1), 515-536 (2023)
- [28] Shetty, S., Mahesh, T.: Skgdc: Effective segmentation based deep learning methodology for banana leaf, fruit, and stem disease prediction. SN Computer Science 5 (6), 698 (2024)
- [29] Acidri, R., al.: Phytochemical profile and antioxidant capacity of coffee plant organs compared to green and roasted coffee beans. Antioxidants 9 (2), 93 (2020)
- [30] Yoosefzadeh-Najafabadi, M., al.: Application of machine learning algorithms in plant breeding: predicting yield from hyperspectral reflectance in soybean. Frontiers in Plant Science 11 , 624273 (2021)
- [31] Xu, W., al.: Detection and classification of tea buds based on deep learning. Computers and Electronics in Agriculture 192 , 106547 (2022)
- [32] P.M. Kai, B.M.d.O., Costa, R.M.: Deep learning-based method for classification of sugarcane varieties. Agronomy 12 (11), 2722 (2022)
- [33] Neri, F., Cotta, C.: Memetic algorithms and memetic computing optimization: A

- literature review. Swarm and Evolutionary Computation 2 , 1-14 (2012)
- [34] Huang, G., al.: Densely connected convolutional networks. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (2017)
- [35] Khan, S.U.R., al.: Folc-net: A federated-optimized lightweight architecture for enhanced mri disease diagnosis across axial, coronal, and sagittal views. arXiv preprint arXiv:2507.06763 (2025)
- [36] Asim, M.N., Malik, M.I., Zehe, C., Trygg, J., Dengel, A., Ahmed, S.: A robust and precise convnet for small non-coding rna classification (rpc-snrc). IEEE Access 9 , 19379-19390 (2020)
- [37] Nabeel Asim, M., Ali Ibrahim, M., Fazeel, A., Dengel, A., Ahmed, S.: Dna-mp: a generalized dna modifications predictor for multiple species based on powerful sequence encoding method. Briefings in Bioinformatics 24 (1), 546 (2023)
- [38] Wasim, M., Mahmood, W., Asim, M.N., Khan, M.U.: Multi-label question classification for factoid and list type questions in biomedical question answering. IEEE Access 7 , 3882-3896 (2018)
- [39] Khan, S.U.R., al.: Shallowmri: A novel lightweight cnn with novel attention mechanism for multi brain tumor classification in mri images. Biomedical Signal Processing and Control 111 , 108425 (2026)
- [40] Shrivastava, V.K., Pradhan, M.K.: Rice plant disease classification using color features: a machine learning paradigm. Journal of Plant Pathology 103 (1), 17-26 (2021)
- [41] Sharif, M., al.: Detection and classification of citrus diseases in agriculture based on optimized weighted segmentation and feature selection. Computers and Electronics in Agriculture 150 , 220-234 (2018)
- [42] Harakannanavar, S.S., al.: Plant leaf disease detection using computer vision and machine learning algorithms. Global Transitions Proceedings 3 (1), 305-310 (2022)
- [43] Shah, D., al.: Rests: Residual deep interpretable architecture for plant disease detection. Information Processing in Agriculture 9 (2), 212-223 (2022)
- [44] V. Singh, N.S., Singh, S.: A review of imaging techniques for plant disease detection. Artificial Intelligence in Agriculture 4 , 229-242 (2020)
- [45] Rao, B.J., al.: Development of deep learning technique for crop pest classification. In: International Conference on Renewable Energy, Green Computing, and Sustainable Development. Springer, ??? (2025)

- [46] Deng, F., al.: Multiple diseases and pests detection based on federated learning and improved faster r-cnn. IEEE Transactions on Instrumentation and Measurement 71 , 1-11 (2022)