INTRODUCTION
============

En théorie linéaire, les amplitudes des ondes qui se propagent dans un
plasma sont considérées comme très faibles; une analyse perturbative
permet alors de ne retenir que les termes du premier ordre. Mais si les
ondes ont des amplitudes suffisamment élevées, les termes non-linéaires
présents dans les équations qui gouvernent leur propagation ne sont plus
des perturbations négligeables mais leurs contributions doivent être
prises en compte[^1], permettant ainsi la mise en évidence d’effets
physiques nouveaux. C’est ce que nous étudierons dans ce chapitre; en
particulier, nous prendrons comme exemple les ondes électrostatiques
acoustiques ioniques.

La dispersion et la non-linéarité sont deux aspects fondamentaux en
physique des plasmas. Nous verrons comment une balance entre ces deux
effets dans un plasma permet l’apparition d’une structure remarquable :
le soliton, onde non-linéaire solitaire qui se propage dans un plasma
sans se déformer ni sans être affectée par d’éventuelles interactions
avec d’autres solitons. Ainsi, les effets dispersifs peuvent empêcher
l’effondrement d’une onde que provoqueraient les effets non-linéaires
liés au raidissement du front d’onde. Les ondes solitons sont des
solutions stationnaires de l’équation dite de Korteweg-de Vries. Cette
équation, obtenue par Korteweg et de Vries lors de la résolution d’un
problème d’hydrodynamique (ondes à la surface de l’eau), apparaît dans
le traitement de nombreux problèmes physiques concernant des systèmes
dispersifs faiblement non-linéaires.

D’autre part, lorsqu’un processus de dissipation est présent, un autre
type d’onde non-linéaire peut se propager : c’est l’onde de choc non
collisionnelle, qui permet par sa structure de connecter entre elles des
régions de l’espace où le plasma est fortement perturbé et des régions
où il ne l’est pas. Ces ondes peuvent exister dans un plasma même en
l’absence de collisions interparticulaires, ce qui peut paraître de
prime abord surprenant. Elles constituent des solutions stationnaires de
l’équation dite de Burger-Korteweg-de Vries qui inclut à la fois des
termes dispersif, dissipatif et non-linéaire.

EQUATIONS D’ONDES NON-LINEAIRES
===============================

L’onde solitaire en hydrodynamique
----------------------------------

John Scott Russell (1808-1882) est un ingénieur écossais qui décrivit
pour la première fois l’observation qu’il fit d’une onde solitaire se
propageant le long d’un canal. Russell étudiait le mouvement des vagues
à la surface de l’eau et leur rôle dans la résistance au mouvement des
bateaux pour en déduire les formes des coques de navires les plus aptes
à la navigation dans des canaux. Il écrit : ”*J’observais le mouvement
d’un bateau que deux chevaux tiraient rapidement dans un canal étroit,
lorsque ce bateau vint à s’arrêter tout à coup; mais il n’en fut pas de
même de la masse d’eau qu’il avait mise en mouvement; elle s’accumula
autour de la proue dans un état de violente agitation, puis, laissant
tout à coup le bateau en arrière, se mit à cheminer en avant avec une
grande vitesse sous la forme d’une seule grande ondulation, dont la
surface était arrondie, lisse et parfaitement déterminée. Cette onde
continua sa marche dans le canal sans que sa forme et sa vitesse
parussent s’altérer en rien. Je la suivis à cheval et la retrouvai
encore cheminant encore avec une vitesse de 8 à 9 milles[^2] à l’heure
et conservant sa img/figure initiale (environ 30 pieds de longueur sur 1
pied à 1 pied et demi de hauteur[^3]). La hauteur de l’onde diminuait
graduellement, et après l’avoir suivie pendant un mille ou deux, je la
perdis dans les sinuosités du canal. Ainsi au mois d’août 1834 ai-je eu
la chance de ma première rencontre avec ce phénomène étrange et
beau.*”[^4]

Bien que l’étude mathématique de la propagation d’ondes de faible
amplitude à la surface d’un fluide ait débuté dès le 18$^{i\grave{e}me}$
siècle, la description analytique d’ondes de plus grande amplitude et
stables telles que l’onde solitaire décrite par Russell a été réalisée
par Boussinesq (1869) et Saint-Venant (1885), puis la résolution exacte
du problème a été effectuée par Korteweg et de Vries en 1895. Après un
déclin de l’intérêt pour le sujet de près de 60 ans, les deux chercheurs
américains Zabusky et Kruskal[^5] démontrent en 1965 par des simulations
numériques que deux ondes solitaires vérifiant l’équation de Korteweg-de
Vries, dirigées de manière à se heurter, entrant en collision sans se
déformer. Cet effet très surprenant et remarquable donne alors naissance
au terme de ”*soliton*”. Le concept de soliton infiltre ensuite
rapidement dans de nombreux domaines des mathématiques et de la physique
où il a permis de décrire et de comprendre de multiples phénomènes en
hydrodynamique, en optique non-linéaire, en physique des solides, des
gaz, des plasmas, des lasers, ou encore en neurobiologie, par exemple.

Essayons de comprendre à présent quels sont les divers phénomènes
physiques qui interviennent dans la formation et la propagation d’une
onde solitaire dans un plasma.

Non-linéarités dans le mouvement d’un fluide
--------------------------------------------

L’équation hydrodynamique d’un fluide dans un plasma (ions ou électrons)
est donnée par

$$\underline{\overline{mn\frac{d\mathbf{U}}{dt}=mn\left[  \frac{\partial
\mathbf{U}}{\partial t}+(\mathbf{U\cdot\nabla)U}\right]  \mathbf{=F,\qquad
U=U(r},t\mathbf{),}}}\label{A1}$$

où $\mathbf{U}$ est la vitesse du fluide considéré et $mn$ sa densité de
masse; $\mathbf{F}$ est la force totale s’exerçant sur le fluide,
pouvant inclure les effets électromagnétiques, collisionnels et
thermiques. Le terme $(\mathbf{U\cdot\nabla)U}$ est un terme
non-linéaire appelé dérivée convective de la vitesse. Quels effets
physiques induit-il ?

Considérons un cas simple. Dans un modèle à une dimension et en
l’absence de force, ([A1]) s’écrit sous la forme

$$\frac{dU}{d\tau}=\frac{\partial U}{\partial\tau}+\frac{\partial U}{\partial
\xi}\frac{d\xi}{d\tau}=\frac{\partial U}{\partial\tau}+U\frac{\partial
U}{\partial\xi}=0,\qquad U=U(\xi,\tau),\label{A2}$$

où $\xi$ et $\tau$ sont deux variables indépendantes d’espace et de
temps; $U\frac{\partial U}{\partial\xi}$ est la dérivée convective de la
vitesse. La solution générale de ([A2]) est de la forme

$$U(\xi,\tau)\equiv F(s(\xi,\tau))=F(\xi-U(\xi,\tau)\tau),\label{A3}$$

où la fonction différentiable $F(s)$ est une solution implicite de
([A2]). On le vérifie aisément en différentiant ([A3])

$$U(\xi,\tau)=F(s(\xi,\tau))\Rightarrow dF=\frac{dF}{ds}ds=\frac{dF}{ds}(\frac{\partial s}{\partial\xi}d\xi+\frac{\partial s}{\partial\tau}d\tau)=dU=\frac{\partial U}{\partial\xi}d\xi+\frac{\partial U}{\partial\tau
}d\tau,$$

d’où

$$\frac{\partial U}{\partial\xi}=\frac{dF}{ds}\frac{\partial s}{\partial\xi
}=F^{\prime}(s)(1-\frac{\partial U}{\partial\xi}\tau)\text{,\qquad}\frac{\partial U}{\partial\tau}=\frac{dF}{ds}\frac{\partial s}{\partial\tau
}=-F^{\prime}(s)(U+\frac{\partial U}{\partial\tau}\tau),$$

puisque

$$s=\xi-U(\xi,\tau)\tau=s(\xi,\tau)\Rightarrow ds=\frac{\partial s}{\partial\xi
}d\xi+\frac{\partial s}{\partial\tau}d\tau=(1-\frac{\partial U}{\partial\xi
}\tau)d\xi-(U+\frac{\partial U}{\partial\tau}\tau)d\tau.$$

Par conséquent il vient

$$\frac{\partial U}{\partial\tau}=-\frac{UF^{\prime}(s)}{1+\tau F^{\prime}(s)},\qquad\frac{\partial U}{\partial\xi}=\frac{F^{\prime}(s)}{1+\tau
F^{\prime}(s)},\label{A7}$$

qui montre ([A3]). Considérons, à $\tau=0$, une valeur particulière
$U=F(\xi)$ correspondant à une certaine valeur de $\xi.$ A un temps
$\tau>0$ ultérieur, cette même valeur de $U$ correspondra à une valeur
de $\xi$ telle que la valeur de $F(\xi-U(\xi,\tau)\tau) $ est inchangée
(voir ([A3])), c’est-à-dire à un $\xi=\xi^{\prime}$ plus grand que le
précédent d’une quantité $U\tau$

$$\left\{
\begin{array}
[c]{c}\tau=0,\quad U=F(\xi)\\
\tau>0,\quad U=F(\xi^{\prime}-U\tau)
\end{array}
\right\}  \Rightarrow F(\xi)=F(\xi^{\prime}-U\tau),\qquad\xi^{\prime}=\xi+U\tau.\label{A8}$$

Cela signifie que chaque valeur particulière de $U$ se propage vers la
droite (i.e., vers les $\xi$ croissants) avec la vitesse $U$. Par
conséquent, les grandes valeurs de $U$ se propagent plus vite que les
petites, ce qui entraîne une distortion de $U$ en fonction de $\xi$ lors
de son évolution temporelle, comme le montre la img/figure 1. La pente
négative de $U$ devient de plus en plus abrupte à mesure que le temps
s’écoule: c’est le phénomène de* raidissement du front*. Il arrive un
moment où la pente $\frac{\partial U}{\partial\xi}<0$ devient infinie
(voir $U(\xi,\tau=\tau_{2})$, img/figure 1) pour une certaine valeur de
$\xi$; au-delà de cette valeur, la solution de ([A2]) devient
multivaluée, ce qui est impossible physiquement, puisqu’au même point
$\xi$, le fluide ne peut pas se propager avec plusieurs vitesses $U $
différentes (voir $U(\xi,\tau=\tau_{3})$, img/figure 1). La pente
$\frac{\partial U}{\partial\xi}$ devient infinie au temps $\tau_{c}$

$$\frac{\partial U}{\partial\xi}\rightarrow\infty\Rightarrow\tau_{c}=\min
_{s}\left(  -\frac{1}{F^{\prime}(s)}\right)  ,\label{A9}$$

et, finalement, l’onde se brise comme le ferait une vague sur la mer
(phénomène d’*effondrement*).

Le raidissement du front est lié à l’apparition de composantes de
courtes longueurs d’ondes dans la perturbation, qui sont dues à
l’existence d’harmoniques supérieures $(nk,n\omega,n>1)$ de l’onde
$(k,\omega)$ générées par le terme non-linéaire
$(\mathbf{U\cdot\nabla)U}$. L’effondrement de l’onde qui achève sa phase
de distortion résulte du fait que le terme de non-linéarité
$U\frac{\partial U}{\partial\xi}$ n’est pas contrebalancé dans ([A2])
par des termes de dispersion ou de dissipation qui tendent à limiter le
raidissement du front. En effet, celui-ci apparaît quand les harmoniques
supérieures se couplent non-linéairement avec l’onde $(k,\omega),$ ce
couplage étant d’autant plus fort si l’onde et ses harmoniques se
propagent à la même vitesse; si ce n’est pas le cas, l’effet de
raidissement est réduit à cause de la dispersion. Pour les ondes
acoustiques ioniques par exemple, la relation de dispersion (voir plus
loin ([A26])-([AA26])) montre que les composantes de plus petites
longueurs d’onde se propagent moins vite que l’onde principale
$(k,\omega)$ , rendant le couplage non-linéaire inefficace: le
raidissement du front est en partie contrecarré par la dispersion.
Ainsi, nous verrons plus loin comment, grâce à une balance entre
dispersion et non-linéarité dans l’équation ([A2]), la perturbation $U$
peut être une structure propagative stable appelée impulsion solitaire
ou soliton, vérifiant l’équation de Korteweg-de Vries. D’autre part,
l’introduction d’un terme dissipatif dans l’équation hydrodynamique
([A2]) conduit à l’équation de Burger, dont les solutions stationnaires
sont des ondes de chocs non collisionnelles.

.

![image](img/fig1new.tif)\
**Figure 1**<span>. Variation de </span>$U(\xi,\tau)$<span> en fonction
de </span>$\xi$<span> pour différents instants de temps
</span>$\tau$<span>; on observe le raidissement du front pour
</span>$\tau\lesssim\tau_{2}$<span> et l’effondrement pour
</span>$\tau\simeq\tau_{3}.$

Equations non-linéaires dispersives
-----------------------------------

En 1895, les physiciens Korteweg et de Vries présentent une équation
contenant les effets dispersifs et non-linéaires évoqués plus haut pour
laquelle ils obtiennent une famille de solutions exactes stationnaires,
avec, comme solution particulière, l’onde solitaire. Cette équation,
dite de Korteweg-de Vries ou plus simplement KdV, apparaît dans le
traitement de différents problèmes physiques concernant des systèmes
dispersifs faiblement non-linéaires et s’écrit sous la forme

$$\underline{\overline{\frac{\partial U}{\partial\tau}+aU\frac{\partial
U}{\partial\xi}+b\frac{\partial^{3}U}{\partial\xi^{3}}=0,}}\label{A10}$$

où $\tau$ et $\xi$ sont des variables indépendantes et $a$ et $b$ sont
des réels. Alors que les corrections non-linéaires (terme
$U\frac{\partial U}{\partial\xi}$) ont tendance à rendre le profil de
l’onde plus abrupt (effet de raidissement), les corrections dispersives
(terme $\frac{\partial^{3}U}{\partial\xi^{3}}$) ont par contre tendance
à étaler ce profil[^6]. La forme particulière de l’onde solitaire et sa
stabilité résultent de la compétition entre ces deux effets et de leur
compensation en tout point du profil de l’onde. En faisant le changement
de variable $\xi\longrightarrow\xi b^{-1/3}$ et
$U\longrightarrow Uab^{-1/3}$, ([A10]) se met sous une forme simple

$$\underline{\overline{\frac{\partial U}{\partial\tau}+U\frac{\partial
U}{\partial\xi}+\frac{\partial^{3}U}{\partial\xi^{3}}=0.}}\label{A11}$$

L’équation de Burger est une équation non-linéaire comprenant non plus
un terme dispersif mais un terme dissipatif
$\alpha\frac{\partial^{2}U}{\partial\xi^{2}}$ ainsi que le terme
non-linéaire $U\frac{\partial
U}{\partial\xi}$

$$\overline{\underline{\frac{\partial U}{\partial\tau}+U\frac{\partial
U}{\partial\xi}-\alpha\frac{\partial^{2}U}{\partial\xi^{2}}=0,\qquad\alpha
>0.}}\label{A12}$$

Notons que l’équation ([A12]) sans son terme non-linéaire est de type
diffusif puisqu’elle s’écrit
$\frac{\partial U}{\partial\tau}=\alpha_{D}\ \nabla^{2}U$, où
$\alpha_{D}$ est un coefficient de diffusion, montrant bien la présence
d’une dissipation dans ([A12]).

Notons également l’existence d’autres équations non-linéaires admettant
des solutions de type soliton, que nous n’étudierons pas ici, comme
l’équation de Kadomtsev-Petviashvili qui est la généralisation à deux
dimensions ($\xi,\xi^{\prime}$) de l’équation KdV

$$\frac{\partial^{2}\phi}{\partial\xi\partial\tau}+\frac{\partial\phi}{\partial\xi}\frac{\partial^{2}\phi}{\partial\xi^{2}}+\frac{\partial^{4}\phi
}{\partial\xi^{4}}+\frac{1}{2}\frac{\partial^{2}\phi}{\partial\xi^{\prime2}}=0,\qquad\mathbf{U}=\mathbf{\nabla}\phi,\label{AB12}$$

où $\phi$ est le potentiel associé à $\mathbf{U,}$ ou encore l’équation
de Sine-Gordon

$$\frac{\partial^{2}U}{\partial\xi^{2}}-a\frac{\partial^{2}U}{\partial\tau^{2}}=\sin U\label{AA12}$$

qui décrit de nombreux phénomènes physiques, notamment en physique des
solides et des supraconducteurs. Toutefois, nous étudierons dans un
prochain chapitre l’équation de Schrödinger non-linéaire qui admet comme
solution le soliton enveloppe.

L’équation de Korteweg-de Vries
-------------------------------

L’existence de solutions de type ”solitons” dans l’équation de
Korteweg-de Vries est liée à l’existence d’une infinité de lois de
conservation à une dimension du type

$$\frac{\partial T_{n}}{\partial\tau}+\frac{\partial X_{n}}{\partial\xi
}=0,\qquad n\geq1,\label{AC12}$$

où $T_{n}$ et $X_{n}$ sont des fonctions de $\xi,$ $\tau,$ $U$ et des
dérivées de $U$ par rapport à $\xi$; par conséquent, $T_{n}$ est associé
à l’invariant $I_{n}$ de l’équation de Korteweg-de Vries de la façon
suivante

$$(\text{\ref{AC12}})\Rightarrow\underset{-\infty}{\overset{\infty}{\int}}\frac{\partial T_{n}}{\partial\tau}d\xi=\left[  X_{n}\right]  _{-\infty
}^{\infty}=0\Rightarrow I_{n}=\underset{-\infty}{\overset{\infty}{\int}}T_{n}(\xi,\tau)d\xi,\qquad\frac{\partial I_{n}}{\partial\tau}=0,\qquad
n\geq1.\label{ACC12}$$

Cette remarquable propriété montre l’intérêt fondamental de l’équation
KdV pour la physique. Celle-ci peut s’écrire sous la forme d’une
équation de conservation pour $n=1$ (pour simplifier les expressions
ci-dessous, on a fait le changement de variable $U\rightarrow-6U $ dans
([A11]))

$$\text{(\ref{A10})}\Rightarrow\frac{\partial U}{\partial\tau}+\frac{\partial
}{\partial\xi}\left(  -3U^{2}+\frac{\partial^{2}U}{\partial\xi^{2}}\right)
=0,\qquad X_{1}=-3U^{2}+\frac{\partial^{2}U}{\partial\xi^{2}},\qquad
T_{1}=U,\label{AD12}$$

qui est une équation de conservation de la quantité de mouvement;
l’invariant correspondant est

$$I_{1}=\underset{-\infty}{\overset{\infty}{\int}}U(\xi,\tau)d\xi,\label{ADD12}$$

comme nous le verrons également plus loin.

En multipliant ([AD12]) par $2U$, puis en réarrangeant l’expression
correspondante, une autre loi de conservation s’obtient sous la forme
(le changement de variables ci-dessus est maintenu)

$$\frac{\partial}{\partial\tau}U^{2}+\frac{\partial}{\partial\xi}\left[
-4U^{3}+2U\frac{\partial^{2}U}{\partial\xi^{2}}-\left(  \frac{\partial
U}{\partial\xi}\right)  ^{2}\right]  =0,\qquad T_{2}=U^{2},\label{AE12}$$

représentant la conservation de l’énergie. Les lois de conservation
d’ordres supérieurs n’ont par contre pas de signification physique.

L’équation KdV peut être résolue de façon exacte comme un problème aux
conditions initiales par la méthode dite ”*Inverse Scattering Method*”,
ce qui peut être traduit par ”*Méthode de Diffusion *ou de* Dispersion
Inverse”*. Celle-ci permet de réduire le problème consistant à résoudre
une équation non-linéaire aux dérivées partielles en $\xi$ et $\tau$ à
un problème comprenant deux équations linéaires, c’est-à-dire, d’une
part, à une équation de type Schrödinger indépendante du temps
($\tau=0$) et  d’autre part, à une équation intégrale dite de
Gelfand-Levitan où $\tau$ apparaît comme un paramètre. Toutefois, le but
de ce chapitre n’est pas d’exposer cette méthode mais, comme nous le
verrons dans le paragraphe suivant, d’obtenir l’équation de type KdV
correspondante pour les ondes acoustiques ioniques, puis de la résoudre
pour des solutions stationnaires du type ”soliton” ou ”train de
solitons”.

Illustrons la résolution numérique de l’équation KdV par un exemple en
prenant

$$\frac{\partial U}{\partial\tau}+\frac{a}{2}U\frac{\partial U}{\partial\xi
}+b\frac{\partial^{3}U}{\partial\xi^{3}}=0,\qquad b=0.022,\qquad
a=2,\label{AG12}$$

avec la condition initiale suivante

$$U(\xi,\tau=0)=\cos\pi\xi,\label{AH12}$$

comme le montre la courbe en pointillés sur la img/figure 2a.

![image](img/fig2new.tif)\
**Figure 2a.** <span>Variation de </span>$U(\xi,\tau)$<span> en fonction
de </span>$\xi$<span> (en unités arbitraires) pour trois instants de
temps </span>$\tau=t$<span> : </span>$\tau=0$<span> (impulsion
excitatrice), </span>$\tau=t_{B}$<span> et
</span>$\tau=3.6t_{B}$<span> (N.J. Zabusky and M.D. Kruskal, Interaction
of solitons in a collisionless plasma and the recurrence of initial
states, Phys. Rev. Lett., 15(6), 240, 1965).</span>

Les simulations numériques effectuées montrent qu’au temps $t=t_{B}$
(img/figure 2a), le front de l’onde devient abrupt dans la région où la
pente était initialement négative. La structure oscillante visible pour
$\xi<1/2$ est due au terme dispersif $\frac{\partial^{3}U}{\partial
\xi^{3}}$ qui prévient la formation d’une discontinuité. Pour $t>t_{B}$,
l’amplitude des oscillations croît et finalement en $t=3.6t_{B} $ le
train de solitons est formé (les solitons sont numérotés de 1 à 8 sur la
img/figure 2a); chaque soliton se déplace avec une vitesse uniforme
proportionnelle à son amplitude. La img/figure 2b montre un autre
exemple d’évolution temporelle d’une impulsion initiale en train de
solitons.

![image](img/fig2newbis.tif)\
**Figure 2b.** <span>Variation de </span>$U(\xi,\tau)$<span> en fonction
de </span>$\xi$<span> (en unités arbitraires) pour différents instants
de temps </span>$\tau$<span> =7.5, 10, 15, 20, 30, 40, 50,
60</span>$\mu s,$<span> l’impulsion initiale
(</span>$\tau=0)$<span> étant représentée par la courbe supérieure
(E. Okutsu and Y. Nakamura, Experiment on ion-acoustic solitons as an
initial value problem, *Plasma Physics*, 21, 1053, 1979).</span>

LE SOLITON ACOUSTIQUE IONIQUE
=============================

Dans ce paragraphe nous allons obtenir, à partir des équations
hydrodynamiques et de Maxwell, l’équation d’évolution non-linéaire d’une
onde acoustique ionique. Nous montrerons que cette équation est du type
KdV et, en la résolvant, nous obtiendrons des solutions stationnaires,
les solitons acoustiques ioniques, et nous les caractériserons. Pour
simplifier notre étude, nous la limiterons au cas des ondes acoustiques
ioniques. Bien que nous nous soyons limités ici à l’étude de ce type de
solitons, il en existe évidemment d’autres, comme par exemple les
solitons de Langmuir, associés aux ondes de plasma électroniques. Notons
que bien que le plasma se comporte comme un milieu non-linéaire et que
presque tous les types d’ondes dans un plasma présentent de la
dispersion, les solitons n’existent que pour un nombre limité d’ondes,
dont font partie les ondes acoustiques ioniques.

Dispersion linéaire des ondes acoustiques ioniques
--------------------------------------------------

Etudions tout d’abord les propriétés dispersives des ondes acoustiques
ioniques en théorie linéaire. Dans le cadre d’un modèle à une dimension,
on considère un plasma uniforme, non collisionnel et non magnétisé,
neutre à l’équilibre, $n_{e0}=n_{i0}\equiv n_{0}$. Les ions sont
supposés froids et immobiles à l’équilibre, $v_{i0}=0.$ Les électrons
sont chauds, $T_{i}\ll T_{e},$ et l’on néglige leur inertie, i.e.,
$m_{e}\longrightarrow0.$ On suppose que la température des électrons est
constante et que l’équation d’état isotherme est vérifiée

$$p_{e}=n_{e}k_{B}T_{e},\qquad\gamma_{e}=1.\label{A13}$$

Etudions la propagation d’ondes planes électrostatiques dans ce système
bi–fluide (on utilisera les correspondances $\frac{\partial
}{\partial x^{\prime}}\leftrightarrow ik$ et $\frac{\partial}{\partial
t^{\prime}}\leftrightarrow-i\omega$). On désigne par $x^{\prime}$ et
$t^{\prime} $ les coordonnées d’espace et de temps dans le référentiel
du laboratoire ($\mathcal{R}_{L}$). On suppose que le potentiel est nul
à l’équilibre, $\varphi_{0}=0$. En utilisant les développements
perturbatifs

$$\varphi=\varphi_{0}+\delta\varphi=\delta\varphi,\qquad v_{i}=v_{i0}+\delta
v_{i}=\delta v_{i},\label{A15}$$

$$n_{e}=n_{0}+\delta n_{e},\qquad n_{i}=n_{0}+\delta n_{i},\qquad\delta
n_{e},\delta n_{i}\ll n_{0},\label{A14}$$

où toutes les perturbations par rapport à l’état d’équilibre sont
supposées très faibles, on peut linéariser l’équation de Poisson

$$\frac{\partial^{2}\varphi}{\partial x^{\prime2}}=\frac{e}{\varepsilon_{0}}(n_{e}-n_{i})\Rightarrow\frac{\partial^{2}}{\partial x^{\prime2}}\delta\varphi=-k^{2}\delta\varphi=\frac{e}{\varepsilon_{0}}(\delta
n_{e}-\delta n_{i}).\label{A16}$$

D’autre part, les ions vérifient l’équation de conservation

$$\frac{\partial n_{i}}{\partial t^{\prime}}+\frac{\partial(n_{i}v_{i})}{\partial x^{\prime}}=0\label{A17}$$

$$\Rightarrow-i\omega\delta n_{i}+\frac{\partial}{\partial x^{\prime}}(n_{0}\delta v_{i}+\delta n_{i}\delta v_{i})=0\Rightarrow-i\omega\delta
n_{i}+ikn_{0}\delta v_{i}\simeq0\Rightarrow\delta n_{i}\simeq\frac
{kn_{0}\delta v_{i}}{\omega},\label{A18}$$

et l’équation hydrodynamique

$$\frac{\partial v_{i}}{\partial t^{\prime}}+v_{i}\frac{\partial v_{i}}{\partial
x^{\prime}}=\frac{e}{m_{i}}E=-\frac{e}{m_{i}}\frac{\partial\varphi}{\partial
x^{\prime}}\label{A19}$$

$$\Rightarrow-i\omega\delta v_{i}+\delta v_{i}ik\delta v_{i}=-\frac{e}{m_{i}}ik\delta\varphi\Rightarrow\delta v_{i}\simeq\frac{ek}{m_{i}\omega}\delta\varphi,\label{A20}$$

où $\mathbf{E}=-\mathbf{\nabla}\varphi$ est le champ électrique. La
linéarisation au premier ordre de l’équation du mouvement des électrons
donne à son tour ($m_{e}\simeq0)$

$$m_{e}\frac{dv_{e}}{dt}=-eE-\frac{1}{n_{e}}\frac{\partial p_{e}}{\partial
x^{\prime}}\Rightarrow eE\simeq-\frac{1}{n_{e}}\frac{\partial p_{e}}{\partial
x^{\prime}}\Rightarrow\frac{\partial n_{e}}{\partial x^{\prime}}\simeq
\frac{en_{e}}{k_{B}T_{e}}\frac{\partial\varphi}{\partial x^{\prime}}\Rightarrow n_{e}\simeq n_{0}\exp(\frac{e\varphi}{k_{B}T_{e}})\label{A21}$$

$$\Rightarrow n_{0}+\delta n_{e}\simeq n_{0}(1+\frac{e\delta\varphi}{k_{B}T_{e}})\Rightarrow\delta n_{e}\simeq\frac{en_{0}}{k_{B}T_{e}}\delta\varphi
.\label{A22}$$

En combinant ([A16])-([A22]), il vient

$$-k^{2}\delta\varphi=\frac{e}{\varepsilon_{0}}(\delta n_{e}-\delta n_{i})\simeq\frac{e}{\varepsilon_{0}}(\frac{en_{0}}{k_{B}T_{e}}\delta\varphi
-\frac{kn_{0}\delta v_{i}}{\omega})\simeq\frac{e}{\varepsilon_{0}}\delta\varphi(\frac{en_{0}}{k_{B}T_{e}}-\frac{ek^{2}n_{0}}{m_{i}\omega^{2}}).\label{A23}$$

Cette relation fournit l’équation de dispersion des ondes acoustiques
ioniques

$$k^{2}=\frac{n_{0}e^{2}}{\varepsilon_{0}k_{B}T_{e}}(\frac{k^{2}k_{B}T_{e}}{m_{i}\omega^{2}}-1)\Rightarrow\omega^{2}=c_{s}^{2}k^{2}(1+k^{2}\lambda
_{D}^{2})^{-1},\label{A24}$$

$$\Rightarrow\overline{\underline{\omega=\pm c_{s}\left\vert k\right\vert
(1+k^{2}\lambda_{D}^{2})^{-1/2},\qquad c_{s}=\left(  \frac{k_{B}T_{e}}{m_{i}}\right)  ^{1/2}}},\label{A25}$$

où $c_{s}$ est la vitesse acoustique ionique ($T_{i}\simeq0$). Dans
l’approximation des grandes longueurs d’ondes ($k\lambda_{D}\ll1$), un
développement limité de ([A25]) donne

$$\omega\simeq c_{s}\left\vert k\right\vert (1-\frac{1}{2}k^{2}\lambda_{D}^{2})+...\simeq c_{s}\left\vert k\right\vert ,\label{A26}$$

où seul le signe $+$ dans ([A24]) a été conservé car $\omega>0$. Si
$k\lambda_{D}$ est grand, un tel développement limité n’est pas possible
et, dans ce cas, le terme proportionnel à $k^{3},$ dû aux effets
thermiques électroniques, n’est plus un terme correctif dans l’équation
de dispersion linéaire ([A26]). Ce terme est dispersif puisque les
vitesses de phase et de groupe des ondes acoustiques ioniques

$$v_{\varphi}=\frac{\omega}{k}\simeq c_{s}(1-\frac{1}{2}k^{2}\lambda_{D}^{2}),\qquad v_{g}=\frac{d\omega}{dk}\simeq c_{s}(1-\frac{3}{2}k^{2}\lambda_{D}^{2}),\qquad k>0,\label{AA26}$$

dépendent de $k$ par son intermédiaire. De même, vu la correspondance
$ik\leftrightarrow\frac{\partial}{\partial\xi},$ le terme
$\frac{\partial^{3}U}{\partial\xi^{3}}$ dans l’équation KdV obtenue plus
loin et qui décrit l’évolution non-linéaire des ondes acoustiques
ioniques est un terme dispersif.

L’équation d’évolution non-linéaire
-----------------------------------

Lors de la linéarisation effectuée au paragraphe précédent, le terme
convectif dans l’équation hydrodynamique des ions ([A19])-([A20]), du
deuxième ordre, a été négligé. Il s’agit maintenant de le prendre en
compte (on considère que les perturbations ne sont plus négligeables,
bien qu’étant toutefois faibles) et d’étudier les phénomènes physiques
induits par la non-linéarité qu’il introduit dans l’équation d’évolution
des ondes acoustiques ioniques.

Pour simplifier l’écriture des équations, on utilise la normalisation
suivante

$$v=\frac{v_{i}}{c_{s}},\qquad x=\frac{x^{\prime}}{\lambda_{D}},\qquad
t=\omega_{pi}t^{\prime},\qquad n=\frac{n_{i}}{n_{0}},\qquad\Phi=\frac
{e\varphi}{k_{B}T_{e}}.\label{A27}$$

Les équations de Poisson ([A16]), de conservation des ions ([A17]), du
mouvement des ions ([A19]) et des électrons ([A21]) s’écrivent alors
sous la forme

$$\frac{k_{B}T_{e}}{e}\frac{1}{\lambda_{D}^{2}}\frac{\partial^{2}\Phi}{\partial
x^{2}}=\frac{n_{0}e}{\varepsilon_{0}}(e^{\Phi}-n)\Rightarrow
\underline{\overline{\frac{\partial^{2}\Phi}{\partial x^{2}}=e^{\Phi}-n,}}\label{A28}$$

$$\omega_{pi}\frac{\partial n}{\partial t}+\frac{c_{s}}{\lambda_{D}}\frac{\partial(nv)}{\partial x}=0\Rightarrow\overline{\underline{\frac
{\partial n}{\partial t}+\frac{\partial(nv)}{\partial x}=0,}}\label{A29}$$

$$c_{s}\omega_{pi}\left(  \frac{\partial v}{\partial t}+\frac{c_{s}}{\omega
_{pi}\lambda_{D}}v\frac{\partial v}{\partial x}\right)  =-\frac{e}{m_{i}}\frac{\partial\Phi}{\partial x}\frac{k_{B}T_{e}}{e\lambda_{D}}\Rightarrow
\underline{\overline{\left(  \frac{\partial v}{\partial t}+v\frac{\partial
v}{\partial x}\right)  =-\frac{\partial\Phi}{\partial x},}}\label{A30}$$

$$\frac{\partial n_{e}}{\partial x}=n_{e}\frac{\partial\Phi}{\partial
x}\Rightarrow\overline{\underline{\frac{{}}{{}}n_{e}=n_{0}e^{\Phi}\frac{{}}{{}},}}\label{A31}$$

où nous avons introduit l’équation de Boltzmann ([A31]) dans ([A28]).
Remarquons que ([A31]) est identique à ([A21]), car l’hypothèse
$m_{e}\simeq0$ ne permet pas d’introduire le terme non-linéaire
convectif.

Effectuons le changement de variables suivant (notons que cela revient à
changer de référentiel)

$$\xi=\varepsilon^{1/2}(x-t),\qquad\tau=\varepsilon^{3/2}t,\qquad0<\varepsilon
\ll1,\label{A32}$$

où $\varepsilon$ est un réel, et calculons les opérateurs différentiels

$$x=x(\xi,\tau)\Rightarrow\frac{\partial}{\partial x}=\frac{\partial\xi
}{\partial x}\frac{\partial}{\partial\xi}+\frac{\partial\tau}{\partial x}\frac{\partial}{\partial\tau}=\varepsilon^{1/2}\frac{\partial}{\partial\xi
},\label{A33}$$

$$t=t(\xi,\tau)\Rightarrow\frac{\partial}{\partial t}=\frac{\partial\xi
}{\partial t}\frac{\partial}{\partial\xi}+\frac{\partial\tau}{\partial t}\frac{\partial}{\partial\tau}=-\varepsilon^{1/2}\frac{\partial}{\partial\xi
}+\varepsilon^{3/2}\frac{\partial}{\partial\tau}.\label{A34}$$

Les équations ([A28])-([A30]) deviennent alors

$$\varepsilon\frac{\partial^{2}\Phi}{\partial\xi^{2}}=e^{\Phi}-n,\label{A35}$$

$$\varepsilon\frac{\partial n}{\partial\tau}-\frac{\partial n}{\partial\xi
}+\frac{\partial(nv)}{\partial\xi}=0,\label{A36}$$

$$(v-1)\frac{\partial v}{\partial\xi}+\varepsilon\frac{\partial v}{\partial\tau
}=-\frac{\partial\Phi}{\partial\xi}.\label{A37}$$

Soit le développement en série d’une fonction $f(x)$ autour de l’état
d’équilibre non perturbé $f^{(0)}$

$$f(x)=\underset{n}{\sum}\varepsilon^{n}f^{(n)}=f^{(0)}+\varepsilon
f^{(1)}+\varepsilon^{2}f^{(2)}+...,\label{A38}$$

où $\varepsilon^{n}f^{(n)}$ est la perturbation d’ordre $n$ et où le
réel $\varepsilon\ll1$ est une mesure de l’amplitude de la perturbation
(voir aussi ([A32])). Puisqu’à l’équilibre $n_{i}=n_{0}$ $(n^{(0)}=1)$,
$v_{i}=0$ $(v^{(0)}=0)$ et $\varphi=0$ $(\Phi^{(0)}=0)$, on obtient

$$\begin{aligned}
n  & =n^{(0)}+\varepsilon n^{(1)}+\varepsilon^{2}n^{(2)}+...=1+\varepsilon
n^{(1)}+\varepsilon^{2}n^{(2)}+...,\label{A39}\\
v  & =v^{(0)}+\varepsilon v^{(1)}+\varepsilon^{2}v^{(2)}+...=\varepsilon
v^{(1)}+\varepsilon^{2}v^{(2)}+...,\label{A40}\\
\Phi & =\Phi^{(0)}+\varepsilon\Phi^{(1)}+\varepsilon^{2}\Phi^{(2)}+...=\varepsilon\Phi^{(1)}+\varepsilon^{2}\Phi^{(2)}+...\label{A41}\end{aligned}$$

En introduisant ([A39])-([A41]) dans ([A35])-([A37]) et en ne gardant
que les termes d’ordres inférieurs ou égaux à 2, il vient
$$\varepsilon\left(  \varepsilon\frac{\partial^{2}\Phi^{(1)}}{\partial\xi^{2}}+\varepsilon^{2}\frac{\partial^{2}\Phi^{(2)}}{\partial\xi^{2}}+...\right)
=\exp(\varepsilon\Phi^{(1)}+\varepsilon^{2}\Phi^{(2)}+...)-1-\varepsilon
n^{(1)}-\varepsilon^{2}n^{(2)}+...$$

$$\Rightarrow\varepsilon\left(  \Phi^{(1)}-n^{(1)}\right)  +\varepsilon
^{2}\left(  -\frac{\partial^{2}\Phi^{(1)}}{\partial\xi^{2}}-n^{(2)}+\Phi
^{(2)}+\frac{1}{2}[\Phi^{(1)}]^{2}\right)  \simeq0,\label{A42}$$

$$\varepsilon\left(  \varepsilon\frac{\partial n^{(1)}}{\partial\tau
}+\varepsilon^{2}\frac{\partial n^{(2)}}{\partial\tau}+...\right)  -\left(
\varepsilon\frac{\partial n^{(1)}}{\partial\xi}+\varepsilon^{2}\frac{\partial
n^{(2)}}{\partial\xi}+...\right)  +\frac{\partial}{\partial\xi}\left(
1+\varepsilon n^{(1)}+\varepsilon^{2}n^{(2)}+...)(\varepsilon v^{(1)}+\varepsilon^{2}v^{(2)}+...\right)  =0$$

$$\Rightarrow\varepsilon\left(  -\frac{\partial n^{(1)}}{\partial\xi}+\frac{\partial v^{(1)}}{\partial\xi}\right)  +\varepsilon^{2}\left(
\frac{\partial n^{(1)}}{\partial\tau}-\frac{\partial n^{(2)}}{\partial\xi
}+\frac{\partial}{\partial\xi}\left(  n^{(1)}v^{(1)}\right)  +\frac{\partial
v^{(2)}}{\partial\xi}\right)  \simeq0,\label{A43}$$

$$(-1+\varepsilon v^{(1)}+\varepsilon^{2}v^{(2)}+...)\left(  \varepsilon
\frac{\partial v^{(1)}}{\partial\xi}+\varepsilon^{2}\frac{\partial v^{(2)}}{\partial\xi}+...\right)  +\varepsilon\left(  \varepsilon\frac{\partial
v^{(1)}}{\partial\tau}+\varepsilon^{2}\frac{\partial v^{(2)}}{\partial\tau
}+...\right)  =-\varepsilon\frac{\partial\Phi^{(1)}}{\partial\xi}-\varepsilon^{2}\frac{\partial\Phi^{(2)}}{\partial\xi}$$

$$\Rightarrow\varepsilon\left(  -\frac{\partial v^{(1)}}{\partial\xi}+\frac{\partial\Phi^{(1)}}{\partial\xi}\right)  +\varepsilon^{2}\left(
v^{(1)}\frac{\partial v^{(1)}}{\partial\xi}-\frac{\partial v^{(2)}}{\partial\xi}+\frac{\partial v^{(1)}}{\partial\tau}+\frac{\partial\Phi^{(2)}}{\partial\xi}\right)  \simeq0.\label{A44}$$

En identifiant de part et d’autre dans ([A42])-([A44]) les termes en
$\varepsilon$, on obtient

$$\Phi^{(1)}=n^{(1)},\qquad\frac{\partial n^{(1)}}{\partial\xi}=\frac{\partial
v^{(1)}}{\partial\xi}=\frac{\partial\Phi^{(1)}}{\partial\xi}.\label{A45}$$

L’intégration de ([A45]) entraîne que $\Phi^{(1)}=v^{(1)}+f_{1}(\tau),$
$\Phi^{(1)}=n^{(1)}+f_{2}(\tau)$ et $v^{(1)}=n^{(1)}+f_{3}(\tau),$
$\forall\xi,$ où $f_{1},f_{2}$ et $f_{3} $ sont des fonctions
quelconques de $\tau$. Puisque l’on s’intéresse à des perturbations
localisées (voir le paragraphe suivant), la condition suivante doit être
vérifiée

$$\Phi^{(1)},v^{(1)},n^{(1)}\rightarrow0\qquad\text{quand}\qquad\xi
\rightarrow\infty.\label{A46}$$

Par conséquent $f_{1}(\tau)=f_{2}(\tau)=f_{3}(\tau)=0$ et

$$\underline{\overline{\frac{^{{}}}{{}}\Phi^{(1)}=n^{(1)}=v^{(1)}\frac{^{{}}}{{}}.}}\label{A47}$$

D’autre part, en injectant l’expression de $n^{(2)}$ issue de
l’annulation du terme proportionnel à $\varepsilon^{2}$ dans ([A42]),
c’est-à-dire

$$n^{(2)}=-\frac{\partial^{2}\Phi^{(1)}}{\partial\xi^{2}}+\Phi^{(2)}+\frac{1}{2}[\Phi^{(1)}]^{2},\label{A48}$$

dans l’équation fournie par l’annulation du terme proportionnel à
$\varepsilon^{2}$ dans ([A43])

$$-\frac{\partial v^{(2)}}{\partial\xi}=\frac{\partial n^{(1)}}{\partial\tau
}-\frac{\partial n^{(2)}}{\partial\xi}+\frac{\partial}{\partial\xi}\left(
n^{(1)}v^{(1)}\right)  ,\label{A49}$$

on obtient

$$-\frac{\partial v^{(2)}}{\partial\xi}=\frac{\partial^{3}\Phi^{(1)}}{\partial\xi^{3}}-\frac{\partial\Phi^{(2)}}{\partial\xi}-\frac{1}{2}\frac{\partial}{\partial\xi}[\Phi^{(1)}]^{2}+\frac{\partial n^{(1)}}{\partial\tau}+\frac{\partial}{\partial\xi}\left(  n^{(1)}v^{(1)}\right)
.\label{A50}$$

En injectant ([A50]) dans ([A44]) et en utilisant ([A47]), l’annulation
du terme proportionnel à $\varepsilon^{2}$ dans ([A44]) aboutit à
$$\frac{\partial^{3}n^{(1)}}{\partial\xi^{3}}-\frac{\partial\Phi^{(2)}}{\partial\xi}-\frac{1}{2}\frac{\partial}{\partial\xi}[\Phi^{(1)}]^{2}+\frac{\partial n^{(1)}}{\partial\tau}+\frac{\partial\lbrack n^{(1)}]^{2}}{\partial\xi}+\frac{\partial n^{(1)}}{\partial\tau}+n^{(1)}\frac{\partial
n^{(1)}}{\partial\xi}=-\frac{\partial\Phi^{(2)}}{\partial\xi},$$ ce qui
donne finalement

$$\overline{\underline{\frac{\partial n^{(1)}}{\partial\tau}+n^{(1)}\frac{\partial n^{(1)}}{\partial\xi}+\frac{1}{2}\frac{\partial^{3}n^{(1)}}{\partial\xi^{3}}=0,}}\label{A52}$$

qui est l’équation de Korteweg-de Vries ([A10]) pour $a=1$ et $b=1/2$;
([A52]) est également vérifié par les perturbations de potentiel et de
vitesse, $\Phi^{(1)}$ et $v^{(1)}$ (voir ([A47])). Cette équation décrit
l’évolution non-linéaire des perturbations $n^{(1)}$, $\Phi^{(1)}$ et
$v^{(1)}$ se propageant au voisinage de la vitesse acoustique ionique,
comme nous le verrons au paragraphe suivant. Le terme non-linéaire
$n^{(1)}\frac{\partial n^{(1)}}{\partial\xi}$ provient de la convection
et le terme dispersif $\frac{\partial^{3}n^{(1)}}{\partial\xi^{3}}$ de
l’écart $\delta n_{e}-\delta n_{i}$ à la neutralité dans l’équation de
Poisson (voir ([A16]), ([A28]) et ([A35])).

SOLUTIONS DE L’EQUATION DE KORTEWEG-DE VRIES
============================================

Recherche de solutions stationnaires
------------------------------------

Cherchons des solutions stationnaires de l’équation KdV ([A52]). Faisons
le changement de référentiel suivant

$$s(\xi,\tau)=\xi-c_{M}\tau\Rightarrow ds=d\xi-c_{M}d\tau,\qquad c_{M}>0.\label{A53}$$

Puisque $\xi=\varepsilon^{1/2}(x-t)\ $et $\tau=\varepsilon^{3/2}t$
([A32]), on a

$$s=\varepsilon^{1/2}(x-t)-c_{M}\varepsilon^{3/2}t=\varepsilon^{1/2}(x-t(c_{M}\varepsilon+1))\Rightarrow s=\varepsilon^{1/2}(x-Mt),\label{A70}$$

où le facteur $\varepsilon c_{M}$ définit le nombre de Mach $M$ par

$$\underline{\overline{\frac{^{{}}}{{}}\varepsilon c_{M}\equiv\delta M\equiv
M-1>0,\frac{^{{}}}{{}}}}\label{A71}$$

$$\overline{\underline{\frac{^{{}}}{{}}\varepsilon\ll1,\quad0<\varepsilon
c_{M}\ll1\Rightarrow0<\delta M\ll1\Rightarrow M\gtrsim1\frac{^{{}}}{{}}.}}\label{AA71}$$

On se place par conséquent dans le référentiel en mouvement avec une
vitesse normalisée $M$ par rapport à ($\mathcal{R}_{L});$
$\varepsilon c_{M}=\delta M$ représente l’écart du nombre de Mach $M$ au
nombre de Mach $M=1;$ $\delta M$ est choisi suffisamment petit pour que
l’amplitude de la perturbation $U$ soit suffisamment faible.

Dans ce paragraphe, on notera les perturbations $n^{(1)}$, $\Phi^{(1)}$
et $v^{(1)}$ indifféremment par la variable $U^{(1)}$ ou plus simplement
$U;$ on utilisera les formes différentielles suivantes

$$U(s)=U(s(\xi,\tau))\Rightarrow dU=\frac{dU}{ds}ds=\frac{dU}{ds}(\frac{\partial
s}{\partial\xi}d\xi+\frac{\partial s}{\partial\tau}d\tau)\label{A56}$$

$$\Rightarrow\frac{\partial U}{\partial\xi}=\frac{dU}{ds}\frac{\partial
s}{\partial\xi}=\frac{dU}{ds},\qquad\frac{\partial U}{\partial\tau}=\frac
{dU}{ds}\frac{\partial s}{\partial\tau}=-c_{M}\frac{dU}{ds}.\label{A57}$$

L’équation KdV ([A10]) ou ([A52]) devient alors

$$\frac{\partial U}{\partial\tau}+U\frac{\partial U}{\partial\xi}+b\frac
{\partial^{3}U}{\partial\xi^{3}}=0\Rightarrow-c_{M}\frac{dU}{ds}+U\frac
{dU}{ds}+b\frac{d^{3}U}{ds^{3}}=0,\label{A59}$$

$$\Rightarrow-c_{M}\int\frac{dU}{ds}ds+\frac{1}{2}\int\frac{d(U^{2})}{ds}ds+b\int\frac{d}{ds}\left(  \frac{d^{2}U}{ds^{2}}\right)
ds=\mathrm{const}\label{A60}$$

$$\Rightarrow-c_{M}U+\frac{U^{2}}{2}+b\frac{d^{2}U}{ds^{2}}=\mathrm{const}=K=0.\label{A61}$$

La constante $K$ est nulle car $U\rightarrow0$ et
$\frac{d^{n}U}{ds^{n}}\equiv
U^{(n)}\rightarrow0$ quand $\left|  s\right|  \rightarrow\infty$ (on
cherche des perturbations localisées). Poursuivant l’intégration de
([A61]), on obtient

$$-c_{M}\int U\frac{dU}{ds}ds+\frac{1}{2}\int U^{2}\frac{dU}{ds}ds+b\int\frac{dU}{ds}\frac{d^{2}U}{ds^{2}}ds=K^{\prime}\label{A62}$$

$$\Rightarrow-c_{M}\frac{U^{2}}{2}+\frac{U^{3}}{6}+\frac{b}{2}\left(  \frac
{dU}{ds}\right)  ^{2}=K^{\prime}=0\label{A63}$$

$$\Rightarrow\left(  \frac{dU}{ds}\right)  ^{2}=\frac{1}{b}U^{2}(c_{M}-U/3)\Rightarrow\int\frac{dU}{U\sqrt{c_{M}-U/3}}=\pm\sqrt{\frac{1}{b}}s+K^{\prime\prime}.\label{A64}$$

Pour intégrer ([A64]), faisons le changement de variable

$$c_{M}-U/3=y^{2}\Rightarrow-dU/3=2ydy,\qquad\epsilon_{y}=sign(y),\label{A65}$$

permettant d’écrire

$$\int\frac{dU}{U\sqrt{c_{M}-U/3}}=2\epsilon_{y}\int\frac{dy}{y^{2}-c_{M}}=\frac{\epsilon_{y}}{\sqrt{c_{M}}}\mathrm{Ln}\left[  \frac{y-\sqrt{c_{M}}}{y+\sqrt{c_{M}}}\right]  =-\frac{2\epsilon_{y}}{\sqrt{c_{M}}}\tanh^{-1}(\frac{y}{\sqrt{c_{M}}})\label{A66}$$

$$\Rightarrow\tanh^{-1}(\frac{y}{\sqrt{c_{M}}})=\pm\sqrt{\frac{c_{M}}{4b}}s+K^{\prime\prime}\Rightarrow y^{2}=c_{M}\tanh^{2}\left(  \pm\sqrt
{\frac{c_{M}}{4b}}s+K^{\prime\prime}\right)  =c_{M}-U/3,\label{A67}$$

où $\tanh^{-1}(x)\equiv$Arg$\tanh(x)$ représente la fonction inverse de
$\tanh(x)$. Finalement, on obtient une solution de l’équation KdV (pour
$K^{\prime\prime}=0$) sous la forme[^7]

$$U(s)\equiv U^{(1)}(s)=3c_{M}\sec^{2}\left(  \sqrt{\frac{c_{M}}{4b}}s\right)
.\label{A68}$$

Finalement, la solution stationnaire de KdV obtenue en ([A68]), qui est
la perturbation $U^{(1)}\equiv n^{(1)}$, $\Phi^{(1)}$ ou $v^{(1)},$
s’écrit dans le référentiel du laboratoire ($\mathcal{R}_{L})$ de la
façon suivante

$$U^{(1)}(x,t)=3c_{M}\sec^{2}\left(  (c_{M}/4b)^{1/2}\varepsilon^{1/2}(x-Mt)\right) \label{A72}$$

$$\Rightarrow\overline{\underline{\frac{^{{}}}{{}}U(x,t)\equiv\varepsilon
U^{(1)}(x,t)=3\delta M\sec^{2}\left(  (\delta M/4b)^{1/2}(x-Mt)\right)
,\frac{^{{}}}{{}}}}\label{A73}$$

et, pour des ondes acoustiques ioniques ($b=1/2)$, on obtient

$$\overline{\underline{U(x,t)=U(s)=3\ \delta M\sec^{2}\left(  (\delta
M/2)^{1/2}(x-Mt)\right)  ,\qquad s=\varepsilon^{1/2}(x-Mt),\qquad b=\frac
{1}{2}.}}\label{A74}$$

Cette solution stationnaire est appelée onde (ou impulsion) solitaire ou
encore soliton. Le soliton se propage le long de $s$ (ou de $x$) avec la
vitesse $v=M$ (i.e., $v_{i}=Mc_{s}$) par rapport à ($\mathcal{R}_{L}),$
sans aucune modification de sa forme : c’est une structure stable; il
est immobile dans le référentiel ($\mathcal{R}_{S})$ en mouvement avec
la vitesse $M$ par rapport à ($\mathcal{R}_{L})$. Puisque $M\gtrsim1$
(voir ([A71])-([AA71]) et ([A72])), le soliton acoustique ionique est
une structure non-linéaire stable et supersonique se propageant avec une
vitesse légèrement supérieure à la vitesse acoustique ionique,
$v_{i}=Mc_{s}\gtrsim c_{s}$. La img/figure 3 montre la forme d’un
soliton dans le référentiel ($\mathcal{R}_{S})$ : la perturbation $U(s)$
montre un profil symétrique (fonction paire) laissant le plasma ambiant
non perturbé à la fois avant et après le passage du front du soliton; en
effet, la perturbation $U(s)$ s’annule pour $\left|  s\right|
\rightarrow\pm\infty;$ $U(s)$ atteint son maximum en $s=0;$ l’amplitude
du soliton est donc $U_{0}\equiv U(s=0)=3\ \delta M$ (img/figure 3).

![image](img/fig2.tif)\
**Figure 3.**<span> Soliton acoustique ionique dans le référentiel
</span>$(R_{S})$<span> en mouvement avec la vitesse
</span>$Mc_{s}$<span> par rapport à </span>$(R_{L})$<span>.</span>

Puisque $U_{0}=3\ \delta M=3(M-1),$ il s’en suit qu’un soliton plus
rapide a une amplitude plus grande qu’un soliton plus lent. D’autre part
on peut définir la largeur caractéristique du soliton ([A73]) par

$$\Delta s\propto\sqrt{\frac{4b\varepsilon}{\delta M}}=\sqrt{\frac
{12b\varepsilon}{U_{0}}},\label{A76}$$

et, par conséquent, le soliton est d’autant plus large qu’il est lent et
de faible amplitude et inversement.

Puisque l’équation vérifiée par le soliton peut s’écrire sous la forme
d’une loi de conservation

$$\frac{\partial}{\partial\tau}U+\frac{\partial}{\partial\xi}\left(
b\frac{\partial^{2}U}{\partial\xi^{2}}+\frac{U^{2}}{2}\right)  =0,\label{A78}$$

et que $U(\xi,\tau)$,$\frac{\partial^{n}U}{\partial\xi^{n}}(\xi,\tau
)\rightarrow0$ pour $\xi\rightarrow\pm\infty$, on obtient que la surface
balayée par le soliton est un invariant

$$\frac{\partial}{\partial\tau}\underset{-\infty}{\overset{\infty}{\int}}U(\xi,\tau)d\xi=-\left(  b\frac{\partial^{2}U}{\partial\xi^{2}}+\frac{U^{2}}{2}\right)  _{-\infty}^{\infty}\Rightarrow\frac{\partial}{\partial\tau
}\underset{-\infty}{\overset{\infty}{\int}}U(\xi,\tau)d\xi=0,\label{A80}$$

résultat que nous avions déjà évoqué au paragraphe précédent. Ainsi, le
soliton est une structure stable : $U(\xi,\tau)$ subit des distortions
par rapport à son profil initial telles que la surface totale ([A80])
(c’est-à-dire la quantité de mouvement totale) reste constante.

Le nombre et les caractéristiques de l’ensemble des solitons solutions
de l’équation KdV dépendent principalement des conditions initiales
(nécessaires pour résoudre complètement l’équation différentielle KdV),
c’est-à-dire de la nature et des propriétés de l’impulsion appliquée en
$t=0,$ comme nous l’avons vu plus haut (img/figure 2). Des simulations
numériques ont montré qu’une perturbation sinusoïdale initiale génère un
train de solitons de vitesses différentes (img/figure 2a); ceux qui ont
les vitesses les plus grandes ont les plus fortes amplitudes et sont les
plus étroits, et inversement.

Puisque les solitons les plus rapides du train vont rattraper les
solitons les plus lents, on peut s’attendre à ce qu’ils interagissent
entre eux. Or les calculs théoriques et les simulations numériques ont
montré que rien de tel ne survient. Les solitons ne subissent quasiment
aucune interaction due à leurs collisions mutuelles. Après leur
collision, deux solitons continuent leur propagation en conservant leur
forme, comme le montre la img/figure 4 où un soliton de vitesse
$M_{2}c_{s}$, plus rapide, dépasse un soliton de vitesse $M_{1}c_{s}$,
plus lent, sans interagir avec lui. Cette propriété remarquable est
caractéristique des solitons. Dans la chaîne qu’ils forment quand
$\tau\rightarrow\infty$, les solitons se propagent dans un ordre bien
déterminé, celui possédant la plus faible amplitude (et la largeur la
plus grande) étant le plus lent et celui possédant la plus grande
amplitude (et la plus petite largeur) étant le plus rapide (voir la
img/figure 2a).

![image](img/fig3.tif)\
**Figure 4.** <span>Collision entre deux solitons : à gauche, le soliton
le plus rapide (le plus étroit) entre en collision avec le soliton le
plus lent et le dépasse.</span>

Le potentiel de Sagdeev
-----------------------

Par analogie avec l’équation de Newton à une dimension incluant une
force électrostatique $F_{el}(x)$

$$m\ddot{x}=F_{el}(x)\propto-\frac{dV}{dx},\label{A81}$$

où $V$ est un potentiel, ([A61]) peut s’écrire sous la forme

$$b\frac{d^{2}U}{ds^{2}}=c_{M}U-\frac{U^{2}}{2}\equiv-\frac{dV_{S}}{dU},\label{A82}$$

où le pseudo-potentiel $V_{S}$ est appelé potentiel de Sagdeev; pour une
pseudo-particule en mouvement dans le potentiel de Sagdeev, les
variables $s$ et $U$ jouent le rôle du temps et de l’espace,
respectivement. Le potentiel $V_{S}(U)$ s’obtient en intégrant ([A82])

$$V_{S}(U)=-c_{M}\frac{U^{2}}{2}+\frac{U^{3}}{6}.\label{A83}$$

Le pseudo-potentiel $V_{S}(U)$ est représenté sur la img/figure 5a ainsi
que la pseudo-trajectoire d’un soliton; le soliton est réfléchi en
$U=U_{0}$ (voir en correspondance la img/figure 5b montrant la structure
du soliton); en effet, considérant ([A68]) et puisque$\ \sec x<1$
$\forall x,$ l’amplitude du soliton vérifie $U(=U^{(1)})<3c_{M}$ ou
encore $U(=\varepsilon U^{(1)})<3\delta M$ ([A71]).

![image](img/fig5.tif)\
**Figure 5.** <span>(a) Potentiel de Sagdeev </span>$V_{S}(U)$<span> et
(b) profil </span>$U(s)$<span> correspondant du soliton.</span>

Conditions d’existence du soliton acoustique ionique
----------------------------------------------------

Montrons que le soliton acoustique ionique n’existe que pour un nombre
de Mach vérifiant $1<M\lesssim1.6$.

Considérons les équations ([A28])-([A30])

$$\frac{\partial^{2}\Phi}{\partial x^{2}}=e^{\Phi}-n,\qquad\frac{\partial
n}{\partial t}+\frac{\partial(nv)}{\partial x}=0,\qquad\left(  \frac{\partial
v}{\partial t}+v\frac{\partial v}{\partial x}\right)  =-\frac{\partial\Phi
}{\partial x},\label{A90}$$

où l’on fait le changement de variable suivant pour passer du
référentiel du laboratoire au référentiel se déplaçant à la vitesse $M$
(voir aussi ([A70]) où la normalisation est différente d’un facteur
$\varepsilon^{1/2}$)

$$s=x-Mt,\qquad\frac{\partial}{\partial x}\leftrightarrow\frac{d}{ds},\qquad\frac{\partial}{\partial t}\leftrightarrow-M\frac{d}{ds},\label{A91}$$

par analogie avec ([A53]) et ([A57]). On obtient alors les relations

$$(v-M)\frac{dv}{ds}=-\frac{d\Phi}{ds}\Rightarrow-\Phi=\frac{v^{2}}{2}-Mv+K\Rightarrow v=M\pm\sqrt{M^{2}-2(K+\Phi)},\label{A92}$$

$$-M\frac{dn}{ds}+\frac{d(nv)}{ds}=0\Rightarrow(v-M)\frac{dn}{ds}=-n\frac
{dv}{ds}\Rightarrow\frac{dn}{n}=\frac{dv}{M-v}\Rightarrow n(v-M)=K^{\prime
},\label{A93}$$

où $K$ et $K^{\prime}$ sont des constantes. Puisque les perturbations
sont localisées, le plasma n’est pas perturbé en $s\rightarrow
\pm\infty$

$$s\rightarrow\pm\infty\Rightarrow\Phi\rightarrow0,\qquad\frac{d\Phi}{ds}\rightarrow0,\qquad v\rightarrow0\ (v_{i}\rightarrow0),\qquad
n\rightarrow1\ (n_{i}\rightarrow n_{0}).\label{AA94}$$

Ces conditions aux limites montrent que $K=0$ et $K^{\prime}=-M$ dans
([A92])-([A93]); par conséquent

$$n=\frac{M}{M-v},\qquad v=M-\sqrt{M^{2}-2\Phi},\label{AB94}$$

le signe $-$ devant la racine carrée dans ([AB94]) étant déterminé par
les conditions aux limites $s\rightarrow\pm\infty.$ D’autre part, en
intégrant l’équation de Poisson dans ([A90]) il vient

$$\int\frac{d\Phi}{ds}\frac{d^{2}\Phi}{ds^{2}}ds=\int e^{\Phi}d\Phi-\int
nd\Phi\Rightarrow\frac{1}{2}\left(  \frac{d\Phi}{ds}\right)  ^{2}=e^{\Phi
}+K^{\prime\prime}-\int nd\Phi,\qquad K^{\prime\prime}=\mathrm{const},\label{A95}$$

et en utilisant ([A92]) et ([AB94]), on obtient

$$\frac{1}{2}\left(  \frac{d\Phi}{ds}\right)  ^{2}=e^{\Phi}+K^{\prime\prime
}+\int\frac{M}{M-v}(v-M)dv=e^{\Phi}+K^{\prime\prime}-Mv\label{AA95}$$

$$\Rightarrow\frac{1}{2}\left(  \frac{d\Phi}{ds}\right)  ^{2}=e^{\Phi
}-1-Mv,\label{AB95}$$

où l’on a utilisé ([AA94]) pour déterminer la constante
$K^{\prime\prime}$; finalement, en tenant compte de ([AB94]), ([AB95])
s’écrit

$$\overline{\underline{\frac{1}{2}\left(  \frac{d\Phi}{ds}\right)  ^{2}=e^{\Phi
}-1+M(\sqrt{M^{2}-2\Phi}-M)\equiv-V_{S}(\Phi)}},\label{A98}$$

où $V_{S}(\Phi)$ est le potentiel de Sagdeev. La dérivée
$\frac{d\Phi}{ds}$ s’annule pour le maximum $\Phi_{0}$ de $\Phi$, qui
est l’amplitude du soliton; par conséquent $V_{S}(\Phi_{0})=0,$ ce qui
entraîne que

$$M(M^{2}-2\Phi_{0})^{1/2}=(M^{2}+1)-e^{\Phi_{0}}.\label{A99}$$

En élevant ([A99]) au carré, il vient

$$-M^{2}(2\Phi_{0}+2-2e^{\Phi_{0}})=e^{2\Phi_{0}}-2e^{\Phi_{0}}+1\Rightarrow
M^{2}=\frac{(e^{\Phi_{0}}-1)^{2}}{2(e^{\Phi_{0}}-1-\Phi_{0})}.\label{A100}$$

D’autre part, le terme img/figurant sous la racine carrée dans ([A98])
doit être positif, et par conséquent la condition suivante est
nécessaire

$$M^{2}\geq2\Phi,\quad\forall\Phi\Rightarrow M^{2}\geq2\Phi_{0}.\label{A101}$$

En injectant la condition seuil $M^{2}=2\Phi_{0}$ dans ([A100]), une
résolution numérique conduit à

$$2\Phi_{0}\leq\frac{(e^{\Phi_{0}}-1)^{2}}{2(e^{\Phi_{0}}-1-\Phi_{0})}\Rightarrow\Phi_{0}<(\Phi_{0})_{\max}\simeq1.3.\label{AA101}$$

La valeur correspondante du nombre de Mach s’obtient alors par la
condition seuil

$$M^{2}=2(\Phi_{0})_{\max}\Rightarrow M\simeq1.6.\label{A102}$$

Puisqu’un soliton d’amplitude plus faible se déplace avec une vitesse
plus faible qu’un soliton d’amplitude plus élevée, on obtient finalement
la condition d’existence du soliton acoustique ionique sous la forme

$$\underline{\overline{\frac{^{{}}}{{}}\Phi_{0}<(\Phi_{0})_{\max}\simeq
1.3\Rightarrow M<M_{\max}\simeq1.6,\frac{^{{}}}{{}}}}\label{AB102}$$

où $c_{s}M_{\max}$ est la vitesse maximale possible du soliton$.$

D’autre part, puisque $\left(  \frac{d\Phi}{ds}\right)  ^{2}>0$, ([A98])
implique que

$$e^{\Phi}-1+M(\sqrt{M^{2}-2\Phi}-M)>0.\label{A103}$$

En développant ([A103]) jusqu’au second ordre en $\Phi\ll1$ (on rappelle
qu’on considère des perturbations faibles, les solitons étant supposés
de faible amplitude), on obtient

$$1+\Phi+\frac{\Phi^{2}}{2}-1+M(M(1-\frac{2\Phi}{M^{2}})^{1/2}-M)=\Phi
+\frac{\Phi^{2}}{2}+M^{2}(1-1-\frac{\Phi}{M^{2}}-\frac{1}{8}\frac{4\Phi^{2}}{M^{4}}+...)\simeq\frac{\Phi^{2}}{2}-\frac{\Phi^{2}}{2M^{2}}>0\Rightarrow
M>1,\label{A104}$$

montrant que le soliton est supersonique.

Finalement, en combinant ([AB102]) et ([A104]), le soliton acoustique
ionique n’existe que si son nombre de Mach $M$ vérifie

$$\overline{\underline{\frac{^{{}}}{{}}1<M\lesssim1.6.\frac{^{{}}}{{}}}}\label{A105}$$

On verra plus loin que cette condition est la même dans le cas des ondes
de choc acoustiques ioniques (voir le paragraphe suivant) puisque les
équations KdV et Burger-KdV (cette dernière décrivant les ondes de choc
non collisionnelles) ont le même potentiel de Sagdeev. En effet, la
relation ([A105]) résulte de la forme du potentiel de Sagdeev et non de
l’équation différentielle non-linéaire considérée.

Ainsi, on a finalement montré qu’il existe des structures non-linéaires
qui peuvent se propager sans déformation, à une vitesse légèrement
supérieure à la vitesse acoustique ionique (structure supersonique),
dans un plasma où les ions sont froids et les électrons chauds et
isothermes : ce sont des solitons acoustiques ioniques.

L’ONDE DE CHOC ACOUSTIQUE IONIQUE
=================================

L’onde de choc non collisionnelle
---------------------------------

On a vu que le soliton est une onde non-linéaire associée à des
perturbations localisées et symétriques qui n’affectent pas le plasma
pour $s\rightarrow\pm\infty.$ Celui-ci reste en équilibre et identique
en amont et en aval du front du soliton. Supposons à présent qu’une
partie des ions du plasma ambiant soient réfléchis par la barrière de
potentiel du soliton (il suffit pour cela que ces ions aient une énergie
totale inférieure à la barrière de potentiel); après réflection, ces
ions rebroussent chemin, pouvant introduire une dissymétrie dans le
plasma et provoquer une dissipation[^8]. On peut décrire ce type de
processus analytiquement en introduisant un terme dissipatif dans
l’équation KdV : on obtient alors l’équation dite de Burger-KdV, dont
les solutions stationnaires sont des ondes de choc non collisionnelles.
L’état du plasma en amont d’une onde de choc est différent de son état
en aval de l’onde; celle-ci permet de connecter entre eux le plasma non
perturbé en amont et le plasma perturbé par des oscillations en aval.
Ainsi, une onde de choc peut apparaître dans un plasma si pour une
raison quelconque une dissymétrie des paramètres physiques apparaît.

Dans un gaz neutre, l’onde de choc non collisionnelle ne peut exister,
car ce sont les collisions entre les molécules qui assurent la
transmission de la quantité de mouvement et la propagation de l’onde
acoustique : le phénomène de viscosité moléculaire (collisions) entre en
compétition avec l’effet de raidissement du front de l’onde et empêche
celle-ci de s’effondrer. Dans un plasma non collisionnel par contre, le
transfert de la quantité de mouvement est assuré par des ondes
engendrées par les perturbations de courant et de densité de charge :
l’existence d’ondes de choc non collisionnelles est par conséquent
possible.

Rôle de la dissipation
----------------------

Nous nous limiterons ci-après, comme pour les solitons, au cas des ondes
de chocs acoustiques ioniques. Examinons tout d’abord la balance entre
dissipation et non-linéarité dans l’équation de Burger ([A12]). Celle-ci
comprend un terme de dissipation $\alpha\frac
{\partial^{2}U}{\partial\xi^{2}}$ qui tend à compenser l’action du terme
non-linéaire $U\frac{\partial U}{\partial\xi}$: ainsi, l’évolution de
l’onde ne se limite pas au raidissement du front et à son
effondrement.[^9]

Comme dans le cas des solitons, cherchons des ondes stationnaires
solutions de l’équation de Burger ([A12]). En utilisant la variable
$s=\xi
-c_{M}\tau$ (voir équations ([A53])-([A61])), on peut mettre ([A12])
sous la forme

$$\frac{\partial U}{\partial\tau}+U\frac{\partial U}{\partial\xi}-\alpha
\frac{\partial^{2}U}{\partial\xi^{2}}=0\Rightarrow-c_{M}\frac{dU}{ds}+U\frac{dU}{ds}-\alpha\frac{d^{2}U}{ds^{2}}=0.\label{A106}$$

En intégrant ([A106]) on obtient

$$-c_{M}\int\frac{dU}{ds}ds+\frac{1}{2}\int\frac{dU^{2}}{ds}ds-\alpha\int\frac{d}{ds}\left(  \frac{dU}{ds}\right)  ds=-c_{M}U+\frac{U^{2}}{2}-\alpha\frac{dU}{ds}=K.\label{A107}$$

Rappelons que le choc étant une structure dissymétrique qui laisse le
plasma non perturbé en amont, les conditions aux limites ([AA94]) sont
encore applicables pour $s\rightarrow+\infty$ (mais pas pour
$s\rightarrow
-\infty$). Considérant la famille de solutions pour $K=0$, il s’en suit
que

$$\alpha\frac{dU}{ds}=\frac{U}{2}(U-2c_{M})\Rightarrow\frac{2\alpha
dU}{U(U-2c_{M})}=ds\Rightarrow2\alpha\int\frac{dU}{(U-c_{M})^{2}-c_{M}^{2}}=2\alpha\int\frac{dy}{y^{2}-c_{M}^{2}}=s+K^{\prime},\label{A108}$$

où $K^{\prime}$ est une constante et où l’on a posé $y=U-c_{M}$.
Finalement (on rappelle que $\alpha>0$ et $c_{M}>0$), on obtient

$$-\frac{2\alpha}{c_{M}}\tanh^{-1}\left(  \frac{y}{c_{M}}\right)  =s+K^{\prime
}\Rightarrow\frac{y}{c_{M}}=\tanh\left[  -\frac{c_{M}}{2\alpha}(s+K^{\prime
})\right]  \Rightarrow U(s)=c_{M}(1-\tanh\left[  \frac{c_{M}}{2\alpha
}(s+K^{\prime})\right]  ),\label{A109}$$

et, par conséquent, en choisissant des conditions initiales
correspondant à $K^{\prime}=0$, on obtient une solution de l’équation de
Burger sous la forme

$$U(s)\equiv U^{(1)}(s)=c_{M}(1-\tanh\left(  \frac{c_{M}s}{2\alpha}\right)
).\label{A110}$$

En utilisant les coordonnées $x$ et $t$ dans le référentiel du
laboratoire on a

$$\underline{\overline{U(x,t)=\varepsilon U^{(1)}(s)=\delta M\left[
1-\tanh\frac{\delta M}{2\alpha\varepsilon^{1/2}}(x-Mt)\right]  ,\qquad
s=\varepsilon^{1/2}(x-Mt).}}\label{A111}$$

La variation de $U(s)$ dans le référentiel ($\mathcal{R}_{S}$) en
mouvement avec le choc est représentée sur la img/figure 8$.$ La
solution stationnaire de l’équation de Burger est une rampe de choc qui
se propage avec le nombre de Mach $M$ le long de $x$ (i.e., à la vitesse
$Mc_{s}$ par rapport à ($\mathcal{R}_{L}$)) : le choc est une structure
supersonique tout comme le soliton ($M>1$). La dissipation, qui
contrecarre la non-linéarité, empêche finalement l’onde de s’effondrer
par suite du raidissement du front et permet ainsi la formation de la
rampe du choc. La hauteur de la rampe est $2\delta M$; sa largeur
$\Delta s$ inversement proportionnelle à $\delta M$, est obtenue en
calculant la pente de $U(s)$ en $s=0$

$$U(s)=\delta M\left[  1-\tanh\frac{\delta M}{2\alpha\varepsilon^{1/2}}s\right]
\Rightarrow\left(  \frac{dU}{ds}\right)  _{s=0}=-\delta M\left(  \frac{\delta
M}{2\alpha\varepsilon^{1/2}}\right)  \left(  \frac{1}{\cosh^{2}\frac{\delta
M}{2\alpha\varepsilon^{1/2}}s}\right)  _{s=0}\label{A112}$$

$$\Rightarrow\frac{\Delta U}{\left\vert \Delta s\right\vert }=\frac{(\delta
M)^{2}}{2\alpha\varepsilon^{1/2}}\Rightarrow\left\vert \Delta s\right\vert
=2\delta M\frac{2\alpha\varepsilon^{1/2}}{(\delta M)^{2}}=4\varepsilon
^{1/2}\frac{\alpha}{\delta M}.\label{AA112}$$

Plus la dissipation est forte (plus $\alpha$ est grand) et plus la rampe
est large. Lorsque la dissipation disparaît ($\alpha\rightarrow0$), la
rampe tend à devenir verticale et sa largeur est quasi-nulle : dans ce
cas la non-linéarité n’est quasiment plus compensée par la dissipation
et le raidissement du front est l’effet dominant.

Dans chaque zone du choc, la vitesse des ions est différente (il en est
de même des perturbations de densité et de potentiel). A la traversée de
la rampe le fluide ionique est accéléré par l’onde de choc.

![image](img/fig7.tif)\
**Figure 8.** <span>Solution de l’équation de Burger : onde de choc non
collisionnelle (cas où le terme de dispersion n’est pas
considéré).</span>

Solutions de l’équation de Burger-KdV
-------------------------------------

Ajoutons à présent le terme dispersif
$b\frac{\partial^{3}U}{\partial\xi^{3}}$ dans l’équation de Burger

$$\frac{\partial U}{\partial\tau}+U\frac{\partial U}{\partial\xi}+b\frac
{\partial^{3}U}{\partial\xi^{3}}-\alpha\frac{\partial^{2}U}{\partial\xi^{2}}=0,\label{A113}$$

(notons que cela revient au même d’ajouter le terme dissipatif
$-\alpha\frac{\partial^{2}U}{\partial\xi^{2}}$ dans l’équation KdV),
formant ainsi l’équation dite de Burger-KdV[^10]. Cherchons des
solutions stationnaires de ([A113]) de la même façon que précédemment
(voir ([A53])-([A61])); on obtient alors

$$-c_{M}\frac{dU}{ds}+U\frac{dU}{ds}+b\frac{d^{3}U}{ds^{3}}-\alpha\frac{d^{2}U}{ds^{2}}=0\label{A114}$$

$$\Rightarrow-c_{M}\int\frac{dU}{ds}ds+\frac{1}{2}\int\frac{d(U^{2})}{ds}ds+b\int\frac{d}{ds}\left(  \frac{d^{2}U}{ds^{2}}\right)  ds-\alpha
\int\frac{d}{ds}\left(  \frac{dU}{ds}\right)  ds=\mathrm{const}\label{A115}$$

$$\Rightarrow-c_{M}U+\frac{U^{2}}{2}+b\frac{d^{2}U}{ds^{2}}-\alpha\frac{dU}{ds}=\mathrm{const}=K=0.\label{A116}$$

Par analogie avec l’équation de Newton à une dimension incluant une
force électrostatique $F_{el}(x)$ et une force de friction $F_{f}(x)$

$$m\ddot{x}=F_{el}(x)+F_{f}(x)\propto-\frac{\partial V_{S}}{\partial x}+\alpha\dot{x},\label{A117}$$

([A116]) se met sous la forme

$$b\frac{d^{2}U}{ds^{2}}-\alpha\frac{dU}{ds}=c_{M}U-\frac{U^{2}}{2}\equiv
-\frac{\partial V_{S}}{\partial U},\label{A118}$$

où $V_{S}$ est le potentiel de Sagdeev, identique à celui obtenu
précédemment pour les solitons (voir ([A82])-([A83])). Il ne s’agit pas
ici de résoudre analytiquement l’équation ([A116]) mais seulement de
décrire le sens physique des solutions, qui, comme on peut le prévoir,
combinent des solutions des équations de Burger et de Korteweg-de Vries,
c’est-à-dire des solutions du type rampe de choc et soliton.

Analysons tout d’abord le mouvement d’une pseudo-particule dans le
potentiel de Sagdeev associé à un soliton (voir img/figure 5a). Partant
de $U\simeq0$, la pseudo-particule voit sa vitesse augmenter jusqu’à ce
qu’elle soit réfléchie lorsque $U=U_{0}=3\delta M$; puis
la pseudo-particule rebrousse chemin, sa vitesse décroissant jusqu’à
zéro; elle ne subira aucune autre réflection. Ce mouvement dans le
potentiel de Sagdeev correspond à un soliton, comme le montre la
correspondance entre les img/figures 5a et 5b. Dans le cas de l’équation
de Burger-KdV (où l’on est en présence d’un effet supplémentaire de
dissipation), la pseudo-particule se meut dans le même potentiel de
Sagdeev, mais elle n’a pas le même comportement. En effet, soit une
pseudo-particule située en $U=U_{C}$ (voir la img/figure 9a représentant
la variation du potentiel de Sagdeev $V_{S}(U)$). En présence de
dissipation mais sans dispersion (équation de Burger), la particule
tombe dans le puits de potentiel vers sa position d’équilibre, se
stabilisant au point A d’énergie minimale quand $\tau\rightarrow\infty.$
Si la dispersion s’ajoute à la dissipation, la particule rejoint son
point d’équilibre après avoir effectué plusieurs oscillations dans le
puits (img/figure 9a). La variation correspondante de $U(s)$ en fonction
de $s$ dans le repère en mouvement avec le choc (img/figure 9b) combine
alors une rampe caractéristique d’un choc avec des oscillations
associées à la dispersion, correspondant aux oscillations de la
pseudo-particule dans le puits; $U(s)$ oscille autour de la vitesse
$U_{A}=2\delta M$ avec un maximum $U_{B}$ au point B (comparer aussi
avec la img/figure 8 qui correspond au cas où la dispersion est très
faible ($b\rightarrow0$)). Notons que le choc représenté sur la
img/figure 9b se déplace vers la droite si on le considère dans le
référentiel du laboratoire, la région définie comme l’amont étant la
première rencontrée par le choc dans son déplacement.

![image](img/fig9new.tif)\
**Figure 9.** <span>(a) Potentiel de Sagdeev </span>$V_{S}(U)$<span> et
(b) profil </span>$U(s)$<span> correspondant de l’onde de choc non
collisionnelle.</span>

MISE EN EVIDENCE EXPERIMENTALE
==============================

Observations de solitons
------------------------

Différents types de solitons ont été observés en laboratoire et dans la
magnétosphère terrestre. Dans le premier exemple que nous présentons
ici[^11], la formation de solitons acoustiques ioniques et leur
interaction ont été étudiées dans un caisson à plasma appelé ”*machine à
double plasma*” (densité $n_{e}\simeq
$10$^{9}\ $cm$^{-3}$, températures $T_{e}\simeq$1.5-3 eV et $T_{i}\simeq
$0.2 eV). Dans ce type de machine, deux plasmas produits par deux
décharges indépendantes sont séparés par une grille polarisée
négativement qui empêche les électrons de passer d’un plasma à l’autre;
l’application pulsée de différences de potentiel entre les deux plasmas
permet l’excitation d’ondes[^12]. Lorsque les deux solitons se déplacent
dans le même sens avec des vitesses différentes (img/figure 6a), le
soliton le plus rapide (le plus étroit et le plus haut) finit par
dépasser le plus lent (chaque trace sur la img/figure 6a est séparée de
la suivante par un intervalle de 10$\mu s$, la trace supérieure
correspondant au temps initial): en effet, au temps final, le soliton le
plus rapide n’est en plus en queue comme en $t=0$ mais en tête. La
collision entre les solitons s’est effectuée sans que ceux-ci ne
subissent d’altération autre que celle de l’amortissement linéaire de
Landau, très visible sur la img/figure 6a (comparer les amplitudes des
solitons aux temps initial et final). D’autre part, dans la même
expérience, la collision entre deux solitons de vitesses égales mais de
sens opposés a été étudiée (img/figure 6b): de même que pour le cas
précédent, ils ne sont pas affectés par la collision (notons que pour
les mesures de la img/figure 6b, l’effet Landau est négligeable). On
remarque que les deux solitons se superposent linéairement lors de leur
croisement (interaction de type linéaire), contrairement au premier cas
(img/figure 6a) où les deux solitons restent toujours séparés
(interaction de type non-linéaire).

![image](img/fig6.tif)\
**Figure 6.** <span>Collision entre deux solitons (a) qui se propagent
dans le même sens et (b) dans des directions opposées (en
</span>$t=0$<span> (voir les courbes supérieures), chaque soliton est
repéré par une flèche indiquant sa vitesse) : perturbation de la densité
électronique (en unités arbitraires) en fonction de la distance (en cm),
pour différents instants de temps (séparés de 10</span>$\mu s$
<span>dans la img/figure 6a et indiqués sur la img/figure
6b)</span>$.$<span> La longueur de Debye est de l’ordre de
</span>$\lambda
_{D}\simeq2\ 10^{-2}$<span>cm</span>$.$

Dans la même expérience, après avoir vérifié l’équation de dispersion
linéaire des ondes acoustiques ioniques se propageant dans un plasma non
magnétisé, on a augmenté l’amplitude de l’impulsion initiale permettant
d’exciter les ondes pour faire apparaître des effets non-linéaires. La
img/figure 7 montre, dans le référentiel se déplaçant avec la vitesse
acoustique ionique, l’excitation d’une impulsion initiale (courbe
supérieure représentant le potentiel appliqué en $t=0$) ainsi que son
évolution au cours du temps pour différentes positions dans le plasma
(courbes inférieures représentant la variation temporelle de la
perturbation de densité normalisée pour différentes distances par
rapport à la grille interfaçant les deux plasmas). L’expérience montre
des résultats similaires à ceux obtenus lors de la résolution numérique
de l’équation KdV (comparer avec la img/figure 2) : après le
raidissement du front, une structure oscillante se développe et,
finalement, un train de solitons apparaît.

![image](img/fig7new.tif)\
**Figure 7.** <span>Variation de la perturbation de la densité
électronique normalisée en fonction du temps (5 </span>$\mu
s$<span> par division) pour différentes distances (en cm) par rapport à
la grille interfaçant les deux plasmas. L’impulsion excitatrice
(appliquée en </span>$\tau=0,$<span> de l’ordre de 1V) est la courbe
supérieure.</span>

Observations d’ondes de chocs non collisionnelles
-------------------------------------------------

Dans la même expérience de laboratoire que celle mentionnée au
paragraphe précédent (machine à double plasma), une impulsion (rampe de
potentiel) est générée à l’instant initial dans un plasma dont le profil
de densité spatial présente un gradient[^13] (situé à la position de la
grille, c’est-à-dire à l’interface des deux plasmas). L’évolution
temporelle de la réponse du plasma à cette excitation montre la
propagation d’une onde de choc acoustique ionique se déplaçant vers la
droite de la img/figure 10; celle-ci représente la variation de la
densité du plasma en fonction de la distance à la grille pour différents
instants $t$ et différentes températures $T_{e}.$ On observe un flux
d’ions réfléchis par le front du choc; celui-ci est responsable de la
dissipation (notons que ce flux est d’autant plus important que $T_{e}$
est plus faible).

![image](img/fig10new.tif)\
**Figure 10. **<span>Variation de la densité électronique du plasma en
fonction de la distance à la grille pour différents instants de temps
</span>$\tau=$<span>12, 24, 36, 48, 72 </span>$\mu s$<span>; (a)
</span>$T_{e}=1.5$<span> eV et (b) </span>$T_{e}=3$<span> eV
(</span>$T_{i}=0.2$<span> eV,
</span>$n_{0}=10^{9}$<span>cm</span>$^{-3}$<span> est la densité du
plasma non perturbé). Le flux des ions est indiqué par des flèches
verticales (streaming ions). Une échelle représentant
30</span>$\lambda_{D}$<span> est représentée sur la img/figure.</span>

D’autre part, des ondes de choc non collisionnelles ont été maintes fois
observées in-situ par des sondes et des satellites au voisinage de la
Terre et des autres planètes. Ces ondes de choc sont produites dans les
zones où le vent solaire rencontre le champ magnétique de la planète.
Par exemple, les sondes Voyager ont détecté des ondes acoustiques
ioniques engendrées par les ions réfléchis par l’onde de choc de
Jupiter; la img/figure 11 montre la variation du champ magnétique des
ondes en fonction du temps, enregistré par la sonde lors de sa traversée
de l’onde de choc (le vent solaire s’écoule de la gauche vers la droite
sur la img/figure). Sur le spectrogramme de la img/figure 11 où la
fréquence est représentée en fonction du temps, on observe dans le
domaine des très basses fréquences les ondes acoustiques ioniques
excitées. Les ondes de plus haute fréquence visibles sur le
spectrogramme sont dues à des électrons chauffés par les ondes de choc.

![image](img/fig11.tif)\
**Figure 11.** <span>Variation en fonction du temps du champ magnétique
(en Gauss</span>$\times$<span>10</span>$^{-5}$<span>) des ondes (courbe
supérieure) et des fréquences (en kHz) observées (image inférieure) lors
de la traversée par la sonde Voyager de l’onde de choc de
Jupiter.</span>

[^1]: Notons toutefois que les amplitudes des ondes ne doivent pas être
    trop élevées. En effet, si tel était le cas, d’autres méthodes de
    résolution devraient être substituées à la méthode perturbative, et
    nous serions dans le domaine de la turbulence forte qui n’est pas
    notre propos dans ce chapitre.

[^2]: Un mille vaut 1.6 km.

[^3]: Un pied vaut 30.48 cm.

[^4]: Quelques années plus tard, en 1865, dans sa ”Recherche
    expérimentale sur la propagation des ondes”, M. Bazin résume ainsi
    :” *Toutes les fois qu’un certain volume d’eau, momentanément
    soulevé au-dessus du niveau général de la masse, est abandonné à
    lui-même, il donne naissance, en s’affaissant pour y rentrer, à une
    onde de translation. Ce soulèvement momentané peut être produit soit
    par le mouvement d’un solide (comme le bateau dont il vient d’être
    parlé) agissant à la façon d’un piston qui pousse le liquide, soit
    par la projection d’un certain volume d’eau dans un liquide
    tranquille, etc. L’onde de translation est tout entière en saillie
    au-dessus du niveau de l’eau sur laquelle elle chemine, ce qui la
    distingue des ondes oscillatoires que nous étudierons plus loin et
    dont chaque saillie est accompagnée d’une cavité correspondante. De
    plus, les ondes d’oscillation sont toujours réunies par groupe et se
    succèdent à intervalles réguliers : l’onde de translation chemine
    seule, aussi Scott Russell a-t’il donné à celle qu’il a étudiée la
    dénomination d’onde solitaire, qui est appliquée plus spécialement
    aujourd’hui à une onde de translation particulière ayant la
    propriété de se propager sans se déformer*”.

[^5]: N.J. Zabusky and M.D. Kruskal, Interaction of solitons in a
    collisionless plasma and the recurrence of initial states, *Phys.
    Rev. Lett*., 15(6), 240, 1965.

[^6]: Ces ondes acoustiques de très grandes longueurs d’onde dans un
    milieu isotrope ont une équation de dispersion de la forme
    $\omega^{2}\simeq c_{s}^{2}k^{2}.$ Dans ce cas, les ondes se
    propagent sans dispersion: leur vitesse de groupe est égale à leur
    vitesse de phase et à la vitesse $c_{s}$. Si les ondes ne possèdent
    pas de très grandes longueurs d’ondes, la dispersion apparaît sous
    la forme d’une correction $-\beta^{2}k^{4}$
    $$\omega^{2}\simeq c_{s}^{2}k^{2}-\beta^{2}k^{4}\Rightarrow\omega\simeq
    c_{s}k-\frac{\beta^{2}}{2c_{s}}k^{3},$$ le dernier terme en $k^{3}$
    correspondant à $\frac{\partial^{3}U}{\partial\xi^{3}}.$

[^7]: On tient compte des relations suivantes
    $$\sec(x)=\sec(-x),\qquad\sec x=\frac{1}{\cosh x},\qquad\tanh^{2}x+\sec
    ^{2}x=1\qquad\tanh^{-1}x=\frac{1}{2}\mathrm{Ln}\left[  \frac{x+1}{x-1}\right]
    .$$

[^8]: Des processus turbulents peuvent également être responsables de la
    dissipation.

[^9]: La façon la plus simple de voir pourquoi le terme
    $\alpha\frac{\partial^{2}U}{\partial\xi^{2}}$ traduit une
    dissipation est de linéariser l’équation de Burger (on néglige le
    terme en $U^{2}$), de poser $U\propto\exp(i\omega\tau-ik\xi)$ et de
    calculer l’équation de dispersion
    $$\frac{\partial U}{\partial\tau}+U\frac{\partial U}{\partial\xi}-\alpha
    \frac{\partial^{2}U}{\partial\xi^{2}}=0\Rightarrow i\omega U+\alpha
    k^{2}U\simeq0\Rightarrow\omega\simeq i\alpha k^{2}.$$ Ainsi l’on
    obtient $U\propto\exp(i\operatorname{Re}(\omega)\tau)\exp(-\alpha
    k^{2}\tau)\exp(-ik\xi)$, le terme $\exp(-\alpha k^{2}\tau)$ montrant
    l’amortissement car $\alpha>0$ et par conséquent la dissipation.

[^10]: Le terme dû à l’amortissement Landau linéaire s’exprimerait pour
    des ondes acoustiques ioniques sous la forme
    $\eta\mathcal{P}\left(  \int_{-\infty}^{\infty}\frac{\partial U(\xi^{\prime})}{\partial\xi^{\prime}}\frac{d\xi^{\prime}}{\xi-\xi^{\prime}}\right)  $
    ($\eta>0),$ où $\mathcal{P}$ désigne la valeur principale. Bien que
    ce terme corresponde à une véritable dissipation, son introduction
    dans l’équation de Burger à la place du terme
    $-\alpha\frac{\partial^{2}U}{\partial\xi^{2}}$ ne donne pas lieu à
    des solutions de type onde de choc, car ce terme n’apporte pas un
    amortissement en $k^{2}$ mais en $\left\vert
    k\right\vert .$

[^11]: <span>H. Ikezi, R.J. Taylor and D.R. Baker, Formation and
    interaction of ion-acoustic solitons, *Phys. Rev. Lett*., 25, 11,
    1970.</span>

[^12]: Ondes de compression dans un des plasmas et ondes de raréfaction
    dans l’autre.

[^13]: R.J. Taylor, D.R. Baker and H. Ikezi, Observation of
    collisionless electrostatic shocks, *Phys. Rev. Lett*., 24, 206,
    1970.
