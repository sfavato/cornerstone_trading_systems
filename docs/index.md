# Welcome to Cornerstone Indice

## The "Glass Box" Dashboard: Quantified Trust

This dashboard provides a live, transparent view into the historical performance of our strategies. We believe in "Quantified Trust" over "accuracy" hype.

<!-- Placeholder for the custom HTML/JavaScript block -->
<div id="glass-box-dashboard">
  <h3>Live Performance Metrics</h3>
  <ul>
    <li><strong>Equity Curve:</strong> Loading...</li>
    <li><strong>Profit Factor:</strong> Loading...</li>
    <li><strong>Max Drawdown:</strong> Loading...</li>
  </ul>
</div>

Cornerstone Indice is a sophisticated algorithmic trading system. Its primary purpose is to identify, validate, and execute high-probability trading opportunities based on harmonic chart patterns.

It's crucial to understand that the bot is not a simple signal generator. It is a multi-stage validation pipeline designed to filter out low-quality "noise" and only act on "A+" grade setups. The entire process can be broken down into three phases:

1.  **Detection (The "Cornerstone Detector"):** The system scans hundreds of assets across multiple timeframes (4h, 1D, 3D) 24/7. Its goal is to identify the geometric structure of a "Detected Pattern" (e.g., a Gartley, Bat, or Deep Crab).
2.  **Validation (The "Confidence Engine"):** This is the core of the system. Every Detected Pattern is immediately passed to a scoring engine. This engine assigns a **Confidence Score (0-100)** based on a deep analysis of the pattern's geometry, market context, and proprietary AI-driven factors.
3.  **Execution (The "Trade Monitor"):** Only patterns that achieve a high Confidence Score (e.g., 70/100 or higher) are promoted to a "Trade Signal." Before any order is placed, this signal must pass a final set of real-time filters for risk management and market regime.

## Onwards

- [Getting Started](./getting_started.md)
- [Core Concepts](./core_concepts/confidence_score.md)
