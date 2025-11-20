# Smart Reversal Override (Priorité au Retournement Intelligent)

## Introduction

Le "Smart Reversal Override" (Priorité au Retournement Intelligent) est un protocole critique introduit dans notre mise à jour de novembre 2025. Il représente une avancée majeure dans notre logique de validation, allant au-delà du simple suivi de tendance pour permettre une exécution contre-tendance intelligente.

## Le Problème : Tendance vs Opportunité

Les bots de trading traditionnels échouent souvent de deux manières :

1.  **Combattre la Tendance :** Acheter chaque baisse lors d'un crash (attraper des couteaux qui tombent).
2.  **Manquer le Creux :** Refuser d'acheter des retournements valides parce que la "tendance est encore baissière".

## La Solution : La Divergence comme Vérité

Le mécanisme Smart Reversal résout ce problème en priorisant la **Divergence** sur la direction simple de la tendance.

### Comment Ça Marche

Lorsque le Détecteur Cornerstone identifie un pattern harmonique haussier (par exemple, un Gartley Bullish) dans un environnement de marché baissier, il ne le rejette pas automatiquement. Au lieu de cela, il recherche un signal de "Smart Reversal" :

1.  **Action des Prix :** Plus Bas (Baissier).
2.  **Oscillateur/Momentum :** Plus Haut (Haussier).

Cette divergence indique que bien que les vendeurs poussent le prix vers le bas, le *momentum* de la pression de vente s'épuise.

### La Logique de "Priorité" (Override)

Normalement, notre système filtre les signaux d'achat si le marché global (Tendance BTC) est baissier. Cependant, si une **Divergence de Classe A** forte est détectée aux côtés d'un pattern harmonique à haute confiance, le protocole Smart Reversal **surpasse** (override) le filtre de tendance.

*   **Résultat :** Le système exécute le trade, achetant le "dip" avec une haute précision juste au moment où la tendance est sur le point de se retourner.
*   **Bénéfice :** Cela permet à Cornerstone Indice de capturer des trades à fort multiple R au tout début d'une nouvelle tendance, plutôt que d'attendre une confirmation lorsque le prix est déjà 10 à 20 % plus haut.

Cette fonctionnalité démontre notre engagement envers la sophistication : nous ne suivons pas juste des lignes ; nous mesurons l'énergie sous-jacente du marché.
