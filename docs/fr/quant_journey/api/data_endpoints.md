# Points d'Accès aux Données

Cette section fournit des informations détaillées sur les points d'accès de l'API HarmoFinder disponibles pour nos utilisateurs du niveau "Quant". Notre API est construite sur une pile haute performance à faible latence (FastAPI, TimescaleDB) pour fournir des données de qualité institutionnelle.

## `/api/v1/ohlcv/{ex}/{sym}`

**Méthode :** `GET`

**Description :** Récupère les barres historiques OHLCV (Open, High, Low, Close, Volume), y compris notre `volume_delta` propriétaire. Ce point d'accès est idéal pour le backtesting et l'analyse historique.

=== "Python (requests)"
    ```python
    import requests
    import json

    API_URL = "https://api.harmofinder.ai/api/v1/ohlcv/binance/btcusdt"
    # Remplacez par votre clé API réelle
    headers = {"Authorization": "Bearer VOTRE_CLÉ_API"}

    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Erreur : {response.status_code}")
    ```

=== "cURL (Shell)"
    ```bash
    curl -X GET "https://api.harmofinder.ai/api/v1/ohlcv/binance/btcusdt" \
         -H "Authorization: Bearer VOTRE_CLÉ_API"
    ```

=== "Réponse JSON (Exemple)"
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

## Référence des Points d'Accès de l'API

| Point d'Accès              | Méthode | Description (Source)                             | Persona Cible       |
|----------------------------|---------|--------------------------------------------------|---------------------|
| `/api/v1/ohlcv/{ex}/{sym}` | `GET`   | Récupère les barres OHLCV historiques + `volume_delta`. | Quant (Backtesting) |
| `/api/v1/trades/{ex}/{sym}`| `GET`   | Récupère les données de tick brutes pour une analyse approfondie. | Quant (Recherche)   |
| `/ws/v1/cvd/{ex}/{sym}`    | `WS`    | Diffuse les mises à jour de tick en direct et les notifications de clôture de barre. | Quant (Trading en Direct)|
