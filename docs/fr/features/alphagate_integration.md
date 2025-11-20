# Intégration AlphaGate

!!! warning "Avertissement Technique"
    Ce document est une spécification technique destinée aux ingénieurs et intégrateurs. AlphaGate est un protocole de transport, pas un conseiller financier automatisé.

## 1. Introduction & Philosophie

AlphaGate est conçu comme un **Protocole de Transport de Données** sécurisé et non comme une "Machine à Gains" autonome. Sa fonction unique est de transmettre des signaux de trading structurés (JSON) depuis notre infrastructure d'analyse vers votre environnement d'exécution local.

### Gestion des Attentes ("Assumptions Management")

*   **Assumption (Fausse Croyance) :** "Le bot trade tout seul magiquement."
*   **Réalité Technique :** AlphaGate transmet un signal brut (JSON) à votre instance locale. L'exécution finale (placement de l'ordre) dépend entièrement de **VOTRE** infrastructure (Docker), de **VOS** fonds disponibles, et de **VOTRE** connexion internet. Nous fournissons le signal ; vous fournissez l'exécution.

## 2. Architecture & Latence

Le système n'est pas conçu pour le High-Frequency Trading (HFT). Il opère sur des échelles de temps Swing et Intraday où la latence de quelques secondes est négligeable.

### Trajet du Signal

1.  **Moteur IA (Cloud)** : Détection du pattern et génération du signal.
2.  **Webhook (Internet)** : Transmission sécurisée via HTTPS.
3.  **Client Docker (Utilisateur)** : Réception et signature du payload.
4.  **Exchange** : Exécution de l'ordre via API.

### La Vérité sur la Vitesse

*   **Assumption :** "C'est du HFT avec 0ms de latence."
*   **Réalité :**
    *   Le système utilise des Webhooks standards sur HTTPS.
    *   La latence réseau moyenne est comprise entre **200ms et 2000ms** selon la charge du réseau et la localisation de votre serveur.
    *   **Attention :** Si vous hébergez le Docker Client sur une connexion domestique (ADSL/4G), des délais supplémentaires sont à prévoir. L'utilisation d'un VPS dédié (ex: DigitalOcean, AWS, OVH) est fortement recommandée pour minimiser la latence et garantir la stabilité.

## 3. Gestion de la Disponibilité (Cold Start)

Notre infrastructure est Cloud-Native (Serverless) pour garantir une évolutivité maximale.

*   **Assumption :** "Le système est instantané 24/7."
*   **Réalité :** Les composants Cloud peuvent entrer en veille lors de périodes de faible volatilité. Un temps de "réveil" (**Cold Start**) de quelques secondes est possible après une longue inactivité.
    *   Ce délai est normal et **n'impacte pas la validité des signaux Swing/Intraday**, qui visent des mouvements de prix se développant sur plusieurs heures ou jours.

## 4. Sécurité & Responsabilité

La sécurité de l'exécution repose sur un modèle de responsabilité partagée. Nous sécurisons le transport ; vous sécurisez le point de terminaison.

### Le Secret HMAC (`ALPHAGATE_HMAC_SECRET`)

Ce paramètre est la clé de voûte de la sécurité. Il permet à votre client Docker de vérifier que le signal provient bien de nos serveurs et n'a pas été altéré.

!!! danger "Responsabilité de l'Hôte"
    Vous êtes responsable de la sécurité de votre machine hôte. Si votre conteneur Docker ou votre serveur est compromis, vos clés API le sont aussi.

### Bonnes Pratiques de Sécurité

1.  **Exécution Root :** Ne jamais faire tourner le conteneur en mode `root` (géré par défaut par notre image, mais vérifiez vos configurations personnalisées).
2.  **Restrictions API :** Restreindre strictement les permissions des Clés API sur l'Exchange :
    *   ✅ Autoriser : "Spot Trade", "Futures Trade".
    *   ❌ **INTERDIRE ABSOLUMENT** : "Withdraw" (Retrait).
    *   ✅ Utiliser une **IP Whitelist** si votre VPS a une IP statique.

## 5. FAQ des Limitations

Cette section adresse les problèmes courants liés à l'infrastructure utilisateur.

**Q: Pourquoi mon ordre ne s'est-pas déclenché alors que j'ai reçu une notification ?**
**R:** Vérifiez immédiatement vos logs Docker (`docker logs alphagate`). Les causes les plus fréquentes sont :
*   Fonds insuffisants sur l'exchange (Balance < Taille de position).
*   Clés API expirées ou invalides.
*   Perte de connexion internet momentanée de votre serveur/PC.

**Q: Le prix d'entrée réel est légèrement différent du prix du signal.**
**R:** C'est normal. C'est le résultat combiné du **"Slippage"** (glissement naturel du marché entre le moment du signal et l'exécution) et du délai réseau. AlphaGate ne peut pas garantir le prix d'exécution exact au centime près.
