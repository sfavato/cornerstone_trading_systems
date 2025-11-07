from pydantic import BaseModel, Field
from typing import List

class CanonicalTick(BaseModel):
    """
    Represents a single, standardized trade tick from any exchange.
    """
    timestamp: int = Field(..., description="UNIX timestamp of the trade")
    price: float = Field(..., description="Execution price of the trade")
    volume: float = Field(..., description="Volume of the trade")
    side: str = Field(..., description="Side of the aggressor ('buy' or 'sell')")
