# Intégration AlphaGate

## Architecture
AlphaGate est un conteneur Docker "headless" qui agit comme un pont entre notre API d'analyse et l'exchange de l'utilisateur.

## Pré-requis
*   **Docker** installé.
*   **Clés API Exchange** (avec permissions de trading activées).
*   **Serveur VPS** ou **Cloud Run**.

## Sécurité (Point Fort)
Le système utilise un mécanisme **HMAC** pour sécuriser les communications.

L'utilisateur **doit** configurer son `ALPHAGATE_HMAC_SECRET` pour éviter toute injection d'ordre frauduleux. Ce secret partagé garantit que seuls les signaux valides du système Cornerstone peuvent déclencher des transactions.

## Installation
Voici la commande type pour lancer le conteneur :

```bash
docker run -d \
-e BITGET_API_KEY="votre_cle" \
-e BITGET_SECRET="votre_secret" \
-e ALPHAGATE_HMAC_SECRET="votre_secret_partage" \
ghcr.io/gem-org/alphagate-client:latest
```

## Avertissement de Risque
!!! warning "Exécution Automatique"
    Le logiciel exécute les instructions reçues sans délai. Assurez-vous de surveiller votre instance.
