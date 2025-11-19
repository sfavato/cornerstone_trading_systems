# Risk Management: A Dual-Level Approach

A trading strategy is nothing without rigorous risk management. Our system, via the `monitor_trades` microservice, applies a two-level Stop-Loss (SL) approach to protect capital while adapting to market conditions. This distinction between an initial SL and a dynamic SL is at the heart of our capital preservation logic.

## 1. Geometric / Static SL: The Initial Safeguard

The first level of protection is the **Geometric Stop-Loss**. It is "static" because it is defined at the time of position entry and is based purely on the **geometric structure of the harmonic pattern**.

-   **Definition:** This SL is calculated by the `shared_models/SLTP.py` module. It is usually placed just beyond the structural point that would invalidate the pattern (e.g., beyond the X point for most patterns).
-   **Role:** It is the **absolute safeguard**. It represents the price level at which the technical logic behind the trade is fundamentally invalidated. If this level is reached, the trade is cut without exception, as the initial hypothesis is no longer valid.
-   **Characteristic:** It is predefined and does not change, thus offering full transparency on the maximum initial risk (`1R`) of each trade.

## 2. Dynamic / Invalidation SL: Real-Time Adjustment

The second level is the **Dynamic Stop-Loss**. This is a more sophisticated logic, applied in real-time by the `monitor_trades/enforce_stoploss_rules.py` module. Its objective is to detect if the "behavior" of the price invalidates the trade, **even if the Geometric SL has not yet been hit**.

-   **Definition:** This SL is not a fixed price level, but a **behavioral rule**. It can be triggered by various conditions that indicate the expected scenario is not materializing.
-   **Examples of invalidation rules:**
    -   **Candle Close:** One of the most common rules. The trade can be canceled if a candle (e.g., on the trade's timeframe) **closes** beyond a certain risk threshold, even if the wick has not touched the Geometric SL. This allows exiting a trade that shows strong opposing pressure.
    -   **Volatility Stop:** The system can use a volatility indicator like the "Chandelier Exit" or a multiple of the ATR (Average True Range) to trail the price. If the price crosses this moving threshold, the trade is cut to adapt to an unexpected increase in volatility.
    -   **Time Stop:** If a trade stagnates for a prolonged period without moving towards the target, it can be closed to free up capital.

By combining a Geometric SL for structural risk and a Dynamic SL for behavioral risk, our system aims to optimize risk management: cutting losses decisively when the trade is invalidated, but also adapting intelligently when the market shows early warning signs of danger.
