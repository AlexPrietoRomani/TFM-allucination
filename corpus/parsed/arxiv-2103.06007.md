---
id: arxiv-2103.06007
title: Pest control using farming awareness: impact of time delays and optimal use of biopesticides
year: 2021
country: Internacional
source: ArXiv (math.OC, q-bio.QM)
doc_type: Artículo científico
language: en
tags:
  - control biológico
  - biopesticidas
  - manejo de plagas
  - manejo integrado de plagas
  - dinámica de poblaciones
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## Pest control using farming awareness: impact of time delays and optimal use of biopesticides ∗

Teklebirhan Abraha 1 tekbir98@yahoo.com

Fahad Al Basir 2 fahadbasir@gmail.com

Legesse Lemecha Obsu 1 legesse.lemecha@astu.edu.et

Delfim F. M. Torres 3 † delfim@ua.pt

1 Department of Mathematics, Adama Science and Technology University, Adama, Ethiopia

2 Department of Mathematics, Asansol Girls' College, West Bengal 713304, India

3 R&amp;D Unit CIDMA, Department of Mathematics, University of Aveiro, 3810-193 Aveiro, Portugal

## Abstract

We investigate a mathematical model in crop pest management, considering plant biomass, pest, and the effect of farming awareness. The pest population is divided into two compartments: susceptible pest and infected pest. We assume that the growth rate of self-aware people is proportional to the density of healthy pests present in the crop field. Impacts of awareness is modeled via a saturated term. It is further assumed that self-aware people will adopt biological control methods, namely integrated pest management. Susceptible pests are detrimental to crops and, moreover, there may be some time delay in measuring the healthy pests in the crop field. A time delay may also take place while becoming aware of the control strategies or taking necessary steps to control the pest attack. In agreement, we develop our model incorporating two time delays into the system. The existence and the stability criteria of the equilibria are obtained in terms of the basic reproduction number and time delays. Stability switches occur through Hopf-bifurcation when time delays cross critical values. Optimal control theory has been applied for the cost-effectiveness of the delayed system. Numerical simulations illustrate the obtained analytical results.

Keywords: mathematical modeling of biological systems; time delays; stability; Hopf bifurcation; optimal control; numerical simulations.

MSC 2020: 34H20; 37G15; 49N90; 92D25.

## 1 Introduction

In recent times, integrated pest management is gaining more attention among researchers and its application is also increasing in the crop field. This method seeks to reduce the reliance on pesticides by emphasizing the contribution of biological control agents. The important role of microbial pesticides in integrated pest management is well-known in agriculture, forestry, and public health. As integrated pest management, bio-pesticides give noticeable pest control reliability in case of crops [1]. The use of viruses against insect pests, as pest control agents, is seen in North America and in European countries [2, 3, 4]. Awareness campaigns, in particular through radio or TV, are required so that people will gain trustworthiness on a biological control approach.

∗ This is a preprint of a paper whose final and definite form is published by 'Chaos Solitons Fractals' (ISSN: 0960-0779). Paper Submitted 08/Sept/2020; Revised 25/Feb/2021; Accepted 10/March/2021.

† Corresponding author. Email: delfim@ua.pt

Farmers, in their own awareness, can keep the crop under observation and, therefore, if correctly instructed, they will spray bio-pesticides or incorporate fertile to make the pest susceptible to their bio-agents. For the effect of awareness coverage in controlling infectious diseases we refer the reader to [5], where a SIS model is formulated considering individuals' behavioral changes due to the influences of media coverage, and where the susceptible class is divided into two subclasses: aware susceptible and unaware susceptible.

Correct and relevant knowledge about crop and its pests is very much essential for people engaged in cultivation. The role of electronic media is critical for keeping the farming community updated and by providing them with relevant agricultural information [6, 7]. Accessible pesticide information campaigns help farmers to be aware on the serious risks that pesticides have on human health and environment and minimize negative effects [8]. Adopting awareness programs, intended to educate farmers', results in a better comprehensive development for the cultivars and also for the farmers. Farmers learn the use and dangers of pesticides mainly by oral communication. Self-aware farmers employ considerably improved agronomic practices, safeguarding health and reducing environmental hazards [9]. Therefore, awareness is important in crop pest management.

Television, radio, and mobile telephony are particularly useful media in providing information about agricultural practices and crop protection [6]. Adopting new technologies during agricultural awareness programs represents a major route for innovating and improving agronomy. Le Bellec et al. [10] have studied how an enabling environment for interactions between farmers, researchers, and other factors, can contribute to reduce current problems associated with crop. Al Basir et al., describe the participation of farming communities in Jatropha projects for biodiesel production and protection of plants from mosaic disease, using a mathematical model to forecast the development of renewable energy resources [11]. In [12], authors have developed a mathematical model for pest control using bio-pesticides. Moreover, they also incorporate optimal control theory to minimize the cost in pest management due to bio-pesticides. For the use of optimal control theory to eradicate the number of parasites in agroecosystems, see [13]. The usefulness of time-delays in epidemiological modeling is well-known [14]. In [15], a model for pest control is proposed and analyzed, where the impact of farming awareness and a time delay in local awareness is investigated. They conclude that raising awareness among people, with tolerable time delay, may be a proper aspect for the control of pests in a crop field while reducing the serious issues that pesticides have on human health and environment [15]. Later, in [16], Al Basir has discussed the effects of delay in pest control due to the implementation of control interventions. In [17], Al Basir and Ray analyze the dynamics of vector borne plant disease dynamics influenced by farming awareness. Here, a mathematical model is formulated to protect crops through awareness campaigns, modeled via saturated terms, and a delayed optimal control problem for biopesticides is posed and solved.

The paper is organized as follows. In Section 2, the model is derived assuming that the rate of awareness is proportional to the number of susceptible pests in the field. Moreover, we make the model more realistic considering a time delay due to the measure of pest in the field. In Section 3, nonnegativity and boundedness of the solutions are proved by finding the invariant region. The equilibria, the basic reproduction number, and the stability of the pest-free equilibrium are studied, using qualitative theory, in Section 4. In Sections 5 and 6, we study the direction and stability of the Hopf bifurcation, investigating the stability switches of the equilibrium points, respectively for the system without and with delays. We show that stability switch occurs through Hopf bifurcation. An optimal control problem is then formulated and solved analytically in Section 7, with the goal to minimize the cost of biopesticides. The obtained analytical results are illustrated through numerical simulations in Section 8. We end with Section 9 of discussion and conclusion.

## 2 Model Derivation

In this section, we present a deterministic pest control model to prevent yield loss. The model includes crop biomass, X ( t ); healthy pest, S ( t ); infected pest, I ( t ); and level of awareness, A ( t ). Due to the finite size of the crop field, we assume logistic growth for the density of crop biomass,

with net growth rate r and carrying capacity K . Susceptible attacks the crop, thereby causing considerable crop reduction. If we infect the susceptible pest by pesticides, then the attack by pest can be controlled. Here we assume that self-aware farmers will adopt biological pesticides for the control of crop pest as it has fewer side effects and are also environment-friendly [15]. Bio-pesticides are used to infect healthy pest. The infected pest has additional mortality due to infection. We further assume that infected pests cannot consume crop [12].

Let λ be the consumption rate of pests with conversion rate m . There is a pest infection rate, h , because of self-aware human interactions and activity such as the use of bio-pesticides, modeled via the usual mass action term hAS 1+ A [18]. Here, d is the natural mortality rate of pest and α is the additional mortality rate of infected pest due to self-aware people activity. It is assumed that the level of awareness will increase at a rate proportional to the number of susceptible pests per plant noticed in the farming system. A fading of interest in this exploitation is possible, and we denote by η the rate of awareness fading.

There might be a delay in observing the number or activity of pests in a field. Usually, this estimate is generated by observing previous cases of pest occurrence and thus the intensity of awareness and the level of implication of preventive countermeasures varies. A delay τ 1 &gt; 0 is expected in the execution of such measures. The intensity of the awareness programs, being executed at time t , will be in accordance with the number of pests at the time t -τ 1 &gt; 0. Also, after an advertisement, farmers take some time to become aware of the technologies/pesticide to use and their management. We assume τ 2 &gt; 0 as the time delay parameter taken for organizing an awareness campaign and the farmers to become aware.

Based on the above assumptions, the mathematical model is formulated subject to initial conditions

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where φ ∈ [ -τ, 0] with τ = max { τ 1 , τ 2 } . The meaning of the parameters of model (1) is summarized in Table 1, together with the values that later will be used in our numerical simulations.

Table 1: Meaning of the parameters of model (1) with values used in Section 8 for numerical simulations.

Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: r, Description: growth rate of crop biomass, Value: 0.1 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: K, Description: maximum density of crop biomass, Value: 100 m - 2.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: λ, Description: consumption rate of pest, Value: 0.05 biomass - 1 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: d, Description: natural mortality of pest, Value: 0.02 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: m, Description: conversion efficacy, Value: 0.6.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: h, Description: aware people activity rate, Value: 0.025 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: a, Description: aware people growth rate, Value: 0.012 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: α, Description: additional mortality rate, Value: 0.025 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: ω, Description: rate of awareness from global source, Value: 0.003 day - 1.
Según Pest control using farming awareness: impact of time delays and optimal use of biopesticides (2021), Parameters: η, Description: fading of memory of aware people, Value: 0.015 day - 1.
## 3 Model Analysis

In this section, some basic properties of the solutions of the delayed system (1) are proved. In concrete, we show positive invariance and boundedness of solutions.

Theorem 1 (Non-negative invariance) . All solutions of (1) with given/fixed initial conditions (2) are non-negative.

Proof. The result is straightforward: using the fundamental lemma in [19], one can easily show that a solution to the initial value problem (1)-(2) exists in the region R 4 + and all solutions remain non-negative for all t &gt; 0. Therefore, the positive octant R 4 + is an invariant region.

Theorem 1 is important because positivity implies, biologically, the survival of the populations. We now prove another important characteristic of the solutions of (1): they are bounded.

Theorem 2 (Boundedness of solutions) . Every solution of system (1) that starts in

<!-- formula-not-decoded -->

is uniformly bounded, where D is defined with B 1 = max { X (0) , K } and B 2 = aM ( r +4 d ) 4 d .

Proof. Let us consider the first equation of our model (1). Then,

<!-- formula-not-decoded -->

where M = max { X (0) , K } . Let W = X + S + I at any time t . It follows, using (3) and the fact that rX [ 1 -X K ] is quadratic in X and its maximum value is rk 4 , that

<!-- formula-not-decoded -->

Now, after a simple calculation, one gets

<!-- formula-not-decoded -->

Finally, from the last equation of system (1) and (4), we get

<!-- formula-not-decoded -->

which implies that lim sup t →∞ A = aM ( r +4 d ) 4 ηd . Thus, the region of attraction given by the set D is positively invariant, attracting all solutions initiating inside the interior of the positive octant.

## 4 Equilibria and Stability

Model (1) has three equilibria: (i) the origin E 0 = ( 0 , 0 , 0 , ω η ) , (ii) the equilibrium in which only the healthy plants population thrives, E 1 = ( K, 0 , 0 , ω η ) , which is always feasible, and (iii) the coexistence equilibrium, E ∗ = ( X ∗ , S ∗ , I ∗ , A ∗ ) with

<!-- formula-not-decoded -->

where A ∗ is the positive root of

<!-- formula-not-decoded -->

with

<!-- formula-not-decoded -->

Our next result characterizes the feasibility of the coexistence equilibrium E ∗ .

Proposition 3 (Feasibility of the coexistence equilibrium) . Let E ∗ = ( X ∗ , S ∗ , I ∗ , A ∗ ) be as (5) .

- (i) If L 3 &gt; 0 , then there is a unique coexisting equilibrium E ∗ .
- (ii) If L 3 = 0 and L 2 &gt; 0 , then there is a unique coexisting equilibrium E ∗ with A ∗ = -L 2 L 1 .
- (iii) If L 3 &lt; 0 and L 2 ≤ 0 , then there is no positive coexisting equilibrium of the system.
- (iv) Assuming that L 3 &lt; 0 and L 2 &gt; 0 ,

-

A

-

-

if if

D

D

=

= 0

2

2

4

L

1

L

3

&gt;

0

, then there exist two coexisting equilibria

E

, then there exists a unique coexisting equilibrium

E

∗

;

-if D &lt; 0 , then there exists no positive coexisting equilibrium E ∗ .

Proof. The result follows applying Descartes' rule of signs to equation (6).

Linearizing system (1) about the pest free equilibrium E 1 , we obtain that

<!-- formula-not-decoded -->

with F , G and H the 4 × 4 matrices

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where F 11 := r ( 1 -2 X K ) -λS . The characteristic equation is given by that is,

<!-- formula-not-decoded -->

with one eigenvalue being ξ = -( d + α ) &lt; 0 and the rest of the spectrum being given by the roots of the transcendental equation

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

Note that the origin, E 0 , is always stable, in view of the fact that its eigenvalues r &gt; 0, -m&lt; 0, -ζ &lt; 0, and -η are all negative. At the equilibrium E 1 with only healthy plants, however, the eigenvalues are -r &lt; 0, λk -d , -d -α &lt; 0, and -η &lt; 0, so E 1 is stable only if λk -d &lt; 0. This stability is well characterized through the basic reproduction number, denoted by R 0 , which is one of the most important quantities in epidemiology.

Theorem 4 (Basic reproduction number R 0 ) . The basic reproduction number of system (1) is given by

<!-- formula-not-decoded -->

∗

with

V

∗

=

-

L

2

L

2

± √

1

D

;

Proof. We use the next-generation matrix method. Let Y = ( S, I ) T . Then, from system (1), we can write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where

The Jacobian matrix of F ( Y ) and V ( Y ), at the pest free equilibrium E 1 , are given respectively as

<!-- formula-not-decoded -->

with

<!-- formula-not-decoded -->

The reproduction number R 0 is given by the spectral radius of DF ( E 1 )( DV ( E 1 )) -1 , that is,

<!-- formula-not-decoded -->

The proof is complete.

Remark 5. It is fundamental to note that R 0 does not depend on a . For this reason, irrespective of how capably farmers turn aware of disease due to inspection of infected plants, this by itself is not sufficient to result in the eradication of infection. Because R 0 is monotonically decreasing with increasing of ω , this suggests that eradication of plant disease, as represented by a stable pest-free steady-state E 1 , is only possible if R 0 &lt; 1 . One existing means to achieve this consists to increase the rate ω of global awareness.

We finish this section characterizing the locally stability of the the pest-free equilibrium E 1 in terms of the basic reproduction number R 0 given by Theorem 4.

Theorem 6 (Local stability of the pest-free equilibrium) . For R 0 &lt; 1 , the pest-free equilibrium E 1 is locally stable. For R 0 &gt; 1 , E 1 is unstable and the coexistence equilibria E ∗ exists. A transcritical bifurcation occurs at R 0 = 1 .

Proof. The characteristic equation at the pest free equilibrium E 1 is given by

<!-- formula-not-decoded -->

Thus, the eigenvalues are -r , -η , -d -α , and mλK -hω η + ω -d . Therefore, E 1 is locally stable if mλK -hω η + ω -d &lt; 0, from which mλK &lt; hω + d ( η + ω ), that is,

<!-- formula-not-decoded -->

We conclude that R 0 &lt; 1, as intended.

## 5 Stability and Hopf Bifurcation in Absence of Delays

In this section we consider τ 1 = τ 2 = 0, investigating the direction and stability of the bifurcating periodic solution. More precisely, we focus our analysis on the consumption rate λ of pest, which is one of the biologically most important parameters of the model.

Theorem 7 (Local stability of the coexistence equilibrium-undelayed case) . Let us consider system (1) with τ 1 = τ 2 = 0 and let E ∗ = ( X ∗ , S ∗ , I ∗ , A ∗ ) be its coexistence equilibrium. Then E ∗ is locally asymptotically stable if, and only if,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where and

Proof. The Jacobian of system (1) without delays at the coexistence state E ∗ is

<!-- formula-not-decoded -->

The characteristic equation in ξ for the Jacobian matrix J ( E ∗ ) is given by

<!-- formula-not-decoded -->

that is,

<!-- formula-not-decoded -->

∣ which gives

∣

<!-- formula-not-decoded -->

with σ 1 , σ 2 and σ 3 as in (11). By the Routh-Hurwitz theorem, it follows that the coexistence equilibrium E ∗ is locally asymptotically stable if, and only if, σ 1 &gt; 0, σ 2 &gt; 0, σ 3 &gt; 0, and σ 1 σ 2 -σ 3 &gt; 0. Due to the positivity of parameters, σ 1 and σ 2 are always positive, so the stability condition can be given by (10).

Hopf bifurcation of the endemic steady state can occur if the characteristic equation (12) has a pair of purely imaginary eigenvalues for some λ = λ ∗ ∈ (0 , ∞ ) and, additionally, all other eigenvalues have negative real parts [20]. The characteristic equation (12) has one negative root, namely, -( d + α ). Hopf bifurcation occurs according to the following theorem.

Theorem 8 (Hopf bifurcation-undelayed case) . Let σ i , i = 1 , 2 , 3 , be given by (11) . System (1) with τ 1 = τ 2 = 0 , at the endemic equilibrium point E ∗ , undergoes Hopf bifurcation at λ = λ ∗ in the following domain:

/negationslash

<!-- formula-not-decoded -->

where we use the 'dot' to denote differentiation with respect to λ .

Proof. Using the condition σ 1 σ 2 -σ 3 = 0, the characteristic equation (12) becomes

<!-- formula-not-decoded -->

which has three roots: ξ 1 = i √ σ 2 , ξ 2 = -i √ σ 2 , and ξ 3 = -σ 1 . Therefore, a pair of purely imaginary eigenvalues exists for σ 1 σ 2 -σ 3 = 0. Now, we verify the transversality condition. Differentiating the characteristic equation (12) with respect to λ , we have

<!-- formula-not-decoded -->

Therefore, and Hopf bifurcation occurs at λ = λ ∗ .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Remark 9. When the parameter λ crosses the critical value λ ∗ , a limit cycle of system (1) occurs around E ∗ .

## 6 Stability and Hopf Bifurcation of the Delayed System

In this section, we investigate stability and Hopf bifurcation for the delayed system (1). Without loss of generality, it is assumed that E ∗ = ( X ∗ , S ∗ , I ∗ , A ∗ ) is the interior equilibrium point of the system with delays. In the sequel, we define τ as the sum of the two delays of the system, that is,

<!-- formula-not-decoded -->

Theorem 10 (Local stability of the coexistence equilibrium-delayed case) . Let a i , i = 1 , . . . , 5 , be given by (9) . Define S 1 := a 2 1 -2 a 2 , S 2 := a 2 2 -2 a 1 a 5 -a 2 4 , and S 3 := a 2 5 -a 2 3 . If the conditions

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

are satisfied, then the infected steady state E ∗ is locally asymptotically stable for all τ ≥ 0 .

Proof. For the stability of the endemic equilibrium, the distribution of the roots of (8) needs to be analyzed. The characteristic equation (8) becomes

<!-- formula-not-decoded -->

Equation (13) is a transcendental equation in ξ with infinitely many roots. It is known that the coexistence equilibrium E ∗ is locally stable (or unstable) if all the roots of the corresponding characteristic equation have negative real parts (or have positive real parts). Suppose ξ = iw ( τ ) is a root of equation (13). Then,

<!-- formula-not-decoded -->

Separating the real and imaginary parts, we obtain the following equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Squaring and adding the real and imaginary parts, we get

<!-- formula-not-decoded -->

/negationslash

/negationslash

Let θ = w 2 . Then, equation (17) becomes

<!-- formula-not-decoded -->

Now, if the following conditions

<!-- formula-not-decoded -->

are satisfied, then equation (18) has no positive real roots. We get from (18) that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since we assume S 2 &gt; 0, we have √ S 2 1 -3 S 2 &lt; S 1 and hence neither θ 1 nor θ 2 is positive. Thus, equation (19) does not have any positive roots. Since F (0) = S 3 ≥ 0, we conclude that equation (18) has no positive roots.

Remark 11. The parameters in Table 1 satisfy the conditions of Theorem 10. Thus, the steady state E ∗ of the delayed model (1) is asymptotically stable for all τ &gt; 0 , i.e., the stability of the system at the coexistence equilibrium is delay independent.

A Hopf-bifurcating periodic solution appears when purely imaginary roots exist. We shall now check the possible occurrence of Hopf-bifurcation.

If S 3 &lt; 0, then there exists a positive root θ 0 for which the characteristic equation (8) has pair of purely imaginary roots ± iw 0 . Equation (18) satisfies H (0) &lt; 0 and lim θ →∞ H ( θ ) = ∞ . Thus, equation (18) has at least one positive root, θ 0 . Again, if S 2 &lt; 0, then √ S 2 1 -3 S 2 &gt; S 1 and hence θ 1 &gt; 0. This implies that equation (17) possesses purely imaginary roots ± iw 0 . For w ( τ 0 ) = w 0 , equations (15) and (16) give

<!-- formula-not-decoded -->

where

Therefore, the following result holds.

<!-- formula-not-decoded -->

Theorem 12 (Hopf bifurcation-delayed case) . Let a i , i = 1 , . . . , 5 , and S j , j = 1 , . . . , 3 , be as in Theorem 10. Suppose that the interior equilibrium point E ∗ exists and a 1 &gt; 0 , a 3 + a 5 &gt; 0 , and a 1 ( a 2 + a 4 ) -( a 3 + a 5 ) &gt; 0 . Define

<!-- formula-not-decoded -->

where w 0 is given by (22) . If either S 3 &lt; 0 or S 3 ≥ 0 and S 2 &lt; 0 , then E ∗ is asymptotically stable when τ &lt; τ 0 and unstable when τ &gt; τ 0 . When τ = τ 0 , a Hopf bifurcation occurs: a family of periodic solutions bifurcates at E ∗ as τ passes through the critical value τ 0 , provided the transversality condition is satisfied with

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which has two roots

Proof. Differentiating (15) and (16) with respect to τ , we have

<!-- formula-not-decoded -->

∣ Therefore, d dτ [ Re { λ ( τ ) } ] τ = τ 0 ,w = w 0 &gt; 0 if P ( w 0 ) R ( w 0 ) -Q ( w 0 ) S ( w 0 ) &gt; 0. Thus, the transversality condition is satisfied and hence a Hopf bifurcation occurs at τ = τ 0 [21].

The full characterization of the direction and stability of the bifurcating periodic solution for the delayed system (1) is cumbersome but can be done following the approach of [22, 23]. In Section 8 we illustrate the nature of Hopf bifurcation through numerical simulations.

## 7 Optimal Control

Optimal control with delays is a subject under strong current research [24, 25, 26], in particular with respect to applications in biological control systems [27, 28, 29]. Our main aim here is to find the optimal profile u 1 ( t ) and u 2 ( t ) to minimize the cost of biopesticides used in pest control. We introduce the parameters u 1 ( t ) and u 2 ( t ) as control parameters: u 1 ( t ) is an admissible control representing the efficiency of pesticide being used and u 2 ( t ) characterizes the cost of the awareness campaign. The control induced state system is given as follows:

<!-- formula-not-decoded -->

 subject to initial conditions (2). We want to minimize the pest and also the cost of pest management. With this in mind, we define the cost functional for the minimization problem as

<!-- formula-not-decoded -->

subject to the control system (26). The parameters B i , i = 1 , 2, represent a weight constant on the benefit of the cost of production, while C is the penalty multiplier. Our aim is to find the optimal control u ∗ ( · ) = ( u 1 ( · ) , u 2 ( · )) such that

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

The Pontryagin Minimum Principle with delays in the state system can be found in [30, 31] and references therein, providing necessary optimality conditions for our delayed optimal control problem. Roughly speaking, Pontryagin's Principle reduces problem (26)-(29) to a problem of minimizing the Hamiltonian H given by

<!-- formula-not-decoded -->

Precisely, the following theorem characterizes the solution of our delayed optimal control problem.

Theorem 13 (Necessary optimality conditions for the delayed optimal control problem) . Let u ∗ be solution to the optimal control problem (26) -(29) and ( X ∗ , S ∗ , I ∗ , A ∗ ) be the corresponding (optimal) state. Then there exist multipliers ξ 1 , ξ 2 , ξ 3 and ξ 4 that satisfy the adjoint system

<!-- formula-not-decoded -->

 where τ = max { τ 1 , τ 2 } , subject to the transversality conditions ξ i ( t f ) = 0 , i = 1 , . . . , 4 . Moreover, the optimal control is given by

<!-- formula-not-decoded -->

Proof. The result is a direct consequence of the Pontryagin Minimum Principle with delays, which asserts that the solution to the delayed optimal control problem satisfies the adjoint equations

<!-- formula-not-decoded -->

and the transversality conditions ξ i ( t f ) = 0, i = 1 , 2 , 3 , 4. Moreover, according to the Pontryagin Minimum Principle, when the optimal control u ∗ takes values on (0 , 1), then ∂H ∂u i ( t ) = 0 , i = 1 , 2. Now, taking partial differentiation of (30) with respect to u 1 and u 2 , we get

<!-- formula-not-decoded -->

Using the boundedness of the controls, i.e., the fact that admissible controls take values such that 0 ≤ u i ( t ) ≤ 1 , i = 1 , 2, it follows from the minimality condition of Pontryagin's Principle that

<!-- formula-not-decoded -->

The proof is complete.

State system (26) subject to (2) is an initial value problem while the co-state system (31) subject to the transversality conditions ξ i ( t f ) = 0, i = 1 , . . . , 4, is a terminal value problem. For this reason, one solves numerically the boundary value problem given by Theorem 13 through forward iteration in the state system while the co-state system (31) is integrated through backward iteration [32]. Numerical results are given in Section 8.3.

## 8 Numerical Simulations

In this section, we provide numerical simulations obtained from the application of our analytical results, as given in previous sections. To illustrate the behavior of model (1), we did numerical simulations with the set of parameter values in Table 1. Some of these values are estimated from [1, 11, 33]. We begin by simulating the system without delays, then with delays.

## 8.1 Numerical simulations of the stability of equilibria

The parameters of model (1) used in the numerical simulations are given in Table 1. The initial values are chosen as

<!-- formula-not-decoded -->

where τ = max { τ 1 , τ 2 } .

Figure 1: Stability behavior of the endemic state for the non-delayed population system (1), i.e., when τ 1 = 0 and τ 2 = 0.

<!-- image -->

When we choose τ 1 = 0 and τ 2 = 0, the behavioral patterns of the densities of susceptible pest, infected pest, crop biomass, and aware population are presented taking the parameters from Table 1. All the system populations oscillate initially and finally become asymptotically stable and converge to the endemic state value (see Figure 1). Here, it is to be noted that all conditions of Theorem 7 are satisfied and thus the coexistence equilibrium E ∗ is stable.

Figure 2 contains the contour plot of the basic reproduction number R 0 , given by Theorem 4, as a function of the awareness active rate h and global awareness rate ω . The region where E ∗ exists and E 1 is stable are identified. We see that if both h and ω are large, then the coexistence equilibria E ∗ will not be feasible but the pest-free equilibrium E 1 is feasible and stable as R 0 &lt; 1 there. Consequently, a transcritical bifurcation occurs at R 0 = 1. This is also clear from Figure 3.

Figure 2: Plot of the basic reproduction number R 0 as a function of h and ω . All other parameters are as in Table 1.

<!-- image -->

Figure 3: Forward bifurcation. Plot of the basic reproduction number R 0 as a function of S and I . All other parameters are as in Table 1. Coexisting equilibrium E ∗ exists for R 0 &gt; 1 and for R 0 &lt; 1 it is not feasible but pest-free equilibrium E 1 is stable.

<!-- image -->

Figure 4 displays the effect of local awareness rate a on the steady state values of the model populations (without delay). As expected, we see that awareness of population is increased as the value of a increases and the uninfected pest population decreases.

Figure 4: Effect of local awareness, a , on the nondelayed system (1) with values of the other parameters given in Table 1.

<!-- image -->

## 8.2 Numerical simulations with different time delays

In this part, we examine the influence of the time delays on the number of infected pest by performing some numerical simulations.

When the time delay τ 2 = 0 is fixed and τ 1 takes values τ 1 = 6 and τ 1 = 16, respectively, we observe that oscillation increases as τ 1 increases and periodic oscillation is seen at τ 1 = 16 days (see Figure 5). Stability switch occurs through Hopf bifurcation.

In Figure 6, the time delay τ 1 = 0 is fixed and τ 2 takes value τ 2 = 16. We see a similar result as the one of Figure 5.

For any combination of τ 1 and τ 2 , when τ 1 + τ 2 = 16, periodic oscillation (Hopf bifurcation) can be seen. Figure 7 confirms that the Hopf bifurcation is of supercritical type.

Figures 5, 6 and 7 indicate that the populations always oscillate initially and ultimately approach towards their equilibrium values when τ 1 &lt; τ 0 = 16. This indicates that the number of pest will be high and sometimes low. If the value of delay, τ i , exceeds its critical value, τ 0 = 16 days approximately, the population becomes periodic. In this situation, it is very difficult to make the prediction about the size of the epidemic. Hence, these figures indicate that the endemic equilibrium E ∗ of model system (1) with delay is stable for τ &lt; τ 0 and unstable for τ &gt; τ 0 . For τ &gt; τ 0 , bifurcating periodic solutions are observed. This is in agreement with Theorem 12.

In Figure 8, the region of stability in the λ -τ 2 parameter plane is shown. The critical value of τ 2 , for which Hopf bifurcation occurs, depends on the consumption rate λ . The critical value of τ 2 decreases as λ increases.

Figure 5: The behavior of the model population for different values of τ 1 and fixed τ 2 = 0. Red line represents τ 1 = 6 and blue line represents τ 1 = 16. Other parameters are as in Figure 1.

<!-- image -->

Figure 6: The behavior of the model population for τ 2 = 16 and fixed τ 1 = 0.

<!-- image -->

Figure 7: Supercritical bifurcation. The behavior of the solution for different initial conditions and τ 1 = 16. Phase portrait converges to the same limit cycle.

<!-- image -->

Figure 8: Region of stability in the λ -τ 2 parameter plane. Other parameters are as in Table 1.

<!-- image -->

## 8.3 Numerical simulations of optimal control

Finally, we solve numerically the optimality system (Theorem 13) and we display the results found graphically. The parameters of model (26) and (31) are given in Table 1 and the initial values for (26) chosen as in (35). The weight constants of the objective functional are selected, for illustrative purposes, as B = 1 2 , B 2 = 1 2 and C = 1. The optimal system (26) has been solved numerically and the results have been displayed diagrammatically. As already remarked at the end of Section 7, this optimal system is a two-point boundary value problem (BVP) with separated boundary conditions at times t = 0 and t = t f . An efficient technique to solve two-point BVPs numerically is the collocation method [34, 35]. A suitable collocation code is given by solver bvp4c of the MATLAB numerical computing environment, which can be used to solve nonlinear two-point

BVPs. Solving our system requires an iterative scheme developed by [36]. This involves the use of an appropriate algorithm. Let h &gt; 0 be the discretization step size and let us consider integers ( n, m ) ∈ N 2 with τ = mh and t f = nh . In our programming we consider m knots to the left of 0 and to the right of t f , and we obtain the following partition:

<!-- formula-not-decoded -->

Then, we have t i = ih , -m ≤ i ≤ n + m . Next we define the state and adjoint variables X ( t ), S ( t ), I ( t ), A ( t ), ξ 1 ( t ), ξ 2 ( t ), ξ 3 ( t ), ξ 4 ( t ), and control u ( t ) in terms of the nodal points. Now, a combination of forward and backward difference approximations is applied to obtain the solutions. To demonstrate the consequences numerically, we select the set of parameters of Table 1.

The optimal control function u ∗ = ( u ∗ 1 , u ∗ 2 ) is intended in such a way that it minimizes the cost functional given by (27). In Figure 9, we present the numerical solutions of the population class with control. We operate the control through insecticide spraying up to 100 days. Crop biomass increased and pest population decreased significantly with the influence of the optimal profiles of global awareness and awareness based control activity, as shown in Figure 9. It is also observed that susceptible pest population goes to extinction within first 90 days due to effort of optimal control. Thus, optimal control by means of awareness-based biocontrol is of great value in controlling a pest problem is a crop field.

The Pontryagin controls are shown in Figure 10. We see they are bang-bang controls.

Figure 9: Numerical solution of the optimal control problem with τ 1 = 0, τ 2 = 40, and remaining parameter values from Table 1.

<!-- image -->

Figure 10: Numerical approximation of the Pontryagin extremal controls u ∗ 1 and u ∗ 2 (32).

<!-- image -->

## 9 Discussion and Conclusion

In this paper, a mathematical model has been proposed and analyzed to study the effect of awareness programs on the control of pests in agricultural practice. Namely, the model has for populations the density of crop biomass, density of susceptible pests, infected pests, and selfaware population. We suppose that self-aware people adopt biological control as integrated pest management as it is eco-friendly and less injurious to human health. With this approach, the susceptible pest is made infected. Also, we presume that infected pests cannot harm the crop. For this, awareness campaigns are taken as relative to the density of susceptible pests present in the crop field. There might be a delay in measuring the density of susceptible pests or in organizing awareness programs. Thus, we have included time delays in the modeling process.

The proposed model exhibits three equilibria: (i) the origin, which is always unstable, (ii) the pest-free equilibria, which are stable if the basic reproduction number R 0 is less than one while for R 0 &gt; 1 it becomes unstable, (iii) the endemic equilibrium, which exists and is, as well, stable for R 0 &lt; 1. From our analytical and numerical study, we observed that the most significant parameters involved in the system are a and τ , respectively the awareness population growth rate and the combined time delay. If the impact of awareness campaigns increases, the density of crop increases. As a consequence, pest prevalence declines. On the other hand, endemic equilibrium is locally stable when the delay is less than its critical value, i.e., when τ &lt; τ 0 = 44 . 5, approximately. The system loses its stability when τ &gt; τ 0 and a Hopf-bifurcation occurs at τ = τ 0 . In conclusion, raising awareness among people with tolerable time delay may be a good aspect for the optimal control of a pest in the crop field, decreasing the serious issues that pesticides have on human health and surroundings.

It remains open the question of how to define a Lyapunov function to prove global stability for the proposed delayed model. In this direction, the techniques of [37] should be helpful. This is under investigation and will be addressed elsewhere.

## Acknowledgements

Abraha acknowledges Adama Science and Technology University for its hospitality and support during this work through the research grant ASTU/SP-R/027/19. Torres is grateful to the financial support from the Portuguese Foundation for Science and Technology (FCT), through CIDMA and project UIDB/04106/2020. The authors are very grateful to two anonymous reviewers for valuable remarks and comments, which significantly contributed to the quality of the paper.

## References

- [1] Bhattacharyya S, Bhattacharya DK. Pest control through viral disease: mathematical modeling and analysis. J. Theoret. Biol. 238 (2006), no. 1, 177-197.
- [2] Franz JM, Huber J. Feldversuche mit insektenpathogenen viren in Europa. Entomophaga 24 (1979), no. 4, 333-343 .
- [3] van den Bosch R, Messenger PS, Gutierrez AP. Microbial Control of Insects, Weeds, and Plant Pathogens. In: An Introduction to Biological Control, Springer, Boston, MA, 1982, 59-74.
- [4] Naranjo SE, Ellsworth PC, Frisvold GB. Economic value of biological control in integrated pest management of managed plant systems. Annual Review of Entomology 60 (2015), 621645.
- [5] Al Basir F, Ray S, Venturino E. Role of media coverage and delay in controlling infectious diseases: a mathematical model. Appl. Math. Comput. 337 (2018), 372-385.
- [6] Khan GA, Muhammad S, Khan MA. Information regarding agronomic practices and plant protection measures obtained by the farmers through electronic media. Journal of Animal and Plant Sciences 23 (2013), no. 2, 647-650.
- [7] Kumar M, Kuppast I, Mankani K, Prakash K, Veershekar T. Use and awareness of pesticides in Malnad Region of Karnataka. J. Pharm. Res. 5 (2012), no. 7, 3875-3877.
- [8] van Lenteren JC, Bale J, Bigler F, Hokkanen HMT, Loomans AJM. Assessing risks of releasing exotic biological control agents of arthropod pests. Annu. Rev. Entomol. 51 (2006), 609-634.
- [9] Yang X, Wang F, Meng L, Zhang W, Fan L, Violette G, Coen JR, Farmer and retailer knowledge and awareness of the risks from pesticide use: a case study in the Wei river catchment, China. Science of The Total Environment 497 (2014), 172-179.
- [10] Le Bellec F, Rajaud A, Ozier-Lafontaine H, Bockstaller C, Malezieux E. Evidence for farmers' active involvement in co-designing citrus cropping systems using an improved participatory method. Agronomy for Sustainable Development 32 (2012), no. 3, 703-714.
- [11] Al Basir F, Venturino E, Roy PK. Effects of awareness program for controlling mosaic disease in Jatropha curcas plantations. Math. Methods Appl. Sci. 40 (2017), no. 7, 2441-2453.
- [12] Chowdhury J, Al Basir F, Takeuchi Y, Ghosh M, Roy PK. A mathematical model for pest management in Jatropha curcas with integrated pesticides: An optimal control approach. Ecological Complexity 37 (2019), 24-31.
- [13] Silva CJ, Torres DFM, Venturino E. Optimal spraying in biological control of pests. Math. Model. Nat. Phenom. 12 (2017), no. 3, 51-64. arXiv:1704.04073
- [14] Elazzouzi A, Lamrani Alaoui A, Tilioua M, Torres DFM. Analysis of a SIRI epidemic model with distributed delay and relapse. Stat. Optim. Inf. Comput. 7 (2019), no. 3, 545-557. arXiv:1812.09626
- [15] Al Basir F, Banerjee A, Ray S. Role of farming awareness in crop pest management-a mathematical model. J. Theoret. Biol. 461 (2019), 59-67.
- [16] Al Basir F. A multi-delay model for pest control with awareness induced interventions-Hopf bifurcation and optimal control analysis, International Journal of Biomathematics 13 (2020), no. 6, 2050047, 22 pp.

- [17] Al Basir F, Ray S. Impact of farming awareness based roguing, insecticide spraying and optimal control on the dynamics of mosaic disease. Ricerche di Matematica 69 (2020), 393412.
- [18] Al Basir F, Blyuss KB, Ray S. Modelling the effects of awareness-based interventions to control the mosaic disease of Jatropha curcas . Ecological Complexity 36 (2018), 92-100.
- [19] Yang X, Chen L, Chen J. Permanence and positive periodic solution for the single-species nonautonomous delay diffusive models. Comput. Math. Appl. 32 (1996), no. 4, 109-116.
- [20] Hassard BD, Kazarinoff ND, Wan YH. Theory and applications of Hopf bifurcation , London Mathematical Society Lecture Note Series, 41, Cambridge University Press, Cambridge, 1981.
- [21] Freedman HI, Sree Hari Rao V. The trade-off between mutual interference and time lags in predator-prey systems. Bull. Math. Biol. 45 (1983), no. 6, 991-1004.
- [22] Al Basir F, Elaiw AM, Ray S. Effect of time delay in controlling crop pest using farming awareness. Int. J. Appl. Comput. Math. 5 (2019), no. 4, Paper No. 110, 19 pp.
- [23] Riad D, Hattaf K, Yousfi N. Mathematical analysis of a delayed IS-LM model with general investment function. The Journal of Analysis 27 (2019), no. 4, 1047-1064.
- [24] Benharrat M, Torres DFM. Optimal control with time delays via the penalty method. Math. Probl. Eng. 2014 (2014), Art. ID 250419, 9 pp. arXiv:1407.5168
- [25] Frederico GSF, Torres DFM. Noether's symmetry theorem for variational and optimal control problems with time delay. Numer. Algebra Control Optim. 2 (2012), no. 3, 619-630. arXiv:1203.3656
- [26] Lemos-Pai˜ ao AP, Silva CJ, Torres DFM. A sufficient optimality condition for non-linear delayed optimal control problems. Pure Appl. Funct. Anal. 4 (2019), no. 2, 345-361. arXiv:1804.06937
- [27] Allali K, Harroudi S, Torres DFM. Analysis and optimal control of an intracellular delayed HIV model with CTL immune response. Math. Comput. Sci. 12 (2018), no. 2, 111-127. arXiv:1801.10048
- [28] Silva CJ, Maurer H, Torres DFM. Optimal control of a tuberculosis model with state and control delays. Math. Biosci. Eng. 14 (2017), no. 1, 321-337. arXiv:1606.08721
- [29] Silva CJ, Maurer H. Optimal control of HIV treatment and immunotherapy combination with state and control delays. Optimal Control Appl. Methods 41 (2020), no. 2, 537-554.
- [30] G¨ ollmann L, Kern D, Maurer H. Optimal control problems with delays in state and control variables subject to mixed control-state constraints. Optimal Control Appl. Methods 30 (2009), no. 4, 341-365.
- [31] Rodrigues F, Silva CJ, Torres DFM, Maurer H. Optimal control of a delayed HIV model. Discrete Contin. Dyn. Syst. Ser. B 23 (2018), no. 1, 443-458. arXiv:1708.06451
- [32] Campos C, Silva CJ, Torres DFM. Numerical optimal control of HIV transmission in Octave/MATLAB. Math. Comput. Appl. 25 (2020), no. 1, 20 pp. arXiv:1912.09510
- [33] Chowdhury J, Al Basir F, Pal J, Roy PK. Pest control for Jatropha curcas plant through viral disease: a mathematical approach. Nonlinear Stud. 23 (2016), no. 4, 517-532.
- [34] Laarabi H, Abta A, Hattaf K. Optimal control of a delayed SIRS epidemic model with vaccination and treatment. Acta Biotheoretica 63 (2015), no. 2, 87-97.

- [35] Almoaeet MK, Shamsi M, Khosravian-Arab H, Torres DFM. A collocation method of lines for two-sided space-fractional advection-diffusion equations with variable coefficients. Math. Methods Appl. Sci. 42 (2019), no. 10, 3465-3480. arXiv:1902.09267
- [36] Hattaf K, Yousfi N. Optimal control of a delayed HIV infection model with immune response using an efficient numerical method. ISRN Biomath 2012 (2012), Art. ID 215124, 7 pp.
- [37] Hattaf K. Global stability and Hopf bifurcation of a generalized viral infection model with multi-delays and humoral immunity. Phys. A 545 (2020), 123689, 14 pp.