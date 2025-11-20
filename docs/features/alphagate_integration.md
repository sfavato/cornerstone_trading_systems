# AlphaGate Integration

!!! warning "Technical Warning"
    This document is a technical specification intended for engineers and integrators. AlphaGate is a transport protocol, not an automated financial advisor.

## 1. Introduction & Philosophy

AlphaGate is designed as a secure **Data Transport Protocol**, not an autonomous "Money Machine". Its sole function is to transmit structured trading signals (JSON) from our analysis infrastructure to your local execution environment.

### Assumptions Management

*   **Assumption:** "The bot trades magically on its own."
*   **Technical Reality:** AlphaGate transmits a raw signal (JSON) to your local instance. Final execution (order placement) depends entirely on **YOUR** infrastructure (Docker), **YOUR** available funds, and **YOUR** internet connection. We provide the signal; you provide the execution.

## 2. Architecture & Latency

The system is not designed for High-Frequency Trading (HFT). It operates on Swing and Intraday timescales where latency of a few seconds is negligible.

### Signal Path

1.  **AI Engine (Cloud):** Pattern detection and signal generation.
2.  **Webhook (Internet):** Secure transmission via HTTPS.
3.  **Docker Client (User):** Reception and payload signing.
4.  **Exchange:** Order execution via API.

### The Truth About Speed

*   **Assumption:** "It's HFT with 0ms latency."
*   **Reality:**
    *   The system uses standard Webhooks over HTTPS.
    *   Average network latency is between **200ms and 2000ms** depending on network load and your server location.
    *   **Warning:** If you host the Docker Client on a domestic connection (ADSL/4G), additional delays are to be expected. Using a dedicated VPS (e.g., DigitalOcean, AWS, OVH) is strongly recommended to minimize latency and ensure stability.

## 3. Availability Management (Cold Start)

Our infrastructure is Cloud-Native (Serverless) to ensure maximum scalability.

*   **Assumption:** "The system is instant 24/7."
*   **Reality:** Cloud components may go idle during periods of low volatility. A "wake-up" time (**Cold Start**) of a few seconds is possible after long inactivity.
    *   This delay is normal and **does not impact the validity of Swing/Intraday signals**, which target price movements developing over several hours or days.

## 4. Security & Responsibility

Execution security relies on a shared responsibility model. We secure the transport; you secure the endpoint.

### The HMAC Secret (`ALPHAGATE_HMAC_SECRET`)

This parameter is the keystone of security. It allows your Docker client to verify that the signal indeed originates from our servers and has not been tampered with.

!!! danger "Host Responsibility"
    You are responsible for the security of your host machine. If your Docker container or server is compromised, your API keys are too.

### Security Best Practices

1.  **Root Execution:** Never run the container in `root` mode (handled by default by our image, but check your custom configurations).
2.  **API Restrictions:** Strictly restrict API Key permissions on the Exchange:
    *   ✅ Allow: "Spot Trade", "Futures Trade".
    *   ❌ **ABSOLUTELY FORBID**: "Withdraw".
    *   ✅ Use an **IP Whitelist** if your VPS has a static IP.

## 5. Limitations FAQ

This section addresses common issues related to user infrastructure.

**Q: Why didn't my order trigger even though I received a notification?**
**R:** Check your Docker logs immediately (`docker logs alphagate`). Common causes are:
*   Insufficient funds on the exchange (Balance < Position size).
*   Expired or invalid API Keys.
*   Momentary loss of internet connection on your server/PC.

**Q: The actual entry price is slightly different from the signal price.**
**R:** This is normal. It is the combined result of **"Slippage"** (natural market movement between signal and execution) and network delay. AlphaGate cannot guarantee the exact execution price.
