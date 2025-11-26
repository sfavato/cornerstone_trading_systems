## Pattern vs. Signal : Une Comparaison Visuelle

<ul class="grid cards" markdown>

<li>
### Pattern Détecté (Faible Confiance)
**Confiance** : 🔴 Faible (15/100)
**Analyse** : Bruit de marché
**Action** : Observation uniquement
</li>

<li>
### Signal Validé (Haute Confiance)
**Confiance** : 🟢 Élevée (85/100)
**Analyse** : Opportunité de trade exploitable
**Facteurs de Confluence** :
- ✅ Structure de marché (Zone de liquidité)
- ✅ Flux d'ordres (Divergence CVD)
- ✅ Pression des dérivés (OI, Financement)
- ✅ Métriques On-Chain (MVRV, SOPR)
</li>

</ul>

## Le Concept Clé

C'est la distinction la plus importante à comprendre pour les parties prenantes. Le bot sépare les "patterns" des "signaux".

### Pattern Détecté

Un **Pattern Détecté** est simplement une matière première. C'est une forme géométrique que le service `harmofinder` a identifiée. Le système peut en détecter des centaines par jour. La plupart sont des patterns de faible qualité, "brouillons", et sont immédiatement rejetés par le moteur de notation. Un Pattern Détecté n'est *pas* une instruction de trader.

### Signal de Trade

Un **Signal de Trade** est une opportunité de haute qualité et validée. C'est un Pattern Détecté qui a passé avec succès l'ensemble du pipeline de validation et a reçu un **Score de Confiance** élevé. Seules ces configurations de premier ordre sont transmises au service `monitor_trades` pour une exécution potentielle.

> **Analogie :** Un **Pattern Détecté** est comme identifier un nuage qui *ressemble* à un nuage de pluie. Un **Signal de Trade** est ce même nuage, *plus* une baisse de température confirmée de 20 degrés, une lecture d'humidité de 90% et un vent qui se lève. Nous n'agissons que sur le signal, pas sur la forme.

## La Zone d'Approche : "Nearest Trade"

Pour fournir aux utilisateurs un avertissement précoce, le système n'attend pas simplement que le prix d'entrée exact d'un signal à haute confiance soit déclenché. Il surveille également une **Zone d'Approche**.

Lorsque le prix de marché actuel d'un signal validé entre dans cette zone de proximité (par exemple, à moins de 0.5% du prix d'entrée), le système émet une alerte **"Nearest Trade"**. Cela sert d'avertissement, vous permettant de vous préparer à une entrée potentielle sans avoir à surveiller constamment les graphiques. C'est l'état final avant qu'un signal ne devienne une transaction active.
