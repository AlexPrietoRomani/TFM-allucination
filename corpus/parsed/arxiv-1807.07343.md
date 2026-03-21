---
id: arxiv-1807.07343
title: Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks
year: 2018
country: Internacional
source: ArXiv (cs.CV)
doc_type: Artículo científico
language: en
tags:
  - Botrytis
  - vid
  - especies invasoras
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks

Pierre Barr´ e 1 , Katja Herzog 3 , Rebecca H¨ ofle 3 , Matthias B. Hullin 2 , Reinhard T¨ opfer 3 and Volker Steinhage 1 *

1 University of Bonn, Institute of Computer Science IV, Endenicher Allee 19A, Bonn 53115, Germany

2 University of Bonn, Institute of Computer Science II, Endenicher Allee 19A, Bonn 53115, Germany

3 Julius K¨ uhn-Institut(JKI)-Federal Research Centre of Cultivated Plants, Institute for Grapevine Breeding Geilweilerhof, Siebeldingen 76833, Germany

Author to whom correspondence should be addressed: steinhag@cs.uni-bonn.de

## Abstract

In viticulture the epicuticular wax as the outer layer of the berry skin is known as trait which is correlated to resilience towards Botrytis bunch rot. Traditionally this trait is classified using the OIV descriptor 227 (berry bloom) in a time consuming way resulting in subjective and error-prone phenotypic data. In the present study an objective, fast and sensor-based approach was developed to monitor berry bloom. From the technical point-of-view, it is known that the measurement of different illumination components conveys important information about observed object surfaces. A Mobile Light-Separation-Lab is proposed in order to capture illumination-separated images of grapevine berries for phenotyping the distribution of epicuticular waxes (berry bloom). For image analysis, an efficient convolutional neural network approach is used to derive the uniformity and intactness of waxes on berries. Method validation over six grapevine cultivars shows accuracies up to 97.3%. In addition, electrical impedance of the cuticle and its epicuticular waxes (described as an indicator for the thickness of berry skin and its permeability) was correlated to the detected proportion of waxes with r=0.76. This novel, fast and non-invasive phenotyping approach facilitates enlarged screenings within grapevine breeding material and genetic repositories regarding berry bloom characteristics and its impact on resilience towards Botrytis bunch rot.

Keywords Convolutional Neural Networks (CNN); Direct and Global Illumination; Classification; Vitis vinifera ; Berry Bloom; Botrytis cinerea ; Plant Phenotyping

## 1 Introduction

The risk for Botrytis bunch rot, a disease caused by Botrytis cinerea Pers., is seriously increasing in viticultural regions especially when high air humidity or prolonged rain cause in persistent moisture on grapevine berry surfaces. Botrytis infestation then reduces grape yield and the quality of wines due to off-flavors or reduced wine stability in susceptible grapevine cultivars [1]. Besides climatic conditions, susceptibility of grapes against Botrytis bunch rot is mainly influenced by morphological properties like the bunch compactness, canopy structure as well as the thickness of the berry skin and hydrophobic characteristics of the berry cuticle ([2], [3], [4], [5], [6]). The cuticle and its epicuticular wax layer hereby represents the outer layer of the grapevine berries (cf. figure 1), it shows semi-crystalline to crystalline structure and influences the retention of pesticides, the hydrophobic characteristics of the grapevine berry surface and the adhesive ability of plant pathogens (citation overview is given by [3]). Furthermore, it is described as important economic feature: the berry bloom imparts a frosted appearance to the berry, which is considered attractive and desirable by consumers of table grapes [7]. The berry epicuticular waxes influences the oviposition of European grapevine moth [8] but interestingly they are also scattering light. For the grapevine berry cuticle, classification of phenotypes by traditional visual estimations is only possible for the appearance of the wax layer (OIV 227). This method is very time consuming and phenotypic data are subjective with low resolution which renders the differentiation between visibly similar genotypes hardly possible. Thus, more precision phenotyping methods are needed which are often based on labor-intensive light or scanning electron microscopy ([3], [4], [9]) as well as expensive and time-consuming chemical analyses ([8], [10]).

Figure 1: Exemplary bunches of the grapevine cultivar Morio Muskat (a) and the breeding strain Seibel 7511 (b) . The berries of Morio Muskat show no epicuticular wax layer (c) and the berries of Seibel 7511 show uniform and intact epicuticular wax layer (d)

<!-- image -->

Laborious phenotyping methods are not feasible in grapevine research and breeding where berries of several hundreds of genotypes have to be evaluated in a short time. Regarding objective and highthroughput phenotyping techniques, Herzog et al. [6] developed a sensor-based method in order to characterize the thickness and permeability of grape berry cuticles by measuring the electrical impedance. High impedance is described as an indicator for thick berry cuticle and berry bloom [6]. Within this I-sensor the cuticle and the epicuticular wax layer as well as the epidermal cell layer of berries are located between two electrically conducting compartments: (1) berries placed on a NaCl solution and (2) an electrode within the berry flesh [11]. As described by [11], the impedance as its own is the sum of the real resistor (permeability of the cuticle, the wax layer and air) and the imaginary resistor (thickness of the cuticle, the wax layer and air). [6] observed a high negative correlation between the grape berry impedance of the cuticule and its epicuticular waxes and the susceptibility of berries to Botrytis bunch rot. The measurement of impedance is a point measurement and minimal-invasive due to a spotty puncture. The distribution, the uniformity or the intactness of epicuticular waxes as very important features cannot directly be determined due to point measurements. Subsequent infection tests on the suceptibility towards Botrytis bunch rot are not feasible because of the puncture which functions as portal of entry for pathogene.

In addition to the non-imaging impedance as indicator for thickness of the grape berry cuticle, imaging methods will enable objective characterization of the appearance and uniformity of berry bloom on the berry surface. Light-separation methods are useful to recognize parts or structures that consumer cameras usually cannot distinguish, e.g. surface texture.

From materials science, it is known that different illumination components will be reflected in different ways from the illuminated object surfaces. Therefore, different reflectance components convey important information about the observed object surfaces that cannot be inferred from their sum. Recently, several approaches were published separating illuminations and reflection components ([12], [13], [14], [15], [16], [17], [18]). In the present study, we will focus on polarization-based and pattern-based approaches that are most relevant to the scope of this contribution. One key observation is that specular reflections become polarized, i.e., the light waves are aligned in one single plane, while in turn, diffuse reflections are basically unpolarized. Generally, specular reflections are caused by smooth surface patches while diffuse reflections are caused by rough surface patches. Wolff and Boult [13] present a polarization reflectance model showing that all polarization-based methods follow from this model. They demonstrate the capability of polarization-based methods to segment material surfaces according to varying levels of relative electrical conductivity, especially by distinguishing non-conducting dielectrics from conductive metals. Nayar et al. [16] use controlled illumination to separate direct from global reflections. More precisely, they employ high frequency illumination patterns derived by chessboard-like arrangements of transparent and opaque filter cells. In general, direct reflections are due to direct illumination of surface patches by the light source. Global reflections are due to different physical phenomena including interreflection of light between different scene points but also subsurface scattering within the medium beneath the object surface. Garces et al. [18] present an outdoor upgrade of Nayar's method [16] by employing the sun and sky lighting as incident light sources and creating high frequency patterns by casting a stick over the observed objects.

In the given study, we present and evaluate a novel sensor- and computer-based phenotyping method combining the concept of light-separation and deep learning in order to provide an automated phenotyping of epicuticular waxes on the grapevine berry surface, the berry bloom. We used the polarization-based approach of Wolff and Boult [13] and the pattern-based approach of Nayar et al. [16] to separate illumination and reflections into four channels showing specular reflections, diffuse reflections, direct reflections and global reflections. These four image channels characterize surface patches in terms of smoothness and depth of reflection (surface or sub-surface reflections) and are used to measure epicuticular waxes of grapevine berries. To facilitate light-separation within image capture, we designed and built a mobile device, the LSL ( L ight S eparation L ab) for image capture of grapevine berries employing both lightseparation methods.

While common image analysis approaches to visual detection and measurement of objects include serious feature engineering, i.e. the employment of domain-specific knowledge to create descriptive features for localizing the berries and measuring the epicuticular waxes, deep learning approaches use convolutional neural networks (CNN) that allow for an automated feature derivation. CNNs were successfully applied in plant sciences [19], especially in order to study plant diseases and in particular leaf lesions. Lu et al.

[20] developed a deep-learning method to detect six crop diseases. Mohanty et al. [21] detect 38 leaf diseases from the PlantVillage data set [22] using two approaches: an AlexNet-based CNN [23] and the GoogLeNet CNN with the inception architecture [24]. Since they used the same data set, the last work can be directly related with Wang et al. [25] using the concept of transfer learning. Sladojevic et al. [26] collected leaf images from the internet which are classified under thirteen kinds of diseases and used a CNN network based on AlexNet [23].

The major objective of the present study was the combination and evaluation of light-separation methods with fast and high-resolution learning approaches using Convolutional Neural Networks (CNN) in order to facilitate an automated phenotyping of epicuticular waxes on the grapevine berry surface, the berry bloom. First, we will show the proof-of-concept that the pattern-based and polarization-based lightseparation methods improve the accuracy of the detection of berry and its epicuticular waxes. Secondly, we will show the results on precision and validity of our system by computing the proportion of epicuticular waxes on the detected berry surface and the correlation of these phenotypic data to impedance measurements. Thirdly, we will analyze the correlation between impedance measurements on the one hand and the derived surface proportion of the epicuticular waxes for validation.

## 2 Results

In the present study, we employed a workflow of two CNNs: Hereby, standard RGB images and four separated reflection channels were used in the first shifting pattern recognition CNN for detection and localization of berries in images resulting in Areas of Interest (AoI). The same data (RGB and reflection channels) were used in the second CNN in order to segment the detected AoI according to the presence of epicuticular wax. The most important advantage of the developed CNN-based approach is that both CNNs automatically learned to derive appropriate features over the given input channels. We assumed that electrical impedance of the cuticle and its epicuticular wax is related to the presence of the wax layer and would thus be useful as reliable reference parameter. Accordingly, the impedance of each investigated berry (cf. [6]) was measured after the LSL-based image capture.

## 2.1 Detection of the Berry and Its Epicuticular Waxes

Image capture with the the LSL (Light Separation Lab) generates five outputs: (1) a standard color RGB image without any light separation; (2) a color image showing specular reflections; (3) a color image showing diffuse reflections, (4) a color image showing direct reflections; (5) a color image showing global reflections. We evaluated the results of berry detection and quantification of epicuticular waxes on the berry surface with four input modes: (I) only standard color images (1) as baseline for comparison; (II) color images (2) and (3) generated by polarization-based light separation; (III) color images (4) and (5) generated by pattern-based light separation; (IV) input of all images (1) to (5). Both CNNs for berry detection and quantification of epicuticular waxes were evaluated using k-fold cross-validation with k = 3 based on 270 berry images captured by the LSL (4.1). In each run of the 3-fold cross-validation 180 images are used for training and 90 images are used for evaluation. More precisely, about 18,000,000 labeled pixels are extracted using a semi-automated annotation tool that allows labeling all pixels in rectangular crops in one step. The 18,000,000 pixels are labeled as berry pixels or background pixels. In a similar way, about 1,800,000 labeled pixels are extracted that are labeled as wax pixels, non-wax pixels (i.e., pixels depicting berry surface without wax) or background pixels (i.e., pixels depicting background, lignifications or the pedicle of the berry). The extraction of labeled pixels for the evaluation of wax measurement is more difficult due to smaller crops showing the same classes of pixels. Each run of the 3-fold cross-validation of the CNN-based berry detection employs 12,000,000 labeled pixels taken from the 180 training images for training and 6,000,000 labeled pixels taken from the 90 test images for evaluation. As final result, we derive the averaged accuracy of the pixel classification over these three runs. Analogously, each run of the 3-fold cross-validation of the CNN-based wax measurement employs 1.200,000 labeled pixels for training and 600,000 labeled pixels for evaluation. Table 1 shows the averaged accuracy values for berry detection and wax quantification as well as the averaged times

for image capture.

The highest accuracies are obtained by using all inputs (i.e., input mode IV) showing improvements of the accuracy values of 6.6% and 8.1% compared to the baseline mode I (only standard color images). The best accuracy values of a stand-alone separation method are obtained by using only the pattern-based light separation showing improvements of 4,9% and 7,4% compared to the baseline mode. Generally, we can observe that each of the light separation approaches improve the accuracy values for berry detection and wax quantification compared to the baseline mode. On the other hand, the time required by pattern-based light separation approach is a magnitude higher compared to the time requirement of the polarized-based light separation approach.

Table 1: Averaged accuracy values for berry detection and epicuticular waxes quantification as well as average time requirements for image capture.

Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Input Mode: (I) Standard, Accuracy Berry Detection: 0,913, Accuracy Wax Detection: 0,892, Capture Time: ∼ 2-3 sec.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Input Mode: (II) Polarization-based separation, Accuracy Berry Detection: 0,970, Accuracy Wax Detection: 0,945, Capture Time: ∼ 2-3 sec.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Input Mode: (III) Pattern-based separation, Accuracy Berry Detection: 0,962, Accuracy Wax Detection: 0,966, Capture Time: ∼ 15 sec.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Input Mode: (IV) Standard + pattern-based + polarization-based separation, Accuracy Berry Detection: 0,979, Accuracy Wax Detection: 0,973, Capture Time: ∼ 19-21 sec.
## 2.2 Quantification of Epicuticular Waxes

To characterize the uniformity and intactness of the epicuticular waxes, we derive a quantification of pixels depicting epicuticular waxes on a berry's surface. Figure 2 shows the visualization of the areas covered by epicuticular waxes detection.

Figure 2: Quantification of epicuticular waxes (green) using the pattern-based light-separation method. Blue pixels depict background, lignification or pedicle within the area of interest. Red pixels depict regions of the berry surface without epicuticular waxes. Top row: standard color images. Middle row: Manually generated ground truth in order to visually compare with the estimated classification (Bottom row).These ground truths are not used to train the CNN. From left to right: berries of the cultivars Morio Muskat, Dakapo, Seibel 7511, Sauvignon Blanc, Cabernet Sauvignon and Riesling.

<!-- image -->

As expected the cultivar Morio Muskat shows the lowest proportion of wax and thus, the lowest amount of berry bloom. The most consistent layer of epicuticular waxes was observed on berries of Cabernet Sauvignon, followed by Seibel 7511 with only small interruptions in the berry bloom.

Figure 3: (a) Distribution of the proportion of epicuticular waxes on the berry surface per cultivar. (b) Distribution of the impedance Z rel CW on the berry surface per cultivar. With N = 45 berries for each cultivar, except for Cabernet Sauvignon in (b) where N = 44 (see Supplementary Table S1).

<!-- image -->

The left box plot in figure 3 (a) depicts the distributions of the proportion of epicuticular waxes on the berry surfaces for each cultivar derived by the k-fold cross-validation with k = 3 on the sample of 270 berry images (cf. section 2.1) using the combination of all inputs, i.e., input mode IV. As visible in figure 3 (a) , the detected proportion of the berry surface with epicuticular waxes partially differentiates considerable between the investigated cultivars. In contrast to the estimated OIV 227 classification (Table 2, section 4.1) the highest proportion of epicuticular wax was obtained on berries of Cabernet Sauvignon, the proportion on berry surfaces of Riesling, Sauvignon Blanc and Dakapo was comparable. The variance of detected proportion of wax was larger for Dakapo and Riesling in comparison to Sauvignon blanc. Similar observations were obtained for the thickness of the cuticle, the impedance Z rel CW . Both boxplots indicate a positive correlation between relative impedance values and proportions of epicuticular waxes. The relative impedance of the cuticle waxes is described as an indicator for the thickness and permeability of the cuticle and thus, is described as indicator for resilience towards Botrytis bunch rot [6]. The right box plot in figure 3 (b) depicts the distributions of the impedance values Z rel CW on the berry surfaces for each cultivar. Figure 4 illustrates the relation between electrical impedance and the detected proportion of epicuticular waxes (computed with classification results using input mode IV) over the cultivars. The linear relation between the distribution of waxes and the electrical impedance indicates that both phenotypic traits (thickness and distribution/ uniformity) are linked.

Figure 4: Correlation plot of the measured relative impedance Z rel CW and the proportion of epicuticular waxes per cultivars using images of the combination of the three methods. N=269 investigated berries. Using the pattern-based method we obtain a correlation value of R = 0 , 738 with 1 . 742 × 10 -47 and using the polarization-based method a correlation value of R = 0 . 761 with 3 . 564 × 10 -52

<!-- image -->

## 3 Discussion

The aim of the present study was the development of an automated and mobile light-separation camera system and the development of an automated CNN-based image analysis approach. We assumed that pattern-based and polarization-based light-separation methods are promising imaging tools in order to characterize the distribution and proportion of the grape berry epicuticular waxes. The best accuracy of the CNN for the berry detection could be observed with the application of the polarization-based method which needs only few seconds. Using this light-separation method for epicuticular wax detection, the accuracy decreased to 0.95 in comparison to the input mode IV (0.97). From the practical point-ofview, the accuracy of both is reliable enough for further investigations and phenotypic screenings. More important now is the time which is needed for single measurements because of the limited period of only a few days when the berry epicuticular wax can be phenotyped. The polarization-based method, however, seems to be the most promising manner in order to screen large samples e.g. within breeding programs. Single light reflection components captured during light-separation process contain also important information about surface characteristics of grapevine berries especially about its epicuticular waxes, the berry bloom. This phenotypic information is successfully classified with the deep-learning method and so the proportion of epicuticular waxes are computed. We achieved positive correlations between the relative impedance and the proportion of epicuticular waxes. This correlation indicates the linear relation between the thickness and permeability of the cuticle (impedance) and the homogeneity of the wax distribution. Both characteristics are described as important traits to increase the resilience of cultivars and thus, the acquisition of both traits are promising to improve the selection procedure within grapevine breeding purposes regarding thickness and quality of berry bloom. The combination of both sensor-based approaches (visible and non-visible) will improve existing prediction models as described by [6] or [11].

We detected different proportions of waxes between the exemplary investigated cultivars. The intactness of the wax layer depends on the density of the bunches, i.e. normal bunches (OIV 204 =5) like

the bunches of Cabernet Sauvignon, show a more consistent wax layer in comparison to cultivars like Riesling showing dense bunches. In dense bunches the berries come into contact with each other which interrupts the wax layer [9]. Regarding the relation of a thick, consistent epicuticular wax and an increased resilience towards Botrytis bunch rot, further investigations are needed. The application of the presented method enables non-invasive phenotyping of individual berries and subsequently, the usage of the same berries for Botrytis infection test under controlled lab conditions [27]. The system defines also a refined approach to measure quality and quantity of epicuticular waxes which is a good indicator for vulnerability to Botrytis bunch rot. In addition, the application of the developed light-separation system could be extended due to the screening of genetic resources showing different wax compositions as shown by [8]. The chemical analysis of such wax compositions is very time-consuming and expensive, it is not feasible to investigate wax content on single berry level thus the presented method may be a promising tool to detect different berry bloom characteristics due to different wax compositions. However, grapevine breeding purposes require (field) screenings of large breeding population, genetic repository or seedlings with more than 50,000 plants. The light-separation method is a promising tool for high-throughput applications in the field. For this, the first step would be to capture several berries at once and then part of wine grapes instead of a single berry per image, which requires to adapt berry and epicuticular waxes methods, applied a full-segmentation process such as by [28]. Through this new approach, images of whole grapes can be captured by enlarging the LSL to produce a sufficiently light scene over the whole grape. Secondly, the light-separation methods have to be adjusted to outdoor conditions, using for example approaches as described by [18] or build a larger LSL that cover whole vines to neutralize the natural light. Finally, this field version of the LSL could be mounted on a mobile platform such as the PhenoBOT [29] or Phenoliner [30] to obtain as much information as possible with light-separation-methods.

## 4 Data and Methods

First, we will describe in more detail the generation of our sample set of 270 berry images captured by the LSL (cf. section 4.1). Secondly, we will briefly explain the main principles of pattern and polarizationbased light-separation (cf. section 4.2). Thirdly, we will present the hardware and software aspects of the technical implementation of the LSL (cf. section 4.3 and section 4.4). Finally, we report relevant specifications of the architecture as well as of the training and evaluation settings of both convolutional neural networks for berry detection and epicuticular wax quantification (cf. 4.5).

## 4.1 Data

Our sample set of 270 berry images was captured using the mobile LSL at the Julius K¨ uhn-Institute (JKI), Institute for Grapevine Breeding Geilweilerhof, Siebeldingen in Rhineland-Palatinate, Germany. The LSL-based capturing of the berry images was part of an overall measurement campaign at the JKI also including impedance measurements of the cuticle and its epicuticular waxes as additional objective phenotypic data. This measurement campaign included berries from six cultivars (also cf. figure 5), which are listed in table 2.

Figure 5: Overview of the six cultivars. From left to right and top to bottom: Morio Muskat, Dakapo, Seibel 7511, Sauvignon blanc, Cabernet Sauvignon, Riesling.

<!-- image -->

Table 2: The six cultivars and their respective descriptors OIV 204 (bunch density) and OIV 227 (berry bloom) (cf. [31]) and the estimated susceptibility towards Botrytis bunch rot.

Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: Morio Muskat Dakapo Seibel 7511 Sauvignon Blanc Riesling, OIV 204: 9, OIV 227: 1, Susceptibility towards Botrytis bunch rot: highly susceptible (9) medium susceptible (5) resilient (1) medium susceptible (5) resilient (1) susceptible (7).
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: 7, OIV 204: 5.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: 5, OIV 204: 7.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: 7, OIV 204: 5.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: Cabernet Sauvignon, OIV 204: 5, OIV 227: 5.
Según Automated Phenotyping of Epicuticular Waxes of Grapevine Berries Using Light Separation and Convolutional Neural Networks (2018), Cultivar: 7, OIV 204: 3.
Six different grapevine cultivars (table 2 and figure 5) were selected due to their berry bloom (OIV 227) and their susceptibility towards Botrytis bunch rot. All cultivars show compact bunch structure (OIV 204). Data acquisition was done in three tiers, each tier dealing with fifteen berries of each cultivar. Therefore, we acquired data from ninety berries per tier and 270 berries in total. All image samples were captured with LSL at the same day yielding for each berry one standard RGB image (baseline reference) and four light separated RGB images showing specular reflections, diffuse reflections, direct reflections, and global reflections, respectively (cf. section 2.1 and table 1).

## 4.2 Light Separation Methods

The pattern-based method of Nayar et al. [16] generates high frequency binary illumination patterns derived by chessboard-like arrangements of transparent and opaque filter cells positioned in front of the illumination source. While the light can pass the transparent filter cells it is blocked by the opaque filter cells. A light ray passing a transparent filter cell is part of the direct illumination by the source and will cause direct reflections on object surfaces. A patch of an object surface that is not illuminated directly from the light source (because it is shadowed due to an opaque filter cell) shows only global reflections caused by light rays that are reflected from other illuminated scene surfaces and by subsurface scattering within the medium beneath the object surface (cf. fig. 6). Of course, the directly illuminated surface patches receive also global illumination. Therefore, for all surface patches, the total radiance measured at a camera pixel is the sum of the direct and global components: I = I Global + I Direct .

In theory, two images of the scene taken with such a binary illumination pattern and its complementary binary pattern (transparent filter cells are now opaque transparent filter and vice versa) are sufficient to estimate the direct and global components for all surface patches (cf. equations 1 and 2 in section 4.4.1). The direct reflections contain most surface information, i.e., about a berry's cuticle and its epicuticular waxes while the global reflections contain most subsurface information, like a berry's color appearance.

Figure 6: Direct and global illumination components. Measuring different illumination components of an object conveys information about the object's surface that cannot be inferred from their sum.

<!-- image -->

The polarization-method uses linear polarization filters to obtain two images called perpendicular image and parallel image. A linear polarization filter confines waves to only one plane. Parallel images are acquired by placing one linear polarization filter in front of the camera and a second one at the light source, where both filters show the same orientation (cf. fig. 7 (a) ). The perpendicular image in turn is derived by choosing perpendicular orientations of both filters (cf. fig. 7 (b) ). A pair of parallel and perpendicular images allows deriving the diffuse reflections and the specular reflections (cf. equations 3 and 4 in section 4.4.1). Generally, specular reflections are caused by smooth surface patches (indicating no or little epicuticular waxes) while diffuse reflections are caused by rough surface patches (indicating epicuticular waxes).

Figure 7: The polarization method is used to derive a parallel image and a perpendicular image. For both cases, the light from the illumination source is first polarized with linear polarized filter. This polarized light is then reflected in a unpolarized way from rough object surface patches (diffuse reflection) but it is reflected in a polarized way from smooth surface patches maintaining the polarization orientation (specular reflection). All reflected light is then polarized by a second filter at the front of the camera. (a) In the case of parallel oriented filters both types of reflections, i.e., diffuse and specular reflections are passed to the camera. (b) In the case of perpendicular oriented filters only the diffuse reflection can pass the filter to the camera.

<!-- image -->

## 4.3 LSL (Light Separation Lab) and I-Sensor (Impedance Sensor)

We designed the L ight S eparation L ab (LSL) to create a mobile solution for image capture including light-separation. The light in the LSL is generated by a DLP R © LightCrafter TM Evaluation Module from Texas Instruments and the camera used is a Flea3 (FL3-U3-88S2C-C) camera from FLIR. The Light Separation Lab shows four components (see figure 8):

- a scaffold for camera and beamer (A)
- a wheel for the polarization filter (B)
- a camera housing (C)
- a stepper motor (D)

Figure 8: Main components of the LSL. (a) Technical sketch of the LSL with a scaffold for camera and beamer (A), the rotatable wheel for the polarization filters (B), the camera housing (C), and a screw fixed on the motor (D). (b) Constructed prototype of LSL controlled by a laptop.

<!-- image -->

The scaffold positions camera and beamer next to each other. Thus, each of the three windows of the polarization wheel can be placed in front of both: camera and beamer. The polarization wheel is composed of three windows (cf. fig. 9): (1) one window without any filter (used when applying the pattern-based separation), (2) one window with parallel oriented filters (case (a) of fig. 7) and (3) one window with two perpendicular oriented filters (case (b) of fig. 7). For wheel positioning we use a stepper motor (28BY-J48) which is controlled by an Arduino Uno board and a ULN2003 driver board.

For an easy background separation we aimed for a background that reduces reflections and other interactions with illumination. First, we intended to use black velvet as background, but, since berries can lose juice while measuring, we just painted the interior of the LSL camera housing with black color. In the measurement campaign itself an additional small glass bin was used to position the berries quickly. For the next measurement campaign, we will provide a dark bin. Given the black background, berries of 'white' grapes - that are actually green in color - are more easily distinguishable from the background. This is actually not the case for berries of 'red' grapes - that are actually dark purple in color.

Impedance measurements were performed at room temperature using the 'I-sensor' as developed by [6]. Relative impedance values Zrel were calculated according to [6]. The impedance measurements employ:

- AD5933 high precision impedance converter system (Analog Devices GmbH, Munich, Germany)
- USB-I2C module (Devantech Ltd (Robot Electronics, Norfolk, United Kingdom) using FTDI FT232R USB chip.

Figure 9: The wheel carrying the polarization filters shows three windows: one window without any linear polarization filter (for standard and pattern images), one window with parallel oriented filters and one window with two perpendicular oriented filters. Each window can be placed in front of camera and beamer.

<!-- image -->

## 4.4 Software

Figure 10: Workflow. First, standard, direct, global, diffuse and specular images of a berry are captured using the LSL. Secondly, berries are detected and localized in the images using a CNN-based shifting pattern recognition. Thirdly, epicuticular waxes are detected using a second CNN-based segmentation approach. Finally, the localization and quantification of the epicuticular waxes are used to analyze the proportion of waxes per berry or to extract coherent regions with wax or without wax etc.

<!-- image -->

The first step of the process chain implements the data acquisition via the LSL. Secondly, two CNNs are used to localize the berry in the image and to detect epicuticular waxes on the berry's surface. Finally, the detected epicuticular waxes are used for different analyses, for example to correlate impedance measure and proportion of epicuticular waxes or to extract single regions. Figure 10 shows this workflow.

## 4.4.1 Data Acquisition

To capture the light-separated images our controlling software uses the LightCrafter [32], FlyCapture [33] and Arduino API [34] to control the hardware. Additionally we use the OpenCV [35] framework to transform the raw images delivered by the camera and save them in a datafile system. Before using the LSL, users can calibrate the hardware, e.g., initializing the position of the polarization wheel, or setting the focus of camera or/and beamer. Theoretically, the pattern-based method needs two images of chessboard-patterns in the best-case, each transparent and opaque filter cell having a size of 8 × 8 pixels. This size was derived empirically and turned out to capture the indirect reflection best. In practice, the boundaries of the squared filter cells are smooth due to the blurred projection of beamers. Therefore, we have to employ - according to Nayar et al. [16] - a larger number of illumination patterns, so that each surface point of the scene shows maximum illumination as well as maximum darkness in different images. In our experiments, the same chessboard-pattern is twenty-five times shifted (five times vertically and five times horizontally) which ensures that each pixel of a scene image shows maximum and minimum brightnesses (cf. [16]). Additionally, the black value of the beamer is computed, which represents the light intensity captured when the beamer projects only a black image. The twenty-five images derived that way are used to compute the direct and global images according to equations 1 and 2, where the b value represents the computed black value (cf. [16] and [18]).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The polarization method generates first a parallel image and a perpendicular image (cf. section 4.2). The derivation of the two images showing the diffuse reflections and the specular reflections, respectively, follows equations 3 and 4.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 11 gives an impression of the image generation using both light separation methods. The first image is the standard RGB image generated without any light separation. The second image shows one example of an image illuminated by the projection of one of the 25 high frequency patterns. The third and fourth image depict the obtained direct and global reflection components while the last two images depict the diffuse and specular reflection components.

## 4.4.2 Berry and Epicuticular Waxes Detection

We use two CNNs: one for the berry detection and one for the detection of the epicuticular waxes. A straightforward CNN-based approach to the berry detection would be to train and employ a CNN for pixel-wise classification, i.e. classifying each pixel of an input image into classes 'berry' or 'background'. This approach shows two disadvantages: First, the annotation of the partially very small and arbitrary shaped waxed and non waxed surface areas (cf. fig. 2) is a very difficult, time consuming and error-prone work. Secondly, this approach would demand for the processing of complete full HD input images of size 1 , 920 × 1 , 080 = 2 , 073 , 600 pixels. But in the most cases, the berries are placed in the top-left part of the visual field. Therefore, runtime performance can be increased by using a sliding patch approach where a patch of size 128 × 128 = 16 , 384 pixels is scanning the full HD input image with an appropriate stepsize starting at the top-left corner of the input image. An additional speed-up can be achieved by

Figure 11: Overview of resulting images of the two light-separation processes, picture details, manually cropped (400 × 400 pixels) out of images with dimensions 1920 × 1080 pixels. Berries are manually placed in the LSL, so we use our berry detector to localize them automatically in the image. We proceed with a gamma correction for both images of the polarization-based method in order to have a better visualization.

<!-- image -->

using a sliding pattern template instead of a complete patch as input of a CNN. The pattern template shows only 17 selected pixels out of a complete patch. These 17 pixels form a pattern yielding a sparse representation of interior and boundary pixels of a patch (cf. 12). Given this pre-processing, there is no need to train a deep CNN with encoder and decoder part for a complete labeling of all pixels of patches. Instead, a by far smaller CNN is used on annotated image crops of size 3 × 3 pixels to learn the classification of the central pixel into the classes 'berry' and 'background'. Therefore, the CNN is very small with respect to the visual field and very efficient (cf. fig. 13 a)). If the 17-pixel-pattern reports a hit, the centre and the radius of a spherical area of interest (AoI) as a first rough estimation of the visible berry shape can be determined by only four shifts of the pattern. After detection of the AoI, the second CNN is employed to classify all pixels in the AoI into the classes 'epicuticular waxes', 'no epicuticular waxes' and 'others'. Also this second CNN is designed as a small and efficient classification network that is trained again on annotated image crops of size 3 × 3 pixels to learn the classification of the central pixel into the classes 'epicuticular waxes', 'no epicuticular waxes' and 'others' (cf. fig. 13 (b)). The annotation of training data and ground truth can now be done very effeciently using our semi-automated annotation tool that allows labeling all pixels in rectangular crops in one step. This annotation tool allows to label hundred of pixels in less than thirty seconds.

To cope with berries of different sizes, the pre-processing employs a multi-scale approach to the patternbased berry detection. It starts with positioning the 17-pixel-pattern in patches of size 128 × 128 pixels. In the next scales the 17-pixel-pattern is positioned in patches of sizes 64 × 64 , 32 × 32 , 16 × 16 , 8 × 8 , 4 × 4, successively. The multi-scale iteration stops after having found the berry in one scale. Comparing this customized approach to a fully convolutional network approach (e.g., an AlexNet-based FCN with an up-convolution-based decoder part) working on the complete full HD images, we save more than 30 % of the runtime in average.

Figure 12: The sliding template method. (a) The 17 sensor pixels of the sliding pattern do not vote for berry detection. (b) The 17 sensor pixels of the sliding pattern vote for the detection of a berry.

<!-- image -->

## 4.4.3 Results Analysis

Given the identification, localization and quantification of epicuticular waxes from the last CNN-based classification step, these results represent the starting point for various analyses and evaluations. In our current experiments for example, we evaluated the correlation between the visually derived quantification of epicuticular waxes with corresponding measurements of relative impedance values that we used for validation (cf. section 2.2 and the analysis step correlation with impedance in fig. 10). Another opportunity is the extraction and quantification of connected and coherent regions of epicuticular waxes (cf. the analysis step region extraction in fig. 10). The distributions and sizes of these regions of epicuticular waxes can give additional insights with respect to other phenotyping traits like compactness of grape bunches etc. We will consider additional options of analysis in our ongoing work. The visualization part of the result analysis is developed in Python 3.5 using the Numpy [36], Seaborn [37], Matplotlib [38] and Pandas [39] libraries.

## 4.5 CNN Training

For the detection of berries and epicuticular waxes, we used two segmentation CNNs, i.e, each single pixel of the image input is classified into a category. The input for both CNNs is 3 × 3 crops of the image to learn the classification of the central pixel of a crop. We train both CNNs with the following parameters: momentum = 0.9, weight decay = 5 × 10 -4 and a decreasing learning rate from 10 -4 to 10 -6 at training iterations 50.000 and 100.000, respectively. Training's duration has been about thirty minutes for processing training datasets of about 6,000,000 and 600,000 pixels for berry detection and epicuticular waxes detection, respectively. The CNN for the berry detection processes also the pixel coordinates for the localization of the berries. The coordinates are represented in an additional input layer. A concatenation layer merges both resulting outputs (pixel values and pixel coordinates) as shown in figure 13 (a) . After localization of the berry, the second CNN for wax detection is not in need for an additional input layer holding pixel coordinates (cf. figure 13 (b) ).

## 5 Conclusions

In order to phenotype the distribution of epicuticular waxes of the grapevine berry surfaces as important indicator for resilience towards Botrytis bunch rot and as quality trait for table grape production, we 1) set up an automated and mobile light-separation camera system; and 2) developed an automated Con-

Figure 13: Both CNNs for respectively object and epicuticular waxes detection. There is a Rectified linear Unit (ReLU) after each of the fully-connected and convolution layers ( a ) Design of the CNN for the pixel-wise berry detection. ( b ) Design of the CNN for the pixel-wise epicuticular waxes.

<!-- image -->

volutional Neural Network (CNN) based approach for fast image analysis. Regarding high-throughput applications in the future, especially with a view to breeders and the grape industry, several berries need to be phenotyped at once or on the go from an assembly line or in the field. Therefore, the most efficient light-separation setting needs to be determined and a new design of the capturing box will be necessary, for example build an input/output mechanic with a conveyor belt to get berries under the camera and beamer, so that the data acquisition process can be fully automated. Moreover, to take full advantage of the non-invasive quality of our approach, an outdoor adaption is conceivable by placing camera and beamer in a darkest possible field vehicle like the Phenoliner. The application of this non-invasive manner enables comparable monitoring studies and the precise characterization of large breeding material and genetic repositories as well as a promising quality control tool for table grape production. Hereby, automation, mobility, simple-to-apply and minimal user-interaction are important requirements in order to transfer the method to different labs or groups irrespective to scientific background. The availability of a user-friendly graphical user interface will extend the application field of the presented system.

Funding We gratefully acknowledge the financial support of the Federal Office for Agriculture and Food (Bundesanstalt f¨ ur Landwirtschaft und Ern¨ ahrung, BLE) and the Federal Ministry of Food and Agriculture (Bundesministerium f¨ ur Ern¨ ahrung und Landwirtschaft, BMEL).This work was funded by BMEL in the framework of Vitismart (FZK 2815ERA05C) and the Deutsche Forschungsgemeinschaft (STE 806/2-1 and TO 152/6-1). Further, we thank the German Federal Ministry of Education and Research (Bundesministerium f¨ ur Bildung und Forschung (BMBF), Bonn, Germany (NoViSys: FKZ 031A349E)).

Acknowledgments We also thank Florian Schwander (JKI, Siebeldingen) for improving the setup of the I-Sensor and many thanks to Daniel Zendler (JKI, Siebeldingen) for the 3D-print of the I-Sensor casing. Further, we thank Jenny Mack (University of Bonn) for proofreading this article.

Abbreviations The following abbreviations are used in this manuscript:

CNN

Convolutional Neural Network

LSL

Light Separation Labor

RoI

Region of Interest

ReLU

Rectified Linear Unit

## References

1. Meneguzzo, J., Miele, A., Rizzon, L. A. &amp; Ayub, M. Effect of bunch rot on the sensory characteristics of the Gew¨ urztraminer wine. Journal International des Sciences de la Vigne et du Vin 42, 107 (2008).
2. Rosenquist, J. K. &amp; Morrison, J. C. The development of the cuticle and epicuticular wax of the grape berry. Vitis 27, 63-70 (1988).
3. Percival, D., Sullivan, J. &amp; Fisher, K. Effect of cluster exposure, berry contact and cultivar on cuticular membrane formation and occurrence of bunch rot(Botrytis cinerea PERS.: FR.) with 3 Vitis vinifera L. cultivars. Vitis 32, 87-97 (1993).
4. Gabler, F. M., Smilanick, J. L., Mansour, M., Ramming, D. W. &amp; Mackey, B. E. Correlations of morphological, anatomical, and chemical features of grape berries with resistance to Botrytis cinerea. Phytopathology 93, 1263-1273 (2003).
5. Molitor, D., Behr, M., Fischer, S., Hoffmann, L. &amp; Evers, D. Timing of cluster-zone leaf removal and its impact on canopy morphology, cluster structure and bunch rot susceptibility of grapes. J. Int. Sci. Vigne Vin 45, 149-159 (2011).
6. Herzog, K., Wind, R. &amp; T¨ opfer, R. Impedance of the Grape Berry Cuticle as a Novel Phenotypic Trait to Estimate Resistance to Botrytis Cinerea. en. Sensors 15, 12498-12512. issn : 1424-8220 (May 2015).
7. K¨ ok, D. &amp; C ¸elik, S. Determination of characteristics of grape berry skin in some table grape cultivars (V. vinifera L.) Journal of Agronomy 3, 141-146 (2004).
8. Rid, M., Markheiser, A., Hoffmann, C. &amp; Gross, J. Waxy bloom on grape berry surface is one important factor for oviposition of European grapevine moths. Journal of Pest Science, 1-15 (2018).
9. Becker, T. &amp; Knoche, M. Deposition, strain, and microcracking of the cuticle in developing 'Riesling'grape berries. Vitis 51, 1-6 (2012).
10. ¨ Ozer, N. et al. Investigations on the role of cuticular wax in resistance to powdery mildew in grapevine. Journal of General Plant Pathology 83, 316-328 (2017).
11. Molitor, D. et al. Multi-annual comparisons demonstrate differences in the bunch rot susceptibility of nine Vitis vinifera L.'Riesling'clones. Vitis: Journal of Grapevine Research 57, 17-25 (2018).
12. Anderson, R. R. Polarized light examination and photography of the skin. Arch. Dermatol 127, 1000-1005 (1991).
13. Wolff, L. B. &amp; Boult, T. E. Constraining object features using a polarization reflectance model. IEEE Transactions on Pattern Analysis and Machine Intelligence 13, 635-657 (1991).
14. Jacques, S. L., Roman, J. R. &amp; Lee, K. Imaging superficial tissues with polarized light. Lasers in Surgery and Medicine 26, 119-129 (2000).
15. Jacques, S. L., Ramella-Roman, J. C. &amp; Lee, K. Imaging skin pathology with polarized light. Journal of Biomedical Optics 7, 329-341 (2002).

16. Nayar, S. K., Krishnan, G., Grossberg, M. D. &amp; Raskar, R. Fast Separation of Direct and Global Components of a Scene Using High Frequency Illumination. ACM Trans. Graph. 25, 935-944. issn : 0730-0301 (July 2006).
17. Subramaniam, N., Saman, G. &amp; Hancock, E. Detection of skin lesions using diffuse polarisation in 2010 IEEE International Conference on Image Processing (Sept. 2010), 3021-3024. doi: 10.1109/ ICIP.2010.5651786 . &lt; http://dx.doi.org/10.1109/ICIP.2010.5651786 &gt; .
18. Garces, E., Martin, F. &amp; Gutierrez, D. Low Cost Decomposition of Direct and Global Illumination in Real Scenes. in Spanish Computer Graphics Conference (CEIG) (eds Sbert, M. &amp; Lopez-Moreno, J.) (The Eurographics Association, 2015). doi: 10.2312/ceig.20151200 . &lt; http://dx.doi.org/ 10.2312/ceig.20151200 &gt; .
19. ImageCLEF - The CLEF Cross Language Image Retrieval Track | ImageCLEF / LifeCLEF - Multimedia Retrieval in CLEF http://www.imageclef.org/ [Online; accessed 31. May 2018]. May 2018. &lt; http://www.imageclef.org &gt; .
20. Lu, J., Hu, J., Zhao, G., Mei, F. &amp; Zhang, C. An in-field automatic wheat disease diagnosis system. Computers and Electronics in Agriculture 142, 369-379 (2017).
21. Mohanty, S. P., Hughes, D. P. &amp; Salath´ e, M. Using Deep Learning for Image-Based Plant Disease Detection. Frontiers in Plant Science 7, 1419 (2016).
22. Hughes, D. P. &amp; Salath´ e, M. An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing. CoRR abs/1511.08060. &lt; http://arxiv.org/abs/1511.08060 &gt; (2015).
23. Krizhevsky, A., Sutskever, I. &amp; Hinton, G. E. ImageNet Classification with Deep Convolutional Neural Networks in Advances in Neural Information Processing Systems 25 (eds Pereira, F., Burges, C. J. C., Bottou, L. &amp; Weinberger, K. Q.) (Curran Associates, Inc., 2012), 1097-1105.
24. Szegedy, C. et al. Going deeper with convolutions in 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (June 2015), 1-9. doi: 10.1109/CVPR.2015.7298594 . &lt; http: //dx.doi.org/10.1109/CVPR.2015.7298594 &gt; .
25. Wang, G., Sun, Y. &amp; Wang, J. Automatic Image-Based Plant Disease Severity Estimation Using Deep Learning. Computational Intelligence and Neuroscience 2017. doi: 10.1155/2017/2917536 . &lt; http://dx.doi.org/10.1155/2017/2917536 &gt; (2017).
26. Sladojevic, S., Arsenovic, M., Anderla, A., Culibrk, D. &amp; Stefanovic, D. Deep Neural Networks Based Recognition of Plant Diseases by Leaf Image Classification. Computational Intelligence and Neuroscience 2016. doi: 10.1155/2016/3289801 . &lt; http://dx.doi.org/10.1155/2016/3289801 &gt; (2016).
27. Sapkota, S., Chen, L.-L., Schreiner, K., Ge, H. &amp; Hwang, C.-F. A phenotypic study of Botrytis bunch rot resistance in Vitis aestivalis-derived 'Norton'grape. Tropical Plant Pathology 40, 279282 (2015).
28. Badrinarayanan, V., Kendall, A. &amp; Cipolla, R. Segnet: A deep convolutional encoder-decoder architecture for image segmentation. IEEE transactions on pattern analysis and machine intelligence 39, 2481-2495 (2017).
29. Kicherer, A. et al. An automated field phenotyping pipeline for application in grapevine research. Sensors 15, 4823-4836 (2015).
30. Kicherer, A. et al. Phenoliner: A New Field Phenotyping Platform for Grapevine Research. Sensors 17, 1625 (2017).
31. SPECIES, N. E. O. T. O. D. L. F. G. V. A. V. Organisation Internationale de la vigne et du vin http://www.oiv.int [Online; accessed 30. May 2018]. May 2018. &lt; http://www.oiv.int &gt; .
32. DLPLIGHTCRAFTER DLP R © LightCrafter TM Evaluation Module [Online; accessed 18. May 2018]. May 2018.
33. FlyCapture SDK https://www.ptgrey.com/flycapture-sdk [Online; accessed 18. May 2018]. May 2018. &lt; https://www.ptgrey.com/flycapture-sdk &gt; .

34. Arduino - Software https://www.arduino.cc/en/Main/Software [Online; accessed 18. May 2018]. May 2018. &lt; https://www.arduino.cc/en/Main/Software &gt; .
35. Bradski, G. The OpenCV Library. Dr. Dobb's Journal of Software Tools (2000).
36. Van der Walt, S., Colbert, S. C. &amp; Varoquaux, G. The NumPy Array: A Structure for Efficient Numerical Computation. Computing in Science &amp; Engineering 13, 22-30. issn : 1521-9615 (Mar. 2011).
37. Waskom, M. et al. mwaskom/seaborn: v0.8.1 (September 2017) DOI: 10.5281/zenodo.883859. doi: 10. 5281/zenodo.883859 . &lt; https://doi.org/10.5281/zenodo.883859 &gt; (Sept. 2017).
38. Hunter, J. D. Matplotlib: A 2D Graphics Environment. Computing in Science &amp; Engineering 9, 90-95. issn : 1521-9615 (2007).
39. McKinney, W. Data structures for statistical computing in python in Proceedings of the 9th Python in Science Conference 445 (Austin, TX, 2010), 51-56. &lt; http://pandas.pydata.org/ &gt; .