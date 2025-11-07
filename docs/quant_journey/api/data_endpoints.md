# Data Endpoints

This section provides detailed information about the HarmoFinder API endpoints available to our "Quant" tier users. Our API is built on a high-performance, low-latency stack (FastAPI, TimescaleDB) to deliver institutional-grade data.

## `/api/v1/ohlcv/{ex}/{sym}`

**Method:** `GET`

**Description:** Fetches historical OHLCV (Open, High, Low, Close, Volume) bars, including our proprietary `volume_delta`. This endpoint is ideal for backtesting and historical analysis.

=== "Python (requests)"
    ```python
    import requests
    import json

    API_URL = "https://api.harmofinder.ai/api/v1/ohlcv/binance/btcusdt"
    # Replace with your actual API key
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.status_code}")
    ```

=== "cURL (Shell)"
    ```bash
    curl -X GET "https://api.harmofinder.ai/api/v1/ohlcv/binance/btcusdt" \
         -H "Authorization: Bearer YOUR_API_KEY"
    ```

=== "JSON Response (Example)"
    ```json
    {
      "exchange": "binance",
      "symbol": "btcusdt",
      "bars": [
        {
          "timestamp": 1672531200,
          "open": 16542.3,
          "high": 16559.2,
          "low": 16521.9,
          "close": 16533.1,
          "volume": 4500.23,
          "volume_delta": -150.78
        }
      ]
    }
    ```

## API Endpoint Reference

| Endpoint                   | Method | Description (Source)                             | Target Persona      |
|----------------------------|--------|--------------------------------------------------|---------------------|
| `/api/v1/ohlcv/{ex}/{sym}` | `GET`  | Fetches historical OHLCV bars + `volume_delta`.  | Quant (Backtesting) |
| `/api/v1/trades/{ex}/{sym}`| `GET`  | Fetches raw tick data for deep analysis.         | Quant (Research)    |
| `/ws/v1/cvd/{ex}/{sym}`    | `WS`   | Streams live tick updates and bar close notifications. | Quant (Live Trading)|
