# Modèles de Données

Notre API utilise des modèles Pydantic standardisés pour garantir la cohérence et la clarté des données sur tous les points d'accès. Cette approche permet une intégration et une validation faciles côté client.

## CanonicalTick

C'est le modèle de données de base pour un seul tick de trade. Il est conçu pour être une représentation universelle d'un trade, quelle que soit la bourse d'origine.

```python
--8<-- "temp_src/models/canonical.py"
```
