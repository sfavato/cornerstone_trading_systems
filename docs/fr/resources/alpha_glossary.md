# Glossaire Alpha

Ce glossaire définit les métriques "alpha" de base que notre système utilise pour générer et valider des signaux. Comprendre ces concepts est essentiel pour tirer le meilleur parti de Cornerstone Indice.

!!! note "Alpha Exotique"
    **L'Alpha Exotique** fait référence à l'avantage informationnel (l'alpha) dérivé de **sources de données non traditionnelles ou non corrélées** aux graphiques de prix. Plutôt que de se limiter à l'analyse technique classique, cet alpha intègre des facteurs externes pour évaluer la santé et le sentiment du marché.
    - **Exemples :** Données On-Chain (flux de cryptomonnaies entre portefeuilles et échanges), données de dérivés (liquidations, Open Interest), analyse de sentiment sur les réseaux sociaux, ou même des données macro-économiques.
    - **Rôle dans notre système :** C'est un pilier clé de notre **Score de Confiance**, permettant de filtrer des signaux techniquement valides mais qui font face à un contexte de marché défavorable.

!!! note "Alpha Structurel"
    **L'Alpha Structurel** est l'avantage (l'alpha) obtenu de l'analyse inhérente à la **structure géométrique des patterns** et à leur interaction avec la dynamique des prix. Il repose sur l'hypothèse que certaines formes graphiques récurrentes ont une probabilité de résolution prédictible.
    - **Exemples :** La précision des ratios de Fibonacci d'un pattern harmonique, la localisation d'un signal par rapport aux niveaux de support/résistance majeurs (identifiés via Gann ou le Volume Profile).
    - **Rôle dans notre système :** Il constitue la base de notre détection. L'alpha structurel identifie "quoi" et "où", tandis que l'alpha exotique valide le "quand".

!!! note "Delta de Volume Cumulatif (CVD)"
    Le CVD est au cœur de notre analyse du flux d'ordres. C'est un total cumulé de la différence entre le volume d'achat et le volume de vente. Un CVD en hausse indique une pression d'achat nette, tandis qu'un CVD en baisse indique une pression de vente nette. Une **divergence** entre le prix et le CVD est un signal puissant qui précède souvent un renversement.

!!! note "Intérêt Ouvert (OI)"
    L'Intérêt Ouvert représente le nombre total de contrats dérivés (futures ou options) en circulation qui n'ont pas été réglés. Un OI en hausse indique que de nouveaux capitaux entrent sur le marché, tandis qu'un OI en baisse suggère que des positions sont en train d'être fermées. Il donne un aperçu de la force et de la conviction derrière un mouvement de prix.

!!! note "Taux de Financement"
    Les Taux de Financement sont des paiements périodiques effectués entre traders pour maintenir le prix d'un contrat à terme perpétuel en ligne avec le prix au comptant sous-jacent. Des taux de financement positifs élevés suggèrent qu'une majorité de traders sont longs et paient une prime pour maintenir leurs positions, ce qui peut être un indicateur contraire. Inversement, des taux négatifs élevés suggèrent un sentiment baissier.

!!! note "Score de Risque Weekend (WRS)"
    Le WRS est une métrique propriétaire de Cornerstone Indice conçue pour quantifier le risque systémique associé aux sessions de trading à faible liquidité, typiquement observées durant les weekends sur le marché crypto. Le score est un agrégat de plusieurs indicateurs avancés, incluant mais non limité à, le Ratio de Levier Estimé (ELR), la divergence de l'Intérêt Ouvert (OI), et les patterns de compression de volatilité. Un score WRS élevé déclenche des protocoles de gestion des risques prédéfinis pour protéger le capital.

!!! note "Smart Reversal Override"
    Un mécanisme de sécurité qui permet au système d'entrer en position contre la tendance principale UNIQUEMENT si une divergence spécifique (Prix vs Momentum) est détectée. Il filtre les faux signaux en s'assurant que le mouvement contre-tendance possède une véritable dynamique.

!!! note "Score de Confiance"
    Un score de probabilité (0-10) généré par nos modèles de Machine Learning (XGBoost/GNN). Il prédit la probabilité qu'un pattern atteigne son objectif. Seuls les signaux au-dessus d'un seuil dynamique (ex: 7.5/10) sont exécutés.

!!! note "Drift Monitoring"
    Un processus continu qui compare les propriétés statistiques des données de marché en direct avec les données utilisées pour entraîner nos modèles. Si le marché "dérive" trop loin des conditions d'entraînement (Concept Drift), le système nous alerte d'une dégradation potentielle de la performance, garantissant que l'IA s'adapte aux changements de régime de marché.
