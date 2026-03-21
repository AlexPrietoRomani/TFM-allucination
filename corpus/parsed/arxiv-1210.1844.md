---
id: arxiv-1210.1844
title: Prediction of invasion from the early stage of an epidemic
year: 2012
country: Internacional
source: ArXiv (q-bio.PE, stat.AP)
doc_type: Artículo científico
language: en
tags:
  - patógenos vegetales
  - epidemiología
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Prediction of invasion from the early stage of an epidemic

Francisco J. P´ erez-Reche 1 , ∗ , Franco M. Neri 2 , Sergei N. Taraskin 3 , Christopher A. Gilligan 2

1 SIMBIOS Centre, University of Abertay Dundee, Dundee, UK

2 Department of Plant Sciences, University of Cambridge, Cambridge, UK

3 St. Catharine's College and Department of Chemistry, University of Cambridge, Cambridge, UK

∗ E-mail: p.perezreche@abertay.ac.uk

## Abstract

Predictability of undesired events is a question of great interest in many scientific disciplines including seismology, economy, and epidemiology. Here, we focus on the predictability of invasion of a broad class of epidemics caused by diseases that lead to permanent immunity of infected hosts after recovery or death. We approach the problem from the perspective of the science of complexity by proposing and testing several strategies for the estimation of important characteristics of epidemics, such as the probability of invasion. Our results suggest that parsimonious approximate methodologies may lead to the most reliable and robust predictions. The proposed methodologies are first applied to analysis of experimentally observed epidemics: invasion of the fungal plant pathogen Rhizoctonia solani in replicated host microcosms. We then consider numerical experiments of the SIR (susceptible-infected-removed) model to investigate the performance of the proposed methods in further detail. The suggested framework can be used as a valuable tool for quick assessment of epidemic threat at the stage when epidemics only start developing. Moreover, our work amplifies the significance of the small-scale and finite-time microcosm realizations of epidemics revealing their predictive power.

## 1 Introduction

Predictability of catastrophic events such as earthquakes, epidemics, fracture or financial crashes [1-3] is a topic of increasing interdisciplinary interest. The predictability of these events is inextricably linked to the inherent complexity of the phenomena under consideration [1,2]. Here, we focus on epidemiology. Within this context, many studies have been devoted to prediction of the temporal incidence of epidemics (i.e. the evolution of the number of infected hosts in the course of an epidemic) [4-8]. Recently, an increasing number of papers have also considered the prediction of the spatio-temporal evolution of epidemics [9-12].

Both the temporal and the spatio-temporal incidence depend on complex factors related to the transmission of infection and the properties of the hosts. For instance, the hosts are not identical in susceptibility and transmissibility of infection due to difference in age, size, genotype and neighbourhood. [5,9,10,13]. The transmission of infection is stochastic, meaning that a healthy host is infected by contact with inoculum from an infected host with a certain probability only. Many epidemics, notably those involving transmission by invertebrate vectors, or by wind and rain for many plant pathogens, are subject to variability in weather. This environmental stochasticity can also influence the evolution of epidemics in such heterogeneous systems [14]. All these factors make prediction of disease incidence an extremely challenging and sometimes controversial task [4, 15, 16]. In Ref. [4], it was suggested that, although obtaining precise quantitative predictions for the incidence would be obviously desirable, qualitative predictions may be more valuable. This is very much along the lines of ideas from the science of complexity claiming that, despite the fact that giving accurate predictions for the detailed evolution of complex systems might be an illusory task, certain qualitative features of the evolution, such as occurrence or absence of a catastrophic event, could be more amenable for prediction [2,17,18].

Here, we address the question of predictability of epidemics using a methodological framework inspired by the science of complexity. The main aim is to estimate the probability that an emerging epidemic will

invade a significant fraction of the population in the future. This quantity can be viewed as a qualitative feature of the complete spatio-temporal evolution of epidemics.

We propose several methods for approaching the problem that offer different levels of precision. Our results suggest that the most precise methods do not necessarily lead to more reliable predictions. Instead, parsimony seems to be the key ingredient for prediction based on inherently limited observations. The framework presented below deals with epidemics caused by a broad class of pathogens leading to permanent immunity of infected hosts after recovery (or death). There are numerous examples of such diseases affecting populations of humans [19,20], animals [21] and plants [22]. The advantage in analysis of such epidemics is that they are characterised by a well-defined final state consisting of only hosts that were never infected and hosts that were infected and became immune. In particular, we focus on the estimation of the probability that an epidemic is invasive in the final state.

The proposed methods are first applied to prediction of invasion of a pathogen in an experimental model system in which the fungal plant pathogen, Rhizoctonia solani , spreads through a population of hosts represented by discrete nutrient sites. The properties of the sites, e.g. nutrient concentration, can be varied for different realisations of epidemics. Such a system is convenient for generation and observation of rapid, highly replicated and repeatable epidemics and it is used as a benchmark for description of our methodologies and analyses. The epidemic prediction analysis for experimental system is followed by a test of our methods in numerical experiments for epidemics spreading on networks of hosts arranged on a regular lattice. The advantage of investigating such epidemics is that their properties are known beforehand and this allows us to provide a precise analysis of the performance of prediction methods by comparing with the expected behaviour.

## 2 Methods

The methods follow four steps that are basic for any scientifically meaningful prediction of the behaviour of a complex system: (i) Observation of the initial evolution of the process over a certain period of time, t obs . (ii) Construction of a model for description of the observed behaviour. (iii) Fitting the model to the data obtained from observations. (iv) Extrapolation of the behaviour to the future by using the model with the fitted parameters. These steps are interconnected and we argue that they should be kept at a similar level of complexity in order to make their interplay as consistent as possible. In this paper, we investigate whether or not such consistency is important for obtaining reliable predictions by exploring several combinations of strategies for steps (i)-(iii) (see summary in Table 1).

For concreteness, we illustrate our prediction methods for the particular case of fungal colony invasion in microcosms comprising populations of nutrient sites (agar dots) [23]. In these experiments, the central agar dot in ensembles with the geometry shown in Fig. 1 was inoculated by the soil-borne fungal plant pathogen R. solani and the spread of the fungal colony is scored in discrete time steps (e.g. daily).

Según Prediction of invasion from the early stage of an epidemic (2012), Methodology: A B, Step (i): data: Mean field (MF), C ( t ), Step (ii): model: RF RF, Step (iii): fitting: MD ABC, Parameters: (ii) T, ̂ τ exp (ii) T, τ exp . (iii) /epsilon1, d 2: d 2 c = ∑ t [ c sim ( t ) - c obs ( t )] 2.
Según Prediction of invasion from the early stage of an epidemic (2012), Methodology: C D E, Step (i): data: Shell, F ( l, t ), Step (ii): model: RF RF CT, Step (iii): fitting: MD ABC, Parameters: ̂ (ii) T, ̂ τ exp (ii) T, ̂ τ exp . (iii) /epsilon1 (ii) T, τ 0 ,k . (iii) /epsilon1, d 2: d 2 f = ∑ l,t [ F sim ( l, t ) - F obs ( l, t )].
Según Prediction of invasion from the early stage of an epidemic (2012), Methodology: F, Step (i): data: Site, { t i }, Step (ii): model: CT, Step (iii): fitting: DA-MCMC, Parameters: (i) { t i } . (ii) T, τ 0 ,k.
Table 1. Overview of methods for prediction. Combination of possible data sets considered in step (i) and methods used for addressing steps (ii) and (iii) in the prediction process. The first column introduces a label for each set of methods, which are ordered according to their overall expected precision. The second column gives the format of the data obtained from observations in step (i). The smallest precision of the data corresponds to methods A and B in which only the incidence, C ( t ), is used. Methods C-E use a limited spatio-temporal knowledge of the evolution of the infection given by the shell-evolution function F ( l, t ). Method F uses the time of infection of each host, { t i } , which is typically unknown from observations but can be inferred in step (iii). In step (ii), RF and CT are abbreviations for the Reed-Frost and continuous-time model, respectively. In step (iii), we have used several methods for fitting: Minimum Distance (MD), Approximate Bayesian Computation (ABC), and data-augmented Markov Chain Monte Carlo (DA-MCMC). Column five lists the parameters involved in each step for prediction of the fungal invasion in the agar-dot experiment. Methods based on the RF dynamics are parametrised by the transmissibility, T , and a time scale ̂ τ exp . The CT dynamics used in methods E and F is parametrised by T , a characteristic time τ 0 , and a shape parameter for the time-dependence of the transmission of infection, k . The RF dynamics corresponds to the limit k →∞ of the CT dynamics. The MD method for fitting consists in minimising the parameter d 2 (last column) which measures the difference between observations and numerical simulations. The ABC fitting procedure assumes that a simulated invasion fits well the observed epidemic if d 2 &lt; /epsilon1 , where /epsilon1 is a free parameter. As shown in the last column, the definition of d 2 depends on the descriptors for observations used in step (i). For methods A and B, d 2 is defined in terms of the observed and simulated incidences, c obs ( t ) = C obs ( t ) /N and c sim ( t ) = C sim ( t ) /N , normalised to the number of hosts in the population, N . In methods C-E, d 2 is defined in terms of the shell-evolution function for observations and simulations. Sections I and II of SI Appendix give more details on the definition of models used in step (ii) and fitting methods used in step (iii).

In the following, we give a general description of the steps for prediction of epidemic invasion with particular assumptions suitable for the analysis of the fungal invasion experiment. The main details of all the methodologies are summarised in Table 1. The methodology C is mainly used for illustration of our concepts. Details of other explored methodologies are given in SI Appendix . The motivation for choosing methodology C is twofold: (i) it keeps all the steps for prediction of the behaviour at a similar level of complexity, as illustrated by analysis of the fungal colony invasion in the agar-dot experiment; (ii) it is a parsimonious methodology that leads to predictions that are, at least, as robust as (or, arguably, even more robust than) those based on more sophisticated approaches (Table 1).

Step (i). The information that can be extracted from observation of the time evolution of epidemics is usually limited. In many cases, the only available information is the incidence, C ( t ) (the number of infected hosts), at subsequent observations, and occasionally the spatial location of infected hosts is also known, e.g. for epidemics in populations of plants [8, 22, 24, 25]. These limitations have a dramatic influence on subsequent steps in the prediction process and it is crucial to identify which quantities are sufficient for prediction of the catastrophic event (i.e. the probability of an invasive epidemic in our case). As shown in Table 1, we consider three types of observations. The first consists of discrete temporal observations of C ( t ) (Methods A and B in Table 1). The second possibility (Methods C-E) considers discrete spatio-temporal observations giving the evolution of infection at discrete times, t , in shells at a 'chemical distance' l from the initially inoculated host. As explained in Fig. 1(a), such observations can be properly described in terms of a shell-evolution function F ( l, t ). As a third possibility (Method F), we use a method for data augmentation in step (iii) that infers the unobserved time of infection for each host, { t i } [8, 24, 25].

Step (ii). We describe the evolution of the epidemic in terms of a spatial SIR (susceptible-infectedremoved) epidemiological model where the hosts can be either susceptible (S), infected (I) or removed (R) [19, 21, 22, 26]. This is a prototype model for a wide class of epidemics where disease leads to permanent immunity of hosts after recovery or death. In particular, this paradigm has been shown to be appropriate for description of fungal invasion [23,27,28]. In principle, a continuous-time dynamic model is necessary to provide a precise description of epidemic evolution characterised by stochasticity in times of infection and removal/recovery of hosts. Following this idea, it would be natural to use a model with continuous-time (CT) dynamics (described in SI Appendix ). The drawback of this approach is that it requires knowledge of the precise times of infection of hosts, { t i } , which are typically not available from discrete spatio-temporal observations in step (i). In order to match an appropriate model with the level of detail of observations, we consider the discrete-time dynamics model which reduces the SIR framework to the so-called Reed-Frost (RF) model [29]. This simplified description is not expected to capture the dynamical details of the evolution of the epidemic but reproduces well its final state [30, 31]. This is a very important consequence of the fact that, no matter how complicated the evolution of the epidemic is, the final state of an epidemic with death of infected individuals or permanent acquired immunity after recovery depends only on the probability T , called transmissibility, that the infection has ever been passed between each pair of connected hosts (as shown in Fig. 1(b)). Although the transmissibility is expected to exhibit a certain degree of spatial heterogeneity in real epidemics, we make the minimal assumption that the trend of the epidemic can be well approximated by a RF process with a homogeneous effective transmissibility T .

Step (iii). The goal of this step is to estimate the values of the parameters of the model used in step (ii) that give a good description of the observations. Consider, for definiteness, methodology C in Table 1. Due to factors such as stochasticity and heterogeneity in transmission, a given observed spatiotemporal map for infection can occur for different values of the estimated transmissibility, ̂ T . However, some of these values for ̂ T are more likely to produce the observed spatio-temporal pattern than others. To account for this, we introduce the probability density function (p.d.f.), ρ ( ̂ T ), which quantifies the probability that the observed spatio-temporal pattern is reproduced by a certain value of ̂ T . As shown schematically in Fig. 1(c), ρ ( ̂ T ) is calculated by generating a large number of stochastic realizations

Figure 1. Steps for prediction used in methodology C (Table 1). (a-left) Discrete spatio-temporal observations of evolution (spatio-temporal map) of a hypothetical epidemic spreading from the central host in a population of hosts (circles) arranged on a triangular lattice with lattice spacing a and L hosts per side of the hexagonal boundaries of the system. The arrangement of nutrient sites in the fungal invasion experiment analysed below is of this type. Numbers inside the circles denote the times, t = 0 , 1 , . . . , of infection of hosts by the observation time t obs = 2. Empty circles correspond to healthy (susceptible) hosts by the same time. The hexagons with dotted lines indicate the shells of hosts at a given chemical distance, l , to the centre of the system. (a-right) The spatio-temporal evolution of the epidemic is described by the shell-evolution function F ( l, t ) giving the relative number of hosts in layer l infected by time t . For instance, F (2 , 2) = 3 / 12 for the epidemic shown in the (a-left) panel. (b) In step (ii), the epidemic is described in terms of an SIR model. An infected host, I © , remains infectious during the infectious period τ which, for simplicity, is taken as being constant over the whole population and set as a unit of time, τ = 1. After the infectious period τ , the host is removed, R © . During the time τ , I © can transmit the infection to a neighbouring susceptible host, S © , with probability T (transmissibility). Alternatively, I © can be removed without passing the infection to S © with probability 1 -T . In the discrete time Reed-Frost (RF) dynamics used in our approach, the infection is passed instantaneously from I © to S © at t = τ . (c) In step (iii), the fitting procedure consists in finding the probability density function (p.d.f.) ρ ( ̂ T ) for transmissibilities ̂ T (c-left) such that a RF process with ̂ T and shell-evolution function F sim ( l, t ) give a good description of the observed shell-evolution function, F sim ( l, t ) (c-right). For visualization clarity in c-right, an example of F sim ( l, t ) represented by the blue-grid surface does not fit well the observed shell-evolution function, F obs ( l, t ) (the shaded surface). The p.d.f. ρ ( ̂ T ) is obtained by running many RF epidemics with random transmissibility and minimising the parameter d that quantifies the difference between the observed and the RF shell-evolution functions. (d) Once ρ ( ̂ T ) has been obtained (continuous curves in c-left and d-left), the probability of an invasive epidemic, ̂ P inv ( L ), can be calculated by Eq. (1) which involves the conditional probability of invasion P inv ( ̂ T ; L ) for any given ̂ T (dashed line in d-left). The value of ̂ P inv ( L ) is represented graphically in d-right by the area under the curve (shaded region) for the function P inv ( ̂ T ; L ) ρ ( ̂ T ).

<!-- image -->

of the RF epidemic with transmissibilities T sampled uniformly from the interval [0 , 1] and comparing their shell-evolution functions, F sim ( l, t ) (see caption to Fig. 1 for definition), with the observed one, F obs ( l, t ). Ideally, the distribution ρ ( ̂ T ) would correspond to the histogram of values for ̂ T producing shell-evolution functions F sim ( l, t ) identical to F obs ( l, t ) but obtaining an exact match is computationally very demanding. Moreover, reproducing F obs ( l, t ) by a RF model is in general impossible in realistic epidemics for which time is not discrete. Therefore, we use a minimum distance (MD) algorithm to calculate ρ ( ̂ T ) approximately as the histogram of values of ̂ T minimising the quantity d 2 f defined in Table 1 that measures the distance between F sim ( l, t ) and F obs ( l, t ). In this way, the sampled values of ̂ T reproduce F obs ( l, t ) approximately rather than necessarily with distance d 2 f = 0. This approach is similar to the Approximate Bayesian Computation (ABC) method that determines ρ ( ̂ T ) as the histogram of values of ̂ T for which d 2 f ≤ /epsilon1 , where /epsilon1 is a parameter used in the method [32]. Both ABC and MD algorithms give similar results despite the fact that MD does not require the use of an additional parameter /epsilon1 . In addition to these approximate methods, we have fitted the spatio-temporal evolution of the CT model proposed in step (ii) for comparison by means of a more standard Bayesian procedure using Markov chain Monte Carlo (MCMC) method with data augmentation (method F in Table 1).

Step (iv). In the final stage of the prediction process, given ρ ( ̂ T ), we evaluate the probability ̂ P inv ( L ) that the observed epidemic will ever invade a system of size L . The epidemic is defined as being invasive if the final cluster of removed hosts has reached at least one node on each of the six edges of the system. Otherwise, the epidemic is classified as being non-invasive. The conditional probability of invasion P inv ( ̂ T ; L ) in a system of size L by an SIR process with a given transmissibility , ̂ T , can be calculated numerically by running many stochastic realisations of the epidemic and counting the fraction of invading events. As shown in Fig. 1(d), P inv ( ̂ T ; L ) exhibits a sigmoidal dependence on ̂ T which indicates a non-invasive (invasive) regime of epidemics for relatively small (large) values of ̂ T . Once P inv ( ̂ T ; L ) and ρ ( ̂ T ) are known, the estimated probability of invasion can be calculated as follows:

This formula defines the probability that the invasion occurs given our knowledge about the effective transmissibility encoded by ρ ( ̂ T ) (see a simple graphical interpretation in terms of the shaded area in Fig. 1(d)). Importantly, Eq. (1) gives an extrapolation of the behaviour of the epidemic to its final state without necessarily providing a detailed description of the actual evolution leading to such a state.

<!-- formula-not-decoded -->

## 3 Application to fungal invasion

In the fungal invasion experiments, the spatio-temporal maps of infected agar dots were scored daily over 21 days (see two typical patches of colonisation after 21 days in Fig. 2(a)). The transmissibility in this experiment corresponds to the probability of fungal colonisation between two adjacent agar dots and it was controlled by variable lattice spacing, a = 8 , 10 , 12 , 14 , 16 , 18 mm. Clearly, the experimental setup is restricted both in space and time. Our aim is to use these limited observations to estimate the probability of invasive epidemics in larger systems and for longer times. The analysis is performed for each individual realisation of the experiment (6 replicates per value of a ).

In order to make a proper comparison between the experimental observations with the RF model used in methods A-D, it is necessary to rescale the time step of the RF dynamics with dimensionless τ = 1 to ̂ τ exp measured in days. The value of ̂ τ exp is not known and it is treated at the same level as the transmissibility. More explicitly, we deal with a bi-variate probability density function, ρ 2 ( ̂ T, ̂ τ exp ), which can be determined for each epidemic with a simple extension of the methods explained in Sec. 2 (step (iii)) for obtaining ρ ( ̂ T ). The estimated ̂ P inv is obtained from Eq. (1) by defining ρ ( ̂ T ) as the marginal p.d.f.,

Figure 2. Fungal invasion in the system of agar dots placed on a triangular lattice. (a) The observed mean probability of invasion P exp obtained by counting the relative number of invasive epidemics after 21 days is shown by the continuous line. The probability of invasion after 21 days was estimated for each replicate by observing the initial evolution of colonisation during t obs = 10 days. The corresponding mean over replicates with the same value of a is shown with a different symbol type (the same as in Figs. 4-5) for each method for prediction. The inserts show the invasive (left) and non-invasive (right) state of the epidemic after 21 days for two representative replicates with lattice spacings a = 10 mm and a = 14 mm, as marked by arrows. Solid (open) circles in the inserts represent colonised (not colonized) dots. (b) Prediction of ̂ P inv with different methodologies for individual replicates of the epidemic in a large system of size L = 51 obtained from observations during t obs = 21 days of the smaller experimental system ( L &lt; 8). The mean of ̂ P inv over replicates for each value of a is shown by different symbol types corresponding to different methodologies. The mean probability of invasion P exp obtained by counting the relative number of invasive epidemics after 21 days is shown by the continuous line.

<!-- image -->

Figure 3. Estimates of the transmissibility for fungal invasion in the system of agar dots. The p.d.f.'s ρ ( ̂ T ) obtained with different fitting methodologies are plotted for the fungal colony invasion in a population of agar dots with lattice spacing a = 10 mm. Estimates correspond to observation of the fungal spread during t obs = 21 days. Different symbol types correspond to different fitting methodologies, as marked in the legend. Fig. S1 in SI Appendix shows similar plots for six replicates of the system.

<!-- image -->

ρ ( ̂ T ) = ∫ ∞ 0 ρ 2 ( ̂ T, ̂ τ exp )d ̂ τ exp . As explained in more detail in Sec. I of SI Appendix and summarised in Table 1, the continuous-time SIR model used in methods E and F involves three parameters: T , τ 0 , and k . The fitting of the data results in a p.d.f. ρ 3 ( T, τ 0 , k ) from which we obtain ρ ( ̂ T ) = ∫ ∞ 0 ρ 3 ( ̂ T, τ 0 , k )d τ 0 d k . The probability of invasion is then calculated from Eq. (1) in the same way as for methods A-D.

## 3.1 Uncertainty of the estimated transmissibility

The functions ρ ( ̂ T ) obtained for the fungal invasion experiments typically exhibit a pronounced peak (see the results for one replicate in Fig. 3 and similar results for more replicates in Fig. S1 of SI Appendix ). The peaked shape of ρ ( ̂ T ) suggests that ̂ T can be suitably described in terms of its mean value 〈 ̂ T 〉 and standard deviation σ T = ( 〈 ̂ T 2 〉 - 〈 ̂ T 〉 2 ) 1 / 2 . For each methodology, Fig. 4 shows the average over replicates of 〈 ̂ T 〉 and σ T as a function of the lattice spacing. These estimates correspond to observations of the evolution of infection during t obs = 21 days. All the methods give similar values for 〈 ̂ T 〉 which have a clear and expected tendency to decrease with increasing a . The uncertainty in ̂ T , quantified by σ T , exhibits greater variations between methodologies but it takes values that are smaller than 〈 ̂ T 〉 for all the methods and lattice spacings (Fig. 4(b)). This means that 〈 ̂ T 〉 is a good measure of the typical value of the transmissibility. However, the value of 〈 ̂ T 〉 on its own does not necessarily provide a good approximation for ̂ P inv because the width of ρ ( ̂ T ) can bring a significant contribution to the integral in Eq. (1). This is explicitly shown in Sec. 4. Comparison of 〈 ̂ T 〉 , σ T , and ρ ( ̂ T ) for different methods leads to the following conclusions: (1) Given a level of description (step (i)) and a model (step (ii)), the estimates of the transmissibility obtained with ABC and MD methods are, in general, in good agreement (cf. method A with method B, and method C with method D in Figs. 3 and 4).

- (2) Given a level of description (step (i)) and an estimation method (step (iii)), the posteriors obtained

Figure 4. Statistical characteristics of the estimates of the transmissibility for fungal invasion in the system of agar dots. Dependence on the lattice spacing of (a) the mean value 〈 ̂ T 〉 , and (b) standard deviation σ T of the transmissibility calculated from the p.d.f. ρ ( ̂ T ) corresponding to observations during t obs = 21 days. For clarity, each symbol gives the average of (a) 〈 ̂ T 〉 and (b) σ T over 6 replicates of the experiments for each lattice spacing, a . As marked in the legend, different symbol types correspond to different methods for addressing the steps (i)-(iii) summarised in Table 1.

<!-- image -->

using discrete- and continuous-time models are in reasonable agreement (cf. method D with method E in Figs. 3 and 4). The only difference is a trend for ρ ( ̂ T ) corresponding to CT dynamics to have a 'heavy tail' for large values of ̂ T (see the replicate 4 in Fig. S1, SI Appendix ). Large values of ̂ T are correlated with large values of the time scale τ 0 (i.e., slower processes with high ̂ T ) and small values of the shape parameter k , that are ruled out by the RF model. This effect becomes more important for larger values of the lattice spacing, as indicated by the large values of 〈 T 〉 and σ T corresponding to method E (asterisks in Fig. 4).

- (3) The estimates from augmented-data MCMC (methodology F) are in general different from those obtained by other methods. Moreover, the p.d.f.'s ρ ( ̂ T ) obtained with MCMC show no systematic trend with respect to the other methods. With respect to, e.g., the ρ ( ̂ T ) obtained with MD, they can be located at slightly higher (replicates 5 and 6 in Fig. S1) or lower (replicates 2 and 3) values of ̂ T , or approximately at the same value (replicates 1 and 4). Moreover, the variation in the peak position of ρ ( ̂ T ) between different replicates is larger than for the other methods. This suggests that the MCMC method is more sensitive to fine details of the evolution of the epidemic. A possible explanation is that augmented-data MCMC involves the inference of the unobserved colonisation times and thus is intrinsically individual-based, in contrast to shell-based (or mean-field) methods, which try to match the colonisation times in an approximate manner only.

## 3.2 Comparison of fitted models with experimental data

In order to assess the quality of the assumptions used for estimation, we compare the fitted models with the available experimental data. For methods A-D, we compare the incidence and shell-evolution function obtained numerically (RF dynamics) with values for ̂ T and ̂ τ exp sampled from ρ 2 ( ̂ T, ̂ τ exp ) estimated by means of the spatio-temporal maps at maximum observation time t obs = 21 days with the actual incidence and shell-evolution function for each epidemic. Similarly, the fits from methods E and F are compared

with experimental observations by running numerical epidemics with parameters for the CT dynamics sampled from the p.d.f. ρ 3 ( ̂ T, τ 0 , k ). We make a quantitative comparison based on squared distances d 2 c and d 2 f (cf. Table 1) between simulated epidemics and experimental fungal invasions. More explicitly, we define the root mean square (rms) distances,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where ∆ t = 21 days is the time interval used for calculations of d 2 c or d 2 f . The quantity l max is the maximum chemical distance to the centre of the system of agar dots. Its value decreases with the lattice spacing and ranges from l max = 2 for a = 16 mm to l max = 8 for a = 8 mm [23]. From the definition of d 2 c given in Table 1, it is easy to see that ∆ c gives the typical deviation of the simulated incidence per unit host at a given time, c sim ( t ), from the observed incidence per host at the same time, c obs ( t ). Similarly, ∆ F gives the typical deviation of the simulated shell-evolution function, F sim , evaluated at any spatio-temporal coordinates ( l, t ) from the observed value at the same coordinates.

Fig. 5 shows the mean of the rms distances obtained by averaging over stochastic simulations and over replicates with given lattice spacing. The low values of the rms distances (∆ c /lessorsimilar 0 . 2 and ∆ F /lessorsimilar 0 . 3) indicate that the observed C ( t ) and F ( l, t ) are statistically well described by the fitted models. For any given method and lattice spacing, we obtained ∆ c &lt; ∆ F , which is expected because reproducing the spatio-temporal evolution represented by F ( l, t ) is more demanding than capturing the temporal evolution of the colonisation given by c ( t ). Both ∆ c and ∆ F tend to be larger for a around 10-12 mm which, as shown below, corresponds to cases that are close to the invasion threshold (i.e. where P inv decreases from 1 to 0 on increasing a , as shown by the continuous line in Fig. 2(a)). Variability between replicates of epidemics with given T is larger around the invasion threshold, which is associated with a critical phase transition and characterised by large fluctuations [13,21,23,26-28]. As a consequence, the quality of fits is lower in the vicinity of the invasion threshold and this leads to larger values of ∆ c and ∆ F .

Methodology C gives a good balance between performance and number of parameters involved. Methods C-E based on an approximate spatio-temporal description of epidemics given by F ( l, t ) result in more accurate predictions than methods A (squares in Fig. 5) and B (diamonds) that neglect spatial features of invasion. Moreover, the approximate methods C-E also perform better than even methodology F (triangles in Fig. 5) despite the fact that the latter aims for a more precise spatio-temporal description. A more qualitative and visual comparison of estimated and observed C ( t ) reveals similar differences between all the methodologies (see details in Sec. III of SI Appendix ).

## 3.3 Two applications for prediction methods

As a first application of the proposed methods, we have studied the predictive power of the estimates of the probability of invasion and the incidence by calculating ρ ( ̂ T ) from the early stages of the actual epidemic, i.e. for t obs &lt; 21 days. In particular, based on the estimated ρ ( ̂ T ) for t obs = 10 days, we have obtained estimates for the probability of invasion at time t = 21 days (squares and dashed line in Fig. 2(a)) and compared them with the probability P exp of invasion at t = 21 days obtained directly from the experimental data. The observed probability of invasion, P exp , is estimated by counting (for each a ) the fraction of replicates in which the fungus has reached the six outer edges of the experimental system by 21 days. The mean of ̂ P inv averaged over replicates with the same value of a (symbols in Fig. 2(a)) gives a reasonable estimate for the observed mean of P exp (solid curve in Fig. 2(a)) after t = 21 days for most of the methods. Overall, the best predictions for ̂ P inv are obtained with methodology C (solid

Figure 5. Comparison of fitted models with experimental data. Mean rms distances (a) ∆ c and (b) ∆ F between observed and simulated fungal invasions in populations of agar dots. The mean value of rms distances is obtained by averaging over 10 4 stochastic realisations of simulations and over 6 replicates for each lattice spacing, a . Simulations are based on fits to observations over t obs = 21 days. Different symbols correspond to different methodologies summarised in Table 1, as marked in the legend.

<!-- image -->

circles in Fig. 2(a)). As expected, ̂ P inv decreases with increasing a for all methodologies, illustrating the existence of the threshold for epidemics around a /similarequal 12 mm [23]. Similarly, the experimentally observed incidence and shell-evolution function are statistically well captured by the numerical extrapolation for their simulated counterparts up to time t = 21 days obtained from observations over times t obs &lt; 21 days. A visual illustration of the agreement between the observed and predicted incidence is given in Sec. III of Appendix SI . Fig. 6 shows the rms distances between the observed and predicted evolutions from day 11 to day 21. The time interval used to calculate ∆ c and ∆ F from Eqs. (2) and (3) is ∆ t = 11 days. The relative trends of ∆ c and ∆ F between methods and lattice spacings are similar to those reported in Fig. 5 for the comparison between observations and numerical simulations with t obs . The main difference is that the values of the rms distances corresponding to predictions of the evolution of colonisation (Fig. 6) are systematically larger than those obtained by simply comparing observed evolutions with their respective fittings (Fig. 5). This is in agreement with the intuitive idea that predicting the a priori unknown evolution of a system is more challenging than reproducing a fitted evolution.

As a second application of our methodology, we have calculated ̂ P inv at the end of the epidemic as a function of the lattice spacing in systems of size L = 51, i.e., larger than the experimental samples of sizes L = 2 , ..., 8 which decrease with increasing lattice spacing (see the two populations for different value of a shown in Fig. 2(a)). Such predictions are based on estimates for the transmissibility obtained from observations up to day t obs . As expected, ̂ P inv decreases with increasing a , illustrating the existence of the threshold for epidemics around a /similarequal 12 mm [23]. The results of applying each of the prediction methods are shown in Fig. 2(b) for the mean probability averaged over replicates for each value of a . All the methods except E give similar predictions for ̂ P inv . The large values of ̂ P inv predicted by method E are a consequence of the 'heavy tail' of the p.d.f. ρ ( ̂ T ) which gives a significant weigh to the high values of P inv for large ̂ T in Eq. (1). The dependence of ̂ P inv on a differs from the observed probability of invasion, P exp (continuous curve in Fig. 2(b)). The difference can be qualitatively understood by recalling that ̂ P inv gives an extrapolation both in space and time. Indeed, ̂ P inv ≥ P exp because some epidemics that are non-invasive after 21 days have a certain probability to invade a system of size L = 51 for

Figure 6. Comparison of the predicted and observed evolution of fungal invasion in the system of agar dots. Predictions of the fungal spread in the period of time between days 10 and 21 are made from observation of the initial spread during t obs = 10 days. The vertical axes show the mean over replicates of the rms distances (a) ∆ c and (b) ∆ F between observed and predicted fungal evolution during the time interval 11 -21 days. The mean value of rms distances is obtained by averaging over stochastic realisations of simulations and over 6 replicates for each lattice spacing, a . Simulations are based on fittings to observations over t obs = 10 days. Different symbols correspond to different methodologies summarised in Table 1, as marked in the legend.

<!-- image -->

t &gt; 21 days. In addition, both infectivity and susceptibility are expected to be subject to heterogeneity in the agar-dot system due to, e.g., inherent variability. Based on the results presented in Sec. 4 for numerical experiments with heterogeneity in transmission, we expect the estimated ̂ P inv to give an upper bound to the actual probability of invasion. This can also contribute to the difference between ̂ P inv and P exp for large values of a .

## 4 Numerical experiment

The quality of the predictions presented in the previous section is influenced by the quality of the observations in step (i), the suitability of the model chosen in step (ii) for description of the data, and the fitting procedure used in step (iii). In principle, the effect of these factors on predictions could be minimised by optimising the procedures used in each step for prediction. Stochasticity associated with the transmission of infection also influences the ability of making reliable predictions. In contrast to the previous factors, stochasticity is inherent to the nature of the system and its negative effect on predictions cannot be minimised without modifying the system. In this section, we present a sensitivity analysis of our methods by applying them to prediction of invasion for numerically-simulated epidemics where the main factor compromising predictability is the intrinsic stochasticity in transmission of infection. The advantage in this case with respect to more realistic situations is that both the transmissibility, T , and the probability of invasion, P inv ( T ; L ), are known and it is then possible to investigate the performance of the estimates for ρ ( T ) and P inv ( L ) by comparing with the known quantities.

̂ ̂ We first consider the simplest situation when the observed epidemics follow the RF dynamics with homogeneous transmission (i.e. T is the same for all pairs of nearest neighbours in the population). The idea is to run numerical experiments with known T , observe the evolution of the epidemic over an initial

Figure 7. Numerical experiments of SIR epidemics with homogeneous transmissibility. Hosts are placed on the nodes of a triangular lattice of size L = 51 (cf. Fig. 1(a)). The evolution of epidemics starting from the central host is observed over time t ≤ t obs = 7 τ . The line marked by circles shows the dependence of the conditional probability of invasion, P inv ( T ; L ), on transmissibility obtained by the simulations in the system of size L = 51. The shaded region shows the levels of confidence in percentage of the p.d.f ρ ( ̂ T ) around the most probable transmissibility, ̂ T /star (continuous black line) corresponding to each value of ̂ P inv ( L ). The horizontal dashed line illustrates the case of estimations giving ̂ P inv ( L ) = 0 . 2. If the observed epidemic has a value of the transmissibility such as ̂ T l that is to the left of the curve for P inv (line with circles), the estimated ̂ P inv ( L ) overestimates P inv . In contrast, for values of the transmissibility that are to the right of the curve for P inv (e.g. ̂ T h ), the probability ̂ P inv ( L ) underestimates P inv .

<!-- image -->

For concreteness, we consider the arrangement shown in Fig.1(a) and use methodology C for steps (i)-(iii). RF epidemics are observed during t obs = 7 τ with the aim of estimating the probability that they will invade a system of size L = 51. Note that over the time interval t ≤ t obs = 7 the epidemic at most invades a hexagon of size L = 15. Then, the behaviour of the epidemic is extrapolated both in space and time. We proceed by, first, calculating the p.d.f. ρ ( ̂ T ) for the estimated transmissibilities ̂ T compatible with observation (spatio-temporal map). Fig. 1(c) shows an example of ρ ( ̂ T ) obtained from the analysis of the evolution of an epidemic with T = 0 . 4. In general, the most probable estimate for the transmissibility, ̂ T ∗ , corresponding to the maximum of ρ ( ̂ T ) for a single epidemic, differs from T but not significantly. In many cases, T lies within the 68% confidence interval for ρ ( ̂ T ) around its maximum (see a more detailed discussion in SI Appendix ). The distribution ρ ( ̂ T ) allows the probability of invasion ̂ P inv ( L ) in the system of size L = 51 to be estimated using Eq. (1). We have applied this prediction method to many ( ∼ 10 4 ) spatio-temporal maps created with known transmissibility T spanning the interval [0 , 1]. For each value of estimated ̂ P inv ( L ), the distribution ρ ( ̂ T ) is represented by a horizontal slice of the shaded area in Fig. 7 (see e.g. the slice along the dashed blue line corresponding to ̂ P inv ( L ) = 0 . 2 with darker colour corresponding to higher probability relative to the maximum of ρ ( ̂ T )). The black ridge in the shaded area corresponds to the most probable transmissibility, ̂ T /star , for each value of ̂ P inv ( L ).

interval of time, t obs , and then apply the methods described above to calculate ̂ P inv ( L ) assuming that T is unknown (as it occurs for real epidemics).

To test the quality of the predictions, the estimate of the probability of invasion P inv ( ̂ T ; L ) is compared

with the probability P inv ( T ; L ) that would be obtained if the exact value of T was known a priori (see line marked by circles in Fig. 7). Making such a comparison we can see that for epidemics with low transmissibility where invasion is possible but not highly probable, ̂ P inv ( L ) overestimates P inv ( T ; L ) for most of the possible values of ̂ T contributing to ̂ P inv ( L ) (the shaded area including the ridge region corresponding to the typical values of ̂ T is mainly above the line marked by circles in Fig. 7). This means that the estimations are biased upwards and the most likely is that the actual probability of invasion will be smaller than predicted. In other words, such predictions will typically give a safe bound for the probability of invasion. Obviously, there is a non-zero probability that the observed epidemic has a large value of the transmissibility (such as ̂ T h in Fig. 7). In this case, ̂ P inv ( L ) would underestimate the actual probability P inv . For more invasive epidemics (i.e. epidemics with P inv /greaterorsimilar 0 . 5), the shaded area is mainly below the line marked by the circles in Fig. 7 meaning that the predicted probability of invasion ̂ P inv underestimates P inv for most of the possible values for ̂ T , including the most probable, ̂ T /star . In these situations however, both ̂ P inv and P inv are large and the predictions allow for a reasonable assessment for invasion to be done. In Sec. VI of SI Appendix we show mathematically that differences between ̂ P inv ( L ) and P inv evaluated at the most probable transmissibility ̂ T /star are mainly dictated by the curvature of P inv around ̂ T /star and is intrinsically linked to the non-zero width of the p.d.f. ρ ( ̂ T ). This general result implies that the biases in the probability of invasion at low and high transmissibility are independent of the fitting method (Table 1) because all methods lead to a p.d.f. ρ ( T ) with non-zero width.

̂ The results presented above correspond to RF epidemics with homogeneous transmission. A similar approach has been used to deal with more realistic epidemics where the transmission of infection is heterogeneous due to variability in the infectivity and the susceptibility of hosts. As already mentioned in the previous section, the estimated ̂ P inv ( L ) for such epidemics usually gives a bound to the actual probability of invasion that is even safer than that obtained for cases with homogeneous transmissibility (see SI Appendix for more detail).

## 5 Discussion

The methodology introduced here focuses on the prediction of relatively simple but important features of epidemics. This is in contrast to much previous work dealing with the prediction of quantitative properties of epidemics such as the detailed spatio-temporal evolution of the incidence. The advantage in dealing with simple characteristics of epidemics is that they can be more easily predicted in terms of simplified description of the spatio-temporal evolution. Our results demonstrate that, under quite general assumptions, it is possible to give reliable prediction of the final state of an epidemic with permanent immunisation from the early stage of its evolution. Such a prediction is possible even for a single realisation of an epidemic and thus the framework is relevant to inherently unique real-world epidemics. In fact, our approach can be applied for prediction of epidemics in real systems characterised by a wide range of space and time scales (e.g. crops) based on micro- or meso-cosm experiments of finite size and over finite time.

The results obtained for experimental fungal invasion by using approximate methods (C-E in Table 1) are more robust than those based on supposedly more precise methodology F. This might be a consequence of the interplay between the high fitting precision for MCMC methods involving data augmentation with a poor description of the actual dynamics given by the continuous-time model fitted to the observations. A model capturing dynamical details at a level consistent with that offered by the fitting procedure might exhibit more predictive power than that presented here. This is an illustration of the importance of keeping all the steps involved in prediction at a similar level of complexity in order to give reliable predictions. For practical applications, the particular method to be used for obtaining the most reliable prediction depends on the problem in hand. The general rule that seems to emerge from our analysis is that a reasonable method should use as much informations as available from observations, and avoid

inferring data that is not directly available unless this is strictly required by the problem. This is the case for methods C-E in our particular study of fungal colony invasion in the population of agar-dots. Methods A and B use less information than available from observations (i.e. they use C ( t ) instead of F ( l, t )) while method F infers information that is not available from observations.

The proposed methods assume that epidemics can be approximately described by an effective transmissibility that is constant over time and homogeneous in space. However, their applicability goes beyond epidemics with constant transmissibility. In particular, we have shown that the method gives reliable predictions in the presence of spatial heterogeneity in the transmission of infection. We expect that the methododology can also be successfully applied to cases where the transmissibility changes over time but it remains within the bounds for the effective transmissibility estimated from the early stage.

We have characterised the final state of epidemics by the probability of invasion. This quantity is suitable for systems with well-defined boundaries such as, e.g. the population of agar-dots analysed above. In cases where hosts are placed on the nodes of more complex networks, the boundaries of the system are not necessarily well-defined [33] and it is more convenient to characterise the final state of epidemics in terms of the mean number of removed (i.e. ever infected) hosts, N R . Our approach also applies to such complex networks. The formula given by Eq. (1) provides an estimated size, ̂ N R ( L ), if P inv ( ̂ T ; L ) is replaced by the function N R ( T ; L ) giving the size of SIR epidemics with given transmissibility, T .

̂ ̂ Our methods have been applied under the assumption that the network of contacts between hosts remains unchanged during the course of epidemics. Such an approximation has been widely used in the past [33] and it is reasonable for cases in which the rate of change of the configuration of contacts is much smaller than the removal rate of hosts (i.e. ∼ τ -1 in our notation). This condition is clearly satisfied for the fungal colony invasion of the population of agar-dots considered here and also for many other epidemics associated with pathogens spreading in, e.g., networks of plants [22], farms [9], or airports [11]. This paradigm is also applicable to the spread of many infections in human populations (for instance, measles or SARS that have recovery periods of the order of few days). In contrast, the dynamics of contacts between humans plays an important role for other infectious diseases such as syphilis with a recovery period of 100 days [34]. A possible strategy to make predictions in this kind of networks would involve inferring the mixing parameter for contacts (as defined, for instance, in [34]) based on observations (step (i)) in a similar way as we estimated the parameters of the SIR model in step (iii).

Another interesting task would be to extend the ideas presented here to deal with epidemics with persistence where immunity after recovery is not permanent (i.e. recovered hosts can be re-infected). In this case, the simplest model for description of observations is the SIS model (susceptible-infectedsusceptible) [35] and a possible quantity to be predicted would be the stationary prevalence of infection (i.e. the density of infected hosts in the stationary state reached after a transient [35]).

Due to stochasticity in transmission of infection, it is not possible to determine the parameters of a model describing an epidemic with absolute certainty even if the epidemic is observed during a long time t obs before attempting inference. Furthermore, if it were possible to determine the exact value of the parameters, it would still be impossible to make arbitrarily precise predictions of the evolution of the epidemic in the future or predict with absolute certainty if the epidemic is going to be invasive or not (instead, one has to deal with the probability of invasion). The uncertainty in the prediction of the evolution of epidemics grows monotonically with the look-ahead time (see, e.g. the forecast of the incidence in Sec. IV of SI Appendix ). There exists a prediction horizon beyond which the uncertainty of predictions of the evolution of the epidemic is too large for predictions to be useful. The location of the horizon is epidemic-dependent and also depends on how precise we want our predictions to be. In contrast, for a pure SIR epidemic, there is no prediction horizon for quantities such as P inv or N R that only depend on the transmissibility. In other words, different replicates of epidemics with given T will follow different evolutions that have a prediction horizon but will lead to the same P inv or N R [26,30,31]. More complex nonlinear dynamics for transmission associated with, for instance, a seasonal component in the transmission rate may lead to chaotic behaviour [36]. Predictability of catastrophic events in systems

exhibiting chaotic behaviour is a non-trivial question that has been widely studied in the past [37] and still receives considerable attention at present [38]. Even in the absence of stochasticity, the prediction horizon in these systems is intrinsically limited due to the high sensitivity of chaotic processes to the initial conditions and the values of the parameters. In addition, the accuracy of predictions does not necessarily increase monotonically with the observation time, t obs , before prediction [39]. In such situation, it would be necessary to estimate the value of t obs leading to the most reliable prediction. Due to all these factors, the methods proposed in this paper may not work when applied for prediction of catastrophic events in nonlinear dynamical systems. However, the ideas presented here together with approaches proposed for prediction in nonlinear dynamical systems may help in devising strategies for prediction in stochastic non-linear systems.

## Acknowledgements

The authors acknowledge helpful discussions with G.J. Gibson and funding from BBSRC (Grant No. BB/E017312/1). CAG acknowledges support of a BBSRC Professorial Fellowship.

## References

1. Sornette D (2000) Critical Phenomena in Natural Sciences , Springer Series in Synergetics (Springer Verlag, Berlin).
2. Sornette D (2002) Predictability of catastrophic events: Material rupture, earthquakes, turbulence, financial crashes, and human birth. Proc Natl Acad Sci USA 99:2522 - 2529.
3. Sornette D (2003) Why Stock Markets Crash (Princeton University Press, Princeton).
4. Medley GF (2001) EPIDEMIOLOGY: Predicting the Unpredictable. Science 294:1663-1664.
5. Valleron AJ, Boelle PY, Will R, Cesbron JY (2001) Estimation of Epidemic Size and Incubation Time Based on Age Characteristics of vCJD in the United Kingdom. Science 294:1726-1728.
6. d'Aignaux JNH, Cousens SN, Smith PG (2001) Predictability of the UK Variant Creutzfeldt-Jakob Disease Epidemic. Science 294:1729-1731.
7. Morton A, Finkenstdt BF (2005) Discrete time modelling of disease incidence time series by using markov chain monte carlo methods. J. R. Stat. Soc. C 54:575-594.
8. Kleczkowski A, Gilligan C (2007) Parameter estimation and prediction for the course of a single epidemic outbreak of a plant disease. J. Roy. Soc. Interface 4:865-877.
9. Keeling MJ, et al. (2001) Dynamics of the 2001 UK Foot and Mouth Epidemic: Stochastic Dispersal in a Heterogeneous Landscape. Science 294:813-817.
10. Ferguson NM, Donnelly CA, Anderson RM (2001) The Foot-and-Mouth Epidemic in Great Britain: Pattern of Spread and Impact of Interventions. Science 292:1155-1160.
11. Hufnagel L, Brockmann D, Geisel T (2004) Forecast and control of epidemics in a globalized world. Proc Natl Acad Sci USA 101:15124-15129.
12. Riley S (2007) Large-Scale Spatial-Transmission Models of Infectious Disease. Science 316:12981301.

13. P´ erez-Reche FJ, Taraskin SN, Costa LdF, Neri FM, Gilligan CA (2010) Complexity and anisotropy in host morphology make populations less susceptible to epidemic outbreaks. J. Roy. Soc. Interface 7:1083-1092.
14. Truscott JE, Gilligan CA (2003) Response of a deterministic epidemiological system to a stochastically varying environment. Proc. Natl. Acad. Sci. USA 100:9067-9072.
15. Dye C, Gay N (2003) EPIDEMIOLOGY: Modeling the SARS Epidemic. Science 300:1884-1885.
16. May RM (2004) Uses and Abuses of Mathematics in Biology. Science 303:790-793.
17. Pearce N, Merletti F (2006) Complexity, simplicity, and epidemiology. Int. J. Epidemiol. 35:515519.
18. Goldenfeld N, Kadanoff LP (1999) Simple lessons from complexity. Science 284:87 - 89.
19. Anderson RM, May RM (1991) Infectious diseases of humans: dynamics and control (Oxford University Press, Oxford).
20. Murray JD (2002) Mathematical Biology. I. An Introduction (Springer), 3rd edition.
21. Davis S, Trapman P, Leirs H, Begon M, Heesterbeek J (2008) The abundance threshold for plague as a critical percolation phenomenon. Nature 454:634-637.
22. Otten W, Filipe JAN, Bailey DJ, Gilligan CA (2003) Quantification and analysis of transmission rates for soilborne epidemics. Ecology 84:3232 - 3239.
23. Bailey DJ, Otten W, Gilligan CA (2000) Saprotrophic invasion by the soil-borne fungal plant pathogen rhizoctonia solani and percolation thresholds. New Phytol. 146:535 - 544.
24. Gibson GJ, Kleczkowski A, Gilligan CA (2004) Bayesian analysis of botanical epidemics using stochastic compartmental models. Proc. Natl. Acad. Sci. USA 101:12120-12124.
25. Gibson GJ, et al. (2006) Bayesian estimation for percolation models of disease spread in plant populations. Stat Comput 16:391 - 402.
26. Grassberger P (1983) On the critical behavior of the general epidemic process and dynamical percolation. Math. Biosc. 63:157-172.
27. Otten W, Bailey DJ, Gilligan CA (2004) Empirical evidence of spatial thresholds to control invasion of fungal parasites and saprothophs. New Phytol. 163:125 - 132.
28. Neri F, et al. (2011) The effect of heterogeneity on invasion in spatial epidemics: from theory to experimental evidence in a model system. PLoS Comput. Biol. 7:e1002174.
29. Daley DJ, Gani J (1999) Epidemic modelling (Cambridge University Press, Cambridge).
30. Ludwig D (1975) Final size distribution for epidemics. Math. Biosc. 23:33 - 46.
31. Pellis L, Ferguson NM, Fraser C (2008) The relationship between real-time and discrete-generation models of epidemic spread. Math. Biosc. 216:63 - 70.
32. Marjoram P, Molitor J, Plagnol V, Tavar´ e S (2003) Markov chain Monte Carlo without likelihoods. Proc. Natl. Acad. Sci. USA 100:15324 - 15328.
33. Barrat A, Barth´ elemy M, Vespignani A (2008) Dynamical Processes on Complex Networks (Cambridge University Press, Cambridge).

34. Volz E, Meyers LA (2007) Susceptible-infected-recovered epidemics in dynamic contact networks. Proceedings of the Royal Society B: Biological Sciences 274:2925-2934.
35. Marro J, Dickman R (1999) Nonequilibrium Phase Transitions in Lattice Models (Cambridge University Press, Cambridge).
36. Olsen L, Schaffer W (1990) Chaos versus noisy periodicity: alternative hypotheses for childhood epidemics. Science 249:499-504.
37. Abarbanel HDI, Brown R, Sidorowich JJ, Tsimring LS (1993) The analysis of observed chaotic data in physical systems. Rev. Mod. Phys. 65:1331-1392.
38. Wang WX, Yang R, Lai YC, Kovanis V, Grebogi C (2011) Predicting catastrophes in nonlinear dynamical systems by compressive sensing. Phys. Rev. Lett. 106:154101.
39. Van Dyke Parunak H, Belding T, Brueckner S (2008) in Engineering Environment-Mediated MultiAgent Systems , Lecture Notes in Computer Science, eds Weyns D, Brueckner S, Demazeau Y (Springer Berlin / Heidelberg) Vol. 5049, pp 88-102.

## Prediction of invasion from the early stage of an epidemic. Supplementary methods and results

1 , 2 3 4

Francisco J. P´ erez-Reche , Franco M. Neri , Sergei N. Taraskin , and Christopher A. Gilligan 3

1 SIMBIOS Centre, University of Abertay Dundee, Dundee, UK

2 Department of Chemistry, University of Cambridge, Cambridge, UK

3 Department of Plant Sciences, University of Cambridge, Cambridge, UK

4 St. Catharine's College and Department of Chemistry, University of Cambridge, Cambridge, UK

## CONTENTS

Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): II. Methods for fitting models to data in step (iii), 2: 2.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): A. Minimum distance (MD) method, 2: 4.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): B. Approximate Bayesian Computation (ABC), 2: 5.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): C. Markov Chain Monte-Carlo (MCMC) method with data augmentation, 2: 7.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): D. Distribution for the estimated transmissibility, ρ ( ˆ T ), 2: 9.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): III. Additional comparisons of fitted models with experimental data, 2: 11.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): IV. Forecast of the incidence, 2: 12.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): V. Additional results for the numerical experiments, 2: 14.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): A. Homogeneous transmission of infection, 2: 14.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): B. Heterogeneous transmission of infection, 2: 17.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): VI. Differences between P inv and ˆ P inv, 2: 20.
Según Prediction of invasion from the early stage of an epidemic (2012), I. Continuous-time epidemiological model for step (ii): References, 2: 20.
## I. CONTINUOUS-TIME EPIDEMIOLOGICAL MODEL FOR STEP (II)

In this section, we present the three-parameter continuous-time (CT) model used in methods E and F (Table 1, main text) to address step (ii) for prediction. In principle, this model is more realistic than the Reed-Frost (RF) model used in methods A-D and allows the existence of possible effects caused by the discrete-time character of the RF description to be explored. We use the fungal invasion experiment as a benchmark for the comparison between different models. In the CT, the spread (transmission) of the fungal colony between two neighbouring dots is treated as a time-inhomogeneous Poisson process [1]. The waiting time distribution f ( t ) for each transmission event can be modelled by a Weibull distribution multiplied by the transmissibility T :

<!-- formula-not-decoded -->

where τ 0 is the characteristic time scale of the process, and k is a shape parameter of the distribution. Given the cumulative probability function P ( t ) = ∫ t u =0 f ( u )d u , the survival function S ( t ) (giving the probability that transmission did not occur by time t ) obeys the following relation:

<!-- formula-not-decoded -->

The rate of the transmission process, φ ( t ), is a function of the time since colonisation of the donor dot and is given by the expression:

<!-- formula-not-decoded -->

In the limit k →∞ , the CT model reduces to the RF model, with the same value of T and infectious period τ = τ 0 . Indeed, for k →∞ , the survival probability given by Eq. (S.2) becomes a step function,

<!-- formula-not-decoded -->

which corresponds to a RF model, in which infection can be transmitted from an infected host to a susceptible neighbour with probability T only once the infectious period τ 0 has passed.

## II. METHODS FOR FITTING MODELS TO DATA IN STEP (III)

The aim of this section is to give a detailed description of the different methods used for fitting models M to data D described in step (iii) of the methods for prediction proposed in the main text. The ideas presented in the main text can be framed within a Bayesian approach which assumes that

the parameters θ describing M are random variables. The aim of step (iii) is to evaluate π ( θ |D ), the probability density that M with parameters θ describes the data. According to Bayes' rule:

<!-- formula-not-decoded -->

 Several challenges arise when using this Bayesian approach in the analysis of epidemic spread. The first difficulty is associated with inherent limitations in the observations. A complete spatio-temporal data set would contain the precise time of colonisation t j of each host j in the population, i.e. D = { t j } . Unfortunately, it is often the case that observations do not provide such detailed information. In the particular experimental data set considered in the main text, the status of each dot is only recorded at discrete (1-day) time intervals. Hence, the actual dataset is D = { d j } , where d j is the day when dot j was first observed as colonised. We have explored two possible ways to deal with the lack of precise information. The option used in methods A-E (Table 1, main text) involves identifying descriptors for the evolution of the epidemic that are suitable for the prediction of the catastrophic event. The lowerdimensional descriptors used in this work are the cumulative incidence, C ( t ), and the shell-evolution function, F ( l, t ). Another option is to use data augmentation [2] that treats the unobserved colonisation times as parameters to be estimated. This is the procedure followed in method F.

 where π ( θ ) is the prior distribution of the parameters, reflecting our initial belief in their values, and ( D| θ ) is the likelihood (the probability of the data given the parameters).

Another source of difficulties is due to the fact that the analytical calculation of the posterior π ( θ |D ) is, in general, impossible [3]. Therefore, it is common to resort to numerical methods to sample from π ( θ |D ). In order to do this, we propose a new approximate method (denoted as MD), which is based on the calculation of the minimal distance between two datasets and does not require knowledge of the likelihood ( D| θ ). In addition, we have used two known methods:

-  · a method belonging to the class of Approximate Bayesian Computation (ABC) [4], which calculates an approximate posterior, and which shares several basic features with the MD method.
- Markov-chain Monte Carlo (MCMC) with data augmentation [2, 5], which relies on the exact analytical form of ( D| θ ) to sample from the exact posterior π ( θ |D ).

 The ABC method was used with multiple purposes:

- (a) to test the new MD method (involving the minimisation of a given distance between observed and simulated data) against an already-known method (ABC, which involves a cutoff on the same distance).

- (b) to test different choices in step (ii), by comparing estimations obtained using the RF model with estimations obtained by means of the CT model.

The MCMC method was employed to test the new MD method against a widely-used technique that uses both a different level of description (site-level vs. shell or MF level) and a different model M (CT dynamics instead of RF dynamics).

## A. Minimum distance (MD) method

Let D obs be the observed data, θ a set of candidate parameters, and D sim a simulated dataset generated using θ . Then, if D obs = D sim , the vector of parameters, θ , is drawn from π ( θ |D obs ). In practice, obtaining an exact match between observed and simulated dataset is often computationally unfeasible, and one has to resort to an approximate match. To this end, we define a metric d 2 ( D 1 , D 2 ) that measures the distance between two datasets D 1 and D 2 . The aim of the MD method is to calculate the distribution of parameters θ that minimise d 2 ( D 1 , D 2 ) and gives an approximate posterior. The choice of the metric d 2 ( D sim , D obs ) is problem-specific and, in general, not unique. We have tested two different metrics, corresponding to different descriptors of the data (cf. step (i) of the main text):

1. For the shell-based description, we used d 2 f = ∑ l, t ( F sim ( l, t ) -F obs ( l, t )) 2 , where l enumerates the shells, t is the discretised time (observation times in days), and F is the shell-evolution function.
2. Another option is to ignore any spatial information from the data (mean-field (MF) description) and consider only the total fraction of colonised sites at time t , c ( t ) = C ( t ) /N . In this case, we chose the distance function d 2 c = ∑ t ( c sim ( t ) -c obs ( t )) 2 , where t is again the discretised time.

The algorithm to implement the MD method considers two indexes, n , counting the parameter vectors resulting from the minimisation procedure, and r , counting the iterations. The values of n and r are in the range n, r ∈ N with maximum values n max and R , respectively, and proceeds as follows:

- MD.1 Set n = 0
- MD.2 Set r = 0
- MD.3 Chose a value θ ( r ) n for the parameter vector sampled from the prior π ( θ ).
- MD.4 Generate a data set D ( r ) sim from the model M with parameters θ ( r ) n .

MD.5 Calculate d 2 ( D obs , D ( r ) sim ) and

-If r &lt; R , set r = r +1 and return to MD.3 or

-If r = R , go to MD.6

- MD.6 Among all the parameters { θ ( r ) n ; r = 0 , 1 , . . . , R } , chose the set of parameters θ n ∈ { θ ( r ) n } giving the closest simulated data, D sim to observations, i.e. d 2 ( D obs , D sim ) = min r =0 ,...,R { d 2 ( D obs , D ( r ) sim ) } .

MD.7 Set n = n +1 and return to MD.2 until n = n max .

The result of this algorithm is a set of parameter vectors { θ n ; n = 0 , 1 , . . . , n max } that give simulated data with minimum distance to observations. The normalised histogram for the obtained parameter vectors { θ n } defines a p.d.f. ρ ( θ ) that approximates the posterior π ( θ |D ).

For all the results presented in the paper and obtained with the MD algorithm, we set R = 5000. For some fungal epidemics, we have checked that larger values of R do not lead to smaller values of d 2 ( D obs , D sim ) in step [MD.6].

## B. Approximate Bayesian Computation (ABC)

In common with the MD method, the ABC approximate Bayesian method we have used also relies on the definition of a metric, d 2 . If the distance between observed and simulated datasets is less than a given tolerance parameter, /epsilon1 , i.e. d 2 ( D obs , D sim ) ≤ /epsilon1 , then θ is drawn from the approximate posterior π ( θ | d 2 ( D obs , D sim ) ≤ /epsilon1 ) . The accuracy of the approximation increases as /epsilon1 → 0.

For our estimations, we used a Markov-chain Monte Carlo algorithm that can be summarised as follows:

ABC.1 Set n = 0 and choose the initial value θ 0 of the parameter vector.

ABC.2 Generate a candidate vector, θ ′ , from a proposal distribution q ( θ ′ | θ n ).

ABC.3 Generate a data set D sim from the model M with parameters θ ′ .

ABC.4 Calculate d 2 ( D obs , D sim ) and

-if d ( D , D ) &gt; /epsilon1 , set θ = θ and go to ABC.7.

<!-- formula-not-decoded -->

TABLE I. Values of /epsilon1 used for methods B, D, and E (Table 1, main text) using the ABC inference method in step (iii) for prediction.

Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 1, D: 0 . 03, B: 1 . 5, E: 0 . 5.
Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 2, D: 0 . 03, B: 1 . 5, E: 0 . 7.
Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 3, D: 0 . 03, B: 1 . 5, E: 1 . 5.
Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 4, D: 0 . 03, B: 1 . 5, E: 0 . 5.
Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 5, D: 0 . 03, B: 1 . 5, E: 1.
Según Prediction of invasion from the early stage of an epidemic (2012), Rep.: 6, D: 0 . 03, B: 1 . 5, E: 1.
ABC.5 Calculate the probability of acceptance:

<!-- formula-not-decoded -->

ABC.6 Set θ n +1 = θ ′ with probability p acc , or θ n +1 = θ n with probability 1 -p acc .

ABC.7 Set n = n +1 and return to ABC.2 until the chain has converged and the required number of samples has been collected.

In our estimations, either a uniform distribution with the same support as the prior (see below) or normal distribution, N (0 , σ 2 ) were used for the proposal distribution q ( . ) (cf. steps ABC.2 and ABC.5). The criterion for the choice between these two distributions was to minimize the average number of simulations needed to generate a dataset with d 2 ( D obs , D sim ) ≤ /epsilon1 in step [ABC.4]. The value of σ for the normal distribution was chosen according to the same criterion, and was typically a fraction between 0 . 05 and 0 . 1 of the support of the prior distribution.

Every chain was run for 5 × 10 4 steps, discarding an initial burn-in period of 5 × 10 3 steps. Since very small values of the tolerance /epsilon1 imply very low acceptance rates, the final choice of /epsilon1 was the result of a tradeoff between the accuracy of the approximation and CPU time available. The values of /epsilon1 that were finally used in our analyses are shown in Table SI.

For both MD and ABC approaches, we assumed independent priors for all the parameters: π ( θ ) = π ( T ) π ( τ exp ) (RF model) and π ( θ ) = π ( T ) π ( τ 0 ) π ( k ) (CT model). For the RF model, all the priors were uniform: π ( T ) = U (0 , 1) and π ( τ exp ) = U ( τ min , τ max ), where τ min = 1d and τ max was changed between treatments (increasing with the lattice spacing, from τ max = 6d for the lattice with a = 8mm spacing to τ max = 12d for the lattice with a = 16mm spacing). For the CT model, we used two sets of priors: (i) noninformative uniform priors for all the parameters ( π ( T ) = U (0 , 1), π ( τ 0 ) = U (0 , 20),

π ( k ) = U (0 , 20)) and (ii) noninformative prior for the transmissibility ( π ( T ) = U (0 , 1)) and exponential priors for the other two parameters ( π ( τ 0 ) = Exp(1), π ( k ) = Exp(1) as for the augmented-data MCMC estimations). Only results for noninformative priors from set (i) are presented below, and compared with results from the RF model. The different choice for the priors from set (ii) has an effect on the posterior distributions, but does not affect significantly the predicted incidence curves (see Section 3) and, for the sake of brevity, results from set (ii) are not presented.

The ABC and MD methods share several common features. Both of them rely on the simulation of epidemics using the current parameters, and on the calculation of a distance between simulated epidemics and the observed data. However, the ABC method considers any distance below the cutoff /epsilon1 , while the MD method seeks to minimise the distance over a given number of simulations R . The iterative procedure used in MD method allows the use of an additional parameter analogous to /epsilon1 in ABC method to be avoided. In both cases, the exact posterior is recovered in the proper limit ( /epsilon1 → 0 and R →∞ , respectively).

## C. Markov Chain Monte-Carlo (MCMC) method with data augmentation

In order to implement the data-augmented MCMC method, it is necessary to calculate the explicit form of the likelihood  ( D| θ ) (with θ = ( T, τ 0 , k )). We sketch here the main steps of the calculation. Let I be the set of the dots that are colonised before the end of the experiment (at time t end = 21 days), and U be the set of those that are still uncolonised at t = t end . Assume first that we know the times of colonisation t j of each dot j ∈ I . The data then consist of the vector t of colonisation times, plus the set of uncolonised dots, i.e. D = ( t , U ). The nearest neighbours of dot j form the set N j , and the potential donors of j form the subset S j ⊆ N j . If j ∈ U , then S j contains the colonised neighbouring dots, i.e. S j = { i : i ∈ N j ∩ I} . If in contrast j ∈ I , S j contains the neighbouring dots that are colonised before j , i.e. S j = { i : i ∈ N j ∩I , t i &lt; t j , } .

Given these definitions, the likelihood function can be written as the product of the contributions from individual dots j :

<!-- formula-not-decoded -->

where f I j ( t j ), is the p.d.f. for the colonisation times t j , and P U j ( t end ) is the probability for dot j to be uncolonised by the end of the experiment. These contributions can be calculated explicitly as follows. The probability that a dot j ∈ I has not been colonised by a given neighbour i ∈ S j by time t j is given by the survival function S ( t j -t i ) (see Eq. (S.2)). Hence, the probability P I j ( t j ) that dot j is still

uncolonised at time t j is given by the product over all i ∈ S j :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where we used the relation S ( t ) = exp( -∫ t 0 φ ( u )d u ). The p.d.f. for t j is then given by:

Likewise, a dot j ∈ U is still uncolonised by time t end when transmission did not occur from any of its neighbours i ∈ S j , yielding the probability:

/negationslash

In general, we are interested in obtaining the marginal distribution of a single parameter (in particular, T ) from Eq. (S.3), and thus all other parameters entering the expression for  ( D| θ ) have to be integrated out. This is, in general, unfeasible analytically. In the fungal invasion experiment, the calculation is further complicated by censoring , i.e., by the fact that experimental observations are made at discrete (1-day) time intervals. As a consequence, if d j is the day when dot j was first recorded as colonised, then the colonisation time t j is constrained to lie in the interval t j ∈ ( d j -1 , d j ), but its exact value is unknown. The actual dataset is hence D = ( d , U ), and the likelihood has to be calculated from Eqs. (S.4-S.7) by integrating out the unobserved colonisation times,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the integral is performed over the (high-dimensional and, in general, very complex) space T ( d ) compatible with the observed data.

Since the high-dimensional integrals introduced above are analytically intractable, numerical techniques are commonly used to sample values from the posterior distribution π ( θ |D ). The MCMC method consists in implementing a Markov chain for θ that has π ( θ |D ) as stationary distribution. A large literature exists on this subject (see e.g. Ref. [5]), to which the reader is referred for details. In our case, a Metropolis-Hastings algorithm has been used to build the Markov chain.

The algorithm can be summarised as follows:

MCMC.1 Set n = 0 and choose the initial value θ 0 of the parameter vector.

MCMC.2 Generate a candidate value of the vector θ ′ from a proposal distribution q ( θ ′ | θ n ).

MCMC.3 Calculate the probability of acceptance:

 MCMC.4 Set θ n +1 = θ ′ with probability p acc , or θ n +1 = θ n with probability 1 -p acc .

<!-- formula-not-decoded -->

MCMC.5 Set n = n +1 and return to MCMC.2 until the chain has converged and the required number of samples has been collected.

In order to deal with the unobserved colonisation times t , we used data augmentation [2]. Their values were treated as parameters to estimate, i.e. the original parameter vector θ was expanded (augmented) to ( θ , t ).

New colonisation times were then proposed and accepted/rejected within the same MetropolisHastings algorithm. Additional care had to be taken in this case, since at each step a pathway of transmission must exist between the dot inoculated at time t = 0 and all the other colonised dots in the system (see the discussion in [2] and [6]).

Independent priors were used for all the parameters, so that π ( θ ) = π ( T ) π ( τ 0 ) π ( k ). Anoninformative uniform prior was used for the transmissibility, i.e. π ( T ) = U (0 , 1). For the other two parameters, exponentially distributed priors were used, i.e. π ( τ 0 ) = Exp(1), π ( k ) = Exp(1). Such choice was made in order to exploit our prior knowledge, i.e., respectively, that the typical time scale of the fungal spread in our system is of the order of days, and that the waiting-time distribution is not step-like (i.e., k is not too large; note that such assumption is opposite to that of the RF model). We checked that the posterior distribution was not too sensitive to changes up to a factor 2 in the parameters of the exponential priors. A uniform prior was used for each augmented colonisation time.

Every chain was run for 10 5 MCMC steps discarding an initial burn-in period of 10 3 steps. We checked that the final posterior distribution was robust with respect to the choice of the inital point θ 0 .

## D. Distribution for the estimated transmissibility, ρ ( ˆ T )

This section complements the results presented in the main text (Figs. 2 and 3) for the p.d.f. ρ ( ˆ T ) obtained with different methods for parameter estimation in the fungal invasion experiment. Within the Bayesian framework, the analogous of the distribution ρ ( ˆ T ) introduced in the main text for the MD method is the marginal p.d.f of the posterior π ( θ |D ) integrated over the variable τ exp for the RF model and over the variables τ 0 and k for the CT model.

Fig. S1 shows the comparison of the probability density functions ρ ( ˆ T ) obtained for the agar dot experiment by all the methods summarised in Table 1 of the main text. The posteriors are shown for

Fig. S1. Comparison of marginal posterior distributions ρ ( ˆ T ) obtained with methods listed in Table 1 of the main text. Different symbols and lines correspond to different methods, as indicated by the legend. All the replicates correspond to invasion in populations with lattice spacing a = 10 mm.

<!-- image -->

experiments in populations with lattice spacing a = 10mm. This particular set of results was chosen because it summarised well all the main effects of the methodologies used. All the estimations correspond to observations over the complete duration of the experiment, i.e. t ≤ t obs = 21 days.

## III. ADDITIONAL COMPARISONS OF FITTED MODELS WITH EXPERIMENTAL DATA

In the main text, we presented a test of the goodness of fit of models to data based on the mean squared distances d 2 c and d 2 f . The purpose of this section is to give a more visual comparison between fitted models and observations based on the cumulative incidence.

For every model used, we obtain the statistics for the incidence corresponding to fitted models by sampling the parameters θ from the joint (exact or approximate) posterior, π ( θ |D ). This procedure gives a p.d.f. ρ ( C | t ) for the incidence C at any given time t . The dispersion of ρ ( C | t ) is associated both with the stochasticity in the simulated model for each value of the parameters, θ , and the dispersion for the values of these parameters given by π ( θ |D ). Strictly speaking, the comparison of the experimental incidence with that obtained by methods A-D based on the RF model makes sense only when the stochastic nature of the process is taken into account. Indeed, the fine details of the two types of processes are different: while the experimental curve C ( t ) corresponds to a discrete sampling of a continuous-time process (discrete set of observations), ρ ( C | t ) gives the statistics of effective discretetime processes with random values of transmissibility corresponding to θ being drawn from π ( θ |D ).

Figs. S2 and 3 show the comparison of the experimental incidence for systems with lattice spacing a = 10 mm with the estimations ρ ( C | t ) obtained from observations during time t ≤ t obs = 21 days. Comparisons are presented for methodologies B, C, E, and F. Results for methodology A (based on the MD method in step (iii) for prediction) are comparable to those obtained by methodology B (based on the ABC method) and have not been plotted in Figs. S2 and 3 for clarity. Similarly, the comparison for methodology D (based on the ABC inference method) is similar to that plotted for methodology C (based on the MD method) (not shown in Figs. S2 and 3). These results imply that, given a level of description of data (step (i)) and model in step (ii), results are quite independent of whether MD or ABC approaches are used to address step (iii).

As can be seen from the figures, the p.d.f ρ ( C | t ) obtained by methods C, D, and E give a better description of the observed data for most of the replicates. On the other hand, the p.d.f. obtained by methodology F are often not able to capture the global trend of the incidence (see, e.g., replicate 3). This suggests that the focus of methodology F on finer details of the evolution may prevent the predictability of the invasive properties of the system. As discussed in the main text, this might be due to the negative interplay between the simplicity of the CT model and the individual-based description of the data-augmented MCMC method for inference.

Fig. S2. Incidence (line with circles) for fungal invasion of a set of agar dots arranged on a triangular lattice with spacing a = 10 mm [7]. Replicates 1-3 are shown. For each replicate, four panels are shown, with the p.d.f. ρ ( C | t ) for the incidence C at any time t obtained by means of methods B, C, E, and F (as described in Table 1 of the main text). In all the panels, the ridge (bold solid line) corresponds to the median of ρ ( C | t ). The grey-scale shaded areas are the 20% (darker), 40%, 60%, and 80% (lighter) percentiles around the median.

<!-- image -->

## IV. FORECAST OF THE INCIDENCE

In the main text, we quantified the differences between predictions and observations for all methods and fungal invasion experiments in terms of the quantities ∆ c and ∆ F (cf. Fig. 6 of the main text). In this section, we give a more visual comparison between observations and predictions based on the temporal incidence, C ( t ).

Fig. S3. Same as in Fig. S2, for replicates 4-6.

<!-- image -->

Figs. S4 and S5 show the comparison for the six replicates available in the experiments with a = 10 mm and a = 12 mm, respectively. Predictions of the incidence between days 11 and 21 are based on estimates of the transmission parameters made during the first 10 days with methodology C. As can be seen, the estimated incidence provides a reasonable statistical description for the observed incidence for all the replicates. The quantity ∆ c quantifies the rms distance between the observed incidence and the predicted incidence obeying the p.d.f ρ ( C | t ) (given by the grey-scale shaded area in Figs. S4 and S5).

Fig. S4. Forecast of the incidence for fungal invasion in a lattice of agar dots with a = 10 mm. Each panel corresponds to a different experimental replicate of the epidemic. The grey-scaled shaded area shows the p.d.f. ρ ( C | t ) for the numerically extrapolated incidence based on observations over time t ≤ t obs = 10 days, as marked by arrows. The grey-scale shaded areas are the 20% (darker), 40%, 60%, and 80% (lighter) percentiles around the median (bold solid line).

<!-- image -->

## V. ADDITIONAL RESULTS FOR THE NUMERICAL EXPERIMENTS

## A. Homogeneous transmission of infection

Here, we give numerical support to the claim made in the main text that the most probable estimate for transmissibility, ̂ T /star , corresponding to the maximum of the probability density function (p.d.f.) ρ ( ̂ T ), does not differ significantly from the actual transmissibility, T . This is shown in Fig. 6 where the estimate for the transmissibility, ̂ T , is plotted as a function of the transmissibility T . The estimates have been obtained for many different SIR numerical epidemics ( ∼ 10 4 ) with T ∈ [0 , 1]. The analysis has been restricted to epidemics with final size N R (i.e. the number of removed hosts) greater than a certain cut-off, N 0 , in order to avoid estimates for small epidemics giving a poor estimator for transmissibility. Excluding small epidemics from the analysis also makes sense from a practical point of view because they are not a threat in terms of invasion. We have checked that the statistics for ̂ T do not depend

Fig. S5. Similar representation as in Fig. S4 for fungal epidemics in populations of agar dots with lattice spacing a = 12 mm.

<!-- image -->

significantly on N 0 for N 0 /greaterorsimilar 5. For each epidemic i with given T , we obtain the p.d.f. ρ i ( ̂ T | T ) for the effective transmissibility, ̂ T , from observations of the initial stage (for t ≤ t obs = 7 τ , where τ is the infectious period for infected hosts which is taken as the unit of time, τ = 1). Then, the mean p.d.f., 〈 ρ ( ̂ T | T ) 〉 e , is calculated by averaging ρ i ( ̂ T | T ) over N e ( T ) different stochastic realisations of epidemics with given value of T :

The first moment of 〈 ρ ( ̂ T | T ) 〉 e gives an estimate for the mean 〈 ̂ T /star 〉 e averaged over stochastic realisations. The dependence of 〈 ̂ T /star 〉 e on T is shown by the continuous line in Fig. S6. The dispersion of 〈 ρ ( ̂ T | T ) 〉 e , shown by the shaded region in Fig. S6 as a function of T , contains contributions from both the width of each individual distribution, ρ i ( ̂ T | T ), and dispersion of the maxima for different replicates. In particular, the standard deviation, σ ( T ), of 〈 ρ ( T | T ) 〉 e is given by where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is the average over stochastic realisations of the variance σ 2 i of ρ i ( ̂ T | T ). The quantity σ 2 /star is the variance of ̂ T /star,i over stochastic realisations, calculated as

<!-- formula-not-decoded -->

As can be seen from Fig. S6 the actual value for the transmissibility is statistically well described by the distribution 〈 ρ ( ̂ T | T ) 〉 e . The mean for the most probable estimate for the transmissibility, 〈 ̂ T /star 〉 e , is in good agreement with the actual transmissibility. In particular, 〈 ̂ T /star 〉 e provides an excellent estimate for T in the most interesting situations with T /greaterorsimilar 0 . 3 where invasion is more likely. The deviations of 〈 ̂ T /star 〉 e from T are larger for small values of T because epidemics are typically small and the deviations are large. However, it is important to note that 〈 ̂ T /star 〉 e overestimates T in these situations and thus provides a safe bound for invasion.

Fig. S6. Estimates of the transmissibility for numerical SIR epidemics with homogeneous transmissibility. The shaded yellow-brown region shows the levels of confidence as percentage of the p.d.f. 〈 ρ ( ̂ T | T ) 〉 e around the most probable mean transmissibility, 〈 ̂ T /star 〉 e (continuous line), corresponding to each value of T . The dashed line representing the ideal situation (i.e. exact prediction) with ˆ T = T is given for comparison with the actual prediction shown by the continuous line.

<!-- image -->

## B. Heterogeneous transmission of infection

In the main text, we have analysed the epidemics in model systems with homogeneous transmissibility for all pairs of connected hosts. Realistic populations of hosts exhibit inherent heterogeneity in transmissibility and it is crucial to understand its effect on the prediction method introduced in the main text.

In order to study the predictability of invasion for epidemics with heterogeneity in transmission of infection, we consider a simple but generic situation in which transmission is heterogeneous due to variability in the infectivity, I , and susceptibility, S , of hosts. As a first approximation, the rate of infection from an infected donor host with infectivity I d to a susceptible recipient host with susceptibility S r is defined as β d-r = I d S r [8]. We assume that I d and S r are independent random variables distributed according to truncated normal distributions, N ( ¯ I , σ 2 I ) and N ( ¯ S , σ 2 S ), respectively, which are the same for each host[9]. The mean values, ¯ I and ¯ S , provide an effective measure of the mean strength of the transmissibility while the standard deviations, σ I and σ S , characterize the degree of heterogeneity. The multiplicative form of the infection transmission rate β d-r = I d S r brings correlations in transmissibilities, T d-r = 1 -e τβ d-r [10]. Indeed, all the transmissibilities from a donor are affected by the value of I d and thus they are not independent. Similarly, all the transmissibilities to a recipient are influenced by its susceptibility S r and thus also correlated. Such correlations make the invasion probability for heterogeneous system to be dependent on the whole set of transmissibilities { T d-r } . In spite of that, the method based on a single effective transmissibility, T , and Eq. [1] in the main text is still applicable and useful. In realistic situations, the transmissibility is often assumed to be homogeneous because the precise degree of heterogeneity in transmission of infection is unknown and difficult to infer in detail.

In order to test our methodology in heterogeneous systems with different strengths of transmissibility, we perform numerical experiments for epidemics with σ S = σ I = 0 . 2, mean infectivity set to ¯ I = 0 . 4 and variable ¯ S . Again, observations are made over an initial interval of time t ≤ t obs = 7 τ for estimation of the effective transmissibility, ̂ T . Similarly to the analysis given in the previous section for epidemics with homogeneous transmission, Fig. S7 shows a comparison between the p.d.f. 〈 ρ ( ̂ T |〈 T 〉 ) 〉 e averaged over stochastic realisations of epidemics (shaded region) with the ideal situation giving exact prediction of the spatially averaged transmissibility used in the simulations, i.e. ˆ T = 〈 T 〉 (dashed line). As can be seen, the estimates are statistically consistent with 〈 T 〉 . In fact, the mean of the most probable transmissibility, 〈 ̂ T /star 〉 e , gives a good description for 〈 T 〉 (compare the continuous and dashed lines in Fig. S7). We proceed further as in the case with homogeneous transmission by calculating ̂ P inv ( L ) for

Fig. S7. Estimates for the effective transmissibility in numerical SIR epidemics with heterogeneous transmissibility introduced by Gaussian randomness in infectivity I and susceptibility S (with σ I = σ S = 0 . 2, mean infectivity set to ¯ I = 0 . 4, and variable mean susceptibility 0 . 1 ≤ ¯ S ≤ 3 . 5). The shaded yellow-brown region shows the levels of confidence as percentage of the p.d.f. 〈 ρ ( ̂ T |〈 T 〉 ) 〉 e around the most probable mean transmissibility, 〈 ̂ T /star 〉 e (continuous line). The dashed line representing the ideal situation (i.e. exact prediction) with ̂ T = 〈 T 〉 is given for comparison with actual prediction shown by the continuous line.

<!-- image -->

each of the numerical epidemics in a system of size L = 51 (see Fig. 2(a) in the main text) by using Eq. [1] in the main text, the estimated ρ ( ̂ T ), and the probability of invasion P hom ( ̂ T ; L ) for systems with homogeneous transmissibility equal to ̂ T . Note that here P hom ( ̂ T ; L ) corresponds to the function denoted as P inv ( ̂ T ; L ) in the main text. The notations have been changed in order to distinguish between the probability of invasion in homogeneous systems and the probability of invasion in the presence of heterogeneity, denoted as P het ( ̂ T ; L ). The results of our estimations are shown in Fig. S8. The relation between ̂ P inv ( L ) and P hom ( ̂ T ; L ) is very similar to the relation reported in the main text for epidemics with homogeneous transmission. Indeed, for epidemics with low transmissibility, ̂ P inv ( L ) typically overestimates P inv . In contrast, for more invasive epidemics, ̂ P inv ( L ) underestimates P inv for most of the possible effective transmissibilities. Although this comparison has some interest, in the current situation it makes more sense to compare the estimated probability of invasion with the actual probability of invasion in heterogeneous system, P het ( ̂ T ; L ), that can be calculated numerically and

Fig. S8. Numerical experiments of SIR epidemics with heterogeneous transmissibility induced by Gaussian randomness in infectivity I and susceptibility S (with σ I = σ S = 0 . 2, mean infectivity set to ¯ I = 0 . 4, and variable mean susceptibility 0 . 1 ≤ ¯ S ≤ 3 . 5). The lines marked by circles and squares correspond to the probabilities of invasion P hom and P het plotted vs 〈 T 〉 for homogeneous and heterogeneous systems of size L = 51, respectively,. Estimates for the probability of invasion, ̂ P inv ( L ), have been evaluated for each epidemic (out of ∼ 10 4 ) using the p.d.f. ρ ( ̂ T ) obtained by observing the initial evolution during time t ≤ t obs = 7 τ and then fitting the observed spatio-temporal map by the shell-evolution function. Horizontal slices of the yellow-brown shaded area corresponding to a fixed value of ̂ P inv ( L ) represent the distribution ρ ( ̂ T ) averaged over realisations of epidemics with the same value of ̂ P inv ( L ). The points on the ridge (black solid curve) of the shaded area correspond to the most probable transmissibility, ̂ T ∗ , averaged over epidemics with a certain value of ̂ P inv ( L ).

<!-- image -->

shown by the line with squares in Fig. S8. The comparison of this line with the shaded region reveals that the estimated ̂ P inv ( L ) overestimates the actual probability of invasion in most of the situations both for cases with low and high transmissibility. Therefore, the estimates of ̂ P inv typically provide safe bounds for the probability of invasion. In fact, the larger the heterogeneity in susceptibility and/or infectivity, the safer the bound is. This is a consequence of the inequality P inv ( 〈 T 〉 ) ≥ P het ( 〈 T 〉 ) that holds for any given value of 〈 T 〉 under quite general conditions due to the existence of correlations in transmission induced by heterogeneity in the transmission rates [8, 11]. Indeed, Fig. S8 shows that the inequality holds for the numerical experiments considered here with 〈 T 〉 = ̂ T (i.e. the line corresponding to the heterogeneous case marked by the squares is below the line marked by the circles for homogeneous system). These results are particularly encouraging for analysis of realistic epidemics in which a certain

degree of heterogeneity in susceptibility and infectivity of hosts is expected to be ubiquitous.

## VI. DIFFERENCES BETWEEN P inv AND ˆ P inv

In this section, we discuss the origin of the difference between the estimated probability of invasion, ˆ P inv ( L ), evaluated at the most probable transmissibility, ̂ T /star , and the actual probability of invasion P inv ( T ; L ) one would obtain if the transmissibility of the epidemic was known exactly.

̂ To start with, recall that the relation between ˆ P inv ( L ) and P inv ( ̂ T ; L ) is given by Eq. [1] in the main text. As we have seen, ρ ( ̂ T ) is a peak-shaped function approximately symmetric about the peak position at ̂ T /star . Therefore, the peak region will mainly contribute to the integral in Eq. [1] of the main text. If ̂ T /star is not too close to the inflection point of P inv ( ̂ T ; L ), the Taylor series expansion of P inv ( ̂ T ; L ) in ( ̂ T -̂ T /star ) to second order, i.e.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is sufficient to estimate the deviation of ̂ P inv from P inv . Indeed, substitution of Eq. (S.10) into Eq. [1] of the main text gives:

The distribution of ̂ T is approximately symmetric around the maximum, i.e. ρ ( ̂ T -̂ T /star ) /similarequal ρ ( ̂ T /star -̂ T ) (see Fig. 2(b) in the main text), and thus the term containing P ′ inv in Eq. (S.11) is negligible in comparison with other terms in the sum. This means that

<!-- formula-not-decoded -->

where we have taken into account that the last integral in Eq. (S.11) is positive. The above inequalities demonstrate that the value and sign of ̂ P inv ( L ) -P inv ( ̂ T /star ; L ) depends on the curvature of P inv ( ̂ T ; L ) around ̂ T = ̂ T /star which is given by P ′′ inv .

- [1] D. R. Cox and V. Isham, Point Processes , Monographs on Applied Probability and Statistics 12 (Chapman &amp; Hall, London, 1980)
- [2] G. J. Gibson and E. Renshaw, IMA Journal of Mathematics Applied in Medicine and Biology 15 , 19 (1998)
- [3] P. Marjoram, J. Molitor, V. Plagnol, and S. Tavar´ e, Proc. Natl. Acad. Sci. USA 100 , 15324 (2003)

- [4] P. Marjoram, J. Molitor, V. Plagnol, and S. Tavar´ e, Proc Natl Acad Sci USA 100 , 15324 (2003)
- [5] A. Gelman, J. B. Carlin, H. S. Stern, and D. B. Rubin, Bayesian Data Analysis (Chapman and Hall/CRC, 2004)
- [6] G. J. Gibson, W. Otten, J. A. N. Filipe, A. Cook, G. Marion, and C. A. Gilligan, Stat Comput 16 , 391 (2006)
- [7] D. J. Bailey, W. Otten, and C. A. Gilligan, New Phytol. 146 , 535 (2000)
- [8] J. Miller, J. Appl. Probab. 45 , 498 (2008)
- [9] The support of the normal distributions has been restricted to [0 , ∞ ) to ensure that both I i and S i are positive.
- [10] P. Grassberger, Math. Biosc. 63 , 157 (1983)
- [11] J. T. Cox and R. Durrett, Stoch. Proc. Appl. 30 , 171 (1988)