---
id: arxiv-2403.19273
title: A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors
year: 2024
country: Internacional
source: ArXiv (cs.LG, cs.AI)
doc_type: Artículo científico
language: en
tags:
  - temperatura
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors

Forkan Uddin Ahmed Department of CSE Chittagong University of Engineering &amp; Technology Chattogram, Bangladesh forkan1510699@gmail.com

Annesha Das Department of CSE Chittagong University of Engineering &amp; Technology Chattogram, Bangladesh annesha@cuet.ac.bd

Abstract -The development of an intelligent agricultural decision-supporting system for crop selection and disease forecasting in Bangladesh is the main objective of this work. The economy of the nation depends heavily on agriculture. However, choosing crops with better production rates and efficiently controlling crop disease are obstacles that farmers have to face. These issues are addressed in this research by utilizing machine learning methods and real-world datasets. The recommended approach uses a variety of datasets on the production of crops, soil conditions, agro-meteorological regions, crop disease, and meteorological factors. These datasets offer insightful information on disease trends, soil nutrition demand of crops, and agricultural production history. By incorporating this knowledge, the model first recommends the list of primarily selected crops based on the soil nutrition of a particular user location. Then the predictions of meteorological variables like temperature, rainfall, and humidity are made using SARIMAX models. These weather predictions are then used to forecast the possibilities of diseases for the primary crops list by utilizing the support vector classifier. Finally, the developed model makes use of the decision tree regression model to forecast crop yield and provides a final crop list along with associated possible disease forecast. Utilizing the outcome of the model, farmers may choose the best productive crops as well as prevent crop diseases and reduce output losses by taking preventive actions. Consequently, planning and decision-making processes are supported and farmers can predict possible crop yields. Overall, by offering a detailed decision support system for crop selection and disease prediction, this work can play a vital role in advancing agricultural practices in Bangladesh.

Index Terms -Agriculture, Crop suggesting model, SARIMAX, Crop production, Crop disease, Haversine formula, Machine learning.

## I. INTRODUCTION

Agriculture remains a central lifeline of Bangladesh's economy, contributing to 12% of the nation's GDP and employing 45% of its workforce [1]. Nevertheless, increased population pressure and various challenges are testing the sector's capabilities. Key problems include limited knowledge of appropriate crop selection considering soil nutrition, weather forecasting limitations, and vulnerability to pests and diseases. Modernizing agriculture is essential, and the implementation of machine learning and artificial intelligence knowledge in the age of the fourth industrial revolution can instigate such transformation.

Md. Zubair Department of CSE Chittagong University of Engineering &amp; Technology Chattogram, Bangladesh zubairhossain773@gmail.com

Crops cultivated in Bangladesh are influenced by numerous factors including soil nutrients, weather, and disease risks, all varying across the country's regions. Recognizing these regulators is crucial as not all crops are suitable for all areas. Soil testing is particularly important for understanding soil composition and nutrient levels, paving the way for better crop selection [2]. Machine learning can streamline this process by analyzing soil states and suggesting suitable crops accordingly.

Weather forecasting is another crucial determinant of crop production [3]. By incorporating machine learning and AI into weather prediction, more accurate forecasts can be generated to support crop selection. Furthermore, machine learning's predictive capabilities can help to assess the risk level of crop diseases based on weather parameters such as temperature, rainfall, humidity and, thereby influencing crop choices.

Despite significant research in crop suggestions based on various parameters, no work has yet combined weather forecasts, soil nutrition, and disease prediction for improved crop productivity in Bangladesh. The primary objective is to blend these factors for crop recommendation. The main challenge lies in merging disease prediction with weather parameters to enhance the quality of suggestions. Data related to disease risks and weather conditions need to be meticulously organized and categorized for different crops.

The contributions of the proposed work can be summarized as follows:

- A unified framework is created for weather prediction in Bangladesh, integrating different meteorological variables using the SARIMAX time series model.
- A dataset of the diseases of different crops based on weather parameters (temperature and humidity) is developed.
- A user-friendly crop-suggesting model is introduced that aids farmers in making efficient decisions based on their soil attributes, weather forecasts, and disease risks, thereby enhancing their crop yield and profitability.

Section II delves into a review of existing literature on this topic. Our methodology is depicted thoroughly in Section III.

A practical assessment of our model is exhibited in Section IV, and the paper is concluded in Section V.

## II. RELATED WORK

Several researchers have been attempting to use modern approaches in the agricultural field to improve crop production recently. Hatfield et al. [4] used the Seasonal Autoregressive Integrated Moving Average model, and for estimating the crop's yield, they utilized the random forest regression technique. However, they did not include the impact of diseases on crop production. S. Khaki et al. [5] introduced a deep neural network model for forecasting crop production. They identified the significant influence of weather factors on crop production compared to genotype. They also employed the neural network model to predict the weather. Saranya et al. [2] used SVM, KNN, and logistic regression to predict the best crop according to soil tests and weather forecasts. Elavarasan et al. [6] applied various machine learning models, both supervised and unsupervised, to guess crop production and saw that the expectation-maximization algorithm and the support vector machine gave finer results than the other algorithms based on various error measurement approaches. Khattab et al. [7] focused on disease prediction based on weather parameters. They made use of an IoT-based monitoring system to forecast early plant disease. Ryan et al. [8] utilised Markov random fields, which are responsible for the spatial element among neighbouring sites for herbicide resistance. Afrin et al. [9] focused on crop yield prediction by analyzing soil properties of 28 sub-districts of Bangladesh. Crop yield predictions were made by using DBSCAN, PAM, CLARA, K-means, and other data mining techniques and four different types of linear regression. Parveen et al. [10] gave a review of machine learning methods for agricultural crop disease prediction. It discussed the integration of meteorological factors and historical disease data and stressed the potential of machine learning in enhancing disease management tactics. Limitations in data availability and quality were found, particularly in emerging areas. The intricacy of disease connections and the requirement for precise and timely disease data were also stressed. An early crop disease prediction method using machine learning was described by Vijayakumar et al. [11]. It investigated the use of meteorological variables and physiological information about plants to create forecasting models. To safeguard crops, the study emphasized the value of early disease identification. The complexity of disease interactions and the requirement for real-time data updates were also cited in the article as major obstacles to creating reliable and accurate disease prediction models. Ahmed et al. [12] used a Human-Computer Interaction (HCI) oriented method namely Soft System Methodology (SSM) along with different machine learning models such as Naive Bayes, j48, Sequential Minimal Optimization, and Multiclass classifier for predicting crop yields. Aggarwal et al. [13] proposed a machine learning-based integrated solution for crop recommendation and yield prediction. It developed thorough models by combining soil properties, meteorological variables, and historical yield data. The study highlighted the advantages of including these aspects while making agricultural decisions. The report discussed the difficulties in gathering data, particularly when it comes to precise and dependable soil and meteorological data. It also suggested that models needed to be improved to fit certain agroecological zones.

## III. OUTLINE OF METHODOLOGY

This section describes the suggested approach for our work. Bangladesh is mainly an agricultural country and its economic development vastly depends on the advancement of the agricultural sector. But this field faces a lot of difficulties. The cultivable land is reducing over the years when the demand for production is increasing. climate change and its consequences are also making a large impact on the production of agricultural products. It was challenging to identify the most productive crops. We have to follow a sequential process to get short-listed suggestions for the top-producing crops and the possible disease vulnerability forecast for each crop on the suggested list. Making real-world datasets is challenging because crop productivity is heavily influenced by weather, soil quality, season, and disease possibility. The methodology contains several steps, depicted in Fig. 1. The steps applied in the methodology are discussed in the next sections.

## A. Dataset Preparation

Bangladesh has 64 districts, 492 sub-districts, and 30 agroecological zones [12]. We have used seven different datasets for the proposed work. Details about each of the datasets are presented in the following Table I and discussed in the following sections.

Fig. 1: Overall system architecture

<!-- image -->

TABLE I: DATASET OVERVIEW

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Soil Nutrition, Attributes: District, Sub-district, Longitude, Latitude, Agro-ecological zone, pH, Phosphorus, Potassium, Nitrogen, Data Source: Bangladesh Soil Insti- tute [14].
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Crop Nutrition, Attributes: Crops, Potassium, Phos- phorus, Nitrogen, Data Source: Agriculture Dept. of Bangladesh [15].
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Crop Production, Attributes: Temperature, Rainfall, pH, Crops, Production, Data Source: Agriculture Dept. of Bangladesh.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Crop Disease, Attributes: Region, Latitude, Longi- tude, Temperature, Hu- midity, Crop Diseases, Data Source: Bangladesh Agro- Meteorological Dept. [16].
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Monthly Avg. Temperature, Attributes: Year, Month, Avg. Tem- perature, Data Source: Bangladesh Meteoro- logical Dept. [17].
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Monthly Avg. Rainfall, Attributes: Year, Month, Avg. Rain- fall, Data Source: Bangladesh Meteoro- logical Dept..
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Dataset Name: Monthly Avg. Humidity, Attributes: Year, Month, Avg. Hu- midity, Data Source: Bangladesh Meteoro- logical Dept..
- 1) Meteoro-agro Region &amp; Soil Nutrition Dataset: The types of soil nature and the level of different nutrient elements in the soil of all locations are not similar [18]. That is why, dividing the areas into different agroecological zones based on soil nutrition level is a must to predict the production and disease possibilities for different crops in different regions.

This dataset is a compilation of information related to soil characteristics and agricultural dependencies in different regions of Bangladesh. It includes details such as the division, district, upazila (sub-district), latitude, and longitude of each location.

Additionally, it provides information on the agroecological zone number and name, meteorological station, the pH level of the soil, and the content of phosphorus and potassium in the soil.

- 2) Crop Nutrition Dataset: The rate of production of crops depends on the amount of soil nutrition gained by crops. All crops do not require the same level of nutrition elements. Hence, we have to keep in mind the soil nutrition facts of a region to suggest the best productive crops for that region. This dataset contains information about the nutrient requirements of various crops, specifically regarding phosphorus and potassium levels. The dataset includes 18 crops along with their corresponding phosphorus and potassium levels.
- 3) Crop Production Dataset: Crop production depends on different key factors. Weather parameters and soil quality affect the production of a crop very much. So, we have created a dataset of the production of crops in ton/hector for different combinations of weather parameters and soil quality. This dataset provides information on rainfall, temperature, pH level, crop type, and corresponding production.
- 4) Crop Disease Dataset: Production of crops is greatly reduced by the impact of different crop diseases [19]. If we want to build a crop-suggesting system for best production, then we must consider the possible diseases for the cultivated crop. On the other hand, diseases of crops depend on different weather parameters [20]. Temperature and humidity are two of the major weather parameters affecting crop disease possibilities
4. [21]. The dataset provides specific information about different crops in different regions of Bangladesh, including the latitude and longitude coordinates, temperature, humidity, and the corresponding diseases observed under those conditions. The acquired data were not in a usable format to be used by machine learning algorithms. So, we have to create the crop disease dataset using the information of the Bangladesh Agrometeorological Department. This dataset helps to detect the possible diseases for any crop in a given location.
- 5) Monthly Average Temperature Dataset: This dataset is composed of information about the average temperature (in °C) by month at different meteorological stations in Bangladesh. Almost 50+ years of information is placed in the dataset which has been used for future temperature prediction. The predicted temperature has been used to predict the production of crops and possible crop diseases.
- 6) Monthly Average Rainfall Dataset: This dataset is a collection of information about the average rainfall (in mm) per month at different meteorological stations in Bangladesh. There are almost 50+ years of information in this dataset for machine learning approach-based future rainfall prediction. The predicted rainfall along with the predicted temperature have been used for predicting the production of crops.
- 7) Monthly Average Humidity Dataset: Information about average the humidity (in %) by month of different meteorological stations in Bangladesh is stated in this dataset. Like the other two weather parameter datasets, almost 50+ years of information is available in the dataset for future humidity prediction. The predicted humidity has been used to predict possible crop diseases.

## B. Location Based Soil Nutrition Extraction

At first, the closest sub-district (agro-meteorological zone) to the user location is determined by applying the Haversine formula [22]. If the latitude and longitude of two sites on Earth are known, the distance between them can be determined using the Haversine formula. The Haversine formula is derived from the Haversine law by using the sides and angles of spherical triangles. The Haversine formula is as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where:

- ∆ ϕ is the difference in latitude between the user location and the agricultural zone,
- ∆ λ is the difference in longitude between the user location and the agricultural zone,
- ϕ 1 and ϕ 2 are the latitudes of the user location and the agricultural zone respectively,
- R is the radius of the Earth,
- a is the square of half the chord length between the user location and the agricultural zone (also known as the haversine),
- c is the angular distance in radians between the user location and the agricultural zone,
- d is the distance between the user location and the agricultural zone in the same units as the Earth's radius.

Here we estimated the closest possible agricultural zone and meteorological station for the given user location based on latitude and longitude. It is necessary for the precision of soil nutrition identification and weather information accuracy. Then, using the Meteoro-agro Region &amp; Soil Nutrition Dataset, which contains information on soil nutrition according to the meteorological zone and agricultural zone, the information about the soil nutrition level of the nearest sub-district is found.

## C. Primary Crops Finding

In this phase, the crop nutrition dataset is utilized to determine whether the found soil nutrition level satisfies the appropriate crops' needs or not for a given user area. A list of the major crops is thus discovered.

## D. Weather Parameter Forecast

The suggested model automatically pulls the local temperature, rainfall, and humidity data from respective datasets when the user location is chosen. Rainfall, humidity, and temperature fluctuate from month to month. Furthermore, the time series data is one-dimensional. We have employed the SARIMAX (Seasonal Autoregressive Integrated Moving Average with Exogenous Variables) model, which can more accurately capture the seasonal pattern, as temperature, rainfall, and humidity are seasonal data[23]. SARIMAX(p, d, q)(P, D, Q, s) can be used to specify the SARIMAX model where p, d, and q represent the successive order of differencing and moving average terms, respectively, in autoregressive terms. Additionally, P, D, Q, and s stand for the seasonal duration, seasonal moving average terms, seasonal order of differencing, and seasonal autoregressive terms respectively.

The best SARIMAX model parameters were found by using the Akaike Information Criterion (AIC) measurement. AIC is a statistician's tool for assessing the relative merits of several statistical models, especially in the context of model selection. It offers a trade-off between a model's goodness of fit and complexity. In this work, the best SARIMAX model parameters for temperature, rainfall, and humidity are as follows:

- Temperature : SARIMAX(1, 0, 0) (2, 1, 0, 12)

- Rainfall : SARIMAX(1, 0, 0) (0, 1, 1, 12)

- Humidity : SARIMAX(1, 0, 1) (1, 1, 0, 12)

## E. Crop Production Prediction

In previous subsections, we have retrieved information on the primary cultivable crops, temperature, and rainfall. Our primary prediction model was developed at this stage. Our suggested model uses the supervised regression machine learning technique because this is the prediction of a continuous variable. Applying the Decision Tree Regression (DTR) technique, the prediction model is trained to forecast the main cultivable crops' production.

## F. Crop Disease Prediction

Crops are vulnerable to diseases which vary based on weather conditions. The model is given the agricultural location along with its predicted temperature, humidity, and selected crop list based on crop and soil nutrition. The model then predicts the possible diseases and total disease count for each of the primary selected crops. We have used the Support Vector Classifier (SVC) to predict the possible disease for a list of crops.

## IV. RESULT AND DISCUSSION

This section is focused on the discussion of the outcome of each of the steps of our work. Results acquired from each step of methodology and comparative analysis of the prediction models are shown in the following subsections.

## A. Experimental Results

The suggested model was developed using Bangladesh's geography and put into practice within the setting of Bangladeshi agriculture. With the datasets we have gathered, we have assessed the model. The subsections that follow talk about the experimental results we achieved.

- 1) Location Based Soil Nutrition Extraction: Our methodology begins by finding the longitude and latitude of the user's current position. The closest sub-district is then determined by the model using the Haversine formula. Consider utilizing the Rangpur Sadar Upazila as the test location (Longitude: 25.740580 °N, Latitude: 89.261139 °E). The model selects the closest agricultural zone and retrieves the pertinent information about soil nutrition as shown in Table II.
- 2) Primary Crops List: The crop nutrition dataset is used to choose the main cultivable crops based on the information about soil nutrition from Table II. A crop will be chosen as the major cultivable crop if its nutritional value satisfies the nutritional standard for that area. The selected crops are displayed in Table III.
- 3) Weather Parameter Forecast: Crop productivity and disease susceptibility are regulated by three key factors including temperature, rainfall, and humidity. SARIMAX model is used for forecasting Temperature (in °C), rainfall (in millimetres), and humidity (in %) for the given user location which is Rangpur Sadar Upazila. These weather parameters have been derived from three weather datasets.

## TABLE II: EXTRACTED SOIL NUTRITION DATA

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: Agro-Meteoro Zone, Value: Rangpur.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: Latitude, Value: 25.740580 ˆ A°N.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: Longitude, Value: 89.261139 ˆ A°E.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: pH, Value: 5.6-6.5.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: Phosphorus, Value: VH.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Parameter: Potassium, Value: M.
TABLE III: PRIMARILY SELECTED CROPS

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 1 2 3 4 5 6 7, Crop Name: Garlic Lentil Papaya Rice Soyabean Sugarcane Tomato.
TABLE IV: EXTRACTED WEATHER DATA

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Jan, Temp.(°C): 15.8, Rain.(mm): 0, Hum.(%): 82.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Feb, Temp.(°C): 20.5, Rain.(mm): 10, Hum.(%): 75.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Mar, Temp.(°C): 23.7, Rain.(mm): 24, Hum.(%): 68.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Apr, Temp.(°C): 26.6, Rain.(mm): 94, Hum.(%): 77.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: May, Temp.(°C): 27.4, Rain.(mm): 232, Hum.(%): 82.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Jun, Temp.(°C): 29, Rain.(mm): 289, Hum.(%): 80.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Jul, Temp.(°C): 28.4, Rain.(mm): 542, Hum.(%): 83.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Aug, Temp.(°C): 28.4, Rain.(mm): 572, Hum.(%): 85.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Sep, Temp.(°C): 28, Rain.(mm): 299, Hum.(%): 84.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Oct, Temp.(°C): 27.1, Rain.(mm): 116, Hum.(%): 84.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Nov, Temp.(°C): 22.6, Rain.(mm): 3, Hum.(%): 78.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Month: Dec, Temp.(°C): 18.4, Rain.(mm): 0, Hum.(%): 80.
The temperature, rainfall, and humidity statistics of the user location for 2023 are displayed in Table IV.

- 4) Crop Disease Prediction: By using the temperature and humidity data for user location from Table IV and primary selected crops list from Table III, the possible diseases for each crop are suggested in Table V.
- 5) Crop Production Prediction: The soil nutrition, primary cultivable crops, expected temperature, and rainfall are all obtained from the aforementioned procedures. In this stage, the system trains the proposed regression model to forecast the production amount of the primary selected crops by using the crop production dataset.
- 6) Final Suggested Crops List: The model then arranges the predicted production for different crops in decreasing order. The model generates the final list of crops displayed in Table VI for the stated user location (Rangpur Sadar Upazila).

TABLE V: PREDICTED CROP DISEASES

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 1, Crop: Garlic, Count: 0.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 2, Crop: Lentil, Count: 1, Disease: Foot rot.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 3, Crop: Papaya, Count: 0.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 4, Crop: Rice, Count: 0.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 5, Crop: Soyabean, Count: 1, Disease: Anthracnose.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 6, Crop: Sugarcane, Count: 1, Disease: Smut.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Initial Order: 7, Crop: Tomato, Count: 0.
TABLE VI: FINAL CROPS LIST

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 1, Crop: Papaya, Production (ton/hectare): 134.24, Disease: Not found.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 2, Crop: Sugarcane, Production (ton/hectare): 106.79, Disease: Smut.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 3, Crop: Tomato, Production (ton/hectare): 35.17, Disease: Not found.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 4, Crop: Garlic, Production (ton/hectare): 12.79, Disease: Not found.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 5, Crop: Soyabean, Production (ton/hectare): 11.44, Disease: Anthracnose.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 6, Crop: Rice, Production (ton/hectare): 7.99, Disease: Not found.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Final Order: 7, Crop: Lentil, Production (ton/hectare): 0.85, Disease: Foot rot.
## B. Comparative Analysis of Disease Prediction Models

Different classification models have been applied to find the best-suited model for predicting the possible diseases of the suggested crops. A few well-known factors have been considered for this purpose which are stated below:

- Accuracy : A classification model's overall correctness can be estimated by its accuracy. It determines the proportion of accurately predicted occurrences to all of the dataset's instances.
- Precision : Precision is the measurement of the accuracy of positive predictions given by the model. It is calculated as the proportion of true positives to the total number of positive predictions (true positives + false positives) from the whole dataset.
- Recall : Recall represents the ability of a model to accurately recognize all relevant instances in the dataset. It can be measured as the ratio of true positives to the total number of real positives (true positives + false negatives).
- F1 Score : The harmonic mean of precision and recall can be stated as the F1 score. The trade-off between precision and recall is balanced by this F1 score and it suggests a single summarizing score about a model's performance.

Using the crop disease dataset, the Support Vector Classifier (SVC), Random Forest Classifier (RFC), Gradient Boosting Classifier (GBC), and Logistic Regression (LoR) model are trained and tested on the evaluation metrics. The findings of the comparative error analysis are shown in Table VII.

Most often, higher values of accuracy, precision, recall, and F1 score indicate the best classification model. For this work, SVC provides the best disease predictions rather than other models.

## C. Comparative Analysis of Production Prediction Models

To forecast the production of the primarily selected crops, different regression methods have been compared to choose the most compatible model. The most common method of assessment is to estimate how well the projected value matches the actual value. The following metrics for evaluation are investigated for choosing the best model:

- Mean Squared Error (MSE) : The mean square difference between predicted and actual values for regression algorithms is known as MSE.
- Root Mean Squared Error(RMSE) : This error type provides the root mean square difference between the anticipated and real values.
- R-squared : R-squared value shows how appropriate the data is to the fitted regression line.

TABLE VII: EVALUATION METRICS FOR THE DISEASE PREDICTION MODEL

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: SVC, Accuracy: 0.94, Precision: 0.91, Recall: 0.94, F1 Score: 0.92.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: RFC, Accuracy: 0.91, Precision: 0.89, Recall: 0.91, F1 Score: 0.9.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: GBC, Accuracy: 0.9, Precision: 0.89, Recall: 0.9, F1 Score: 0.9.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: LoR, Accuracy: 0.56, Precision: 0.59, Recall: 0.56, F1 Score: 0.57.
TABLE VIII: EVALUATION METRICS FOR THE PRODUCTION PREDICTION MODEL

Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: DTR, MSE: 1.06, RMSE: 1.03, R-Squared: 0.997.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: RFR, MSE: 1.19, RMSE: 1.09, R-Squared: 0.996.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: LR, MSE: 42.89, RMSE: 6.54, R-Squared: 0.891.
Según A Machine Learning Approach for Crop Yield and Disease Prediction Integrating Soil Nutrition and Weather Factors (2024), Model: GBR, MSE: 4.54, RMSE: 2.13, R-Squared: 0.988.
The optimal regression procedure for the final forecast is what we are aiming for. Using the crop production dataset, the Linear Regression (LR), Decision Tree Regression (DTR), Gradient Boosting Regression (GBR), and Random Forest Regression (RFR) models are trained and tested. The findings of the comparative error analysis are shown in Table VIII.

The lower MSE and RMSE values suggest that the forecasted result and the real outcome are quite close to each other. The R-squared value, on the other hand, ranges from 0 to 1. The greater the number is, the more accurately the model is fitted. DTR is the ideal model for our system, according to the findings.

## V. CONCLUSION

In this work, we have created a model to recommend the most productive crops along with probable crop diseases based on the user's location. Bangladesh serves as the backdrop for the creation of the whole work. The fast-expanding population increases food consumption, yet the amount of arable land is steadily shrinking in this country. Therefore, increasing agricultural output is now unavoidable. In this work, a model that suggests economically and more productive crops throughout the year in any place has been developed using machine learning techniques.

We utilized SARIMAX as the rainfall, humidity, and temperature forecasting model for the weather forecast. Then, probable disease is predicted based on temperature and humidity for the primary selected crops. At last, crop production is determined using a regression model based on soil nutrition data and forecasted temperature and rainfall data. Compared to other models, the SVC model shows better outcomes for crop disease prediction and the DTR model performs better in predicting crop yield. Hopefully, the application of our strategy to the agriculture sector would increase crop yield and result in economic growth. We intend to provide Bangladeshi farmers access to this technology through a mobile platform in the future. Converting this work into the form of software will be more beneficial and easier for the farmers to know which crops they should cultivate to maximize their economic profit and also get prepared for possible crop diseases. Besides, the work can be extended by using more crop and disease data along with more weather parameter dependency.

## REFERENCES

- [1] M. T. Rahman, 'Role of agriculture in bangladesh economy: uncovering the problems and challenges,' International Journal of Business and Management Invention , vol. 6, no. 7, 2017.
- [2] N. Saranya and A. Mythili, 'Classification of soil and crop suggestion using machine learning techniques,' International Journal of Engineering Research &amp; Technology (IJERT) , vol. 9, no. 02, pp. 671-673, 2020.
- [3] J. L. Hatfield, K. J. Boote, B. A. Kimball, L. Ziska, R. C. Izaurralde, D. Ort, A. M. Thomson, and D. Wolfe, 'Climate impacts on agriculture: implications for crop production,' Agronomy journal , vol. 103, no. 2, pp. 351-370, 2011.
- [4] M. Zubair, S. Ahmed, A. Dey, A. Das, and M. M. Hasan, 'An intelligent model to suggest top productive seasonal crops based on user location in the context of bangladesh,' in Smart Systems: Innovations in Computing: Proceedings of SSIC 2021 . Springer, 2021, pp. 289-300.
- [5] S. Khaki and L. Wang, 'Crop yield prediction using deep neural networks,' Frontiers in plant science , vol. 10, p. 621, 2019.
- [6] D. Elavarasan, D. R. Vincent, V. Sharma, A. Y. Zomaya, and K. Srinivasan, 'Forecasting yield by integrating agrarian factors and machine learning models: A survey,' Computers and Electronics in Agriculture , vol. 155, pp. 257-282, 2018.
- [7] A. Khattab, S. E. Habib, H. Ismail, S. Zayan, Y. Fahmy, and M. M. Khairy, 'An iot-based cognitive monitoring system for early plant disease forecast,' Computers and Electronics in Agriculture , vol. 166, p. 105028, 2019.
- [8] R. H. Ip, L.-M. Ang, K. P. Seng, J. Broster, and J. Pratley, 'Big data and machine learning for crop protection,' Computers and Electronics in Agriculture , vol. 151, pp. 376-383, 2018.
- [9] S. Afrin, A. T. Khan, M. Mahia, R. Ahsan, M. R. Mishal, W. Ahmed, and R. M. Rahman, 'Analysis of soil properties and climatic data to predict crop yields and cluster different agricultural regions of bangladesh,' in 2018 IEEE/ACIS 17th International Conference on Computer and Information Science (ICIS) . IEEE, 2018, pp. 80-85.
- [10] S. Parveen, M. M. Hassan, and M. A. H. Bhuyan, 'Disease prediction in agricultural crops using machine learning: A review,' Agricultural Research , vol. 9, no. 2, pp. 211-228, 2020.
- [11] N. Vijayakumar, R. Venkatesan, R. Rajkumar, and P. Senthil Kumar, 'A machine learning approach for early prediction of crop diseases,' International Journal of Computer Applications , vol. 168, no. 4, pp. 1-6, 2017.
- [12] M. T. Ahmed, M. N. Imtiaz, and N. S. Mitu, 'Impact of weather on crops in few northern parts of bangladesh: Hci and machine learning based approach,' Aust. J. Eng. Innov. Technol , vol. 2, no. 1, pp. 7-15, 2020.
- [13] H. Aggarwal, K. Singh, and S. Vyas, 'Integrated approach for crop recommendation and yield prediction using machine learning,' Egyptian Informatics Journal , vol. 20, no. 2, pp. 103-112, 2019.
- [14] 'Bangladesh soil institute,' 2023. [Online]. Available: http://www.srdi. gov.bd/
- [15] 'Bangladesh agricultural research institute,' 2023. [Online]. Available: http://www.bari.gov.bd
- [16] 'Bangladesh agro-meteorogical information portal,' 2023. [Online]. Available: https://www.bamis.gov.bd/en/calendar
- [17] 'Bangladesh meteorological department,' 2023. [Online]. Available: https://bmd.gov.bd/
- [18] M. Islam, 'Soil fertility history, present status and future scenario in bangladesh,' Bangladesh Journal of Agriculture and Environment , vol. 4, pp. 129-151, 2008.
- [19] C. L. Carroll, C. A. Carter, R. E. Goodhue, and C.-Y. C. L. Lawell, 'Crop disease and agricultural productivity,' National Bureau of Economic Research, Tech. Rep., 2017.
- [20] H. R. Regmi, 'Effect of unusual weather on cereal crop production and household food security,' Journal of Agriculture and Environment , vol. 8, pp. 20-29, 2007.
- [21] C. Rosenzweig, A. Iglesius, X.-B. Yang, P. R. Epstein, and E. Chivian, 'Climate change and extreme weather events-implications for food production, plant diseases, and pests,' 2001.
- [22] N. R. Chopde and M. Nichat, 'Landmark based shortest path detection by using a* and haversine formula,' International Journal of Innovative Research in Computer and Communication Engineering , vol. 1, no. 2, pp. 298-302, 2013.
- [23] S. Wang, J. Feng, and G. Liu, 'Application of seasonal time series model in the precipitation forecast,' Mathematical and Computer modelling , vol. 58, no. 3-4, pp. 677-683, 2013.