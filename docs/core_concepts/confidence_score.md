# The "Confidence Score" (0-100)

The "Confidence Score" is the final, aggregated rating (from 0 to 100) that the system assigns to a pattern after its detection. It answers one question: **"What is the probability of this pattern succeeding right now, in the current market conditions?"**

- **Score 0-40:** Very low quality. Ignored.
- **Score 41-69:** Average quality. Potential for manual analysis but generally ignored by the bot.
- **Score 70-100:** High quality, validated "Trade Signal." Sent to the execution engine.

The 70 threshold is our default benchmark, but "Pro" and "Quant" users can adjust this filter via the API.

## Score Components: How It's Calculated

The final 0-100 score is an aggregation of several independent scores.
`Final Score (0-100) = (Geometric Purity Score) + (Market Confluence Bonus) + (AI Context Bonus/Penalty)`

### 1. Geometric Purity Score (The Base)

- **Description:** A score of the pattern's technical perfection.
- **Calculation:** Measures the proximity of the Fibonacci ratios (X, A, B, C, D points) to the "perfect" definition of the pattern. A Gartley with a B point at 0.617 will have a much higher purity score than one at 0.590.
- **Impact:** Forms the basis of the score. A "sloppy" pattern starts with a low base and is unlikely to become a Trade Signal.

### 2. Market Confluence Score (The "Where")

- **Description:** Analyzes where on the chart the pattern completes. A pattern forming at a major structure level is more reliable.
- **Components:**
    - **Volume Profile Alignment:** Checks the entry price (D point) against the Volume Profile. A bonus is given if the D point lands on the Point of Control (POC), Value Area High (VAH), or Value Area Low (VAL).
    - **RSI Divergence:** Checks for the presence of a classic or hidden RSI divergence on the pattern's timeframe, indicating a weakening of the opposing momentum.
    - **VWAP Location:** Compares the entry price to the VWAP (Volume-Weighted Average Price). A bullish pattern forming above the VWAP is considered stronger.
    - **HTF Trend:** Analyzes if the pattern aligns with the trend of the Higher-Timeframe for better filtering.

### 3. AI Context Score (The "When" / Exotic Alpha)

- **Description:** Our "secret sauce." A predictive score from an AI model (XGBoost) trained on our historical data to answer the question: "Is now a good time for this pattern to succeed?"
- **Data Analyzed:**
    - **Derivatives Data:** Funding Rates, Open Interest, CVD, and Liquidation Data.
    - **On-Chain Data:** Exchange Netflows, MVRV (Market Value to Realized Value).
    - **Options Data:** Put/Call Ratio.
- **Impact:** Acts as a powerful bonus or penalty. A perfect pattern (Purity) at a key level (Confluence) can still be rejected if the AI detects that market conditions (e.g., excessively high funding) are strongly opposing the trade.
