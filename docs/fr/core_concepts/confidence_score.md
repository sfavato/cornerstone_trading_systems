# Le Score de Confiance : Le Cœur de Notre Alpha

Le **Score de Confiance** est bien plus qu'une simple note ; c'est le cœur de notre Alpha. Il agit comme un filtre dynamique et intelligent qui évalue la **probabilité de succès** d'un pattern harmonique détecté. Chaque score est la sortie d'un modèle prédictif (Machine Learning) qui a été entraîné sur des milliers de cas de trades passés pour optimiser sa capacité à distinguer les opportunités réelles du bruit de marché.

Notre modèle a démontré une performance robuste durant notre phase de R&D (Phase I), avec une **AUC (Area Under Curve) d'environ 0.80**, confirmant sa forte capacité prédictive.

## Les Trois Piliers du Score de Confiance

Le score est le résultat d'une analyse intégrée de trois piliers d'information. Le modèle ne se contente pas de "voir" le pattern, il analyse le contexte global du marché pour prendre une décision éclairée.

### 1. Facteurs Géométriques : La Pureté de la Structure

- **Objectif :** Évaluer la conformité du pattern avec sa définition théorique.
- **Analyse :** Le modèle mesure la précision des ratios de Fibonacci entre les points clés (X, A, B, C, D) du pattern. Une structure qui respecte rigoureusement les ratios théoriques (par exemple, un point B exactement à 0.618 pour un Gartley) recevra une évaluation positive sur ce pilier. C'est la base de la validation : sans une géométrie correcte, il n'y a pas de signal.

### 2. Confluence Technique : La Validation par le Marché

- **Objectif :** Confirmer que le signal est en harmonie avec les conditions actuelles du marché.
- **Analyse :** Le modèle intègre une série d'indicateurs techniques classiques pour s'assurer que le pattern n'apparaît pas "hors contexte". Les facteurs incluent, mais ne se limitent pas à :
    - **Le Volume :** Une augmentation du volume dans la zone de complétion du pattern.
    - **Le RSI (Relative Strength Index) :** La présence de divergences confirmant un essoufflement de la tendance précédente.
    - **La Tendance de Fond :** L'alignement du signal avec la tendance sur les unités de temps supérieures.

### 3. Alpha Exotique : L'Avantage Informationnel

- **Objectif :** Intégrer des données externes et macro-économiques pour obtenir une vision complète du risque systémique.
- **Analyse :** C'est ici que notre Alpha prend toute sa dimension. Le modèle analyse des sources de données non corrélées au prix pour évaluer la santé globale du marché :
    - **Le Régime de Marché :** Est-ce un marché en tendance, en range, volatile ?
    - **Les Données On-Chain (pour les cryptos) :** Analyse des flux de capitaux, de l'activité des portefeuilles, etc.
    - **Les Données de Dérivés :** Open Interest, liquidations, qui peuvent indiquer une faiblesse structurelle.

---

**Contrainte de Propriété Intellectuelle (IP) :** Il est essentiel de comprendre que le Score de Confiance est le fruit de notre recherche et développement. Les features exactes utilisées par le modèle, leurs pondérations spécifiques et l'architecture du modèle lui-même restent notre propriété intellectuelle et ne sont pas divulguées. Notre transparence réside dans la performance vérifiable du score, pas dans la révélation de sa formule.
