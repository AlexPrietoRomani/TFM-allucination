---
id: arxiv-2510.06111
title: An additional food driven biological control patch model, incorporating generalized competition
year: 2025
country: Internacional
source: ArXiv (q-bio.PE)
doc_type: Artículo científico
language: en
tags:
  - control biológico
  - manejo de plagas
  - clima
  - especies invasoras
  - artículo científico
  - ArXiv
  - agronomía de campo
---

## An additional food driven biological control patch model, incorporating generalized competition

Urvashi Verma 1 , Kanishka Goyal 1 , Chanaka Kottegoda 2 , Rana D. Parshad 1 ∗

1) Department of Mathematics, Iowa State University, Ames, IA 50011, USA

2)Department of Mathematics and Physics, Marshall University, Huntington, WV 25755, USA

## Abstract

Additional food sources for an introduced predator are known to increase its efficiency on a target pest. In this context, inhibiting factors such as interference, predator competition, and the introduction of temporally dependent quantity and quality of additional food are all known to enable pest extinction. As climate change and habitat degradation have increasing effects in enhancing patchiness in ecological systems, the effect of additional food in patch models has also been recently considered. However, the question of complete pest extinction in such patchy systems remains open. In the current manuscript, we consider a biological control model where additional food drives competition among predators in one patch, and they subsequently disperse to a neighboring patch via drift or dispersal. We show that complete pest extinction in both patches is possible. Further, this state is proved to be globally asymptotically stable under certain parametric restrictions. We also prove a codimension-2 Bogdanov-Takens bifurcation. We discuss our results in the context of designing pest management strategies under enhanced climate change and habitat fragmentation. Such strategies are particularly relevant to control invasive pests such as the Soybean aphid ( Aphis glycines ), in the North Central United States.

Keywords: Additional food, biological control, patch model, drift, dispersal, global stability, higher codimension bifurcation.

## 1. Introduction

Invasive species and pests are a major global concern, causing substantial annual crop damage [1, 2], and posing serious environmental and economic threats [3, 4, 5]. Managing them is challenging, and while there are several control strategies, chemical treatments constitute a significant share of these [6]. This is despite their negative environmental effects, such as pest species developing resistance [7, 8]. Thus, there is a need for alternative strategies that are eco-friendly, such as top-down or classical biological control. This method involves introducing a natural enemy of the targeted pest species [9, 10], to suppress the pest population, thereby decreasing the frequent use of insecticides [11]. In cases when the introduced predator fails to reduce the pest population to the desired level, its effectiveness can be improved through several methods, one of which is providing additional food (AF) to the predator, different from the targeted prey [12, 13]. Several mathematical models have been formulated to describe predatorpest dynamics with AF [14, 15, 16, 17, 18, 19, 20], suggesting that providing a sufficient quantity of high-quality AF to the predator will result in pest extinction. However, AF-mediated models with species movement mechanisms such as dispersal and drift have been far less investigated.

Climate change can have direct and indirect influences on species movement [21], since the decision to disperse can be affected by changes in the speed of wind [22], in storm conditions [23], and in flooding events [24]. This type of movement mechanism can be categorized as drift, where the flow of water/direction of wind determines the direction of movement, typically from

∗ Corresponding author

Email addresses: uverma@iastate.edu (Urvashi Verma 1 ), kgoyal@iastate.edu (Kanishka Goyal 1 ), kottegoda@marshall.edu (Chanaka Kottegoda 2 ), rparshad@iastate.edu (Rana D. Parshad 1 )

an upstream to a downstream location. Species can also disperse for food, mates, and resources [25], and several studies incorporate dispersal in prey-predator systems, including dispersal in only one species and dispersal linked to predation [26, 27]. Fragmentation of natural habitat due to human intervention will result in a growing number of habitat 'patches", and species will often disperse between these small interactive 'patches." To this end, patch models have been intensely investigated [28, 29] as the dynamics of prey-predator systems in a two or multipatch setting with dispersal between patches can differ from those where only a single patch is considered [30, 31]. Recent research has also explored drift in aquatic ecosystems with network structures, so in multi-patch environments, as well as in eco-epidemic systems with dispersal [32, 33, 34]. Evidence from the landscape ecology literature suggests that natural enemies of pests are more abundant in smaller patches adjacent to crop fields [35]. Spatial arrangements such as landscape heterogeneity and providing alternative food sources to natural enemies are promising approaches not only for biological pest control, but they also support biodiversity conservation [36, 37, 38]. This combined strategy is often referred to as 'landscape features supporting natural pest control" (LF-NPC). Among other landscape management practices, one is the strategy of planting prairie strips, small sections (about 10-20 % ) of crop fields dedicated to various plants instead of the primary crop. STRIPS (Science-based Trails of Row Crops Integrated with Prairie Strips) is an ongoing project pioneered and led in Iowa [39] that explores how integrating a small percentage of prairie into row crops significantly improves soil and water quality, boosts biodiversity, and is among the most affordable conservation practices for farm landowners [40]. Literature suggests that this AF source ' boosts' predators' energy, driving their dispersal out of the AF patch, into the crop field [41, 42]. Conversely, the AF can also act as an attractant for predators wanting to disperse out of the crop field into the AF patch, particularly if the AF provides better nutritional diversity [43]. Thus, the inclusion of dispersal and drift in prey-predator patch models with an AF source is increasingly relevant, as it strongly affects species distribution, population dynamics, and overall ecosystem functioning [44, 45] - particularly under enhanced effects of climate change and habitat fragmentation. Biological control strategies are effective, but they have limitations. These include the risk of an unbounded predator population [46] and effects on non-target species [47]. In these situations, competition between predators can act as a natural self-regulating system [48]. Prairie strips adjacent to crop fields offer predators nutritious resources like nectar and pollen, along with suitable microclimatic conditions and refuge [49, 50, 51]. However, these strips are usually much smaller than the crop fields and exist in limited patches. This can lead to predators gathering in the strips, increasing local predator density. As a result, competition for resources in the prairie or space limitations may increase intraspecific competition among predators. A recent study explored intraspecific competition in the presence of additional food under type IV response [52].

The following general model for an introduced predator population y ( t ) preying on a target pest population x ( t ) , also provided with an additional food source of quantity ξ and quality 1 α , has been proposed in the literature [14, 15, 17],

<!-- formula-not-decoded -->

Here, f ( x, ξ, α ) is the functional response of the predator, which depends on both pest and additional food. Likewise, g ( x, ξ, α ) is the numerical response of the predator. Earlier literature on AF has shown that increasing ξ beyond a threshold ξ critical in models of type (1.1) yields pest extinction. Due to the positivity of solutions, trajectories will converge onto the predator axis, and this can occur in minimal time [15, 17, 20, 53]. Subsequently, it was shown that pest extinction only occurs in infinite time [46], and can also result in infinite time blow-up of the predator population [54]. The type III response has been considered in a number of AF models, [18, 19], but an adaptation of the results in [46] shows pest extinction can occur asymptotically but only at the cost of unbounded growth of the introduced predator. The model defined in equation 1.1, with type II response and constant predator harvesting with rate ρ , is studied in [55]. If ρ &gt; 0 , then up to two interior equilibria can exist, with an unstable axial pest-free state, and finite time extinction of the predator is achievable for certain initial conditions. Several codimension-one

bifurcations exist (Hopf and saddle-node) along with a codimension-two Bogdanov-Takens bifurcation. However, the behavior for large initial data above the stable manifold of the interior saddle equilibrium remains unresolved. To prevent unbounded predator growth, several predatordependent inhibitory mechanisms have been proposed. These include prey defense through type IV functional response [20], predator interference by the Beddington-DeAngelis functional response [16, 56], purely ratio-dependent response [57, 58], and intraspecific predator competition [54]. In Prasad et al. [16], the model was considered with the Beddington-DeAngelis functional response [59] that incorporates mutual interference. In case of high interference, there is always one unique interior equilibrium - if a feasible pest-free equilibrium exists, it is a saddle, making pest eradication unfeasible. For low interference, predator density remains bounded, and up to one interior equilibrium exists depending upon the quantity of AF. Pest-free and interior equilibria may coexist, with the pest-free state being always a saddle. A predator-free equilibrium can also exist, and a pest-free state is globally stable when the quantity of additional food exceeds a certain threshold. Recent work [56] shows pest extinction is achievable in a tighter parametric regime.

For many decades, people have used bifurcation theory as a tool in understanding how variations in a system's parameters can cause qualitative changes in the dynamical system [60, 61, 62]. Many researchers, [63, 64], have studied and analyzed complex predator-prey models with nonlinear functional responses, and have proven that these models often exhibit rich bifurcation structures, including Hopf, saddle-node, and Bogdanov-Takens (BT) bifurcations. In particular, BT point acts as an organizing center from where critical bifurcations emerge, such as homoclinic loops and multiple limit cycles [65, 66, 67]. Even a small perturbation in parameters can flip the system's behavior from stable co-existence to oscillations or even to extinction states. In complex predator-prey systems, these rich bifurcation structures help to predict changes in regime and design biologically feasible pest management strategies. Of particular interest are bifurcations of higher codimension, wherein qualitative behavior of a system changes as two or more parameters vary. For instance, [68], in a generalist predator model with alternative food source, identify degenerate Hopf (codim-3) and Bogdanov-Takens (codim-4) bifurcations; [69] establish a codim-3 BT bifurcation in a constant-yield harvesting setting; [70] find Hopf (codim-2) and BT (codim-2 and 3) bifurcations in models with type II response and predator release; and [71, 72] uncover nilpotent cusp (codim-3), degenerate Hopf, and heteroclinic (codim-2) bifurcations in predator-prey systems with Allee effects under generalized type III and IV functional responses. However, in the context of AF models, the literature has results on primarily codimension one bifurcations [14, 15, 17] - that is, qualitative changes as the quantity or quality of the AF vary, or perhaps predator birth or death rates, or prey carrying capacity vary.

Competition, among predators, is ubiquitous in natural systems [73]. Previous studies have shown that including predator competition in predator-prey models can generate much richer dynamics than without such competition [74, 67, 66]. In [75], a two-patch prairie-crop field model with predator movement was considered. Sufficient drift and dispersal were found to prevent predator blow-up, and with drift, the pest extinction in the crop field was proved to be globally stable under certain parametric conditions. Overall pest densities in the two-patch system were lower than in classical AF-only or classical predator-prey models; however, the complete pest extinction state in both patches could not be achieved with either drift or dispersal. Thus, although such movement is crucial to many ecological processes, and heightened due to climate change and habitat fragmentation, complete pest extinction has not been achieved in AF (multi) patch models thus far - it is only seen in single patch models, primarily with interference mechanisms, and competition. Also, higher codimension bifurcations for AF models are much less reported in the literature, to the best of our knowledge [54].

Motivated by these findings, we consider a two-patch model where intraspecific competition among predators initiates because of the presence of additional food in the AF patch (prairie strip), and the other patch (crop field) follows the classical prey-predator dynamics. Note, although classical predator competition is modeled as a -y 2 term, in the predator state ( y ), we consider -y p , 1 &lt; p ≤ 2 . This enables us to generalize the competition term to cover applications such as hyperbolic mortality, nonlinear harvesting, generalized competition/interference [76, 77,

78, 79]. The special case p = 2 covers the case of classical competition. The mathematical analysis for the drift model is provided in Section 2, and the analysis for the dispersal model is detailed in Section 3. Section 4 presents bifurcation analysis of higher codimension. Section 5 discusses future directions and summarizes the main findings with biological implications.

Our primary contributions in the current manuscript are as follows,

- Two novel AF biological control models with patch structure (2.1) and (3.1), are introduced. Here, the additional food triggers generalized intraspecific competition among predators in the AF patch (prairie strip). The predators then move to the neighboring crop field patch via drift, (2.1) or dispersal (3.1).
- Complete pest extinction state in both patches is proved to be globally asymptotically stable with both drift and dispersal (see Theorem 4 and Theorem 9), respectively.
- Pest extinction in the crop field is globally asymptotically stable with drift via Theorem 7.
- The patch model enables pest extinction in the crop field with dispersal via Lemma 8.
- Wealso consider a single-patch system (4.1), where we show the existence of the codimension2 Bogdanov-Takens bifurcation (see Theorem 10). This bifurcation signifies a critical threshold for qualitative changes in predator-prey dynamics, including the emergence of oscillatory behavior in both pest and predator populations.
- We discuss the implications of our results in controlling certain key invasive pests, such as the soybean aphid ( Aphis glycines ), in the North-Central United States.

## 2. Modeling Drift Between Ω 1 &amp; Ω 2

We next derive the biological control model, considered in the current manuscript. Motivated by pest management tactics and strategies, such as the STRIPS program, we consider two patches that make up our landscape: a crop field ( Ω 2 ), the larger unit, and a prairie strip ( Ω 1 ), the smaller unit. The prairie strip, by design, possesses row crops that provide additional food, such as nectar and pollen, to the predator, which would enhance its effectiveness in targeting the pest that resides primarily in the crop field. The introduction of additional food initiates the competition among predators with an intraspecific rate c . The function f ( ξ ) = ξ drives the competitive interactions amongst predators. The crop field has no AF. Because of the different in sizes of patches Ω 1 and Ω 2 , we have two different carrying capacities k p and k c . Thus, for the patch Ω 1 , the quantity of AF is ξ and the quality of AF is 1 α . So, in Ω 1 , we have an AFdriven predator-pest system with pest density as x 1 and predator density as y 1 . In Ω 2 , we have the classical prey-predator system since ξ = 0 , and the pest density is x 2 and predator density is taken as y 2 . The functional response chosen here is the classical Holling type II functional response.

<!-- formula-not-decoded -->

The assumption on drift rates is that the predators will drift away from Ω 1 into Ω 2 . The rate of drift out of the prairie strip ( Ω 1 ) is q 1 , and the rate at which predators 'arrive" or are drifted into crop field ( Ω 2 ) is q 2 . Here, the drift is driven by flooding or wind.

Figure 1: Drift: Pest extinction in both patches. Fig. 1a is the time series plot showing pest extinction in both patches Ω 1 and Ω 2 while predator populations reach an equilibrium level for the drift model (2.1). Figs. 1b and 1c represent the prey and predator nullclines in patch Ω 1 and Ω 2 , respectively. The parameters used are k p = 10 , k c = 50 , α = 0 . 1 , ξ = 0 . 99 , /epsilon1 1 = 0 . 3 , /epsilon1 2 = 0 . 5 , δ 2 = 0 . 12 , q 1 = 0 . 25 , q 2 = 0 . 1 , c = 0 . 006 , p = 2 with I.C., x 1 (0) = 30 , y 1 (0) = 30 , x 2 (0) = 30 , y 2 (0) = 30 .

<!-- image -->

## 2.1. Mathematical Analysis

Theorem 1. Assume the parameters k p , k c , /epsilon1 1 , /epsilon1 2 , ξ, α are all positive and the drift rates q 1 , q 2 are non-negative. Then, the model (2.1) is positively invariant in R 4 + .

<!-- formula-not-decoded -->

We now consider the existence and local stability analysis of the biologically relevant equilibrium points for the system (2.1). The Jacobian matrix ( ˆ J ) for (2.1) is given by:

<!-- formula-not-decoded -->

## 2.1.1. Pest-free state in both Ω 1 &amp; Ω 2

Lemma 1.

The equilibrium point

<!-- formula-not-decoded -->

Lemma 2. The equilibrium point ˆ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is locally asymptotically stable when, y ∗ 1 &gt; max { δ 2 q 2 , 1 + αξ } .

<!-- formula-not-decoded -->

## 2.1.2. Pest-free state only in Ω 2

Lemma 3. The equilibrium point ˆ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) exists if /epsilon1 1 ξ &lt; A (1+ αξ ) and /epsilon1 1 &gt; A where A = q 1 + cξ ( y ∗ 1 ) p -1 .

<!-- formula-not-decoded -->

Lemma 4. The equilibrium point ˆ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) is conditionally locally asymptotically stable.

<!-- formula-not-decoded -->

E

1

= (0

ˆ

, y

∗

1

,

, y

0

∗

2

)

exists if

ξ &gt;

/epsilon1

1

q

1

-

αq

1

and

/epsilon1

1

&gt; α

δ

(

1

+

q

1

.

)

Figure 2: Drift: Pest extinction only in the crop field patch. Fig. 2a is the time series plot showing the pest extinction in the crop field patch Ω 2 after oscillations and the populations in Ω 1 reaching an equilibrium level for the drift model (2.1). Figs. 2b and 2c represent the prey and predator nullclines in patch Ω 1 and Ω 2 , respectively. The parameters used are k p = 2 , k c = 20 , α = 0 . 48 , ξ = 0 . 2 , /epsilon1 1 = 0 . 45 , /epsilon1 2 = 0 . 8 , δ 2 = 0 . 09 , q 1 = 0 . 224 , q 2 = 0 . 1 , c = 0 . 006 , p = 2 with I.C., x 1 (0) = 30 , y 1 (0) = 30 , x 2 (0) = 30 , y 2 (0) = 30 .

<!-- image -->

2.2. Global stability of the equilibrium point ˆ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 )

Remark 1. The two-patch model (2.1) can be considered as two distinct patches, as the dynamics in Ω 1 are not affected by populations in Ω 2 , and when the predator population in Ω 1 reaches an equilibrium level, it can be considered as a constant predator stocking in Ω 2 .

Remark 2. Fig. 1 shows the time series plot of model (2.1) where pest extinction occurs in both Ω 1 and Ω 2 , and the nullclines plot of both the patches, showing that the prey and predator nullclines do not intersect with each other, and gives the pest extinction state.

2.2.1. Pest-free state in the patch Ω 1

Theorem 2. Consider the following parametric restriction on c, c &lt; c ∗ = min { c ∗ 1 , c ∗ 2 , c ∗ 3 , c ∗ 4 } where, c ∗ 1 = ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) p ) 1 p -1 , c ∗ 2 = ( q 2 δ 2 ) p -1 ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) ) , c ∗ 3 = ( /epsilon1 1 -q 1 ξ )( 4 k p (1+ αξ + k p ) 2 ) p -1 and , c ∗ 4 = h ( x ) 2 -p ξ ( 4 /epsilon1 1 (1+ αξ -ξ ) ( p -1)(1+ k p + αξ ) 2 ) p -1 ( k p k p -(1+ αξ ) ) p -1 , then the equilibrium point (0 , y ∗ 1 ) is globally stable.

Proof. From Lemma 2, we should have y ∗ 1 &gt; max { δ 2 q 2 , 1 + αξ } else this equilibrium point will be unstable. This will hold if the following two conditions are also satisfy in terms of the parameter c .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The equations representing dynamics in patch Ω 1 for (2.1) are given by:

<!-- formula-not-decoded -->

We also need that the maximum of the prey ( x 1 ) nullcline is below the horizontal asymptote

of the predator ( y 1 ) nullcline, which requires the following inequality to hold,

<!-- formula-not-decoded -->

Now, in order to avoid the existence of an interior equilibrium point, the prey and predator nullclines should not intersect. Thus, we require that the predator nullcline g ( x 1 ) remain higher than the prey nullcline f ( x 1 ) on the interval x 1 ∈ [0 , 1 2 ( k p -1 -αξ )] . A sufficient condition for this is g (0) ≥ f (0) and min g ′ ( x 1 ) &gt; max f ′ ( x 1 ) for x 1 ∈ [0 , 1 2 ( k p -1 -αξ )] . The minimum of g ′ ( x 1 ) occurs at x 1 = 1 2 ( k p -1 -αξ ) , and the maximum of f ′ ( x 1 ) occurs at x 1 = 0 . Then, using these values and finding the inequality that satisfies the above condition is,

<!-- formula-not-decoded -->

where h ( x ) = /epsilon1 1 ( x 1 + ξ 1+ x 1 + αξ ) -q 1 . Thus, for no interior equilibrium to exist, we require taking the minimum of (2.3), (2.4), (2.6), and (2.7). Thus, only boundary ( k p , 0) and trivial (0 , 0) equilibria exist, which are saddle and unstable, respectively. Thus, no periodic orbit exists.

## 2.2.2. Pest-free state in the patch Ω 2

The equations representing dynamics in patch Ω 2 are given by:

<!-- formula-not-decoded -->

Using the value of y ∗ 1 from (7.2) we have,

<!-- formula-not-decoded -->

where G 1 represents the constant predator stocking [80]. We state the following lemma,

Theorem 3. Consider the system (2.9) . Then under the parametric restriction /epsilon1 2 &gt; δ 2 ( 1 -1 k c ) and , δ 2 &lt; q 2 ( /epsilon1 1 ξ -q 1 (1+ αξ ) cξ (1+ αξ ) ) 1 p -1 , we have that the pest free state (0 , y ∗ 2 ) in the crop field to (2.9) , is globally attracting for any positive ( x 2 (0) , y 2 (0)) .

Proof. From the prey nullcline in patch Ω 2 we have,

<!-- formula-not-decoded -->

and from the predator nullcline in patch Ω 2 we have,

<!-- formula-not-decoded -->

The constant predator stocking in terms of parameters can be written as,

/negationslash

<!-- formula-not-decoded -->

The critical stocking rate for which the equilibrium reaches the pest-free state is given by [80],

<!-- formula-not-decoded -->

Now, the pest extinction state in the crop field Ω 2 is possible for all initial conditions if,

<!-- formula-not-decoded -->

This proves the lemma.

Theorem 4. Consider the following parametric restrictions, c &lt; c ∗ = min { c ∗ 1 , c ∗ 2 , c ∗ 3 , c ∗ 4 } , /epsilon1 2 &gt; δ 2 ( 1 -1 k c ) and, δ 2 &lt; q 2 ( /epsilon1 1 ξ -q 1 (1+ αξ ) cξ (1+ αξ ) ) 1 p -1 where, c ∗ 1 = ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) p ) 1 p -1 , c ∗ 2 = ( q 2 δ 2 ) p -1 ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) ) , c ∗ 3 = ( /epsilon1 1 -q 1 ξ )( 4 k p (1+ αξ + k p ) 2 ) p -1 and , c ∗ 4 = h ( x ) 2 -p ξ ( 4 /epsilon1 1 (1+ αξ -ξ ) ( p -1)(1+ k p + αξ ) 2 ) p -1 ( k p k p -(1+ αξ ) ) p -1 then the equilibrium point ˆ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is globally stable.

Proof. The proof follows from Theorem 2 and 3.

2.3. Global stability of the equilibrium point ˆ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 )

Remark 3. Considering the two-patch model (2.1) as two distinct patches, we make use of the Dulac criterion to exclude the possibility of periodic orbits and establish the interior equilibrium as globally stable in Ω 1 , and the pest extinction state in Ω 2 is proved globally stable via constant predator stocking.

Remark 4. Fig. 2 shows the time series plot of model (2.1) , where the dynamics in Ω 1 exhibit coexistence and the pest extinction state is achieved in Ω 2 . The nullclines plot of both patches shows that the prey and predator nullclines intersect, yielding a stable interior equilibrium in patch Ω 1 , and in patch Ω 2 , the nullclines do not intersect, giving rise to the pest extinction state.

2.3.1. Coexistence state in the patch Ω 1

Theorem 5. Consider the parametric restriction ξ &gt; q 1 /epsilon1 1 -αq 1 , c &gt; ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) p ) 1 p -1 and let D be the region defined as, D = { ( x 1 , y 1 ) ∈ R 2 + ∣ ∣ 0 &lt; x 1 &lt; k p , 0 &lt; y 1 &lt; y min } and if 1 &lt; p &lt; 2 where y min = min { ( /epsilon1 1 -q 1 cξ ) 1 p -1 , ( 1 2 ξc (1+ αξ )( p -1) ) 1 p -2 } then, only one interior equilibrium exists and that is globally attracting. When p = 2 , then, for the interior equilibrium to be globally attracting, we require the following parametric restriction to hold, c &gt; 1 2 ξ (1+ αξ ) .

Proof. In order for the interior equilibrium to exist, we have the following condition from Lemma 3.

<!-- formula-not-decoded -->

We will now use the Dulac criterion to exclude the existence of periodic orbits. Consider the

<!-- formula-not-decoded -->

auxiliary function φ ( x 1 , y 1 ) = 1 x 1 y 1 ,

<!-- formula-not-decoded -->

Thus, we require

<!-- formula-not-decoded -->

and since p -2 &lt; 0 if p = 2 we get an upper bound on y 1 ,

<!-- formula-not-decoded -->

Now, for the case when p = 2 , the interior equilibrium is globally attracting if the following parametric restriction is satisfied, c &gt; 1 2 ξ (1+ αξ ) . Thus, via the Dulac criterion, the limit cycles would not exist. Looking at the patch Ω 1 , the extinction state (0 , 0) is an unstable node and the predator-free state ( k p , 0) is a saddle, based on the parametric restriction mentioned on ξ .

1

Also, the pest extinction state (0 , y ∗ ) will be a saddle if c &gt; ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) p ) p -1 , see Lemma 2. Therefore, the only interior equilibrium that exists is globally attracting.

## 2.3.2. Pest-free state in the patch Ω 2

From equation (2.8) and using the value of y ∗ 1 from (7.5) we have,

<!-- formula-not-decoded -->

Theorem 6. Consider the system (2.12) . Then under the parametric restriction /epsilon1 2 &gt; δ 2 ( 1 -1 k c )

and , δ 2 &lt; q 2   /epsilon1 1 ( x ∗ 1 + ξ 1+ x ∗ 1 + αξ ) -q 1 cξ   1 p -1 , we have that the pest free state (0 , y ∗ 2 ) in the crop field to (2.9) , is globally attracting for any positive ( x 2 (0) , y 2 (0)) .

Proof. From the predator nullcline in patch Ω 2 , we have,

<!-- formula-not-decoded -->

From equation (2.9) we know that the system can be written in the form of a constant predator

/negationslash

stocking represented by G 2 . The expression of y ∗ 1 is written in terms of x ∗ 1 because finding an explicit expression in terms of parameters is not feasible due to non nonlinearity involved. The constant predator stocking is then given by,

/negationslash

The critical stocking rate for which the equilibrium reaches the pest-free state is given by [80],

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now, the pest free state in the crop field patch Ω 2 is possible for all initial conditions if,

<!-- formula-not-decoded -->

This proves the lemma.

Theorem 7. Let D be the region, D = { ( x 1 , y 1 ) ∈ R 2 + ∣ ∣ 0 &lt; x 1 &lt; k p , 0 &lt; y 1 &lt; y min } and, consider the parametric restrictions in patch Ω 1 , ξ &gt; q 1 /epsilon1 1 -αq 1 , c &gt; ( /epsilon1 1 ξ -q 1 (1+ αξ ) ξ (1+ αξ ) p ) 1 p -1 and if p ∈ (1 , 2) where y min = min { ( /epsilon1 1 -q 1 cξ ) 1 p -1 , ( 1 2 ξc (1+ αξ )( p -1) ) 1 p -2 } , when p = 2 , we need c &gt; 1 2 ξ (1+ αξ ) and the following parametric restriction in patch Ω 2 , /epsilon1 2 &gt; δ 2 ( 1 -1 k c ) and , δ 2 &lt; q 2   /epsilon1 1 ( x ∗ 1 + ξ 1+ x ∗ 1 + αξ ) -q 1 cξ   1 p -1 , then the equilibrium point ˆ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) is globally stable.

Proof. The proof follows from Theorem 5 and 6.

## 3. Modeling Dispersal Between Ω 1 &amp; Ω 2

<!-- formula-not-decoded -->

Here, the assumptions on patches Ω 1 &amp; Ω 2 are the same as mentioned in Section 2. The predators now disperse between the two patches, where q 1 is the rate predators move out of the prairie strip ( Ω 1 ) after gaining energy from additional food and then enter the crop field ( Ω 2 ) at a rate of q 2 . Similarly, the predators disperse out of the crop field since AF can act as an attractant, at a rate of q 3 , and enter the strip with a rate of q 4 . The assumption here on dispersal rates are q 2 ≤ q 1 and q 4 ≤ q 3 . Note, if q 3 = q 4 = 0 then the model reduces to the drift model (2.1).

Figure 3: Dispersal: Pest extinction in both patches. Fig. 3a is the time series plot showing pest extinction in both patches Ω 1 and Ω 2 while predator populations reach an equilibrium level for the dispersal model (3.1). Figs. 3b and 3c represent the prey and predator nullclines in patch Ω 1 and Ω 2 , respectively. The parameters used are k p = 10 , k c = 50 , α = 0 . 1 , ξ = 0 . 99 , /epsilon1 1 = 0 . 3 , /epsilon1 2 = 0 . 8 , δ 2 = 0 . 12 , q 1 = 0 . 158 , q 2 = 0 . 05 , q 3 = 0 . 15 , q 4 = 0 . 1 , c = 0 . 006 , p = 2 with I.C., x 1 (0) = 30 , y 1 (0) = 30 , x 2 (0) = 30 , y 2 (0) = 30 .

<!-- image -->

## 3.1. Mathematical Analysis

Theorem 8. Assume the parameters k p , k c , /epsilon1 1 , /epsilon1 2 , ξ, α are all positive and the dispersal rates q 1 , q 2 , q 3 , q 4 are non-negative. Then, the model (3.1) is positively invariant in R 4 + .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We now consider the existence and local stability analysis of the biologically relevant equilibrium points for the system (3.1). The Jacobian matrix ( ˜ J ) for the additional food patch model (3.1) is given by: (3.2)

<!-- formula-not-decoded -->

## 3.1.1. Pest-free state in both Ω 1 &amp; Ω 2

Lemma 5. The equilibrium point ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) exists if ξ &gt; B /epsilon1 1 -αB , and , /epsilon1 1 -αB &gt; 0 where B = q 1 -q 4 q 2 δ 2 + q 3 .

<!-- formula-not-decoded -->

Lemma 6. The equilibrium point ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is locally asymptotically stable if, y ∗ 1 &gt; max { δ 2 + q 3 q 2 , 1 + αξ } .

Proof.

<!-- formula-not-decoded -->

## 3.1.2. Pest-free state only in Ω 2

Lemma 7. The equilibrium point ˜ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) exists if if /epsilon1 1 ξ &lt; D (1 + αξ ) and /epsilon1 1 &gt; D where, D = cξ ( y ∗ 1 ) p -1 + q 1 -q 4 q 2 δ 2 + q 3 .

<!-- formula-not-decoded -->

Lemma 8. The equilibrium point ˜ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) is conditionally locally asymptotically stable.

<!-- formula-not-decoded -->

Figure 4: Dispersal: Pest extinction only in the crop field patch. Fig. 4a is the time series plot showing the pest extinction in the crop field patch Ω 2 and coexistence in the patch Ω 1 for the dispersal model (3.1). Figs. 4b and 4c represent the prey and predator nullclines in patch Ω 1 and Ω 2 , respectively. The parameters used are k p = 15 , k c = 60 , α = 0 . 7 , ξ = 1 . 5 , /epsilon1 1 = 0 . 3 , /epsilon1 2 = 0 . 8 , δ 2 = 0 . 02 , q 1 = 0 . 258 , q 2 = 0 . 18 , q 3 = 0 . 1 , q 4 = 0 . 08 , c = 0 . 08 , p = 2 with I.C., x 1 (0) = 30 , y 1 (0) = 30 , x 2 (0) = 30 , y 2 (0) = 30 .

<!-- image -->

Remark 5. Fig. 4 shows the time series plot of (3.1) , where the dynamics in Ω 1 exhibit coexistence and the pest extinction state is achieved in Ω 2 . The nullclines plot of both patches shows that the prey and predator nullclines intersect, yielding a stable interior equilibrium in patch Ω 1 , and in patch Ω 2 , the nullclines do not intersect, giving rise to the pest extinction state due to constant predator stocking.

3.2. Global stability of the equilibrium point ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 )

Remark 6. Fig. 3 shows the time series plot of model (3.1) where pest extinction occurs in both Ω 1 and Ω 2 , and the nullclines plot of both the patches, showing that the prey and predator nullclines do not intersect with each other, yielding the pest extinction states in both patches.

Theorem 9. If y ∗ 1 &gt; max { δ 2 + q 3 q 2 , 1 + αξ } then, the equilibrium point ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is globally asymptotically stable.

Proof. Let D be the region where, D = { ( x 1 , y 1 , x 2 , y 2 ) ∈ R 4 + | x 1 ≥ 0 , y 1 ≥ 0 , x 2 ≥ 0 , y 2 ≥ 0 } . We define a function, L ( x 1 , x 2 , y 1 , y 2 ) = /epsilon1 1 x 1 + /epsilon1 2 x 2 + y 1 + y 2 , which is non-negative and L →∞ as || ( x 1 , y 1 , x 2 , y 2 ) || → ∞ , so radially unbounded. Upon differentiating L along the positive solutions of (3.1),

<!-- formula-not-decoded -->

Canceling the interaction terms involving /epsilon1 1 and /epsilon1 2 gives,

<!-- formula-not-decoded -->

Notice, 1 + x 1 + αξ ≥ 1 + αξ and from the assumptions on the dispersal rates in model (3.1) we have, q 2 ≤ q 1 and q 4 ≤ q 3 , this implies -q 1 y 1 + q 2 y 1 ≤ 0 , q 4 y 2 -q 3 y 2 ≤ 0 so, ( q 4 -q 3 -δ 2 ) y 2 ≤ 0 then,

<!-- formula-not-decoded -->

Since the max for the logistic terms involving x 1 , x 2 occurs at k p 2 , k c 2 respectively. Also, for initial conditions x 1 (0) , x 2 (0) &gt; 0 , the logistic dynamics ensures that 0 &lt; x 1 ( t ) &lt; k p and 0 &lt; x 2 ( t ) &lt; k c , for all sufficiently large t , and any perturbation from the respective carrying capacities decays to zero as t →∞ . Therefore, any deviation can be absorbed into a vanishing term /epsilon1 ( t ) → 0 . Then, we have the following bounds,

<!-- formula-not-decoded -->

Neglecting the vanishing term /epsilon1 ( t ) in the long-term limit gives,

<!-- formula-not-decoded -->

We require, f ( y 1 ) ≤ 0 = ⇒ C 1 + C 2 y 1 ≤ cξy p 1 . Since 1 &lt; p ≤ 2 , the right-hand side grows faster than the linear terms on the left side. This inequality will hold for y 1 ≥ M , where M is given by the exact solution where f ( y 1 ) = 0 . Thus, there exists a threshold value M for which f ( y 1 ) &lt; 0 . So, the bounded subset of D can be written as, Ω = { ( x 1 , y 1 , x 2 , y 2 ) ∈ D | L ( x 1 , x 2 , y 1 , y 2 ) ≤ L 0 , x 1 ≤ k p , y 1 ≥ M, x 2 ≤ k c } , where L 0 = L ( x 1 (0) , x 2 (0) , y 1 (0) , y 2 (0)) and we have ˙ L ≤ 0 on this domain Ω . This has been checked graphically as well, see Fig. 5. After surpassing the threshold of y 1 , we observed f ( y 1 ) &lt; 0 . Now, look at the set where ˙ L = 0 so from (3.3) we have,

<!-- formula-not-decoded -->

/negationslash

Note that the points where x 1 = k p , x 1 = k c are not invariant under the flow and can not belong to the omega limit set for y 1 , y 2 = 0 . So, in the invariant set, we only have x 1 = x 2 = 0 . And now, y 1 , y 2 should satisfy the reduced system.

<!-- formula-not-decoded -->

The above equation only holds at the equilibrium point values, since from (7.7) using the value of y ∗ 2 and from (7.8) using the expression for y ∗ 1 we have,

<!-- formula-not-decoded -->

But we already know,

<!-- formula-not-decoded -->

So, the largest invariant set E where ˙ V = 0 is,

<!-- formula-not-decoded -->

So, by LaSalle's invariance principle, since L is radially unbounded and ˙ L ≤ 0 in a positively invariant region Ω , and the largest invariant set where ˙ L = 0 being the singleton equilibrium point ˜ E 1 so, all solution trajectories approach ˜ E 1 . Thus, from Lemma 6, if y ∗ 1 &gt; max { δ 2 + q 3 q 2 , 1 + αξ } , the equilibrium point ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is globally asymptotically stable.

Figure 5: This figure shows that beyond the threshold value M , which is represented by the black dotted line, the function f ( y 1 ) &lt; 0 since the RHS (blue curve) grows faster than the LHS (red curve), making ˙ L ≤ 0 in Ω . The parameters used are k p = 10 , k c = 50 , α = 0 . 1 , ξ = 0 . 99 , /epsilon1 1 = 0 . 3 , /epsilon1 2 = 0 . 8 , δ 2 = 0 . 12 , q 1 = 0 . 158 , q 2 = 0 . 05 , q 3 = 0 . 15 , q 4 = 0 . 1 , c = 0 . 006 , p = 2 .

<!-- image -->

## 4. Single Patch Analysis and Bifurcation Structure

We now restrict our attention to a single-patch version of the model to conduct a detailed bifurcation analysis. In this reduced setting, we consider the dynamics of the pest and predator populations within one patch in the presence of additional food, but in the absence of inter-patch movement.

The simplified system is given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

To make our system biologically admissible, we consider (4.1) in the region R 2 + = { ( x, y ) | x ≥ 0 , y ≥ 0 } . Also, it can be seen that the region

<!-- formula-not-decoded -->

∣ of system (4.1) is positively invariant and bounded, ensuring that solutions starting within it remain nonnegative and bounded for all t ≥ 0 .

Three equilibrium points lie on the boundary ∂ R : D 0 = (0 , 0) , representing the extinction of both species; D k p = ( k p , 0) , representing the extinction of the predator population; and D y = (0 , y ) , where y = ( /epsilon1 c ( αξ +1) ) 1 p -1 , representing a pest-free state where the predator persists due to the presence of additional food and is well-defined as c &gt; 0 , α &gt; 0 and ξ &gt; 0 . The equilibrium D y exists for 1 &lt; p ≤ 2 .

## 4.1. Linear Analysis

The Jacobian matrix for (4.1) at any equilibrium point ( x ∗ , y ∗ ) is given by:

<!-- formula-not-decoded -->

For the interior equilibrium E = ( x ∗ , y ∗ ) with y ∗ = F ( x ∗ ) , we have

<!-- formula-not-decoded -->

♥✂✄✄☎✄✆♥✝

Figure 6: Existence of interior equilibria via nullcline intersections. Parameters used: α = 0 . 2 , ξ = 0 . 5 , c = 0 . 20456 , /epsilon1 = 0 . 23153 . 6a k p = 7 , p = 1 . 9 : one interior equilibrium; 6b k p = 7 , p = 1 . 8 : three interior equilibria; 6c k p = 4 . 32857 , p = 2 : three interior equilibria within a restricted range of prey density. Boundary equilibria are omitted.

<!-- image -->

<!-- formula-not-decoded -->

To locate the positive interior equilibrium, we solve the equation

<!-- formula-not-decoded -->

The existence of interior equilibria can be visualized via nullcline intersections ( see Fig. 6). Depending on the parameter regime, the system admits either a single positive equilibrium (see Fig. 6a) or up to three distinct equilibria (see Figs. 6b-6c). Define

<!-- formula-not-decoded -->

Then, differentiating g ( x ∗ ) yields (4.7)

<!-- formula-not-decoded -->

Solving equation (4.5) for c , we obtain:

<!-- formula-not-decoded -->

Substituting this expression for c into (4.7) and determinant equation, we get:

<!-- formula-not-decoded -->

Thus, the determinant of the Jacobian at the interior equilibrium can be written compactly as:

<!-- formula-not-decoded -->

Remark 7. As illustrated in Fig. 6c, the existence of three interior equilibria for p = 2 has also been reported in a related predator-prey system that incorporates a predator death term (see

[54]). In our setting, a similar multiplicity of equilibria is present, but without the predator's death term.

## 4.2. Bogdanov-Takens bifurcation: cusp of order 2

For the system (4.1) to exhibit a Bogdanov-Takens (BT) bifurcation at an interior equilibrium ( x ∗ , y ∗ ) , the Jacobian M at ( x ∗ , y ∗ ) must have a double zero eigenvalue in a single Jordan block. This implies that both the determinant and the trace of the Jacobian matrix M vanish simultaneously. That is,

<!-- formula-not-decoded -->

From (4.10),

<!-- formula-not-decoded -->

Solving g ′ ( x ∗ ) = 0 for k p , we obtain the critical value:

<!-- formula-not-decoded -->

Next, the trace of the Jacobian matrix is given by

(4.13)

<!-- formula-not-decoded -->

Solving tr ( M ) = 0 for /epsilon1 yields the critical value:

(4.14)

<!-- formula-not-decoded -->

To ensure that both parameters k ∗ p and /epsilon1 ∗ are positive, the following conditions must hold for x ∗ &gt; 0 , α &gt; 0 , ξ &gt; 0 , and 1 &lt; p ≤ 2 :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We now show that when ( k p , /epsilon1 ) = ( k ∗ p , /epsilon1 ∗ ) , the equilibrium E = ( x ∗ , F ( x ∗ )) is a cusp singularity of codimension2 . To establish this, we require the following lemma [61].

Lemma 9. Any system of the form

<!-- formula-not-decoded -->

is equivalent to the system

<!-- formula-not-decoded -->

Theorem 10. For any choice of x ∗ &gt; 0 , α &gt; 0 , ξ &gt; 0 , and 1 &lt; p ≤ 2 satisfying conditions (4.15) -(4.16) , the equilibrium E = ( x ∗ , F ( x ∗ )) is a cusp singularity of codimension2 precisely when ( k p , /epsilon1 ) = ( k ∗ p , /epsilon1 ∗ ) .

Proof. We begin by shifting coordinates via the affine transformation x 1 = x -x ∗ and y 1 = y -F ( x ∗ ) , which brings the equilibrium E = ( x ∗ , F ( x ∗ )) to the origin. Expanding the system in a Taylor series around E , we obtain the following reduced system:

<!-- formula-not-decoded -->

Under the Bogdanov-Takens (BT) bifurcation conditions, (4.20)

<!-- formula-not-decoded -->

system (4.19) simplifies to

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

From the first BT condition in equation (4.20), we have

<!-- formula-not-decoded -->

Since r ( x ∗ ) &gt; 0 , this implies F ′ ( x ∗ ) &gt; 0 and hence

<!-- formula-not-decoded -->

/negationslash

Similarly, the second BT condition in equation (4.20) yields

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

Hence, to bring the system (4.21) to a more canonical form, we apply the transformation

<!-- formula-not-decoded -->

which directly implies

Figure 7: Fig. 7a shows the behavior of the normal-form coefficient β 2 for α = 0 . 20 and ξ = 0 . 50 . The dashed line marks β 2 = 0 ; the red dot indicates the sign change at x ∗ ≈ 0 . 537 . The green star highlights the equilibrium abscissa used in Fig. 7b, x ∗ = 0 . 36336 , where β 2 = 0 . 159438 &gt; 0 (vertical dotted line). Fig. 7b Phase portrait of system (4.1) with ( k ∗ p , /epsilon1 ∗ , c, p ) = (4 . 16 , 0 . 23153 , 0 . 20456 , 2) and the same ( α, ξ ) as in Fig. 7a. Trajectories from the I.C.s, (0 . 20465 , 1 . 20529) (blue) and (0 . 44465 , 1 . 37748) (red), converge to a unique attracting periodic orbit (stable limit cycle), while the interior equilibrium E = (0 . 36336 , 1 . 33550) (black dot) is an unstable focus enclosed by the cycle. Together, the figures indicate that for these parameters the model lies in the regime β 2 &gt; 0 and exhibits a stable limit cycle surrounding the unstable equilibrium.

<!-- image -->

Under this change of variables, the system becomes

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

Using lemma (9), the system (4.23) is transformed to the standard normal-form:

<!-- formula-not-decoded -->

where the normal-form coefficients are given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

Therefore, if β 1 β 2 = 0 , the E = ( x ∗ , F ( x ∗ )) is a cusp singularity of codimension2 , and the system exhibits a codimension2 Bogdanov-Takens bifurcation.

Remark 8. The signs of the normal-form coefficients β 1 and β 2 depend on the underlying parameter values ( x ∗ , α, ξ, p ) and hence on the expressions for k ∗ p and /epsilon1 ∗ . Thus, both β 1 and β 2 can be either positive or negative depending on the specific choice of these parameters.

## 5. Discussion &amp; Conclusion

In this study, we develop and analyze a two-patch biological control model - this is relevant to model current innovative agricultural practice in a landscape containing a prairie strip ( Ω 1 ) and a crop field ( Ω 2 ). This is motivated by recent innovative developments in landscape management, such as the STRIPS program. We posit the following assumptions: (i) only predators can move between patches; while prey stay in the crop field; (ii) predator movement between Ω 1 and Ω 2 is modeled via drift (2.1) and dispersal (3.1); (iii) AF initiates generalized competition among predators within the prairie strip. The effect of drift and dispersal between the two patches has been studied, and the biological implications of the results have also been analyzed.

When the predators move via drift, away from Ω 1 and into Ω 2 , then the complete pest extinction state in both patches is globally stable under certain parametric conditions via Theorem 4; (see Fig. 1). The conditions outlined in Theorem 4 indicate that the intraspecific competition rate c needs to be less than a certain threshold, suggesting that the competition among predators must be weak enough and that drift into the crop field must be fast enough to compensate for predators' mortality for the result to hold. The pest extinction only in the crop field is also globally stable via Theorem 7; (see Fig. 2) suggests that the predator competition should be greater than a threshold so that the prey-predator can coexist in Ω 1 . Also, the drift into Ω 2 should be sufficient to eradicate the pest from the crop field. Similar outcomes were observed when predators dispersed between the patches in both directions. Complete pest eradication is globally asymptotically stable via Theorem 9; (see Fig. 3) indicating that the predator density in Ω 1 should be high enough to keep a constant predation pressure on the pest. The interaction of predators between patches also drives predators in Ω 2 above a certain level, which helps eliminate pests from the crop field. Lemma 7 provides the existence of pest extinction only in the crop field state and the related local stability via Lemma 8 for model 3.1; (see Fig. 4).

/negationslash

In section 4, we conducted a detailed bifurcation analysis for the single-patch model 4.1 in the presence of additional food supplements to reveal how predator-prey dynamics change with biological parameters. In particular, we established the conditions for the existence of a codimension2 Bogdanov-Takens (BT) bifurcation via Theorem 10. This BT bifurcation corresponds to the parameter regime where the Jacobian at an interior equilibrium point has a double zero eigenvalue, signaling the onset of rich and intricate local behavior. It also acts as an organizing center from which multiple dynamical phenomena can emerge. In its unfolding, one typically observes the appearance of saddle-node bifurcations and homoclinic loops - each contributing to qualitative changes such as the birth or destruction of limit cycles, bistability, and sharp transitions. Fig. 7 shows the emergence of a stable limit cycle, which corresponds to long-term, sustained oscillations in pest and predator populations, representing ecological scenarios where neither species goes extinct nor settles to a steady state. The presence of limit cycles in the vicinity of the BT point is essential for developing some robust pest control strategies that are resilient to disturbances in the environment. In this work, we restricted our analysis to the generic case β 1 β 2 = 0 , which leads to a codimension-2 Bogdanov-Takens bifurcation. The degenerate case β 1 β 2 = 0 may involve higher codimension bifurcations and more complex local dynamics, but lies outside the scope of the current work and remains a direction for future study. Furthermore, in the current work, we consider the regime 1 &lt; p ≤ 2 for the -y p generalized competition-type term. It remains as future work to investigate the regime 0 &lt; p &lt; 1 . This is a more delicate regime to handle, due to the possibility of finite time extinction dynamics, and its ensuing, often counterintuitive effect on the competitive dynamics [81, 82].

The summary of our findings illustrates that intraspecific competition among predators can be beneficial for pest extinction in a crop field, which is the primary area of concern from a biological control perspective. This result is of importance to the control of invasive pests such as the soybean aphid, which has plagued soybean crops since its first detection in the United States in Wisconsin in July 2000 [83]. The main predator of the soybean aphid is the Asian Beetle ( Harmonia Axyridis ), which is known to have evolved several aggressive traits, making it a fierce inter and intraspecific competitor [84]. Thus, a possible nuanced strategy is to plant certain AF that Harmonia Axyridis prefers in prairie strips adjoining soybean crop fields. Herein, as increased precipitation is predicted in the Midwestern US [85], drift between adjoining fields,

due to vectors such as flooding, becomes increasingly important. Also, a possible direction of current and future interest is to consider interspecific competition among various biological control agents, such as predators, parasitoids, pathogens, and combinations thereof [86]. These could include the effects of intraguild predation. As noted earlier, we have proved the existence of a BT2 bifurcation in the AF (single) patch setting. We expect this result to hold in the case of linear drift. In addition, the presence of limit cycles that occur in the vicinity of the BT point is relevant to maintaining a cyclical population of predators. In terms of application to the soybean aphid and its chief predator Harmonia Axyridis , one can consider the /epsilon1 -k p parameters. Next, we can infer /epsilon1 , the conversion efficiency of the predator from the literature - then choose an appropriate k p , which essentially governs the 'size" of the prairie strip, so that we stay in a feasible BT2 regime. This method would enable an AF patch of appropriate size, so that we could maintain a cyclical population of predators, dispersing/drifting into an adjoining soybean field, to target the aphid. All in all, we believe our results have value in designing tactics and strategies relevant to the practical control of various current invasive pests. These strategies are particularly relevant considering the increasing effects of climate change, and the evolution of dispersal strategies for pests, as habitat fragmentation continues to increase the patchiness of agricultural landscapes.

## 6. Funding

UV, KG, and RP acknowledge valuable partial support by the Agricultural and Food Research Initiative grant no. 2023-67013-39157 from the USDA National Institute of Food and Agriculture.

## 7. Appendix

## 7.1. Proof of Theorem 1

Proof. From the differential equations of x 1 , x 2 we have, ˙ x 1 | x 1 =0 = 0 , ˙ x 2 | x 2 =0 = 0 . And same reasoning applies to ˙ y 1 we have ˙ y 1 | y 1 =0 = 0 . Now for ˙ y 2 we have ˙ y 2 = q 2 y 1 if y 2 = 0 and this implies ˙ y 2 | y 2 =0 ≥ 0 if y 1 ≥ 0 . Therefore, by Theorem A. 4 in [87], the model (3.1) is positive invariant in R 4 + .

## 7.2. Proof of Lemma 1

Proof. From the nullcline ˙ y 2 = 0 we have,

<!-- formula-not-decoded -->

From the nullcline ˙ y 1 = 0 we have,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

/negationslash

Thus, the equilibrium point ˆ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) exists if ξ &gt; q 1 /epsilon1 1 -αq 1 and, /epsilon1 1 &gt; αq 1 .

## 7.3. Proof of Lemma 2

Proof. Using (7.2), the general Jacobian matrix (2.2) at (0 , y ∗ 1 , 0 , y ∗ 2 ) becomes,

<!-- formula-not-decoded -->

Now the characteristic equation is given as,

<!-- formula-not-decoded -->

λ 1 = cξ (1 -p )( y ∗ 1 ) p -1 &lt; 0 ⇔ p &gt; 1 (which is true) , λ 2 = 1 -y ∗ 2 &lt; 0 ⇔ y ∗ 2 &gt; 1 ⇔ y ∗ 1 &gt; δ 2 q 2 ,

<!-- formula-not-decoded -->

Therefore, ˆ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) is locally asymptotically stable if y ∗ 1 &gt; max { δ 2 q 2 , 1 + αξ } .

## 7.4. Proof of Lemma 3

Proof. From the nullcline ˙ y 2 = 0 we have,

<!-- formula-not-decoded -->

From the nullcline ˙ x 1 = 0 , either x ∗ 1 = 0 or,

<!-- formula-not-decoded -->

Now, using the predator nullcline in patch Ω 1 ,

<!-- formula-not-decoded -->

∴ either y ∗ = 0

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving the above equation for x ∗ 1 , we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, the equilibrium point E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) exists if /epsilon1 1 ξ &lt; A (1 + αξ ) and /epsilon1 1 &gt; A .

where A is defined by,

<!-- formula-not-decoded -->

ˆ

## 7.5. Proof of Lemma 4

Proof. The general Jacobian matrix (2.2) at ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) becomes,

<!-- formula-not-decoded -->

The characteristic polynomial is,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now the characteristic equation becomes,

<!-- formula-not-decoded -->

To satisfy the Routh-Hurwitz stability criteria for all negative roots, we should have the following conditions:

<!-- formula-not-decoded -->

Thus, if all the conditions mentioned in equation (7.6) are satisfied, then the lemma is proved.

## 7.6. Proof of Theorem 8

Proof. From the differential equations of x 1 , x 2 we have, ˙ x 1 | x 1 =0 = 0 , ˙ x 2 | x 2 =0 = 0 . And looking at ˙ y 1 we have ˙ y 1 = q 4 y 2 if y 1 = 0 and this implies ˙ y 1 | y 1 =0 ≥ 0 if y 2 ≥ 0 , applying the same logic for ˙ y 2 we have, ˙ y 2 | y 2 =0 ≥ 0 if y 1 ≥ 0 . Therefore, by Theorem A. 4 in [87], the model (3.1) is positive invariant in R 4 + . Let D be the region where, D = { ( x 1 , y 1 , x 2 , y 2 ) ∈ R 4 + | x 1 ≥ 0 , y 1 ≥ 0 , x 2 ≥ 0 , y 2 ≥ 0 } .

## 7.7. Proof of Lemma 5

Proof. From the nullcline ˙ y 2 = 0 we have,

<!-- formula-not-decoded -->

and from ˙ y 1 = 0 ,

<!-- formula-not-decoded -->

Using the value of y ∗ 2 from (7.7),

<!-- formula-not-decoded -->

/negationslash

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So for positivity of y ∗ 1 we need, q 1 &lt; /epsilon1 1 ξ 1+ αξ + q 4 q 2 δ 2 + q 3 . Solving this for ξ gives, ξ &gt; q 1 -q 4 q 2 δ 2 + q 3 /epsilon1 1 -α ( q 1 -q 4 q 2 δ 2 + q 3 ) , provided /epsilon1 1 -α ( q 1 -q 4 q 2 δ 2 + q 3 ) &gt; 0 . Thus the equilibrium ˜ E 1 = (0 , y ∗ 1 , 0 , y ∗ 2 ) exists if ξ &gt; B /epsilon1 1 -αB , and , /epsilon1 1 -αB &gt; 0 where B = q 1 -q 4 q 2 δ 2 + q 3 .

## 7.8. Proof of Lemma 6

Proof. Using equation (7.8), the general Jacobian matrix (3.2) at (0 , y ∗ 1 , 0 , y ∗ 2 ) becomes,

<!-- formula-not-decoded -->

Now the characteristic equation is given as,

<!-- formula-not-decoded -->

λ

<!-- formula-not-decoded -->

## 7.9. Proof of Lemma 7

Proof. From the nullcline ˙ y 2 = 0 we have,

<!-- formula-not-decoded -->

Using the nullcline ˙ x 1 = 0 , either x ∗ 1 = 0 or,

<!-- formula-not-decoded -->

So, for y ∗ 1 &gt; 0 we should have, x ∗ 1 &lt; k p . Now, using the nullcline ˙ y 1 = 0 , and substituting the value of y ∗ 2 from (7.10) we have,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

{ }

∴ either y ∗ 1 = 0 or,

<!-- formula-not-decoded -->

Solving for x ∗ 1 we have,

<!-- formula-not-decoded -->

where D is defined by,

<!-- formula-not-decoded -->

Thus, the equilibrium point ˜ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) exists if /epsilon1 1 ξ &lt; D (1 + αξ ) and /epsilon1 1 &gt; D .

## 7.10. Proof of Lemma 8

Proof. Using (7.12) and (7.11) the general Jacobian matrix (3.2) at ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) becomes,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

˜ E 2 = cξ (1 -p )( y ∗ 1 ) p -1 -q 4 q 2 δ 2 + q 3 where ˜ B 2 &lt; 0 . The Jacobian matrix can now be written as,

<!-- formula-not-decoded -->

The characteristic polynomial comes out as:

<!-- formula-not-decoded -->

Further simplification gives us the following characteristic equation,

<!-- formula-not-decoded -->

Let ˜ F 2 = δ 2 + q 3 and, ˜ G 2 = cξ (1 -p )( y ∗ 1 ) p -1 ( δ 2 + q 3 ) . Rewriting the above equation gives,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

To satisfy Routh-Hurwitz stability criteria for all negative roots, the following conditions should hold,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, if all conditions mentioned from (7.16) - (7.20) hold the equilibrium point ˜ E 2 = ( x ∗ 1 , y ∗ 1 , 0 , y ∗ 2 ) is locally asymptotically stable.

## References

- [1] D. R. Paini, A. W. Sheppard, D. C. Cook, P. J. De Barro, S. P. Worner, M. B. Thomas, Global threat to agriculture from invasive species, Proceedings of the National Academy of Sciences 113 (27) (2016) 7575-7579, https://doi.org/10.1073/pnas.1602205113 .
- [2] D. Pimentel, R. Zuniga, D. Morrison, Update on the environmental and economic costs associated with alien-invasive species in the united states, Ecological economics 52 (3) (2005) 273-288, https://doi.org/10.1016/j.ecolecon.2004.10.002 .
- [3] T. W. Sappington, Emerging issues in integrated pest management implementation and adoption in the north central usa, Integrated Pest Management: Experiences with Implementation, Global Overview, Vol. 4 (2014) 65-97 https://doi.org/10.1007/978-94-007-7802-3\_4 .
- [4] M. E. O'Neal, A. J. Varenhorst, M. C. Kaiser, Rapid evolution to host plant resistance by an invasive herbivore: soybean aphid (aphis glycines) virulence in north america to aphid resistant cultivars, Current opinion in insect science 26 (2018) 1-7, https://doi.org/10.1016/j.cois.2017.12.006 .
- [5] A. Banerjee, I. Valmorbida, M. E. O'Neal, R. Parshad, Exploring the dynamics of virulent and avirulent aphids: A case for a 'within plant'refuge, Journal of economic entomology 115 (1) (2022) 279-288, https://doi.org/10.1093/jee/toab218 .

- [6] D. Pimentel, Environmental and economic costs of the application of pesticides primarily in the united states, Environment, development and sustainability 7 (2005) 229-252, https://doi.org/10.1007/s10668-005-7314-2 .
- [7] M. L. Hladik, A. R. Main, D. Goulson, Environmental risks and challenges associated with neonicotinoid insecticides, https://doi.org/10.1021/acs.est.7b06388 (2018).
- [8] C. Bass, I. Denholm, M. S. Williamson, R. Nauen, The global status of insect resistance to neonicotinoid insecticides, Pesticide biochemistry and physiology 121 (2015) 78-87, https://doi.org/10.1016/j.pestbp.2015.04.004 .
- [9] R. G. Van Driesche, T. S. Bellows, R. G. Van Driesche, T. S. Bellows, Pest origins, pesticides, and the history of biological control, Biological Control (1996) 320 https://doi.org/10.1073/pnas.1620229114 .
- [10] W. E. Snyder, D. H. Wise, Predator interference and the establishment of generalist predator populations for biocontrol, Biological Control 15 (3) (1999) 283-292, https://doi.org/10.1006/bcon.1999.0723 .
- [11] G. E. Heimpel, Y. Yang, J. D. Hill, D. W. Ragsdale, Environmental consequences of invasive species: greenhouse gas emissions of insecticide use and the role of biological control in reducing emissions, PLoS One 8 (8) (2013) e72293, https://doi.org/10.1371/journal.pone.0072293 .
- [12] M. W. Sabelis, P. C. Van Rijn, et al., When does alternative food promote biological pest control?, IOBC WPRS BULLETIN 29 (4) (2006) 195, https://hdl.handle.net/11245/1.266182 .
- [13] A. Tena, A. Pekas, D. Cano, F. L. Wäckers, A. Urbaneja, Sugar provisioning maximizes the biocontrol service of parasitoids, Journal of Applied Ecology 52 (3) (2015) 795-804, https://doi.org/10.1111/1365-2664.12426 .
- [14] P. Srinivasu, B. Prasad, M. Venkatesulu, Biological control through provision of additional food to predators: a theoretical study, Theoretical Population Biology 72 (1) (2007) 111-120, https://doi.org/10.1016/j.tpb.2007.03.011 .
- [15] P. Srinivasu, B. Prasad, Time optimal control of an additional food provided predator-prey system with applications to pest management and biological conservation, Journal of mathematical biology 60 (4) (2010) 591-613, https://doi.org/10.1007/s00285-009-0279-2 .
- [16] B. Prasad, M. Banerjee, P. Srinivasu, Dynamics of additional food provided predator-prey system with mutually interfering predators, Mathematical biosciences 246 (1) (2013) 176-190, https://doi.org/10.1016/j.mbs.2013.08.013 .
- [17] P. Srinivasu, B. Prasad, Role of quantity of additional food to predators as a control in predator-prey systems with relevance to pest management and biological conservation, Bulletin of mathematical biology 73 (10) (2011) 2249-2276, https://doi.org/10.1007/s11538-010-9601-9 .
- [18] P. Srinivasu, D. Vamsi, V. Ananth, Additional food supplements as a tool for biological conservation of predator-prey systems involving type iii functional response: A qualitative and quantitative investigation, Journal of theoretical biology 455 (2018) 303-318, https://doi.org/10.1016/j.jtbi.2018.07.019 .
- [19] P. Srinivasu, D. Vamsi, I. Aditya, Biological conservation of living systems by providing additional food supplements in the presence of inhibitory effect: a theoretical study using predator-prey models, Differential Equations and Dynamical Systems 26 (2018) 213-246, https://doi.org/10.1007/s12591-016-0344-4 .
- [20] V. Ananth, D. Vamsi, Achieving minimum-time biological conservation and pest management for additional food provided predator-prey systems involving inhibitory effect: A qualitative investigation, Acta Biotheoretica 70 (1) (2022) 1-51, https://doi.org/10.1007/s10441-021-09430-2 .
- [21] J. M. Travis, M. Delgado, G. Bocedi, M. Baguette, K. Bartoń, D. Bonte, I. Boulangeat, J. A. Hodgson, A. Kubisch, V. Penteriani, et al., Dispersal and species' responses to climate change, Oikos 122 (11) (2013) 1532-1540, https://doi.org/10.1111/j.1600-0706.2013.00399.x .
- [22] C. Thomas, P. Brain, P. Jepson, Aerial activity of linyphiid spiders: modelling dispersal distances from meteorology and behaviour, Journal of Applied Ecology (2003) 912927 https://doi.org/10.1046/j.1365-2664.2003.00844.x .

- [23] M.-A. Lea, D. Johnson, R. Ream, J. Sterling, S. Melin, T. Gelatt, Extreme weather events influence dispersal of naive northern fur seals, Biology letters 5 (2) (2009) 252-257, https://doi.org/10.1098/rsbl.2008.0643 .
- [24] E. A. Roche, C. L. Gratto-Trevor, J. P. Goossen, C. L. White, Flooding affects dispersal decisions in piping plovers (charadrius melodus) in prairie canada, The auk 129 (2) (2012) 296-306, https://doi.org/10.1525/auk.2012.11196 .
- [25] C. Cosner, Y. Lou, Does movement toward better environments always benefit a population?, Journal of mathematical analysis and applications 277 (2) (2003) 489-503, https://doi.org/10.1016/S0022-247X(02)00575-9 .
- [26] R. Arditi, C. Lobry, T. Sari, Asymmetric dispersal in the multi-patch logistic equation, Theoretical population biology 120 (2018) 11-15, https://doi.org/10.1016/j.tpb.2017.12.006 .
- [27] K. Messan, Y. Kang, A two patch prey-predator model with multiple foraging strategies in predators: Applications to insects, arXiv preprint arXiv:1511.04388 https://doi.org/10.3934/dcdsb.2017048 (2015).
- [28] J. Wu, O. L. Loucks, From balance of nature to hierarchical patch dynamics: a paradigm shift in ecology, The Quarterly review of biology 70 (4) (1995) 439-466, http://www.jstor.org/stable/3035824?origin=JSTOR-pdf .
- [29] D. H. Thornton, L. C. Branch, M. E. Sunquist, The influence of landscape, patch, and within-patch factors on species presence and abundance: a review of focal patch studies, Landscape Ecology 26 (2011) 7-18, https://doi.org/10.1007/s10980-010-9549-z .
- [30] S. A. Gourley, Y. Kuang, Two-species competition with high dispersal: the winning strategy, Math. Biosci. Eng 2 (2) (2005) 345-362, https://doi.org/10.3934/mbe.2005.2.345 .
- [31] F. S. Berezovskaya, B. Song, C. Castillo-Chavez, Role of prey dispersal and refuges on predator-prey dynamics, SIAM Journal on Applied Mathematics 70 (6) (2010) 1821-1839, https://doi.org/10.1137/080730603 .
- [32] S. Chen, J. Liu, Y. Wu, Evolution of dispersal in advective patchy environments with varying drift rates, SIAM Journal on Applied Dynamical Systems 23 (1) (2024) 696-720, https://doi.org/10.1137/22M1542027 .
- [33] S. Chen, J. Shi, Z. Shuai, Y. Wu, Evolution of dispersal in advective patchy environments, Journal of Nonlinear Science 33 (3) (2023) 40, https://doi.org/10.1007/s00332-023-09899-w .
- [34] R. B. Salako, Y. Wu, On degenerate reaction-diffusion epidemic models with mass action or standard incidence mechanism, European Journal of Applied Mathematics (2024) 128 https://doi.org/10.1017/S0956792523000359 .
- [35] N. L. Haan, Y. Zhang, D. A. Landis, Predicting landscape configuration effects on agricultural pest suppression, Trends in ecology &amp; evolution 35 (2) (2020) 175-186, https://doi.org/10.1016/j.tree.2019.10.003 .
- [36] D. A. Landis, S. D. Wratten, G. M. Gurr, Habitat management to conserve natural enemies of arthropod pests in agriculture, Annual review of entomology 45 (1) (2000) 175-201, https://doi.org/10.1146/annurev.ento.45.1.175 .
- [37] C. Kremen, A. M. Merenlender, Landscapes that work for biodiversity and people, Science 362 (6412) (2018) eaau6020, https://doi.org/10.1126/science.aau6020 .
- [38] A. Klinnert, A. L. Barbosa, R. Catarino, T. Fellmann, E. Baldoni, C. Beber, J. Hristov, M. L. Paracchini, C. Rega, F. Weiss, et al., Landscape features support natural pest control and farm income when pesticide application is reduced, Nature Communications 15 (1) (2024) 5384, https://doi.org/10.1038/s41467-024-48311-3 .
- [39] L. A. Schulte, A. L. MacDonald, J. B. Niemi, M. J. Helmers, Prairie strips as a mechanism to promote land sharing by birds in industrial agricultural landscapes, Agriculture, Ecosystems &amp; Environment 220 (2016) 55-63, https://doi.org/10.1016/j.agee.2016.01.007 .

- [40] L. A. Schulte, J. Niemi, M. J. Helmers, M. Liebman, J. G. Arbuckle, D. E. James, R. K. Kolka, M. E. O'Neal, M. D. Tomer, J. C. Tyndall, et al., Prairie strips improve biodiversity and the delivery of multiple ecosystem services from corn-soybean croplands, Proceedings of the National Academy of Sciences 114 (42) (2017) 11247-11252, https://doi.org/10.1073/pnas.1620229114 .
- [41] M. Carter, A. Dixon, Honeydew: an arrestant stimulus for coccinellids, Ecological Entomology 9 (4) (1984) 383-387, https://doi.org/10.1111/j.1365-2311.1984.tb00834.x .
- [42] C. MONSRUD, S. TOFT, The aggregative numerical response of polyphagous predators to aphids in cereal fields: attraction to what?, Annals of Applied Biology 134 (3) (1999) 265-270, https://doi.org/10.1111/j.1744-7348.1999.tb05263.x .
- [43] C. Borg, S. Toft, Value of the aphid rhopalosiphum padi as food for grey partridge perdix perdix chicks, Wildlife Biology 5 (1) (1999) 55-58, https://doi.org/10.2981/wlb.1999.001 .
- [44] J. D. Murray, Mathematical Biology: II: Spatial Models and Biomedical Applications, Vol. 3, Springer, 2003, https://doi.org/10.1007/b98868 .
- [45] U. Dieckmann, B. O'Hara, W. Weisser, The evolutionary ecology of dispersal, Trends in Ecology &amp; Evolution 14 (3) (1999) 88-90, https://doi.org/10.1016/S0169-5347(98)01571-7 .
- [46] R. D. Parshad, S. Wickramsooriya, S. Bailey, A remark on 'biological control through provision of additional food to predators: A theoretical study'[theor. popul. biol. 72 (2007) 111-120], Theoretical population biology 132 (2020) 60-68, https://doi.org/10.1016/j.tpb.2019.11.010 .
- [47] R. D. Parshad, E. Quansah, K. Black, M. Beauregard, Biological control via 'ecological' damping: an approach that attenuates non-target effects, Mathematical biosciences 273 (2016) 23-44, https://doi.org/10.1016/j.mbs.2015.12.010 .
- [48] H. Klomp, Intraspecific competition and the regulation of insect numbers, Annual review of entomology 9 (1) (1964) 17-40, https://doi.org/10.1146/annurev.en.09.010164.000313 .
- [49] F. Kordbacheh, M. Liebman, M. Harris, Strips of prairie vegetation placed within row crops can sustain native bee communities, PLoS One 15 (10) (2020) e0240354, https://doi.org/10.1371/journal.pone.0240354 .
- [50] L. A. Schulte, J. Niemi, M. J. Helmers, M. Liebman, J. G. Arbuckle, D. E. James, R. K. Kolka, M. E. O'Neal, M. D. Tomer, J. C. Tyndall, et al., Prairie strips improve biodiversity and the delivery of multiple ecosystem services from corn-soybean croplands, Proceedings of the National Academy of Sciences 114 (42) (2017) 11247-11252, https://doi.org/10.1073/pnas.1620229114 .
- [51] W. E. Snyder, Give predators a complement: Conserving natural enemy biodiversity to improve biocontrol, Biological control 135 (2019) 73-82, https://doi.org/10.1016/j.biocontrol.2019.04.017 .
- [52] D. B. Prakash, D. Vamsi, Role of intra-specific competition and additional food on prey-predator systems exhibiting holling type-iv functional response, arXiv preprint arXiv:2504.09078 https://doi.org/10.48550/arXiv.2504.09078 (2025).
- [53] D. B. Prakash, D. Vamsi, Stochastic time-optimal control and sensitivity studies for additional food provided prey-predator systems involving holling type-iv functional response, Frontiers in Applied Mathematics and Statistics 9 (2023) 1122107, https://doi.org/10.3389/fams.2023.1122107 .
- [54] R. D. Parshad, S. Wickramasooriya, K. Antwi-Fordjour, A. Banerjee, Additional food causes predators to explode-unless the predators compete, International Journal of Bifurcation and Chaos 33 (03) (2023) 2350034, https://doi.org/10.1142/S0218127423500347 .
- [55] M. Sen, P. Srinivasu, M. Banerjee, Global dynamics of an additional food provided predator-prey system with constant harvest in predators, Applied Mathematics and Computation 250 (2015) 193211, https://doi.org/10.1016/j.amc.2014.10.085 .
- [56] S. D. Wickramsooriya, A. Banerjee, J. Martin, R. D. Parshad, Novel dynamics in an additional food provided predator-prey system with mutual interference, Under Review https://doi.org/10.48550/arXiv.2312.11726 (2023).

- [57] D. Kumar, S. P. Chakrabarty, A predator-prey model with additional food supply to predators: dynamics and applications, Computational and Applied Mathematics 37 (2018) 763-784, https://doi.org/10.1007/s40314-016-0369-x .
- [58] D. Kumar, S. P. Chakrabarty, A comparative study of bioeconomic ratio-dependent predatorprey model with and without additional food to predators, Nonlinear Dynamics 80 (2015) 23-38, https://doi.org/10.1007/s11071-014-1848-5 .
- [59] D. L. DeAngelis, R. Goldstein, R. V. O'Neill, A model for tropic interaction, Ecology 56 (4) (1975) 881-892, https://doi.org/10.2307/1936298 .
- [60] Y. A. Kuznetsov, Elements of applied bifurcation theory, Springer, 1998, https://doi.org/10.1007/978-1-4757-3978-7 .
- [61] L. Perko, Differential equations and dynamical systems, Vol. 7, Springer Science &amp; Business Media, 2013, https://doi.org/10.1007/978-1-4613-0003-8 .
- [62] J. Guckenheimer, P. Holmes, Nonlinear oscillations, dynamical systems, and bifurcations of vector fields, Vol. 42, Springer Science &amp; Business Media, 2013, https://doi.org/10.1007/978-1-4612-1140-2 .
- [63] H. Zhu, S. A. Campbell, G. S. Wolkowicz, Bifurcation analysis of a predator-prey system with nonmonotonic functional response, SIAM Journal on Applied Mathematics 63 (2) (2003) 636-682, https://doi.org/10.1137/S0036139901397285 .
- [64] D. Xiao, S. Ruan, Global analysis in a predator-prey system with nonmonotonic functional response, SIAM Journal on Applied Mathematics 61 (4) (2001) 1445-1472, https://doi.org/10.1137/S0036139999361896 .
- [65] F. Dumortier, R. Roussarie, J. Sotomayor, H. Zoladek, Bifurcations of planar vector fields: nilpotent singularities and Abelian integrals, Springer, 2006, https://doi.org/10.1007/BFb0098353 .
- [66] M. Lu, J. Huang, Global analysis in bazykin's model with holling ii functional response and predator competition, Journal of Differential Equations 280 (2021) 99-138, https://doi.org/10.1016/j.jde.2021.01.025 .
- [67] J. Huang, S. Ruan, J. Song, Bifurcations in a predator-prey system of leslie type with generalized holling type iii functional response, Journal of Differential Equations 257 (6) (2014) 1721-1752, https://doi.org/10.1016/j.jde.2014.04.024 .
- [68] M. Banerjee, J. Huang, Q. Pan, L. Zou, Bifurcations of higher codimension in a preypredator model with generalist predator, Discrete Contin. Dyn. Syst. B 29 (9) (2024) 3744-3774, https://doi.org/10.3934/dcdsb.2024022 .
- [69] J. Huang, S. Liu, S. Ruan, X. Zhang, Bogdanov-takens bifurcation of codimension 3 in a predatorprey model with constant-yield predator harvesting, Commun. Pure Appl. Anal 15 (3) (2016) 10411055, https://doi.org/10.3934/cpaa.2016.15.1041 .
- [70] H. Zhou, S. Tang, Bogdanov-takens bifurcation of codimension 3 of a predator-prey model with constant-yield predator releasing rate, Discrete and Continuous Dynamical Systems-B 29 (12) (2024) 4671-4697, https://doi.org/10.3934/dcdsb.2024061 .
- [71] A. Arsie, C. Kottegoda, C. Shan, A predator-prey system with generalized holling type iv functional response and allee effects in prey, Journal of Differential Equations 309 (2022) 704-740, https://doi.org/10.1016/j.jde.2021.11.041 .
- [72] A. Arsie, C. Kottegoda, C. Shan, High codimension bifurcations of a predator-prey system with generalized holling type iii functional response and allee effects, Journal of Dynamics and Differential Equations 35 (4) (2023) 3355-3380, https://doi.org/10.1007/s10884-022-10214-6 .
- [73] J. M. Chase, P. A. Abrams, J. P. Grover, S. Diehl, P. Chesson, R. D. Holt, S. A. Richards, R. M. Nisbet, T. J. Case, The interaction between predation and competition: a review and synthesis, Ecology letters 5 (2) (2002) 302-315, https://doi.org/10.1046%2Fj.1461-0248.2002.00315.x .
- [74] A. D. Bazykin, Nonlinear dynamics of interacting populations, World Scientific, 1998, https://doi.org/10.1142/2284 .

- [75] U. Verma, A. Banerjee, R. D. Parshad, T (w) o patch or not t (w) o patch: A novel additional food model, Under Review https://doi.org/10.48550/arXiv.2310.17003 (2023).
- [76] M. Sambath, K. Balachandran, M. Suvinthra, Stability and hopf bifurcation of a diffusive predator-prey model with hyperbolic mortality, Complexity 21 (S1) (2016) 34-43, https://doi.org/10.1002%2Fcplx.21708 .
- [77] P. B. Fenberg, K. Roy, Ecological and evolutionary consequences of size-selective harvesting: how much do we know?, Molecular ecology 17 (1) (2008) 209-220, https://doi.org/10.1111/j.1365-294X.2007.03522.x .
- [78] K. Antwi-Fordjour, R. D. Parshad, M. A. Beauregard, Dynamics of a predator-prey model with generalized holling type functional response and mutual interference, Mathematical biosciences 326 (2020) 108407, https://doi.org/10.1016/j.mbs.2020.108407 .
- [79] D. Barman, S. Roy, P. K. Tiwari, S. Alam, Two-fold impacts of fear in a seasonally forced predatorprey system with cosner functional response, Journal of Biological Systems 31 (02) (2023) 517-555, https://doi.org/10.1142/S0218339023500183 .
- [80] F. Brauer, A. Soudack, Constant-rate stocking of predator-prey systems, Journal of Mathematical Biology 11 (1981) 1-14, https://doi.org/10.1007/BF00275820 .
- [81] R. D. Parshad, K. Antwi-Fordjour, E. M. Takyi, Some novel results in two species competition, SIAM Journal on Applied Mathematics 81 (5) (2021) 1847-1869, https://doi.org/10.1137/20M1387274 .
- [82] A. Banerjee, U. Verma, M. T. Lewis, R. D. Parshad, Two species competition with a" non-smooth" allee mechanism: applications to soybean aphid population dynamics under climate change, Mathematical Biosciences and Engineering 22 (3) (2025) 604-651, https://doi.org/10.3934/mbe.2025023 .
- [83] D. W. Ragsdale, D. J. Voegtlin, R. J. O'neil, Soybean aphid biology in north america, Annals of the Entomological Society of America 97 (2) (2004) 204-208, https://doi.org/10.1603/0013-8746(2004)097[0204:SABINA]2.0.CO;2 .
- [84] N. Osawa, Ecology of harmonia axyridis in natural habitats within its native range, BioControl 56 (4) (2011) 613-621, https://doi.org/10.1007/s10526-011-9382-6 .
- [85] H. Lee, K. Calvin, D. Dasgupta, G. Krinner, A. Mukherji, P. Thorne, C. Trisos, J. Romero, P. Aldunce, K. Barrett, et al., Climate change 2023: synthesis report. Contribution of working groups I, II and III to the sixth assessment report of the intergovernmental panel on climate change, The Australian National University, 2023, http://dx.doi.org/10.59327/IPCC/AR6-9789291691647 .
- [86] U. Verma, M. Lewis, J. Lehman, R. D. Parshad, Towards improved pest management of the soybean aphid, arXiv preprint arXiv:2505.16013 (2025).
- [87] H. R. Thieme, Mathematics in population biology, Princeton University Press, 2003, https://doi.org/10.2307/j.ctv301f9v .