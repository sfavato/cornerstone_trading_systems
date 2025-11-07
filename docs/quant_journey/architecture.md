# Architecture : Vue d'Ensemble des Microservices

Notre système est conçu comme un écosystème de microservices distribués, orchestrés via RabbitMQ et monitorés avec Prometheus/Grafana. Cette architecture garantit une haute disponibilité, une scalabilité horizontale et une isolation des pannes. Pour nos utilisateurs "Quant" qui interagissent avec notre API, comprendre cette architecture est essentiel pour évaluer la robustesse et la fiabilité de notre infrastructure.

## Diagramme d'Architecture (C4 Model - Niveau 2)

```mermaid
graph TD
    subgraph "Utilisateurs (API & UI)"
        A[Interface Frontend (React)]
        B[Clients API (Python/JS)]
    end

    subgraph "Infrastructure Cloud (AWS)"
        C[Gateway API (NGINX)]
        D[Bus de Messages (RabbitMQ)]

        subgraph "Services CORE"
            E[Service d'Ingestion de Données]
            F[Service de Détection de Patterns (GNN)]
            G[Service de Scoring de Confiance (XGBoost)]
        end

        subgraph "Services de Support"
            H[Service de Données Historiques]
            I[Service de Monitoring de Trades]
            J[Service de Notifications (WebSocket)]
        end

        subgraph "Bases de Données"
            K[Base de Données Time-Series (TimescaleDB)]
            L[Cache (Redis)]
        end
    end

    A --> C
    B --> C
    C --> D

    D -- "Nouvelles Données du Marché" --> E
    E --> K

    D -- "Nouveau Candlestick" --> F
    F -- "Pattern Détecté" --> D

    D -- "Pattern Détecté" --> G
    G -- "Pattern Scoré" --> D

    D -- "Signal Validé" --> I
    I -- "Alerte de Trade" --> D

    D -- "Alerte de Trade" --> J
    J -- "Notification" --> A

    G -- "Besoin de Données Historiques" --> H
    H --> K

    G -- "Besoin de Contexte Rapide" --> L
```

## Description des Services Clés

- **Gateway API :** Le point d'entrée unique pour toutes les requêtes. Gère l'authentification (JWT), la limitation de débit (rate limiting) et le routage.
- **Bus de Messages (RabbitMQ) :** Le cœur de notre architecture asynchrone. Permet aux services de communiquer de manière découplée, assurant qu'un pic de charge ou la panne d'un service n'entraîne pas une défaillance en cascade.
- **Service de Détection de Patterns (GNN) :** Notre innovation principale. Au lieu de boucles `for` classiques, nous utilisons un Graph Neural Network (GNN) pour identifier les patterns harmoniques. Cela nous permet de détecter des variations de patterns plus complexes et de réduire considérablement les faux positifs.
- **Service de Scoring de Confiance (XGBoost) :** Le service qui exécute notre modèle IA pour calculer le "Confidence Score". Il est isolé pour pouvoir être mis à jour et ré-entraîné indépendamment des autres composants.
- **Base de Données Time-Series (TimescaleDB) :** Choisie pour sa performance dans l'ingestion et l'interrogation de grandes quantités de données de marché.

## Implications pour les Développeurs API

- **Asynchronisme :** Ne vous attendez pas à une réponse synchrone immédiate pour les tâches complexes (ex: "scanner tous les actifs"). Vous soumettez une tâche et recevez un `task_id`. Vous devrez ensuite interroger un endpoint de "résultats" ou vous abonner à un webhook.
- **Fiabilité :** Notre architecture est conçue pour une disponibilité de 99.9%. La défaillance d'un service de scoring, par exemple, n'arrêtera pas la détection de patterns.
- **Scalabilité :** Si la latence augmente, nous pouvons simplement augmenter le nombre de "workers" pour un service spécifique (ex: plus de workers de scoring) sans perturber le reste du système.
