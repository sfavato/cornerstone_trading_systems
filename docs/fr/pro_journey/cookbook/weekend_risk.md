# Comprendre le Protocole 'Risque Weekend' (WRS)

Le marché des cryptomonnaies ne dort jamais, mais sa nature change radicalement le weekend. Cette page explique comment HarmoFinder gère proactivement les risques associés à ces changements de dynamique.

## Pour le Trader Pro : Votre Assurance Contre les "Flash Crashs"

**Le Message Clé :** "Le marché crypto change le weekend. La liquidité institutionnelle disparaît, rendant le marché fragile et sujet aux 'flash crashs'. Notre bot le sait. Le 'Disjoncteur Intelligent' est votre assurance : il réduit l'exposition ou sécurise le capital avant que ces chutes violentes ne se produisent."

Le "Disjoncteur Intelligent" est un protocole de sécurité conçu pour vous protéger. Basé sur notre "Weekend Risk Score" (WRS), il active des mesures défensives lorsque le risque d'une baisse soudaine et violente augmente.

Il existe deux niveaux d'intervention :

*   **Niveau 1 : Filtre (Risque Élevé)**
    *   **Ce que vous voyez :** Un message "Nouveaux trades LONG désactivés" apparaît sur votre tableau de bord.
    *   **Pourquoi c'est intelligent :** Le système anticipe une possible cascade de liquidations. En suspendant les nouveaux achats, il évite d'entrer sur le marché à un moment de vulnérabilité maximale, vous protégeant ainsi d'un achat juste avant une chute.
*   **Niveau 2 : Disjoncteur (Risque Extrême)**
    *   **Ce que vous voyez :** Une notification vous informe que vos positions LONG ont été clôturées.
    *   **Pourquoi c'est nécessaire :** À ce niveau, le système estime qu'un "flash crash" est imminent. La priorité absolue est la préservation du capital. La clôture active de vos positions est une mesure de dernier recours pour sécuriser vos gains et limiter les pertes avant que le marché ne décroche violemment.

## Pour l'Analyste Quant : La Méthodologie du "Weekend Risk Score" (WRS)

**Le Message Clé :** "Nous avons quantifié 'l'Effet Weekend'. Le système calcule un 'Weekend Risk Score' (WRS) basé sur des prédicteurs de levier (ELR, Divergence OI, Taux de Financement) et des multiplicateurs de magnitude (Squeeze de Volatilité, Gap CME). Cette page explique la logique derrière les actions de filtrage ou de clôture du système."

Le WRS est une métrique propriétaire conçue pour évaluer le risque systémique spécifique aux fins de semaine. Il est calculé le vendredi soir et agrège plusieurs indicateurs clés pour anticiper la fragilité du marché.

### Les Composants du WRS :

1.  **Prédicteurs de Levier :**
    *   **Estimated Leverage Ratio (ELR) :** Un ratio élevé indique un marché sur-endetté, vulnérable à une cascade de liquidations.
    *   **Divergence Open Interest (OI) vs. Prix :** Une divergence où l'OI augmente alors que le prix stagne ou baisse signale une accumulation de positions qui pourraient être liquidées en masse.
    *   **Taux de Financement (Funding Rates) :** Des taux excessivement élevés ou négatifs peuvent indiquer une tension sur le marché du levier.
2.  **Multiplicateurs de Magnitude :**
    *   **Squeeze de Volatilité :** Une période de volatilité extrêmement basse (mesurée par la largeur des bandes de Bollinger, par exemple) précède souvent une expansion violente.
    *   **Gap CME :** La présence d'un "gap" non comblé sur les contrats à terme du CME Bitcoin peut agir comme un aimant sur le prix, augmentant le risque de mouvements brusques à la réouverture des marchés traditionnels.

Le WRS combine ces facteurs pour générer un score de risque. Lorsque ce score dépasse des seuils prédéfinis, le "Disjoncteur Intelligent" active les protocoles de filtrage (Niveau 1) ou de clôture active (Niveau 2) pour gérer l'exposition de manière algorithmique.
