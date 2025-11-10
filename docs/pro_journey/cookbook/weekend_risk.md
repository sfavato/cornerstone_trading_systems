# Understanding the Weekend Risk Protocol (WRS)

The cryptocurrency market never sleeps, but its nature changes dramatically over the weekend. This page explains how HarmoFinder proactively manages the risks associated with these dynamic shifts.

## For the Pro Trader: Your Insurance Against "Flash Crashes"

**The Key Message:** "The crypto market changes on weekends. Institutional liquidity disappears, making the market fragile and prone to 'flash crashes.' Our bot knows this. The 'Intelligent Circuit Breaker' is your insurance: it reduces exposure or secures capital before these violent drops occur."

The "Intelligent Circuit Breaker" is a safety protocol designed to protect you. Based on our "Weekend Risk Score" (WRS), it activates defensive measures when the risk of a sudden, violent downturn increases.

There are two levels of intervention:

*   **Level 1: Filter (High Risk)**
    *   **What you see:** A "New LONG trades disabled" message appears on your dashboard.
    *   **Why it's smart:** The system anticipates a possible cascade of liquidations. By suspending new purchases, it avoids entering the market at a moment of maximum vulnerability, protecting you from buying just before a crash.
*   **Level 2: Circuit Breaker (Extreme Risk)**
    *   **What you see:** A notification informs you that your LONG positions have been closed.
    *   **Why it's necessary:** At this level, the system believes a "flash crash" is imminent. The absolute priority is capital preservation. Actively closing your positions is a last-resort measure to secure your gains and limit losses before the market drops violently.

## For the Quant Analyst: The "Weekend Risk Score" (WRS) Methodology

**The Key Message:** "We have quantified the 'Weekend Effect.' The system calculates a 'Weekend Risk Score' (WRS) based on leverage predictors (ELR, OI Divergence, Funding Rates) and magnitude multipliers (Volatility Squeeze, CME Gap). This page explains the logic behind the system's filtering or closing actions."

The WRS is a proprietary metric designed to assess systemic risk specific to weekends. It is calculated on Friday evening and aggregates several key indicators to anticipate market fragility.

### The Components of the WRS:

1.  **Leverage Predictors:**
    *   **Estimated Leverage Ratio (ELR):** A high ratio indicates an over-leveraged market, vulnerable to a cascade of liquidations.
    *   **Open Interest (OI) vs. Price Divergence:** A divergence where OI increases while the price stagnates or falls signals an accumulation of positions that could be liquidated en masse.
    *   **Funding Rates:** Excessively high or negative rates can indicate tension in the leverage market.
2.  **Magnitude Multipliers:**
    *   **Volatility Squeeze:** A period of extremely low volatility (as measured by the width of Bollinger Bands, for example) often precedes a violent expansion.
    *   **CME Gap:** The presence of an unfilled "gap" on CME Bitcoin futures can act as a magnet on the price, increasing the risk of sharp movements when traditional markets reopen.

The WRS combines these factors to generate a risk score. When this score exceeds predefined thresholds, the "Intelligent Circuit Breaker" activates the filtering (Level 1) or active closing (Level 2) protocols to manage exposure algorithmically.
