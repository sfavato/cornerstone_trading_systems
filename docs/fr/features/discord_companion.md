# Compagnon Discord : G.E.M.

Le Bot Discord G.E.M. est une extension mobile puissante de la plateforme Cornerstone Indice, vous permettant de rester connecté aux opportunités de marché et à l'état du système lors de vos déplacements.

## Commandes

### !gem

Cette commande fournit un aperçu en temps réel des configurations de trading les plus prometteuses que le système surveille actuellement.

### !stats

Utilisez cette commande pour obtenir un aperçu rapide de l'état de santé et du statut opérationnel du système.

## Lecture des Alertes

Le bot émettra deux types principaux d'alertes dans les canaux Discord désignés.

### 🟢 Trade Actif

Cette alerte signifie qu'une transaction a été exécutée et est actuellement active. Le prix d'entrée a été atteint et la position est en cours.

### 🚨 Configuration Imminente (Trade le Plus Proche)

Cette alerte, également connue sous le nom de "Nearest Trade", est un avertissement de pré-exécution. Elle indique qu'un signal à haute confiance approche de sa zone d'entrée idéale (généralement à moins de 1.5%). Cela vous donne le temps de vous préparer et de surveiller la configuration avant son déclenchement.

!!! example "Exemple : Alerte de Configuration Imminente"

    === "Mode Clair"

        ```text
        +--------------------------------------------------+
        | 🚨 CONFIGURATION IMMINENTE - BTC/USDT            |
        |--------------------------------------------------|
        | Pattern:       Chauve-souris haussière          |
        | Timeframe:     4H                                 |
        | Proximité:     À 0.5% de l'Entrée                 |
        | Prix d'Entrée: 65,000 $                           |
        | Stop-Loss:     63,500 $                           |
        | Cible:         68,000 $                           |
        |--------------------------------------------------|
        | Score de Confiance: 8.2/10 ★★★☆☆                  |
        | Risque/Récompense: 3.5                             |
        +--------------------------------------------------+
        ```

    === "Mode Sombre"

        ```text
        +--------------------------------------------------+
        | 🚨 CONFIGURATION IMMINENTE - BTC/USDT            |
        |--------------------------------------------------|
        | Pattern:       Chauve-souris haussière          |
        | Timeframe:     4H                                 |
        | Proximité:     À 0.5% de l'Entrée                 |
        | Prix d'Entrée: 65,000 $                           |
        | Stop-Loss:     63,500 $                           |
        | Cible:         68,000 $                           |
        |--------------------------------------------------|
        | Score de Confiance: 8.2/10 ★★★☆☆                  |
        | Risque/Récompense: 3.5                             |
        +--------------------------------------------------+
        ```

!!! warning "Image en attente"
    Une capture d'écran réelle d'une alerte Discord sera ajoutée ici sous peu pour remplacer cette représentation textuelle.

### Le Score de Confiance

Chaque message d'alerte inclut un **Score de Confiance**. Cette métrique représente le niveau de certitude de l'IA quant au succès potentiel de la transaction. Un score plus élevé indique un profil risque/récompense plus favorable.
