# Guide de Démarrage Rapide : Votre Interface Frontend

Bienvenue sur votre portail de trading. Le site [**https://cornerstone-indice.com**](https://cornerstone-indice.com) est la **représentation visuelle et en temps réel** des signaux de trading générés par notre architecture de microservices. Il ne s'agit pas d'un site de simulation, mais d'une interface directe qui lit en continu l'état de notre base de données pour vous informer des opportunités détectées et des positions gérées par notre système.

Cette interface est conçue pour être votre copilote, vous offrant une transparence totale sur les opérations de notre moteur Alpha.

## Les Trois Sections Clés de Votre Interface

Votre interface est organisée en trois sections principales, chacune ayant un rôle précis pour vous aider à interpréter l'activité du système.

### 1. Le Dashboard : Votre Vue d'Ensemble

- **Objectif :** Fournir une synthèse immédiate de l'état du marché et des performances globales du système.
- **Ce que vous y trouverez :**
    - Les derniers signaux validés.
    - Un résumé des performances clés (KPIs).
    - L'état actuel du marché (par exemple, le régime de volatilité).
- **Comment l'utiliser :** C'est votre point de départ quotidien pour prendre le pouls du marché et de notre Alpha en un coup d'œil.

### 2. La Vue "Signals" : Le Cœur Opérationnel

- **Objectif :** Afficher en détail les opportunités de trading détectées et leur statut actuel.
- **Ce que vous y trouverez :**
    - **`Nearest Trades` :** Les patterns harmoniques qui ont été validés par notre **Score de Confiance** mais qui attendent encore d'atteindre leur prix d'entrée pour devenir actifs.
    - **`Active Trades` :** Les positions qui ont été exécutées et qui sont actuellement gérées par notre service `monitor_trades`.
- **Comment l'utiliser :** C'est ici que vous suivez l'évolution des opportunités, de la détection à l'exécution.

### 3. La Vue "Performance" : La Preuve par les Chiffres

- **Objectif :** Offrir une analyse détaillée et transparente de l'historique des performances du système.
- **Ce que vous y trouverez :**
    - Des métriques de performance standard (Profitabilité, Drawdown, Facteur de Profit).
    - L'analyse des trades par R-Multiple (Risk-to-Reward), notre métrique centrale pour évaluer la qualité de la prise de risque.
- **Comment l'utiliser :** Utilisez cette section pour auditer nos résultats et comprendre le profil de risque et de rendement de notre stratégie.
