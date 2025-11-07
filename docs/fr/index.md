# Introduction : Comment Fonctionne le Bot

## Le Tableau de Bord "Glass Box" : La Confiance Quantifiée

Ce tableau de bord offre une vue transparente et en direct des performances historiques de nos stratégies. Nous croyons en la "Confiance Quantifiée" plutôt qu'au battage médiatique sur la "précision".

<!-- Placeholder for the custom HTML/JavaScript block -->
<div id="glass-box-dashboard">
  <h3>Métriques de Performance en Direct</h3>
  <ul>
    <li><strong>Courbe de Capitaux :</strong> Chargement...</li>
    <li><strong>Facteur de Profit :</strong> Chargement...</li>
    <li><strong>Drawdown Maximal :</strong> Chargement...</li>
  </ul>
</div>

Le Bot HarmoFinder est un système de trading algorithmique sophistiqué. Son objectif principal est d'identifier, de valider et d'exécuter des opportunités de trading à haute probabilité basées sur des patterns harmoniques.

Il est crucial de comprendre que le bot n'est pas un simple générateur de signaux. C'est un pipeline de validation en plusieurs étapes conçu pour filtrer le "bruit" de faible qualité et n'agir que sur des configurations de premier ordre. Le processus complet peut être décomposé en trois phases :

1.  **Détection (Le "HarmoFinder") :** Le système scanne des centaines d'actifs sur plusieurs unités de temps (4h, 1D, 3D) 24/7. Son but est d'identifier la structure géométrique d'un "Pattern Détecté" (par exemple, un Gartley, une Chauve-souris ou un Crabe Profond).
2.  **Validation (Le "Moteur de Confiance") :** C'est le cœur du système. Chaque Pattern Détecté est immédiatement transmis à un moteur de notation. Ce moteur attribue un **Score de Confiance (0-100)** basé sur une analyse approfondie de la géométrie du pattern, du contexte du marché et de facteurs propriétaires basés sur l'IA.
3.  **Exécution (Le "Moniteur de Trade") :** Seuls les patterns atteignant un Score de Confiance élevé (par exemple, 70/100 ou plus) sont promus au rang de "Signal de Trade". Avant qu'un ordre ne soit passé, ce signal doit passer une dernière série de filtres en temps réel pour la gestion des risques et le régime de marché.

## Prochaines Étapes

- [Commencer](./getting_started.md)
- [Comprendre les Concepts](./core_concepts/confidence_score.md)
