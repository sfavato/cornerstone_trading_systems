# Comprendre la Vue "Signals" : De la Détection à l'Exécution

La vue "Signals" est le centre névralgique de votre interface. Elle vous permet de suivre en temps réel le cycle de vie d'une opportunité de trading, depuis sa validation par notre moteur Alpha jusqu'à sa gestion active. Pour interpréter correctement les informations, il est crucial de comprendre la distinction entre les deux états d'un signal.

## 1. `Nearest Trades` : Les Opportunités en Attente

Un signal affiché dans la section **`Nearest Trades`** n'est pas encore une position active. Il s'agit d'un pattern harmonique qui a satisfait à nos critères de validation les plus stricts, c'est-à-dire qu'il a obtenu un **Score de Confiance** élevé.

- **Statut :** C'est un "trade potentiel" validé.
- **Condition pour l'activation :** Le marché doit encore atteindre le **Prix d'Entrée** (le point D du pattern) pour que le trade soit déclenché par le service `monitor_trades`.
- **Action de l'utilisateur :** C'est une phase de surveillance. Vous pouvez analyser le pattern, préparer votre propre analyse ou simplement attendre l'exécution par le système.

### L'Indicateur "Proximity Info" : Votre Radar de Proximité

L'un des indicateurs les plus importants de la vue `Nearest Trades` est le **"Proximity Info"**.

- **Rôle :** Il mesure en temps réel la **distance (en pourcentage) entre le prix actuel du marché et le prix d'entrée cible (le point D)**.
- **Exemple :** Une valeur de `-0.5%` signifie que le prix actuel est à seulement 0.5% en dessous du niveau d'entrée requis pour un ordre d'achat.
- **Utilité :** Cet indicateur vous permet de savoir en un coup d'œil si un trade potentiel est sur le point d'être déclenché, vous aidant ainsi à anticiper l'action du marché.

## 2. `Active Trades` : Les Positions en Cours

Lorsqu'un signal passe de `Nearest Trades` à **`Active Trades`**, cela signifie que les conditions de marché ont été remplies et que la position a été exécutée.

- **Statut :** C'est une position de trading "live".
- **Gestion :** Le trade est désormais sous le contrôle actif du microservice `monitor_trades`, qui applique les règles de Stop-Loss et de Take-Profit définies par le système.
- **Action de l'utilisateur :** C'est une phase de suivi. Vous pouvez observer la performance de la position en temps réel et analyser comment le système gère le risque.

En résumé, la vue "Signals" vous donne une fenêtre transparente sur notre chaîne de décision : les `Nearest Trades` vous montrent ce que notre Alpha a validé, et les `Active Trades` vous montrent ce que notre gestionnaire de risque exécute.
