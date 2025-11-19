# Le Tableau de Bord de Performance : La Transparence Radicale

Notre tableau de bord de performance est au cœur de notre engagement envers la "Confiance Quantifiée". Il ne s'agit **pas d'un backtest idéalisé**, mais d'une représentation des **résultats d'exécution réels ou simulés avec une haute fidélité**. Chaque trade affiché a suivi le même processus que celui que vous observez en direct, garantissant que les performances passées sont une mesure honnête de la stratégie.

## Les Indicateurs Clés de Performance (KPIs)

Nous nous concentrons sur des métriques qui évaluent non seulement la profitabilité, mais surtout la **qualité de la gestion du risque**.

- **Courbe de Capitaux (Equity Curve) :** Visualise la croissance d'un portefeuille qui aurait suivi tous les signaux exécutés, offrant une vue claire de la progression et des périodes de drawdown.
- **Profitabilité (Profit Factor) :** Le ratio classique des gains bruts divisés par les pertes brutes. Un indicateur rapide de la viabilité de la stratégie.
- **Drawdown Maximal :** La mesure la plus critique du risque. Elle indique la perte maximale subie d'un pic à un creux, vous aidant à comprendre le risque historique de la stratégie.
- **Distribution des R-Multiples :** Un histogramme qui classe les trades en fonction de leur multiple de risque (combien de "R" ont été gagnés ou perdus).

## Le R-Multiple : Notre Métrique Centrale d'Évaluation

Au-delà du simple ratio gain/perte, nous utilisons le **R-Multiple (Risk-to-Reward)** comme principale mesure de la qualité d'un signal.

- **Définition :** Le "R" est le **risque initial** défini pour un trade (la distance entre le point d'entrée et le Stop-Loss). Un R-Multiple de `+3R` signifie que le trade a généré un profit équivalent à trois fois le risque initial. Un trade perdant se termine toujours à `-1R`.
- **Pourquoi est-ce si important ?** Cette métrique normalise la performance. Un gain de 1000$ sur un trade à haut risque n'a pas la même valeur qu'un gain de 1000$ sur un trade à faible risque. Le R-Multiple nous permet de juger de l'**efficacité de la stratégie** indépendamment de la taille de la position.
- **Comment l'analyser :** Une stratégie robuste génère de manière constante des gains de `+2R`, `+3R` ou plus, tout en coupant systématiquement les pertes à `-1R`. Notre tableau de bord vous permet de visualiser cette distribution et de confirmer la capacité du système à trouver des trades avec un avantage asymétrique.

## Comment Utiliser le Tableau de Bord

- **Analyse de Risque :** Avant de suivre une stratégie, évaluez son drawdown maximal pour vous assurer qu'il correspond à votre tolérance au risque.
- **Optimisation de Filtre :** Utilisez le graphique de distribution des R-Multiples pour voir comment la performance change à différents niveaux de risque et de récompense.
- **Identifier les Régimes de Marché :** En filtrant par date, vous pouvez analyser comment la stratégie a performé pendant différentes conditions de marché (ex: bull market vs. bear market).
