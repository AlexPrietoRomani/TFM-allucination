---
id: arxiv-2404.03839
title: A Complete Mathematical Model For Trichoderma Fungi Kinetics
year: 2024
country: Internacional
source: ArXiv (math.DS)
doc_type: Artículo científico
language: en
tags:
  - Trichoderma
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## A Complete Mathematical Model For Trichoderma Fungi Kinetics

Asmae Hardoul 1* and Zoubida Mghazli 1

1 Ibn Tofail University, Faculty of Sciences, ´ Equipe d'Ing´ enierie MAth´ ematique (E.I.MA.), PDE, Algebra and Spectral Geometry Laboratory, Kenitra, BP 133, Morocco.

*Corresponding author(s). E-mail(s): asmae.hardoul@uit.ac.ma; Contributing authors: zoubida.mghazli@uit.ac.ma;

## Abstract

We develop an unstructured mathematical model to describe the growth kinetics of the Trichoderma fungus and its enzyme (cellulase) production in the rhizosphere. This model incorporates hydrolysis, where organic matter is broken down, producing a liquefied substrate that supports fungal growth and enzyme synthesis. The resulting Captures the interactions between substrate degradation, fungal growth, and enzyme formation. Analysis of the model's asymptotic behavior reveals convergence to a global attractor comprising infinite non-hyperbolic equilibria, depending on initial conditions. Numerical simulations with data from the literature confirm the theoretical study and validate the model.

Keywords: Modeling; Ordinary Differential Equations; Kinetic models; Trichoderma; Hydrolysis; Global attractor.

MSC Classification: 92-10 , 37N25 , 34D35 , 34D05 , 34D45.

## 1 Introduction

Trichoderma is a fungus that grows in almost all soils and is a constituent of the fungal communities of the rhizosphere. They are also present on the root surfaces of many plants [12]. They play an important role in the soil nutrient cycle. Indeed, they have a beneficial effect on plant growth and soil fertility, [21, 30]. Fungi of the genus Trichoderma have been used as biological control

agents against a wide spectrum of soil-borne pathogens. Their antagonistic behavior has been demonstrated in numerous researches. [3, 4, 8, 20]. It has also been shown that these fungi play a key role in the production of a wide range of hydrolytic extracellular enzymes such as cellulase, which allows the degradation of cellulose [29]. These enzymes are also involved in the suppression of plant diseases [10] and generally have an antifungal effect. They are also highly synergistic in their antifungal activity when combined with fungicides whose mode of action affects the cell membranes of pathogenic fungi [16].

Kinetic models for the production of cellulase by Trichoderma reesei have been developed in various research [1, 15, 23, 24, 32], in which a soluble substrate has been used. For example, in the reference [24], a kinetic model of cell growth and cellulase formation has been developed, without using a substrate consumption equation. Muthuvelayudham and Viruthagiri [23], found that the logistic model, the Luedeking-Piret model and the integrated logistic model with Leudeking-Piret could accurately describe the cellulase production process, but they did not provide any numerical simulation. Bader et al [1], developed detailed kinetics for the production of an individual enzyme component, but cellulose data were not available although the model was provided. The most comprehensive kinetic models, including cell growth, substrate consumption, and cellulase production from cellulose, were first introduced by Velkovska et al [32]. Their study developed a simple model of product formation using total enzyme and variable substrate reaction models. However, the model was unable to predict the biomass curves. Furthermore, the effect of the substrate on cellulose production is not considered, and the rate of hydrolysis is assumed to be equal to the rate of consumption of the substrate throughout the process, which is usually not the case. Lijuan Ma et al [18], developed a simple and complete model for the cellulase production process using cellulose, but did not consider the product equation. Experimental data on cellulose, biomass and cellulase were used for parameter estimation and validation of the model by comparing the simulations with the experimental results of (Velkovska et al. [32]).

Hydrolysis is a key step in the biodegradation of organic matter, since it converts complex compounds into soluble substrates that can be directly assimilated by microorganisms. As shown by Vavilin et al. [31], in mechanistic models of solid matter degradation, this step is generally limiting for substrate availability. In the case of Trichoderma, which cannot directly utilize native cellulose, enzymatic hydrolysis by extracellular cellulases completely determines fungal growth. This is confirmed by recent studies on Trichoderma [9], as well as several works showing that the substrate flux resulting from hydrolysis governs biomass dynamics and enzyme production (Bischof et al. [6]; Li et al.[14]; Qian et al.[28]). A hydrolysis constant that is too low, therefore, limits substrate availability and slows microbial growth. Thus, it is essential to establish appropriate assumptions regarding this constant to ensure a realistic and stable representation of the process.

To the best of our knowledge, none of the mathematical models describing the growth kinetics of biomass (Trichoderma) and enzyme production (cellulase) during substrate degradation has taken the hydrolysis step into account.

The objective of this paper is the development and analysis of a complete system that models the kinetics of enzyme production (cellulase with cellulose) by the fungus Trichoderma in the rhizosphere. Inspired by the model of Lijuan Ma et al. [18], we develop an unstructured mathematical model that integrates the step of hydrolysis of organic matter and takes into account the formation of a product (cellulase), which makes it a more realistic and complete model. A fraction of dead microorganisms can constitute a new substrate. According to [7], they are then recycled as organic matter to be hydrolyzed. In the proposed model, we consider the mortality parameter, as well as the substrate consumption maintenance parameter, and the product formation maintenance parameter. We analyze the asymptotic behavior of the dynamics of the system obtained and prove that we have a continuum of non-hyperbolic equilibria. An analogous analysis was performed in [26], for a problem related to an anaerobic digestion model in the landfill. We show that each trajectory of the system is bounded and converges towards one of these non-hyperbolic equilibria according to the initial conditions. Some numerical tests are presented.

The article structure is as follows. The model and assumptions are introduced and discussed in the next section. Section 2 gives a mathematical analysis of the asymptotic behaviour and the set of equilibria. Finally, in Section 3, numerical simulations for different values of data from the literature and different initial conditions are given, confirming the theoretical study. A discussion, conclusions, and bibliography conclude this article.

## 2 Model and hypotheses

Modeling the growth and product formation of various micro-organisms is generally a very difficult task due to the complexity of living systems. The number of factors that influence the ability of the organism to grow and produce enzymes is very large and leads to complex complex systems with many parameters. In order to build a model that is accessible to mathematical analysis and numerical simulations, while taking into account the essential factors to describe the kinetics of enzyme production by the filamentous fungus Trichoderma in the rhizosphere, we will make the following assumptions. As a first assumption, we assume that the overall biomass has a single morphological form and that it is fed by a single substrate. We also assume that the extracellular medium (soil) is perfectly homogeneous. The model is based on the principle of mass balance applied to variables that are the concentrations of the components of the system. We note by X , B , s and P the concentrations of organic matter, living biomass, substrate and product (enzyme), respectively. The dynamics of the biomass B , taking into account the biological process of mortality, are given by

<!-- formula-not-decoded -->

where µ ( s ) is the growth function and k d is the specific mortality rate. The concentration of the substrate s and the cell growth are obviously interdependent. As the cells grow, they use up the substrate, which is thus depleted. The rate of substrate consumption is described by the equation :

<!-- formula-not-decoded -->

where Y B/s is the coefficient of efficiency of conversion of the substrate s into the biomass B . The substrate utilization kinetics, given in Eq. (2), can be modified to take into account the cell maintenance, which means living consumes substrate:

<!-- formula-not-decoded -->

Where m s is the coefficient of cell-specific maintenance by the substrate s . To model the kinetics of the formation of the product P , we use the LuedekingPiret model ( see [17]):

<!-- formula-not-decoded -->

where Y P/s is the conversion efficiency of a substrate s to a product P , expressed as 'the quantity of P formed per quantity of s consumed' , and m P is the cell-specific maintenance coefficient for the product P . We note that Equation (4) describing the formation of the product P , is related to the growth rate of B and its maintenance.

We assume that the parameters satisfy the following assumptions.

Hypothesis 1 The specific growth rate function µ ( · ) is of class C 1 with µ (0) = 0 and µ ( s ) &gt; 0 for all s &gt; 0.

Hypothesis 2 The coefficients k d , Y B/s , Y P/s , m s and m P satisfy the following conditions.

1. 0 &lt; k &lt; max µ ( s
2. 0 &lt; Y &lt; 1 and 0 &lt; Y &lt;
3. m s &gt; 0 and m P &gt;

<!-- formula-not-decoded -->

All the conditions of Hypothesis 2 are verified in real biological phenomena. A large number of growth rate functions satisfy Hypothesis 1 . The Monod law [19] is the most widely used, and many adaptations have been made to this growth model, such as the Teissier law, the Contois law and the Dabes et al law [25], where the growth rate is limited only by the substrate. Other models take into account an inhibition of, at least, one of the variables, such

as the Haldane law, the Luong law, the Aiba law, the Han and Levenspiel law, the Yano law and the Luong law [11]. It is known that Trichoderma fungi have no inhibitors for their growth. So, Monod's law is suitable for our problem. It takes the form:

<!-- formula-not-decoded -->

where µ max is the maximum growth rate and k s is the half-saturation constant.

Hydrolysis constitutes the key step in the valorization of lignocellulosic substrates because Trichoderma is not capable of directly assimilating native cellulose. Access to assimilable carbon depends exclusively on the extracellular enzymatic conversion of the polymeric matrix into soluble sugars (glucose, cellobiose), which subsequently feed intracellular metabolic pathways. Consequently, the efficiency of hydrolysis directly determines the amount of soluble substrate available to the biological system. When the cellulolytic activity is high, the hydrolytic flux ensures a continuous supply of carbon, enabling sustained biomass growth. In contrast, slow hydrolysis leads to a limitation in soluble substrate, even when the physiological potential for fungal growth remains high. In this case, the limiting factor does not stem from an intrinsic metabolic cap but from an insufficient upstream hydrolytic flux. This analysis is fully consistent with the experimental evidence available in the literature. Several studies have shown that the intensity of extracellular cellulase secretion by Trichoderma is strongly correlated with the solubilization of cellulose and the rate of biomass accumulation. Bischof et al. (2013)[6] demonstrated that enhanced enzyme production results in a faster release of soluble sugars and a significant increase in cellular productivity. Similar findings were reported by Li et al. (2016)[14] and Qian et al. (2017)[28], who emphasized that improved hydrolytic performance systematically increases bioavailable carbon flux. More recently, Duarte et al. (2021)[9] experimentally confirmed, using Trichoderma longibrachiatum isolates, that the efficiency of lignocellulosic forage hydrolysis directly controls the availability of soluble sugars as well as the growth and metabolic activity dynamics. Their results show that increasing cellulolytic activity immediately accelerates hydrolysis and enhances carbon release, thus validating the central role of the hydrolysis rate in the governance of the system. Together, these observations, both classical and recent, demonstrate that hydrolysis acts as the primary control step of mycelial growth dynamics in mechanistic degradation models. In standard models, hydrolysis is described by first-order kinetics:

<!-- formula-not-decoded -->

where K H is the hydrolysis constant. According to [7], a fraction α of dead microorganisms limited by biological constraints: 0 ≤ α &lt; 1 can constitute a new substrate and is then recycled as a material to be hydrolyzed. In this case, the last equation becomes :

<!-- formula-not-decoded -->

Moreover, since hydrolysis transforms organic matter into a new substrate, the term K H X is therefore a source term in Eq. (3) which becomes

<!-- formula-not-decoded -->

From equation (8), the dynamics of the substrate is based on the opposition between the consumption induced by biomass, represented by ( 1 Y B/s µ ( s ) + m s ) B , and the flux of the substrate produced by hydrolysis, given by K H X .

To represent a biologically realistic situation in which Trichoderma has a carbon flux that supports its growth, hydrolysis production must be sufficient at all times to compensate for metabolic consumption. This requirement leads to the introduction of a hydrolysis efficiency, which states that the substrate flux resulting from hydrolysis must be sufficient to compensate for the consumption induced by the biomass.

## Hypothesis 3 : for all t &gt; 0:

<!-- formula-not-decoded -->

This condition reflects the biological reality of the system. For Trichoderma, growth can occur only if enough sugars are produced by hydrolysis of cellulose. If consumption by the biomass exceeds hydrolytic production, the available substrate becomes insufficient and growth slows down, not because of a physiological limitation of the fungus, but because of a lack of assimilable substrate. The introduced inequality therefore ensures that the model remains consistent with reality: it guaranties that the soluble substrate never becomes limiting, thus allowing growth that is consistent with experimental observations. Hypothesis 3 establishes a direct link between hydrolysis kinetics and microbial dynamics, thereby constituting an essential component for the accurate modeling of microbial growth and substrate utilization.

Building upon the equations that describe the underlying dynamics and the key assumptions outlined above, we construct a comprehensive mathematical model. This model comprises four coupled equations representing the temporal

evolution of organic matter X , biomass B , substrate s , and product P :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which can be written as where

<!-- formula-not-decoded -->

## 3 Equilibrium points and asymptotic behaviour

This section presents an analysis of the system (10). We show that the solution remains positive, determine the equilibrium points, and give the asymptotic behavior of the solution.

## 3.1 Positivity of the solution and equilibrium points

We begin by proving the positivity of the solution.

Proposition 1 For any vector ( X 0 , B 0 , s 0 , P 0 ) with non-negative components, the solution of the system (10) with the initial condition ( X (0) , B (0) , s (0) , P (0)) = ( X 0 , B 0 , s 0 , P 0 ) exists and is unique and non-negative.

Proof The existence and uniqueness of the solution to system (10) are guaranteed by the Cauchy-Lipschitz theorem, since all functions involved in this system are globally Lipschitzian (see [33]). assuming µ ( · ) is bounded and C 1 , Hypothesis 1 To show the positivity of the solution of system (10), let X 0 ≥ 0, , B 0 ≥ 0, s 0 ≥ 0, and P 0 ≥ 0 be given. We proceed by step and show, first, that B ( t ) ≥ 0, then we deduce that X ( t ) ≥ 0, and then finally the positive result for s ( t ) and P ( t ).

1/ The explicit solution of B ( t ) is

<!-- formula-not-decoded -->

Since B (0) ≥ 0 and the exponential is always positive, it follows that B ( t ) ≥ 0 for all t ≥ 0.

- 2/ Using the positivity of B ( · ), any solution of the first equation, with ( X 0 , B 0 , s 0 , P 0 ) in R 3 + satisfies dX ( t ) dt ≥ -K H X ( t ) for all t &gt; 0. We deduce, by integration, that X ( t ) ≥ X 0 e -K H t , for all t &gt; 0. Therefore, for any vector ( X 0 , B 0 , s 0 , P 0 ), with non-negative components, we have X ( t ) ≥ 0, for all t &gt; 0.

## 3/ 4. Positivity of s ( t ) via Hypothesis 3.

The substrate equation reads

<!-- formula-not-decoded -->

By Hypothesis 3 , K H X ( t ) is sufficiently large relative to µ ( s ), m s , and B ( t ), which immediately gives

<!-- formula-not-decoded -->

- s ( t ) is also non-negative for all t &gt; 0, and cannot reach 0 in finite time, whatever ( X 0 , B 0 , s 0 , P 0 ) in R 3 + .
- 4/ By Hypothesis 1 , Hypothesis 2 and the positivity of B ( · ), all the coefficients of the last equation of Eq. (10) are non-negative. We deduce that dP dt is non-negative and therefore P ( t ) is increasing. Therefore, based on the fact that P (0) is in R + , P ( t ) is also non-negative for all t &gt; 0.

/square

An equilibrium point of the non-linear system (10), E = ( X ∗ , B ∗ , s ∗ , P ∗ ), is a solution of the system

<!-- formula-not-decoded -->

where A and V are defined in Eq.(12).

From the second equation of the system (13), we derive either B = 0 or µ ( s ) = k d .

- /check If B = 0 then by the first equation, we have X = 0 whatever s ∈ R , and the last two equations are automatically verified for any s, P ∈ R . The vector E = (0 , 0 , s, P ), for s, P ∈ R is then an equilibrium point.

/negationslash

- /check If B = 0, the the fourth equation of Eq.(13) gives k d Y p/s = -m p , which is not possible because m p &gt; 0 and k d Y p/s ≥ 0.

So, we have a continuum of equilibrium points given by E = (0 , 0 , s, P ), for s and P in R , whatever the function µ .

Usually, using the linearisation method, the stability of equilibria of ODEs is determined, by the sign of real part of eigenvalues of the Jacobian matrix. For

a point E = (0 , 0 , s ∗ , P ∗ ) these eigenvalues are given by

<!-- formula-not-decoded -->

We cannot conclude on the stability or instability, because these equilibrium points are not hyperbolic (the eigenvalues λ 3 and λ 4 are zero). In such situations, one could use the Lyapunov function (see [33], page 319), but it is generally difficult to find such a function, especially for a complex non-linear system. We show in the next section, using Barbalat's lemma (see [2]), that the solutions of the system tend to an equilibrium point when t tends to + ∞ , which makes it a globally and asymptotically stable equilibrium.

Note that λ 2 ≤ 0 if and only if µ ( s ∗ ) ≤ K d . In the study of basins of attraction, we will introduce the set of the values of s such µ ( s ) ≤ K d defined by

<!-- formula-not-decoded -->

Under Hypothesis 1 and Hypothesis 2 , this set has a non-empty interior. For the Monod law, we have

<!-- formula-not-decoded -->

## 3.2 Asymptotic behaviour

In this section, we describe the asymptotic behavior of the system solution (10) and deduce the stability of the equilibrium points. We begin by showing that when time goes to infinity, the solution tends to a point of the form (0 , 0 , s ∗ , P ∗ ) for some values s ∗ and P ∗ which depend on the parameters of the problem and the initial conditions.

Theorem 2 Let ( X 0 , B 0 , s 0 , P 0 ) be a vector with non-negative components, and suppose Hypothesis 1 and Hypothesis 2 are satisfied. Then the solutions of the system (10) with the initial condition ( X (0) , B (0) , s (0) , P (0)) = ( X 0 , B 0 , s 0 , P 0 ) converge asymptotically to an equilibrium point (0 , 0 , s ∗ , P ∗ ) such that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The coefficients a and b are positive numbers given by the following expressions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Moreover, when X 0 or s 0 is non-zero, we have s /star &gt; 0 and s /star belongs to S , where S is defined by Eq. (16) .

Proof Consider the function Z ( t ) defined by

<!-- formula-not-decoded -->

This function satisfies some properties that are essential for the rest of the proof. We start by mentioning them before evaluating the limits at infinity of the components of the solution of the system (10).

- Z ( t ) ≥ 0, for all t ≥ 0.
- The derivative of Z ( t ) is given by

<!-- formula-not-decoded -->

which makes it possible to write Z ( t ) also in the form

<!-- formula-not-decoded -->

- There exists 0 ≤ Z ∞ &lt; + ∞ such that

<!-- formula-not-decoded -->

indeed Z ( t ) is decreasing (by Hypothesis 2 , ( αY B/s -1 ) -m s Y B/s k d ) &lt; 0) and minorized by zezo.

- The second derivative of Z ( t ) is given by

<!-- formula-not-decoded -->

1. We begin by showing that the solution of Eq. (10) converge asymptotically to an equilibrium point.

## Limits of X ( t ) and B ( t )

With respect to the definition of Z ( t ), the limit (22) implies that the variables X ( t ), B ( t ) and s ( t ) are bounded (since they are non-negative). We deduce that the second derivative (23) is bounded, therefore dZ dt is uniformly continuous on R + . Barbalat's Lemma see [2] allows us to assert that lim t → + ∞ dZ dt = 0. By Eq. (20), we obtain lim t → + ∞ X ( t ) = 0.

Similarly, d 2 X dt 2 , which is expressed as a function of X ( t ) and B ( t ), is also bounded, and then dX dt is uniformly continuous and by Barbalat's lemma,

we deduce lim t → + ∞ dX dt = 0, and therefore, by the first equation of the system and knowing that lim t → + ∞ X ( t ) = 0, we have lim t → + ∞ B ( t ) = 0.

Limit of s ( t )

By Eqs. (19), and (22), and as we have already shown that lim t → + ∞ X ( t ) = lim t → + ∞ B ( t ) = 0, we can affirm that there exists a positive real s /star such that

<!-- formula-not-decoded -->

The function Z being decreasing, we have Z ∞ ≤ Z (0), and then s /star ≤ Z (0) αY B/s .

<!-- formula-not-decoded -->

Limit of P ( t )

Consider Z ( t ) written in the form of Equation (21). The function Z ( . ) is bounded, we deduce that it is the same for ∫ t 0 X ( τ ) dτ , then using the integration of the system (10) between 0 and t for t &gt; 0 gives

<!-- formula-not-decoded -->

We deduce by cascade that ∫ t 0 B ( τ ) dτ &lt; + ∞ , ∫ t 0 µ ( s ( τ )) B ( τ ) dτ &lt; + ∞ and that lim t → + ∞ P ( t ) is finite and positive as a limit of a positive and bounded increasing function.

Taking the limit in the last expressions of X ( t ), B ( t ) and P ( t ), when t tends to + ∞ , and having lim t → + ∞ X ( t ) = lim t → + ∞ B ( t ) = 0 and Eq. (17) gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Linear combinations of the first three equations give

<!-- formula-not-decoded -->

By replacing the expressions (26) and (27) in Eq. (25), we obtain the expression (18). Note that by Hypothesis 2 , [ 1 -Y B/s ( α -m s k d ) ] is strictly positive.

<!-- formula-not-decoded -->

/negationslash

/negationslash

2. Let us now show that s /star cannot be equal to 0 when X 0 or s 0 are not zero. Suppose that X 0 = 0 or s 0 = 0 and that s ( t ) tends to 0 when t tends to infinity. Then by continuity, the function µ ( s ( t )) will tend towards zero too, and there would exist T such that for all t ≥ T we have

<!-- formula-not-decoded -->

The sum of the first and third equations of the system (10) allows us to write

<!-- formula-not-decoded -->

By (28) we conclude that d dt ( X ( t ) + s ( t )) ≥ 0 for all t &gt; T. Using the same argument as the one used in the demonstration of the positivity of the solution, we conclude that if X (0) + s (0) &gt; 0, the variable X ( · ) or s ( · ) cannot reach 0 in finite time. We then have X ( t ) + s ( t ) ≥ X ( T ) + s ( T ) &gt; 0 for all t &gt; T , which is a contradiction to the fact that X ( t ) + s ( t ) tends to 0 when t tends to + ∞ .

3. We prove now that s ∗ belongs to S . Let ( X 0 , s 0 , B 0 , P 0 ) be in R 4 + with X 0 &gt; 0 and B 0 &gt; 0. Suppose that s ∗ , defined by Equation (17), does not belong to S . Then there would exist ˜ T &gt; 0 such that for all t &gt; ˜ T we would have : µ ( s ( t )) -k d &gt; η := µ ( s ∗ ) -k d 2 . By the system (10), we would then have dB ( t ) dt &gt; ηB ( t ) . Therefore, we would have B ( t ) &gt; B ( s ) exp η ( t -s ) for all

t, s &gt; ˜ T, such that t ≥ s, and then B ( . ) cannot converge asymptotically to 0, which is incompatible with the previous results .

/square

## 3.3 Properties of the equilibrium points

As we have already pointed out, the equilibria of the system (10) are not hyperbolic. We cannot conclude on their stability by directly using the linearization technique and the central variety theorem (see [27]). However, using a suitable variable change, we prove the existence of an invariant stable variety in the following theorem.

Theorem 3 Assume that Assumption 1 and Assumption 2 are satisfied. For each stationary point E = (0 , 0 , s ∗ , P ∗ ) with s ∗ in int S , there exists a stable twodimensional invariant variety M in R 4 + such that any solution of (10) with the initial condition in M converges asymptotically to E.

Proof The proof of this theorem is based on two variables changes, the first is for the variable s , and the second is for the variable P . We obtain a new system associated with the system (10) and whose equilibria are now hyperbolic. To define the variable change for s , we fix s ∗ &gt; 0 and P ∗ &gt; 0 so that µ ( s ∗ ) &lt; k d . Consider the solutions of (10) with B ( t ) &gt; 0, for t ∈ [0 , + ∞ ), and let

<!-- formula-not-decoded -->

which is equivalent to

<!-- formula-not-decoded -->

The function z ( t ) satisfies the equation (see the Appendix, page 20, for more details)

<!-- formula-not-decoded -->

with γ := [ k d (1 -αY B/s ) + Y B/s m s Y B/s ( k d -µ ( s ∗ )) ] &gt; 0, and using Eq. (31) we can write µ ( s ) in terms of the new variable and denote by F ( z, X, B ) the following expression

<!-- formula-not-decoded -->

The second change of variable is defined by setting P ∗ &gt; 0 and s ∗ &gt; 0 such that µ ( s ∗ ) &lt; k d . For the solutions of (10) with B ( t ) &gt; 0 for t ∈ [0 , + ∞ ), we define

<!-- formula-not-decoded -->

which is equivalent to

<!-- formula-not-decoded -->

The variable W ( t ) satisfies the equation (see A, page 21, for more details)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The system (10) becomes with the variables z and W , using Equation (33)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

 defined in the domain given by

By condition s ∗ ∈ int S , we have µ ( s ∗ ) = k d , and we can check that (0 , 0 , 0 , 0) is the only equilibrium of (37) in D . Indeed, if E = ( z ∗ , X ∗ , B ∗ , W ∗ ) is an equilibrium point, from the 3 th equation, we derive that either B = 0 or F ( z ∗ , X ∗ , B ∗ ) = k d .

- If F ( z ∗ , X ∗ , B ∗ ) = k d , from the equations 1 th and 4 th of the system (37) we deduce that µ ( s ∗ ) = k d contradicts condition s ∗ ∈ int S .
- The same reasoning as used for the equation 4 th gives W = 0.
- If B = 0, by the equation 2 th , we have X = 0 whatever s ∗ ∈ R + . In this case, from the first equation we deduce that we necessarily have z = 0 since we cannot have µ ( s ∗ ) = k d .

Thus, the vector E = (0 , 0 , 0 , 0) is the only equilibrium point of the system (37) in D and the Jacobian matrix associated is given by

<!-- formula-not-decoded -->

It admits a double eigenvalue r 1 and two single eigenvalues r 2 and r 3 :

<!-- formula-not-decoded -->

all of them are real and non-zero. According to the Central Variety Theorem [34] page 35) and under the condition µ ( s ∗ ) &lt; K d , the point (0 , 0 , 0 , 0) is thus a hyperbolic equilibrium point with a stable two-dimensional variety L and an unstable twodimensional variety U which are, respectively, positive and negative invariants. So, any trajectory ( z ( . ) , X ( . ) , B ( . ) , W ( . )) in D of the system (37) in the stable twodimensional invariant variety L∩D converges asymptotically to (0 , 0 , 0 , 0).

Finally, we conclude from the Invariance of Stability (see [5], Proposition 6.6, page 283) that by equivalence there exists a stable two-dimensional invariant variety M in R 4 + such that any solution of the system (10) with the initial condition in M converges asymptotically to (0 , 0 , s ∗ , P ∗ ). /square

## 4 Numerical tests

This section is dedicated to different numerical tests. As a validation of our model, we compare the results obtained by our system (10) with those obtained in [18] and [22]. After that, we present numerical tests that confirm the theoretical results obtained in the previous sections. The system (10) is autonomous. To achieve good accuracy, we choose the Runge-Kutta method of order 4 (RK4) and the Matlab computer software package to solve it.

## Validation tests

For the first test, we consider the data of Table 1 and Table 2 given in reference [18] for the first table and references [22] and [26] for the second. The evolution

Figure 1 : Evolution of X , B , s and P , using the parameters of Table 1, Table 2 and the initial conditions ( X 0 , B 0 , s 0 , P 0 ) = (45 , 15 , 50 , 0)

<!-- image -->

Table 1

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), µ max (1 /h ): 0.096, k s (g/l): 11.27, k d (1/h): 0.048, Y B/s (g/g): 1.19, m s (1/h): 0.0047, s 0 (g/l): 50, B 0 (g/l): 15, P 0 (g/l): 0.
## Table 2

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), α: 0.2, k H: 0.176, m P (1/h): 0.002, 1 Y P/s (g/g): 0.2, X 0 (g/l): 45.
curves over time of the organic matter X , the substrate s , the biomass B and the product P , using the resolution of the system (10) by Matlab are given in Fig. 1. We notice that the curve of the substrate s is very close to that given

experimentally in [18] (Fig. 3, page 195). This is a validation of our model. The curve of the biomass B of the same reference in which the results are also experimental converges towards a stationary phase, contrary to our system where it tends towards 0. This is explained by the fact that the experiment in [18] was carried out with fed-batch fermentation, while in the rhizosphere, the culture is discontinuous (batch) and forces the cell to go through exponential, stationary and finally decay phases.

After this first validation test, we consider another validation test related to the formation of the product, using the data of Table 3 and Table 4 given in the references [22], [18] and [26]. In [22] the authors highlighted the influence of various carbon substrates in the production of the cellulase protein using T. reesei 97.177 and Tm3. Cellulase shows the maximum yield of cellulose as a synthetic source. Kinetic studies were also done for growth and production using the Monod equation and Leudeking Piret model, respectively. Our results are given in Fig. 2 and are close to those of [22] (Fig. 5, page 1879).

Figure 2 : Evolution of X , B , s , P , using the parameters of Table 3 and Table 4 with ( X 0 , B 0 , s 0 , P 0 ) = (17 , 5 , 9 . 5 , 1 . 5)

<!-- image -->

## Table 3

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), µ max (1/h): 0.2, k s (g/l): 35.55, 1 Y P/s (g/g): 0.2, m P (1/h): 0.002, B 0 (g/l): 5, s 0 (g/l): 9.5, P 0 (g/l): 1.5.
Table 4

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), α: 0.2, k H: 0.176, Y B/s (g/g): 1.19, m s (1/h): 0.0047.
## Numerical experiments

First test: variation of X 0 . In Theorem 2 we studied the asymptotic behaviour of the system (10). We have highlighted, theoretically, the importance of the initial condition of organic matter in the production of enzymes (cellulase). Indeed we have shown that when time tends to infinity, the solution tends to an equilibrium point (0 , 0 , s ∗ , P ∗ ) for specific values s ∗ and P ∗ , which depend on the parameters of the problem and the initial conditions. In the following test, these theoretical considerations are confirmed numerically.

We fix all the parameters and vary the initial condition of the organic matter X 0 . The solution of the system (10) is performed with the data of Table 1 and Table 2 for initial conditions:

<!-- formula-not-decoded -->

The simulations in Figs. 3, 4, 6 and 5 describe the evolution, in the same time

<!-- image -->

Figure 3 : Evolution of X for initial conditions X i 0 for i = 1 , ..., 4 .

<!-- image -->

Figure 5 : Evolution of P for initial conditions X i 0 for i = 1 , ..., 4 .

Figure 4 : Evolution of B for initial conditions X i 0 for i = 1 , ..., 4 .

<!-- image -->

Figure 6 : Evolution of s(.) for initial conditions X i 0 for i = 1 , ..., 4 .

<!-- image -->

interval, of the variable X i , B i , s i and P i , respectively associated with the initial conditions X i 0 for i = 1 , ..., 4. We notice as expected in Theorem 2 , that:

- -if we have more initial organic matter, we will have more product formation,
- -whatever the initial condition, the variables X and B tend to zero when time becomes large,

- -for an initial condition B 0 &gt; 0, the variable s ( t ) do not tend towards 0 but tends towards a value s ∗ &gt; 0, when time becomes large.

The limit values are summarised in Table 5.

Second test: variation of k d . We now consider another test that allows us to

Table 5 : Limit values of X , B , s and P for different initial conditions X 0

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), X 0: 45, X ∗: 2,7402e-07, B ∗: 8,7454e-10, s ∗: 1,1745, P ∗: 31,8399.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), X 0: 90, X ∗: 7,8690e-07, B ∗: 9,1595e-10, s ∗: 1,1761, P ∗: 46,5702.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), X 0: 180, X ∗: 7,1684e-07, B ∗: 8,8018e-10, s ∗: 1,1766, P ∗: 76,0315.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), X 0: 360, X ∗: 2,3503e-07, B ∗: 8,3535e-10, s ∗: 1,1766, P ∗: 134,9544.
observe the effect of the variation of k d on the evolution of the concentrations of X , B , s , and P . In this test, we consider the resolution of the system (10) with the data of Table 1 and Table 2 except for µ max which will take the value. µ max = 0 . 2, and we make vary the value of k d as following

<!-- formula-not-decoded -->

The simulations in Figs. 7, 8, 9 and 10 represent the evolution, over time, of the variables X , B , s and P , respectively associated with the values of k i d for i = 1 , ... 4 . The respective curves of X , B , s and P are presented in the same time interval to visualize their relative behaviours. As modelled in the equations, we notice, as expected, that when the value of k d increases:

The maximum and limit values are summarised in Table 6.

Table 6 : Maximum and limit value of B , s and P for different values of k d

Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), k d: 0.03, B max: 96.6588, s max: 61.242, P max = P ∗: 32.9487, s ∗: 0.1629, B ∗: 0.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), k d: 0.09, B max: 57.1921, s max: 63.5208, P max = P ∗: 30.9508, s ∗: 1.7971, B ∗: 0.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), k d: 0.12, B max: 38.8395, s max: 65.024, P max = P ∗: 30.3268, s ∗: 3.0865, B ∗: 0.
Según A Complete Mathematical Model For Trichoderma Fungi Kinetics (2024), k d: 0.18, B max: 15, s max: 69.1788, P max = P ∗: 24.6089, s ∗: 20.4477, B ∗: 0.
- -the maximum value of the the concentration of the biomass B decreases (see Figs. 7, 8, 9, 10 and Table 6 ).

<!-- image -->

Figure 7 : Evolution of X ( · ), B ( · ), s ( · ) and P ( · ) with k d = 0 . 03

<!-- image -->

Figure 9 : Evolution of X ( · ), B ( · ), s ( · ) and P ( · ) with k d = 0 . 12

Figure 8 : Evolution of X ( · ), B ( · ), s ( · ) and P ( · ) with k d = 0 . 09

<!-- image -->

Figure 10 : Evolution of X ( · ), B ( · ), s ( · ) and P ( · ) with k d = 0 . 18

<!-- image -->

- -the maximum value of the concentration of the substrate s increases and so (it is natural) it stabilizes at a larger value s ∗ (see Figs. 7, 8, 9, 10 and Table 6 ),
- -The concentration of P remains an increasing function but the limit value decreases and is reached earlier (see Figs. 7, 8, 9, 10 and Table 6 ).

## 5 Conclusion

We developed an unstructured mathematical model describing the growth kinetics of Trichoderma and the production of enzymes (cellulase) by degradation of a substrate (cellulose). This model is more complete than the references cited here. We integrated the hydrolysis step of organic matter in our description. Furthermore, using the theorem of stable and unstable varieties, and Barbalat's lemma, we showed that each trajectory of the system is bounded and converges to one of the non-hyperbolic equilibria depending on the initial conditions. Numerical simulations with data from the literature confirm the theoretical study and validate the model.

Spatialising the model by introducing diffusion would constitute an immediate perspective of this work, which leads to a system of partial differential equations (PDE), of the reaction-diffusion type, instead of ordinary differential equations. We expect steel to be a global attractor. Since Trichoderma positively impacts plant growth, it would be interesting to consider a PDE system that models this impact and analyzes it mathematically.

## Acknowledgments

The authors warmly thank Pr. Ouazzani Touhami Amina from Laboratoire des Productions v´ eg´ etales, animals et Agro-industries (Ibn Tofail University) for all the discussions they had with her, allowing them to enrich their biological knowledge of Trichoderma.

## ORCID

asmae hardoul - https://orcid.org/0000-0003-4768-7834 zoubida mghazli - https://orcid.org/0000-0003-0264-0637

## A

## Determination of equation (32)

Consider the variable change (30) and introduce the function L defined by

<!-- formula-not-decoded -->

Then, using the expressions dX dt , dB dt and ds dt given in the system (10), we have

<!-- formula-not-decoded -->

Let

<!-- formula-not-decoded -->

which can be written as follows:

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

then with

By (42), we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since B ( t ) is assumed not to vanish, and using the second equation of (10), we obtain

<!-- formula-not-decoded -->

which is the equation (32).

## Determination of the equation (36)

Consider the variable change (34) and let K the function defined by

<!-- formula-not-decoded -->

Then using the equations of the system (10), we have

<!-- formula-not-decoded -->

Let

<!-- formula-not-decoded -->

which can be written as follows:

<!-- formula-not-decoded -->

and then

with

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

According to (44), we have

<!-- formula-not-decoded -->

Using the second equation of (10), we obtain

<!-- formula-not-decoded -->

which is the equation (36).

## References

- [1] Bader, J., Klingspohn, U., Bellgardt, K. H., Sch¨ ugerl, K., 'Modeling and simulation of the growth and enzyme production of Trichoderma reesei Rut C30,' Journal of Biotechnology , vol. 29, (1993), pp. 121-135.
- [2] Barbalat, I., 'Syst` emes d'´ equations diff´ erentielles d'oscillations non lin´ eaires,' Rev. Math. Pures Appl. , vol. 4, no. 2, (1959), pp. 267-270.
- [3] Benitez, T., Delgado-Jarana, J., Rinc´ on, A., Rey, M., Lim´ on, C., 'Biofungicides: Trichoderma as a biocontrol agent against phytopathogenic fungi,' Recent Res. Dev. Microbiol. , vol. 2, no. 1, (1998), pp. 129-150.
- [4] Berber, F., Ouazzani-Touhami, A., Badoc, A., Douira, A., 'Antagonisme in vitro et in vivo de deux Trichoderma ` a l'´ egard de quatre esp` eces de Bipolaris pathog` enes sur le sorgho,' Bull. Soc. Pharm. Bordeaux , vol. 148, (2009), pp. 93-114.
- [5] Betounes, D., 'Differential Equations: Theory and Applications,' New York: Springer , (2010).
- [6] Bischof R, Fourtis L, Limbeck A, Gamauf C, Seiboth B, Kubicek CP. 'Comparative analysis of the Trichoderma reesei transcriptome during growth on the cellulase inducing substrates wheat straw and lactose,' Biotechnology for biofuels ,Sep 9;6(1):127, (2013).
- [7] Dochain, D., 'Automatic Control of Bioprocesses Control Systems,' John Wiley and Sons , (2010).
- [8] Davet, P., 'Activit´ e parasitaire des Trichoderma vis-` a-vis des champignons ` a scl´ erotes : corr´ elation avec l'aptitude ` a la comp´ etition dans un sol non st´ erile,' Agronomie , vol. 6, no. 9, (1986), pp. 863-867.
- [9] Duarte, E.R., Maia, H.A.R., Freitas, C.E.S., Alves, J.M.S., Val´ erio, H.M., Cota, J., Hydrolysis of lignocellulosic forages by Trichoderma longibrachiatum isolate from bovine rumen, Biocatalysis and Agricultural Biotechnology , 36, 102135, 2021.
- [10] Elad, Y., Chet, I., Henis, Y., 'Degradation of plant pathogenic fungi by Trichoderma harzianum,' Can. J. Microbiol. , vol. 28, (1982), pp. 719-725.
- [11] Halmi, M.I.E., Abdullah, S.R.S., Johari, W.L.W., Ali, M.S.M., Shaharuddin, N.A., Khalid, A., Shukor, M.Y., 'Modelling the kinetics of hexavalent molybdenum (Mo6+) reduction by the Serratia sp. strain MIE2 in batch culture,' Rendiconti Lincei , vol. 27, no. 4, (2016), pp. 653-663.
- [12] Harman, G.E., Kubicek, C.P., 'Trichoderma and Gliocladium: Enzymes, Biological Control, and Commercial Applications,' London: Taylor and

Francis Ltd , (1998).

- [13] Lakshmikantham, V., Leela, S., 'Differential and Integral Inequalities: Theory and Applications: Volume I: Ordinary Differential Equations,' Academic Press , (1969).
- [14] Li Y, Yu J, Zhang P, Long T, Mo Y, Li J, Li Q., 'Comparative transcriptome analysis of Trichoderma reesei reveals different gene regulatory networks induced by synthetic mixtures of glucose and β -disaccharide. Bioresources and bioprocessing,' Jul 3;8(1):57, (2021).
- [15] Lo, C.M., Zhang, Q., Callow, N.V., Ju, L.K., 'Cellulase production by continuous culture of Trichoderma reesei Rut C30 using acid hydrolysate prepared to retain more oligosaccharides for induction,' Bioresource Technology , vol. 101, (2010), pp. 717-723.
- [16] Lorito, M., Peterbauer, C., Hayes, C.K., Harman, G.E., 'Synergistic interaction between fungal cell wall degrading enzymes and different antifungal compounds enhances inhibition of spore germination,' Microbiology , vol. 140, (1994), pp. 623-629.
- [17] Luedeking, R., Piret, E.L., 'A kinetic study of the lactic acid fermentation. Batch process at controlled pH,' J. Biochem. Microbiol. Technol. Eng. , vol. I, no. 4, (1959), pp. 393-412.
- [18] Ma, L., Li, C., Yang, Z., Jia, W., Zhang, D., Chen, S., 'Kinetic studies on batch cultivation of Trichoderma reesei and application to enhance cellulase production by fed-batch fermentation,' Journal of Biotechnology , Elsevier, (2013), pp. 192-197.
- [19] Monod, J., 'Recherches sur la croissance des cultures bact´ eriennes,' Hermann et Cie, Paris, France , (1942).
- [20] Mouria, B., Ouazzani-Touhami, A., Badoc, A., Douira, A., 'Effet de diverses farines sur la comp´ etitivit´ e des inoculums de trois souches de Trichoderma vis-` a-vis des champignons phytopathog` enes du sol,' Bull. Soc. Pharm. Bordeaux , vol. 144, (2005), pp. 211-224.
- [21] Mouria, B., Ouazzani-Touhami, A., Douira, A., 'Effet de diverses souches de Trichoderma sur la croissance d'une culture de tomate en serre et leur aptitude ` a coloniser les racines et le substrat,' Phytoprotection , vol. 88, no. 3, (2007), pp. 103-110.
- [22] Muthuvelayudham, R., Viruthagiri, T., 'Fermentative production and kinetics of cellulase protein on Trichoderma reesei using sugarcane bagasse and rice straw,' African Journal of Biotechnology , (2006).

- [23] Muthuvelayudham, R., Viruthagiri, T., 'Optimization and modeling of cellulase protein from Trichoderma reesei Rut C30 using a mixed substrate,' African Journal of Biotechnology , vol. 6, (2007), pp. 041-046.
- [24] Rakshit, S.K., Sahai, V., 'Optimal control strategy for the enhanced production of cellulase enzyme using the new mutant Trichoderma reesei E-12,' Bioprocess Engineering , vol. 6, (1991), pp. 101-107.
- [25] Ruggeri, B., Sassi, G., 'On the modeling approaches of biomass behaviour in a bioreactor,' Chemical Engineering Communications , vol. 122, no. 1, (1993), pp. 1-56.
- [26] Ouchtout, S., Mghazli, Z., Harmand, J., Rapaport, A., Belhachmi, Z., 'Analysis of an anaerobic digestion model in landfill with mortality term,' Communications on Pure and Applied Analysis , vol. 19, no. 4, (2020), pp. 2333-2346.
- [27] Perko, L., 'Differential Equations and Dynamical Systems,' Springer , 3rd ed., (2011).
- [28] Qian Y, Zhong L, Gao J, Sun N, Wang Y, Sun G, Qu Y, Zhong Y. 'Production of highly efficient cellulase mixtures by genetically exploiting the potentials of Trichoderma reesei endogenous cellulases for hydrolysis of corncob residues,' Microbial cell factories Nov 21;16(1):207, (2017).
- [29] Schuster, A., Schmoll, M., 'Biology and biotechnology of Trichoderma,' Applied Microbiology and Biotechnology , vol. 87, (2010), pp. 787-799.
- [30] Talbi, Z., Chliyeh, M., Mouria, B., El Asri, A., Aguil, F.A., OuazzaniTouhami, A., Benkirane, R., Douira, A., 'Effect of double inoculation with endo-mycorrhizae and Trichoderma harzianum on the growth of carob plants,' IJAPBC , vol. 5, no. 1, (2016), pp. 44-58.
- [31] Vavilin, V.A., Fernandez, B., Palatsi, J., Flotats, X., 'Hydrolysis kinetics in anaerobic degradation of particulate organic material: An overview,' Waste Management , vol. 28, no. 6, (2008), pp. 939-951.
- [32] Velkovska, S., Marten, M.R., Ollis, D.F., 'Kinetic model for batch cellulase production by Trichoderma reesei RUT C30,' Journal of Biotechnology , vol. 54, (1997), pp. 83-94.
- [33] Walter, W., 'Ordinary Differential Equations,' Springer , (1998).
- [34] Wiggins, S., Golubitsky, M., 'Introduction to Applied Nonlinear Dynamical Systems and Chaos,' Springer , (2003).