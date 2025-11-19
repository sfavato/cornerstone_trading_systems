# Understanding the "Signals" View: From Detection to Execution

The "Signals" view is the nerve center of your interface. It allows you to follow the lifecycle of a trading opportunity in real-time, from its validation by our Alpha engine to its active management. To correctly interpret the information, it is crucial to understand the distinction between the two signal states.

## 1. `Nearest Trades`: Pending Opportunities

A signal displayed in the **`Nearest Trades`** section is not yet an active position. It is a harmonic pattern that has met our strictest validation criteria, meaning it has obtained a high **Confidence Score**.

- **Status:** It is a validated "potential trade."
- **Condition for activation:** The market must still reach the **Entry Price** (the D point of the pattern) for the trade to be triggered by the `monitor_trades` service.
- **User action:** This is a monitoring phase. You can analyze the pattern, prepare your own analysis, or simply wait for the system to execute.

### The "Proximity Info" Indicator: Your Proximity Radar

One of the most important indicators in the `Nearest Trades` view is the **"Proximity Info"**.

- **Role:** It measures in real-time the **distance (in percentage) between the current market price and the target entry price (the D point)**.
- **Example:** A value of `-0.5%` means the current price is only 0.5% below the required entry level for a buy order.
- **Utility:** This indicator lets you know at a glance if a potential trade is about to be triggered, helping you anticipate market action.

## 2. `Active Trades`: Positions in Progress

When a signal moves from `Nearest Trades` to **`Active Trades`**, it means that the market conditions have been met and the position has been executed.

- **Status:** It is a "live" trading position.
- **Management:** The trade is now under the active control of the `monitor_trades` microservice, which applies the Stop-Loss and Take-Profit rules defined by the system.
- **User action:** This is a tracking phase. You can observe the position's performance in real-time and analyze how the system manages risk.

In summary, the "Signals" view gives you a transparent window into our decision-making chain: `Nearest Trades` show you what our Alpha has validated, and `Active Trades` show you what our risk manager is executing.
