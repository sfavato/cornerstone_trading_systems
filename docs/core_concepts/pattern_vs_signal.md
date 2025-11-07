## Pattern vs. Signal: The Core Concept

This is the most important distinction for stakeholders to understand. The bot separates "patterns" from "signals."

### Detected Pattern

A **Detected Pattern** is simply raw material. It is a geometric shape that the `harmofinder` service has identified. The system may detect hundreds of these per day. Most are low-quality, "sloppy" patterns and are immediately discarded by the scoring engine. A Detected Pattern is *not* an instruction to trade.

### Trade Signal

A **Trade Signal** is a high-quality, validated opportunity. It is a Detected Pattern that has successfully passed through the entire validation pipeline and received a high **Confidence Score**. Only these "A+" grade setups are passed to the `monitor_trades` service for potential execution.

> **Analogy:** A **Detected Pattern** is like identifying a cloud that *looks* like a rain cloud. A **Trade Signal** is that same cloud, *plus* a confirmed 20-degree drop in temperature, a 90% humidity reading, and a rising wind. We only act on the signal, not the shape.
