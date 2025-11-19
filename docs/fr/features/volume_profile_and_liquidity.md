# Volume Profile & Données de Liquidité : Connaître les Flux de Capitaux

Pour notre système, le prix seul ne suffit pas. Une analyse robuste doit impérativement intégrer la connaissance des **flux de capitaux** et de la **liquidité** du marché. C'est pourquoi nous utilisons le Volume Profile et les données de dérivés comme des filtres essentiels pour valider la pertinence d'un pattern harmonique.

## Le Volume Profile : Identifier les Zones de Forte Accumulation

Le **Volume Profile** est un outil d'analyse avancé qui affiche le volume total négocié à chaque niveau de prix sur une période donnée. Contrairement au volume traditionnel (qui est basé sur le temps), le Volume Profile nous montre "où" l'activité a eu lieu.

Nous utilisons trois points de données clés du Volume Profile pour valider nos signaux :

-   **Point of Control (PoC) :** Le niveau de prix où le plus grand volume a été échangé. C'est le "juste prix" perçu par le marché et il agit comme un puissant aimant ou une zone de réjection.
-   **Value Area High (VAH) :** Le niveau de prix le plus élevé de la "zone de valeur" (où ~70% du volume a eu lieu).
-   **Value Area Low (VAL) :** Le niveau de prix le plus bas de la "zone de valeur".

Un pattern harmonique dont le point d'entrée (point D) coïncide avec l'un de ces trois niveaux a une probabilité de succès bien plus élevée. Cela signifie que le retournement attendu se produit dans une zone où le marché a déjà montré un intérêt significatif, rendant le niveau plus difficile à franchir.

## Données de Dérivés : Mesurer la Faiblesse Systémique (Alpha Exotique)

Les données de dérivés (comme les contrats à terme et les options) nous donnent un aperçu de la **spéculation** et du **positionnement des acteurs du marché**. Nous intégrons ces données en tant qu'**Alpha Exotique** pour mesurer la "faiblesse systémique" du marché, un facteur de filtrage crucial pour notre Score de Confiance.

Les métriques clés que nous analysons sont :

-   **Liquidations :** Lorsque des positions à effet de levier sont fermées de force, cela crée une pression d'achat ou de vente soudaine. Nous surveillons les niveaux de prix où se concentrent les larges pools de liquidations. Un pattern qui se forme juste avant un de ces niveaux a une plus grande chance d'être "poussé" par la cascade de liquidations.
-   **Open Interest (OI) :** L'intérêt ouvert total sur les contrats dérivés. Une forte augmentation de l'OI dans une tendance peut signaler un sur-levier et un épuisement potentiel.

En intégrant ces données, notre système ne se contente pas de trouver une belle "forme" géométrique ; il s'assure que le contexte des flux de capitaux et de la liquidité est également favorable. C'est une étape essentielle pour éviter les "pièges" du marché où un pattern semble parfait mais échoue en raison de conditions de marché sous-jacentes défavorables.
