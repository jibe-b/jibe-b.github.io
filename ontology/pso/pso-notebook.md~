---
title: PSO development notebook
...

_tool: soon, the reader will have the possibility to choose which entries to display (carnet, learning, etc)_


## Axiom Annotation

Added one ObjectProperty : sci:AxiomType

Intended to be used to qualify the axiom that defines a class (described class).

Example:

AnnotationAssertion( sci:AxiomType :AxiomABC sci:DefinitionAxiom )

One axiom is used to define a class (e.g. an ElementaryParticle, and this axiom will then be qualified as a DefinitionAxiom.
Other axioms will be QualifyingAxiom, that is to say, axioms that give information on the class
but are not needed to define it.


In general, the DefinitionAxiom :

- is an equivalent class axiom
- contains the superclass definition and adds one information

e.g. EquivalentClass: SuperClass and ( hasPart some one-more-element )


## [PSO] Classification of Objects

Implemented Elementary Particles and Objects that have a known number of components (from hadrons to clusters).

Objects are classified in a tree in which each further level corresponds to a new criteria (for example, a new quantic number)




### Elementary Particles

Elementary Particles are classified corresponding to their qauntic numbers.

Abstract classes are used to identify objects that have the same quantic number.


### Objects with known number of components

Objects for which the number of components is known are classified according to
objects that are part of them.

Abstract objects are used to identify objects that share the same components.




## [graph] Referenced some fundamental hypothesis

(copy of graph-notebook entry)









## Classification discussion

Le premier niveau de classes est fondamental, puisqu'un Objet ne peut être un phénomène, ni une propriété.

Ensuite, toutes les sous-classes correspondent à  une théorie, qui identifie les caractéristiques (propriétés) et classe les entités suivant les caractéristiques observées et les lois  déduites.





## Issue : How to define a PhysicalQuantity linked to an object to a PhysicalQuantity that is universal?

Do we need a universal Quantity class? It would contain time, probably.

But it is possible to say that time is a physical quantity of the universe and consequaently a physical quantity linked to an object before being a universal Physical Quantity.








## [SCI] Model, theory, statement
2015-29-01, Jibé

(copy of SCI-notebook entry)

The relationships between a model, a theory and a statement are defined basically as:

- model and theory are theoretical frames,
- that have specific relationships to statements (hypothesis, observation, prediction)

Statements are instances of the Statement class (that is very general). Described Classes may be written in the future, specifying the Statements (using the relationships that are made).

[Model, theory and statements sketch (vue)](../sci/sketch/model-theory-statement.vue)
[Model, theory and statements sketch (png)](../sci/sketch/model-theory-statement.png)

NB: these two files are sketches (mindmaps).

## Referencing hypothesis and theorems
Jibé, 2015/01/23

Hypothesis are referenced in a hierarchy of classe in order to enable the inheritance of the axioms implying the hypothesis of upper classes. 

Theorems are referenced in order to enable calling such theorems in applications. For example, in a reasoner. 

## One new main class
Jibé, 2015/01/23

- __TheoryElement__ is a class that  can contain anything about theory in the specific case of Physical Sciences. It is intended to be more specific than a generalist ontology describing theoretical elements. Therefore, the translation/mapping between PSO and such an ontology should be written.


## Intention#1: Five main classes
Jibé, 2015/01/15

- __Object__ and __Phenomenon__ correspond of the _description_ of the physical world, requiring a low-level of abstraction. Both take part to a kind of _zoology_ in Physical Sciences.
- __Quantity__ and __Law__ enable an approach with a high level of abstraction. __Quantity__ require instrumentation and __Law__ require theory to be accessible.
- sub-properties of __Property__  caracterise __Object__ (__ObjectProperty__), __Phenomenon__(__PhenomenonProperty__), __Quantity__ (__QuantityProperty__) and __Law__ (__LawProperty__).

##Issue#1: Similarity between __ObjectProperty__ and __PhenomenonProperty__
Jibé, 2015/01/15

Similarity or equivalence?

Differentiation of __ObjectProperty__ and __PhenomenonProperty__ uses the [Singleton Property approach].

# Author's intentions — not technical documentation
Jibé, 2015/01/15

Intentions: what brought me to write the ontology this way. This is not technicajl documenation but what is not made explicit while writing the ontology.

Issues: problems I identify. Their resolution is intended to be part of the intention part.

# [learning] OWL is based on Description Logic
Jibé, 2015/01/15

Descrition Logic (and thus the OWL language) consists of teminology (TBox) and relations between concepts defined in the terminology (ABox).

# [carnet] Development order
Jibé, 15/01/2015

Order of priority:

- classes and properties definition, enable what comes next
- domain and range definition, correspond to primary specification of properties
- mathematical properties
- combinatoire (fr)

# [carnet] Exprimer les hypothèses et affirmations : réification _vs_ Singleton Property
Jibé, 11/01/2015, modified:2015/01/15

Pour exprimer des hypothèses, il est possible d'écrire :

> ex:Affirmation123 ex:sousHypothèse ex:Hypothèse123
> ex:ex:Hypothèse123 a rdf:statement
> ex:Hypothèse123 rdf:subject ex:Atom
> ex:Hypothèse123 rdf:predicate ex:inPotential
> ex:Hypothèse123 rdf:object ex:CentralPotential

source: [http://www.w3.org/TR/2014/REC-rdf11-mt-20140225/#reification](http://www.w3.org/TR/2014/REC-rdf11-mt-20140225/#reification)

Cela permet de mettre à disposition l'information qu'un tel triplet peut exister mais ne créée pas ce triplet.

Il est nécessaire de passer par la représentation [RDF*](http://arxiv.org/abs/1406.3399) (en particulier turtle* ) pour employer directement un triplet comme sujet ou objet d'un triplet (NB: RDF* n'est pas une spécification du W3C)

Une autre approche est celle des Singleton Properties : définir des propriétés correspondant aux précisions données sur une propriété.

> ex:Atom ex:supposedInPotential ex:CentralPotential

source: [http://mor.nlm.nih.gov/pubs/pdf/2014-www-vn.pdf](http://mor.nlm.nih.gov/pubs/pdf/2014-www-vn.pdf)

Un problème avec les Singleton Properties est qu'elles obligent un programme travaillant sur un graph à connaitre les _la totalité_ det détails pour chaque propriété. Donc chaque cas particulier doit être écrit comme une Singleton Property et le programme doit intégrer chacune des spécificités de cette Singleton Property.

L'approche Singleton Property peut être négligée au profit de la logique descriptive (DL), sur laquelle est basée OWL : TBox pour définir les termes et ABox pour définir des relations générales, en particulier sur des cas particuliers des propriétés (approche de Singleton Property limitée à quelques sous-propriétés).

En cours d'évaluation des intérêts des deux approches.


# Cahier des charges
Jibé, 07/01/2015

## Documentation

- indication des sources
- documentation technique : citation littérale des sources et ajout de documentation originale
- indication des intentions (réflexions au cours du développement)

## Carnet de recherche

- plans :
	+ Roadmap et mises à jour
	+ publication des détails des versions successives
- concepts theéoriques (apprentissage au cours du développement, applications)
- actions réalisées :
	+ objectif
	+ détail des réalisations
	+ bilan

## Stockage en Linked Data

Ce carnet de recherche devra à moyen terme contenir des indications sémantiques.
