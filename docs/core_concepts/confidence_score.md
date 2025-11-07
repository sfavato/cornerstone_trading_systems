## The Confidence Score (1-10)

The Confidence Score is the final, aggregated grade (from 1 to 10) that the system assigns to a pattern *after* it has been detected. It answers one question: **"What is the probability of this pattern succeeding right now, in the current market conditions?"**

*   **Score 1-3:** Very low quality. Ignored.
*   **Score 4-6:** Average quality. Ignored.
*   **Score 7-10:** High quality, validated "Trade Signal." Passed to the execution engine.

### How it Impacts the Trade

The Confidence Score is the primary filter for the entire system. In the `monitor_trades` service, there is a hard filter called the `confidence_score_filter`. We configure a minimum threshold (e.g., `7`). Any pattern that does not meet this minimum score is automatically rejected and will never be traded.

## The Data Pipeline: From Raw Data to Actionable Signal

```mermaid
graph TD
    A[Raw Market Data] --> B{Data Ingestion (FastAPI)};
    B --> C[Time-Series DB (TimescaleDB)];
    C --> D{Pattern Detection Engine};
    D --> E[Detected Pattern (Noise)];
    E --> F{Scoring & Validation Engine};
    F --> G[Validated Signal (Actionable)];

    subgraph "Pro & Quant Confluence Factors"
        H[✅ Market Structure] --> F;
        I[✅ Order Flow] --> F;
        J[✅ Derivatives Pressure] --> F;
        K[✅ On-Chain Metrics] --> F;
    end

    G --> L[High Confidence Score (>=7)];
    G --> M[Low Confidence Score (<7)];

    L --> N[➡️ Actionable Alert];
    M --> O[➡️ Discarded];
```

## Scoring Components: How the Score is Calculated

The final 1-10 score is not just one number. It is an aggregation of several independent scores, each analyzing a different aspect of the trade. The final score is built like this:

`Final Score (1-10) = (Base Score from Geometric Purity) + (Market Confluence Bonus) + (AI Context Bonus/Penalty)`

### 1. Geometric Purity Score (The Base Score)

This is the first and most fundamental score, calculated by the `harmofinder/scoring_engine.py`.

*   **What it is:** A score of the pattern's *technical perfection*.
*   **How it's calculated:** It measures how closely the pattern's Fibonacci ratios (the X, A, B, C, and D points) match the "textbook perfect" definition of that pattern. For example, a perfect Gartley pattern has its B-point at exactly the 0.618 retracement of the XA leg. A pattern with a B-point at 0.617 will receive a much higher purity score than one at 0.590.
*   **Impact:** This forms the base of the final score. A "sloppy" or geometrically "ugly" pattern will start with a low base score and is highly unlikely to ever become a Trade Signal.

### 2. Market Confluence Score (The "Where")

This score answers *where* on the chart the pattern is completing. A pattern that completes at a major support/resistance level is far more reliable.

*   **What it is:** A score measuring the pattern's alignment with high-volume structural levels.
*   **How it's calculated:** The system's `scoring_engine.py` (specifically the `calculate_volume_profile_score` function) checks the pattern's entry price (the D-point) against the **Volume Profile** of the asset.
*   **Impact (Bonus System):**
    *   **High Bonus:** Awarded if the D-point lands directly on the **Point of Control (POC)** (the highest-volume price level).
    *   **Medium Bonus:** Awarded if the D-point lands on the **Value Area High (VAH)** or **Value Area Low (VAL)**.
    *   **No Bonus:** Awarded if the pattern completes in a low-volume "dead zone."

### 3. AI Context Score (The "When" / Exotic Alpha)

This is our proprietary "secret sauce" and a key part of the "deep research" from the `masterplan.txt`. This score answers, "is *now* a good time for this pattern to succeed?"

*   **What it is:** A predictive score from an AI model (XGBoost) trained on our historical trade data (`trade_journal`).
*   **How it's trained:** The `backtesting/train_model.py` script trained the model by analyzing thousands of past trades. It learned what "invisible" market conditions were present during winning trades versus losing trades.
*   **How it's calculated (Live):** The `update_indices/update_confidence_score.py` script runs periodically. It feeds the *live* market context into the AI model, which generates a score. This score is then fed into the final Confidence Score calculation.
*   **Data Used (Exotic Alpha):**
    *   **Derivatives Data:** Funding Rates, Open Interest, CVD, and Liquidation data.
    *   **On-Chain Data:** Exchange Netflows, MVRV (Market Value to Realized Value), and Whale Accumulation.
    *   **Options Data:** Put/Call Ratio.
*   **Impact:** This score acts as a powerful bonus or penalty. A geometrically perfect (Purity) pattern at a key level (Confluence) might *still* be rejected if the AI model detects that, for example, high funding rates and exchange inflows are strongly opposing the trade.
