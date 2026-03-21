---
id: arxiv-2508.03238
title: Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm
year: 2025
country: Internacional
source: ArXiv (math.DS)
doc_type: Artículo científico
language: en
tags:
  - dinámica de poblaciones
  - clima
  - temperatura
  - monitoreo fitosanitario
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm

Xu Chen a ,1, ⋆ , Wenxuan Li b ,1, ⋆ , Xiaoshuang Li c ,2 , Suli Liu b , ∗ ,3 and Yu Gao d , ∗ ,4

a School of Artificial Intelligence, Jilin University, Changchun, 130012, Jilin, China

b School of Mathematics, Jilin University, Changchun, 130012, Jilin, China

c College of Plant Protection, Jilin Agricultural University, Changchun, Changchun, 130118, Jilin, China

d Key Laboratory of Soybean Disease and Pest Correlation, Ministry of Agriculture and Rural Affairs, Changchun, 130118, Jilin, China

## ARTICLE INFO

Keywords : Soybean Pod Borer ( Leguminivora glycinivorella ) Prediction Data fitting Mathematical Models Neural Networks

## ABSTRACT

Against the backdrop of global climate change and agricultural globalization, soybean production is increasingly threatened by pest outbreaks, with Leguminivora glycinivorella (commonly known as the soybean pod borer) being a major pest species. This pest is widely distributed, particularly in northeastern China-the country's primary soybean-producing region-where its outbreaks have significantly affected both yield and quality. Although statistical and mechanistic models have been applied to pest forecasting, existing approaches often fail to effectively integrate climatic factors with pest dynamics and lack sufficient expressive power. To address these limitations, this study proposes a novel pest prediction method based on Physics-Informed Neural Networks (PINNs). Specifically, we formulate a logistic-type ordinary differential equation (ODE) that incorporates microclimate factors-temperature, humidity, and time-to describe the temporal dynamics of the soybean pod borer population. This ODE model is embedded into the PINN framework to develop the Pest Correlation Model Neural Network (PCM-NN), which is used to jointly infer the microclimate-driven parameter function 𝛼 ( 𝑇, 𝐻, 𝑡 ) and fit the pest population dynamics. We evaluate PCM-NN using daily monitoring data of soybean pod borer collected in Changchun, Jilin Province, from July to September during 2020-2023. Experimental results demonstrate that PCM-NN preserves biological interpretability while exhibiting strong nonlinear representational capacity, offering a feasible pathway for pest modeling and forecasting under multi-factor climatic conditions. This approach provides valuable support for agricultural pest monitoring, prevention, and control strategies.

## 1. Introduction

Soybean is an important grain, oil, and feed crop in China and plays a strategic role in the development of the national economy. However, in recent years, climate change and agricultural ecosystem imbalances have exacerbated pest threats to soybean production, among which the Leguminivora glycinivorella (commonly known as the soybean pod borer) is one of the major pests responsible for substantial yield and economic losses. Research indicates that this pest's suitable habitats are widely distributed across most regions of China Gao et al. (2018); Shi et al. (2018); Fei et al. (2024), the Korean Peninsula, the Russian Far East, and Japan Yang et al. (2024). The northeastern region of China, as the country's primary soybean-producing area, faces a particularly severe threat from soybean pod borer outbreaks, according to the 2023 Technical Plan for the Prevention and Control of Major Soybean Diseases and Pests 1 . During the critical soybean growth period (July-September), the larvae bore into pods and feed on seeds, leading not only to direct yield losses but also to a sharp decline in crop market value. For accurate pest identification, Fig. 1

⋆ These authors contributed equally to this work.

liusuli@jlu.edu.cn (S. Liu); gaothrips@jlau.edu.cn (Y. Gao)

∗ Corresponding author

ORCID(s):

2 http://orcid.org/0000-0002-3601-117X

1 http://orcid.org/0000-0002-0866-6857

3 http://orcid.org/0009-0002-3855-0289

5 http://orcid.org/0000-0002-3369-8578

4 http://orcid.org/0000-0002-4354-2665

1 http://www.moa.gov.cn/ztzl/ddymdzfhjs/jszd\_29063/202303/t20230301\_6421921.htm

illustrates the typical morphological characteristics of this pest across its life stages. Given the substantial threat posed by soybean pod borers to soybean production, there is an urgent need to conduct modeling and prediction research on the occurrence dynamics of soybean pod borers, so as to achieve early warning and scientific prevention and control of the pest occurrence.

Figure 1: Different Developmental Stages of the Soybean Pod Borer . (a) Egg Stage. (b) Larvae Stage. (c) Adult Stage. (d) Pupa Stage. Provided by Prof. Shusen Shi.

<!-- image -->

Pest control has long been a pressing global challenge, attracting extensive attention from entomologists and plant protection scientists (Chen et al. (2022b); Jiang-sheng et al. (2021); Kuzmin et al. (2020)). Currently, pest prediction research primarily encompasses two categories: empirical models based on statistical correlations and analytical models based on biophysical mechanisms. Statistical approaches establish associations between environmental factors and pest occurrence through regression analysis or machine learning algorithms. For example, Chen et al. (2022a) demonstrated that lychee stink bug (Tessaratoma papillosa) populations thrive under optimal temperature, humidity, and light conditions. Amjad Bashir et al. (2022) investigated the effects of temperature and humidity on cotton pest complexes, quantifying the correlation coefficients between climatic factors and pest abundance. Similarly, Kumar et al. (2023) analyzed the relationship between major peanut pests and microclimate variables. However, while these methods can identify key environmental drivers, they fail to elucidate the physiological mechanisms underlying pest population responses to environmental changes. On the other hand, mechanistic models employ mathematical tools such as differential equations to describe pest population growth and dispersal dynamics (Sokame et al. (2021); Malaguit et al. (2023)). Yet, existing models often neglect the dynamic influence of climatic factors or treat them merely as external inputs, rather than integrating temperature, humidity, and other variables as deterministic parameters within the model framework (Skendžić et al. (2021); Ma and Ma (2022); Ponti et al. (2021)). A study by Deutsch et al. (2018) revealed that each 1°C increase in global temperature escalates pest-induced crop losses by 10-25%, underscoring the urgent need for predictive models that couple climatic variables with biological parameters. Nevertheless, current research still falls short in effectively integrating climatic factors with pest population dynamics, necessitating novel modeling approaches that simultaneously account for climatic influences and biological mechanisms to enhance prediction accuracy and practical applicability.

To overcome the insufficient integration of climatic factors and pest population dynamics in existing modeling approaches, this study proposes a population dynamics model of soybean pod borer coupled with temperature and humidity. Specifically, we formulate a logistic-type ordinary differential equation (ODE) to describe the temporal evolution of pest populations, and embed a microclimate-driven parameter function 𝛼 ( 𝑇, 𝐻, 𝑡 ) to quantify the combined impact of environmental conditions. To infer the non-explicit function 𝛼 , we integrate the ODE model into a PhysicsInformed Neural Network (PINN) framework and develop a novel Pest Correlation Model Neural Network (PCM-NN). By minimizing the composite loss function composed of ODE residuals and observation errors, this model not only fits the observed soybean pod borer population data but also estimates the evolving form of 𝛼 . Compared to traditional models that require prior assumptions about functional forms, PCM-NN flexibly captures the nonlinear dependencies of 𝛼 on temperature, humidity, and time, thereby enhancing both the expressiveness and the physical consistency of the model. Furthermore, we utilized monitoring data from 2020 to 2023 to train and validate the model. Through this process, we successfully estimated the important microclimate-driven parameter 𝛼 , which is essential for understanding the mechanisms of pest occurrence and developing effective prevention and control strategies. Additionally, we used the trained model to predict the occurrence of soybean pod borer in 2024, providing forward-looking guidance for agricultural production.

The remainder of this study is organized as follows. Section 2 introduces the data sources and preprocessing procedures for soybean pod borer monitoring, followed by a detailed description of the climate-coupled logistic model and its implementation within the PINN framework. Section 3 presents the experimental results and validation analyses, assessing the model's performance and applicability. Section 4 discusses the advantages, limitations, and potential practical implications of the proposed approach. Finally, Section 5 concludes the study and outlines directions for future research.

This study presents an innovative integration of Physics-Informed Neural Networks (PINNs) with pest population dynamics modeling, resulting in the development of the Pest Correlation Model Neural Network (PCM-NN) for soybean pod borer prediction. By embedding the mechanistic pest dynamics model as a physical constraint within the neural network architecture, PCM-NN achieves accurate fitting of pest population trends while simultaneously quantifying and visualizing the regulatory effects of microclimate factors such as temperature and humidity. Due to its methodological flexibility and generalizability, this approach holds significant promise for broader applications in the prediction of other agricultural pests and provides a feasible technical framework for climate-resilient pest forecasting and precision management.

Figure 2: Integrated monitoring system for soybean pod borer ( Leguminivora glycinivorella ) population dynamics. (a) Adult male L. glycinivorella . (b) Final instar larva infesting soybean pod. (c) Synthetic sex pheromone lure. (d) Pheromone trap (PVC construction) deployed at 20-30 cm above soybean canopy. Georeferenced deployment shown at Jilin Agricultural University Experimental Station (43.82°N, 125.42°E).

<!-- image -->

## 2. Data and Methods

## 2.1. Data

## 2.1.1. Data Acquisition

Here, we employ trapping devices to collect data on the male adult soybean pod borer and monitor population dynamics during its peak activity period of emergence. The specific configuration of the trapping device is illustrated in Fig. 2, and the key settings are listed in the following.

Deploying lepidopteran sex pheromones constitutes a cornerstone of precision pest surveillance in modern integrated pest management frameworks Wakamura (1992). For Leguminivora glycinivorella , species-specific pheromone components (predominantly (Z)-9-tetradecenyl acetate and (Z)-11-tetradecenyl acetate in optimized ratios) have been chemically characterized and operationally validated for field monitoring Le et al. (2006). This semiochemical-based approach exploits male moths' obligate orientation behavior toward synthetic pheromone plumes, enabling real-time tracking of adult eclosion peaks and spatiotemporal population gradients Hu et al. (2012).

- Study site . Field monitoring was conducted at the Soybean Regional Technology Innovation Center research base (43.82°N, 125.42°E) of Jilin Agricultural University, located in the suburban agroecosystem of Changchun City, Jilin Province, Northeast China. A 1-hectare (10,000 m 2 ) continuous soybean cropping field was selected to monitor natural soybean pod borer population dynamics. To eliminate anthropogenic interference, no insecticide applications or pheromone-based mating disruption tactics were implemented during the soybean growing season (May-September).
- Trapping devices . Three traps (T1-T3) were deployed in a triangular grid (inter-trap distance ≥ 50 m) in the end of June before the anticipated adult emergence period (at July), positioned 20-30 cm above the soybean canopy to intercept male flight paths. In addition, traps were placed ≥ 10 mfrom field edges to reduce edge-effect bias. Synthetic sex pheromone lures (Ningbo Newcomb Biotechnology Co., LTd., Ningbo, Zhejiang, China) replaced monthly to maintain emission efficacy.
- Aphased observation . Pre-emergence phase: Tri-daily trap inspections to establish the baseline activity. Active Monitoring Phase: Upon initial detection of male adults (defined as ≥ 1 individual/3-trap/day), inspections intensified to daily intervals.
- Meteorological Data . Daily-averaged microclimatic parameters (mean temperature [°C] and relative humidity [%]) for Changchun City were obtained from the Changchun National Benchmark Climate Station under the China Meteorological Administration.

Integrative analysis of daily trap captures (summed across three spatially distributed pheromone traps) revealed consistent interannual patterns in adult soybean pod borer emergence within the Changchun agroecosystem. The population phenology typically exhibited a unimodal curve or occasional bimodal fluctuations. This unimodal/bimodal plasticity likely reflects microclimatic modulation of pupal development synchronicity, with secondary peaks (when observed) correlating with mid-August precipitation events. The standardized trapping system effectively captured these transient dynamics.

## 2.1.2. Data Pre-processing

To minimize phenological variability across years and specifically target the period when the interaction between pest dynamics and environmental factors is most relevant for modeling purposes (as the key life-cycle stages of the soybean pod borer and critical soybean growth phases closely align within this timeframe, facilitating the capture of essential ecological relationships), we restricted analyses to a critical phenological phase (July 25-August 23) during which soybean pod borer adults exhibit peak activity in temperate soybean agroecosystems. The dataset was partitioned chronologically, with observations from 2020 to 2023 allocated to model training and those from 2024 reserved for prospective validation of temporal generalizability.

In this study, daily monitoring records of adult male soybean pod borer populations were systematically collected alongside corresponding mean daily temperature and humidity measurements during July-September annually from 2020 to 2024. Adult emergence is typically initiated in late July (July 25-31), with population peaks occurring between August 8-15, followed by a terminal decline phase in late August that is synchronized with soybean pod hardening (R6 growth stage).

Figure 3: Spatiotemporal dynamics of soybean pod borer ( Leguminivora glycinivorella ) abundance and associated microclimatic drivers during peak activity seasons (2020-2023). (a) Daily male moth captures from July 25 to August 23, with individual annual trajectories (colored points) against the interannual average (colored line). (b) Corresponding daily mean temperature (°C) profiles, illustrating thermal variability across years (individual observations) and climatic baseline (interannual average). (c) Daily relative humidity (%) fluctuations (individual observations and interannual average) during the same period. Interannual averages derived from arithmetic means of synchronized daily records across 2020-2023. Microclimatic data sourced from China Meteorological Administration.

<!-- image -->

Initial comparative analysis of daily observations across consecutive years (2020-2023) revealed pronounced instability and irregularity in soybean pod borer population counts and their associated microclimatic variables (temperature and humidity). These fluctuations, indicative of high stochastic noise inherent in short-term ecological datasets, obscured discernible phenological or climatic trends. To mitigate this limitation, we adopted interannual averaging, a climatologically inspired preprocessing method, to disentangle persistent seasonal signals from transient perturbations, as shown in Fig. 3. It should be noted in Fig. 3 that, given the roughly equal proportion of male and female adult soybean pod moths in the field population, the data shown in Fig. 3 effectively represents the number of adult populations by multiplying the collected number of males by two.

1. Temporal Alignment: For each calendar date between July 25 and August 23 (Day of Year [DOY]), we aggregated four years (2020-2023) of synchronized daily records, including: adult male soybean pod borer counts (individuals/3-trap/day), mean daily temperature (°C), mean relative humidity (%).

Interannual averaging leverages temporal compositing to suppress year-specific anomalies (e.g., extreme weather events, localized management practices) while amplifying recurrent patterns driven by climatic seasonality. This approach aligns with methodologies used in climate science to define baseline bioclimatic norms Change (2023) and has been adapted here for agroecological systems to resolve insect-environment coupling. The procedure entailed two sequential steps:

2. Composite Dataset Generation: The interannual composite was derived by computing the arithmetic mean for each variable at every DOY:

<!-- formula-not-decoded -->

Table 1 Summary of Key Studies on Crop Disease and Pest Analysis Using Logistics

Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Fan and Wang (1998), Methodology: Math models for analyzing optimal harvesting policies, Key Findings: Unique periodic solutions and op- timal harvesting efforts identified, Limitations: Focuses mainly on theoretical models, practical application de- tails lacking.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Liu et al. (preprint), Methodology: Math analysis of cumula- tive lethal effect of pesticide spraying, Key Findings: Conditions for pest extinction and stability of periodic solutions dis- covered, Limitations: Theoretical research; experimen- tal validation and practical appli- cation details limited.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Braness et al. (1991), Methodology: Logistic models and bioassays for insecticide effectiveness, Key Findings: Factors influencing cockroach mortality identified; application frequencies recommended, Limitations: Limitations not specified in ex- cerpt.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Garrido- Jurado et al. (2011), Methodology: Controlled experiments and statistical models for fungi ef- fectiveness, Key Findings: Soil moisture and temperature impact on fungi virulence and insect susceptibility found, Limitations: Specific fungal isolates and insect species tested; controlled condi- tions may not reflect natural vari- ations.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Tang and Cheke (2008), Methodology: Math models and simulations for integrated pest control, Key Findings: Complex dynamical behaviors of pest-parasitoid populations; peri- odic control strategies suggested, Limitations: Simplifying assumptions may limit applicability to real-world scenarios.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Reference: Sun et al. (2018), Methodology: Logistic reaction-diffusion harvesting model with infinite delay, Key Findings: Evolution rate and small diffusion rate benefit species survival, Limitations: Simplifies complex ecological phenomena; further empirical validation needed.
where ̄ 𝑥 𝐷𝑂𝑌 represents the averaged value for a given day-of-year, and 𝑁 = 4 (years). This produced a 30-day synthetic dataset reflecting the "climatological normal" of pest incidence and microclimate during peak activity seasons.

To contextualize 2024 test data against historical patterns, an expanded composite (2020-2024) was generated using identical procedures, though model training strictly utilized the 2020-2023 subset to prevent temporal leakage.

## 2.2. Methods

## 2.2.1. Model Validation

The logistic equation, a classic mathematical model for describing population growth patterns, was first proposed by Verhulst in the mid-19th century to explore the relationship between population growth and resource constraints. Let 𝑥 ( 𝑡 ) represent the population size at time 𝑡 , the classical Logistic equation is

<!-- formula-not-decoded -->

where 𝑟 represents the intrinsic growth rate, and 𝐾 represents the carrying capacity of the environment. Here, the first term 𝑟𝑥 is used to model unimpeded growth rate in the beginning period; and the second term -𝑟 𝐾 𝑥 2 measures the interference between population by competing for some critical resource, such as food or living space. Due to its simplicity and generality, the logistic equation has become a fundamental tool in ecology and complex systems science. Many researchers integrate this differential equation into pest population dynamics to predict development trends and optimize control strategies. To gain a deeper understanding of the application of this model in crop pest research, we conducted an extensive literature review and summarized the relevant research findings in Table 1.

The classical logistic model provides a phenomenological framework for density-dependent population growth, yet its assumption of constant intrinsic growth rate 𝑟 and static carrying capacity 𝐾 limits applicability to poikilothermic

organisms like Leguminivora glycinivorella, whose vital rates are thermally modulated. To mechanistically couple microclimatic factors with pest phenology, we propose a modified logistic equation:

<!-- formula-not-decoded -->

Here, 𝑥 ( 𝑡 ) ∈ ℝ + represents the adult population of soybean pod borer at time 𝑡 ; 𝐴 ∈ ℝ + is the field-realistic baseline growth rate, reflects growth potential under average field conditions, which is inherently lower than laboratory-observed maxima due to persistent ecological pressures (e.g., predation, and suboptimal microhabitats); 𝐵 = 𝐴 𝐾 represents the density-dependent inhibition coefficient, where 𝐾 is the environmental carrying capacity. In addition, 𝛼 ∶ ℝ +3 → ℝ is the climatic modulation function defined as:

<!-- formula-not-decoded -->

with 𝑇 ∗ and 𝐻 ∗ denoting thermal and hygric optima for the survival of soybean pod borer. A possible property of bidirectional climatic modulation function 𝛼 is

<!-- formula-not-decoded -->

quantifying how Leguminivora glycinivorella populations experience growth suppression under thermal/hygric stress (deviations exceeding thresholds 𝑀 1 , 𝑀 2 ) versus growth facilitation when microclimatic conditions remain within optimal ranges. However, the functional form of the climatic modulation term inherently encapsulates complex, nonclear interactions among temperature, humidity, and pest physiology. Traditional explicit parameterizations (e.g., quadratic penalties) risk oversimplifying these higher-order couplings, our enhanced framework employs a fully connected neural network (NN) to represent 𝛼 ( 𝑇, 𝐻, 𝑡 ) , enabling data-driven discovery of nonlinear interactions between microclimatic factors and pest population dynamics. The transfer diagram of model (2) is shown in Fig. 4(a), and the NN diagrammatic representation of (3) is given in Fig. 4(b).

Figure 4: (a) Mechanistic-climate feedback structure of Model (2) . Solid black arrows denote density-dependent growth/decline processes, dashed gray arrows represent microclimatic couplings. (b) A deep neural network architecture for climatic modulation function 𝛼 𝑁𝑁 .

<!-- image -->

## 2.2.2. PCM-NN

This section introduces a new deep learning method - Pest Correlation Model Neural Network (PCM-NN). This method not only inherits the essence of Physical Information Neural Network (PINN), which improves the accuracy of model prediction by incorporating physical laws, but also introduces additional environmental parameters (temperature and humidity) to meet the practical needs of pest management, thereby achieving more accurate description and prediction of pest dynamics.

Figure 5: Schematic diagram of PCM-NN algorithm. 𝑥 𝑁𝑁 𝐷 ( 𝑡, Θ 𝐷 ) serves as the state variable for fitting Model (3) , as depicted in the top-left region of the figure. Concurrently, parameter 𝛼 𝑁𝑁 𝐷 ( 𝑡, Θ 𝐷 ) is utilized for inferring the parameter 𝛼 , illustrated in the top-right region. The term d 𝑥 𝑁𝑁 𝐷 d 𝑡 denotes the self-differential operator, central to the model's dynamics. The overall Loss function, 𝐿𝑜𝑠𝑠 , comprises two components: 𝐿𝑜𝑠𝑠 𝑑𝑎𝑡𝑎 and 𝐿𝑜𝑠𝑠 𝑜𝑑𝑒 . By minimizing 𝐿𝑜𝑠𝑠 , the algorithm achieves simultaneous data fitting and inference of parameter.

<!-- image -->

Fig. 4 (b) shows a schematic diagram of the deep neural network structure of PCM-NN. Unlike traditional PINNs that only receive time 𝑡 as input, PCM-NN's input layer is expanded to include three dimensions: time 𝑡 , ambient temperature 𝑇 , and ambient humidity 𝐻 . This design aims to capture the impact of environmental factors on the occurrence and development of pest infestations, thereby improving the predictive accuracy of the model.

Fig. 5 provides a detailed description of the algorithm flow of PCM-NN. The core lies in embedding the pest model (2) as physical information into the training process of the neural network. This pest model is based on ecological principles and describes the variation of pest numbers over time, temperature, and humidity. In PCM-NN, this physical information is represented by defining a specific Loss function, which includes two parts:

- Data Loss : measures the difference between network predictions and observed pest data. This Loss ensures that the model can learn the dynamic behavior of pests from historical data. The specific form of Loss is:

<!-- formula-not-decoded -->

where 𝑁𝑑 represents the quantity of training data, and 𝑥 𝑁𝑁 ( 𝑡 𝑖 ) represents the daily increase in the number of soybean pod borer.

- ODE (Ordinary Differential Equation) Loss : Based on the physical constraints defined by the pest model (2), calculate the deviation of network predictions from physical laws. This Loss term ensures that the model predictions not only conform to observed data, but also strictly follow the physical mechanisms of pest occurrence. The form of 𝐿𝑜𝑠𝑠 𝑜𝑑𝑒 is as follows:

<!-- formula-not-decoded -->

Table 2 Deep Neural Network Hyperparameter Values and Parameter Settings

Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝑇 ∗, Parameter Interpretation: Optimum temperature, Values: 21 ◦ 𝐶.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝐻 ∗, Parameter Interpretation: Optimum humidity, Values: 84%.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝐴, Parameter Interpretation: Field-realistic baseline growth rate, Values: 0.372.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝐵, Parameter Interpretation: Field-realistic baseline growth rate/carrying capacity, Values: 0.0008.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝛼, Parameter Interpretation: Climatic modulation function, Values: [-1.372, 0.628].
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝑈 𝑁𝑁 ( 𝑡 ), Parameter Interpretation: Number of hidden layers in data, Values: 5*32.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: 𝛼 𝑁𝑁 ( 𝑡 ), Parameter Interpretation: Number of hidden layers for parameters, Values: 3*64.
Según Modeling the Temperature-Humidity Coupling Dynamics of Soybean Pod Borer Population and Assessing the Predictive Performance of the PCM-NN Algorithm (2025), Symbol: Iterations, Parameter Interpretation: Number of iterations, Values: 1 × 10 4.
where 𝑁𝑒 denotes the quantity of residual points, chosen at random from the entire computational domain and

<!-- formula-not-decoded -->

The total Loss function of PCM-NN is the weighted sum of 𝐿𝑜𝑠𝑠 𝑑𝑎𝑡𝑎 and 𝐿𝑜𝑠𝑠 𝑜𝑑𝑒 , and the choice of weights depends on the specific requirements and data characteristics of the problem. By minimizing this total Loss, PCM-NN can simultaneously utilize observational data and physical laws to achieve efficient and accurate pest prediction.

## 2.3. Experiment Settings

As illustrated in Table 2, the depth and width of the neural network employed in our study, along with the number of iterations for the algorithm, were configured to optimize model performance. These configurations encompass the number of hidden layers, the quantity of neurons per layer, and the selection of activation functions, all of which were based on experimental validation and performance evaluation results. Crucially, the table also lists the optimal temperature and humidity for the soybean pod borer, which are 21°C and 84%, respectively. These values are derived from the fundamental survival characteristics of the pest itself. Additionally, we constrained the parameter 𝛼 within the range of [-1 . 372 , 0 . 628] , ensuring that the range of 𝐴 -𝛼 remains within [-1 , 1] .

Firstly, we determined the values of parameters 𝐴 and 𝐵 . Utilizing nonlinear least squares, we employed the annual seasonal average data of soybean pod borer from 2020 to 2023, along with the corresponding temperature and humidity data, and selected the first 1-22 days for nonlinear least squares fitting. The reason for making this choice is that, based on data observation, the initial 22 day data period is relatively close to the trend of the logistic growth curve. Consequently, we obtained the parameter values of 𝐴 = 0 . 372 and 𝐵 = 0 . 0008 . Fig. 6 presents the fitting results of the nonlinear least squares analysis. Our experimental setup aimed to ensure that the neural network model achieves optimal performance in predicting soybean pod borer occurrences, while taking into account environmental factors and specific characteristics of the pest.

## 3. Result

## 3.1. Fitting Results and Inferred Parameter

More importantly, Fig. 7 (b) showcases the inferred parameter 𝛼 over time. Unlike traditional estimation methods that provide a single, fixed value for alpha, our PCM-NN algorithm captures its dynamic nature. This parameter 𝛼

This subsection presents the fitting results of our proposed PCM-NN algorithm. By leveraging the PCM-NN, we aim to capture the dynamic nature of soybean pod borer outbreaks more accurately than traditional methods. To illustrate the fitting effects, Fig. 7 presents two graphs. Fig. 7 (a) shows the comparison between the actual outbreak of soybean pod borer and the fitted value of PCM-NN algorithm This graph clearly demonstrates the model's ability to capture the trends and fluctuations in the outbreak data, highlighting its robustness and reliability.

Figure 6: Nonlinear least squares fitting results. The bar chart in the figure represents the real data of soybean pod borer. The line (represented in green) is a curve obtained by fitting these real data points using nonlinear least squares method.

<!-- image -->

provides a more realistic representation of the underlying processes governing soybean pod borer outbreaks, reflecting changes in environmental conditions, pest management practices, and other relevant factors.

Upon observation, it is evident that the trend of 𝛼 relatively aligns with that of the actual data. Specifically, 𝛼 tends to increase when the population quantity (or other relevant metrics) exhibits an upward trend. Conversely, during periods of data decline, 𝛼 also exhibits a downward trend. While this correlation is not perfectly synchronous due to potential time lags inherent in the system, it is noteworthy that when 𝛼 is greater than zero, it indicates growth promotion, whereas when 𝛼 is less than zero, it indicates growth suppression. Furthermore, when 𝛼 exceeds -0.372, it exhibits a positive correlation with the data, whereas when 𝛼 falls below -0.372, it shows a negative correlation. This nuanced understanding of the dynamic behavior of 𝛼 provides deeper insights into the mechanisms driving soybean pod borer population dynamics.

More importantly, Fig. 7 (b) showcases the parameter 𝛼 inferred over time by our PCM-NN algorithm. Unlike traditional estimation methods that provide a single, fixed value for 𝛼 , our approach captures its dynamic nature. This parameter 𝛼 offers a more realistic representation of the underlying processes governing soybean pod borer outbreaks, reflecting variations in environmental conditions, pest management practices, and other pertinent factors.

## 3.2. Verification by ODE Solution and Predictive Performance of PCM-NN

To further validate the training effectiveness of our PCM-NN algorithm, we conducted two key tests: ODE backsolving verification and predictive performance assessment.

## 3.2.1. Verification

We verified the trained PCM-NN by substituting the inferred parameter 𝛼 back into the modified logistic equation (2) and solving it using a ODE solver. Fig. 8 (a) presents the results of this ODE back-solving. The simulated curve, obtained from the pest model with the inferred climatic modulation function 𝛼 , aligns well with the observed data. This alignment suggests that the training outcomes of PCM-NN are consistent with the underlying transmission mechanisms of the pest model. It confirms that PCM-NN has accurately captured the evolution of pest populations, as reflected in the changing nature of 𝛼 .

## 3.2.2. Predictive Performance Assessment

Weevaluated the predictive capability of PCM-NN in forecasting the daily occurrence of soybean pod borer during July and September 2024. Utilizing the observed data from the first day of 2024 annual average data set, we input this initial value into the model (2), incorporating the estimated 𝛼 by PCM-NN, to predict the subsequent occurrence trend. The prediction results are depicted in Fig. 8 (b). The predictive curve in Fig. 8 (b) exhibits a similar trend to both the interannual average line spanning from 2020 to 2024. It is worth noting that the predicted values also learned the trend of double peaks and are consistent with the real data. This observation underscores PCM-NN's ability to generate reliable predictions based on the inferred 𝛼 and the pest model. It demonstrates that PCM-NN not only fits historical data

Figure 7: PCM-NN fitting inference results. (a) The fitting results of the PCM-NN algorithm are presented. The light green line represents the actual data, while the dark green line depicts the data fitted by the PCM-NN algorithm. (b) The estimated value of the parameter 𝛼 inferred from the fitting results of PCM-NN is shown as a parameter curve over time, which is represented by a red line. The red dashed line represents the growth threshold line, while the black dashed line represents the un-correlated baseline.

<!-- image -->

Figure 8: The ODE inverse solution and prediction results of PCM-NN. (a) Comparison between real data and ODE inverse solution. The light green line represents the actual data, while the dark green line represents the ODE inverse solution. (b) Comparison between forecast curve and interannual average data including 2024. The red dashed line represents the actual data, while the black solid line represents the predicted curve.

<!-- image -->

accurately but also possesses the predictive power to anticipate future pest infestation trends. The ODE back-solving verification confirms the consistency of PCM-NN's training results with the pest model's mechanisms. Additionally, the predictive performance assessment highlights PCM-NN's capacity to forecast future soybean pod borer infestation trends with reasonable accuracy. These findings collectively demonstrate the robustness and practicality of PCM-NN in addressing real-world pest management challenges.

## 3.3. Fitting Accuracy on Three Evaluation Metrics

The PCM-NN algorithm demonstrates excellent fitting performance, as evidenced by the three key metrics: Mean Squared Error ( MSE ), Mean Absolute Error ( MAE ) and the coefficient of determination ( 𝑅 2 ). Specifically, the MSE value indicates the average of the squares of the errors-that is, the average squared difference between the estimated values and the actual data points. A lower MSE value suggests a better fit. MAE measures the average absolute difference between predicted values and actual observed values. The calculation method is to take the absolute difference between the predicted value and the true value of each sample, and then calculate the average of all samples. Similarly, the

Figure 9: Comparison of MSE , MAE , and 𝑅 2 Values for Different Evaluative Aspects.

<!-- image -->

<!-- image -->

<!-- image -->

𝑅 2 value measures the proportion of the variance in the dependent variable that is predictable from the independent variables. An 𝑅 2 value closer to 1 indicates a stronger relationship between the predicted and actual values. The formulas for MSE , MAE and 𝑅 2 are as follows:

<!-- formula-not-decoded -->

Where 𝑛 is the total number of samples, and 𝑦 𝑖 represents the true value of the 𝑖 -th sample, which is the actual observed data. ̂ 𝑦 𝑖 indicate the predicted value of the 𝑖 -th sample. As shown in Fig. 9, PCM-NN demonstrates excellent fitting performance across three metrics, indicating that the model fits the data very well. Furthermore, when the parameter 𝛼 inferred using PCM-NN is substituted into the pest population model (2) and solved using an ODE solver, the resulting data still shows a high level of consistency with the real data, confirming the accuracy of the inferred parameter 𝛼 . Additionally, when compared with the interannual average data from 2020 to 2024, the model's predictions show a high degree of agreement with the true values, further validating the reliability of our proposed method.

## 4. Discussion

A standardized field monitoring was implemented to synchronize pest population dynamics with microclimatic factors across five consecutive growing seasons from 2020 to 2024 at the Soybean Regional Technology Innovation Center research base of Jilin Agricultural University, located in the suburban agroecosystem of Changchun City, Jilin Province, Northeast China. Here, we employ sex pheromone-baited traps to collect data on the male adult soybean pod borer and monitor population dynamics during the soybean growing season (May-September); microclimate data comprising daily-averaged temperature ( ◦ C) and relative humidity (%) records were obtained from Changchun

In this study, we developed the pest correlation model neural network (PCM-NN) algorithm, an improvement upon the physics-informed neural network (PINN) framework, specifically designed for fitting and predicting the soybean pod borer population dynamics. The PCM-NN framework mitigates the inherent limitations of traditional forecasting methods by integrating a mechanistic constraint differential equation model derived from pest physiology and environmental interactions. It reduces reliance on purely data-driven assumptions while maintaining adaptability to nonlinear ecological dynamics. The well-known classical Logistic model could effectively capture three-phase population dynamics: lag (slow growth) phase, exponential growth phase, and the stationary phase. By incorporating a couple of microclimatic factors (temperature 𝑇 and humidity 𝐻 ) through the bidirectional climatic modulation parameter function 𝛼 ( 𝑇, 𝐻, 𝑡 ) , we resolve the classical model's oversimplification of environmental modulation. Diverging from traditional explicit parameterizations of 𝛼 , our enhanced framework employs a fully connected neural network (NN) to represent it. We employ an enhanced PINN architecture to infer time-dependent parameter function 𝛼 , enabling data-driven discovery of nonlinear interactions between microclimatic factors and pest population dynamics while preserving ecological interpretability via embedded biophysical constraints.

National Benchmark Climate Station under the China Meteorological Administration. We implemented an interannual compositing processing to mitigate high-frequency observational noise inherent in time-series data, preserving critical phenological signals for mechanistic modeling. Through the fitting results of the PCM-NN algorithm, we systematically evaluated its predictive performance and predicted future occurrence trends of soybean pod borers. These research findings deepen the theoretical understanding of soybean pod borer ecology and provide practical tools for precision agriculture.

Although the PCM-NN algorithm demonstrates strong performance in both fitting and prediction tasks, certain limitations remain. For instance, its sensitivity to data noise may introduce bias into prediction outcomes. Future work should focus on optimizing the algorithm to enhance its robustness against noisy or incomplete data. Moreover, conducting sensitivity analyses of model parameters is essential to ensure the model's stability and reliability across diverse environmental conditions. Techniques such as regularization, data augmentation, and advanced noise-handling mechanisms can be employed to further improve the model's generalization capability and predictive accuracy. Currently, the model primarily considers temperature and humidity as environmental factors influencing the population dynamics of soybean pod borers. However, pest outbreaks are typically driven by the interplay of multiple factors. Future studies should incorporate additional variables, such as soil type, crop cultivar, and interspecies biological interactions, to construct a more comprehensive, multi-factor coupled model. Such an approach would offer deeper insights into the complex ecological mechanisms of pest emergence and provide a more robust basis for precision pest control strategies. While the PCM-NN algorithm performs well in long-term forecasting, its predictive accuracy may degrade over extended periods. Therefore, its integration into adaptive pest management systems is critical. By continuously monitoring pest population trends and environmental changes and regularly updating model parameters and predictions, real-time forecasting and dynamic responses to pest outbreaks can be achieved. This adaptive strategy would significantly enhance the efficiency and efficacy of pest control measures. Future research should conduct crossregional validations across diverse geographical areas and climatic conditions to evaluate the PCM-NN algorithm's generalizability and scalability. Comparing model predictions with actual pest occurrences in different locations will help assess its adaptability and accuracy. Furthermore, integrating the PCM-NN algorithm with complementary pest control technologies, such as biological and chemical control, could lead to the development of a more holistic and effective pest management system, thereby offering broader technical support for sustainable agricultural production.

## 5. Conclusions

This study establishes a hybrid neural-mechanistic framework (PCM-NN) that resolves temperature-humidity-pest couplings in soybean pod borer population dynamics. Validated against 2020-2023 field data from Changchun, China, PCM-NN achieves high prediction accuracy for 2024 outbreaks while maintaining ecological interpretability through embedded biological constraints. The model's capacity to balance data-driven learning with pest physiology principles offers actionable intelligence for precision pesticide deployment. Future enhancements will optimize data collection methods, improve data quality, and explore additional influencing factors.

## CRediT authorship contribution statement

Xu Chen: Writing - original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. Wenxuan Li: Writing - original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. Xiaoshuang Li: Investigation, Formal analysis, Data curation. Suli Liu: Writing - review &amp; editing, Writing - original draft, Supervision, Resources, Project administration, Funding acquisition, Conceptualization. Yu Gao: Writing - review &amp; editing, Writing - original draft, Supervision, Resources, Project administration, Funding acquisition, Conceptualization..

## Funding

Research of Suli Liu is supported by the National Natural Science Foundation of China (12301627), the Science and Technology Research Projects of the Education Office of Jilin Province, China (JJKH20250046KJ), the Technology Development Program of Jilin Province, China (20210508024RQ). Research of Yu Gao is supported by the Earmarked Fund for China Agriculture Research System of MOF and MARA (Grant No. CARS04), the National Key Research and Development Program of China (2023YFD1401000).

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data used in the study, such as weather data and pest data, are available upon request to the corresponding author. The source code in Python is available at the following repository: https://github.com/jluorganization/PCM-NN.

## References

- Braness, G., Coster, D., Bennett, G., 1991. Logistic models describing effects of temperature and humidity on residual effectiveness of chlorpyrifos and cyfluthrin formulations against German cockroaches (Dictyoptera: Blattellidae). Journal of economic entomology 84, 1746-1752.
- Amjad Bashir, M., Batool, M., Khan, H., Shahid Nisar, M., Farooq, H., Hashem, M., Alamri, S., A. El-Zohri, M., Alajmi, R.A., Tahir, M., et al., 2022. Effect of temperature &amp; humdity on population dynamics of insects' pest complex of cotton crop. Plos one 17, e0263260.
- Change, I.P.O.C., 2023. Technical Summary. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA. pp. 33-144. doi: 10.1017/9781009157896.002 .
- Chen, L., Song, B., Yu, C., Zhang, J., Zhang, J., Bi, R., Li, X., Ren, X., Zhu, Y., Yao, D., et al., 2022b. Identifying soybean pod borer ( Leguminivora glycinivorella ) resistance QTLs and the mechanism of induced defense using linkage mapping and RNA-seq analysis. International Journal of Molecular Sciences 23, 10910.
- Chen, C.J., Li, Y.S., Tai, C.Y., Chen, Y.C., Huang, Y.M., 2022a. Pest incidence forecasting based on internet of things and long short-term memory network. Applied Soft Computing 124, 108895.
- Deutsch, C.A., Tewksbury, J.J., Tigchelaar, M., Battisti, D.S., Merrill, S.C., Huey, R.B., Naylor, R.L., 2018. Increase in crop losses to insect pests in a warming climate. Science 361, 916-919.
- Fei, H., Cui, J., Zhu, S., Xia, Y., Xing, Y., Gao, Y., Shi, S., 2024. Integrative analyses of transcriptomics and metabolomics in immune response of Leguminivora glycinivorella Mats to Beauveria bassiana infection. Insects 15, 126.
- Fan, M., Wang, K., 1998. Optimal harvesting policy for single population with periodic coefficients. Mathematical biosciences 152, 165-178.
- Gao, Y., Shi, S., Xu, M., Cui, J., 2018. Current research on soybean pest management in China. Oil Crop Science .
- Hu, D.H., He, J., Zhou, Y.W., Feng, J.T., Zhang, X., 2012. Synthesis and field evaluation of the sex pheromone analogues to soybean pod borer Leguminivora glycinivorella . Molecules 17, 12140-12150.
- Garrido-Jurado, I., Valverde-García, P., Quesada-Moraga, E., 2011. Use of a multiple logistic regression model to determine the effects of soil moisture and temperature on the virulence of entomopathogenic fungi against pre-imaginal mediterranean fruit fly ceratitis capitata. Biological Control 59, 366-372.
- Jiang-sheng, G., Jing-yi, F., Xia-ping, F., 2021. Hyperspectral imaging for detection of Leguminivora glycinivorella based on 3d few-shot metalearning model. Spectroscopy and Spectral Analysis 41, 2171-2174.
- Kuzmin, A., Anisimov, N., Malashonok, A., 2020. Soybean moth Leguminivora glycinivorella ( Lepidoptera: Tortricidae ): harmfulness in the conditions of the south of the Amur region, in: IOP Conference Series: Earth and Environmental Science, IOP Publishing. p. 012026.
- Kumar, G.S., Chowdary, L.R., Sarada, O., 2023. Seasonal incidence of major insect pests of groundnut and their natural enemies in relation to meteorological parameters. ANGRAU .
- Le, V.V., Ishitani, M., Komai, F., Yamamoto, M., Ando, T., 2006. Sex pheromone of the soybean pod borer, Leguminivora glycinivorella ( Lepidoptera: Tortricidae ): Identification and field evaluation. Applied entomology and zoology 41, 507-513.
- Ma, G., Ma, C.S., 2022. Potential distribution of invasive crop pests under climate change: incorporating mitigation responses of insects into prediction models. Current Opinion in Insect Science 49, 15-21.
- Liu, Z., Zheng, B., Li, J., Yu, J., preprint. Dynamical analysis of a pest control model with the cumulative lethal effect of periodic pesticide spraying. Available at SSRN 5078116 .
- Malaguit, J.C., Mendoza, V.M.P., Tubay, J.M., Mata, M.A.E., 2023. Identifying patterning behavior in a plant infestation of insect pests. Mathematical Biosciences 362, 109032.
- Shi, S., Cui, J., Zhu, S., Xu, W., Wang, X., 2018. Genetic differentiation of soybean pod borer in different geographical populations based on mitochondrial COI gene sequence. Acta Phytophylacica Sinica 45, 214-222.
- Ponti, L., Gutierrez, A.P., de Campos, M.R., Desneux, N., Biondi, A., Neteler, M., 2021. Biological invasion risk assessment of tuta absoluta: mechanistic versus correlative methods. Biological Invasions 23, 3809-3829.
- Skendžić, S., Zovko, M., Živković, I.P., Lešić, V., Lemić, D., 2021. The impact of climate change on agricultural insect pests. Insects 12, 440.
- Sun, S., Pu, L., Lin, Z., 2018. Dynamics of the logistic harvesting model with infinite delay on periodically evolving domains. Commun. Math. Biol. Neurosci. 2018, Article-ID.
- Sokame, B.M., Tonnang, H.E., Subramanian, S., Bruce, A.Y., Dubois, T., Ekesi, S., Calatayud, P.A., 2021. A system dynamics model for pests and natural enemies interactions. Scientific reports 11, 1401.
- Tang, S., Cheke, R.A., 2008. Models for integrated pest control and their biological implications. Mathematical Biosciences 215, 115-125.
- Yang, M., Wang, Y., Ding, W., Li, H., Zhang, A., 2024. Predicting habitat suitability for the soybean pod borer Leguminivora glycinivorella (Matsumura) using optimized maxent models with multiple variables. Journal of Economic Entomology 117, 1796-1808.
- Wakamura, S., 1992. Development in application of synthetic sex pheromone to pest management. Jpn. Pestic. Inform. 61, 26-31.