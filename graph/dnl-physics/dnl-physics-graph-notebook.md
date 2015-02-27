---
title: DNL graph Notebook
author: Jibé
...

# Initialisation of graph

## Sources
2015-01-22

The file cours1_et_latex.tex has been converted to narkdown syntax with the bash command 

> jibe@jibe-HP-ProBook-4530s:~/dynamique-non-lineaire$ pandoc cours1_et_latex.tex  -o cours1_et_mardown.md

## Workflow

Annotation of the already written content using the semantic markdown syntax, therefore embedding turtle triples in the text.

As the pandoc extension for parsing Smd syntax to html+RDFa has not yet been implemented, the triples are extracted manually and stored into a turtle file.

En parallel, triples edited using IsaViz (visual editing) and are embedded inside the source (in markdown).

## Recensement

### First step: recensement (French) of all equations written in the document

Hence:

> ex:equation rdf:type sci:Equation .

and:

adding Equation class to sci (ontology)


## Workflow

1. recensement d'individus à partir d'une ressource (ici : cours de dynamique non-linéaire de Catherine Krafft)
2. recencement de ces individus dans la page resource.md
3. ajout de liens entre les individus
	3.1 à partir des propriétés définies dans des ontologies
	3.2 ou en créant des propriétés ad hoc
4. enrichissement des ontologies avec les classes et propriétés définies


## Définition de la propriété lien

Cette propriété (inclue dans chaque ontologie) permet d'avoir un lien non-défini entre deux individus (et de garder une certaine proximité dans l'affichage des graphs)


## Needs
2015-01-23, Jibé

Besoin de recenser toutes les grandeurs physiques.

Recensement dans bloc.csv

## Lois et théorèmes

Si une loi physique est considérée universelle par la théorie, alors elle est inscrite dans pso. L'expression de cette loi se fait aussi dans pso, mais si l'expression n'apparait pas, alors il faut aller chercher dans le graphe associé.

Les lois intègrent dans leur expression les 

Les hypothèses de physique sont à décrire. La hiérarchie des classes fait qu'une hypothèse 

D'où les classes
Hypothèse de modèle –> hypothèses fondamentales, par exemple 
Hypothèse de modèle de la mécanique classique:
la vitesse du système est négligeable devant la vitesse de la lumière.

Les hypothèses de mécanique classique sont des sous hypothèses de celle-ci donc elles héritent des propriétés.

Mais comment fait-on hériter de propriétés quand on est en mode réification ?

Il faudra probablement passer par un système d'addition des hypothèses.

thmABC123
	a thm ;
	dansModèle MécaniqueClassiqueTheory ;
	hypothèse 	HypABC123 .
	
alors ce théorème a pour hypothèse HypABC123 et en plus, il a les hypothèses du modèle de mécanique classique. Mais ceci est à implémenter dans le résonneur parce qu'il n'y a pas d'héritage au sens de OWL.


alors que si on écrit :
thmABC123
	a thmInTheoryMécaniqueClassique ;
	hypothèse 	HypABC123 .

alors il hérite des axiomes qui font intervenir thmInTheoryMécaniqueClassique,
qui sont probablement qu'un tel théorème a des hypothèses.


donc il faudrait créer une classe de théorèmes inclus dans un modèle.

Donc :

créer un modèle

CLASS
Theory
Model

rmq: un modèle est expérimental sans avoir de théorie sous-jacente

INDIVIDUALS
ClassicalMechanics
QuantumMechanics

et relier ces individus à une hypothèse

hypothèse de mécanique classique
hypothèse de mécanique quantique (ne dit rien sur le caractère relativiste)
hypothèse de mécanique relativiste

et à partir de l'association de ces hypothèses, on obtient les différents modèles de physique.

Donc : 
1. créer classe pso:Theory, pso:Model et sci:Hypothesis avec

pso:TheoryElement
	pso:Theory
	pso:Model
	pso:Hypothesis
	
sci:Proposition
	sci:Hypothesis
	sci:Theorem
	
	
et les propriétés

sci:hasHypothesis
pso:inTheory qui correspond à de la description vague (pour permettre une lecture des axiomes qui ressemblent à la classification normale : soit on écrit: théorème appartient à tel modèle soit on écrit: théorème a telles hypothèses et le résonner doit trouver le même résultat (si c'est bien décrit))

mais pourquoi créer deux classes d'hypothèses, une au sens de sci et une au sens de pso.

pso et sci sont forcément à appeler ensemble. Sci traite de ce qui est de l'ordre du raisonnement et des 
et tous les outils qui peuvent être présents dans sci n'ont pas besoin d'être présents dans pso.

Mais l'hypothèse au sens de PSO sert puisqu'elle permet de créér des individus, qui sont les hypothèses usuelles.

au sens de SCI, les hypothèses sont des objets plus génériques.

## Issue #10: redondance dans la définition de sciHypothesis et PSO:Hypothesis

pso:Hypothesis permet de créer des individus

tels que les hypothèses usuelles en physique :

hypothèse relativiste, hypothèse classique…

donc elle est indispensable.

sci:Hypothesis pourrait (noter la nuance) servir à décrire les connaissances d'un point de vue de l'analyse des théories scientifiques.

On pourrait redéfinir pso:Hypothesis en pso:PhysicalHypothesis, dans le sens ou cette hypothèses serait une hypothèse qui permet de construire un modèle sur une approximation.

sci:Hypothesis pourrait alors être une hypothèse qui permet de faire avancer un raisonnement. sci:Hypothesis serait donc plus générale que pso:Hypothesis, qui elle, se limite à s'appliquer aux approximations faites pour constuire un domaine.

Cette idée finale est acceptée et est décrite dans les commentaires de sci:Hypothesis et pso:Hypothesis




## Singleton Properties and singleton-like calsses

Pour décrire toutes les théories possibles en physique,

il faut tout d'abourd les hypothèses usuelles. Une théorie possède des hypothèses. et toutes les sous-théorier héritent de ces axiomes, c'est-à-dire de toutes ces hypothèses.

Définir une classe théorieABC avec une seule hypothèse permet de créer un individu pour la théorie qui a seulement cette hypothèse.

Un individu qui aurait uniquement des hypothèses d'une ligne de 

Les classes sont donc des classes pour des théories ayant cette propriété. Une théorie complexe est donc instance de plusieurs classes pour hériter des hypothèses correspondantes.

Si on définit un individu avec pour axiomes les hypothèses qu'il a, alors le reasoner définira la classe à laquelle il appartient.

# Documentation: Entry#2

## Theories, models

The first aim is to enable the inheritance of the axioms of the super classes.

So each further level in Theory and Hypothesis classes is the addition of a property to the ones of the upper levels.

Theories and Hypothesis are instanciated as Individuals of various classes. Consequently, they inherit of the axioms of the upper classes.

Names of these hypothesis and levels of theories are not necesarily obvious. Therefore, their names will reflect the hypothesis that they correspond to, in the order of hierarchy (upper classes hypothesis first).


## Why referencing?

Propositions (pieces of knowledge such as theorems) are referenced in order to be callable. That is to say, what is linked to them (expression, python code) should be easily foundable, so that it can be used for computing, for example.

Hypothesis are referenced in order to enable inheritance (write once, use multiple times).




















mais pas en mode Singleton parce qu'il faut alors définir une classe par modèle

CLASS
modèle
modèle classique-relativiste
modèle classique-nonrelativiste
modèle quantique-relativiste
modèle quantique-nonrelativiste
modèle relativiste




























































