---
id: arxiv-2205.07723
title: Interpretable Machine Learning for Pest Prediction
year: 2022
language: en
---

## Pest Presence Prediction Using Interpretable Machine Learning

Ornela Nanushi ∗ 1 , Vasileios Sitokonstantinou ∗ 1,2 , Ilias Tsoumas 1 and Charalampos Kontoes 1

1

National Observatory of Athens, IAASARS, BEYOND Center, Penteli, Greece

Email: {ornela.nanushi, vsito, i.tsoumas, kontoes}@noa.gr

2 Laboratory of Remote Sensing, National Technical University of Athens, Athens, Greece

Abstract -Helicoverpa Armigera, or cotton bollworm, is a serious insect pest of cotton crops that threatens the yield and the quality of lint. The timely knowledge of the presence of the insects in the field is crucial for effective farm interventions. Meteo-climatic and vegetation conditions have been identified as key drivers of crop pest abundance. In this work, we applied an interpretable classifier, i.e., Explainable Boosting Machine, which uses earth observation vegetation indices, numerical weather predictions and insect trap catches to predict the onset of bollworm harmfulness in cotton fields in Greece. The glass-box nature of our approach provides significant insight on the main drivers of the model and the interactions among them. Model interpretability adds to the trustworthiness of our approach and therefore its potential for rapid uptake and context-based implementation in operational farm management scenarios. Our results are satisfactory and the importance of drivers, through our analysis on global and local explainability, is in accordance with the literature.

Keywords -interpretable machine learning, pest insect appearance, helicoverpa armigera, numerical weather predictions, vegetation indices, precision agriculture

## I. INTRODUCTION

Greece is the primary cotton producer for the European Union (EU) and the fifth-largest cotton exporter in the world; which makes cotton one of the most important crops for the national economy [1], [2]. It is therefore imperative to protect cotton fields from pests and diseases with timely and effective actions to avoid damages. Helicoverpa armigera, also called cotton bollworm, is a serious threat to the crop, resulting in yield losses and suboptimal lint quality. This pest is widely abundant, especially in countries with warm or temperate climate like Greece [3]. In this work, we implement an interpretable machine learning approach to detect pest presence using satellite observations and meteorological data. By doing so, we identify the onset of harmfulness. In other words, consecutive presence estimations of the pest act as information about upcoming population peaks. This enables the farmers to optimize their pest management process.

In order to successfully protect crops from pests, we need to understand their life cycle and thereby intervene before the abundance of insects becomes detrimental. Cotton bollworm's life cycle is relatively fast, and it takes place in four stages. First, the female moths lay the eggs. If the weather conditions are favourable, these eggs can hatch in less than three days. Then the eggs hatch and larvae emerge. This is the destructive phase of the pest. Larvae then turn into pupae, which are

* These authors contributed equally to this work

usually buried at a depth of 4 to 10 centimetres in soil and take 10 to 15 days to develop in a cocoon. An adult moth hatches out of the cocoon, ready to start the reproductive cycle all over again. Generally, it takes the pest approximately one month to complete its life cycle [4].

Deep learning models, and mostly Convolutional Neural Networks (CNNs), have been widely used to recognize plant pests and diseases on plant images [5]. The aforementioned techniques work on close-up photos from the field that cannot be available frequently over large areas. As an alternative, one can use coarser spatial resolution data that can provide better coverage and temporal resolution, such as weather predictions and satellite images. For this, however, we need pest traps to know the occurrence and population of insects. There are different types of pest traps, i.e., pheromone, light or sticky traps etc. [6]. Using such traps renders the problem quantitative, i.e., the interest no longer lies on the pest or damage recognition, but on the estimation of its population.

Several studies have worked on estimating pest population (regression) [7] or detecting significant presence (binary classification) [8], [9]. With reference to the latter, knowing the exact population of pests is not always crucial. Instead, action thresholds are used to classify the amount of pests as harmful or not [10]. One can find approaches that make use of i) physical models [11] or ii) data driven models that employ remote sensing and in-situ measurements [8], [12]. It is worth noting that most related studies use weather data, whereas in fewer cases remote Earth observations are used to capture the changes caused by the pests, but also the favourable vegetation conditions for their occurrence [12]. Recurrent Neural Networks (RNN) have been applied to weather data time-series, accounting for the temporal evolution of features and capturing the cyclical nature of pest abundance [13]. In other words, when trying to predict pest occurrence at a given time instance, one cannot ignore the weather conditions and the vegetation status of previous days [14].

Traditional machine learning is also widely used in the literature, with particular focus on regression models. In [15], the authors perform multivariate regression analyses, and they find that temperature and rainfall have significant correlations with the cotton bollworm population. Similarly, in [16] they find temperature, wind speed and sunshine hours to be important. Furthermore, in [17] they perform binary classification for pest occurrence detection using relative humidity and temperature. Complementary to weather factors, some studies also use host plant phenology represented by the Normalized Difference Vegetation Index (NDVI) or other vegetation indices [8]. This is done in order to study the association between the crop's growth and the pest population. Satellite derived vegetation indices are also used in [18], where they introduce an ecology oriented model for population dynamics.

Motivated by real life requirements, we designed and implemented a predictive method to detect harmful cotton bollworm presence in cotton fields. Our model is interpretable, which means that one can understand how it arrived to a specific decision and which are the drivers that mattered the most. This allows the user of the model's outputs (e.g., farmers) to understand and trust them and therefore adhere to the recommendations, and even fine-tune them with their expert knowledge. Our approach makes use of both vegetation indices and weather data, and to the best of our knowledge there is no similar work for cotton bollworm presence estimation. We perform two experiments, i.e., one that makes use of past trap catches and one that does not, yielding satisfactory results for both. The latter experiment is of great significance as it allows for the method to be applicable anywhere in space, irrespective of the presence of pest traps in the vicinity.

## II. METHODOLOGY

Our work focuses on the prediction of cotton bollworm presence based on meteorological data, satellite earth observations and past trap catches. This section elaborates on the formulation of the problem, and the acquisition, pre-processing and engineering of the data to analysis-ready features. Fig. 1 shows an overview of the steps followed.

Fig. 1: Workflow of the method for bollworm presence prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen representa un diagrama de líneas que muestra la relación entre la entrada de datos y la salida de datos en un modelo de aprendizaje automático. El diagrama muestra cómo los datos de entrada se procesan y se transforman en datos de salida a través de diferentes etapas, incluyendo la extracción de características, la modelización y la evaluación. La tendencia principal del diagrama es que la salida de datos es una representación más compleja y detallada de la entrada de datos, con una mayor cantidad de características y una mejor precisión. El diagrama también muestra que la salida de datos es influenciada por la calidad y la cantidad de los datos de entrada, y que la modelización y la evaluación son esenciales para mejorar la precisión de la salida de datos. En resumen, el diagrama muestra la transformación de los datos de entrada en datos de salida a través de diferentes etapas, y cómo la calidad y la cantidad de los datos de entrada influyen en la precisión de la salida de datos. La tendencia principal es que la salida de datos es una representación más compleja y detallada de la entrada de datos, con una mayor



## A. Problem formulation

Let T be the set of traps we have at our disposal. We note as t ij ∈ T the entity describing trap i on date j . Every t ij can be expressed as t ij = ( x ij , y ij ) , where x ij ∈ I R d is a d dimensional vector containing the corresponding weather and satellite features, and y ij ∈ { 0 , 1 } , with 0 referring to pest absence and 1 referring to pest presence. Our aim is to find a model M : I R d → { 0 , 1 } , so that for any trap t ij , to predict the onset of harmful presence of bollworm population that will in turn signal the time for intervention.

Explainable classifier approach: There exist many sophisticated models that could be appropriate for our problem. However, we should bear in mind that in the agricultural sector, whoever be the user, it is common to have substantial empirical knowledge. For example, someone who cultivates cotton is likely to know when to sow, the crop's enemies, the favourable conditions etc. Therefore, it is crucial to make these users trust the model and its outputs [19]. Furthermore, if the users have some insight on the main drivers and find the result unjustifiable, they can disregard the prediction or frame it in context and then take appropriate action. The above examples point out the need for model transparency, which can be achieved using explainable machine learning [20]. We therefore chose to proceed using an interpretable classifier.

The model we used is the Explainable Boosting Machine (EBM), as implemented in the InterpretML framework. In machine learning, there is often a trade-off between accuracy and intelligibility. This is not true for EBM that achieves a performance comparable to powerful black-box models, while offering global and local explanations on the predictions [21]. EBM is an augmented version of the Generalized Additive Models (GAMs), which are expressed by (1).

$$g ( E ( y ) ) = \beta _ { 0 } + \sum f _ { j } ( x _ { j } )$$

In practice, EBM is a GAM model with interactions based on the GA2M method, expressed by (2) [22].

$$g ( E ( y ) ) = \beta _ { 0 } + \sum f _ { j } ( x _ { j } ) + \sum f _ { i j } ( x _ { i } , x _ { j } )$$

Every feature function f j is learnt using many shallow decision trees. The learning is achieved using one predictive feature at a time in round-robin pass over the train data, while performing gradient updates. In more detail, we train a tree on the first feature, then in boosting fashion we update the residual and move to the second feature, then we train another tree and so on. The learning rate is low, and thus the feature order does not matter. Interaction functions, f ij , are learnt via the FAST method [22].

All features' contributions, together with the interactions, yield a logit score. Scores are then summed and passed to the link function g , which is chosen depending on the context. In binary classification, as in our case, EBM uses the logarithmic loss. Since the model is additive, the contributions of the terms can be sorted and visualized. This way, we can understand the main drivers of the model and produce new domain knowledge, but also enhance the trust on the outputs.

## B. Data collection

Trap data: To obtain insect population measurements, we collaborated with the company Corteva Agriscience Hellas that has a trap network for helicoverpa armigera. The network consists of pheromone traps in 26 different locations in the wider region of Central Macedonia, Greece. The traps are located in such a distance so as to not interact with each other and are examined (trapped insect counting) by a specialist every 3-5 days. The observations take place from June 2020 until early September 2020 and June 2021 until early September 2021. The trap data include i) the trap locations, ii) the number of pests on each trap and iii) the Day of Year (DoY) they were recorded. In total, there are 10 locations for 2021 and 16 locations for 2020.

Meteorological data. In real life scenarios, exact weather conditions are very hard to obtain. This is true due to the absence of a dense network of weather stations. To overcome this, we use numerical weather predictions using our own configuration of WRF-ARW [23], [24]. The model is of high spatial resolution (2 km), and predictions are made hourly. For each trap location, we obtained daily values for air (2 m) and soil temperature (0 m), relative humidity (RH), accumulated precipitation (AP), dew point (DP), and wind speed (WS). These parameters have been extensively used in related work.

Satellite data. We used Sentinel-2 images to capture the vegetation status (at the location of the traps) and its evolution through time [25]. Using atmospherically corrected Sentinel2 images, we calculated a number of vegetation indices that highlight particular characteristics of the crops (e.g., moisture, physiological stress etc.) that are known to i) drive the occurrence of pests, but also ii) capture the vegetation cover changes caused by the insects [26]. In detail, we used the normalized difference vegetation (NDVI), water (NDWI), moisture (NDMI), greenness (GI) and greenness chlorophyll (GCVI) indices.

## C. Feature engineering

We provide pest presence predictions for each trap and for each date that we have catches. Each of those instances in time and space (trap/inspection day, 526 instances) is described by a series of features that are engineered using the data variables described earlier. Regarding the trap data, we use the coordinates of the trap locations, the corresponding dates they were visited and the number of insects observed per visit. In the feature space, we included the catches of the three latest visits prior to the day of prediction. The day of visit was encoded using the sine and cosine of the DoY, which is common for cyclical features. The number of catches for the day of prediction function as the labels for training and evaluation. The labels are binarized to pest presence or absence according to a certain threshold ( t = 10 ), which represents the number of insects above which the pest is considered harmful to the crop, also known as the action threshold.

The meteorological and vegetation index variables were engineered into accumulated features to capture the near-past (7 days) information that drives pest occurrence. Specifically, the accumulated vegetation indices were calculated using the cumulative integral of the time-series curve, whereas the accumulated weather features were calculated by summing the daily values over the last 7 days. Growing degree days, which capture the effective growth time of the plant, were also calculated according to (3) [27]. T base refers to the temperature under which the cotton does not develop and is equal to 15.6 ◦ C, and T max , T min are the maximum &amp; minimum air temperatures (2 m), respectively.

$$G D D = \max \left ( \frac { T _ { \max } + T _ { \min } } { 2 } - T _ { b a s e } , 0 \right ) \quad ( 3 ) \quad \exp l a p a l { ( 3 ) } \quad \exp l a p a l { ( 3 ) }$$

The data was standardized using a standard scaler. The EBM was run using 100 inner bags, 100 outer bags, and a learning rate of 0.01 that according to [21] is an appropriate tuning to achieve both high accuracy and interpretability.

## III. EXPERIMENTS &amp; RESULTS

As described in Sec. II-C, we used cumulative integrals of vegetation indices, accumulated and current weather data, and past trap catches to predict the occurrence of bollworms. We also ran experiments without including the insect catches in order to explore the capability of our model to predict pest presence anywhere in space, and not just for regions for which we have traps. Table I depicts the accuracy, AUC and F1 score for both cases, averaged over 10 random train/test splits (70/30).

TABLE I: Performance of the pest prediction model for Case A with all features, and Case B without trap related features.

Según Interpretable Machine Learning for Pest Prediction (2022), Class: Accuracy, Case B: 0.75 ± 0.03.
Según Interpretable Machine Learning for Pest Prediction (2022), Class: AUC, Case B: 0.83 ± 0.03.
Según Interpretable Machine Learning for Pest Prediction (2022), Class: F1 score, Case A: Pest absence, Case B: 0.75 ± 0.04.
Según Interpretable Machine Learning for Pest Prediction (2022), Class: F1 score, Case A: Pest presence, Case B: 0.74 ± 0.04.
As expected, Case A considerably outperforms Case B. It should be noted, however, that Case B showcases promising performance given the model was able to predict pest presence using only earth observations and weather data. In the context of an operational pest management service, the Case B approach has great value, as it can be applicable to any cotton field without the need of being near a pest trap.

The pest presence threshold, set at 10 catches, amounts to approximately 3 insects a day, as traps are visited every 3-5 days. According to local agronomists that we consulted, a couple of catches a day are not considered harmful. Nevertheless, the threshold is only an approximation. Fig. 4 illustrates the seriousness of the errors of our model (Case A) by visualizing how close to the action threshold they occurred. The left histogram depicts the distribution of catches for the model errors. As expected, most errors are situated near the action threshold.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de barras que muestra la distribución de errores en un modelo de aprendizaje automático. El gráfico tiene dos columnas: una para el error tipo "FN" (False Negative) y otra para el error tipo "FP" (False Positive). El eje de la izquierda muestra el número de errores, y el eje de la derecha muestra el porcentaje de errores. La tendencia principal del gráfico es que el error tipo "FN" es mayor que el error tipo "FP". Esto significa que el modelo es más propenso a fallar en la detección de los casos positivos (False Negative) que en la detección de los casos negativos (False Positive). La distribución de los errores es simétrica, con un pico en el centro del gráfico, lo que sugiere que el modelo es más preciso en la detección de los casos positivos y negativos en el centro del rango de valores. En resumen, el gráfico muestra que el error tipo "FN" es mayor que el error tipo "FP" en el modelo de aprendizaje automático, y la distribución de los errores es



∐√̂[˜√

Fig. 2: Distribution of the number of catches for all trap measurements (right) and for the model errors (left).

Using the InterpretML framework, we extracted local and global explainability reports. Global explanations account for all model predictions, whereas local explanations are provided for each individual prediction. Table II shows the global explanations for Cases A and B. The scores indicate how much each feature affected the result. For Case A, the features with the strongest impact were the past trap catches. This is expected since pest presence depends on the population of the previous days. For Case B, it is mostly the weather features, both current and accumulated, as well as their interactions (acting as a new parameter) that compensate for the lack of trap information. Wind speed, relative humidity, precipitation, air, and soil temperature appear to be very important features for both cases. This is also supported by the literature [15], [16], [18]. Time features, such as cos(DoY) and sin(DoY), are also important since there is clear seasonality in bollworm population (see Fig. 3). Finally, the vegetation indices, and interactions of them with weather features for Case B, are also found among best features. This supports the choice of combining satellite earth observations with weather data, which has not been done before for bollworm presence estimation.

TABLE II: Feature importance according to EBM's global explainability report for Case A with all features and Case B without trap related data.

Según Interpretable Machine Learning for Pest Prediction (2022), Case A: Features, Case A: Scores, Case B: Features, Case B: Scores.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: Catches t-1, Case A: 0.29, Case B: WS (min) - AP acc., Case B: 0.13.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: Catches t-2, Case A: 0.16, Case B: WS (max) - T at 0 m (max) acc., Case B: 0.12.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: T at 2 m (min), Case A: 0.15, Case B: RH (min) acc. - GDD, Case B: 0.12.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: cos(DoY), Case A: 0.13, Case B: cos(DoY), Case B: 0.11.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: GI, Case A: 0.13, Case B: T at 0 m (max) acc. - cos(DoY), Case B: 0.11.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: RH (max), Case A: 0.13, Case B: WS (max), Case B: 0.10.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: RH acc. (max), Case A: 0.12, Case B: NDMI - WS (min), Case B: 0.09.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: NDWI, Case A: 0.11, Case B: GCVI, Case B: 0.09.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: Lon, Case A: 0.11, Case B: NDVI - NDMI, Case B: 0.09.
Según Interpretable Machine Learning for Pest Prediction (2022), Case A: GCVI, Case A: 0.10, Case B: GCVI - sin(DoY), Case B: 0.09.
The aforementioned experiments, used train and test data randomly selected from all the available traps. Nevertheless, it is also important to observe the temporal pattern of our predictions. The idea is to identify when the presence is significant, indicating the population peak over the next days and thus the need to intervene. To do so, we needed to see how the model would perform when tested on the entire time-series of a trap. Specifically, instead of training our model (Case A) using samples from all the traps, we would leave out one trap at a time and use it as a test set. Fig.3 shows the actual trap catches against time, together with the action threshold that indicates whether a point should have been classified as pest presence or not. This is an indicative example for a single trap located in Central Macedonia, Greece. The green dots represent pest presence predictions, the red dots represent pest absence predictions, and the dashed line represents the action threshold ( t = 10 ). We can conclude that the model performs rather well for this particular trap. The principal troughs and peaks are clearly identified, indicating that the model is able to predict the onset and termination of pest harmfulness. It is also worth noting how the model was able to identify the end of the bollworm population cycle after DoY 220.

Fig. 3: An indicative time-series of insect catches from a single trap in Macedonia, Greece. The green dots are the pest presence predictions and the red dots are the pest absence predictions. The dashed line represents the action threshold set at t = 10 .



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de líneas que muestra la tendencia de la acción de umbral y la predicción de ausencia y presencia de la pestilencia. El gráfico tiene dos líneas: una en rojo que representa la acción de umbral y otra en verde que representa la predicción de ausencia y presencia de la pestilencia. La línea en rojo se mantiene relativamente constante a lo largo de la escala de la x, mientras que la línea en verde muestra una tendencia de crecimiento. La conclusión principal del gráfico es que la predicción de ausencia y presencia de la pestilencia es mayor que la acción de umbral en la mayoría de los casos. Esto sugiere que la predicción de la pestilencia es más sensible que la acción de umbral en la mayoría de los casos. Sin embargo, en algunos casos, la predicción de la pestilencia es menor que la acción de umbral, lo que sugiere que la predicción de la pestilencia no es siempre más sensible que la acción de umbral. En resumen, el gráfico sugiere que la predicción de



To further investigate this test trap, we used the local explanations of the InterpretML framework. We indicatively examine the prediction for DoY=180. This one, despite being a peak, was not detected as such. Looking at the local explainability graph in Fig. 4, we can gain insight on this decision. The coloured bars indicate which features drove the decision towards pest presence (green) and which features towards pest absence (red). The predicted class is assigned with a probability of only 0.509, indicating uncertainty. The feature which had the strongest impact towards the true label was the interaction of GI with Catches t-3. This is very logical since the catches at the instance t-3 indicated pest presence. On the other hand, the catches at the instance t-1 strongly suggest pest absence. By examining Fig. 3, we can see that the pest catches in the previous visit were zero and hence unlikely to have strong pest presence only four days later.

Fig. 4: Local explainability plot for an uncertain prediction.



> **[💡 Descripción de Imagen VLM]:** La imagen es un gráfico de barras que muestra la tendencia de la temperatura y la humedad relativa en un determinado período de tiempo. El gráfico se divide en dos secciones: la sección superior muestra la temperatura y la sección inferior muestra la humedad relativa. La temperatura se mide en grados Celsius y se muestra en la escala de la izquierda. La temperatura es relativamente constante durante el período de tiempo, con un valor promedio de aproximadamente 25°C. La humedad relativa se mide en porcentaje y se muestra en la escala de la derecha. La humedad relativa es relativamente constante durante el período de tiempo, con un valor promedio de aproximadamente 60%. El gráfico también muestra la tendencia de la temperatura y la humedad relativa en el tiempo. La temperatura y la humedad relativa son relativamente constantes durante el período de tiempo, con un valor promedio de aproximadamente 25°C y 60%, respectivamente. En resumen, el gráfico de barras muestra la tendencia de la temperatura y la humedad relativa en un determinado período de tiempo. La temperatura y la hum



## IV. CONCLUSIONS AND FUTURE WORK

In this work, we used an interpretable classifier to detect significant cotton bollworm presence to indicate the onset of pest harmfulness. This is the first study that uses both weather data and earth observations to model the occurrence of this pest. We ran two experiments: i) one that incorporates past trap catches in the feature space and ii) one that uses only meteorological parameters and vegetation indices. Both approaches yielded satisfactory results, with model (i) outperforming model (ii). Model (ii), however, is of particular interest in the context of pest management, as it can be applicable anywhere in space without being dependent on the presence of pheromone (or other) traps. Moreover, by using the InterpretML framework, we can understand and trust the model's decisions. Not only we predict the onset of the rise in pest population, but we also provide significant insight on the main drivers of the model's outcomes. This makes our approach transparent and easy to understand.

Future work includes forecasting pest presence for the next two to five days using numerical weather predictions and projections of vegetation indices. Moreover, using a larger trap dataset we can enhance the performance of model (ii) and thus expand inference spatially, in areas where no traps are set, resulting in pest presence-absence maps.

## ACKNOWLEDGMENTS

This work has been supported by the EU H2020 projects e-shape (No 820852) &amp; EIFFEL (No 101003518). The authors would like to acknowledge Corteva Agriscience Hellas S.A. for providing the trap data and Nikolaos S. Bartsotas for providing the numerical weather predictions.

## REFERENCES

- [1] V. Engonopoulos, V. Kouneli, A. Mavroeidis, S. Karydogianni, D. Beslemes, I. Kakabouki, P. Papastylianou, and D. Bilalis, 'Cotton versus climate change: the case of greek cotton production,' Notulae Botanicae Horti Agrobotanici Cluj-Napoca , vol. 49, no. 4, pp. 12 54712 547, 2021.
- [2] E. Tsiros, C. Domenikiotis, and N. Dalezios, 'Assessment of cotton phenological stages using agroclimatic indices: An innovative approach,' Italian Journal of Agrometeorology , pp. 50-55, 02 2009.
- [3] C. Jones, H. Parry, W. Tay, D. Reynolds, and J. Chapman, 'Movement ecology of pest helicoverpa: Implications for ongoing spread,' Annual Review of Entomology , vol. 64, pp. 1-19, 10 2018.
- [4] S. F. MP Zalucki, G Daglish and P. Twine, 'The biology and ecology of heliothis-armigera (hubner) and heliothis-punctigera wallengren (lepidoptera, noctuidae) in australia - what do we know,' Australian Journal of Zoology , vol. 34, no. 6, pp. 779 - 814, 1986.
- [5] J. Liu and X. Wang, 'Plant diseases and pests detection based on deep learning: a review,' Plant Methods , vol. 17, 02 2021.
- [6] N. D. Epsky, W. L. Morrill, and R. W. Mankin, 'Traps for capturing insects,' Encyclopedia of entomology , vol. 3, pp. 2318-2329, 2008.
- [7] J. Bana, S. Saxena, P. Ghoghari, H. Sharma, and D. Sharma, 'Prediction of mango hopper, idioscopus nitidulus (walker) based on diurnal variations under south gujarat climatic conditions,' vol. 6, pp. 1042-1045, 10 2018.
- [8] S. Skawsang, M. Nagai, N. Tripathi, and P. Soni, 'Predicting rice pest population occurrence with satellite-derived crop phenology, ground meteorological observation, and machine learning: A case study for the central plain of thailand,' Applied Sciences , vol. 9, p. 4846, 11 2019.
- [9] L. E. Aparecido, G. Rolim, J. Moraes, C. Costa, and P. Souza, 'Machine learning algorithms for forecasting the incidence of coffea arabica pests and diseases,' International Journal of Biometeorology , vol. 64, 12 2019.
- [10] P. Martin, B. Wiseman, and R. Lynch, 'Action thresholds for fall armyworm on grain sorghum and coastal bermudagrass,' The Florida Entomologist , vol. 63, p. 375, 12 1980.
- [11] H. Tonnang, H. Bisseleua, L. Biber-Freudenberger, D. Salifu, S. Subramanian, V. Ngowi, R. Guimapi, A. Bruce, F. M. Moukam Kakmeni, H. Affognon, S. Niassy, T. Landmann, N. Thomas Frank, S. Pedro, T. Johansson, C. Tanga, P. Nana, K. Fiaboe, S. Mohamed, and C. Borgemeister, 'Advances in crop insect modelling methods-towards a whole system approach,' Ecological Modelling , vol. 354, pp. 88-103, 06 2017.
- [12] J. Zhang, Y. Huang, R. Pu, P. González-Moreno, L. Yuan, K. Wu, and W. Huang, 'Monitoring plant diseases and pests through remote sensing technology: A review,' Computers and Electronics in Agriculture , vol. 165, p. 104943, 10 2019.
- [13] Q. Xiao, W. Li, Y. Kai, P. Chen, J. Zhang, and B. Wang, 'Occurrence prediction of pests and diseases in cotton on the basis of weather factors by long short term memory network,' BMC Bioinformatics , vol. 20, 12 2019.
- [14] M. Adan, E. Abdel-Rahman, S. Gachoki, B. Muriithi, H. M. Lattorff, V. Kerubo, T. Landmann, S. Mohamed, H. Tonnang, and T. Dubois, 'Use of earth observation satellite data to guide the implementation of integrated pest and pollinator management (ippm) technologies in an avocado production system,' Remote Sensing Applications: Society and Environment , vol. 23, p. 100566, 06 2021.
- [15] A. Srivastava, M. Nayak, Y. Singh, D. Tomar, and K. Gurjar, 'Weather based prediction of chickpea helicoverpa armigera population in bundelkhand agroclimatic zone of madhya pradesh,' Mausam , vol. 67, pp. 377-388, 01 2016.
- [16] A. Hameed, M. Shahzad, S. Ahmad, and D. Karar, 'Forecasting and modelling of helicoverpa armigera (hub.) in relation to weather parameter in multan, punjab, pakistan,' Pakistan journal of zoology , vol. 47, pp. 15-20, 02 2015.
- [17] D. Markovic, D. Vujiˇ ci´ c, S. Tanaskovic, B. Djordjevic, S. Ran ¯ di´ c, and Z. Stamenkovic, 'Prediction of pest insect appearance using sensors and machine learning,' Sensors , vol. 21, p. 4846, 07 2021.
- [18] M. Blum, D. Nestel, Y. Cohen, E. Goldshtein, D. Helman, and I. Lensky, 'Predicting heliothis (helicoverpa armigera) pest population dynamics with an age-structured insect population model driven by satellite data,' Ecological Modelling , vol. 369, pp. 1-12, 01 2018.
- [19] M. T. Ribeiro, S. Singh, and C. Guestrin, '" why should i trust you?" explaining the predictions of any classifier,' in Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining , 2016, pp. 1135-1144.
- [20] V. Belle and I. Papantonis, 'Principles and practice of explainable machine learning,' Frontiers in Big Data , vol. 4, p. 688969, 07 2021.
- [21] H. Nori, S. Jenkins, P. Koch, and R. Caruana, 'Interpretml: A unified framework for machine learning interpretability,' arXiv preprint arXiv:1909.09223 , 2019.
- [22] Y. Lou, R. Caruana, J. Gehrke, and G. Hooker, 'Accurate intelligible models with pairwise interactions,' in Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining , 2013, pp. 623-631.
- [23] W. C. Skamarock, J. B. Klemp, J. Dudhia, D. O. Gill, Z. Liu, J. Berner, W. Wang, J. G. Powers, M. G. Duda, D. M. Barker et al. , 'A description of the advanced research wrf model version 4,' National Center for Atmospheric Research: Boulder, CO, USA , vol. 145, p. 145, 2019.
- [24] V. Sitokonstantinou, A. Koukos, C. Kontoes, N. S. Bartsotas, and V. Karathanassi, 'Semi-supervised phenology estimation in cotton parcels with sentinel-2 time-series,' in 2021 IEEE International Geoscience and Remote Sensing Symposium IGARSS . IEEE, 2021, pp. 8491-8494.
- [25] D. Kumar, S. Poloju, T. Neelima, M. Uma Devi, K. Suresh, and C. Murthy, 'Monitoring of spectral signatures of maize crop using temporal sar and optical remote sensing data,' International Journal of Bio-resource and Stress Management , vol. 12, pp. 745-750, 01 2022.
- [26] J. Segarra, M. Buchaillot, J. Araus, and S. Kefauver, 'Remote sensing for precision agriculture: Sentinel-2 improved features and applications,' Agronomy , vol. 10, p. 641, 05 2020.
- [27] A. Sharma, R. Deepa, S. Sankar, M. Pryor, B. Stewart, E. Johnson, and A. Anandhi, 'Use of growing degree indicator for developing adaptive responses: A case study of cotton in florida,' Ecological Indicators , vol. 124, p. 107383, 05 2021.