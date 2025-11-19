# The Performance Dashboard: Radical Transparency

Our performance dashboard is at the core of our commitment to "Quantified Trust." This is **not an idealized backtest**, but a representation of **real or high-fidelity simulated execution results**. Every trade displayed has followed the same process as the one you observe live, ensuring that past performance is an honest measure of the strategy.

## Key Performance Indicators (KPIs)

We focus on metrics that assess not only profitability, but especially the **quality of risk management**.

- **Equity Curve:** Visualizes the growth of a portfolio that would have followed all executed signals, offering a clear view of progress and drawdown periods.
- **Profitability (Profit Factor):** The classic ratio of gross gains divided by gross losses. A quick indicator of the strategy's viability.
- **Maximum Drawdown:** The most critical measure of risk. It indicates the maximum loss incurred from a peak to a trough, helping you understand the historical risk of the strategy.
- **R-Multiple Distribution:** A histogram that classifies trades based on their risk multiple (how many "R" were won or lost).

## The R-Multiple: Our Central Evaluation Metric

Beyond the simple win/loss ratio, we use the **R-Multiple (Risk-to-Reward)** as the primary measure of a signal's quality.

- **Definition:** "R" is the **initial risk** defined for a trade (the distance between the entry point and the Stop-Loss). An R-Multiple of `+3R` means the trade generated a profit equal to three times the initial risk. A losing trade always ends at `-1R`.
- **Why is it so important?** This metric normalizes performance. A $1000 gain on a high-risk trade is not the same as a $1000 gain on a low-risk trade. The R-Multiple allows us to judge the **effectiveness of the strategy** regardless of position size.
- **How to analyze it:** A robust strategy consistently generates gains of `+2R`, `+3R`, or more, while systematically cutting losses at `-1R`. Our dashboard allows you to visualize this distribution and confirm the system's ability to find trades with an asymmetric advantage.

## How to Use the Dashboard

- **Risk Analysis:** Before following a strategy, evaluate its maximum drawdown to ensure it aligns with your risk tolerance.
- **Filter Optimization:** Use the R-Multiple distribution chart to see how performance changes at different levels of risk and reward.
- **Identify Market Regimes:** By filtering by date, you can analyze how the strategy has performed during different market conditions (e.g., bull market vs. bear market).
