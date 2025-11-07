# Data Models

Our API uses standardized Pydantic models to ensure data consistency and clarity across all endpoints. This approach allows for easy integration and validation on the client-side.

## CanonicalTick

This is the core data model for a single trade tick. It is designed to be a universal representation of a trade, regardless of the source exchange.

```python
--8<-- "temp_src/models/canonical.py"
```
