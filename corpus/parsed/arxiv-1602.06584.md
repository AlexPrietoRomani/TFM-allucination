---
id: arxiv-1602.06584
title: A model-based approach to assess the effectiveness of pest biocontrol by natural enemies
year: 2016
country: Internacional
source: ArXiv (q-bio.PE)
doc_type: Artículo científico
language: en
tags:
  - control biológico
  - cultivos
  - plaguicidas
  - artículo científico
  - ArXiv
---

## A model-based approach to assess the effectiveness of pest biocontrol by natural enemies

Mamadou  Ciss a ,  Sylvain  Poggi b ,  Mohamed-Mahmoud  Memmah a ,  Pierre  Franck a ,  Marie Gosme c , Nicolas Parisey b , Lionel Roques d a INRA, UR 1115 Plantes et Systèmes de culture Horticoles, F-84000 Avignon, France b INRA UMR 1349 IGEPP, F-35653 Le Rheu Cedex, France c INRA, UMR 1230 SYSTEM, F-34060 Montpellier Cedex 2, France d INRA, UR 546 Biostatiques et Processus Spatiaux, F-84000 Avignon, France

## Abstract

Main  goal: The  aim  of  this  note  is  to  propose  a  modeling  approach  for  assessing  the effectiveness  of  pest  biocontrol  by  natural  enemies  in  diversified  agricultural  landscapes including several pesticide-based management strategies. Our approach combines a stochastic landscape  model  with  a  spatially-explicit  model  of  population  dynamics.  It  enables  us  to analyze  the  effect  of  the  landscape  composition  (proportion  of  semi-natural  habitat,  nontreated crops, slightly treated crops and conventionally treated crops) on the effectiveness of pest biocontrol. Effectiveness is measured through environmental and agronomical descriptors, measuring respectively the impact of the pesticides on the environment and the average agronomic productivity of the whole landscape taking into account losses caused by pests.

Conclusions: The  effectiveness  of  the  pesticide,  the  intensity  of  the  treatment  and  the  pest intrinsic growth rate are found to be the main drivers of landscape productivity. The loss in productivity  due  to  a  reduced  use  of  pesticide  can  be  partly  compensated  by  biocontrol. However, the model suggests that it is not possible to maintain a constant level of productivity while reducing the use of pesticides, even with highly efficient natural enemies. Fragmentation  of  the  semi-natural  habitats  and  increased  crop  rotation  tend  to  slightly enhance the effectiveness of biocontrol but have a marginal effect compared to the predation rate by natural enemies.

This  note  was  written  in  the  framework  of  the  ANR  project  PEERLESS  ``Predictive Ecological  Engineering  for  Landscape  Ecosystem  Services  and  Sustainability"(ANR-12AGRO-0006).

## Organization of the note

Section I is devoted to

- (1) the definition of the landscape models and the main types of landscape compositions that are compared in this note. The models presented in this section allow us to generate dynamic stochastic landscapes made of several types of land-uses with a control of the proportion occupied by each type of land-use, of the landscape fragmentation, and of the temporal changes in land-use;
- (2)  the  definition  of  a  spatially-explicit  dynamical  system  describing  pest  and  natural enemy interactions.

Section II is devoted to the definition of environmental and agronomical performance criteria. Section III describes:

- (1) the range of parameter values which are used in our numerical computations;
- (2) the design of the numerical experiments.

The results are presented in Section IV.

## I. The models

## I.1 Stochastic landscape models

General  framework. The  landscape  model  used  in  this  study  is  inspired  from  statistical physics  and  corresponds  to  an  extension  of  the  stochastic  model  proposed  by  Roques  and Stoica (2007). It is a neutral landscape model in the sense that the value associated to  each position  in  the  landscape  (the  land-use  in  the  present  case)  is  a  random  variable  (Gardner, 1987).  The  initial  model  proposed  in  Roques  and  Stoica  (2007)  only  generated  static  and binary  habitat/matrix  landscapes.  The  model  presented  here  allows  generating  dynamic stochastic  landscapes  made  of  several  types  of  land-uses  with  a  control  of  the  proportion occupied  by  each  type  of  land-use,  of  the  landscape  fragmentation,  and  of  the  temporal changes in land-use.

State space. Landscapes are defined on a lattice (grid with cells), each cell being attached to a given land-use. We assume that the lattice is of size , so that it corresponds to the set of all couples A landscape is a random field defined on the lattice and  that  assigns  each  site a  value corresponding  to  the  land-use.  The proportion of each land-use being fixed (respectively denoted by ), the state space is  defined  as  the  set  of  all  of  the  possible  landscapes corresponding  to  these  fixed proportions.

Static  landscape  model  (MULTILAND). In  a  first  step,  we  define  a  static  landscape  model with types of land-uses. The landscape model is based on the Gibbs measure describing the probability associated to each landscape :

where is a normalization constant and is related to the level of fragmentation of the first  type  of  land-use  in  the  landscape .  More  precisely, is  the  number  of  pairs  of similar  neighbors  in  the  region  occupied  by  the  land-use  1  (see  Roques,  2015  for  a mathematical definition of ). Thus, a landscape pattern is  all  the more aggregated as is high, and all the more fragmented as is small. Based on the quantity and using a method introduced in Garnier et al. (2012) we compute a fragmentation index in ( =1 corresponds to the most fragmented landscapes, see Roques, 2015). The parameter allows us the control of the fragmentation level of the landscapes drawn from the Gibbs  measure :  the  landscape  model  tends  to  produce  more  aggregated  landscapes  as increases and more fragmented landscapes as decreases. In our study, samples from the Gibbs measure were obtained using a Metropolis-Hastings algorithm (Robert and Casella,  2004),  with  adaptive  values  of to  reach  a  priori  fixed  fragmentation  indices.  A Matlab ® source code of the software MULTILAND is available at http://multiland.biosp.org.

Land-use distributions. We consider  24 x 24 lattice landscapes composed of four land-uses: (i) land-use 1 refers to semi-natural habitats, (ii) land-use 2 refers to crops with no pesticide, (iii) land-use 3 refers to slightly treated crops (moderate use of pesticides), and (iv) land-use 4 refers to conventionally treated crops.

Then, we consider five types of land-use distributions (balanced), (half occupied by semi-natural  habitats), (half  occupied  by  not  treated  crops), (half  occupied  by slightly  treated  crops) and (half  occupied by  conventionally treated crops), defined by the  proportions associated  with  each  land-use,  see  Table  1.  Figure  1  shows examples of landscapes generated with our model.

Table 1: Definition of the five types of land-use distributions (balanced), (half occupied by semi-natural habitats), (half occupied by not treated crops), (half occupied by slightly treated crops) and (half occupied by conventionally treated crops). The values associated with each generated  landscape  correspond  to  the  proportions  of  semi-natural  habitats  ( ),  crops  with  no pesticide , slightly treated crops , and conventionally treated crops ( ) respectively.

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 1/4: 1/2, 1/4: 1/6, 1/4: 1/6, 1/4: 1/6.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 1/4: 1/6, 1/4: 1/2, 1/4: 1/6, 1/4: 1/6.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 1/4: 1/6, 1/4: 1/6, 1/4: 1/2, 1/4: 1/6.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 1/4: 1/6, 1/4: 1/6, 1/4: 1/6, 1/4: 1/2.
Figure 1: Landscapes generated with our algorithm. From left to right: balanced distribution , half occupied by semi-natural ,  half  occupied by  non-treated ,  half  occupied  by  slightly  treated and    half  occupied  by  conventionally  treated .  Top  row:  fragmentation  index middle row: fragmentation index bottom row: fragmentation index The colors are:  green  for  semi-natural  habitats;  yellow  for  non-treated  crops;  dark  yellow  for  slightly  treated crops; and red for conventionally treated crops.

<!-- image -->

Dynamic  landscape  model. Our  algorithm  builds  sequences  of  landscapes associated with  a  sequence  of  times corresponding  to  changes  in  the  land-uses.  We  assume  that changes  in  landscapes  are  subject  to  the  following  constraints:  (i)  the  time  increments  are supposed to be constant and equal to one year ( ); (ii) at each change ( ),  a  proportion of  the  cultivated  landscape  is  modified  (this  corresponds  to  an  expected period of years between two changes for each crop in the lattice); (iii) the locations of semi-natural habitats (land-use of type 1) remain unchanged; (iv) the proportions associated with  each  type  of  land-use  remain  unchanged.  To  generate  a  sequence  of  landscapes satisfying  the  above  constraints,  we  first  generate  an  initial  landscape with  the  static MULTILAND model, using a Metropolis-Hastings MCMC algorithm. Then, given ,  the subsequent  landscape is  generated  by  continuing  the  Metropolis-Hastings  MCMC algorithm until a proportion of the landscape is modified.

## I.2. Population dynamics

We use  a  generalized  Lotka-Volterra  model  to  describe  the  populations  of  pests  and  their natural  enemies.  The  approach  adopted  here  falls  in  the  framework  of  lattice  dynamical systems. The main difference between this approach and the more classical reaction-diffusion approach relies in the fact that we work on a discrete space, which may be more suited to the landscapes defined in the previous section.

Using the lattice defined in  Section  I.1,  we  describe  the  dynamics of the pest population and of the population of natural enemies by the following equations:

where is  the  discrete  Laplace operator modeling the movements of the individuals and defined as: . This operator ensures that, during a time interval of length at each position a proportion of the pest population (resp. of the natural enemy population) moves to the adjacent cells. Thus and directly control the mobility of the pest and natural enemy populations. Here, is the length of a unit cell in the landscape. We assume periodic conditions at the boundaries of the lattice.

The  terms and correspond  to  the  pest  and  natural  enemy growth functions, while and describe the pest and natural enemy death rates caused by the use of pesticides. We assume that harvesting occurs at the end of each  year  (i.e.,  for  integer  values  of ),  and  that  during  the  first  half  of  each  year, =0 due to the absence of resource and (no treatment). The precise forms of these functions, depending on the land-use are detailed in Table 2. The interaction terms and describe the effects of predation on the pest and natural enemy growth rates, respectively.

The system (1) has been scaled so that the carrying capacities of and are both equal to 1 (this  means  that  the  population  densities  are  expressed  in  units  of  their  respective  carrying capacities).  We  also  assume  that (see  Section  III.1).    The  initial  condition  at is in  the  semi-natural  habitats and in  the  crops  and everywhere  (no pests). The pests are introduced at the beginning of year 3, with

Table  1: Values  of  the  growth  functions and and  of  the  pesticideinduced death rate in each land-use type ( SN : semi-natural habitat, NT : non-treated crop, ST : slightly treated crop, CT : conventionally treated crop) is  the  pest intrinsic growth rate in the crops in the absence of pesticide, the natural enemy life expectancy in the absence of resource and the natural enemy birth rate in semi-natural habitats. describes the effect of the pesticide on the pest and the natural enemies. The pesticides effects are assumed  (i) to be the same on the pests and the natural enemies and (ii) to be twice as large in conventionally treated crops (land-use type CT ) than in slightly treated crops (land-use type ST ) and zero elsewhere. is the nearest integer less than or equal to .

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Time span: Land use: CT.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Time span: Land use: ST.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Time span: Land use: NT.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Time span: Land use: SN.
## II. Performance criteria

## II.1 Environmental criterion

The environmental criterion is linked to the untreated proportion of the study site. With the assumptions  of  Section  I.2,  the  quantity  of  pesticide  in  slightly  treated  crops  is  half  the quantity in the conventionally treated crops.  Thus, the environmental criterion was expressed as follows:

This formula could be rewritten as follows:

where are  respectively  the  proportions  of  slightly  treated  crops  and  conventionally treated crops. Thus, if no pesticide were used while if the whole study site was conventionally treated .

## II.2 Agronomical criterion

The agronomical criterion reflects  the  average  productivity  of  the  landscape.  We  make  the assumption that, in the absence of pests, the productivity, measured at the end of each year, is proportional to the cultivated area. In the presence of pests, it is weighted by which corresponds to the unaffected resource (we recall that the pest density is expressed in unit of the carrying capacity, thus cannot reach values larger than 1).  With these assumptions, the agronomical criterion is formulated as follows:

with and is the upper time limit for our simulations which was fixed to 30 (years).  Note  that,  with  these  assumptions,  the  agronomical  criterion  reaches  its  maximum value  1  in  the  absence  of  pests  and  if  the  cultivated  area  occupies  the  entire  study  site. Inversely, the agronomical criterion reaches its minimum value 0 if, for each time , the level of  pests  reaches  its  maximum ( )  or  if  the  study  site  is  exclusively  made  of  seminatural habitats. Note that the environmental and agronomical criteria really play antagonistic roles in the sense that (i) if the whole study site was made of semi-natural regions, and ; (ii) if  all of the study site was conventionally treated and if all the pests were eradicated, and

## III. Simulation study

## III.1 Parameter values

Intrinsic growth rates Consider a Malthusian non-spatial model , corresponding to the absence of intraspecific and interspecific interactions, of dispersion and of pesticides. During 1/2 year (corresponding to the period between the emergence of the pest and  the  crop  harvest),  the  population  is  increased  by  a  factor . was  set  to  2ln(2), 2ln(50)  and  2ln(100),  corresponding  to  a  2-times,  50-times  and  hundred-times  population increase in each period. We assumed the increase factor for the natural enemy in semi-natural habitats to be 2 in one year (contrary to the pest, the natural enemy can grow even during the first  half  of  each  year  as  semi-natural  habitats  have  permanent  resources),  meaning  that

Diffusion  coefficients . At    each  time  step a  proportion of  the population (pest or natural enemy) situated in a cell moves into the surrounding cells. We assumed that between and of  the  population  moved  to  the  surrounding  cells  per

day, corresponding approximatively to , with /365 year = 1 day and

Effect of pesticide ( ) . We assumed that the mortality rate induced by the use of pesticide can reach levels comparable to the pest growth rates: }.

Life  expectancy  of  the  natural  enemies  on  the  crops  ( ) .  We  assumed  a  life  expectancy  of year in the crops, in the absence of pests.

Interaction  terms  ( ) .  Consider  an  isolated  and  non-treated  crop .  In  the  absence  of dispersion, and assuming that , the equation (1) becomes:

The steady states of this system are and , which corresponds to a coexistence state between the pest and its natural enemy. This last state only exists (and is stable)  if Here,  we  chose such  that  the  steady  state  corresponding  to  the  pest population is equal to (high effect of predation) or (moderate effect of predation) of the carrying capacity. Namely, We also consider the case where there is no effect  of  predation: Note that equilibrium density of the prey in the above reduced system does not depend on For the sake of simplicity, we assume that

## III.2 Numerical experiments

Numerical  simulations  were  conducted  for  the  five  contrasted  distributions  of  land  uses described  in  Table  1  and  Figure  1.  Each  of  these  land-use  distributions  corresponds  to  a specific  value  of  the  environmental  criterion: , , , and .

For each land-use distribution, each value of the fragmentation index (Table 2), and each value of the crop rotation index we generated sequences of landscapes with the dynamic landscape  model  presented  in  Section I.1.  This  makes  a  total  of sequences of landscapes.

The dynamics of the pest and  of  its  natural  enemy  were  simulated  in  these  landscapes  for three different values of each of the five parameters ,  ,  , and (Table 2), i.e. =243 combinations of the biological/pesticide parameters. This corresponded to a total of simulations. These simulations were performed with Matlab ® .

Table 2: Parameter values used in our simulations. These values are explained in Section III.1.

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Dynamic landscape model, Description: Dynamic landscape model.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Fragmentation index, Description: Dimensionless, Unit: {0.1,0.5,0.9}.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Crop rotation index, Description: Dimensionless, Unit: {0,0.1,0.5}.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Size of the lattice, Description: Dimensionless, Unit: 24.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Model of population dynamics, Description: Model of population dynamics.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Pest diffusion coefficient, Description: Unit area.year -1.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Natural enemy diffusion coefficient, Description: Unit area.year -1.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Pest intrinsic growth rate, Description: year -1.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Predation index, Description: Unit area indiv -1 year -1.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Pesticide effect, Description: year -1.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Parameter: Life expectancy of the natural enemy, Description: year, Unit: 1/2.
## IV. Results

## IV. 1 Effect of land-use distribution on landscape productivity

The  agronomical  performance  criterion AGRO tends  to  be  negatively  correlated  with  the environmental  criterion ENVI across  the  five  land-use  distributions:  the  mean  value  for AGRO criterion over the 65610 simulations of each land-use distribution is 0.66, 0.63, 0.55, 0.5 and 0.38, for and respectively (Figure 2), while , , , and . However, the variability among the AGRO criterion values obtained with different sets of  parameters  remains  high,  showing  that  for  a  given  level  of  the  environmental  criterion, there might be room for improvement of the agronomical criterion.

Figure 2: Boxplots of the agronomical performance criterion AGRO as a function of the five land-use distributions (balanced), (half occupied by semi-natural habitats), (half occupied by not treated crops), (half occupied by slightly treated crops) or (half occupied by conventionally treated crops). The red points correspond to the mean AGRO value of each land-use distribution, the value of the environmental criterion of each land-use distribution is given for reference above each boxplot. in each boxplot, the red point indicates the mean.

<!-- image -->

## IV. 2 Effect of crop rotation on landscape productivity

Rotation frequency ( )  has significant effects on agronomical performances only when pest populations has low growth rate or/and weak dispersion ability. When pest growth rate is low ( )  there  is  a  positive  relationship  between and  AGRO  (Figure  3);  this relationship is even stronger when the pest diffusion coefficient is also low ( and ). This relationship can be observed for all 5 landscape compositions.

<!-- image -->

μ

Y

Figure 3: Boxplots of the agronomical performance criterion ( ) as a function of rotation index corresponding  to  the  average  proportion  of  crops  (land-use  types  CT,  ST  or  NT)  modified  in  the landscape per year. The first row line corresponds to results of all simulations pooled for a given landuse distribution, the second row corresponds to the subset of simulations with low pest growth rate ( ) and the third row corresponds to the subset of simulations with both low pest growth rate ( ) and low pest diffusion coefficient ( ). Red points indicate the mean.

## IV. 3 Relative effects of the input variables on landscape productivity

A linear model (with centered and reduced data) was computed to explain the agronomical performance as function of the model parameters:

All the statistical analyzes were performed with R software. All tested model parameters have a significant linear effect on the agronomical performance (Table 3), but the estimates of the regression parameters indicate that some parameters have a strong impact on the agronomical performance (pesticide efficiency ( ),  pest  growth rate ( )  and predation index ( )),  while the rest have a much smaller effects (rotation frequency index (μ), fragmentation index ( ), pest diffusion coefficient ( ) and natural enemy diffusion coefficient ( )). Unsurprisingly, pesticide effect and predation index have a positive effect on the agronomical criterion while pest growth rate has a negative effect. There is an interaction between the effects of pesticide efficiency and predation index: the effect of the predation rate is stronger when the pesticide efficiency is low (Table 4).

Table 3: Linear regression of as  a  function  of  fragmentation index ( ),  rotation  frequency index (μ), pesticide effects ( ),  pest growth rate ( ),  pest diffusion coefficient ( ), natural enemy diffusion coefficient ( ) and predation index ( ).

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: 0.02, Std. Error: 0.00114, t value: 19.29, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: 0.03, Std. Error: 0.00114, t value: 22.32, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: 0.44, Std. Error: 0.00114, t value: 394.06, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: -0.56, Std. Error: 0.00114, t value: -495.05, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: 0.05, Std. Error: 0.00114, t value: 44.81, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: -0.02, Std. Error: 0.00114, t value: -17.17, Pr(>&#124;t&#124;): <2e-16 ***.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), Estimate: 0.22, Std. Error: 0.00114, t value: 196.37, Pr(>&#124;t&#124;): <2e-16 ***.
Table 4: Mean values of the criterion (±sd) as function of different combination of predation index and pesticide index   values.

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 0.35±0.22: 0.39±0.21, 0.58±0.17: 0.59±0.16, 0.59± 0.17: 0.60± 0.16.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 0.35±0.22: 0.53±0.15, 0.58±0.17: 0.64±0.13, 0.59± 0.17: 0.65±0.13.
For the parameters with small effects, the interpretation of the effects is less straightforward: both fragmentation and rotation frequency increase the agronomical criterion. The diffusion coefficient  of  the  pest  also  increases  the  agronomical  criterion  while  the  natural  enemy's diffusion coefficient reduces it. There is an interaction between fragmentation and predation index:  an  increased  fragmentation  increases  slightly  the  agronomical  performance  for  all configurations, but only if predation can occur (Table 5 ) .

Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 0.50±0.22: 0.52± 0.21, 0.50± 0.21: 0.53± 0.20, 0.50± 0.21: 0.53± 0.20.
Según A model-based approach to assess the effectiveness of pest biocontrol by natural enemies (2016), 0.50±0.22: 0.60± 0.15, 0.50± 0.21: 0.61± 0.14, 0.50± 0.21: 0.61±0.14.
Table 5: Values of mean value of the (±sd) criterion as a function of the predation index and the fragmentation level .

## References

Gardner, R. H., Milne, B. T., Turner, M. G., &amp; O'Neill, R. V. (1987). Neutral models for the analysis of broad-scale landscape pattern. Landscape Ecology, 1 (1), 19-28.

Garnier, J., Roques, L., &amp; Hamel, F. (2012). Success rate of a biological invasion in terms of the spatial distribution of the founding population. Bulletin of Mathematical Biology, 74 (2), 453-473.

Robert, C., &amp; Casella, G. (2004). Monte Carlo Statistical Methods . Paris, France, Springer.

Roques, L. (2015). Multiland: a neutral landscape generator designed for theoretical studies. arXiv:1503.07215v1.

Roques, L., &amp; Stoica, R. S. (2007). Species persistence decreases with habitat fragmentation: an analysis in periodic stochastic environments. Journal of Mathematical Biology, 55 (2), 189205.