# Smart Reversal Override

## Introduction

The "Smart Reversal Override" is a critical protocol introduced in our November 2025 update (Phase I Closure). It represents a significant leap in our validation logic, moving beyond simple trend following to intelligent counter-trend execution.

## The Problem: Trend vs. Opportunity

Traditional trading bots often fail in two ways:

1.  **Fighting the Trend:** Buying every dip in a crash (catching falling knives).
2.  **Missing the Bottom:** Refusing to buy valid reversals because the "trend is still bearish".

## The Solution: Divergence as Truth

The Smart Reversal mechanism solves this by prioritizing **Divergence** over simple trend direction.

### How It Works

When the Cornerstone Detector identifies a bullish harmonic pattern (e.g., a Bullish Gartley) in a bearish market environment, it doesn't automatically reject it. Instead, it checks for a "Smart Reversal" signal:

1.  **Price Action:** Lower Low (Bearish).
2.  **Oscillator/Momentum:** Higher Low (Bullish).

This divergence indicates that while sellers are pushing price down, the *momentum* of the selling pressure is exhausting.

### The "Override" Logic

Normally, our system filters out long signals if the broader market (BTC Trend) is bearish. However, if a **strong Class A Divergence** is detected alongside a high-confidence harmonic pattern, the Smart Reversal protocol **overrides** the trend filter.

*   **Result:** The system executes the trade, effectively "buying the dip" with high precision just as the trend is about to turn.
*   **Benefit:** This allows Cornerstone Indice to capture high R-Multiple trades at the very start of a new trend, rather than waiting for confirmation when the price is already 10-20% higher.

This feature demonstrates our commitment to sophistication: we don't just follow lines; we measure the underlying energy of the market.
