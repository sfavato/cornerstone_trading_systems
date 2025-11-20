# AlphaGate Integration

## Architecture
AlphaGate is a "headless" Docker container that acts as a bridge between the analysis API and the user's exchange.

## Prerequisites
*   **Docker** installed.
*   **Exchange API Keys** (with trading permissions enabled).
*   **VPS** or **Cloud Run** Server.

## Security (Strong Point)
The system uses a **HMAC** mechanism to secure communications.

The user **must** configure their `ALPHAGATE_HMAC_SECRET` to prevent any fraudulent order injection. This shared secret ensures that only valid signals can trigger orders.

## Installation
Here is the standard command to run the container:

```bash
docker run -d \
-e BITGET_API_KEY="your_key" \
-e BITGET_SECRET="your_secret" \
-e ALPHAGATE_HMAC_SECRET="your_shared_secret" \
ghcr.io/gem-org/alphagate-client:latest
```

## Risk Warning
!!! warning "Automated Execution"
    The software executes received instructions without delay. Ensure you monitor your instance.
