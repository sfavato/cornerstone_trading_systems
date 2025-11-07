# Le "Confidence Score" (0-100)

Le "Confidence Score" est la note finale et agrégée (de 0 à 100) que le système attribue à un pattern après sa détection. Il répond à une question : **"Quelle est la probabilité que ce pattern réussisse maintenant, dans les conditions de marché actuelles ?"**

- **Score 0-40 :** Très faible qualité. Ignoré.
- **Score 41-69 :** Qualité moyenne. Potentiel pour une analyse manuelle mais généralement ignoré par le bot.
- **Score 70-100 :** Haute qualité, "Signal de Trade" validé. Transmis au moteur d'exécution.

Le seuil de 70 est notre référence par défaut, mais les utilisateurs "Pro" et "Quant" peuvent ajuster ce filtre via l'API.

## Composants du Score : Comment il est Calculé

Le score final de 0-100 est une agrégation de plusieurs scores indépendants.
`Score Final (0-100) = (Score de Pureté Géométrique) + (Bonus de Confluence de Marché) + (Bonus/Malus de Contexte IA)`

### 1. Score de Pureté Géométrique (La Base)

- **Description :** Une note sur la perfection technique du pattern.
- **Calcul :** Mesure la proximité des ratios de Fibonacci (points X, A, B, C, D) avec la définition "parfaite" du pattern. Un Gartley avec un point B à 0.617 aura un score de pureté bien plus élevé qu'un autre à 0.590.
- **Impact :** Constitue la base du score. Un pattern "brouillon" commence avec une base faible et a peu de chances de devenir un Signal de Trade.

### 2. Score de Confluence de Marché (Le "Où")

- **Description :** Analyse où sur le graphique le pattern se termine. Un pattern se formant sur un niveau de structure majeur est plus fiable.
- **Composants :**
    - **Alignement Volume Profile :** Vérifie le prix d'entrée (point D) par rapport au Volume Profile. Un bonus est accordé si le point D atterrit sur le Point of Control (POC), le Value Area High (VAH) ou le Value Area Low (VAL).
    - **Divergence RSI :** Vérifie la présence d'une divergence (classique ou cachée) du RSI sur l'unité de temps du pattern, indiquant un affaiblissement du momentum contraire.
    - **Localisation VWAP :** Compare le prix d'entrée au VWAP (Volume-Weighted Average Price). Un pattern haussier se formant au-dessus du VWAP est considéré comme plus fort.
    - **Tendance de Fond (HTF) :** Analyse si le pattern est en accord avec la tendance de l'unité de temps supérieure (Higher-Timeframe) pour un meilleur filtrage.

### 3. Score de Contexte IA (Le "Quand" / Alpha Exotique)

- **Description :** Notre "sauce secrète". Un score prédictif issu d'un modèle IA (XGBoost) entraîné sur nos données historiques pour répondre à la question : "Maintenant est-ce un bon moment pour que ce pattern réussisse ?"
- **Données Analysées :**
    - **Données de Dérivés :** Taux de Financement (Funding Rates), Open Interest, CVD, et Données de Liquidation.
    - **Données On-Chain :** Flux Nets des Echanges (Exchange Netflows), MVRV (Market Value to Realized Value).
    - **Données d'Options :** Ratio Put/Call.
- **Impact :** Agit comme un bonus ou un malus puissant. Un pattern parfait (Pureté) sur un niveau clé (Confluence) peut quand même être rejeté si l'IA détecte que des conditions de marché (ex: funding trop élevé) s'opposent fortement au trade.
