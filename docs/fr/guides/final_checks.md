## Vérifications Finales d'Entrée : La Passerelle d'Exécution

Même après qu'un pattern a reçu un Score de Confiance élevé (par exemple, 8/10) et est devenu un "Signal de Trade", le service `monitor_trades` effectue une dernière liste de vérifications avant de placer un ordre. Un signal doit passer *tous* ces filtres :

1.  **Filtre de Score de Confiance :** Le score est-il `> 7` (ou le seuil configuré) ?
2.  **Filtre de Régime de Marché :** Le trade est-il aligné avec la tendance générale du marché ? Le `market_regime_filter.py` bloquera un trade LONG, même s'il a un score élevé, si le marché global est dans un régime de "Tendance Baissière" forte.
3.  **Filtres Contextuels :** Y a-t-il des "drapeaux rouges" immédiats ? Le `funding_rate_filter.py` ou le `liquidation_context_filter.py` peuvent arrêter un trade si les conditions de marché sont dangereusement volatiles ou biaisées.
4.  **Filtre de Gestion des Risques :** Le trade respecte-t-il nos règles internes de Risque/Récompense ? Le `calculation_logic.py` confirme que le stop-loss est valide et calcule une taille de position sûre en fonction de notre capital.

Seul un signal qui passe chaque vérification de cet entonnoir complet — de la Détection à la Pureté, à la Confluence, au Contexte IA et aux Filtres Finaux — aboutira à la passation d'un ordre sur l'échange.
