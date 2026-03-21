---
id: arxiv-2312.03338
title: Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US
year: 2023
country: Internacional
source: ArXiv (q-bio.PE, q-bio.QM)
doc_type: Artículo científico
language: en
tags:
  - especies invasoras
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Modeling human activity-related spread of the spotted lanternfly ( Lycorma delicatula ) in the US

Daniel Str¨ ombom 1 ∗ , Autumn Sands 1 , Jason M. Graham 2 , Amanda Crocker 1 , Cameron Cloud 1 , Grace Tulevech 1 , Kelly Ward 1 .

1

Department of Biology, Lafayette College, Easton, PA, USA. 2 Department of Mathematics, University of Scranton, Scranton, PA, USA.

## Abstract

The spotted lanternfly ( Lycorma delicatula ) has recently spread from its native range to several other countries and forecasts predict that it may become a global invasive pest. In particular, since its confirmed presence in the United States in 2014 it has established itself as a major invasive pest in the Mid-Atlantic region where it is damaging both naturally occurring and commercially important farmed plants. Quarantine zones have been introduced to contain the infestation, but the spread to new areas continues. At present the pathways and drivers of spread are not well-understood. In particular, several human activity related factors have been proposed to contribute to the spread; however, which features of the current spread can be attributed to these factors remains unclear. Here we collect county level data on infestation status and four human activity related factors and use statistical methods to determine whether there is evidence for an association between the factors and infestation. Then we construct a mechanistic network model based on the factors found to be associated with infestation and use it to simulate local spread. We find that the model reproduces key features of the spread 2014 to 2021. In particular, the growth of the main infestation region and the opening of spread corridors in the westward and southwestern directions is consistent with data and the model accurately forecasts the correct infestation status at the county level in 2021 with 81% accuracy. We then use the model to forecast the spread up to 2025 in a larger region. Given that this model is based on a few human activity related factors that can be targeted, it may prove useful in informing management and further modeling efforts related to the current spotted lanternfly infestation in the US and potentially for current and future invasions elsewhere globally.

## Introduction

The spotted lanternfly ( Lycorma delicatula ) is an insect native to China, India and Vietnam that is currently considered an invasive pest in South Korea, Japan and the United States [1,2]. In regions where it is invasive, it is a threat to many naturally occurring plants and a number of economically important interests including the grape, orchard and lumber industries [3,4].

The spotted lanternfly was first confirmed in the US in 2014 and has since rapidly spread and expanded its distribution [5]. Quarantine zones and permitting by respective state Departments of Agriculture have been implemented to restrict the movement of certain products and any living life stage of the spotted lanternfly in an attempt to limit the spread to new regions [6]. In areas where the lanternfly is already present a number of control measures, including insecticides [7], parasite-based biological controls [8, 9], traps [10], egg scraping [11], and removal of the primary host plant [12] have been applied. However, these efforts appear to be insufficient given that the lanternfly is still spreading rapidly to new regions [4,13]. In addition,

∗ Corresponding author: stroembp@lafayette.edu

earlier published niche models based on climate and other factors forecast that the spotted lanternfly may eventually establish itself in a much larger portion of the US than it currently occupies and elsewhere globally [2,14]. However, these models only forecast the eventual maximal distribution, they do not provide information about how the lanternfly is likely to spread from its current limited distribution to this maximal distribution [15] nor what the key drivers of the local spread are. To address the issue of forecasting how the spotted lanternfly, and other pests and pathogens, might spread over time a species agnostic dynamic spatio-temporal forecasting system was recently introduced [16]. Unlike previous models for the lanternfly infestation in the US this system can also provide estimates for when the lanternfly is expected to arrive in a particular region, rather than just that it eventually might. For example, it has been used to forecast that there is a high chance that California will have lanternfly infestations in 2033 [17]. While this system represents a significant advance in dynamic forecasting its high complexity and data-driven nature makes it less suitable for obtaining a causal understanding of the current local spread in terms of key drivers, and how to limit the spread by targeting these. To address such questions a mechanistic model based on a limited number of factors may be more appropriate [18].

The spotted lanternfly is known to spread through two distinct processes; short distance dispersal and long distance dispersal [9]. Short distance dispersal includes natural flight capabilities of up to 40m to infest new host plants [19] and/or local human assisted transport [20]. Long distance dispersal refers to establishment of satellite populations away from the main area of infestation [9], and several potential pathways and drivers of long distance dispersal in the spotted lanternfly have been proposed in the literature. In particular, a number of human activity related factors including the transportation of packing materials and vehicles [1,3], transportation of materials related to gardening and plants [21], and human activity/population density [9,13,22,23]. Unlike climate, geography, host plant distribution, temperature, and other non-human activity related factors that are known, or believed, to affect the spread and settlement of the lanternfly, these human activity related factors may be more readily targetable and affectable by management efforts. A minimal model based on such factors capable of replicating key features of the actual spread could be used as a framework for assessing proposed management efforts before they are deployed, and potentially even to help determine what they should be.

## Results

The data collected for a 166 county region that contained all infested counties [5] on September 28th 2021 (Fig 1A), including number of garden centers (Fig 1B), primary interstate highways (Fig 1C) and population (Fig 1D) is presented in Figure 1.

By fitting a generalized additive logistic regression model [24-26] we find that the data provides evidence for the increase in likelihood of infestation in a county with the presence of interstate highways and larger populations (Table 1). Additionally, the analysis also suggests that the data provides evidence for the increase in likelihood of infestation in a county with an increase in the number of garden centers only when there is also the presence of a primary interstate highway in that county.

See the Methods section for information about the data collection and the statistical methods used.

Table 1: Summary table for estimates for linear terms in generalized additive model. Results are on the log-odds scale.

Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Coefficient: IS Presence - Yes, Estimate: 1.21, SE: 0.63, p-value: 0.054.
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Coefficient: Garden Centers, Estimate: -1.29, SE: 0.63, p-value: 0.041.
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Coefficient: Population (log), Estimate: 1.68, SE: 0.84, p-value: 0.046.
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Coefficient: IS Presence - Yes : Garden Centers, Estimate: 1.96, SE: 0.69, p-value: 0.005.
Figure 1: Visualization of the assessment region and the data collected. (A) County map showing the counties designated as infested by the New York State Integrated Pest Management [5] on September 28th 2021 and the 166 county region defined as the convex hull of those infested counties. (B) The number of garden centers present in each county. (C) The number of primary interstate highways transecting each county. (D) The population of each county on a log scale.

<!-- image -->

## Model

Based on insights presented in the literature and the results of our statistical analyses above we construct a network model of the spread consisting of two components. General short distance spread on the network of adjacent counties and long distance spread on the primary interstate highway network with garden center and population density dependent infestation probabilities. The components and parameters of the model are described in Table 2.

The spread on each of the two interconnected networks follow the independence model introduced in Leung et al. 2004 (See equation (1) in [27]) modified to include the garden center and population dependent spread on the primary interstate highway network. More specifically, the spread on the adjacency network is given by

<!-- formula-not-decoded -->

and the garden center dependent spread on the primary interstate highway network by

<!-- formula-not-decoded -->

and the population dependent spread on the primary interstate highway network by

<!-- formula-not-decoded -->

Table 2: Components and parameters of the model.

Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: t, Description: Timestep (1 year)..
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: i, j, Description: County indices..
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: ¯ q t, Description: Infestation vector. q t,i = 1 if county i is infested at time t , and q t,i = 0 if it is not..
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: A, Description: Adjacency matrix encoding the network of adjacent counties. a ij = 1 if county i and county j share a border, and a ij = 0 if they do not..
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: H, Description: Adjacency matrix encoding the network of counties connected by a primary interstate highway. h ij = 1 if county i and county j share a highway, and h ij = 0 if they do not..
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: p, Description: Probability of spread to an uninfested county from each of its adjacent infested counties. Estimated using the 2014-20 data. See the Methods section for details. Establishment probability vector for primary interstate highway spread by the.
Según Modeling human activity-related spread of the spotted lanternfly (Lycorma delicatula) in the US (2023), Symbol: ¯ s x, Description: factor x. Ex. ¯ s x =(number x in county i )/(total number x). We consider two such factors here: garden centers (¯ s g ) and population (¯ s p )..
We implemented the combined modes of spread over the interconnected adjacency and primary interstate highway networks in Matlab and analyzed the model via simulations. See the Methods section for details on model construction, parameterization, implementation, simulation and assessment.

The results of simulating the model in the 166 county region starting with Berks county, PA, as the only infested county in 2014 and recording the proportion of simulations that yielded each county infested in each year 2015-2021 is presented in the bottom row of Figure 2. We note that the model constructed based on the included factors reproduces key characteristics of the observed spread both qualitatively and quantitatively. Comparing the Top and Bottom rows in Figure 2 shows that not only is the model forecasted growth of the infested region relatively consistent with the observed over the years, but the model also forecasts the opening up of spread corridors from the main infestation region around Berks County, PA, west toward the Pittsburgh area and south-southwest through VA. In particular, the model starts suggesting already in 2017-18 that Alleghany County, PA, had an increasing risk of infestation before it was finally designated as infested in 2020. Similar observations are made in each main direction of infestation spread. Quantitatively, using the rule that if more than half of the simulations resulted in a county being infested to designate a county as infested according to the model, the model predicts the correct 2021 county infestation status with 81% accuracy. More specifically, it forecasts the infestation correctly in 135 counties and incorrectly in 31 counties. Of the 31 mismatches there are 16 false positives, where the model suggests the county should be infested but the data disagrees, and 15 false negatives, where the model suggests the county should not be infested but the data says it is.

Once the model had been assessed in the 166 county region the same parameterized model was simulated in a larger 581 county region. These simulations in the larger region forecasts that the spread along the western corridor through OH and IN, the southwestern corridor on the border of WV and VA, and the southern corridor through VA into NC, will intensify up to the year 2025 (Figure 3).

See the Methods section for more detailed descriptions of the model, model assessment, and the simulation protocols.

## Discussion

The computational model created based on the human activity related factors; primary interstate highways, garden centers and population reproduce both qualitative and quantitative features of the spread through 2014-21. Using the computational model over a larger region of the US to forecast the spread of infestation beyond 2021 suggests that spread will accelerate over this period.

Figure 2: Comparison of observed and model forecasted infestation in the 166 county model 2014-21. The Top row displays the actual observed infestation data from 2014-21. The Bottom row displays the corresponding model forecasts for 2015-21. The coloring indicates the proportion of simulations in which a county became infested in a specific year according to the model. More specifically, a county is solid green if all 1000 simulations rendered it infested in a particular year and white if none of the 1000 simulations resulted in it being infested.

<!-- image -->

Figure 3: Model forecast for 2022-25 in the 581 county region We note that the model suggests that the corridors of spread west, southwest, and south will all intensify over the years. In particular, the model suggests that the area around Cleveland, OH, has had an increased and increasing risk of infestation at least since 2021, and it was recently labeled as infested by the New York State Integrated Pest Management Program. The model also forecasts that the infestation in NC will increase substantially over the next few years.

<!-- image -->

Despite being based on only three specific statistically supported human activity related factors, our model not only reproduces qualitative features of the actual spread, but also forecasts the correct infestation status for 81% of the counties included in the assessment region in 2021. This, together with the observed infestation pattern itself (Figure 2 Top row) supports the assertion that the primary interstate highway system may be a critical pathway for the long distance dispersal of the spotted lanternfly in the US and that human activity in general, and business dealing in plants and plant related materials in particular, are associated with the dispersal along this pathway. While this is consistent with findings and propositions by others as described previously, we note that our finding that primary interstate highways are associated with infestation, rather than road density in general [13] or even all interstate highways, may be a particularly useful insight. There are relatively few primary interstate highways which may make targeting for management and modeling based on those easier and less complex than if a larger classes of roads and transportation pathways are considered. In addition, our statistical finding that garden centers only appear to be associated with increased risk of infestation when primary interstate state highways are present may be useful for prioritizing monitoring and/or management efforts involving garden centers.

Our model does not take into account climate, geography, host plant distribution, temperature, and other factors that are known, or believed, to affect the spread and settlement of the lanternfly. This may explain why the model forecasts the incorrect infestation status in 19% of included counties. If a factor we do not include is severely disadvantageous to lanternfly infestation that factor could explain some of the 16 false positives, and if the excluded factor is severely advantageous to lanternfly infestation it could explain some of the 15 false negatives. However, other explanations for, in particular, the false positives do exist. Notably that sampling effort by authorities and reporting by the public is not uniform throughout the region under consideration [13] so lanternfly infestations may be present in a county but not reported. While it may eventually be useful to add more factors and/or couple our model with niche models [2,14] and/or dynamic forecasting system [16,17] at present it may be most useful in its current minimal form. Primarily because it is already reasonably effective and adding further elements would increase its complexity and reduce its ability to elucidate the causal effects of the specific human activity related factors on the spread of infestation. However, once the infestation has progressed further, both the niche models and the dynamic forecasting system suggest that the conditions for successful establishment of infestation drops significantly (Figure 5 in [17]). If those forecasts are correct our model will produce false positives in these new regions because it does not take into account climate and other factors that they do. If/when the infestation reaches areas with low risk of infestation it will not only serve as a test of our model but also both the niche models [2,14] and forecasting system [16,17]. If the spread significantly slows down or stops our model needs revision, but if it proceeds at the same rate in designated low risk areas or move into areas forecasted as unlikely to be suitable the niche models and forecasting system, and potentially our model too, need revision.

Our forecasts in the larger region suggest that the lanternfly infestation will continue its long range dispersal along the primary interstate highway system in all directions and short distance dispersal will drive the spread outward from the new satellite infestations along these routes (Figure 3). This information may be useful on the ground as a complement to the forecasting system in [17] to forecast where lanternfly infestation is likely to occur next when planning for the application of control measures. In part, because preventing infestation or managing an infestation early is preferable to dealing with a full blown infestation later on [28], but also because of the findings in [29]. Based on available data on the life-stage survival and fecundity [29] estimated that the average annual growth rate of the US spotted lanternfly population is about 5.47. Given this rapid growth even a control measure that kills 100% of treated lanternfly require at least 35% of all lanternfly present in all stages to be treated to induce even the slightest decline in the annual population and this percentage increases rapidly for less effective controls. Given that resources are limited this suggests that using them in the right locations may be critically important. For example, our model forecasts that over the next few years the infestation will intensify in North Carolina (Figure 3). This state has become one of the largest wine producing states with over 525 individually owned vineyards in 2017 [30] and in previously infested regions the grape industry has been particularly adversely affected with one vineyard in Pennsylvania reporting a 90% loss in yield [6]. Our work, including both model and statistical analysis, in conjunction with the infestation data suggests that spread occurs along the primary interstate highways, so efforts to limit the spread risk southward along primary interstates 77, 85, and 95 may lower the risk for North Carolina's wine industry. We are aware that the Pennsylvania Department of Agriculture are focusing on transportation corridors such as major highways and tourist destinations [31], but we are unable to find information about which specific highways or areas they are targeting and/or what decisions to target these are based on. Our model, or a mechanistic model similar to it, could help inform such decisions. Whether it is to assess two or more competing management alternatives with given estimated county-level impacts before implementation, or to minimize spread to a particular region, or even to minimize the overall spread. Comparing alternatives will be particularly straightforward since that would amount to changing county level parameters. For example, say that some action is estimated to decrease the long-distance dispersal through a county by 30%, then the weights on the network links from that county would be reduced by 30% and new simulations run to observe the outcome. Minimizing spread to a particular region, or minimizing the overall spread, requires more work, but there is a wealth of analysis tools available for entities that spread on networks (e.g. infections [32,33]) that could be used to rank the nodes (counties) and the links (transmission pathways) based on their contribution to the overall spread. We believe that using mechanistic modeling as a

complement to other approaches to estimate where the limited resources available to combat the infestation should be deployed for maximum impact with respect to whichever objective is set by professionals on the ground will be necessary to significantly reduce the spread of lanternfly in the US. The low-complexity model based on statistically established factors we present here represents one step in this direction.

## Methods

## Data collection

First, we defined a region for our statistical analyses and model assessment such that it is plausible that the lanternfly would have spread to and infested the counties in this region if the conditions had been favorable by following the convex hull approach used in [13]. This method led to a 166 county region as the convex hull of the counties designated as infested by the New York State Integrated Pest Management [5] on September 28th 2021 (Fig 1A). We also collected data on the number of garden centers (Fig 1B), primary interstate highways (Fig 1C) and population (Fig 1D) for each county in the region. More specifically, for each county in the 166 county region we collected

1. The names and FIPS codes of its adjacent counties from the United States Census Bureau [34].
2. The year in which it was designated as infested by consolidating information from the New York State Integrated Pest Management [5], the Pennsylvania Department of Agriculture [35-38], State of New Jersey Department of Agriculture [39], and the Virginia Polytechnic Institute and State University [40].
3. The number of businesses designated as garden centers (retail or wholesale). This data was collected in October 2021 by manually searching 'Garden centers in [county name] county' in Google Maps [41] and verifying that each search result was indeed a garden center that lies within the county boundary. (Figure 1B).
4. The 2019 population estimate from the United States Census Bureau [42]. (Figure 1D).
5. The primary (two-digit) interstate highways that transect it and their identification numbers from Google Maps [41] (Figure 1E).

In the larger 581 county region we collected the same data using the same sources. The exception being the infestation year because no county outside the 166 county region was infested at that time.

## Statistical analysis to determine relevance of factors

For a statistical test of our hypotheses we used R version 4.3.1 and package mgcv version 1.9 to fit a generalized additive logistic regression model [24-26]. Specifically, we model the log-odds of county infestation in 2021 with tensor product smoothing for longitude and latitude to control for spatial-autocorrelation and include parametric terms for presence/absence of two-digit interstate highway, number of garden centers, county population, and an interaction term for presence/absence of primary (two-digit) interstate highway and number of garden centers. To deal with issues of convergence and variables of different scale, we log transformed the population and normalized the number of garden centers. We used the packages DHARMa version 0.4.6 and gratia gratia version 0.8.1.34 for diagnostics to assess model assumptions [43,44]. Figure 4 shows the estimates on the odds-ratio scale for the parametric terms in our generalized additive logistic regression, as a complement to Table 1 which displays the values for the same estimated coefficients on the log-odds scale.

## Model construction, parameterization, implementation, simulation and assessment

The model was implemented in Matlab and here we describe the main model related elements in more detail.

Figure 4: Estimated coefficients with 95% CIs for the parametric terms in the generalized additive model . Results are on the scale of odds-ratio. The likelihood of infestation for a county in 2021 is predicted to increase with the presence of interstate highways (IS) and larger populations. Interestingly, the likelihood of infestation for a county in 2021 is predicted to increase with an increase in the number of garden centers only when there is also the presence of a primary interstate highway for that county.

<!-- image -->

## Model spaces

The model space consists of two interconnected networks with the included counties as the nodes. See Fig 5. The adjacency matrices for the adjacent counties networks ( A ) were constructed using data from [34]. The adjacency matrices for the primary interstate highway networks ( H ) were created using collected data on which primary interstates transect each county.

## Model parameterization

We fit the parameter p that represents the probability that an uninfested county adjacent to an infested county becomes infested from one year to the next year using the infestation data for 2014-2020 and following the approach in [27]. More specifically, we proceed in the following steps.

1. Find the 'time t to time t +1' infestation distribution as a function of infested adjacent counties using the 2014-2020 data. For all counties that are not infested at time t count the number of infested adjacent counties N i they have and calculate the proportion p I of the counties that got infested in the next time step t +1.
2. Use the result from step 1 to fit the parameter a in p I = 1 -e -aN i . The Matlab function fit was used for this and the result was a = 0 . 2902 with 95% confidence interval (0 . 2048 , 0 . 3756).
3. Use a to calculate the parameter p via p = 1 -e -a which yields p = 0 . 2519.

## Model implementation

See Table 1 for the symbols and description of the model components. Each simulation starts with Berks county, PA, as the only infested county in 2014. Berks county is county number 76 in our 166 county data so at time 0 (2014) the infestation vector, which is a 166 element column vector, contains only 0's except for the 76th element which is a 1. Then on each timestep t from 1 to T the infestation vector ¯ q t is updated by applying equations 1-3 and adding the result as a new column in a matrix Q via the following Matlab code

<!-- image -->

Figure 5: The model networks . The model space for the 166 county and the 581 county models consist of the combination of their adjacency and primary interstate networks. We note that the adjacency networks in both cases are fully connected, but that the primary interstate networks are not.

```
Q=[q]; %Initiate the matrix for collecting infested over time. for t=1:T q=(1-(1-p).^(A*q))>rand(N,1)-q; % adjacent spread q=(1/2)*(1-(1-sg).^(H*q))>rand(N,1)-q; % garden c interstate spread q=(1/2)*(1-(1-sp).^(H*q))>rand(N,1)-q; % population interstate spread Q=[Q,q]; %add updated infestation vector to matrix end
```

The output Q is a matrix that contains the infestation status of each county (rows) in each year from 2014 to 2014+ T (columns). sg is the garden center establishment probability vector (¯ s g in Table 2) and sp is the population establishment probability vector (¯ s p in Table 2). The reason for including the -q in the right hand sides of the implementation of each of the model equations is to ensure that counties that have once become infested stay infested. This works because if q i = 1 then the corresponding left hand side is always larger than the right hand side and county i will remain infested. This reflects reality, as no county that has become infested has subsequently become uninfested during the current US infestation.

## Model simulation and assessment

To assess the accuracy of the model in the 166 county region we ran 1000 simulations starting with Berks county, PA, as the only infested county in 2014 and recorded the proportion of simulations that yielded

each county infested in each year 2015-2021. Model assessment was carried out qualitatively by comparing infestation maps with model forecast maps through 2014-21 and quantitatively by defining a county infested if more than half of the simulations resulted in that specific county being infested in 2021. The qualitative comparison focused on comparing the overall annual range of the infestation and on the empirically observed corridors of spread west into OH, southwest along the VA-WV border, and south through VA. The quantitative assessment consisted of calculating the proportion of counties in the assessment region (Fig 1A) that the model accurately predicted the infestation status of. For example, if the 2021 data says that a county is infested and more than 500 (of 1000) model simulations resulted in it being infested that is a match, as is if both model and data says not infested. Any disagreement between model and data on a particular county was recorded as a mismatch.

Once the model had been assessed in the 166 county region we extended the region to include 581 counties and collected data for each of the factors included in the original 166 county model. To forecast the future spread in the 581 county region we used the same parameterized model and approach as for the simulation in the 166 county region, but simulated for a longer period of time (2014-25). We again started with Berks County, PA, as the only infested county in 2014 and ran 1000 simulations and collected the proportion of simulations that each county got infested in each year up to and including 2025.

## References

- [1] Surendra K Dara, Lawrence Barringer, and Steven P Arthurs. Lycorma delicatula (hemiptera: Fulgoridae): a new invasive pest in the united states. Journal of Integrated Pest Management , 6(1):20, 2015.
- [2] Jae-Min Jung, Sunghoon Jung, Dae-hyeon Byeon, and Wang-Hee Lee. Model-based prediction of potential distribution of the invasive insect pest, spotted lanternfly lycorma delicatula (hemiptera: Fulgoridae), by using climex. Journal of Asia-Pacific Biodiversity , 10(4):532-538, 2017.
- [3] Lawrence E Barringer, Leo R Donovall, Sven-Erik Spichiger, Daniel Lynch, and David Henry. The first new world record of lycorma delicatula (insecta: Hemiptera: Fulgoridae). Entomological news , 125(1):20-23, 2015.
- [4] Julie M Urban and Heather Leach. Biology and management of the spotted lanternfly, lycorma delicatula (hemiptera: Fulgoridae), in the united states. Annual Review of Entomology , 68:151-167, 2023.
- [5] New York State Integrated Pest Management. Spotted lanternfly. Technical report, https: //cals.cornell.edu/new-york-state-integrated-pest-management/outreach-education/ whats-bugging-you/spotted-lanternfly/spotted-lanternfly-reported-distribution-map , year=2023.
- [6] Julie M Urban. Perspective: shedding light on spotted lanternfly impacts in the usa. Pest management science , 76(1):10-17, 2020.
- [7] Heather Leach, David J Biddinger, Greg Krawczyk, Erica Smyers, and Julie M Urban. Evaluation of insecticides for control of the spotted lanternfly, lycorma delicatula,(hemiptera: Fulgoridae), a new pest of fruit in the northeastern us. Crop Protection , 124:104833, 2019.
- [8] Houping Liu. Occurrence, seasonal abundance, and superparasitism of ooencyrtus kuvanae (hymenoptera: Encyrtidae) as an egg parasitoid of the spotted lanternfly (lycorma delicatula) in north america. Forests , 10(2):79, 2019.
- [9] Doo-Hyung Lee, Yong-Lak Park, and Tracy C Leskey. A review of biology and management of lycorma delicatula (hemiptera: Fulgoridae), an emerging global invasive species. Journal of Asia-Pacific Entomology , 22(2):589-596, 2019.

- [10] Joseph A Francese, Miriam F Cooperband, Kelly M Murman, Stefani L Cannon, Everett G Booth, Sarah M Devine, and Matthew S Wallace. Developing traps for the spotted lanternfly, lycorma delicatula (hemiptera: Fulgoridae). Environmental Entomology , 49(2):269-276, 2020.
- [11] Miriam F Cooperband, Ron Mack, and Sven-Erik Spichiger. Chipping to destroy egg masses of the spotted lanternfly, lycorma delicatula (hemiptera: Fulgoridae). Journal of Insect Science , 18(3):7, 2018.
- [12] Spotted lanternfly control program in the mid-atlantic region-environmental assessment. Technical report, USDA APHIS, Washington DC. https://www.aphis.usda.gov/plant\_health/ea/downloads/ 2020/slf-mid-atlantic-region.pdf , 2020.
- [13] Rachel T Cook, Samuel F Ward, Andrew M Liebhold, and Songlin Fei. Spatial dynamics of spotted lanternfly, lycorma delicatula, invasion of the northeastern united states. NeoBiota , 70:23, 2021.
- [14] Tewodros T Wakie, Lisa G Neven, Wee L Yee, and Zhaozhi Lu. The establishment risk of lycorma delicatula (hemiptera: Fulgoridae) in the united states and globally. Journal of Economic Entomology , 113(1):306-314, 2020.
- [15] Tianxiao Hao, Jane Elith, Gurutzeta Guillera-Arroita, and Jos´ e J Lahoz-Monfort. A review of evidence about use and performance of species distribution modelling ensembles like biomod. Diversity and Distributions , 25(5):839-852, 2019.
- [16] Chris M Jones, Shannon Jones, Anna Petrasova, Vaclav Petras, Devon Gaydos, Megan M Skrip, Yu Takeuchi, Kevin Bigsby, and Ross K Meentemeyer. Iteratively forecasting biological invasions with pops and a little help from our friends. Frontiers in Ecology and the Environment , 19(7):411-418, 2021.
- [17] Chris Jones, Megan M Skrip, Benjamin J Seliger, Shannon Jones, Tewodros Wakie, Yu Takeuchi, Vaclav Petras, Anna Petrasova, and Ross K Meentemeyer. Spotted lanternfly predicted to establish in california by 2033 without preventative management. Communications Biology , 5(1):1-9, 2022.
- [18] Ruth E Baker, Jose-Maria Pena, Jayaratnam Jayamohan, and Antoine J´ erusalem. Mechanistic models versus machine learning, a fight worth fighting for the biological community? Biology letters , 14(5):20170660, 2018.
- [19] TC Baker, EC Smyers, JM Urban, Z Meng, KJ Pagadala Damadaram, AJ Myrick, MF Cooperband, and MJ Domingue. Progression of seasonal activities of adults of the spotted lanternfly, lycorma delicatula, during the 2017 season of mass flight dispersal behavior in eastern pennsylvania. Journal of Asia-Pacific Entomology , 22(3):705-713, 2019.
- [20] Michael S Wolfin, Muhammad Binyameen, Yanchen Wang, Julie M Urban, Dana C Roberts, and Thomas C Baker. Flight dispersal capabilities of female spotted lanternflies (lycorma delicatula) related to size and mating status. Journal of Insect Behavior , 32(3):188-200, 2019.
- [21] Ki-Jeong Hong, Jong-Ho Lee, Gwan-Seok Lee, and Seunghwan Lee. The status quo of invasive alien insect species and plant quarantine in korea. Journal of Asia-Pacific Entomology , 15(4):521-532, 2012.
- [22] Hyeban Namgung, Min-Jung Kim, Sunghoon Baek, Joon-Ho Lee, and Hyojoong Kim. Predicting potential current distribution of lycorma delicatula (hemiptera: Fulgoridae) using maxent model in south korea. Journal of Asia-Pacific Entomology , 23(2):291-297, 2020.
- [23] Zachary S Ladin, Donald A Eggen, Tara LE Trammell, and Vincent D'Amico. Human-mediated dispersal drives the spread of the spotted lanternfly (lycorma delicatula). Scientific Reports , 13(1):1098, 2023.
- [24] R Core Team. R: A Language and Environment for Statistical Computing . R Foundation for Statistical Computing, Vienna, Austria, 2023.

- [25] S. N. Wood. Thin-plate regression splines. Journal of the Royal Statistical Society (B) , 65(1):95-114, 2003.
- [26] Simon N Wood. Generalized additive models: an introduction with R . CRC press, 2017.
- [27] Brian Leung, John M Drake, and David M Lodge. Predicting invasions: propagule pressure and the gravity of allee effects. Ecology , 85(6):1651-1660, 2004.
- [28] David Dent and Richard H Binks. Insect pest management . Cabi, 2020.
- [29] Daniel Str¨ ombom and Swati Pandey. Modeling the life cycle of the spotted lanternfly (lycorma delicatula) with management implications. Mathematical biosciences , 340:108670, 2021.
- [30] Whit Winslow. North Carolina WINE Industry Facts. Technical report, https://www.ncwine. org/media#: ~ :text=North%20Carolina%20is%20home%20to,and%20European-style%20vinifera% 20grapes , 2017.
- [31] Agriculture Department To Business Travelers: Don't Take It With You Get A Spotted Lanternfly Permit. Pennsylvania Pressroom. Technical report, https://www.nj.gov/agriculture/news/press/ 2018/approved/press180823.html , 2021.
- [32] Apurba K Nandi and Hugh R Medal. Methods for removing links in a network to minimize the spread of infections. Computers &amp; Operations Research , 69:10-24, 2016.
- [33] Eva A Enns, Jeffrey J Mounzer, and Margaret L Brandeau. Optimal link removal for epidemic mitigation: A two-way partitioning approach. Mathematical biosciences , 235(2):138-147, 2012.
- [34] County Adjacency File. United States Census Bureau. https://www.census.gov/programs-surveys/ geography/library/reference/county-adjacency-file.html , 2020.
- [35] Pennsylvania Department of Agriculture 2015 Entomology Program Summary. Pennsylvania Department of Agriculture, Bureau of Plant Industry, Division of Entomology. Technical report, https://www.agriculture.pa.gov/Plants\_Land\_Water/PlantIndustry/Entomology/ Documents/PA%202015%20Activities%20Report%20for%20EPB.pdf , 2015.
- [36] Pennsylvania Department of Agriculture 2016 Entomology Program Summary. Pennsylvania Department of Agriculture, Bureau of Plant Industry, Division of Entomology. Technical report, https://www.agriculture.pa.gov/Plants\_Land\_Water/PlantIndustry/Entomology/ Documents/PA%202016%20Entomology%20Program%20Highlights.pdf , 2016.
- [37] Pennsylvania Department of Agriculture 2017 Entomology Program Report. Pennsylvania Department of Agriculture, Bureau of Plant Industry, Division of Entomology. Technical report, https://www.agriculture.pa.gov/Plants\_Land\_Water/PlantIndustry/Entomology/ Documents/PA%202017%20Activities%20Report%20for%20EPB.pdf , 2017.
- [38] Pennsylvania Department of Agriculture 2019 Entomology Program Report. Pennsylvania Department of Agriculture, Bureau of Plant Industry, Division of Entomology. Technical report, https://www.agriculture.pa.gov/Plants\_Land\_Water/PlantIndustry/Entomology/ Documents/2019-Entomology-Program-Highlights.pdf , 2019.
- [39] Spotted lanternfly sighting confirmed in hunterdon county. State of New Jersey Department of Agriculture. Technical report, https://www.nj.gov/agriculture/news/press/2018/approved/ press180823.html , 2018.
- [40] Spotted Lanternfly in Virginia. Virginia Polytechnic Institute and State University. Technical report, https://www.nj.gov/agriculture/news/press/2018/approved/press180823.html , 2018.

- [41] Google Maps. Google. https://www.google.com/maps , 2021.
- [42] County Population Totals: 2010-2019. United States Census Bureau. https://www.census.gov/data/ tables/time-series/demo/popest/2010s-counties-total.html , 2019.
- [43] Florian Hartig. DHARMa: Residual Diagnostics for Hierarchical (Multi-Level / Mixed) Regression Models , 2022. R package version 0.4.6.
- [44] Gavin L. Simpson. gratia: Graceful ggplot-Based Graphics and Other Functions for GAMs Fitted using mgcv , 2023. R package version 0.8.1.34.

## Supporting information

S1 Data. Data and simulation results. This Excel file contains all the data collected and generated in this study. It contains 4 tabs; 166 Region Data, 581 Region Data, 166 Region Model and 581 Region Model. The two Data tabs contain the collected data for each county in the respective regions. Specifically, county name, FIPS, number of garden centers, number of primary interstate highways (and their numbers) and population. The Model tabs contain the simulation outputs used to obtain the results presented in the manuscript with interactive maps. Readers can use these to run their own new simulations in Matlab (with or without changes to the code), export the results to the corresponding tab in this Excel file and see the results in map form. The 166 Region Model sheet also contains the calculations for the quantitative results, i.e. the number of model-data matches, false positives and false negatives.