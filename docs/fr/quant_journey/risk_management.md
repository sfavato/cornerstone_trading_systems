# Gestion du Risque : Une Approche à Double Niveau

Une stratégie de trading n'est rien sans une gestion du risque rigoureuse. Notre système, via le microservice `monitor_trades`, applique une approche de Stop-Loss (SL) à deux niveaux pour protéger le capital tout en s'adaptant aux conditions de marché. Cette distinction entre un SL initial et un SL dynamique est au cœur de notre logique de préservation du capital.

## 1. SL Géométrique / Statique : Le Garde-Fou Initial

Le premier niveau de protection est le **Stop-Loss Géométrique**. Il est "statique" car il est défini au moment de l'entrée en position et est basé purement sur la **structure géométrique du pattern harmonique**.

-   **Définition :** Ce SL est calculé par le module `shared_models/SLTP.py`. Il est généralement placé juste au-delà du point structurel qui invaliderait le pattern (par exemple, au-delà du point X pour la plupart des patterns).
-   **Rôle :** C'est le **garde-fou absolu**. Il représente le niveau de prix où la logique technique derrière le trade est fondamentalement invalidée. Si ce niveau est atteint, le trade est coupé sans exception, car l'hypothèse de départ n'est plus valide.
-   **Caractéristique :** Il est prédéfini et ne change pas, offrant ainsi une transparence totale sur le risque maximal initial (`1R`) de chaque trade.

## 2. SL Dynamique / d'Invalidation : L'Ajustement en Temps Réel

Le deuxième niveau est le **Stop-Loss Dynamique**. C'est une logique plus sophistiquée, appliquée en temps réel par le module `monitor_trades/enforce_stoploss_rules.py`. Son objectif est de détecter si le "comportement" du prix invalide le trade, **même si le SL Géométrique n'a pas encore été touché**.

-   **Définition :** Ce SL n'est pas un niveau de prix fixe, mais une **règle de comportement**. Il peut être déclenché par diverses conditions qui indiquent que le scénario attendu ne se matérialise pas.
-   **Exemples de règles d'invalidation :**
    -   **Clôture de Mèche (Candle Close) :** Une des règles les plus courantes. Le trade peut être annulé si une bougie (par exemple, sur l'unité de temps du trade) **clôture** au-delà d'un certain seuil de risque, même si la mèche n'a pas touché le SL Géométrique. Cela permet de sortir d'un trade qui montre une forte pression contraire.
    -   **Invalidation par Volatilité (Volatility Stop) :** Le système peut utiliser un indicateur de volatilité comme le "Chandelier Exit" ou un multiple de l'ATR (Average True Range) pour suivre le prix. Si le prix franchit ce seuil mobile, le trade est coupé pour s'adapter à une augmentation inattendue de la volatilité.
    -   **Invalidation Temporelle (Time Stop) :** Si un trade stagne pendant une période prolongée sans se diriger vers l'objectif, il peut être fermé pour libérer le capital.

En combinant un SL Géométrique pour le risque structurel et un SL Dynamique pour le risque de comportement, notre système vise à optimiser la gestion du risque : couper les pertes de manière décisive lorsque le trade est invalidé, mais aussi s'adapter intelligemment lorsque le marché montre des signes avant-coureurs de danger.
