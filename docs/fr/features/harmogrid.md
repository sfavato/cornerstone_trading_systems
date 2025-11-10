# HarmoGrid : La Stratégie d'Entrée Supérieure

HarmoGrid est une stratégie d'entrée sophistiquée conçue pour optimiser votre exécution sur les patterns harmoniques. Plutôt que de dépendre d'un seul point d'entrée, HarmoGrid construit intelligemment votre position à travers une grille d'ordres limites, vous offrant un contrôle et une précision accrus.

## La Proposition de Valeur : Pourquoi HarmoGrid ?

Dans un marché volatile, entrer au prix exact peut être un défi. Un trade peut frôler votre point d'entrée sans jamais le toucher, vous laissant sur la touche. HarmoGrid est la solution.

- **Prix d'Entrée Moyen Optimisé** : En répartissant les entrées, HarmoGrid vise à obtenir un coût moyen de position plus favorable (DCA - Dollar Cost Averaging).
- **Réduction du Risque de "Trade Manqué"** : La grille couvre une zone d'entrée stratégique, augmentant significativement vos chances de participer au mouvement attendu.
- **Approche Systématique** : Retirez l'émotion de l'équation. HarmoGrid exécute un plan d'entrée prédéfini avec une discipline algorithmique.

Ce n'est pas un bot de grille traditionnel. C'est un mécanisme d'entrée chirurgical, conçu pour la précision des patterns harmoniques.

## Le Mécanisme "HarmoGrid"

Lorsque HarmoFinder identifie une opportunité de trade compatible avec HarmoGrid, il ne place pas un, mais **quatre ordres limites pondérés** stratégiquement au sein de la zone de retournement potentielle (PRZ).

La répartition est la suivante :

- **P_Start (10% de la position)** : Le premier point d'entrée, pour "tâter" le marché.
- **P_True1 (20% de la position)** : Placé à un niveau de confluence plus élevé.
- **P_True2 (30% de la position)** : Au cœur de la zone de retournement.
- **End_SLG (40% de la position)** : Le dernier rempart, offrant le meilleur prix potentiel avant l'invalidation du pattern.

### Le Statut `GRID_PENDING`

Tant que ces quatre ordres sont en attente et qu'aucun n'a été exécuté, le statut de votre trade sera `GRID_PENDING`. Cela vous indique que le système surveille activement le marché, prêt à construire votre position.

Dès que le premier ordre de la grille est touché, le statut du trade change immédiatement pour `in-trade`. Votre position est désormais considérée comme active.

## La Logique d'Annulation : Une Protection Intelligente

C'est le point le plus important à comprendre, et c'est une fonctionnalité, pas un bug.

**Si le trade atteint son premier objectif de profit (TP1), le système annulera automatiquement tous les ordres d'entrée restants dans la grille.**

**Pourquoi ?** C'est une mesure de gestion du risque conçue pour vous protéger. Si le marché a déjà validé la direction du trade et que celui-ci est gagnant, il est stratégiquement imprudent de continuer à acheter (DCA) à des niveaux de prix moins optimaux.

L'annulation des ordres restants permet de :

- **Verrouiller les Gains** : Le trade se concentre désormais sur la sortie, pas sur l'entrée.
- **Éviter le Sur-Risque** : Empêche d'augmenter la taille de la position sur un trade déjà en cours de dénouement.

Faites confiance au processus. Cette logique est conçue pour optimiser votre performance et protéger votre capital, reflétant la philosophie de "Confiance Quantifiée" de HarmoFinder.
