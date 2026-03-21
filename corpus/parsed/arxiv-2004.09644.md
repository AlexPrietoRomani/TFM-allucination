---
id: arxiv-2004.09644
title: Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations
year: 2020
country: Internacional
source: ArXiv (q-bio.PE, cond-mat.stat-mech, physics.soc-ph)
doc_type: Artículo científico
language: en
tags:
  - Phytophthora
  - patógenos vegetales
  - dispersión de esporas
  - artículo científico
  - ArXiv
  - agronomía de campo
---

1

## Site-bond percolation solution to preventing the propagation of Phytophthora zoospores on plantations

J. E. Ram´ ırez ∗ 1,2 , C. Pajares 1,2 , M. I. Mart´ ınez 3 , R. Rodr´ ıguez Fern´ andez 2

Molina-Gayosso , J. Lozada-Lechuga , and A. Fern´ andez T´ ellez

, E. 4 4 3

Departamento de F´ ısica de Part´ ıculas, Universidad de Santiago de Compostela, E-15782 Santiago de Compostela, Espa˜ na

2 Instituto Galego de F´ ısica de Altas Enerx´ ıas, Universidad de Santiago de Compostela, E-15782 Santiago de Compostela, Espa˜ na

3 Facultad de Ciencias F´ ısico Matem´ aticas, Benem´ erita Universidad Aut´ onoma de Puebla, Apartado Postal 165, 72000 Puebla, Pue., M´ exico

4 Universidad Polit´ ecnica de Puebla, Tercer carril del Ejido Serrano, 72640, Juan C. Bonilla, Pue., M´ exico

## Abstract

We propose a strategy based on the site-bond percolation to minimize the propagation of Phytophthora zoospores on plantations, consisting in introducing physical barriers between neighboring plants. Two clustering processes are distinguished: i) one of cells with the presence of the pathogen, detected on soil analysis; and ii) that of diseased plants, revealed from a visual inspection of the plantation. The former is well described by the standard site-bond percolation. In the latter, the percolation threshold is fitted by a Tsallis distribution when no barriers are introduced. We provide, for both cases, the formulae for the minimal barrier density to prevent the emergence of the spanning cluster. Though this work is focused on a specific pathogen, the model presented here can also be applied to prevent the spreading of other pathogens that disseminate, by other means, from one plant to the neighboring ones. Finally, the application of this strategy to three types of commercialy important Mexican chili plants is also shown.

## 1 Introduction

The genus Phytophthora (from Greek, meaning phyto , 'plant,' and phthora , 'destroyer' [1, 2, 3]) is one of the most aggressive phytopathogens that attack the roots of plants and trees in every corner of the world. The diseases caused by exposition to Phytophthora generate tremendous economical losses in agronomy and forestry. For example, P. capsici cause considerable damage in plantations of chili, cucumber, zucchini, etc. [4, 5, 6]. The same occurs with tomato and potato plantations, which are affected by P. infestants [7, 8, 9]. P. cinnamomi harms avocado plantations [10, 11, 12] and, together with P. cambivora , produce the ink disease which is widely distributed along Europe [13, 14, 15]. Phytophthora has caused significant devastation on Galician chestnut and the Australian eucalypt, putting them close to extinction [16, 17, 18].

From a biological perspective, Phytophthora shares morphological characteristics with true fungi (Eumycota) such as mycelial growth or the dispersion of spores of mitotic or asexual origin. Its form of locomotion, by means of flagella [19], is a distinctive feature that enables them to have a great impact on the plant kingdom as phytopathogens. They can disperse through soil moisture or water films including those on the surface of the plants. These motile zoospores, emerging from mature sporangia in quantities of 20 to 40, can swim chemotactically towards the plants [19, 20, 21]. When they reach the surface of the roots they lose their flagella, encyst in the host and form a germination tube through which they penetrate the surface of the plant [22, 23]. Moreover, many species of Phytophthora can persist as saprophytes if the environmental

∗ Corresponding Author: jerc.fis@gmail.com

conditions are not appropriate, but become parasitic in the presence of susceptible hosts [21]. Due to the physiology of the oomycetes most of the fungicides have no effect on them [1, 24, 25, ? ]. Therefore, research on non-chemical strategies that minimize or eliminate the propagation of the pathogen is necessary.

It has been noticed that for some type of plants not all individuals manifest the disease after the exposition to a specific pathogen. We take advantage of this fact to define the pathogen susceptibility ( χ ) of a plant type as the fraction of individuals that get the disease. It can be interpreted as the probability that a sample of the plant gets sick after being exposed to the pathogen, and can be measured in a laboratory or a greenhouse under controlled conditions, or by direct observation in the plantation.

On the other hand, one of the models widely used to describe physical processes is the site-bond percolation, that has been applied to study the spread of diseases [26, 27, 28, 29]. It is a generalization of the site and bond percolation that consists in determining both site and bond occupation probabilities needed to the emergence of a spanning cluster of sites connected by bonds. In this context, two nearest-neighboring sites do not belong to the same cluster if there is not a bond connecting them. In this work, occupied sites in the percolation system represent susceptible plants through which the propagation process can occur, and bonds represent the direction of propagation of the pathogen.

It is worth mentioning that zoospores move directly to neighboring plants. Placing physical barriers between them (that is, perpendicularly to the direction of propagation) can help to decrease the opportunity for root to root pathogen transmission. For instance, the Australian government recommends using physical root barriers such as impermeable membranes made of high-density polyethylene [30, 31, 32, 33], which have been used in agriculture and horticulture. Trenches filled with compost (a mixture of manure and crop residues) in addition with biological control agents (for example Trichoderma spp. or Bacillus spp. ) could be used as a good barrier against soil-borne pathogens like oomycetes and fungi [34, 35, 36]. With the use of barriers it could be possible to fragment the spanning cluster of susceptible plants, preventing the propagation of the pathogen. Thus, if the pathogen susceptibility of the plant is known, one can try to determine the minimal density of barriers ( p w ) that stops the propagation of the pathogen. However, this density does not necessarily corresponds to the bond percolation threshold.

Although this paper is motivated by the important problem caused by the propagation of Phytophthora , which is still unsolved nowadays, the strategy presented here can be adapted to mitigate the spread of other diseases. There exist other phytopathogens relevant to agronomy that disseminate over neighboring plants by, for example, walking [37], rain splashing [38, 39, 40], swimming [41], etc.; such as the red spider mites, leaf rust, Pythium (with similar propagation mechanisms as Phytophthora ) among others. In practice one only needs to find a suitable physical barrier that efficiently avoids nearest-neighbor propagation of the specific phytopathogen.

In Sec. 2, we introduce the site-bond percolation model for the pathogen-plant interaction and the role of the barriers. Section 3 describes the simulation method used in this work and provides the simulation rules for the clustering process. It also shows an example of the simulation process and describes the data analysis method. In Sec. 4, we report the critical curves as a function of the initial percentage of inoculated soil for the barrier-free case. These curves indicate the maximum value of the pathogen susceptibility that guarantees a spanning cluster of diseased plants is not formed even if the soil is completely infested with the pathogen. Additionally, we provide the empirical formulae to determine the density of barriers that prevents the emergence of the spanning cluster when the susceptibility exceeds the aforementioned critical value. In Sec. 5, we show the application of this method to three varieties of Mexican chili plants with high comercial value. Finally, Section 6 presents the conclusions of this work.

## 2 Model

The plantation is modeled as a simple two-dimensional lattice (square, triangular, and honeycomb) wherein each site represents a plant. The lattice spacing is chosen as the maximum displacement length that the pathogen can travel before entering a state of dormancy or before dying due to starvation. This condition ensures the pathogen can only move to the nearest neighbor cells as depicted in Fig. 1. We assume a site with an active pathogen will propagate the disease to all nearest-neighbor sites.

Here, the pathogen susceptibility plays an important role since resistant plants can act as a natural barrier for susceptible plants by locally containing the propagation process, i. e. a resistant plant does not disseminate the disease. In our model resistant plants are uniformly distributed on the system since it is not possible to determine in advance which seeds will grow into resistant or susceptible plants. In this

Figure 1: Possible barrier locations (solid lines), directions of microorganism propagation (dotted lines), and modification of the nearest neighbor meaning induced by inoculated cells with a resistant plant in square [(a) and (d)], triangular [(b) and (e)], and honeycomb [(c) and (f)] lattices. Bottom figures show susceptible plants (green triangle) with a neighboring resistant plant in an inoculated cell ( red triangle). As a consequence of the microorganism propagation (red arrows), the nearest neighbor definition (black arrows) is modified since the site with the susceptible plant can now be linked to farther sites (blue arrows).

<!-- image -->

way the pathogen susceptibility plays the role of the occupation probability in the traditional treatment of percolation theory.

Another essential variable that needs to be considered is the initial fraction of inoculated cells at the beginning of the propagation process which is denoted by I . In our model these cells are distributed uniformly over the lattice. This parameter is relevant to amalgamate adjacent-disjoint clusters promoting a favorable environment for the formation of a spanning cluster of diseased plants or of cells with the presence of the pathogen [42]. Additionally, we put barriers that are randomly distributed in the lattice. These are placed perpendicularly to the direction of propagation of the pathogen (see Fig. 1), and its primary function is to prevent the pathogen from reaching neighbor sites. Note that all possible barriers that can be placed form the dual lattice to that formed by all possible directions of propagation of the pathogen. Then the question we want to answer is: what is the minimal barrier density, in terms of χ and I , that guarantees a spanning cluster will not appear?

We distinguish two different clustering processes: i) the formation of clusters of cells with the presence of the pathogen, and ii) the formation of clusters of diseased plants. Although both processes are consequence of the propagation of the pathogen they depend in different ways on the intrinsic properties of the plants. In practice one would observe the first process if a pathogen soil test is performed while a visual inspection of the damage on the plantation would reveal the second process. In the following we refer to them as soil and plant cases respectively, and the corresponding variables will be labeled with a superscript.

In the soil case, for a lattice with N sites, the mean number of available plants 〈 N 〉 av to the propagation process is 〈 N 〉 av = Nχ . Since the susceptibility of the plant and the inoculation state of the cell are independent variables, it is necessary to take into account the mean number of inoculated cells 〈 N 〉 in with a resistant plant. This condition adds 〈 N 〉 in = N (1 -χ ) I extra available cells. Thus, the total mean number of cells where the propagation process can occur is 〈 N 〉 tot = 〈 N 〉 av + 〈 N 〉 in . Therefore, the propagation takes place in a percolating system with an effective occupation probability p soil eff = I +(1 -I ) χ . In this case, the spanning cluster emerges if p soil eff ≥ p cs , where p cs is the critical probability in the purely site percolation. Thus the desired percolation threshold is p soil eff = p cs .

The introduction of barriers in the soil case makes the system suitable to be modeled with the site-bond percolation. The critical curves as a function of the occupation probabilities of sites ( p s ) and bonds ( p b ) has been empirically fitted using [43] p b = B/ ( p s + A ), where A = ( p cb -p cs ) / (1 -p cb ), B = p cb (1 -p cs ) / (1 -p cb ), and p cb is the critical probability in the purely bond percolation. Moreover, since barriers are located in the dual lattice, the density of barriers and the bond occupation probability are related by p b + p soil w = 1, that is, the joint-set of barriers and bonds it is exactly N b . So we finally find that the critical curves for the soil

case can be written as

<!-- formula-not-decoded -->

On the other hand, for the plant case, inoculated cells with a resistant plant do not belong to the cluster of diseased plants. However, these cells play an essential role since adjacent-disjoint clusters can be amalgamated through them. This fact modifies the nearest neighbor meaning since it is then possible to link two susceptible plants separated by a distance greater than the lattice spacing (see Fig. 1), then the possibility to amalgamate adjacent-disjoint clusters is increased [42].

The main difference between the soil and plant cases is just this amalgamating role played by inoculated cells with a resistant plant at the beginning of the propagation process. In the soil case, these cells are considered as occupied sites, while in the plant case, they do not belong to any cluster; however, they can transmit the disease over neighboring susceptible plants. Schematically, this latter situation looks like a healthy plant with sick neighbors.

## 3 Simulation method

We implemented a modified version of the Newman-Ziff algorithm reported in Refs. [44, 45] to determine the percolation threshold.

Since the susceptibility condition of each plant and the cells' inoculation state are independent of each other they are stored in separate matrices in the simulation. These matrices, that we call X and I , respectively, are initially null. They are then filled according to the predefined values of χ and I . For the case with no barriers, however, only the knowledge of the inoculated cells is required to determine the percolation thresholds.

For simplicity we describe the implementation of the algorithm for a square lattice. However, this algorithm can also be used for other lattices simply changing the implementation of the nearest neighbor definition.

Each cell of the L × L matrices X and I is labeled with a progressive number M = iL + j , for the cell at row i and column j . The set of cells' labels is then N = { 0 , 1 , 2 , . . . , L 2 -1 } . On the other side, the possible propagation directions for all cells form a network with 2 L ( L -1) bonds since the system is considered as free of periodic boundary conditions. As we did with the cells, each bond is labeled with progressive numbers that form the set N b = { 0 , 1 , 2 , . . . , 2 L ( L -1) -1 } .

An initial number of inoculated cells n I is drawn from the binomial distribution B ( L 2 , I ) and then n I labels are randomly taken from the set N . The corresponding cells are the sites from which the infection process will propagate. These cells are marked by changing their state from 0 to 1. The initial distribution of susceptible plants, that is plants that will get the disease if they are exposed to the pathogen, is obtained in a similar way. Note that only the initial conditions are set so far and the propagation process has not been started so that no cells are linked yet.

To add bonds between cells the N b labels are randomly permuted and then the corresponding bonds are added one at a time until a spanning cluster is formed. It should be recalled that bonds determine the direction of propagation in this model.

To decide which bonds will connect the sites we impose rules based on the way the pathogen transports itself from site to site. Since the zoospores are capable of detecting the presence of neighboring plants, they will swim towards them as soon as they emerge from the sporangia. If a zoospore reaches a resistant plant it will either enter a latency state or die from inanition so that it won't be able to further propagate the disease. If, on the other hand, the zoospore arrives at a susceptible plant, it will attack the plant and produce new sporangia. They, in turn, will produce new zoospores that will eventually swim towards neighboring plants. Thus the rules can be stated as follows.

A bond will connect two nearest-neighbor sites if:

1. Soil case:
2. (a) Any of the sites was inoculated during the initial configuration.
3. (b) Both sites have susceptible plants.
2. Plant case:

Figure 2: Examples of possible initial configurations of a system of size L = 10. (a) Distribution of cells with susceptible (filled triangles) and resistant (empty triangles) plants. (b) Distribution of inoculated cells.

<!-- image -->

- (a) Any of the sites was inoculated during the initial configuration and the other has a susceptible plant.
- (b) Both sites have susceptible plants.

This way bonds are added one by one, and sites are connected according to the rules above, until a cluster that connects one side of the lattice to the opposite one, the so-called spanning cluster, appears. The union-find algorithm is used to connect sites. Since not every site pair can interact not every bond can connect adjacent sites. In order to identify the spanning cluster, before starting the simulation process, susceptible plants in the last and first rows are united with auxiliary labels -1 and -2, respectively. Then, the simulation process is stopped when the labels { -1,-2 } change to the same value.

The essential difference between the two cases is the role played by the inoculated cells with a resistant plant. In the soil case they become occupied sites while in the plant case they may merge disjoint clusters.

To visualize the difference between both cases consider an L = 10 system with χ = 0 . 5 and I = 0 . 4. Figure 2 shows one possible initial configuration of susceptible plants and inoculated cells before the propagation process starts.

In a system of size L = 10 there are 180 bonds. A possible random permutation of their labels is listed below:

{ 118, 63, 26, 119, 160, 22, 64, 142, 156, 126, 8, 152, 73, 127, 32, 78, 81, 170, 36, 92, 89, 123, 57, 68, 12, 33, 24, 129, 158, 46, 169, 82, 48, 147, 69, 38, 18, 56, 168, 178, 179, 164, 114, 6, 79, 42, 86, 41, 13, 52, 165, 115, 43, 85, 172, 116, 133, 11, 27, 139, 29, 15, 0, 138, 122, 40, 7, 148, 74, 71, 113, 177, 111, 135, 37, 51, 67, 9, 121, 98, 99, 35, 49, 108, 151, 53, 173, 39, 1, 5, 2, 153, 45, 146, 76, 59, 145, 143, 163, 96, 16, 104, 101, 61, 144, 28, 102, 17, 88, 31, 3, 141, 109, 77, 65, 80, 166, 106, 167, 117, 70, 130, 21, 83, 140, 20, 157, 10, 136, 161, 137, 107, 100, 150, 110, 91, 132, 128, 112, 93, 44, 149, 19, 94, 131, 154, 155, 30, 62, 171, 23, 34, 55, 4, 54, 176, 58, 75, 174, 50, 60, 125, 47, 25, 103, 134, 120, 159, 90, 84, 14, 87, 175, 124, 95, 105, 66, 72, 97, 162 } .

The bonds are added in this order until a spanning cluster appears. The entries of one of the cells a given bond can connect are given by i = /floorleft h/ (2 L -1) /floorright and j = h mod (2 L -1), where h is the bond's label and /floorleft x /floorright denotes the integer part of x . Note that the orientation of the bond is identified as horizontal if j &lt; L -2 or vertical otherwise. In addition, the value of j should be corrected for vertical bonds by subtracting L -1. Then, the cells with entries i, j and i, j + 1 are taken if the bond is horizontal; while the cells at i, j and i +1 , j are taken if the bond is vertical. Finally, if the pair taken fulfills the rules given previously they are connected using the union-find algorithm.

Figure 3 shows the networks formed by connected bonds in both cases. While in the soil case 121 bonds were added before the spanning cluster appeared, in the plant case were needed 160 bonds. Note that, although each network has its own topology, in the plant case the fundamental role for the formation of a spanning cluster is played by the modification of the nearest neighbor definition (yellow lines in Fig. 3b) introduced by the interactions between susceptible plants and inoculated cells with a resistant plant on it (dashed lines in Fig. 3b). This clearly shows the consequence of this type of interactions, namely their capacity to merge disjoint clusters of susceptible plants.

Figure 3: Spanning clusters formed in the a) soil and b) plant cases for the initial conditions of Fig. 2 and the list of bonds given in the text. Only the bonds that connect sites are shown (black lines). In the case (b), bonds connecting a resistant plant in an inoculated site to a susceptible plant are represented with dashed lines. Yellow lines show the modification of the nearest neighbor definition.

<!-- image -->

χ

Figure 4: (a) Critical curves for cluster formation over infested soil (hollow figures) and infected plants (solid figures) on triangular (triangles), square (squares) and honeycomb (circles) lattices with no barriers. Theoretical curves for the soil case (dashed lines) and the fit to the data for the plant case (continuous lines) are also shown. (b) Simulation (figures) and theoretical (lines) critical curves in the soil case for square (squares), triangular (triangles) and honeycomb (circles) lattices for several values of I : 0.0 (black), 0.1 (purple), 0.2 (green), 0.3 (cyan), 0.4 (blue) and 0.5 (red).

<!-- image -->

## 3.1 Data analysis

Using this method, we determined the probability P n that a spanning cluster appears after adding n bonds (or sites) [46] as an average over 10 4 runs for each pair ( χ, I ). Starting in χ = 1 and I = 1 we decreased their values independently in steps of ∆ χ = ∆ I = 0 . 05. Then the percolation probability is computed as P ( p ) = ∑ n B ( N,n,p ) P n where B ( N,n,p ) is the binomial distribution [44, 45], N is the total number of sites or bonds in the lattice and p is the occupation probability of sites or bonds correspondingly. Lastly, the percolation threshold is determined by solving the equation P ( p c ) = 0 . 5 [47]. To this end, the percolation probability is computed from 〈 n c 〉 /L 2 -0 . 15 to 〈 n c 〉 /L 2 + 0 . 15 in steps of ∆ p = 0 . 01. Then, P ( p ) = 0 . 5[1 + tanh(( p -p c ) / ∆ L )] is fitted to the estimated data. Here p c is the estimation of the percolation threshold and ∆ L is the width of the sigmoid transition [47].

To take finite size effects into account we also performed simulations using the system size L = 32, 64, 128, and 256. Thus the percolation threshold in the thermodynamic limit is estimated by the extrapolation of the scaling relation p c -p c ( L ) ∝ L -1 /ν , where ν is the exponent corresponding to the correlation length [48]. It is well known that the transition width ∆ L scales as a function of the system size L as ∆ L ∝ L -1 /ν [49]. From the fit of the percolation probability data, we found that ν = 4 / 3, which is in good agreement with the results reported in the literature for the percolation theory in 2D. Finally, the critical density of barriers is calculated as p w = 1 -p ∗ cb , where p ∗ cb is the bond percolation threshold as a function of χ and I .

Figure 5: Power law relation between χ , χ plant c and p plant w in the plant case when I is fixed for a) square, b) triangular, and c) honeycomb lattices. Black solid line is the identity function. The color scale indicates the value of I from I = 0 (green) up to I = 1 (blue) in steps of ∆ I =0.05.

<!-- image -->

Figure 6: Comparison between simulation results (figures) for p plant w as a function of the susceptibility and the curve proposed in Eq. (2) (solid lines) for a) square, b) triangular and c) honeycomb lattices. The color scale indicates the value of I from I = 0 (green) up to I = 1 (blue) in steps of ∆ I =0.05.

<!-- image -->

## 4 Results

Simulation results for the critical curves of both soil and plant cases with no barriers are shown in Fig. 4 a). Notably, our results for χ soil c are very well described by the parametrization p soil eff = I +(1 -I ) χ = p cs . Notice that the critical curves for χ plant c deviate from those for χ soil c for I &gt; 0 . 15. This is due to non-susceptible plants lying in inoculated cells which do not belong to the clusters and can serve as a bridge between their adjacent sites. We found that χ plant c can be well fitted by the Tsallis distribution p cs / (1 + aI/n ) n , with a =0.91 ± 0.03 and 1.40 ± 0.06 and n =2.0 ± 0.4 and 1.1 ± 0.1 for the square and triangular lattices, respectively. For the honeycomb lattice n takes a large value so we used p cs exp( -aI ) with a =0.63 ± 0.01. This behavior can be understood as the collective contribution of the interaction between susceptible plants and infected cells with a resistant plant. Note that the probability of observing this pair become higher as χ decreases and I increases, and thus, the percolating system looks like a lattice formed by regular sites and sites involving complex nearest neighbors. The main result of this analysis is the existence of a minimal susceptibility that guarantees the non-emergence of a spanning cluster of diseased plants even if all cells are inoculated, that is the value of χ plant c for I = 1. However, if χ &gt; χ soil c or χ &gt; χ plant c it is necessary to use the barrier strategy to reduce the connectedness of the lattice. In Fig. 4 b), we show the simulation results for the soil case. Notice that they are well described by Eq. (1), which corresponds to the description of the typical critical curves in the site-bond percolation with an occupation probability p soil eff . This is because in this case the infected cells are taken into account in the cluster formation process even if the plant does not become sick.

On the other hand we found, for the plants case, that the relation between χ , χ plant c and p plant w is given by the power law ( χ -χ plant c ) = α ( p plant w χ/χ plant c ) β when I is fixed, as it is shown in Fig. 5. It should be noted that both α and β depend on I . Particularly, β takes values between 0.95 and 1.18 for all lattices. Then, the critical curves for the plants case are given by

<!-- formula-not-decoded -->

which matches very well the simulation data for the square, triangular and honeycomb lattices as shown in Fig. 6 for different values of I . Table 1 shows the values of the parameters α and β (for different values of I ) given by the fit to simulation data for the square, triangular and honeycomb lattices. Moreover, in the case χ = 1, p plant w = 1 -p cb as expected since, under this condition, the system corresponds to the traditional bond percolation model.

## 5 Application to chili plantations

Application of Eq. (2) requires the knowledge of the plant's pathogen susceptibility. This quantity has been measured experimentaly as described in Ref. [42]. In general terms their method consists in sowing plants in previously sterilized soil and innoculating a fraction of the substrate with oomycetes. The pathogen is then allowed to propagate through the plantation and the presence of the pathogen is asessed for each plant. The ratio of the number of live infected plants to the total number of infected plants gives the surviving rate P . The pathogen susceptibility of the plant is then calculated as χ = 1 -P .

The reported values of the pathogen susceptibility for the varieties Arbol, Poblano and Serrano plants of chilis (which are of high commercial value un Mexico) are 1.00, 0.89 and 0.60, respectively. Putting these values into Eq. (2) we obtained the curves for p plant w as a function of I shown in Fig. 7 for a square lattice. Note that as the value of χ approaches 1, like for the Arbol and Poblano chilis, the barrier density approaches the bond percolation threshold ( p cb = 0 . 5) since in these particular cases the percolating system is very similar to the bond percolation model. On the other side, as χ approaches the site percolation threshold, like for the Serrano chili, the range of possible values for p plant w becomes larger however p plant w ( I = 1) ≈ 0 . 41 is less than 0.5. In practice this means an 18% less barriers are needed to prevent the disease propagation.

Also, as χ becomes less and less than p cs , the value of p plant w decreases until it vanishes. This point, when p plant w ( I = 1) = 0, corresponds to the intersection of the critical χ plant c curve with the vertical line I = 1 (see Fig. 4). This is just the greatest value of a plant's susceptibility that makes the barrier strategy unnecessary.

Table 1: Fit parameters for the square ( /square ), triangular ( /triangle ) and honeycomb ( © ) lattices. Error estimates in the last significant figure are indicated in parentheses.

Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0, α /square: 0.4870(9), β /square: 1.065(3), α /triangle: 0.3685(5), β /triangle: 1.132(5), α ©: 0.621(5), β ©: 1.031(8).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.05, α /square: 0.4922(8), β /square: 1.050(3), α /triangle: 0.3689(5), β /triangle: 1.099(5), α ©: 0.637(2), β ©: 1.032(3).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.1, α /square: 0.4956(6), β /square: 1.029(2), α /triangle: 0.3673(4), β /triangle: 1.077(3), α ©: 0.636(2), β ©: 1.001(3).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.15, α /square: 0.4982(5), β /square: 1.013(2), α /triangle: 0.3646(4), β /triangle: 1.051(3), α ©: 0.657(3), β ©: 1.003(5).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.2, α /square: 0.5000(4), β /square: 1.005(2), α /triangle: 0.3598(4), β /triangle: 1.032(3), α ©: 0.669(3), β ©: 0.996(5).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.25, α /square: 0.4994(2), β /square: 0.994(1), α /triangle: 0.3530(2), β /triangle: 1.029(1), α ©: 0.674(2), β ©: 0.974(4).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.3, α /square: 0.4977(3), β /square: 0.990(1), α /triangle: 0.3445(1), β /triangle: 1.024(1), α ©: 0.685(2), β ©: 0.974(3).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.35, α /square: 0.4941(4), β /square: 0.989(2), α /triangle: 0.334(1), β /triangle: 1.023(6), α ©: 0.698(3), β ©: 0.980(5).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.4, α /square: 0.4892(3), β /square: 0.991(2), α /triangle: 0.3253(2), β /triangle: 1.022(1), α ©: 0.696(2), β ©: 0.954(3).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.45, α /square: 0.4821(3), β /square: 0.996(2), α /triangle: 0.3145(2), β /triangle: 1.025(1), α ©: 0.711(2), β ©: 0.979(4).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.5, α /square: 0.4741(2), β /square: 1.003(1), α /triangle: 0.3036(3), β /triangle: 1.033(2), α ©: 0.713(1), β ©: 0.982(2).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.55, α /square: 0.4653(2), β /square: 1.013(1), α /triangle: 0.2925(4), β /triangle: 1.047(2), α ©: 0.715(2), β ©: 0.987(4).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.6, α /square: 0.4551(2), β /square: 1.025(1), α /triangle: 0.2825(3), β /triangle: 1.052(2), α ©: 0.720(1), β ©: 1.005(3).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.65, α /square: 0.4450(1), β /square: 1.036(1), α /triangle: 0.2721(3), β /triangle: 1.066(2), α ©: 0.717(2), β ©: 1.016(4).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.7, α /square: 0.4342(3), β /square: 1.050(2), α /triangle: 0.2622(4), β /triangle: 1.080(2), α ©: 0.708(3), β ©: 1.014(8).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.75, α /square: 0.4235(5), β /square: 1.070(3), α /triangle: 0.2531(4), β /triangle: 1.094(2), α ©: 0.705(3), β ©: 1.037(7).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.8, α /square: 0.4120(6), β /square: 1.082(4), α /triangle: 0.2442(4), β /triangle: 1.107(2), α ©: 0.699(4), β ©: 1.057(9).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.85, α /square: 0.4017(8), β /square: 1.104(5), α /triangle: 0.2361(5), β /triangle: 1.122(3), α ©: 0.687(5), β ©: 1.06(1).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.9, α /square: 0.391(1), β /square: 1.123(7), α /triangle: 0.2285(5), β /triangle: 1.137(2), α ©: 0.676(5), β ©: 1.08(2).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 0.95, α /square: 0.380(1), β /square: 1.142(8), α /triangle: 0.2216(6), β /triangle: 1.152(3), α ©: 0.669(5), β ©: 1.11(2).
Según Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations (2020), I: 1, α /square: 0.371(1), β /square: 1.163(9), α /triangle: 0.2148(7), β /triangle: 1.165(4), α ©: 0.654(6), β ©: 1.12(2).
## 6 Conclusions

In summary, we have presented a strategy based on the site-bond percolation model to prevent the propagation of Phytophthora over a plantation. This strategy consists of placing barriers between adjacent cells, whose density depends on χ and I . Two different clustering processes were analyzed: i) clusters of cells with the presence of the pathogen, and ii) clusters of diseased plants. The former is related to a soil test and the latter to a direct visual inspection of the damage on the plantation. It was found that both processes are indistinguishable, and therefore described by the same critical curve, for I &lt; 0 . 15. On the contrary, for I &gt; 0 . 15 this behavior does not hold and different approaches for each process are necessary. Differences in the critical density of barriers between the soil and plant cases are a consequence of the hybridization process of the lattice, which leads to a major deviation when I increases and χ decreases (see Fig. 6). The soil case is described by the site-bond percolation model with an effective occupation probability given by p soil eff = I +(1 -I ) χ . Then the critical curves are as usual (see Eq. (1)) because the clustering process of the infected cells does not distinguish the sickness states of the plant.

In the plant case, the critical curves predict the existence of a minimal susceptibility χ plant c that guarantees a spanning cluster of infected plants will not appear, that is, if χ &lt; χ plant c even when p w = 0 and I = 1. Values for the minimal susceptibility in square, triangular and honeycomb lattices were found to be 0.28883 ± 0.00007, 0.2141 ± 0.0003 and 0.364 ± 0.003, respectively. Particularly, for the square lattice, this value is in agreement with the critical probability of lattices with more complex neighborhoods [50, 51].

Based on the obtained results, we would advise farmers and agronomists either to sow types of plants having a pathogen susceptibility lower than χ plant c , or to apply the barriers strategy with a barrier density given by Eq. (2). A very important advantage of this strategy is that it does not require to remove plants therefore avoiding deforestation.

This strategy could be verified under controlled conditions, for example, in greenhouses, tree nurseries, and hydroponics, where Phytophthora and other phytopathogens cause great devastation. On the other hand, its application on a real life situation requires to take into account other ecological and environmental variables, such as plant-plant or (beneficial) microorganism-plant interactions, irrigation system, spatial

Figure 7: (a) Critical values p plant w for Arbol (A), Poblano (P) and Serrano (S) chili plants sowed with a sqare lattice arrangement. Vertical lines indicate their susceptibilities: 1.00 (A), 0.89 (P) and 0.60 (S). The solid curves are the same as in Fig. 6. χ plant c ( I = 1) = 0 . 28883 ± 0 . 00007 is the maximum value of a plant's susceptibility that inhibits the formation of a cluster of diseased plants, even in the extreme case where the patogen is present all over the plantation. (b) Values of p plant w given by Eq. (2) and data from Table 1 for the Arbol (purple), Poblano (black) and Serrano (red) chili plants on a square lattice.

<!-- image -->

distribution of plants, the care provided by the farmer or the possibility of having more than one type of pathogen in the same parcel of soil.

Finally, Eq. (2) for I = 0 could be used as an alternative parametrization of the critical curves in the site-bond percolation model even for lattices defined in dimensions higher than two.

J. E. R. acknowledges financial support from CONACyT (postdoctoral fellowship Grant no. 289198). C.P. was supported by the grant Maria de Maeztu Unit of Excellence MDM-20-0692 and FPA Project No. 2017-83814-P of Ministerio de Ciencia, Innovaci´ on y Universidades (Spain), FEDER and Xunta de Galicia.

## References

- [1] D. C. Erwin and O. K. Ribeiro, Phytophthora diseases worldwide. St. Paul, Minnesota, USA: American Phytopathological Society (APS Press), 1996.
- [2] D. Shaw, 'Phytophthora diseases worldwide', The american phytopathological society (1996). J. Agr. Sci. , vol. 131, no. 2, pp. 245-249, 1998.
- [3] T. Reglinski, M. Spiers, J. Taylor, and M. Dick, 'Root rot in radiata pine seedlings can be controlled.,' N. Z. J. Forestry , vol. 54, no. 4, pp. 16-18, 2010.
- [4] F. J. Polach and R. K. Webster, 'Identification of strains and inheritance of pathogenicity in phytophthora capsici,' Phytopathology , vol. 62, no. 1, pp. 20-26, 1972.
- [5] M. K. Hausbeck and K. H. Lamour, 'Phytophthora capsici on vegetable crops: Research progress and management challenges,' Plant Dis. , vol. 88, no. 12, pp. 1292-1303, 2004.
- [6] K. H. Lamour, R. Stam, J. Jupe, and E. Huitema, 'The oomycete broad-host-range pathogen phytophthora capsici,' Mol. Plant Pathol. , vol. 13, no. 4, pp. 329-337, 2012.
- [7] H. Lozoya-Salda˜ na, M. N. Robledo-Esqueda, P. Rivas-Valencia, S. Sandoval-Islas, M. T. Beryl Colinas y Le´ on, and C. Nava-D´ ıaz, 'Sensitivity to fungicides of ¡em¿phytophthora infestans¡/em¿ (mont.) de bary in chapingo, mexico,' Rev. Chapingo Ser. Horticultura , vol. 23, no. 3, pp. 175-186, 2017.
- [8] S. K. Shakya, M. M. Larsen, M. M. Cuenca-Condoy, H. Lozoya-Salda˜ na, and N. J. Gr¨ unwald, 'Variation in genetic diversity of phytophthora infestans populations in mexico from the center of origin outwards,' Plant Dis. , vol. 102, no. 8, pp. 1534-1540, 2018.
- [9] B. J. Haas et al. , 'Genome sequence and analysis of the irish potato famine pathogen phytophthora infestans,' Nature , vol. 461, p. 393, 09 2009.

- [10] G. Weste and G. C. Marks, 'The biology of phytophthora cinnamomi in australasian forests,' Annu. Rev. Phytopathol. , vol. 25, no. 1, pp. 207-229, 1987.
- [11] M. You and K. Sivasithamparam, 'Changes in microbial populations of an avocado plantation mulch suppressive of phytophthora cinnamomi,' Appl. Soil Ecology , vol. 2, no. 1, pp. 33 - 43, 1995.
- [12] H. S. Judelson and B. Messenger-Routh, 'Quantitation of phytophthora cinnamomi in avocado roots using a species-specific dna probe,' Phytopathology , vol. 86, no. 7, pp. 763-768, 1996.
- [13] A. Vannini and A. M. Vettraino, 'Ink disease in chestnuts: impact on the european chestnut,' For. Snow Landsc. Res. , vol. 76, no. 3, pp. 345-350, 2001.
- [14] A. M. Vettraino, O. Morel, C. Perlerou, C. Robin, S. Diamandis, and A. Vannini, 'Occurrence and distribution of phytophthora species in european chestnut stands, and their association with ink disease and crown decline,' Eur. J. Plant Pathol. , vol. 111, no. 2, p. 169, 2005.
- [15] A. Vannini, G. Natili, N. Anselmi, A. Montaghi, and A. M. Vettraino, 'Distribution and gradient analysis of ink disease in chestnut forests,' Forest Pathol. , vol. 40, no. 2, pp. 73-86, 2010.
- [16] E. Vieitez, 'El casta˜ no y sus procesos de rizog´ enesis,' Trabajos Dept. Bot. Fisiol. Veg , vol. 11, pp. 25-31, 1981.
- [17] M. V. Gonz´ alez, B. Cuenca, M. L´ opez, M. J. Prado, and M. Rey, 'Molecular characterization of chestnut plants selected for putative resistance to phytophthora cinnamomi using ssr markers,' Sci. Hortic. , vol. 130, no. 2, pp. 459 - 467, 2011.
- [18] M. Miranda-Fontaina, J. Fern´ andez-L´ opez, A. Vettraino, and A. Vannini, 'Resistance of castanea clones to phytophthora cinnamomi: testing and genetic control,' Silvae Genet. , vol. 56, no. 1-6, pp. 11-21, 2007.
- [19] D. C. Erwin and O. K. Ribeiro, Phytophthora diseases worldwide. American Phytopathological Society (APS Press), 1996.
- [20] E. Bernhardt and R. Grogan, 'Effect of soil matric potential on the formation and indirect germination of sporangia of Phytophthora parasitica , Phytophthora capsici , and Phytophthora capsici cryptogea rots of tomatoes, Lycopersicon esculentum ,' Phytopathology (USA) , vol. 72, no. 5, 1982.
- [21] A. R. Hardham, ' Phytophthora cinnamomi ,' Mol. Plant Pathol. , vol. 6, no. 6, pp. 589-604, 2005.
- [22] B. Feng, P. Li, H. Wang, and X. Zhang, 'Functional analysis of pcpme6 from oomycete plant pathogen Phytophthora capsici ,' Microb. Pathogenesis , vol. 49, no. 1, pp. 23 - 31, 2010.
- [23] P. Li, B. Feng, H. Wang, P. W. Tooley, and X. Zhang, 'Isolation of nine Phytophthora capsici pectin methylesterase genes which are differentially expressed in various plant species,' J. Basic Microb. , vol. 51, no. 1, pp. 61-70, 2011.
- [24] Y. Cohen and M. D. Coffey, 'Systemic fungicides and the control of oomycetes,' Annual Review of Phytopathology , vol. 24, no. 1, pp. 311-338, 1986.
- [25] A. Drenth and D. I. Gest, ' Phytophthora in the tropics,' in Diversity and Management of Phytophthora in Southeast Asia (A. Drenth and D. I. Gest, eds.), no. 114, ch. Biology of Phytophthora , pp. 30-41, ACIAR, 2004.
- [26] H. L. Frisch and J. M. Hammersley, 'Percolation processes and related topics,' J. Soc. Ind. Appl. Math. , vol. 11, no. 4, pp. 894-918, 1963.
- [27] D. S. Callaway, M. E. J. Newman, S. H. Strogatz, and D. J. Watts, 'Network robustness and fragility: Percolation on random graphs,' Phys. Rev. Lett. , vol. 85, pp. 5468-5471, Dec 2000.
- [28] M. E. J. Newman, 'Spread of epidemic disease on networks,' Phys. Rev. E , vol. 66, p. 016128, Jul 2002.

- [29] N. Madar, T. Kalisky, R. Cohen, D. ben Avraham, and S. Havlin, 'Immunization and epidemic dynamics in complex networks,' Eur. Phys. J. B , vol. 38, pp. 269-276, Mar 2004.
- [30] W. A. Dunstan, T. Rudman, B. L. Shearer, N. A. Moore, T. Paap, M. C. Calver, R. Armistead, M. P. Dobrowolski, B. Morrison, K. Howard, E. O'Gara, C. Crane, B. Dell, P. O'Brien, J. A. McComb, and G. E. S. J. Hardy, 'Research into natural and induced resistance in australian native vegetation of phytophthora cinnamomi and innovative methods to contain and/or eradicate within localised incursions in areas of high biodiversity in australia.,' Tech. Rep. 19/2005DEH, Centre for Phytophthora Science and Management for the Australian Government Department of the Environment, Water, Heritage and the Arts, 2008.
- [31] C. P. Dunne, C. E. Crane, M. Lee, T. Massenbauer, S. Barrett, S. Comer, G. J. Freebury, D. J. Utber, M. J. Grant, and B. L. Shearer, 'A review of the catchment approach techniques used to manage a phytophthora cinnamomi infestation of native plant communities of the fitzgerald river national park on the south coast of western australia,' N. Z. J. Forestry Sci. , vol. 41, p. S121, 2011.
- [32] W. A. Dunstan, T. Rudman, B. L. Shearer, N. A. Moore, T. Paap, M. C. Calver, B. Dell, and G. E. S. J. Hardy, 'Containment and spot eradication of a highly destructive, invasive plant pathogen (phytophthora cinnamomi) in natural ecosystems,' Biol. Invasions , vol. 12, p. 913, 2011.
- [33] B. L. Shearer, C. E. Crane, R. G. Fairman, M. J. Dillon, and R. M. Buehrig, 'Spatio-temporal variation in invasion of woodlands and forest by phytophthora cinnamomi,' Australas. Plant Path. , vol. 43, pp. 327-337, May 2014.
- [34] G. Bonanomi, V. Antignani, C. Pane, and F. Scala, 'Suppression of soilborne fungal diseases with organic amendments,' J. Plant Pathol. , vol. 89, no. 3, pp. 311-324, 2007.
- [35] H. A. J. Hoitink, L. V. Madden, and A. E. Dorrance, 'Systemic resistance induced by trichoderma spp.: Interactions between the host, the pathogen, the biocontrol agent, and soil organic matter quality,' Phytopathology , vol. 96, no. 2, pp. 186-189, 2006.
- [36] C. M. Craft and E. B. Nelson, 'Microbial properties of composts that suppress damping-off and root rot of creeping bentgrass caused by pythium graminicola.,' Appl. Environ. Microb. , vol. 62, no. 5, pp. 1550-1557, 1996.
- [37] C. E. M. van, den Boom, T. A. van Beek, and M. Dicke, 'Differences among plant species in acceptance by the spider mite tetranychus urticae koch,' J. Appl. Entomol. , vol. 127, no. 3, pp. 177-183, 2003.
- [38] L. Geagea, L. Huber, I. Sache, D. Flura, H. McCartney, and B. Fitt, 'Influence of simulated rain on dispersal of rust spores from infected wheat seedlings,' Agr. Forest Meteorol. , vol. 101, no. 1, pp. 53 66, 2000.
- [39] S. Saint-Jean, A. Testa, L. Madden, and L. Huber, 'Relationship between pathogen splash dispersal gradient and weber number of impacting drops,' Agr. Forest Meteorol. , vol. 141, no. 2, pp. 257 - 262, 2006.
- [40] T. Gilet and L. Bourouiba, 'Rain-induced Ejection of Pathogens from Leaves: Revisiting the Hypothesis of Splash-on-Film using High-speed Visualization,' Integr. Comp. Biol. , vol. 54, pp. 974-984, 10 2014.
- [41] C. A. Walker and P. van West, 'Zoospore development in the oomycetes,' Fungal Biol. Rev. , vol. 21, no. 1, pp. 10 - 18, 2007.
- [42] J. E. Ram´ ırez, E. Molina-Gayosso, J. Lozada-Lechuga, L. M. Flores-Rojas, M. I. Mart´ ınez, and A. Fern´ andez T´ ellez, 'Percolation strategy to improve the production of plants with high pathogen susceptibility,' Phys. Rev. E , vol. 98, p. 062409, Dec 2018.
- [43] Y. Y. Tarasevich and S. C. van der Marck, 'An investigation of site-bond percolation on many lattices,' Int. J. Mod. Phys. C , vol. 10, no. 07, pp. 1193-1204, 1999.
- [44] M. E. J. Newman and R. M. Ziff, 'Efficient monte carlo algorithm and high-precision results for percolation,' Phys. Rev. Lett. , vol. 85, pp. 4104-4107, Nov 2000.

- [45] M. E. J. Newman and R. M. Ziff, 'Fast monte carlo algorithm for site or bond percolation,' Phys. Rev. E , vol. 64, p. 016706, Jun 2001.
- [46] S. Mertens and C. Moore, 'Continuum percolation thresholds in two dimensions,' Phys. Rev. E , vol. 86, p. 061109, Dec 2012.
- [47] M. D. Rintoul and S. Torquato, 'Precise determination of the critical threshold and exponents in a three-dimensional continuum percolation model,' J. Phys. A-Math. Gen. , vol. 30, pp. L585-L592, aug 1997.
- [48] D. Stauffer and A. Aharony, Introduction to percolation theory . Taylor &amp; Francis, 2014.
- [49] A. Coniglio, 'Cluster structure near the percolation threshold,' J. Phys. A-Math. Gen. , vol. 15, no. 12, pp. 3829-3844, 1982.
- [50] K. Malarz and S. Galam, 'Square-lattice site percolation at increasing ranges of neighbor bonds,' Phys. Rev. E , vol. 71, p. 016125, Jan 2005.
- [51] M. Majewski and K. Malarz, 'Square lattice site percolation thresholds for complex neighbourhoods,' Acta Phys. Pol. B , vol. 38, p. 2191, Jun 2007.