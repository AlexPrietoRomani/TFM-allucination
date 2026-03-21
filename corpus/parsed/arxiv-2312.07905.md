---
id: arxiv-2312.07905
title: Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities
year: 2023
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

## Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities

Mingle Xu a , Ji Eun Park a , Jaehwan Lee a , Jucheng Yang b, ∗ , Sook Yoon c, ∗

Department of Electronic Engineering, Core Research Institute of Intelligent Robots, Jeonbuk National University, Jeonju, South Korea

College of Artificial Intelligence, Tianjin University of Science and Technology, Tianjin, China a b

c Department of Computer Engineering, Mokpo National University, Muan, South Korea

## Abstract

Plant disease recognition has witnessed a significant improvement with deep learning in recent years. Although plant disease datasets are essential and many relevant datasets are public available, two fundamental questions exist. First, how to differentiate datasets and further choose suitable public datasets for specific applications? Second, what kinds of characteristics of datasets are desired to achieve promising performance in real-world applications? To address the questions, this study explicitly propose an informative taxonomy to describe potential plant disease datasets. We further provide several directions for future, such as creating challenge-oriented datasets and the ultimate objective deploying deep learning in real-world applications with satisfactory performance. In addition, existing related public RGB image datasets are summarized. We believe that this study will contributing making better datasets and that this study will contribute beyond plant disease recognition such as plant species recognition. To facilitate the community, our project is public available with the information of relevant public datasets.

Keywords: plant disease dataset, deep learning, smart agriculture, precision agriculture

∗ Corresponding author

Email addresses: jcyang@tust.edu.cn (Jucheng Yang ), syoon@mokpo.ac.kr (Sook Yoon )

## 1. Introduction

To have enough food is a basic requirement of human beings. However, more than 600 million people worldwide are estimated to be exposed to hunger in 2030 according to the United Nations. However, many things threaten the availability of food and plant disease is one of the most essential. It is estimated that $ 220 billions loss because of plant disease according to the Food and Agriculture Organization of the United Nations. It is therefore eager to mitigate them and recognizing plant diseases is a fundamental mission. However, a traditional way is that human experts have to go farm to see the plants and then make decisions. This paradigm is expensive and noisy because training experts need time and many factors play a role to human to make decisions such as mood and lasting time to work [1].

Fortunately, deep learning has been showcased the potential to recognize plant diseases automatically in recent years [2, 3, 4, 5, 6, 7]. To achieve a decent performance for deep learning models, dataset is one of the most essential considerations [8, 9, 10, 11]. High-quality training datasets are expected to achieve decent test performance and superior generalization capacity. However, plant disease recognition datasets have received relatively less attention in recent years. We argue that it is worthwhile with the following reasons. First, there is no high quality widely used benchmark, which seriously hinders the further development. A common observation is that current deep learning methods tends to suffer in the real-world applications, especially in generalization in general computer vision tasks [12, 13, 9, 14], as well as in the recognition of plant diseases [15, 16, 17]. The field of plant disease recognition desire those datasets in high-quality and close to real-world applications. Second, this kind of dataset is much difficult to collect as it needs essential understandings in both deep learning and agricultural field. Compared to generic benchmarks in computer vision such as ImageNet [18] and COCO [19] that are related to daily-available objects, strong domain knowledge about agriculture and plant is elusively required to create a plant disease recognition dataset. Simultaneously, knowledge about deep learning should be involved, such as the challenges with current deep learning methods and the strategies to annotate the data. For example, data annotation should be compatible with the application objective and deep learning methods, as detailed in Section 2.6.

To address such issues, this paper aims to bridge agriculture and deep learning, which will enhance the understanding to make superior related

datasets and further facilitate the deployment of deep learning in real-world tasks of plant disease recognition. Our ambitious objective it to deploy deep learning models in real-world applications effectively, efficiently, and robustly. With such goal, this study has the following main contributions:

- It proposes an informative taxonomy for plant disease recognition datasets.
- It summarizes current public plant disease datasets.
- It presents the future directions to create plant disease datasets with additional discussions.

## 2. Taxonomy

As shown in Table 1, this section aims to provide a taxonomy to describe and distinguish datasets to recognize plant diseases. We emphasize that diverse datasets have their disadvantages and advantages, and thus should be considered from different perspectives, which inspires this section. We hope the proposed taxonomy will enhance the understanding for the community from making the objective of real-world applications, collecting suitable datasets, to deploying compatible deep learning methods.

## 2.1. Application objective

In terms of plant disease recognition, different applications may have specific interests , such as the type of plants and organs. For example, some applications focus on one specific crop such as tomatoes [20, 21] and apples [22] whereas others may consider multiple crops [23, 24]. Similarly, diseases exist in different organs, such as leaves, fruits, and stems.

Moreover, applications require different recognition levels. When diseases appear, one may wonder what it is, referring to classification. Sometimes, multiple diseases may happen and localization is thus beneficial. Specifically, one plant may be with more than one unhealthy symptom where the locations give more precise information, as well as one leaf. Furthermore, some decisions and remedies can be adopted based on their magnitudes, termed quantitation, such as the number of infected leaves and the severity in an unhealthy leaf. To some extent, the complexities of the mentioned analysis gradually improves. Fortunately, these analysis can be implemented by choosing appropriate methods from deep learning, including image classification, object detection, and segmentation [17].

Table 1: Taxonomy of datasets to recognize plant diseases using deep learning.

Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Input modality, Application objective: Input modality, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: It covers optical image, video, text, au- dio, and their combinations..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Image acquirement, Application objective: Optical sensor, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Type of sensors to get images, includ- ing the cameras of RGB, hyper-spectral, multi-spectral, thermal, depth image..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Image acquirement, Application objective: Platform, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Place or device to put the optical sensors, including human hand, robot arm, UAV, aircraft, and satellite..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Image variation, Application objective: Image variation, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Change and visual variation of images within a class, such as background, illu- mination, and scale. The image belong- ing to a class in a dataset may be with enormous or few image variation..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Dataset splitting, Application objective: Dataset splitting, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Strategies to split a collected dataset into training, test, and validation datasets, including random, spatial, and temporal..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Annotation, Application objective: Existence, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Datasets can be categorized into fully, partly, and no annotated if every image, part of images, and non images are an- notated, respectively..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Annotation, Application objective: Correctness, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Strategy to make sure that annotations from human experts are correct. In gen- eral, annotations are with bias and noise and voting is an effective yet expensive strategy to reduce them if experts pro- vide annotations individually..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Application objective: Annotation, Application objective: Level, It can be considered from interest, in- cluding types of plant and organ, and recognition levels, including classifica- tion, localization, and quantitation.: Annotation level, including image, in- stance, and pixel level where annotations are given for a holistic image, every in- stance of disease, and every pixel..
## 2.2. Input modality

To recognize plant diseases, human experts use multiple senses such as vision and smell. In addition, knowledge from other experts and their own experience also benefits. In terms of machines equipped with deep learning, similar scenarios exist. Optical images, a kind of vision, are one of the most fundamental modalities of information to recognizing plant diseases. They can be obtained with different devices and with multiple sub-categorizes, as described in the next subsection. Videos and time-series images provide extra information than the images alone. To be more specific, videos may capture the visual patterns of plant diseases from different perspectives and distances which can be taken as accumulated observations. In a similar spirit, time-series images resemble the actions of human experts who investigate the transformation of plant diseases in a row of days to make decisions. Besides, texts are also beneficial with semantic information in nature because they are created by human beings. For example, it depict the characteristics of plant diseases such as color and their changes in temporal. Texts can describe images such as locations of diseases and their magnitudes of severity [25, 26, 27]. Furthermore, texts can be replaced with audio to give human knowledge. More modalities are possible and encouraged such as smell and novel ones because of new types of sensors can also be employed in the future [28].

## 2.3. Image acquirement

Figure 1: Optical sensors and platform to take images for plant disease, adapted from [6] and inspired by [29, 30]. Extra types of sensor and platform are possible and encouraged. Please refer the advantages and disadvantages of the sensors and platform to [29, 30].

<!-- image -->

Although heterogeneous modalities of input exist to recognize plant diseases as mentioned above, optical images are the most widely one. This subsection aims to probe the ways to get them since there are multiple types for optical image beneficial for diverse cases [30, 29]. As shown in Figure 1, optical image acquirement is grouped into two factors, sensors to take images and platform to hold the sensors.

The widely used type of optical sensor is the RGB (red, green, and blue) camera that captures a range of visible wave length. Human understand RGB images very well. One of the reason of the popularity of RGB images is the great availability resulting from the relative cheap mobile phones. Simultaneously, those phones handled by human beings produce enormous RGB images. Imagine the scenario that any person with a phone can take pictures if they are interested in the abnormal plants. Besides, The resolution evolves larger significantly with clear details. Except for human, RGB cameras can be fixed to monitor the growth of plants. RGB cameras placed in robot arms that can move automatically would be an efficient way to free human. We argue that this type is superior to the plants in greenhouses. In spite of its super convenience of RGB images, extra information is also contributing. For example, thermal sensors are light-free and thus can be employed in the night when RGB cameras fail to work. Fluorescence is another possible type although, to the best of our knowledge, there is no related dataset.

The above mentioned sensors take images with a certain range of wavelength. In contrast, multi- and hyper-spectral sensors can also record images with multiple and many levels of wavelength, resulting in images with many channels. In general, many vegetation indexes can be obtained with the two sensors [31, 32, 33, 34]. One of the main advantages is that they are potential to capture images for a large area beyond single leaf and plant [30, 29, 6]. Relatively, those two sensors are generally put into UAVs (unmanned aerial vehicle) and aircraft to surveil many plants. However, their disadvantages are the non-trivial computations resulting from the many channels and inconvenience to use.

## 2.4. Image variation

In the age of traditional machine learning, engineers and researchers carefully consider data collection and thus the collected data are relatively small yet informative [10]. This situation has changed in the era of deep learning where the datasets become much larger yet non-informative. Sometimes,

datasets are collected without any specific objective in advance [10]. Analyzing these datasets is therefore essential and variation is arguable one of the most important for image-based datasets [35, 36, 11, 17, 6, 15]. The inspiration is to achieve decent generalization performance and a basic assumption of machine learning and deep learning is that the training and test datasets are in an identical and independent distribution (i.i.d) [37]. However, this assumption is not hold in many real-world application. Hence, we contend that understanding variation within the collected dataset is beneficial to making robust applications and this study focuses on the RGB image variation because of its prevalence in recent years.

Officially, image variations consist of inter-class, the diversity between two classes, and intra-class, the diversity within one class [17]. One of the basic assumption to distinguish plant diseases is that different diseases have different visual patterns even if they are similar [17]; otherwise, methods belonging to pattern recognition and classification fail. However, those diseases sharing some visual patterns, smaller inter-class image variation , are difficult to be recognized. Those images from one class but with disparate visual patterns, larger intra-class image variation , such as the flower colors in different growth stage, are also challenging to classify. From the perspective of agriculture, it is inevitable to have smaller inter-class and larger intra-class image variations. Therefore, deep learning methods are expected to mitigate the challenge. In general, those test images with similar image variations as the training images tends to receive high performance. By contrast, deep learning methods are expected to have poor generalization ability, such that models training only with the images with controlled imaging environments will have low performance when it is tested in the images with uncontrolled one [16, 15].

Main variations are summarized from the perspective of forming image variations in Table 2 and Figure 2 illustrates some image variations. Some variations are highly related. For example, those images for the plants in the field may have much larger diversity on illumination than the counterparts of greenhouse and laboratory. Similarly, canopies tends to have smaller scales than leaves and fruits. Besides, additional factors may be shared source of multiple variations such that person habits to take pictures result in diversity in scales and viewpoints. We emphasize that we group background as uncontrolled and controlled. For examples, leaves are put on the homogeneous materials such as papers in the laboratories or field. In the field, plant organs of interest can also be moved to have simple background. In contrast,

with the uncontrolled background, images are taken without considering the background. Therefore, backgrounds vary significantly and can be controlled when taking pictures for the plants in fields.

Figure 2: Examples of some image variations from the first to last row: disease stage, illumination, scale, and background. The images are taken from the corresponding datasets. In this paper, image background is grouped into three cases: simple (the first two images), medium (the third and fourth images), and complex (the last image).

<!-- image -->

## 2.5. Dataset splitting

In general, three datasets are adopted to develop deep learning models. Training datasets are to train models and validation datasets are taken to choose the optimal set of hyper-parameters such as the architecture of models. After training and validating, test datasets are finally used to check the performance of the trained models. In practical applications, the training and validation datasets are available in the training process whereas the test

Table 2: Main variations may cause image variations, partially summarized from [17].

Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Category: Plant, Variation: Type of plant such as tomato and apple. Plant organ including leaf, fruit, stem, flower, and canopy. Statue of plant such as florescence and disease such as with early symptom. Environment including field, greenhouse, and labora- tory..
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Category: Imaging process, Variation: Include illumination, scale, viewpoint, and background..
dataset is not available until users use the trained model. In such case, the test performance is not known and thus model developers can not assess the trained models. An alternative scheme is splitting a hold-out dataset as test before training models, resembling the real test data. Empirical results suggest that splitting results in different performance and thus the splitting strategies should be considered. To be clear, the collected dataset is referred as original one that will be split into three parts, training, validation, and test. The real test data from model users are distinguished from the split test dataset.

The most widely used strategy is random splitting that an image in the original dataset is randomly put into one of the three datasets. One of the main issues of this strategy is that multiple images taken for a same observation (a symptom of plant disease in nature) with only slightly differences can be assigned into the training and test dataset, by which the test performance could be overestimated. Moreover, this strategy elusively ignores the generalization challenge [12, 13, 14, 17], commonly existing in real-world applications, such that the real test data are not in the same distribution of the training dataset.

To mitigate the issues, splitting in spatial and temporal is appealing. For example, images taken in a place are put into either training or test [38]. Similarly, images on the same day or in the same year can be used for only one of the three datasets. In spite of being invariant to the type of plant diseases, the spatial and temporal factors explicitly allows that the training and test datasets are in different distributions. Although the strategies introduce new challenges, such as domain shift [17] as suggested in [38], it is worthwhile. In a nutshell, our objective is to achieve the best performance in real test

process, rather than neither in the training nor in the split test datasets. For example, a model trained in the collected data from several farms in this year is probably desired to be deployed in different farms for next couple of years. Beyond spatial and temporal, more things can be considered and are encouraged, such the images taken by same person who may be with certain habits to take pictures.

## 2.6. Annotation strategy

To begin with, we explicitly propose the rules for annotating datasets as follows:

- Annotations are difficult, time-consuming, and expensive to obtain.
- Annotations from human are with bias and noise.
- Images and their annotations should simultaneously satisfy the requirements of deep learning methods and agricultural tasks.

The first rule triggers the first question whether an image is annotated, termed existence of annotation. All images are fully labeled, which is the most case in the related public datasets. On the contrary, all images in a collected dataset can be not annotated completely. A more reasonable case is partially with annotations where some images are labeled whereas other images are not, mainly because the images are more easily available in a relative manner. In such scenario, two more factors should be considered: image level, whether an image should be annotated, and class level, how many images should be annotated for a class. We argue that the partially annotated datasets should be raised considering the characteristic of practical applications. Besides, theory also support it as a margin distribution of images can be useful with the learned conditional distribution or joint distribution, between labels and images [39].

Furthermore, bias and noise appear when human make decisions and the magnitude may be underestimated [1]. For example, the validation dataset of ImageNet [18], used to perform image classification of generic objects such as dogs and cats, has around 6% wrong labels [40]. Compared to this case, plant disease annotation requires more domain knowledge and may be more difficult to be precise. For example, three experts got only 85.9% accuracy on average when labeling 999 wheat images [41]. Noisy annotations in the training datasets could result in an unstable training process and inferior test

performance whereas the noises in validation datasets may lead to wrong selection of hyper-parameters [42]. Deep learning generally assumes that the annotations are correct and tends to obtain better performance if the annotation noise is smaller [42]. Based on this observation, making precise annotations is worthwhile yet requires more resources. For example, voting independent decisions from multiple experts tends to be beneficial [1]. In additional, Polymerase Chain Reaction (PCR) may also contribute [43]. We emphasize that we are not trying to say that the bias and noise should be avoided completely but that they should be noticed when annotating and degrade them considering the trade-off, as well as in the model training and validation stages.

The last law highlights the format of annotation, called levels of the annotation. In generic, image classification can be perform in image-level annotation, an image with an label. Multi-label image classification is also possible if an image has multiple plant diseases. However, bounding boxes can point out the location of every instance of plant disease in an image and thus is called instance level annotation. Moreover, pixel-level annotations are desired to the task of segmentation which assign a label for every pixel. For every level of annotation, extra strategies exist, such as the EEP [17], exclusion that every annotation includes only one specific visual pattern of plant disease, extensiveness that every plant disease in the images should have been annotated, and precision that annotation is expected to be precise for different tasks such as the correct labels and precise location of bounding boxes. Again, we highlight that incompatible formats of annotation become feasible with the concept of weak-supervision [44, 17] yet with negative impact on the test performance. Beside, new type of annotations have been emerged and new models may embrace different types of annotation.

Considering the advantages of localization task using object detection with weak image assumption than image classification and less annotation workload than segmentation [17], we give more details about it beyond the EEP [17] strategy. To be more specific, how can we give bounding box for different diseases in a consistent manner, as illustrated in Figure 3. In general, three independent strategies can be used to have bounding box. First, every instance of fruit or leaf with diseased symptoms is labeled, called global-level. The problem is that an instance may have multiple diseases and thus the corresponding bounding boxes will have diverse labels and include the healthy parts, which may confuse deep learning models or cause challenge to model optimization. Second, every single symptom gets a bounding box

Figure 3: Bounding box annotation strategies in object detection, useful for the localization task. Up first row: three strategies to give bounding box, global (light yellow) that covers one instance such as an instance of fruit or leaf; local (light blue) that covers local areas with dense and intensive symptoms; semi-global (dotted red) that is a trade off of previous two, covering local areas yet allowing a sparse symptoms such as the case in the first image. Up second row: recommended strategy, disease-adaptive, that different diseases may use either local or semi-global strategy. The global one is not recommended because an instance may include more than one type of diseases and may include healthy part. Down: inconsistent annotation when the bounding boxes for the same disease are given in different strategies in a dataset, which may confuse the deep learning model and result in optimizing issues. The picture is adapted from [45].

<!-- image -->

and the symptom is assumed to be dense without non-trivial gap, termed local level. In this case, many bounding boxes may exist in an instance, such as the third and fourth images in the first row of Figure 3, which makes annotation harder and more time-consuming. Besides, different annotators may have diverse definitions about the 'dense'. Third, semi-level is trade off of previous two, allowing a gap between symptoms, especially for those tiny ones but many. Based on our understanding and experimental results, an adaptive strategy [45] is recommended that different disease has different levels of annotation. Another elusive issue is the inconsistency mentioned by Andrew Ng in a video. The underlying is that different annotators or even same annotator in different time would use different level of bounding boxes, as compared of annotations 1 and 2 for same image in Figure 3. This inconsistency in training datasets gives different information to models resulting in unstable learning. In addition, inconsistency in test process may give us an inaccurate evaluation.

## 3. Public Plant Disease Recognition Datasets

Based on our preliminary survey, RGB images taken by handled cameras dominate in public plant disease recognition datasets. Other types of datasets are rarely utilized and public. Therefore, we aim to provide a survey on RGB images to recognize plant diseases in this section. We did not do a complete survey that is impossible to some extent and rather focus on those datasets with a relatively higher frequency of utilization or released recently, which suggests the tendency in this field. For a dataset, the following tags are considered:

- Dataset name. We will assign a name for the dataset if without a given in the original material. The datasets are default public available. Some partial public datasets are also included.
- Crop. If only one crop is included, their name is given. Otherwise, the number of crops is given.
- Number of classes. Disease classes and healthy one are included.
- Number of images. Only those images with public available annotations are counted.

- Image background (BG). We split the image background into three categories as shown in the last row in Figure 2. The simple one are taken in the environments of laboratory where the region of interest (RoI) are put on the controlled material. The complex one is taken in the field with complex background. The medium one is also taken in the field but the RoIs may be moved to have a simpler background. Their corresponding abbreviations are sim, med, cmpx.
- Machine learning (ML) task and official performance (PE). This paper focuses on three types of machine learning task as discussed before, image classification (clf), object detection (obj), segmentation (seg). A dataset may support more than one task. We only report official performance, either in the original publications or in the leaderboard of official challenges. Otherwise, N.A suggests not available.

Table 3 summarizes the related public datasets and our project is public in Github with more detailed information. Although we tried to do our best, some beneficial datasets may be not included and thus any new contribution is welcome. One of the main observations is lacking of enough descriptions about objectives and usages. As mentioned above, localization and quantitation analysis are also beneficial but few relevant datasets with relative high-quality are public available. Another observation is that decent performance is achieved in most of the datasets with reported performance. An exception that a model trained in the PlantVillage with simple image background suffers in the FieldPV dataset with different levels of background. Similar situation appears in the FieldPlant dataset. Besides, we found that no datasets are utilized by the majority of research and compared, except the PlantVillage dataset.

## 4. Future Direction of Plant Disease Recognition Datasets

- Stage one: verification where deep learning methods are verified to be useful to recognize plant diseases.
- Stage two: implementation where deep learning methods are deployed into real-world applications of plant disease recognition with decent performance.
- Stage three: connection where plant disease recognition using deep learning methods is connected to downstream applications.

Table 3: Overview of some public plant disease recognition datasets. Class, image, image BG, ML task, and PE suggest number of classes, number of images, image background, machine learning task, and official performance.

15

Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: Apple2020 [22], Crop: Apple, Class: 4, Image: 1,821, Image BG: med, ML task & PE: clf: 0.984 AUROC.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: Apple2021, Crop: Apple, Class: 6, Image: 18,632, Image BG: med, ML task & PE: clf: 0.883 F1.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PCApple2023, Crop: Apple, Class: 9, Image: 10,212, Image BG: med+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: ASDID [46], Crop: Soybean, Class: 8, Image: 9,648, Image BG: med+sim, ML task & PE: clf: 0.968 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: BRACOL [47], Crop: Coffee, Class: 5, Image: 1,747, Image BG: sim, ML task & PE: clf: 0.956 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: RoCoLe [48], Crop: Coffee, Class: 6, Image: 1,560, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: iCassava [49], Crop: Cassava, Class: 5, Image: 5,656, Image BG: med, ML task & PE: clf: 0.939 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CLDCMakerere, Crop: Cassava, Class: 5, Image: 21,397, Image BG: cmpx+med, ML task & PE: clf: 0.913 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CLDCAmanda [50], Crop: Cassava, Class: 6, Image: 2,249, Image BG: med, ML task & PE: clf: 0.930 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CLDD, Crop: Cassava, Class: 3, Image: 228, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CDRD [51], Crop: Cucumber, Class: 8, Image: 1,289, Image BG: med+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CucumberNegm, Crop: Cucumber, Class: 2, Image: 691, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PaddyDoctor [52], Crop: Rice, Class: 10, Image: 10,407, Image BG: cmpx, ML task & PE: clf: 0.990 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: Rice1426 [53], Crop: Rice, Class: 9, Image: 1,426, Image BG: cmpx+med+sim, ML task & PE: clf: 0.971 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: Rice5932 [54], Crop: Rice, Class: 4, Image: 5,932, Image BG: med, ML task & PE: clf: 0.984 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: HuyDoRice, Crop: Rice, Class: 4, Image: 3,355, Image BG: sim, ML task & PE: clf: 0.984 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: DhanShomadhan [55], Crop: Rice, Class: 5, Image: 1,106, Image BG: cmpx+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: WheatLong [41], Crop: Wheat, Class: 5, Image: 999, Image BG: cmpx, ML task & PE: clf: 0.971 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: WheatLeafDataset, Crop: Wheat, Class: 3, Image: 407, Image BG: med+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: GroundNutLeaf [56], Crop: Groundnut, Class: 5, Image: 3,058, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: MaizeCraze, Crop: Corn, Class: 6, Image: 2,355, Image BG: sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: BisqueCorn 1 2, Crop: Corn, Class: 2, Image: 1,785, Image BG: cmpx, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CornNLB [57], Crop: Corn, Class: 1, Image: 18,222, Image BG: cmpx, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: iBean, Crop: Bean, Class: 3, Image: 1,296, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: SoybeanMignoni [58], Crop: Soybean, Class: 3, Image: 6,410, Image BG: cmpx, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: TaiwanTomato, Crop: Tomato, Class: 6, Image: 622, Image BG: med+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: GLFD [59], Crop: Guava, Class: 5, Image: 527, Image BG: sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CitrusRauf, Crop: Citrus, Class: 10, Image: 759, Image BG: sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PlantVillage [23], Crop: 14, Class: 38, Image: 54,305, Image BG: sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: FieldPV [60], Crop: 14, Class: 38, Image: 665, Image BG: med+sim, ML task & PE: clf: 0.720 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PlantDocCls [61], Crop: 13, Class: 27, Image: 2,598, Image BG: cmpx+med+sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PlantConservation [62], Crop: 12, Class: 10, Image: 4,503, Image BG: sim, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: CCMT [63], Crop: 4, Class: 22, Image: 24,881, Image BG: med, ML task & PE: clf: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PDD271 [24], Crop: N.A, Class: 271, Image: 2,710, Image BG: cmpx+med, ML task & PE: clf: 0.855 Acc.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: PlantDocObj [61], Crop: 13, Class: 27, Image: 2,598, Image BG: cmpx+med+sim, ML task & PE: obj: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: NZDLPlantDiseaseV1 [64], Crop: 5, Class: 20, Image: 3,337, Image BG: med, ML task & PE: obj: 0.745 mAP.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: NZDLPlantDiseaseV2 [65], Crop: 8, Class: 28, Image: 3,039, Image BG: med, ML task & PE: obj: 0.932 mAP.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: FieldPlant [66], Crop: 4, Class: 31, Image: 5,156, Image BG: cmpx+med, ML task & PE: obj: 0.144 mAP.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: GrapevineDiseaseMalo, Crop: Grape, Class: 3, Image: 744, Image BG: cmpx, ML task & PE: obj: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: GrapevineDiseaseMalo, Crop: Grape, Class: 4, Image: 128, Image BG: cmpx, ML task & PE: seg: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: BRACOL [47], Crop: Coffee, Class: 2, Image: 1,560, Image BG: sim, ML task & PE: seg: N.A.
Según Plant Disease Recognition Datasets in the Age of Deep Learning: Challenges and Opportunities (2023), Dataset name: ATLDSD, Crop: Apple, Class: 5, Image: 1,641, Image BG: med+sim, ML task & PE: seg: N.A.
To probe the future direction, We declare three stages of plant disease recognition using deep learning. The first stage is straightforward and almost finished in recent years. However, the second and third stages are still in their infancy. Currently, few publications mentioned the successful implementation in real-world applications. One of the main reasons comes from the assumptions embraced by deep learning methods, that are generally not hold in real-world applications. From this perspective, existing datasets catered for the assumptions. Therefore, one of the future directions of plant disease recognition is to make datasets violating the assumptions, termed deep learning challenge-oriented dataset. Furthermore, we argue that recognition plant disease is not the final objective and should be connected with the downstream work, arriving the third stage. From such perspective, we argue that another future direction is to make the datasets oriented by downstream applications. Besides, achieving better performance is desired in general, two inspirations are discussed, multi-observation and large-scale datasets. The mentioned content are detailed in the following content with additional discussions.

## 4.1. Deep learning challenge-oriented dataset

Although decent performance is achieved in most datasets, the corresponding trained models may suffer when deploying them in real-world applications. One of the reasons is that the assumptions to achieve good performance when training in the existing datasets are not always held [17]. Violating those assumptions results in challenges to deploy the deep learning models. For example, a model trained in the datasets from several farms is desired to give superior results when deploying in other farms, termed spatial generalization . In a similar spirit, a model trained in the datasets collected in a time duration is desired to be decent when deploying in another time duration, termed temporal generalization . Additional disease-invariant characteristics are also expected to have no impacts. However, current datasets do not support this kind of verification. Formally, deep learning challengeoriented datasets are highlighted to test and develop models cater for plant disease recognition. Simultaneously, we argue that datasets should be with meta-data, such as position and time stamp. In the other words, current datasets elusively assume that something in the training and test datasets are shared [67]. For example, a new plant disease may exist in the test stage and is desired to be classified from the known classes that exist in the training dataset [67], the challenge termed open set recognition. Furthermore,

we highlight that realizing the assumptions of deep learning models and incorporating them into the dataset collection stage need the cooperation of researchers from agriculture and deep learning field. Please refer to detailed challenges from the datasets in [17].

## 4.2. Application-oriented dataset

From the perspective of agriculture, recognizing plant diseases may not be the final objective and downstream work may follow. For example, early visual pattern recognition is beneficial to make some remedies to reduce loss. Therefore, collecting such datasets is appealing. Although some papers aims to dedicate this issue, the definition of early disease recognition has no agreement. We contend that such data have two primary characteristics: pattern recognizable and remedies effective. One of the core assumptions embraced by deep learning models is that different plant diseases have their own patterns; otherwise they can not be distinguished. Considering that data modalities have heterogeneous advantages and disadvantages, selecting suitable input modality is essential. On the other hand, statues of diseases cause varying losses and difficulties to take remedies. In an extreme scenario, a plant disease explodes in a farm and plants may all die where recognizing the corresponding disease is not that kind of useful. More application objectives from agriculture field are possible. Although the objectives are from the agriculture, we highlight that trade off exist such as the case in early disease recognition, which requires the cooperation from engineers in deep learning field.

## 4.3. Multi-observation dataset

In general, human experts make superior decisions to recognize plant diseases by looking through multiple observations than single observations. Inspired by this situation, we contend that deep learning methods can also be raised with multi-observation. In a nut shell, multiple observations distribute different information. Multi-modal datasets refer to those datasets with various modalities for the same plant diseases. For example, given a plant disease leaf, various optical images and texts can be made. Besides, datasets can be in time-series , such as taking images for plant diseases in different time. Specially, visual patterns become more clear and easier to be recognized when diseases gradually involve. Time-series datasets may mitigate the challenge of early plant disease recognition. For images data, higher test performance can also be dedicated to multi-spatial datasets , such as taking

images in different scales and perspectives. For example, some plant diseases have different patterns in the front and back of leaves.

## 4.4. Large-scale dataset

Large-scale datasets tend to be beneficial for model generalization in many general computer vision tasks and datasets [68, 69, 70]. Therefore, collecting large-scale datasets for plant disease recognition is appealing and worthwhile although it is time-consuming, difficult, and expensive. One convincing manner is crowdsensing [71] by which related people in different locations take images and then upload them to a platform. Those images will be annotated by the community. In this way, the collected datasets have enormous variations and thus contribute to model generalization [17].

## 4.5. Discussion

Benchmark In recent years, plant disease recognition has witnessed a significant improvement [2, 3, 5, 7, 17], as well as the number of related publications. However, the relative comparison is relative lacking to evaluate different models in diverse applications. One of the main reasons is the shortage of benchmarks, public and widely used high-quality datasets. We argue that this kind of benchmarks will facilitate the community and speed up the deployment of deep learning methods in the real-world applications of plant disease recognition.

Meta-data is the documentary to describe data instances from different perspectives, usually with tags. Most of current relevant public datasets have only the types of plant disease. Other types of information are expected to be beneficial, such as the spatial and temporary tags. Those dataset with meta-data can be used for different applications by making new datasets.

Analysis of datasets In general, different applications have heterogeneous difficulties and challenges. Datasets show the faces of applications and therefore, analysis of datasets are essential to understand the applications and further to achieve a better performance. However, few datasets have corresponding analysis and one of the expected directions is automatic analysis, such as for intra- and inter-class image variations. Furthermore, dataset analysis can be used in an iterate way to make high-quality datasets.

Beyond plant disease recognition Recognizing plant disease is just one of the fundamental requirements to have decent crop yields. This objective may be further facilitated through incorporating recognition and more things. For example, plants may be infected by specific diseases or virus in

some conditions where finding the correlated factors are beneficial to prevent the plants from those diseases.

## 5. Conclusion

Although plant disease recognition has witnessed a significant improvement in recent years, its applications in real-world still surfer and one of the reasons stems from the datasets. Making a high-quality plant disease recognition dataset requires superior understandings in both agriculture field and deep learning. This study aimed to provide the perspective for the creation of plant disease recognition datasets. To depict them clearly, we first provided a systematic taxonomy for related datasets. We specially emphasize dataset splitting and annotation strategies that are few discussed in the literature and elusively suggest challenges in real-world applications. Further, RGB images are observed as the dominate input modality and an extensive summarization was provided. Finally, four kinds of dataset as future directions are described: deep learning challenge-oriented, application-oriented, multiobservation, and large-scale, with an additional discussion. We believe that this paper will enhance the understandings about plant disease recognition and their datasets and is beneficial to make new datasets with the objective, implementing deep learning methods in real-world applications. To facilitate the field, our project is public available and new datasets are encouraged.

## References

- [1] D. Kahneman, O. Sibony, C. R. Sunstein, Noise: a flaw in human judgment, Hachette UK, 2021.
- [2] A. K. Singh, B. Ganapathysubramanian, S. Sarkar, A. Singh, Deep learning for plant stress phenotyping: trends and future perspectives, Trends in plant science 23 (10) (2018) 883-898.
- [3] J. Liu, X. Wang, Plant diseases and pests detection based on deep learning: a review, Plant Methods 17 (2021) 1-18.
- [4] M. Xu, S. Yoon, Y. Jeong, D. S. Park, Transfer learning for versatile plant disease recognition with limited data, Frontiers in Plant Science 13 (2022) 1010981.

- [5] P. S. Thakur, P. Khanna, T. Sheorey, A. Ojha, Trends in vision-based machine learning techniques for plant disease identification: A systematic review, Expert Systems with Applications (2022) 118117.
- [6] M. Xu, Enhanced plant disease recognition with limited training dataset using image translation and two-step transfer learning, Ph.D. thesis, Jeonbuk National University (2023).
- [7] Z. Salman, A. Muhammad, M. J. Piran, D. Han, Crop-saving with ai: latest trends in deep learning techniques for plant pathology, Frontiers in Plant Science 14 (2023).
- [8] R. Krishna, Y. Zhu, O. Groth, J. Johnson, K. Hata, J. Kravitz, S. Chen, Y. Kalantidis, L.-J. Li, D. A. Shamma, et al., Visual genome: Connecting language and vision using crowdsourced dense image annotations, International journal of computer vision 123 (2017) 32-73.
- [9] P. Cui, S. Athey, Stable learning establishes some common ground between causal inference and machine learning, Nature Machine Intelligence 4 (2) (2022) 110-115.
- [10] J. Wright, Y. Ma, High-dimensional data analysis with low-dimensional models: Principles, computation, and applications, Cambridge University Press, 2022.
- [11] M. Xu, S. Yoon, A. Fuentes, D. S. Park, A comprehensive survey of image augmentation techniques for deep learning, Pattern Recognition (2023) 109347.
- [12] M. Arjovsky, L. Bottou, I. Gulrajani, D. Lopez-Paz, Invariant risk minimization, arXiv preprint arXiv:1907.02893 (2019).
- [13] Y. Bengio, Y. Lecun, G. Hinton, Deep learning for ai, Communications of the ACM 64 (7) (2021) 58-65.
- [14] A. Corso, D. Karamadian, R. Valentin, M. Cooper, M. J. Kochenderfer, A holistic assessment of the reliability of machine learning systems, arXiv preprint arXiv:2307.10586 (2023).
- [15] X. Wu, X. Fan, P. Luo, S. D. Choudhury, T. Tjahjadi, C. Hu, From laboratory to field: Unsupervised domain adaptation for plant disease recognition in the wild, Plant Phenomics 5 (2023) 0038.

- [16] F. A. Guth, S. Ward, K. McDonnell, From lab to field: An empirical study on the generalization of convolutional neural networks towards crop disease detection, European Journal of Engineering and Technology Research 8 (2) (2023) 33-40.
- [17] M. Xu, H. Kim, J. Yang, A. Fuentes, Y. Meng, S. Yoon, T. Kim, D. S. Park, Embracing limited and imperfect training datasets: opportunities and challenges in plant disease recognition using deep learning, Frontiers in Plant Science 14 (2023).
- [18] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, L. Fei-Fei, Imagenet: A large-scale hierarchical image database, in: 2009 IEEE conference on computer vision and pattern recognition, Ieee, 2009, pp. 248-255.
- [19] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Doll´ ar, C. L. Zitnick, Microsoft coco: Common objects in context, in: Computer Vision-ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13, Springer, 2014, pp. 740-755.
- [20] A. Fuentes, S. Yoon, S. C. Kim, D. S. Park, A robust deep-learningbased detector for real-time tomato plant diseases and pests recognition, Sensors 17 (9) (2017) 2022.
- [21] M. Xu, S. Yoon, A. Fuentes, J. Yang, D. S. Park, Style-consistent image translation: A novel data augmentation paradigm to improve plant disease recognition, Frontiers in Plant Science 12 (2022) 3361.
- [22] R. Thapa, K. Zhang, N. Snavely, S. Belongie, A. Khan, The plant pathology challenge 2020 data set to classify foliar disease of apples, Applications in plant sciences 8 (9) (2020) e11390.
- [23] D. Hughes, M. Salath´ e, et al., An open access repository of images on plant health to enable the development of mobile disease diagnostics, arXiv preprint arXiv:1511.08060 (2015).
- [24] X. Liu, W. Min, S. Mei, L. Wang, S. Jiang, Plant disease recognition: A large-scale benchmark dataset and a visual region and loss reweighting approach, IEEE Transactions on Image Processing 30 (2021) 2003-2015.

- [25] A. Fuentes, S. Yoon, D. S. Park, Deep learning-based phenotyping system with glocal description of plant anomalies and symptoms, Frontiers in Plant Science 10 (2019) 1321.
- [26] C. Wang, J. Zhou, Y. Zhang, H. Wu, C. Zhao, G. Teng, J. Li, A plant disease recognition method based on fusion of images and graph structure text, Frontiers in Plant Science 12 (2022) 731688.
- [27] Y. Cao, L. Chen, Y. Yuan, G. Sun, Cucumber disease recognition with small samples using image-text-label-based multi-modal language model, Computers and Electronics in Agriculture 211 (2023) 107993.
- [28] C. Zhang, J. Kong, D. Wu, Z. Guan, B. Ding, F. Chen, Wearable sensor: An emerging data collection tool for plant phenotyping, Plant Phenomics 5 (2023) 0051.
- [29] A.-K. Mahlein, Plant disease detection by imaging sensors-parallels and specific demands for precision agriculture and plant phenotyping, Plant disease 100 (2) (2016) 241-251.
- [30] E.-C. Oerke, A.-K. Mahlein, U. Steiner, Proximal sensing of plant diseases, Detection and diagnostics of plant pathogens (2014) 55-68.
- [31] T. Ad˜ ao, J. Hruˇ ska, L. P´ adua, J. Bessa, E. Peres, R. Morais, J. J. Sousa, Hyperspectral imaging: A review on uav-based sensors, data processing and applications for agriculture and forestry, Remote sensing 9 (11) (2017) 1110.
- [32] B. Lu, P. D. Dao, J. Liu, Y. He, J. Shang, Recent advances of hyperspectral imaging technology and applications in agriculture, Remote Sensing 12 (16) (2020) 2659.
- [33] B. Lu, Y. He, P. D. Dao, Comparing the performance of multispectral and hyperspectral images for estimating vegetation properties, IEEE Journal of selected topics in applied earth observations and remote sensing 12 (6) (2019) 1784-1797.
- [34] L. Wan, H. Li, C. Li, A. Wang, Y. Yang, P. Wang, Hyperspectral sensing of plant diseases: Principle and methods, Agronomy 12 (6) (2022) 1451.

- [35] A. Fuentes, D. H. Im, S. Yoon, D. S. Park, Spectral analysis of cnn for tomato disease identification, in: Artificial Intelligence and Soft Computing: 16th International Conference, ICAISC 2017, Zakopane, Poland, June 11-15, 2017, Proceedings, Part I 16, Springer, 2017, pp. 40-51.
- [36] D. Singh, N. Jain, P. Jain, P. Kayal, S. Kumawat, N. Batra, Plantdoc: A dataset for visual plant disease detection, in: Proceedings of the 7th ACM IKDD CoDS and 25th COMAD, CoDS COMAD 2020, Association for Computing Machinery, New York, NY, USA, 2020, p. 249-253. doi:10.1145/3371158.3371196 . URL https://doi.org/10.1145/3371158.3371196
- [37] V. Vapnik, Principles of risk minimization for learning theory, Advances in neural information processing systems 4 (1991).
- [38] S. Beery, G. Wu, T. Edwards, F. Pavetic, B. Majewski, S. Mukherjee, S. Chan, J. Morgan, V. Rathod, J. Huang, The auto arborist dataset: A large-scale benchmark for multiview urban forest monitoring under domain shift, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022, pp. 21294-21307.
- [39] Y. Bengio, A. Courville, P. Vincent, Representation learning: A review and new perspectives, IEEE transactions on pattern analysis and machine intelligence 35 (8) (2013) 1798-1828.
- [40] C. G. Northcutt, A. Athalye, J. Mueller, Pervasive label errors in test sets destabilize machine learning benchmarks, arXiv preprint arXiv:2103.14749 (2021).
- [41] M. Long, M. Hartley, R. J. Morris, J. K. Brown, Classification of wheat diseases using deep learning networks with field and glasshouse images, Plant Pathology 72 (3) (2023) 536-547.
- [42] G. Patrini, A. Rozza, A. Krishna Menon, R. Nock, L. Qu, Making deep neural networks robust to label noise: A loss correction approach, in: Proceedings of the IEEE conference on computer vision and pattern recognition, 2017, pp. 1944-1952.
- [43] M. R. Pereira, F. N. Dos Santos, F. Tavares, M. Cunha, Enhancing host-pathogen phenotyping dynamics: early detection of tomato bac-

terial diseases using hyperspectral point measurement and predictive modeling, Frontiers in Plant Science 14 (2023).

- [44] Z.-H. Zhou, A brief introduction to weakly supervised learning, National science review 5 (1) (2018) 44-53.
- [45] J. Dong, J. Lee, A. Fuentes, M. Xu, S. Yoon, M. H. Lee, D. S. Park, Data-centric annotation analysis for plant disease detection: Strategy, consistency, and performance, Frontiers in Plant Science 13 (2022) 1037655.
- [46] N. Bevers, E. J. Sikora, N. B. Hardy, Soybean disease identification using original field images and transfer learning with convolutional neural networks, Computers and Electronics in Agriculture 203 (2022) 107449.
- [47] J. G. Esgario, R. A. Krohling, J. A. Ventura, Deep learning for classification and severity estimation of coffee leaf biotic stress, Computers and Electronics in Agriculture 169 (2020) 105162.
- [48] J. Parraga-Alava, K. Cusme, A. Loor, E. Santander, Rocole: A robusta coffee leaf images dataset for evaluation of machine learning based methods in plant diseases recognition, Data in brief 25 (2019) 104414.
- [49] E. Mwebaze, T. Gebru, A. Frome, S. Nsumba, J. Tusubira, icassava 2019 fine-grained visual categorization challenge, arXiv preprint arXiv:1908.02900 (2019).
- [50] A. Ramcharan, K. Baranowski, P. McCloskey, B. Ahmed, J. Legg, D. P. Hughes, Deep learning for image-based cassava disease detection, Frontiers in plant science 8 (2017) 1852.
- [51] N. Sultana, S. B. Shorif, M. Akter, M. S. Uddin, A dataset for successful recognition of cucumber diseases, Data in Brief (2023) 109320.
- [52] Petchiammal, B. Kiruba, Murugan, P. Arjunan, Paddy doctor: A visual image dataset for automated paddy disease classification and benchmarking, in: Proceedings of the 6th Joint International Conference on Data Science &amp; Management of Data (10th ACM IKDD CODS and 28th COMAD), 2023, pp. 203-207.

- [53] C. R. Rahman, P. S. Arko, M. E. Ali, M. A. I. Khan, S. H. Apon, F. Nowrin, A. Wasif, Identification and recognition of rice diseases and pests using convolutional neural networks, Biosystems Engineering 194 (2020) 112-120.
- [54] P. K. Sethy, N. K. Barpanda, A. K. Rath, S. K. Behera, Deep feature based rice leaf disease identification using support vector machine, Computers and Electronics in Agriculture 175 (2020) 105527.
- [55] M. F. Hossain, Dhan-shomadhan: A dataset of rice leaf disease classification for bangladeshi local rice, arXiv preprint arXiv:2309.07515 (2023).
- [56] M. Aishwarya, A. P. Reddy, Dataset of groundnut plant leaf images for classification and detection, Data in Brief 48 (2023) 109185.
- [57] T. Wiesner-Hanks, E. L. Stewart, N. Kaczmar, C. DeChant, H. Wu, R. J. Nelson, H. Lipson, M. A. Gore, Image set for deep learning: field images of maize annotated with disease symptoms, BMC research notes 11 (1) (2018) 1-3.
- [58] M. E. Mignoni, A. Honorato, R. Kunst, R. Righi, A. Massuquetti, Soybean images dataset for caterpillar and diabrotica speciosa pest detection and classification, Data in Brief 40 (2022) 107756.
- [59] A. Rajbongshi, S. Sazzad, R. Shakil, B. Akter, U. Sara, A comprehensive guava leaves and fruits dataset for guava disease recognition, Data in Brief 42 (2022) 108174.
- [60] P. Gui, W. Dang, F. Zhu, Q. Zhao, Towards automatic field plant disease recognition, Computers and Electronics in Agriculture 191 (2021) 106523.
- [61] D. Singh, N. Jain, P. Jain, P. Kayal, S. Kumawat, N. Batra, Plantdoc: A dataset for visual plant disease detection, in: Proceedings of the 7th ACM IKDD CoDS and 25th COMAD, 2020, pp. 249-253.
- [62] S. S. Chouhan, U. P. Singh, A. Kaul, S. Jain, A data repository of leaf images: Practice towards plant conservation with plant pathology, in: 2019 4th International Conference on Information Systems and Computer Networks (ISCON), IEEE, 2019, pp. 700-707.

- [63] P. K. Mensah, V. Akoto-Adjepong, K. Adu, M. A. Ayidzoe, E. A. Bediako, O. Nyarko-Boateng, S. Boateng, E. F. Donkor, F. U. Bawah, N. S. Awarayi, et al., Ccmt: Dataset for crop pest and disease detection, Data in Brief (2023) 109306.
- [64] M. H. Saleem, J. Potgieter, K. M. Arif, A performance-optimized deep learning-based plant disease detection approach for horticultural crops of new zealand, IEEE Access 10 (2022) 89798-89822.
- [65] M. H. Saleem, J. Potgieter, K. M. Arif, A weight optimization-based transfer learning approach for plant disease detection of new zealand vegetables, Frontiers in Plant Science 13 (2022) 1008079.
- [66] E. Moupojou, A. Tagne, F. Retraint, A. Tadonkemwa, D. Wilfried, H. Tapamo, M. Nkenlifack, Fieldplant: A dataset of field plant images for plant disease detection and classification with deep learning, IEEE Access 11 (2023) 35398-35410.
- [67] Y. Meng, M. Xu, H. Kim, S. Yoon, Y. Jeong, D. S. Park, Known and unknown class recognition on plant species and diseases, Computers and Electronics in Agriculture 215 (2023) 108408. doi:https://doi.org/10.1016/j.compag.2023.108408 .
6. URL https://www.sciencedirect.com/science/article/pii/S0168169923007962
- [68] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, D. Amodei, Scaling laws for neural language models, arXiv preprint arXiv:2001.08361 (2020).
- [69] X. Zhai, A. Kolesnikov, N. Houlsby, L. Beyer, Scaling vision transformers, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022, pp. 12104-12113.
- [70] M. Xu, S. Yoon, C. Wu, J. Baek, D. S. Park, Plantclef2023: A bigger training dataset contributes more than advanced pretraining methods for plant identification, Working Notes of CLEF (2023).
- [71] A. Coletta, N. Bartolini, G. Maselli, A. Kehs, P. McCloskey, D. P. Hughes, Optimal deployment in crowdsensing for plant disease diagnosis in developing countries, IEEE Internet of Things Journal 9 (9) (2020) 6359-6373.