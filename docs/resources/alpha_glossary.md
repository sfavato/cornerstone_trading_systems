# Alpha Glossary

This glossary defines the core "alpha" metrics that our system uses to generate and validate signals. Understanding these concepts is critical for getting the most out of HarmoFinder.

!!! note "Cumulative Volume Delta (CVD)"
    CVD is the core of our order flow analysis. It is a running total of the difference between buying and selling volume. A rising CVD indicates net buying pressure, while a falling CVD indicates net selling pressure. A **divergence** between price and CVD is a powerful signal that often precedes a reversal.

!!! note "Open Interest (OI)"
    Open Interest represents the total number of outstanding derivative contracts (futures or options) that have not been settled. Rising OI indicates new money flowing into the market, while falling OI suggests that positions are being closed. It provides insight into the strength and conviction behind a price move.

!!! note "Funding Rates"
    Funding Rates are periodic payments made between traders to keep the price of a perpetual futures contract in line with the underlying spot price. High positive funding rates suggest that a majority of traders are long and are paying a premium to maintain their positions, which can be a contrarian indicator. Conversely, high negative rates suggest a bearish sentiment.
