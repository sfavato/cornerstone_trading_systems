# Architecture: Microservices Overview

Our system is designed as an ecosystem of distributed microservices, orchestrated via RabbitMQ and monitored with Prometheus/Grafana. This architecture ensures high availability, horizontal scalability, and fault isolation. For our "Quant" users who interact with our API, understanding this architecture is essential to assess the robustness and reliability of our infrastructure.

## Architecture Diagram (C4 Model - Level 2)

```mermaid
graph TD
    subgraph "Users (API & UI)"
        A[Frontend Interface (React)]
        B[API Clients (Python/JS)]
    end

    subgraph "Cloud Infrastructure (AWS)"
        C[API Gateway (NGINX)]
        D[Message Bus (RabbitMQ)]

        subgraph "CORE Services"
            E[Data Ingestion Service]
            F[Pattern Detection Service (GNN)]
            G[Confidence Scoring Service (XGBoost)]
        end

        subgraph "Support Services"
            H[Historical Data Service]
            I[Trade Monitoring Service]
            J[Notification Service (WebSocket)]
        end

        subgraph "Databases"
            K[Time-Series Database (TimescaleDB)]
            L[Cache (Redis)]
        end
    end

    A --> C
    B --> C
    C --> D

    D -- "New Market Data" --> E
    E --> K

    D -- "New Candlestick" --> F
    F -- "Pattern Detected" --> D

    D -- "Pattern Detected" --> G
    G -- "Pattern Scored" --> D

    D -- "Validated Signal" --> I
    I -- "Trade Alert" --> D

    D -- "Trade Alert" --> J
    J -- "Notification" --> A

    G -- "Need Historical Data" --> H
    H --> K

    G -- "Need Fast Context" --> L
```

## Key Service Descriptions

- **API Gateway:** The single entry point for all requests. Manages authentication (JWT), rate limiting, and routing.
- **Message Bus (RabbitMQ):** The core of our asynchronous architecture. Allows services to communicate in a decoupled manner, ensuring that a load spike or a service failure does not lead to a cascading failure.
- **Pattern Detection Service (GNN):** Our main innovation. Instead of classic `for` loops, we use a Graph Neural Network (GNN) to identify harmonic patterns. This allows us to detect more complex pattern variations and significantly reduce false positives.
- **Confidence Scoring Service (XGBoost):** The service that runs our AI model to calculate the "Confidence Score." It is isolated so it can be updated and retrained independently of other components.
- **Time-Series Database (TimescaleDB):** Chosen for its performance in ingesting and querying large amounts of market data.

## Implications for API Developers

- **Asynchronicity:** Do not expect an immediate synchronous response for complex tasks (e.g., "scan all assets"). You submit a task and receive a `task_id`. You will then need to query a "results" endpoint or subscribe to a webhook.
- **Reliability:** Our architecture is designed for 99.9% availability. The failure of a scoring service, for example, will not stop pattern detection.
- **Scalability:** If latency increases, we can simply increase the number of "workers" for a specific service (e.g., more scoring workers) without disrupting the rest of the system.
