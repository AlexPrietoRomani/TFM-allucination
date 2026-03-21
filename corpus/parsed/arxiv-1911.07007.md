---
id: arxiv-1911.07007
title: Spatiotemporal large-scale networks shaped by air mass movements
year: 2019
country: Internacional
source: ArXiv (stat.AP)
doc_type: Artículo científico
language: en
tags:
  - patógenos vegetales
  - epidemiología
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Spatiotemporal large-scale networks shaped by air mass movements

Maria Choufany a , Davide Martinetti a , Rachid Senoussi a , Cindy E. Morris b , Samuel Soubeyrand a a INRAE, BioSP, 84914 Avignon, France

b INRAE, UR407 Pathologie V´ eg´ etale, Centre de Recherche PACA, Montfavet, France

## Abstract

The movement of atmospheric air masses can be seen as a continuous and complex flow of particles hovering over our planet. It can however be locally simplified by considering three-dimensional trajectories of air masses connecting distant areas of the globe during a given period of time.

In this paper, we present a mathematical framework to construct spatial and spatiotemporal networks where the nodes are the subsets of a partition of a geographical area and the links between these nodes are inferred from sampled trajectories of air masses passing over and across the nodes. We propose different estimators of link intensities relying on different bio-physical hypotheses and covering adjustable time periods. This approach leads to a new class of spatiotemporal networks characterized by adjacency matrices. We applied the approach in two real geographical contexts: the watersheds of the French region Provence-Alpes-CÃťte d'Azur and the coastline of the Mediterranean Sea. The analysis of the constructed networks allowed identifying a marked seasonal pattern in air mass movements in the study areas.

These constructed networks can be used to investigate issues, e.g., in aerobiology and epidemiology of airborne plant pathogens. Similar networks could be estimated from other types of trajectories, such as animal trajectories.

Keywords: Aerobiology; Air masses dynamics; Connectivity; Spatial network; Spatiotemporal network; Trajectory.

## 1. Introduction

Atmospheric air masses are volumes of air with a defined temperature and water vapor content that have long been known to rule fundamental atmospheric phenomena like weather and air currents. Their composition is mostly inert gases, but both organic and inorganic particles have been found to linger in high-altitude air as a consequence of the constant interaction of air masses with the earth's surface below them. A non-exhaustive list includes gases and minerals like wildfire smoke, radioactive material, dust, sand, volcanic ash and sea salt, but also living organisms such as pollen, fungal spores, bacteria, virus and small insects. Despite the relative sparse density of these particles with respect to the volume of an

Email addresses: maria.choufany@inrae.fr (Maria Choufany), davide.martinetti@inrae.fr (Davide Martinetti), rachid.senoussi@inrae.fr (Rachid Senoussi), cindy.morris@inrae.fr (Cindy E. Morris), samuel.soubeyrand@inrae.fr (Samuel Soubeyrand)

air mass, their presence and transportation across the planet has proven to have strong effects on many phenomena impacting human health and safety (pollen (Mahura et al., 2007; ˇ Sauliene and Veriankaite, 2006; Bogawski et al., 2019), dust concentrations (Khaniabadi et al., 2017; Aciego et al., 2017), nuclear byproducts (Moroz et al., 2010; Rolph et al., 2014), human, animal and plant epidemics (Leyronas et al., 2018; Wang et al., 2010; Aylor, 1990; Mundt et al., 2009; Sady´ s et al., 2014; Hiraoka et al., 2017), air pollution (Liu et al., 2018b,a; Talbi et al., 2018), and rainfall (Chen and Luo, 2018; Armon et al., 2018; Rabinowitz et al., 2019)).

The rise in the number of publications on these subjects suggests a growing interest of the scientific community on the effects of air-mass movements on the biosphere, that has surely been boosted by recent available developments, such as the Hybrid Single-Particle Lagrangian Integrated Trajectory model ( HYSPLIT , Stein et al. (2015)), allowing reconstruction of actual air-mass movements at rather fine geographical and temporal scales and with a global cover.

The vast majority of studies focused on isolated events, such as dust storms or peaks of air pollutants, that are rather concentrated in time (from few hours to few weeks) and/or space (just a few locations such as cities). Nonetheless, the movement of air masses is expected to have impacts on a broader spatiotemporal scale, as reviewed in recent studies (Leyronas et al., 2018; Margosian et al., 2009). The purpose of the present paper is then to propose a mathematical framework for studying air-mass movements on large spatiotemporal scales, under the hypothesis that these movements can create stable and recurrent connections between distant portions of a territory. The very nature of these connections will be further specified throughout the manuscript, but as a general rule we will consider that any pair of points (or areas) in space can have a certain degree of connection, regardless of their geographic distance, provided that there are recurrent air-mass trajectories that connect the two points (or areas). The direction and strength of these connections will be estimated by looking at the trajectories linking every pair of points/areas and weighting them according to appropriate measures. In this perspective, it seems natural to resort to graph and network theory, since the formalism of nodes and edges provides an adequate environment for describing complex connections and can further be used to deepen into the topology of the constructed networks in order to infer interesting properties of the graphs, such as the presence of hubs.

From a generic statistical point of view, we aim to (i) estimate the weighted and directed edges of a graph using a sample of trajectories of individuals traveling through the space formed by the nodes of the graph, and (ii) characterize the estimated graph based on relevant statistics.

In the following sections, we first introduce the definitions and properties that will allow us to describe and then estimate connections between points/areas in space via spatiotemporal trajectories. Then, we propose several types of measures to model diverse types of connections. The expected output consists of a spatiotemporal graph describing the network of links induced by trajectories. It's worth noting that our approach is meant to infer connectivity induced by air-mass movements and it is readily applicable to HYSPLIT -type data, but we have maintained a sufficient level of generality to be applied to other

phenomena, provided that trajectory data are available (e.g. animal trajectories). Finally, we apply our method to two case studies concerning the coastline of the Mediterranean sea and the French region of Provence-Alpes-Cˆ ote d'Azur. The two case studies have different spatiotemporal granularities and they will be used to provide examples of application of the proposed methodology.

## 2. Framework for the definition of trajectory-based networks

In this section we show how a set of trajectories evolving within space during a finite time interval can be used to construct pertinent spatiotemporal networks. We first recall some basic definitions related to networks (Section 2.1) and then propose a statistical methodology to infer the network structure from a data set of trajectories (Section 2).

## 2.1. Network theory

Network theory (a.k.a. graph theory) is a mathematical formalism introduced by Leonhard Euler to describe the famous K¨ onigsberg bridge problem (Newman, 2003; Strogatz, 2001; West et al., 1996). The two basic components of a network are a set of nodes linked by a set of edges. Nodes can represent a variety of things, such as persons, regions, computers, neurons, etc., while edges are used to describe the connections between those nodes. Formally, a network G p V, E q is defined as a set of nodes (or vertices) V t v 1 , v 2 , . . . , v N u connected by a set of edges E t e ij u i,j Pt 1 ,...,N u . A natural way of representing a network is given by means of a N N square matrix M , usually referred to as an adjacency matrix , whose term p i, j q , M ij , is non-zero an edge exists between i and j . By convention, adjacency matrices are defined to have an empty diagonal (i.e. M ii 0 , i P t 1 , . . . , N u ), meaning that nodes cannot be self connected. If M is symmetrical (i.e. M ij M ji , i, j P t 1 , . . . , N u ), then the network is said to be undirected , and directed otherwise. If M ij P t 0 , 1 u , the network is said to be binary , meaning that an edge between two nodes i and j either exists or does not. Otherwise, if M ij P R , the network is said to be weighted , meaning that the edge between nodes i and j are more or less connected.

In this paper, a network is said to be spatial (Barth´ elemy, 2014) when nodes correspond to geographic locations, while we use the term temporal (Holme and Saram¨ aki, 2012) to refer to networks where edge values can change over time. Finally, we will use the term spatiotemporal network to refer to network that are simultaneously spatial and temporal, under the constraint that nodes cannot change position, neither appear nor disappear over time. The networks considered in this paper also fall into the rather generic definition of spatiotemporal networks. If the spatial qualifier means that the nodes of the networks represent fixed geographical locations, the temporal qualifier is more complex. Indeed, temporal networks are generally divided in the literature into two main classes, namely contact graphs or interval graphs (Holme and Saram¨ aki, 2012). The former type refers to networks where edges represents instantaneous contacts between nodes (Figure 1(a)), while in the second type edges are active over time intervals instead of instants of time (Figure 1(b)). In this paper we propose a new definition of spatiotemporal networks where nodes correspond to disjoint regions of the space and edges are computed as a function of the flow of trajectories linking these nodes (Figure 1(c)), as it will be explained in the rest of the current section.

Figure 1: Types of temporal networks. The time of activation is indicated within the grey bar next to the edges (ranging between 0 and 8). For contact networks (a), edges activate only for one instant at the time and are marked with black vertical lines inside the grey bars. For example, in panel (a), the edge between nodes A and B is only active at instants 2, 4, 6 and 7. For interval networks (b), edges can be activated during an interval of time. For example, the edge between A and B in panel (b) is active during the time intervals (0,3) and (6,8). For contact networks (c), the edges are quantitatively more or less active across time, and the quantity of activity of any edge is described by a temporal function.

<!-- image -->

## 2.2. Flows and trajectory segments

We consider a function Φ : R R Ω Ω, usually called flow on the spatial domain Ω of R d , satisfying the following properties:

<!-- formula-not-decoded -->

where s, t, t 1 P R and x P Ω. For fixed t and s , the flow Φ p t, s, q is a spatial transformation. For fixed x and varying s or t , the function gives a forward or backward trajectory of a particle over Ω between times t ^ s inf p t, s q and t \_ s sup p t, s q . If s / t , y Φ p t, s, x q gives the future location at time t of the particle presently located at x at time s . Contrarily, if s ¥ t , y Φ p t, s, x q gives the location at past time t that was occupied by the particle located at x at present time s . Φ p t, s, . q is assumed to be a bijective mapping meaning that particles following distinct trajectories cannot be at the same location at the same time.

In general, a flow is defined with respect to a possibly time-dependent vector field F over R Ω, as the solution u : R Ω of an ordinary differential equation (see e.g. Hamilton's equations in classical

mechanics) with specified initial condition at a specified time s :

<!-- formula-not-decoded -->

where F is continuous and Lipschitzian over R Ω. In the setting introduced above, Φ p t, s, x q u p t q with Φ p s, s, x q =u(s)= x . The solution u represents the trajectory of the particle located at x at time s . Varying the initial condition in System (2), i.e. varying s and x , leads to consider pieces of trajectories of all particles which dynamics are governed by the vector field F . In this article, the vector field F will not be made explicit, but we will consider samples of trajectory segments (defined below) for constructing trajectory-based networks.

Definition 2.1. The trajectory segment associated to the flow Φ over the time interval ∆ ts r t ^ s, t \_ s s , s, t P R , for a particle located at x P Ω at time s is defined as follows:

<!-- formula-not-decoded -->

If s t (resp. s ¡ t ), Γ p t, s, x q is a forward (resp. backward) trajectory segment. In this article, we are mainly interested in backward trajectories, but the framework presented here encompasses forward trajectories as well.

Example 2.1. The notions of flow and trajectory segment can be adapted to cope with air mass trajectories over the Earth surface. In this case, the spatial domain Ω representing the Earth surface is the sphere S 2 in R 3 . If in addition, air masses are characterized by altitude and temperature evolving in space and time, then Ω S 2 R R , where R (resp. R ) is the domain of the altitude (resp. temperature) coordinate.

Example 2.2. Animal movements and behaviour activities can also be represented with the notions of flows and trajectory segments, providing, for instance, the animal locations and the covariate value indicating whether animals are feeding or not. In this case, Ω R 2 t 0 , 1 u , where 1 stands for 'the animal is feeding' and 0 otherwise. The use of a binary variable for describing the feeding activity may require the use of stochastic processes or generalized functions undergoing dynamic analog to the System (2) for constructing the flow if it is defined with respect to a vector field F .

## 2.3. Pointwise and integrated connectivities

Trajectory-based networks are grounded on the notion of connectivity used as a quantitative, directed measurement of edges between graph nodes. In this aim, we first define the pointwise connectivity as a measure (or submeasure), in the mathematical sense, of the connectivity between a subset A and a point x of Ω induced by the trajectory segments Γ p t, s, x q of a particle located at x at time s . Then, we use the pointwise connectivity to define the integrated connectivity between two subsets A and B of Ω over a temporal domain ∆ of R (∆ can be the union of disjoint intervals).

Definition 2.2. Let x P Ω and A P B p Ω q , where B p Ω q is a σ -algebra of subsets of Ω. The pointwise connectivity associated to the flow Φ is defined as a real valued function Ψ on B p Ω q R R Ω, conveniently denoted by Ψ p A | t, s, x q , where A Ψ p A | t, s, x q is a measure or a submeasure on Ω for each t, s, x

Diverse types of the pointwise connectivity can be constructed, either using trajectory segments generated by Φ, or directly using Φ. Specific pointwise connectivities can include environmental covariates and even covariates associated to very the movements of particles. Below, we give several examples of such specifications. Some of these examples are graphically represented in Figure 2. Most examples are particularly relevant when Ω is a simple geographic domain and when Φ defines movements of individuals (e.g., air masses, animals or particles) within Ω.

Example 2.3. The contact-based pointwise connectivity is defined by:

<!-- formula-not-decoded -->

where A ts ∆ ts A and 1 denotes the indicator function. Ψ C p A | t, s, x q indicates whether or not the particle whose movement in Ω is governed by Φ p , s, x q hit A during the time interval ∆ ts . Note that A Ψ C p A | t, s, x q is only a submeasure on Ω since Ψ C p A Y A 1 | t, s, x q / Ψ C p A | t, s, x q Ψ C p A 1 | t, s, x q for disjoint sets A and A 1 of B p Ω q .

Remark 1. This example based on the simple contact between sets can be considered as too strict from a statistical and measure-theory perspective since the length or the duration of a contact may be null. Instead, a positive constraint on contact length for example can be used to define another version of the contact-based pointwise connectivity: Equation (4) could then be replaced by

<!-- formula-not-decoded -->

where L p A ts X Γ p t, s, x qq denotes the length of the curve Γ within A . The length operator L will be made explicit in Example 2.5.

Example 2.4. The duration-based pointwise connectivity is defined by:

<!-- formula-not-decoded -->

to measure the duration spent by the particle in A during ∆ ts .

Example 2.5. The length-based pointwise connectivity is defined by:

<!-- formula-not-decoded -->

where ∇ v Φ p v, s, x q stands for the gradient of the flow Φ with respect to the time variable v and ||   || denotes the Euclidean norm. Ψ L p A | t, s, x q measures the distance travelled within A by the particle during ∆ ts .

Example 2.6. The pointwise connectivity based on local volume is defined by:

<!-- formula-not-decoded -->

where det p J x Φ p v, s qq is the determinant of the Jacobian matrix (with respect to x) of the spatial transformation Φ p v, s, q . The absolute value | det p J x Φ p v, s q| of the Jacobian determinant at x gives the ratio by which the function Φ p v, s, q expands/shrinks infinitesimal volumes around location x into infinitesimal volumes around location Φ p v, s, x q . In other words, Ψ V p A | t, s, x q assesses how particle density increases or decreases from x to A along the time interval ∆ ts . Intuitively, if n particles are initially in A and if the infinitesimal volume around any of these particles tends to shrink from A to x , then one expects a high concentration of particles in a fixed volume around x and, therefore, a high connectivity from A to x . Conversely, if the infinitesimal volume around a particle tends to expand from A to x , then one expects a lower concentration of particles in the same fixed volume around x and, therefore, a lower connectivity from A to x .

More sophisticated specifications of the pointwise connectivity can be proposed by incorporating spatio-temporal covariates in its formulation, like in the following examples.

Example 2.7. Let G denote a time-varying vector field defined over R Ω. The pointwise connectivity based on the external vector field G is defined by:

<!-- formula-not-decoded -->

where ∇ v Φ p v, s, x q , G p v, Φ p v, s, x qq ¡ is the scalar product between the gradient with respect to the time variable v of the flow Φ and the vector field G . Larger the average collinearity in A between the instantaneous movement of the particle and the simultaneous direction of the vector field G , higher the connectivity between A and x . For instance, if Φ gives the movement of air masses and G provides the intensity and the direction of a continuous release of specific particles, then the connectivity will be high (resp. low) if the movement of the air in A and the movement of particles released in A are approximately collinear (resp. orthogonal).

Example 2.8. Let Z and ˜ Z be positive real valued spatio-temporal functions defined over R Ω. The pointwise connectivity based on Z and ˜ Z is defined by:

<!-- formula-not-decoded -->

This form of pointwise connectivity may represent, for example, (i) the negative effect of the altitude of the air mass when it is above A on the recruitment of specific particles from the ground, and (ii) the positive effect of rainfall at p s, x q on the deposition of particles from the air mass to the ground (see Figure 3). Thus, lower the average altitude of the air mass above A and more intense the rainfall at p s, x q , larger the contribution to the connectivity between A and x . This is expressed in Equation (8) as follows: (i) ˜ Z is defined as the binary function indicating whether or not the altitude of the air mass (located at x at time s ) is lower than a threshold h when it is located at Φ p v, s, x q at time v ; (ii) Z is a function of the local rainfall intensity at p s, x q .

Remark 2. If in Example 2.8, the altitude of the air mass is incorporated as the third coordinate of Φ and A is a 3D-domain vertically limited by the threshold value h , then, Equation (8) is simplify reduced to Equation (5).

Remark 3. Example 2.8 could be generalized by considering a measure, say µ , over R , to handle the potential contribution of discrete-time events to the pointwise connectivity:

<!-- formula-not-decoded -->

Remark 4. In the same vein, Example 2.8 can also be modified by adding within the integral the term || ∇ v Φ p v, s, x q|| arising in Equation (6) to account for a supplementary effect of the distance travelled within A on the pointwise connectivity.

Each pointwise connectivity defined above can be used for defining the integrated connectivity, which measures the quantitative directional link between two subsets A and B of B p Ω q generated by trajectories of particles located in B at times belonging to the temporal domain T .

Definition 2.3. Let A and B be two sets of B p Ω q and T a subset of the temporal domain R . The δ -lag integrated connectivity linking B to A over T is defined by:

»

<!-- formula-not-decoded -->

where δ P R and ν is a measure on R Ω.

Definition 2.3 encompasses connectivities generated by either forward or backward trajectories, depending on the sign of δ . The use of a unique duration | δ | could be relaxed to account for space-time heterogeneities in the duration of trajectories. It could even be infinite by introducing a measure over time like in Equation (9).

The measure ν in Definition 2.3 can be continuous, discrete or hybrid over R Ω. Indeed, if particles of interest are air masses, then B can be considered as continuously filled in space and time. Conversely, if particles of interest are animals of a specific species, then animals occupy only punctual locations in B at each time and the measure x ν p ds, dx q , given s , is discrete in Ω, whereas the temporal component of ν is continuous. Another examples occurs when the time s corresponds to death times of animals, then ν is both discrete in space and time with a mass only at a countable collection of space-time points.

## 2.4. Trajectory-based network

Definition 2.4. A trajectory-based network generated by Ψ p 2 q ν,δ (given by Equation (10)) over the temporal domain T R , is a graph whose nodes A i , i t 1 , .., I u , are disjoint sets of Ω in B p Ω q and whose directed edges are weighted by integrated connectivities M ij Ψ p 2 q ν,δ p A i A j | T q , 1 / i, j / I and i j .

Definition 2.4 corresponds to a spatial trajectory-based network evaluated over the fixed temporal domain T . It can be extended in different ways to obtain spatiotemporal analogs. For example, if T 1 , . . . , T K denote K disjoint but successive time intervals with equal lengths, then the sequence of

trajectory-based networks generated by Ψ p 2 q ν,δ p      | T k q , k 1 , . . . , K , forms a spatiotemporal trajectorybased network that can be analyzed to assess how connectivities across space are changing with time. This is one of the issues considered in Section 4.2.

Figure 2: Illustration of contact-based, duration-based and length-based pointwise connectivities (resp. Ψ C , Ψ D and Ψ L ) between the elliptic spatial domain A R 2 and different spatial points x at time s 1, for ∆ ts r 0 , 1 s . The left curve on panel (a) never enters the domain A . The middle curve on panel (a) enters A (red part of the curve) over a relatively long duration (as shown by panel (a)) but a short distance (as shown by panel (b)). The right curve on panel (a) enters A over a shorter duration but a longer distance. Thus, Ψ C p A | t, s, x q , Ψ D p A | t, s, x q and Ψ L p A | t, s, x q are zero for the left curve; Ψ C p A | t, s, x q 1 for the two other curves; Ψ D p A | t, s, x q is larger for the middle curve than for the right one, whereas Ψ L p A | t, s, x q is larger for the right curve than for the middle one.

<!-- image -->

Figure 3: Illustration of pointwise connectivity based on a covariate measured along the trajectory (see Example 2.8). In this illustration, the passage of the particle in the elliptic spatial domain A contributes to the pointwise connectivity (red part of the curve in panel (a)) only when the particle is at an altitude lower than a threshold value (grey part of the curve in panel (b)).

<!-- image -->

## 3. Estimation of integrated connectivities

In practice, the integral defining the integrated connectivities between subsets of Ω (Definition 2.3) cannot be analytically computed in general, but can be estimated from a sample of trajectories. For instance, the integrated connectivity Ψ p 2 q ν,δ p B A | T q can be estimated by its empirical counterpart obtained by importance sampling, say p Ψ p 2 q ν,δ p B A | T q :

<!-- formula-not-decoded -->

where s 1 , . . . , s N P T and b 1 , . . . , b N 1 P B are times and locations, respectively, randomly drawn under the measure ν restricted to T B , | T | and | B | are the length and area of T and B , respectively, and Ψ p A | s k δ, s k , b l q is the pointwise connectivity associated to the trajectory of the particle located at b l at time s k and observed over ∆ s k δ,s k r s k ^ s k δ, s k \_ s k δ s .

If ν is constant, other classical numerical approaches can be applied to approximate the integral, such as an hybrid approach in which the mid-point rule is applied in time and a regular point process is used in space. In such a case, the integrated connectivity estimator is also given by Equation (11).

Example 3.1. Using Equation (11), the contact-based pointwise connectivity in Example 2.3 is estimated

by:

<!-- formula-not-decoded -->

where A s k δ,s k ∆ s k δ,s k A . Thus, p Ψ p 2 q C,δ p B A | T q is simply the proportion of sampled trajectories intersecting A , multiplied by | T || B | .

Example 3.2. Using Equation (11), the duration-based pointwise connectivity in Example 2.4 is estimated by the average duration of the intersections between the sampled trajectories and A , multiplied by | T || B | .

Example 3.3. Using Equation (11), the length-based pointwise connectivity in Example 2.5 is estimated by the average length of the intersections between the sampled trajectories and A , multiplied by | T || B | .

## 4. Applications

In this section, we applied our general framework to the flow of air mass movements. Indeed, these movements compiled over years were used to characterize climatic patterns (Hondula et al., 2010) and to describe the transport of pollutants (P´ erez et al., 2015). We show now how to deploy our approach for constructing air-mass movement networks in two real geographical contexts, namely the coastline of the Mediterranean Sea and the French region of Provence-Alpes-Cˆ ote d'Azur. These two examples have been chosen in order to prove the flexibility of our approach to different situations and geographical scales.

## 4.1. Case study regions and network construction

The first study region corresponds to the coast of the Mediterranean Sea, ranging approximately 1,600 km from north to south and 3,860 km from east to west. The temperate climate of the chosen region is strongly influenced by the presence of the Mediterranean Sea, with mild winters, hot summers and relatively scarce precipitations events. The landscape is characterized by coastal vegetation, typically shrubs and pines, and densely populated areas with intensive crop production of wheat, barley, vegetables and fruits, especially olive, grapes and citrus. In this paper, we characterize recurrent movements of air masses through the Mediterranean region by defining a grid with mesh size 74 km covering the coastline from 5 km up to 250 km inland from the coast, including the four largest islands (namely Sicily, Sardinia, Cyprus and Corsica). Thus, we divide the region into 604 cells, where the centroids of the cells will be used as arrival locations of air-mass trajectories and will correspond to the nodes of the constructed network.

The second study region corresponds to the French region of Provence-Alpes-Cˆ ote d'Azur (PACA, hereafter), located in the south-eastern part of France and characterized by a rather complex landscape formed by a densely-populated coastline, agricultural lands (high-value-crops with fruit and olive orchards, vineyards, vegetable cultivation and horticulture), and natural mostly-alpines areas. The choice of this particular region is justified in the context of a research project aimed at assessing the potential longdistance dissemination of phytopathogenic bacterial populations that are known to be transported by air

currents. The bacteria of interest (e.g., Pseudomonas syringae ) can be lifted in to the air from a source location and then be passively transported by air masses until they are deposited back to land onto a different, far away sink location. Since the life cycles of the considered species of bacteria are strongly linked to the water cycle (Morris et al., 2008), we naturally partitioned the study area in a way that fit this assumption. Hence, we considered the 294 watersheds of the PACA region to define the sites that will later constitute the nodes of the constructed network. Since watersheds have irregular shapes and varying sizes, we selected a certain number of arrival locations per watershed (between 1 and 10 and proportionally to the watershed area) in order to cover the watersheds consistently according to the relative importance of their size and estimate the integrated connectivities. In total, a set of 833 arrival locations for air-mass trajectories was generated.

Once the arrival points for the two study regions have been established, we turned to the computation of air-mass trajectories arriving at the prescribed locations using the Hybrid Single-Particle Lagrangian Integrated Trajectory model ( HYSPLIT , (Stein et al., 2015)). The HYSPLIT model can be fed with meteorological data from the Global Data Assimilation System files with a 0.5-degree spatial resolution (GDAS 1 ) and was tuned by us to return 48-hours backward air-mass trajectories arriving at the prescribed locations at an altitude of 500 m above mean sea level. A single trajectory consists of a vector containing the hourly positions (longitude, latitude and altitude) visited by the air mass before arriving at the specified location and time. Air-mass trajectories have been computed for every arrival location (604 for the Mediterranean region and 833 for the PACA region) and for every day between January 1, 2011 and December 31, 2017 (arrival hour is 12:00 GMT). The total number of computed trajectories is 1,543,220 for the Mediterranean region and 2,128,315 for the PACA region.

The final step for the construction of the networks is the estimation of the adjacency matrices of the networks, based on the methodology presented in the previous sections. To do that, for each pair of subsets of the spatial domain, we used the daily 48-hours backward trajectories arriving at the locations sampled within the receptor subset, and computed the contact-based estimator (see Example 3.1). The subsets of the spatial domain are the watersheds for PACA and circular buffers of radius 20 km for the Mediterranean region, as in Leyronas et al. (2018)

In this work we will consider networks corresponding to three temporal contexts: (i) the spatial networks obtained when T is the entire period 2011-2017, (ii) the yearly spatiotemporal networks formed by the seven spatial networks obtained when T 1 encompasses the year 2011, T 2 encompasses 2012 and so on, and (iii) monthly spatiotemporal networks formed by the twelve spatial networks obtained when T 1 represents every January from 2011 to 2017, T 2 every February from 2011 to 2017, and so on. In all these cases, we consider that the length of the time interval was 1 to easily compare the inferred networks (i.e., | T | 1 in Equations (11) and (12)).

1 https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-data-assimilation-system-gdas

## 4.2. Network analysis

The constructed networks are directed and weighted by contact-based connectivities generated by air mass trajectories. They are inherently complex by the sheer amount of spatial and temporal information that they encompass. Hence, there is no easy way of representing the results either graphically or numerically, without compromising the original complexity of the networks. While a comprehensive physical study of the spatiotemporal properties of these networks goes beyond the scope of the paper, we explore the estimated trajectory-based networks by looking at some generic properties through the following indices:

- Diameter: the longest of all possible shortest paths between any two pair of nodes.
- Density: the ratio between the sum of all edge weights and the number of all possible edges (Liu et al., 2009).
- Transitivity (also known as clustering): the equivalent definition of density, but applied to triplets of nodes instead of pairs of nodes (Opsahl and Panzarasa, 2009).
- Shortest path: characterized by the average and standard deviation of the computed shortest path between any possible pair of different nodes (Newman, 2001).
- Small worldness: refers to the property of a network of being highly clustered and having relatively short shortest paths. It is computed as the ratio between the normalized clustering and the normalized average shortest path distance (Li et al., 2007; Colon-Perez et al., 2016).
- Scale-free property: The degree of a node in terms of the total number of edges entering and exiting from it, and for directed networks it can be decomposed in the incoming and outgoing degree, respectively. The degree distribution is the empirical distribution of the degree of a network and it said to be scale free when it approximately follows a power law distribution, i.e. P p k q k p α q , where P p k q represents the probability of a node having degree equal to k (Barab´ asi and Bonabeau, 2003; Barab´ asi and Albert, 1999). Some authors impose that the α parameter of the power law distribution has to fall within the interval r 2 , 3 s (Barab´ asi et al., 2016). Thus, a network is scale free when most of its nodes have low degree, while the probability of having nodes with very high degree is not negligible (fat right tail of the distribution). Nodes with very high degree play a crucial role in dynamics conditional on networks and are often referred as hubs (Liu et al., 2011).
- Degree correlation: in directed networks, it accounts for the correlation between the incoming and the outgoing degree of a node. Networks with positive (resp. negative) degree correlation foster (resp. hamper) epidemic spread (Pautasso et al., 2010).

## 4.3. Results

Figure 4: Networks weighted by contact-based connectivities generated by air mass trajectories between (a) the 604 sampled circular areas within the Mediterranean basin and (b) the 294 watersheds of PACA. Edges with weights lower than 0.3 for (a) and 2 10 3 for (b) are not drawn. The cuts of the intervals in the two legends are chosen in such a way that each interval contains 20% of the observed data. The differences in the values taken by the connectivities in (a) and (b) are due to different measures of the area | B | in Equations (11) and (12): | B | 1 for each node in (a), whereas B is the actual area (expressed in km 2 ) of each whatershed in (b).

<!-- image -->

The two spatial trajectory-based networks representing the strength of tropospheric connections in the Mediterranean region and PACA during the entire period 2011 to 2017 are represented in Figure 4. In order to highlight the edges that represent strong connections, we depicted them with darker shades of color, while we did not draw the connections that had a weight of less than 0.3 for the Mediterranean and 2 10 3 for PACA. It can be seen that the strongest connections tend to link nodes that are geographically close, but nonetheless moderate connections also exist between rather distant nodes (see also Figure 8). This is confirmed by small values of the average shortest path distance 8 . 20 10 4 for the Mediterranean and 2 . 57 10 4 for PACA, and high values of the transitivity index (0.74 for the Mediterranean region and 0.99 for PACA), as shown in the first lines of Tables 1 and 2. The connectivities in PACA are mostly oriented from North-East to South-West, which corresponds to the direction of the prevailing wind in this region. For the Mediterranean basin, the direction of the connectivites depends on the region and does not have a fixed direction (see Figure 9). An interesting additional difference between the two networks is that the one for PACA has a very negative degree correlation ( 0 . 85), meaning that nodes having a high incoming degree will have low outgoing degree, and vice versa. On the other hand, for the Mediterranean network, the value of the degree correlation is moderately positive (0.31), meaning that nodes having high a incoming degree tend to have also high a outgoing degree.

Table 1: Network indices (Diameter, density, transitivity, shortest path (mean and standard deviation), small worldness, scale-free property, degree correlation) calculated from the networks covering the Mediterranean region and estimated in three temporal contexts: the entire period 2011-2017, yearly time periods from 2011 to 2017 and monthly time periods.

Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: Diam, Mediterranean region: Dens, Mediterranean region: Trans, Mediterranean region: S P (mean), Mediterranean region: S P (sd), Mediterranean region: SW, Mediterranean region: S F, Mediterranean region: D C.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2011-2017, Mediterranean region: 3.12 10 3, Mediterranean region: 2.96 10 4, Mediterranean region: 0.74, Mediterranean region: 8.20 10 4, Mediterranean region: 2.19 10 4, Mediterranean region: 18242, Mediterranean region: 11.6, Mediterranean region: 0.31.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2011, Mediterranean region: 0.03, Mediterranean region: 3.0 10 4, Mediterranean region: 0.67, Mediterranean region: 6.17 10 3, Mediterranean region: 1.92 10 3, Mediterranean region: 2222, Mediterranean region: 11.5, Mediterranean region: -0.04.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2012, Mediterranean region: 0.02, Mediterranean region: 2.9 10 4, Mediterranean region: 0.67, Mediterranean region: 6.09 10 3, Mediterranean region: 1.87 10 3, Mediterranean region: 2236, Mediterranean region: 10.4, Mediterranean region: -0.06.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2013, Mediterranean region: 0.01, Mediterranean region: 3.0 10 4, Mediterranean region: 0.66, Mediterranean region: 6.06 10 3, Mediterranean region: 1.86 10 3, Mediterranean region: 2228, Mediterranean region: 13.9, Mediterranean region: 0.20.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2014, Mediterranean region: 0.08, Mediterranean region: 2.9 10 4, Mediterranean region: 0.65, Mediterranean region: 6.52 10 3, Mediterranean region: 2.11 10 3, Mediterranean region: 2044, Mediterranean region: 9.0, Mediterranean region: 0.30.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2015, Mediterranean region: 0.06, Mediterranean region: 3.0 10 4, Mediterranean region: 0.66, Mediterranean region: 6.22 10 3, Mediterranean region: 1.93 10 3, Mediterranean region: 2147, Mediterranean region: 8.2, Mediterranean region: 0.26.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2016, Mediterranean region: 0.55, Mediterranean region: 3.0 10 4, Mediterranean region: 0.66, Mediterranean region: 6.32 10 3, Mediterranean region: 1.97 10 3, Mediterranean region: 2110, Mediterranean region: 8.8, Mediterranean region: 0.25.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: 2017, Mediterranean region: 0.12, Mediterranean region: 3.0 10 4, Mediterranean region: 0.65, Mediterranean region: 6.08 10 3, Mediterranean region: 1.83 10 3, Mediterranean region: 2186, Mediterranean region: 9.2, Mediterranean region: 0.12.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: January, Mediterranean region: 0.23, Mediterranean region: 3.1 10 4, Mediterranean region: 0.63, Mediterranean region: 1.15 10 2, Mediterranean region: 3.81 10 3, Mediterranean region: 1118, Mediterranean region: 14.9, Mediterranean region: 0.14.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: February, Mediterranean region: 0.67, Mediterranean region: 3.0 10 4, Mediterranean region: 0.63, Mediterranean region: 1.15 10 2, Mediterranean region: 3.92 10 3, Mediterranean region: 1106, Mediterranean region: 14.9, Mediterranean region: 0.24.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: March, Mediterranean region: 0.29, Mediterranean region: 3.0 10 4, Mediterranean region: 0.62, Mediterranean region: 1.15 10 2, Mediterranean region: 3.87 10 3, Mediterranean region: 1104, Mediterranean region: 11.9, Mediterranean region: 0.26.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: April, Mediterranean region: 0.70, Mediterranean region: 3.1 10 4, Mediterranean region: 0.64, Mediterranean region: 1.13 10 2, Mediterranean region: 3.91 10 3, Mediterranean region: 1137, Mediterranean region: 15.4, Mediterranean region: 0.18.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: May, Mediterranean region: 1.02, Mediterranean region: 3.2 10 4, Mediterranean region: 0.63, Mediterranean region: 1.20 10 2, Mediterranean region: 4.43 10 3, Mediterranean region: 1064, Mediterranean region: 12.4, Mediterranean region: 0.21.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: June, Mediterranean region: 1.14, Mediterranean region: 3.2 10 4, Mediterranean region: 0.61, Mediterranean region: 1.19 10 2, Mediterranean region: 4.18 10 3, Mediterranean region: 1041, Mediterranean region: 12.9, Mediterranean region: 0.15.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: July, Mediterranean region: 1.41, Mediterranean region: 3.1 10 4, Mediterranean region: 0.60, Mediterranean region: 1.19 10 2, Mediterranean region: 4.01 10 3, Mediterranean region: 1017, Mediterranean region: 28.2, Mediterranean region: -0.07.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: August, Mediterranean region: 1.87, Mediterranean region: 2.9 10 4, Mediterranean region: 0.59, Mediterranean region: 1.22 10 2, Mediterranean region: 4.14 10 3, Mediterranean region: 987, Mediterranean region: 11.9, Mediterranean region: -0.02.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: September, Mediterranean region: 1.51, Mediterranean region: 2.9 10 4, Mediterranean region: 0.60, Mediterranean region: 1.23 10 2, Mediterranean region: 4.18 10 3, Mediterranean region: 994, Mediterranean region: 12.8, Mediterranean region: 0.13.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: October, Mediterranean region: 0.12, Mediterranean region: 2.8 10 4, Mediterranean region: 0.62, Mediterranean region: 1.26 10 2, Mediterranean region: 4.46 10 3, Mediterranean region: 998, Mediterranean region: 14.9, Mediterranean region: 0.12.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: November, Mediterranean region: 0.10, Mediterranean region: 2.7 10 4, Mediterranean region: 0.62, Mediterranean region: 1.27 10 2, Mediterranean region: 4.90 10 3, Mediterranean region: 997, Mediterranean region: 14.3, Mediterranean region: 0.41.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), Mediterranean region: December, Mediterranean region: 1.07, Mediterranean region: 3.0 10 4, Mediterranean region: 0.61, Mediterranean region: 1.16 10 2, Mediterranean region: 3.89 10 3, Mediterranean region: 1079, Mediterranean region: 14.1, Mediterranean region: 0.32.
Table 2: Network indices (Diameter, density, transitivity, shortest path (mean and standard deviation), small worldness, scale-free property, degree correlation) calculated from the networks covering PACA and estimated in three temporal contexts: the entire period 2011-2017, yearly time periods from 2011 to 2017 and monthly time periods.

Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: Diam, PACA: Dens, PACA: Trans, PACA: S P (mean), PACA: S P (sd), PACA: SW, PACA: S F, PACA: D C.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2011-2017, PACA: 6.06 10 3, PACA: 2.51 10 3, PACA: 0.99, PACA: 2.57 10 4, PACA: 1.00 10 4, PACA: 7813, PACA: 19.2, PACA: -0.85.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2012, PACA: 2 . 22 10 3, PACA: 9 . 9 10 4, PACA: 0.97, PACA: 6 10 4, PACA: 1 . 7 10 4, PACA: 3287.37, PACA: 21.50, PACA: -0.88.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2013, PACA: 2 . 42 10 3, PACA: 1 . 01 10 3, PACA: 0.98, PACA: 6 . 5 10 4, PACA: 1 . 8 10 4, PACA: 3069.76, PACA: 23.71, PACA: -0.91.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2014, PACA: 4 . 23 10 3, PACA: 10 3, PACA: 0.98, PACA: 7 . 3 10 4, PACA: 2 . 2 10 4, PACA: 2717.58, PACA: 24.56, PACA: -0.92.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2015, PACA: 2 . 92 10 3, PACA: 1 . 02 10 3, PACA: 0.99, PACA: 7 . 2 10 4, PACA: 2 . 2 10 4, PACA: 2789.31, PACA: 27.09, PACA: -0.92.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2016, PACA: 4 . 18 10 3, PACA: 1 . 01 10 3, PACA: 0.98, PACA: 8 10 4, PACA: 2 . 5 10 4, PACA: 2470.12, PACA: 19.29, PACA: -0.92.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: 2017, PACA: 2 . 46 10 3, PACA: 1 . 01 10 3, PACA: 0.98, PACA: 5 . 9 10 4, PACA: 1 . 6 10 4, PACA: 3348.41, PACA: 17.51, PACA: -0.89.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: January, PACA: 2.76, PACA: 1 . 8 10 3, PACA: 0.69, PACA: 3 . 03 10 3, PACA: 9 . 2 10 4, PACA: 462.54, PACA: 6.84, PACA: -0.66.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: February, PACA: 4.13, PACA: 1 . 64 10 3, PACA: 0.73, PACA: 3 . 35 10 3, PACA: 1 . 09 10 3, PACA: 439.54, PACA: 8.23, PACA: -0.6.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: March, PACA: 0.57, PACA: 1 . 71 10 3, PACA: 0.7, PACA: 2 . 18 10 3, PACA: 6 . 9 10 4, PACA: 651.63, PACA: 22.3, PACA: -0.84.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: April, PACA: 1 . 34 10 2, PACA: 1 . 69 10 3, PACA: 0.99, PACA: 2 . 81 10 4, PACA: 8 . 8 10 4, PACA: 712.56, PACA: 43.44, PACA: -0.98.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: May, PACA: 0.37, PACA: 1 . 86 10 3, PACA: 0.84, PACA: 1 . 73 10 3, PACA: 5 . 7 10 4, PACA: 984.96, PACA: 46.82, PACA: -0.93.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: June, PACA: 5.05, PACA: 1 . 79 10 3, PACA: 0.7, PACA: 5 . 28 10 3, PACA: 2 . 04 10 3, PACA: 270.61, PACA: 6.96, PACA: -0.64.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: July, PACA: 5.02, PACA: 1 . 84 10 3, PACA: 0.71, PACA: 6 . 85 10 3, PACA: 2 . 58 10 3, PACA: 211.02, PACA: 7.92, PACA: -0.64.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: August, PACA: 5.1, PACA: 1 . 84 10 3, PACA: 0.71, PACA: 5 . 25 10 3, PACA: 2 . 21 10 3, PACA: 274.57, PACA: 6.48, PACA: -0.66.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: September, PACA: 5.1, PACA: 1 . 84 10 3, PACA: 0.64, PACA: 2 . 57 10 3, PACA: 7 . 6 10 4, PACA: 505.03, PACA: 6.46, PACA: -0.73.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: October, PACA: 1 . 11 10 2, PACA: 1 . 87 10 3, PACA: 0.99, PACA: 1 . 83 10 3, PACA: 5 . 3 10 4, PACA: 1101.63, PACA: 25.46, PACA: -0.92.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: November, PACA: 8 . 23 10 3, PACA: 1 . 72 10 3, PACA: 0.95, PACA: 1 . 68 10 3, PACA: 5 . 1 10 4, PACA: 1147.04, PACA: 29.41, PACA: -0.89.
Según Spatiotemporal large-scale networks shaped by air mass movements (2019), PACA: December, PACA: 1.55, PACA: 1 . 8 10 3, PACA: 0.73, PACA: 2 . 69 10 3, PACA: 8 . 1 10 4, PACA: 548.04, PACA: 7.08, PACA: -0.7.
Qualitatively, the indices provided in Tables 1 and 2 are overall more variable for the monthly spatiotemporal trajectory-based networks than for the yearly ones. Thus, focusing in what follows on the monthly networks, we investigate possible seasonal patterns by using the complete-linkage hierarchical clustering method (Ferreira and Hitchcock, 2009). We applied the clustering using the Euclidean distance over the 8-dimensional space formed by the 8 indices provided in Tables 1 and 2.

For the Mediterranean region, the dendogram in Figure 5(a) can be used to identify four distinctive periods: summer months (June and July), winter months (January, February, March, April), fall months (August, September, October, November) and a set of transition months (May and December) surrounding the winter months. The spatial networks derived from this clustering are shown in Figure 5(b-e), which displays clear differences in the connectivity patterns even if one observes similarities between the networks for winter months and the surrounding transition months (winter and transition months are precisely in the same dendogram cluster if one increases the cut-off). The main differences are observed

in the northwestern part of the Mediterranean basin with, in particular, increased connectivities in the North of Italy in Winter, in the South of France and the East of Spain in Summer, between Spain and Algeria / Morocco in Summer, and along the eastern Mediterranean coast in Summer.

As shown by Figure 6(a), summer months are characterized by high diameter and density, low values of transitivity, small-worldness and the lowest values of degree correlation. Winter months have lower diameter and show high values of small-worldness due to its high values of clustering and low values of average shortest path distances. Fall months have lower values of density and small-worldness due to its low values of clustering and high values of average shortest path distances. Finally, the group of transition months show high values of density and degree correlation.

For PACA, the dendogram in Figure 7(a) can be used to identify three distinctive periods: summer months (from June to August), winter and spring months (from December to April, plus September that can be considered as an outlier from a chronological viewpoint) and a set of transition months between the two previous periods (May, October and November).

Figure 7(b-d) illustrates the differences between the networks derived from this clustering. The summer network is largely more connected than the two other networks, and the transition months, surprisingly, do not lead to intermediate connectivities but to the lowest connectivities. Based on Figure 6(b), the group of summer months is characterized by a high diameter, density and average shortest path, low values of transitivity, small-worldness and the lowest degree correlations (yet still negative). Winter and spring months have significantly lower diameter, density and average shortest path distances. Finally, the group of transition months show the highest values of small-worldness, due to their high values of clustering and low values of average shortest path distances.

Figure 5: (a): Dendrogram of the months obtained from a hierarchical cluster analysis of the Mediterranean spatiotemporal network based on the monthly dissimilarities of the indices presented in Table 1. (b), (c), (d) and (e): Networks corresponding to the four identified clusters where one displayed only the edges between the nodes connected more than 10 days per month via the air mass trajectories.

<!-- image -->

<!-- image -->

(b) PACA

Figure 6: Boxplot for the different indices (Diameter, density, transitivity, shortest path (mean), small worldness, degree correlation) obtained from (a) the four clusters identified for the Mediterranean region (see Figure 5) and (b) the three clusters for PACA (see Figure 7).

Figure 7: (a): Dendrogram of the months obtained from a hierarchical cluster analysis of the PACA spatio-temporal network based on the monthly dissimilarities of the indices presented in Table 2. (b), (c) and (d): Networks corresponding to the three identified clusters where one displayed only the edges between the nodes connected more than 10 days per month via the air mass trajectories.

<!-- image -->

## 5. Discussion

We presented a framework for estimating and characterizing spatial and spatio-temporal networks generated by trajectory data. The development of this framework was motivated by the study of networks resulting from the movement of air masses sampled over long time periods and large spatial scales. Thus, in the application, we investigated the tropospheric connectivities across the Mediterranean basin and the French region PACA, and their variations through years and months. Our approach could be applied to diverse phenomena, from which trajectories can be observed. For instance, one could estimate networks generated by the movement of animals on the landscape scale based on animal trajectories observed with GPS devices (Bastille-Rousseau et al., 2018). This would allow the characterization of connectivity between different landscape components. Sampled trajectories of humans, sampled transports of specific goods (such as plant material) and sampled trajectories of knowledge in social communities (that cannot be exhaustively observed) could also be used to estimate networks in other applied settings.

In Section 2.3, we proposed diverse measures of connectivity with different underlying (physical or biological) interpretations. Thus, the analyst can adapt the connectivity measure to the mechanistic processes he investigates. In the application section, we only used the contact-based connectivity. Comparisons of contact-based, length-based and duration-based connectivities, not shown in this manuscript, led to little variations for the two case studies considered in this article. However, the use of covariates such as local rainfall and air-mass altitude for defining connectivities, as proposed in Section 2.3, is expected to potentially impact the inferred networks and deserves to be explored. This perspective would be particularly relevant in the context of aerobiology: e.g., the airborne transport of organic particles, such as bacteria and fungal spores, can be influenced by rainfall favoring the deposition of these particles (Morris et al., 2017).

In statistics, we are not only interested in point estimation, but also in the assessment of estimation uncertainties. In this paper, we however, focused on connectivity estimation, even if quantifying the estimation variance could have been useful for more rigorously investigating temporal variation in connectivities. Formally, the connectivity measures that we defined are integrals. Hence, results on integral numerical approximations (e.g., midpoint, trapezoidal or Monte Carlo integration) can be exploited to assess errors or variances of the connectivity estimates (Davis and Rabinowitz, 2007; Caflisch, 1998; Geweke, 1996). However, for this assessment, one should ideally take into account dependencies between connectivity estimates for different pairs of nodes, which is not trivial. Further in-depth methodological developments are required to tackle this issue.

To more finely estimate connectivity, and its uncertainty, one could also take into account, if relevant, the uncertainty about the trajectories themselves. For example, when observed trajectories are smoothed versions of actual trajectories (as it is likely the case for air-mass trajectories calculated with HYSPLIT ) or when the trajectories are partially observed and rather erratic, (i) a probabilistic model grounded on, for instance, a stochastic differential equation, could be used to reconstruct probable trajectories and (ii) the connectivity would be estimated from these reconstructed trajectories. Obviously, step (ii) should

incorporate the uncertainty about the trajectory reconstruction impacted by an eventual preliminary step consisting in estimating the parameters of the above-mentioned probabilistic model.

Concerning the application treated in this article, we observed distinct seasonal patterns in the temporal variation of the networks covering the Mediterranean coastline and PACA. In the former case, the networks corresponding to the four clusters shown in Figure 5(b-e) exhibit different spatial patterns of hubs (in terms of location and size) and different trends in the main connectivity directions. In the latter case, the differences between the three networks identified with the clustering approach are mostly related to connectivity amplitude. It would be interesting to explore whether this observation made at two very different spatial scales and resolutions generally holds by studying regions of size similar to PACA all along the Mediterranean coastline.

In the long-term context of our applied research projects connected to aerobiology, the construction and exploration of networks generated by air-mass movements are a way to unravel epidemiological dynamics (and the resulting genetic patterns) of microbial pathogens disseminated at long distance via air movements in the troposphere (see Leyronas et al., 2018, for a proof of concept). Indeed, even if the pathogen is not explicitly taken into account by the framework proposed in this article, the description of connectivities that it offers provides us a proxy of airborne pathogen movements over long temporal terms and large spatial scales. This proxy is a mean to understand pathogen transportation and to anticipate its long distance dissemination. Specifically, network indices such as those calculated in this article can be associated with particular epidemiological properties such as the probability of long-distance transport of pathogens (Moslonka-Lefebvre et al., 2011; Jeger et al., 2007; Pautasso and Jeger, 2014). For instance, for plant pathogens, recent studies (Nicolaisen et al., 2017; Bowers et al., 2013; Aho et al., 2019) showed that airborne populations of bacteria and fungi are rather constant across the years, while higher diversity can be observed in different seasons. This statement resonates with our analyses where we observed clear seasonal signals in the estimated monthly spatiotemporal networks in Section 4.3 whereas the yearly signals were less obvious.

Finally, the networks estimated using our approach could be a basis for developing epidemiological models (explicitly handling the pathogen) incorporating long-distance dissemination conditional on recurrent air-mass movements. Such models could be exploited to set up surveillance strategies for early warning and epidemic anticipation in order to help reduce the impacts of airborne pathogens on human health, agricultural production and ecosystem functioning (Mundt et al., 2009).

## Acknowledgments

This research was funded by the SPREE project from the French National Research Agency (grant n 0 ANR-17-CE32-0004-01) and the PHYTOSENTINEL project (grant n 0 IB-2019-SPE). The authors thank Lo¨ ıc Houde for his technical assistance in the calculation of trajectories with HYSPLIT .

## References

- Aciego, S., Riebe, C., Hart, S., Blakowski, M., Carey, C., Aarons, S., Dove, N., Botthoff, J., Sims, K., Aronson, E., 2017. Dust outpaces bedrock in nutrient supply to montane forest ecosystems. Nature Communications 8, 14800.
- Aho, K., Weber, C., Christner, B., Vinatzer, B., Morris, C., Joyce, R., Failor, K., Werth, J., BaylessEdwards, A., Schmale III, D., 2019. Spatiotemporal patterns of microbial composition and diversity in precipitation. Ecological Monographs .
- Armon, M., Dente, E., Smith, J.A., Enzel, Y., Morin, E., 2018. Synoptic-scale control over modern rainfall and flood patterns in the levant drylands with implications for past climates. Journal of Hydrometeorology 19, 1077-1096.
- Aylor, D.E., 1990. The role of intermittent wind in the dispersal of fungal pathogens. Annual Review of Phytopathology 28, 73-92.
- Barab´ asi, A.L., Albert, R., 1999. Emergence of scaling in random networks. Science 286, 509-512.
- Barab´ asi, A.L., Bonabeau, E., 2003. Scale-free networks. Scientific American 288, 60-69.
- Barab´ asi, A.L., et al., 2016. Network science. Cambridge University Press.
- Barth´ elemy, M., 2014. Spatial Networks. Springer.
- Bastille-Rousseau, G., Douglas-Hamilton, I., Blake, S., Northrup, J.M., Wittemyer, G., 2018. Applying network theory to animal movements to identify properties of landscape space use. Ecological Applications 28, 854-864.
- Bogawski, P., Borycka, K., Grewling, /suppress L., Kasprzyk, I., 2019. Detecting distant sources of airborne pollen for Poland: Integrating back-trajectory and dispersion modelling with a satellite-based phenology. Science of The Total Environment 689, 109-125.
- Bowers, R.M., Clements, N., Emerson, J.B., Wiedinmyer, C., Hannigan, M.P., Fierer, N., 2013. Seasonal variability in bacterial and fungal diversity of the near-surface atmosphere. Environmental Science &amp; Technology 47, 12097-12106.
- Caflisch, R.E., 1998. Monte carlo and quasi-monte carlo methods. Acta Numerica 7, 1-49.
- Chen, Y., Luo, Y., 2018. Analysis of paths and sources of moisture for the south China rainfall during the presummer rainy season of 1979-2014. Journal of Meteorological Research 32, 744-757.
- Colon-Perez, L.M., Couret, M., Triplett, W., Price, C.C., Mareci, T.H., 2016. Small worldness in dense and weighted connectomes. Frontiers in Physics 4, 14.
- Davis, P.J., Rabinowitz, P., 2007. Methods of numerical integration. Courier Corporation.

- Ferreira, L., Hitchcock, D.B., 2009. A comparison of hierarchical methods for clustering functional data. Communications in Statistics-Simulation and Computation 38, 1925-1949.
- Geweke, J., 1996. Monte carlo simulation and numerical integration. Handbook of Computational Economics 1, 731-800.
- Hiraoka, S., Miyahara, M., Fujii, K., Machiyama, A., Iwasaki, W., 2017. Seasonal analysis of microbial communities in precipitation in the greater Tokyo area Japan. Frontiers in Microbiology 8, 1506.
- Holme, P., Saram¨ aki, J., 2012. Temporal networks. Physics Reports 519, 97-125.
- Hondula, D.M., Sitka, L., Davis, R.E., Knight, D.B., Gawtry, S.D., Deaton, M.L., Lee, T.R., Normile, C.P., Stenger, P.J., 2010. A back-trajectory and air mass climatology for the Northern Shenandoah Valley, USA. International Journal of Climatology 30, 569-581.
- Jeger, M.J., Pautasso, M., Holdenrieder, O., Shaw, M.W., 2007. Modelling disease spread and control in networks: implications for plant sciences. New Phytologist 174, 279-297.
- Khaniabadi, Y.O., Daryanoosh, S.M., Amrane, A., Polosa, R., Hopke, P.K., Goudarzi, G., Mohammadi, M.J., Sicard, P., Armin, H., 2017. Impact of Middle Eastern Dust storms on human health. Atmospheric Pollution Research 8, 606-613.
- Leyronas, C., Morris, C.E., Choufany, M., Soubeyrand, S., 2018. Assessing the aerial interconnectivity of distant reservoirs of sclerotinia sclerotiorum. Frontiers in Microbiology 9, 2257.
- Li, W., Lin, Y., Liu, Y., 2007. The structure of weighted small-world networks. Physica A: Statistical Mechanics and its Applications 376, 708-718.
- Liu, B., Ma, Y., Gong, W., Zhang, M., Yang, J., 2018a. Study of continuous air pollution in winter over Wuhan based on ground-based and satellite observations. Atmospheric Pollution Research 9, 156-165.
- Liu, G., Wong, L., Chua, H.N., 2009. Complex discovery from weighted ppi networks. Bioinformatics 25, 1891-1897.
- Liu, T., Marlier, M.E., DeFries, R.S., Westervelt, D.M., Xia, K.R., Fiore, A.M., Mickley, L.J., Cusworth, D.H., Milly, G., 2018b. Seasonal impact of regional outdoor biomass burning on air pollution in three Indian cities: Delhi, Bengaluru, and Pune. Atmospheric Environment 172, 83-92.
- Liu, Y.Y., Slotine, J.J., Barab´ asi, A.L., 2011. Controllability of complex networks. Nature 473, 167.
- Mahura, A.G., Korsholm, U.S., Baklanov, A.A., Rasmussen, A., 2007. Elevated birch pollen episodes in Denmark: contributions from remote sources. Aerobiologia 23, 171.
- Margosian, M.L., Garrett, K.A., Hutchinson, J.S., With, K.A., 2009. Connectivity of the American agricultural landscape: assessing the national risk of crop pest and disease spread. BioScience 59, 141-151.

- Moroz, B.E., Beck, H.L., Bouville, A., Simon, S.L., 2010. Predictions of dispersion and deposition of fallout from nuclear testing using the NOAA-HYSPLIT meteorological model. Health Physics 99.
- Morris, C.E., Sands, D.C., Vinatzer, B.A., Glaux, C., Guilbaud, C., Buffiere, A., Yan, S., Dominguez, H., Thompson, B.M., 2008. The life history of the plant pathogen Pseudomonas syringae is linked to the water cycle. The ISME Journal 2, 321.
- Morris, C.E., Soubeyrand, S., Bigg, E.K., Creamean, J.M., Sands, D.C., 2017. Mapping rainfall feedback to reveal the potential sensitivity of precipitation to biological aerosols. Bulletin of the American Meteorological Society 98, 1109-1118.
- Moslonka-Lefebvre, M., Finley, A., Dorigatti, I., Dehnen-Schmutz, K., Harwood, T., Jeger, M.J., Xu, X., Holdenrieder, O., Pautasso, M., 2011. Networks in plant epidemiology: from genes to landscapes, countries, and continents. Phytopathology 101, 392-403.
- Mundt, C.C., Sackett, K.E., Wallace, L.D., Cowger, C., Dudley, J.P., 2009. Aerial dispersal and multiplescale spread of epidemic disease. EcoHealth 6, 546-552.
- Newman, M.E., 2001. Scientific collaboration networks. ii. shortest paths, weighted networks, and centrality. Physical Review E 64, 016132.
- Newman, M.E., 2003. The structure and function of complex networks. SIAM Review 45, 167-256.
- Nicolaisen, M., West, J.S., Sapkota, R., Canning, G.G., Schoen, C., Justesen, A.F., 2017. Fungal communities including plant pathogens in near surface air are similar across Northwestern Europe. Frontiers in Microbiology 8, 1729.
- Opsahl, T., Panzarasa, P., 2009. Clustering in weighted networks. Social Networks 31, 155-163.
- Pautasso, M., Jeger, M.J., 2014. Network epidemiology and plant trade networks. AoB Plants 6.
- Pautasso, M., Xu, X., Jeger, M.J., Harwood, T.D., Moslonka-Lefebvre, M., Pellis, L., 2010. Disease spread in small-size directed trade networks: the role of hierarchical categories. Journal of Applied Ecology 47, 1300-1309.
- P´ erez, I.A., Artuso, F., Mahmud, M., Kulshrestha, U., S´ anchez, M.L., Garc´ ıa, M., 2015. Applications of air mass trajectories. Advances in Meteorology 2015.
- Rabinowitz, J.L., Lupo, A.R., Market, P.S., Guinan, P.E., 2019. An investigation of atmospheric rivers impacting heavy rainfall events in the North-Central Mississippi River Valley. International Journal of Climatology .
- Rolph, G., Ngan, F., Draxler, R., 2014. Modeling the fallout from stabilized nuclear clouds using the HYSPLIT atmospheric dispersion model. Journal of Environmental Radioactivity 136, 41-55.

- Sady´ s, M., Skjøth, C.A., Kennedy, R., 2014. Back-trajectories show export of airborne fungal spores (Ganoderma sp.) from forests to agricultural and urban areas in England. Atmospheric Environment 84, 88-99.
- ˇ Sauliene, I., Veriankaite, L., 2006. Application of backward air mass trajectory analysis in evaluating airborne pollen dispersion. Journal of Environmental Engineering and Landscape Management 14, 113-120.
- Stein, A., Draxler, R.R., Rolph, G.D., Stunder, B.J., Cohen, M., Ngan, F., 2015. NOAA's HYSPLIT atmospheric transport and dispersion modeling system. Bulletin of the American Meteorological Society 96, 2059-2077.
- Strogatz, S.H., 2001. Exploring complex networks. Nature 410, 268.
- Talbi, A., Kerchich, Y., Kerbachi, R., Boughedaoui, M., 2018. Assessment of annual air pollution levels with PM1, PM2.5, PM10 and associated heavy metals in Algiers, Algeria. Environmental Pollution 232, 252-263.
- Wang, H., Yang, X., Ma, Z., 2010. Long-distance spore transport of wheat stripe rust pathogen from Sichuan, Yunnan, and Guizhou in southwestern China. Plant Disease 94, 873-880.
- West, D.B., et al., 1996. Introduction to graph theory. volume 2. Prentice Hall Upper Saddle River, NJ.

## Appendices

Figure 8: Boxplot for the distance between the points within the categories. The categories correspond to the intensity of connection between the nodes (a) of the Mediterranean region and (b) PACA. The letters are chosen according to the resulting p-values of Wilcoxon signed-rank test, based on the significance level of 0.05, to compare the distribution of the distances between every couple of the categories in Figure 8. The categories having the same letter doesn't have a significant difference between them.

<!-- image -->

<!-- image -->

Angle

## (a) Mediterranean region

<!-- image -->

Angle

(b) PACA

Figure 9: Circular histogram illustrating the direction of the connectivities between the nodes whithin the categories (a) of the Mediterranean region and (b) PACA.