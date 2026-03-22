---
id: arxiv-2512.11871
title: Automated Plant Disease and Pest Detection System Using Hybrid Lightweight CNN-MobileViT Models for Diagnosis of Indigenous Crops
year: 2025
country: Internacional
source: ArXiv (cs.CV, cs.AI)
doc_type: Artículo científico
language: en
tags:
  - enfermedades de plantas
  - detección de plagas
  - cultivos
  - transformer
  - dispositivos móviles
  - artículo científico
  - ArXiv
---

## Automated Plant Disease and Pest Detection System Using Hybrid Lightweight CNN-MobileViT Models for Diagnosis of Indigenous Crops

Tekleab G. Gebremedhin * , Hailom S. Asegede, Bruh W. Tesheme, Tadesse B. Gebremichael, Kalayu G. Redae

Department of Computer Science &amp; Engineering and Department of Information Technology Mekelle University - Mekelle Institute of Technology, Ethiopia

Email: tekleab.gebremedhin@singularitynet.io

Abstract -Agriculture supports over 80% of the population in the Tigray region of Ethiopia, where infrastructural disruptions limit access to expert crop disease diagnosis. We present an offline-first detection system centered on a newly curated indigenous cactus-fig ( Opuntia ficus-indica ) dataset consisting of 3,587 field images across three core symptom classes. Given deployment constraints in postconflict, edge environments, we benchmarked three mobile-efficient architectures: a custom lightweight CNN, EfficientNet-Lite1, and the CNN-Transformer hybrid MobileViT-XS.

While the broader system contains independent modules for potato, apple, and corn, this study isolates cactus-fig model performance to evaluate attention sensitivity and inductive bias transfer on indigenous morphology alone.

Results establish a Pareto trade-off: EfficientNet-Lite1 achieved 90.7% test accuracy, our lightweight CNN reached 89.5% with the most favorable deployment profile (42 ms inference latency, 4.8 MB model size), and MobileViT-XS delivered 97.3% mean crossvalidation accuracy, showing that MHSA-based global reasoning disambiguates pest clusters from 2D fungal lesions more reliably than local-texture CNN kernels. The ARM-compatible models are deployed inside a Tigrigna and Amharic-localized Flutter application supporting fully offline inference on Cortex-A53-class devices, strengthening inclusivity for food-security-critical diagnostics.

Index Terms -Cactus-Fig, CNN-ViT Hybrid, Edge AI, ICT4D, Food Security, Deep learning, Django backend, TensorFlow Lite, localization, Tigrigna, Amharic, Ethiopia.

## I. INTRODUCTION

Agriculture is critical to livelihoods in Ethiopia's Tigray region, a post-conflict environment where damaged infrastructure disrupts expert crop disease diagnosis and timely advisory interventions [1]. The drought-resilient cactus-fig ( Opuntia ficus-indica ), locally known as 'Beles,' plays a dual socioeconomic role: as a seasonal buffer crop supporting food availability during pre-harvest scarcity and as an industrial raw material used in local manufacturing sectors [6].

Ecologically unique to the highland agro-system, cactus-fig acts as a strategic buffer crop against seasonal food scarcity, providing nutrition when alternative yields are depleted. A major production threat is the invasive cochineal insect ( Dactylopius coccus ) and fungal rots, which form visually ambiguous symptoms (white wax clusters vs. mildew-like textures) capable of causing large-scale yield devastation if not detected early [6], [13].

Corresponding author. The source code and dataset are publicly available at: https://github.com/Tekleab15/Automated plant disease and pest detection system

† A shorter version of this work was presented at the International Conference on Postwar Technology for Recovery and Sustainable Development in Mekelle, Tigray, in Feb. 2025.

Historically, disease diagnosis relied on manual inspection by agricultural extension workers. However, the recent conflict in the region has severely damaged infrastructure and disrupted the human advisory supply chain, leaving millions of farmers isolated from expert support. In this context, automated, offline-first diagnostic tools are not merely a convenience but a humanitarian necessity.

Recent advances in Computer Vision have enabled automated disease recognition, with Convolutional Neural Networks (CNNs) achieving high accuracy on global datasets like PlantVillage [3].

However, deploying these models for indigenous highland crops presents two specific scientific challenges:

- 1) The Data Gap: Xerophytic crops like Cactus-fig are morphologically distinct from the broad-leaf crops (e.g., Apple, Corn) found in standard datasets. Their cladodes (pads) exhibit waxy surfaces, glochids (spines), and irregular 3D structures that confound standard pre-trained models.
- 2) The Architectural Dilemma: Distinguishing between fungal lesions (2D surface textures) and cochineal infestations (3D clustered pests) requires a model that captures both local texture details and global context. Standard CNNs excel at local features but lack the global receptive field to identify scattered pest clusters. Conversely, Vision Transformers (ViTs) capture global context but are often too computationally heavy for the low-end hardware found in rural Ethiopia.

To bridge this gap, this paper presents an Automated Plant Disease and Pest Detection System built upon a novel, field-verified dataset of indigenous crops. We propose a hybrid approach, benchmarking a custom Lightweight CNN (optimized for extreme efficiency) against the MobileViT-XS architecture, a CNN-ViT hybrid that combines the inductive bias of convolutions with the self-attention of Transformers.

Our specific contributions are:

- Indigenous Dataset Construction: We introduce a dataset of 3,587 annotated images of Opuntia ficusindica , capturing real-world field variability (dust, shadows, mixed infections) often absent in laboratory datasets.
- Hybrid Architecture Benchmarking: We rigorously evaluate the trade-off between Inductive Bias (CNN) and Self-Attention (ViT). We demonstrate that the hybrid MobileViT-XS architecture achieves SOTA accuracy
- (97.3%) by effectively resolving visual ambiguities that mislead pure CNNs.
- Offline-First Deployment: We deploy the optimized models in a Tigrigna and Amharic-localized Flutter application capable of running on ARM Cortex-A53 devices without internet connectivity, ensuring equitable access for resource-constrained farming communities.

The remainder of this paper is organized as follows: Section II provides biological and technical background. Section IV details the dataset and hybrid model architectures. Section V presents the comparative results and explainability analysis. Section VI concludes with implications for food security.

## II. BACKGROUND

## A. Plant Pathology and Visual Symptom Variability

Plant diseases manifest through complex visual cues such as chlorosis, necrotic spots, pustules, and wilting. From a computer vision perspective, these symptoms present a significant challenge due to their high intra-class variance and inter-class similarity. Symptoms are often non-uniform, multi-stage, and visually confounded by environmental factors such as dust, nutrient deficiencies, or physical damage.

The target crop, Opuntia ficus-indica (Cactus-fig), introduces unique morphological constraints. Unlike the planar leaf structures of broad-leaf crops (e.g., maize, apple), cactus cladodes (pads) are voluminous, waxy, and covered in glochids (spines). The primary pest threat, the cochineal insect ( Dactylopius coccus ), creates white, cottony wax clusters that can be visually indistinguishable from certain fungal mildews to standard texture-based classifiers. Discriminating between these 3D pest clusters and 2D fungal lesions requires a model capable of understanding both local texture and global geometric context.

## B. Convolutional Neural Networks (CNNs)

CNNs have established themselves as the standard for agricultural image analysis due to their ability to learn hierarchical feature representations. A typical CNN is composed of stacked convolutional layers that extract local features (edges, textures) and pooling layers that introduce spatial invariance.

Formally, a convolutional layer computes a feature map F from an input X using a learnable kernel W and bias b :

$$F _ { i , j } = \sigma \left ( \sum _ { m } \sum _ { n } W _ { m , n } \cdot X _ { i + m , j + n } + b \right ) \quad ( 1 ) \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \stackrel { A c r } { \ s h i f t } , \quad \$$

where σ is a non-linear activation function (e.g., ReLU). While CNNs excel at extracting local patterns, their limited receptive field can struggle to capture long-range dependencies, such as the spatial distribution of a pest infestation across a large cladode.

Fig. 1: CNN Architecture



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un **C [ ] [ ] [ ] [



Fig. 2: MobileVIT Architecture [7]



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un **trans



## C. Vision Transformers and Self-Attention

To address the limitations of local receptive fields, Vision Transformers (ViTs) adapt the self-attention mechanism from Natural Language Processing to image data. Unlike CNNs, which process pixels in fixed neighborhoods, Transformers treat an image as a sequence of patches and compute the relationship between every patch pair simultaneously.

The core mechanism is Multi-Head Self-Attention (MSA), which allows the model to weigh the importance of different image regions globally. For a given input sequence Z , the attention output is computed as:

$$A t e n t i o n ( Q , K , V ) = \text {softmax} \left ( \frac { Q K ^ { T } } { \sqrt { d _ { k } } } \right ) V \quad ( 2 )$$

where Q , K , V represent the Query, Key, and Value matrices projected from the input. This global context awareness makes ViTs particularly effective at distinguishing complex, scattered pathologies like cochineal clusters from background noise. MobileViT, the architecture used in this study, creates a hybrid by embedding this global processing block inside a lightweight CNN backbone to retain efficiency.

## D. Domain Shift in Field Settings

A critical barrier to deploying AI in agriculture is domain shift , where models trained on controlled laboratory images fail in real-world field conditions. Field images introduce uncontrolled variables such as harsh lighting shadows, occlusion by other plants, and background clutter (soil, sky, weeds). For xerophytic crops, the high reflectivity of the waxy cuticle under direct sunlight creates specular highlights that can be misclassified as lesions. This study explicitly addresses domain

shift by training on a dataset captured entirely in uncontrolled field environments.

## E. Edge AI and Model Quantization

Deploying deep learning models in rural Tigray requires overcoming severe hardware constraints. Farmers typically rely on low-end Android devices with limited RAM, battery life, and computational power (e.g., ARM Cortex-A53 processors). Cloud-based inference is often unfeasible due to intermittent internet connectivity.

To enable offline execution, we employ Post-Training Quantization (PTQ). This process maps high-precision 32-bit floating-point weights ( W fp 32 ) to lower-precision 16-bit floats ( W fp 16 ) or 8-bit integers:

$$W _ { q } = \text {round} \left ( \frac { W _ { f p 3 2 } } { S } \right ) + Z \quad \quad ( 3 ) \quad ^ { C . \ E q } \quad \begin{matrix} C . & E q \\ F o r \end{matrix}$$

where S is a scaling factor and Z is the zero-point. This compression reduces model size and inference latency with minimal degradation in accuracy, making complex architectures like MobileViT deployable on edge devices.

## F. Explainability (XAI) in Agriculture

Trust is a prerequisite for technology adoption in agrarian communities. Black-box AI models offer little insight into their decision-making process. To bridge this gap, we integrate Explainable AI (XAI) techniques such as Local Interpretable Model-agnostic Explanations (LIME). LIME generates saliency maps that highlight the specific image regions driving a prediction. By visualizing that the model is focusing on the pest or lesion rather than background artifacts, we provide agronomic validation that builds user confidence in the automated diagnosis.

## III. RELATED WORK

The automation of plant disease diagnosis has evolved from hand-crafted feature extraction to end-to-end deep learning. This section reviews the trajectory of these technologies and identifies critical gaps regarding indigenous crops and resource-constrained deployment.

## A. Deep Learning in Global Plant Pathology

The foundational work by Mohanty et al. [3] established the viability of Convolutional Neural Networks (CNNs) for crop disease diagnosis, achieving nearly 99% accuracy on the PlantVillage dataset. Subsequent studies optimized architectures such as ResNet and VGG to improve robustness against lighting variations [4]. However, a systematic review of agricultural AI in Ethiopia [2] reveals a persistent bias: models are predominantly trained on globally commercial crops (maize, tomato, apple) with broad planar leaves. These models generalize poorly to xerophytic crops like Opuntia ficus-indica , whose morphology (voluminous cladodes, glochids) and pathology (3D cochineal clusters) differ fundamentally from leaf spots [6].

## B. Hybrid Architectures and Transformers

To address the receptive field limitations of CNNs, researchers have increasingly adopted Vision Transformers (ViTs). Recent hybrid architectures like MobileViT [7] and PMVT [8] merge the inductive bias of convolutions with the global awareness of self-attention. In the specific domain of cactus pathology, Berka et al. [5] introduced CactiViT , a Transformer-based network designed for diagnosing cactus cochineal infestation. While their work demonstrated the efficacy of attention mechanisms for this crop, it primarily targeted high-end smartphone deployment. This leaves a gap for architectures optimized for the legacy hardware prevalent in post-conflict zones, where computational efficiency is as critical as accuracy.

## C. Edge AI and Offline Deployment

For deployment in the Global South, efficiency is paramount. Architectures like EfficientNet [10] and L-Net [12] utilize depth-wise separable convolutions to reduce parameter counts. Chowdhury et al. [14] demonstrated that model quantization could enable offline inference on mobile devices. Despite these advances, a trade-off remains: ultra-lightweight CNNs often sacrifice the semantic understanding required to distinguish complex pest clusters from physical scarring. Furthermore, few systems incorporate Explainable AI (XAI) techniques like LIME [15] directly into the mobile workflow to build user trust in rural communities.

## D. Gap Analysis

Most plant pathology models prioritize global commercial crops using convolution-dominated benchmarks and static leaf morphology [3], [4]. Transformer-based vision models show strong separation but incur O( N 2 ) self-attention latency and RAM pressure, limiting fully offline use on low-end devices [5], [8]. Lightweight CNNs offer low latency yet fail to encode geometric correlation needed to separate 3D cochineal clusters from 2D scars or fungal rot on cactus cladodes [10], [11]. No prior work benchmarks indigenous cactus-fig field imagery with failure-mode isolation and transfer-leakage prevention. This study evaluates a 1.2M-parameter CNN vs. a fine-tuned MobileViT-XS hybrid, measuring accuracy, latency, and size without cross-crop knowledge leakage.

## IV. METHODOLOGY

This section details the dataset curation, preprocessing pipeline, and the architectural design of the two competing models: a custom lightweight CNN (efficiency-focused) and the MobileViT-XS hybrid (accuracy-focused). All design choices are motivated by the dual constraints of high diagnostic precision and deployment on low-end mobile hardware in offline environments.

## A. Dataset Curation

1) Multi-Crop Backbone: To ensure the models learn robust, generalized vegetative features, we aggregated a background dataset of 26,394 images from public repositories (e.g.,

PlantVillage), spanning tomato, potato, maize, and apple crops. This pre-training step stabilizes the early layers of the feature extractors before fine-tuning on the target domain.

- 2) Indigenous Cactus-Fig Dataset: The core contribution of this work is the curation of a domain-specific dataset for Opuntia ficus-indica (Beles), collected at Mekelle University and Adigrat University experimental sites. The full dataset has been open-sourced and is accessible via the project repository and Kaggle. The dataset consists of 3,587 high-resolution field images categorized into three classes:
- Affected (1,500 images): Cladodes exhibiting symptoms of cochineal infestation (white waxy clusters) or fungal rot (necrotic lesions).
- Healthy (1,500 images): Asymptomatic cladodes with natural variations in color and texture.
- No Cactus (587 images): Background images (soil, sky, weeds) to train the model to reject non-plant inputs.

Fig. 3: Example of affected cactus-fig cladode showing cochineal clusters and fungal lesions.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



Fig. 4: Example of healthy cactus-fig cladode with no disease or pest symptoms.



> **[💡 Descripción de Imagen VLM]:** La imagen es un conjunto de 9 sub-imagens de cactos en diferentes ás



## B. Preprocessing and Augmentation

Input images are resized to 256 × 256 pixels and normalized to the unit interval [0 , 1] . To mitigate overfitting given the limited size of the indigenous dataset, we employ a Sanitized Validation Protocol : geometric augmentations are applied only to the training split, while validation is performed on clean, static images. The augmentation function A ( X ; θ ) is defined as:

$$\tilde { X } = \mathcal { A } ( X ; \theta ) = T _ { \text {rot} } ^ { \theta _ { r } } \cdot T _ { \text {zoom} } ^ { \theta _ { z } } \cdot T _ { \text {flip} } ^ { \theta _ { f } } ( X )$$

where θ represents random parameters for rotation ( ± 20 ◦ ), zoom ( ± 15% ), and horizontal flipping.

## C. Model Architectures

We investigate two distinct architectural paradigms to identify the optimal trade-off for edge deployment.

- 1) Custom Lightweight CNN (Efficiency-First): Designed for ultra-low latency on legacy devices, this model consists of three sequential convolutional blocks. Each block k performs feature extraction defined by:

$$\i t e s t a r { \text { for } } \quad F _ { k } ( i , j ) = & \, \text {Pool} \left ( \sigma \left ( \sum _ { m , n } W _ { k } ( m , n ) \cdot X ( i + m , j + n ) + b _ { k } \right ) \right ) \\ \i t e s t a r { \text { has } } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where σ is the ReLU activation function. The architecture prioritizes a small receptive field to capture local texture anomalies (e.g., rot spots) with minimal computational cost ( ∼ 1 . 2 M parameters).

- 2) MobileViT-XS (Accuracy-First): To capture global context, we implement the MobileViT-XS architecture [7] which contains approximately 2.3 million parameters. Unlike pure CNNs, MobileViT introduces a hybrid block that combines standard convolutions for local processing with Multi-Head Self-Attention (MHSA) for global interaction. This allows the model to see the entire image at once, effectively distinguishing between scattered pest clusters (cochineal) and random environmental noise. The model was fine-tuned using the AdamW optimizer with a Cosine Decay learning rate schedule to ensure stable convergence on the small dataset.

## D. On-Device Deployment

For offline-first operation on low-end Android devices in rural post-conflict Tigray, trained models were exported to the TensorFlow Lite runtime and compressed using Float16 PostTraining Quantization (PTQ), enabling reduced storage footprint and efficient on-device inference. The custom lightweight CNN serves as the default real-time scanner for rapid local symptom screening, while MobileViT-XS is invoked as a selective high-precision model to resolve visually ambiguous cases, particularly the 2D fungal lesion versus 3D cochineal cluster dilemma. A dedicated non-plant rejection class mitigates false activations from background artifacts such as soil, sky, and weeds. All predictions and agronomic guidance are delivered through a Tigrigna and Amharic-localized Flutter Android interface to ensure fully offline, farmer-centric decision support in low-resource environments.

## V. EXPERIMENTS AND RESULTS

This section evaluates the proposed architectures across diagnostic precision, computational efficiency, and robustness to field variability. All results are derived from the held-out test set ( N = 1 , 195 ) of the indigenous cactus-fig dataset to ensure generalization.

## A. Experimental Setup

Training was conducted on an NVIDIA Tesla P100 GPU (16 GB VRAM) using PyTorch and the timm library. We utilized 3-Fold Stratified Cross-Validation to ensure statistical robustness. All models were trained for 50 epochs using the AdamW optimizer ( η = 2 e -4 , weight decay = 0 . 05 ) and a Cosine Decay learning rate scheduler.

Fig. 5: Cactus-fig symptom detection screen from the deployed Flutter Android application demonstrating offline image capture for real-time local screening.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



Fig. 6: Tigrigna and Amharic-localized recognition and disease-information interface providing offline condition classification, medicine recommendation, and usage guidance.



> **[💡 Descripción de Imagen VLM]:** La imagen es un grá



## B. Quantitative Benchmarks

We benchmarked three architectures representing the spectrum of mobile AI. Table I summarizes the performance tradeoffs.

TABLE I: Performance vs. Efficiency Trade-offs (Test Set)

Según Automated Plant Disease and Pest Detection System Using Hybrid Lightweight CNN-MobileViT Models for Diagnosis of Indigenous Crops (2025), Model: EfficientNet-Lite1, Acc.: 90.7%, F1: 0.9, Params: 4.6 M, Size: 19.0 MB, Latency: 55 ms.
Según Automated Plant Disease and Pest Detection System Using Hybrid Lightweight CNN-MobileViT Models for Diagnosis of Indigenous Crops (2025), Model: Proposed CNN, Acc.: 89.5%, F1: 0.89, Params: 1.2 M, Size: 4.8 MB, Latency: 42 ms.
Según Automated Plant Disease and Pest Detection System Using Hybrid Lightweight CNN-MobileViT Models for Diagnosis of Indigenous Crops (2025), Model: MobileViT-XS, Acc.: 97.3%, F1: 0.98, Params: 2.3 M, Size: 9.3 MB, Latency: 68 ms.
## C. Confusion Matrix Analysis

To understand the behavioral differences between Inductive Bias (CNNs) and Global Attention (Transformers), we analyzed the confusion matrices of the three models (Fig. 7).

1) Texture Ambiguity in CNNs: Both the Custom CNN and EfficientNet-Lite1 exhibited a specific failure mode: misclassifying older, scarred Healthy cladodes as Affected . This 'Scarring vs. Lesion' ambiguity accounts for 68% of the Custom CNN's errors. Convolutional filters, which rely on local texture gradients, struggle to differentiate the rough texture of a physical scar from the necrotic texture of fungal rot.

- 2) Global Context in MobileViT: The MobileViT-XS effectively resolved this ambiguity, achieving a precision of 0.97 for the 'Affected' class. The Multi-Head Self-Attention (MHSA) mechanism allows the model to correlate the visual feature with its spatial context. Specifically, it learned that cochineal infestations appear as clusters of white powder, whereas scarring appears as random, isolated patches. This global context awareness enabled the model to reject 94% of the false positives generated by the CNN baselines.

## D. Robustness to Field Scenarios

Beyond aggregate metrics, we evaluated the models under challenging field conditions common in Tigray:

- Scenario A: Early-Stage Infestation. MobileViT successfully detected minute cochineal specks ( &lt; 5% surface area) that EfficientNet missed. The Transformer's ability to attend to small, salient regions regardless of position proved critical for early warning.
- Scenario B: Background Clutter. The 'No Cactus' class (background soil/sky) was classified with 99% precision by all models. However, MobileViT showed superior robustness in 'Mixed' frames where a healthy cactus was partially occluded by weeds, correctly focusing on the plant rather than the noise.
- Scenario C: Variable Lighting. Under harsh midday sunlight (high specular reflection on waxy pads), the Custom CNN occasionally predicted false lesions due to glare. MobileViT's feature representations remained invariant to these local lighting intensity shifts.

## E. Discussion: The Pareto Frontier

The results establish a clear tiered deployment strategy. The Proposed CNN provided the most efficient deployment profile (42 ms, 4.8 MB), suitable for real-time video scanning on legacy hardware. The MobileViT-XS offered the best diagnostic reliability (97.3%), serving as a high-precision verification tool. This dual capability directly addresses the hardware diversity found in post-conflict agricultural zones. Comparative confusion matrices on the cactus-fig test set are shown below. Custom CNN errors stem mainly from scarvs-lesion texture ambiguity, EfficientNet-Lite1 reduces these errors but retains false positives, and MobileViT-XS achieves strong separation of cochineal clusters from lesions. Following that there is a learning curve and LIME explanation output samples.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de líneas que compara la evolución de la “C ”



Fig. 7: Comparative confusion matrices on the cactus-fig held-out test set. (Left) Custom CNN shows confusion between Healthy and Affected due to re-scaled local texture ambiguity. (Center) EfficientNet-Lite1 reduces margin errors but retains false positives under scar-like textures. (Right) MobileViT-XS resolves ambiguity by leveraging global self-attention, achieving strong separation for cochineal clusters versus fungal lesions.

Fig. 8: Training and validation learning curves for the proposed lightweight CNN.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de dos líneas que representan la curv



Fig. 9: LIME-based explanation for an Affected prediction, highlighting cochineal clusters and lesion regions driving the MobileViT-XS decision.



> **[💡 Descripción de Imagen VLM]:** La imagen es un diagrama de un cactus de “ “ “ “ “



## VI. CONCLUSION AND FUTURE WORK

## A. Conclusion

This study developed an offline-first crop disease diagnostic benchmark for the indigenous cactus-fig crop in Tigray, Ethiopia, critical for resilient agricultural decision support in infrastructure-broken zones [1]. Using a curated field dataset ( N = 3 , 587 ), we compared local convolution-based and global self-attention models without auxiliary transfer learning. Results demonstrate a Pareto trade-off: a lightweight CNN enables rapid localized texture diagnosis (42 ms, 4.8 MB, 89.5% accuracy), while the CNN-Transformer hybrid

MobileViT-XS achieves superior diagnostic reliability (97.3% mean cross-validation accuracy) by resolving spatially correlated symptom ambiguities that local convolutions cannot model effectively. A rejection class reduces background false triggers, and a Tigrigna and Amharic-localized Flutter Android interface ensures fully offline inference and farmer-centric guidance. This work provides a practical engineering blueprint for scalable Edge AI deployment on legacy Android devices in conflict-affected agricultural environments.

## B. Future Work

Future iterations of this system will focus on:

- Hybrid Deployment: Implementing a tiered system where the lightweight CNN performs real-time scanning, while ambiguous cases are flagged for analysis by the more accurate MobileViT model when connectivity allows.
- Dataset Expansion: Extending the indigenous dataset to include other regional staples such as Teff and Sorghum, and incorporating diverse pests like the Fall Armyworm.
- UAV Integration: Adapting the lightweight model for deployment on low-cost drones to enable large-scale, autonomous monitoring of cactus plantations in inaccessible terrain.

## REFERENCES

- [1] FAO, 'The future of food and agriculture - Trends and challenges,' Food and Agriculture Organization of the United Nations , Rome, 2022.
- [2] T. Alemu, 'Plant Disease Detection Using Digital Image Processing for Commonly Consumed Food Plants in Ethiopia: A Systematic Literature Review,' Communications in Computer and Information Science , Springer, 2025.
- [3] S. P. Mohanty, D. P. Hughes, and M. Salath´ e, 'Using deep learning for image-based plant disease detection,' Frontiers in Plant Science , vol. 7, p. 1419, 2016.
- [4] E. C. Too et al. , 'A comparative study of fine-tuning deep learning models for plant disease detection,' Artificial Intelligence in Agriculture , vol. 2, pp. 81-90, 2019.
- [5] A. Berka, A. Hafiane, and Y. Es-saady, 'CactiViT: Image-based smartphone application and transformer network for diagnosis of cactus cochineal,' Artificial Intelligence in Agriculture , vol. 9, pp. 100370, 2023.

- [6] L. P. da Silva et al. , 'Testing Opuntia ficus-indica genotypes for resistance against Dactylopius coccus (Hemiptera: Dactylopiidae),' Revista Colombiana de Entomolog´ ıa , vol. 49, no. 2, 2023.
- [7] S. Mehta and M. Rastegari, 'MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer,' International Conference on Learning Representations (ICLR) , 2022.
- [8] L. Wang et al. , 'PMVT: A lightweight vision transformer for plant disease identification on mobile devices,' Frontiers in Plant Science , vol. 14, 2023.
- [9] M. Tonmoy et al. , 'MobilePlantViT: A Mobile-friendly Hybrid ViT for Generalized Plant Disease Image Classification,' arXiv preprint arXiv:2503.16628, 2025.
- [10] M. Tan and Q. V. Le, 'EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks,' International Conference on Machine Learning (ICML) , 2019.
- [11] ¨ U. Atila et al. , 'Plant disease detection with a lightweight convolutional neural network,' IEEE Access , vol. 9, pp. 19826-19834, 2021.
- [12] S. Kumar et al. , 'L-Net: A Lightweight CNN Framework for Sustainable Multicrop Leaf Disease Detection on Edge Devices,' Sustainable Food Technology , 2025.
- [13] X. Zhang et al. , 'High-Accuracy Detection of Maize Leaf Diseases CNN Based on Multi-Pathway Activation Function Module,' Remote Sensing , vol. 13, no. 21, p. 4218, 2021.
- [14] M. E. H. Chowdhury et al. , 'A Mobile-Based System for Detecting Plant Leaf Diseases Using Deep Learning,' Sensors , vol. 21, no. 9, 2021.
- [15] M. T. Ribeiro, S. Singh, and C. Guestrin, 'Why should I trust you?: Explaining the predictions of any classifier,' Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining , 2016.