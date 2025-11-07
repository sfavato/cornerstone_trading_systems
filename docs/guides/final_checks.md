## Final Entry Checks: The Execution Gateway

Even after a pattern receives a high Confidence Score (e.g., 8/10) and becomes a "Trade Signal," the `monitor_trades` service performs a final list of checks before placing an order. A signal must pass *all* of these filters:

1.  **Confidence Score Filter:** Is the score `> 7` (or the configured threshold)?
2.  **Market Regime Filter:** Is the trade aligned with the broader market trend? The `market_regime_filter.py` will block a LONG trade, even if it has a high score, if the overall market is in a strong "Trending Down" regime.
3.  **Contextual Filters:** Are there any immediate "red flags"? The `funding_rate_filter.py` or `liquidation_context_filter.py` can stop a trade if market conditions are dangerously volatile or skewed.
4.  **Risk Management Filter:** Does the trade meet our internal Risk/Reward rules? The `calculation_logic.py` confirms the stop-loss is valid and calculates a safe position size based on our account equity.

Only a signal that passes every single check in this entire funnel—from Detection to Purity to Confluence to AI Context to Final Filters—will result in an order being placed on the exchange.
