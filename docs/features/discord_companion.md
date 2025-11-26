# Discord Companion: G.E.M.

The G.E.M. Discord Bot is a powerful mobile extension of the Cornerstone Indice platform, allowing you to stay connected with market opportunities and system status on the go.

## Commands

### !gem

This command provides a real-time snapshot of the most promising trade setups the system is currently monitoring.

### !stats

Use this command to get a quick overview of the system's health and operational status.

## Reading Alerts

The bot will issue two primary types of alerts in the designated Discord channels.

### 🟢 Active Trade

This alert signifies a trade that has been executed and is currently active. The entry price has been met, and the position is live.

### 🚨 Imminent Setup (Nearest Trade)

This alert, also known as a "Nearest Trade," is a pre-execution warning. It indicates that a high-confidence signal is approaching its ideal entry zone (typically < 1.5% away). This gives you time to prepare and monitor the setup before it triggers.

!!! example "Example: Imminent Setup Alert"

    === "Light Mode"

        ```text
        +--------------------------------------------------+
        | 🚨 IMMINENT SETUP - BTC/USDT                     |
        |--------------------------------------------------|
        | Pattern:       Bullish Bat                        |
        | Timeframe:     4H                                 |
        | Proximity:     0.5% from Entry                    |
        | Entry Price:   $65,000                            |
        | Stop-Loss:     $63,500                            |
        | Target:        $68,000                            |
        |--------------------------------------------------|
        | Confidence Score: 8.2/10 ★★★☆☆                   |
        | Risk/Reward:   3.5                                |
        +--------------------------------------------------+
        ```

    === "Dark Mode"

        ```text
        +--------------------------------------------------+
        | 🚨 IMMINENT SETUP - BTC/USDT                     |
        |--------------------------------------------------|
        | Pattern:       Bullish Bat                        |
        | Timeframe:     4H                                 |
        | Proximity:     0.5% from Entry                    |
        | Entry Price:   $65,000                            |
        | Stop-Loss:     $63,500                            |
        | Target:        $68,000                            |
        |--------------------------------------------------|
        | Confidence Score: 8.2/10 ★★★☆☆                   |
        | Risk/Reward:   3.5                                |
        +--------------------------------------------------+
        ```

!!! warning "Image Pending"
    A real screenshot of a Discord alert will be added here shortly to replace this textual representation.

### The Confidence Score

Each alert embed includes a **Confidence Score**. This metric represents the AI's level of certainty in the trade's potential success. A higher score indicates a more favorable risk/reward profile.
