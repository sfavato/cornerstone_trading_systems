# Contenu UX pour HarmoGrid

## Infobulles (Tooltips)

### 1. Statut `GRID_PENDING`
**Texte :** "Le système a placé une grille de 4 ordres d'entrée. Le statut passera à 'in-trade' dès que le premier ordre sera exécuté."

### 2. Liste des `grid_order_ids`
**Texte :** "Voici les identifiants des 4 ordres limites de la grille HarmoGrid. Le système construit la position à travers ces points d'entrée."

## Entrées de la FAQ

### 1. Pourquoi mon trade a-t-il placé 4 ordres d'entrée ?
**Réponse :** Votre trade utilise la stratégie HarmoGrid. C'est un mécanisme d'entrée avancé qui répartit votre point d'entrée sur quatre ordres limites pondérés. L'objectif est d'obtenir un meilleur prix d'entrée moyen et d'augmenter les chances que votre trade soit exécuté, même dans un marché volatile.

### 2. Mon trade était gagnant et a atteint le TP1. Pourquoi le bot a-t-il annulé mes autres ordres d'entrée ?
**Réponse :** C'est une fonctionnalité de protection intentionnelle de la stratégie HarmoGrid. Lorsque votre trade est déjà gagnant (atteinte du TP1), le système annule les ordres d'entrée restants pour éviter d'acheter un actif qui est déjà en phase de vente. C'est une mesure de gestion du risque qui sécurise vos gains et protège votre capital.
