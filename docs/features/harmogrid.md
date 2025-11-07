# HarmoGrid: The Superior Entry Strategy

HarmoGrid is a sophisticated entry strategy designed to optimize your execution on harmonic patterns. Rather than relying on a single entry point, HarmoGrid intelligently builds your position across a grid of limit orders, giving you increased control and precision.

## The Value Proposition: Why HarmoGrid?

In a volatile market, entering at the exact price can be a challenge. A trade can come close to your entry point without ever touching it, leaving you on the sidelines. HarmoGrid is the solution.

- **Optimized Average Entry Price**: By spreading out the entries, HarmoGrid aims to achieve a more favorable average position cost (DCA - Dollar Cost Averaging).
- **Reduced Risk of "Missed Trades"**: The grid covers a strategic entry zone, significantly increasing your chances of participating in the expected move.
- **Systematic Approach**: Take the emotion out of the equation. HarmoGrid executes a predefined entry plan with algorithmic discipline.

This is not a traditional grid bot. It is a surgical entry mechanism, designed for the precision of harmonic patterns.

## The "HarmoGrid" Mechanism

When HarmoFinder identifies a trade opportunity compatible with HarmoGrid, it places not one, but **four weighted limit orders** strategically within the potential reversal zone (PRZ).

The distribution is as follows:

- **P_Start (10% of the position)**: The first entry point, to "test" the market.
- **P_True1 (20% of the position)**: Placed at a higher confluence level.
- **P_True2 (30% of the position)**: At the heart of the reversal zone.
- **End_SLG (40% of the position)**: The last line of defense, offering the best potential price before the pattern is invalidated.

### The `GRID_PENDING` Status

As long as these four orders are pending and none have been executed, the status of your trade will be `GRID_PENDING`. This indicates that the system is actively monitoring the market, ready to build your position.

As soon as the first order in the grid is hit, the trade status immediately changes to `in-trade`. Your position is now considered active.

## The Cancellation Logic: An Intelligent Protection

This is the most important point to understand, and it is a feature, not a bug.

**If the trade reaches its first profit target (TP1), the system will automatically cancel all remaining entry orders in the grid.**

**Why?** This is a risk management measure designed to protect you. If the market has already validated the direction of the trade and it is profitable, it is strategically unwise to continue buying (DCA) at less optimal price levels.

Canceling the remaining orders allows you to:

- **Lock in Gains**: The trade is now focused on the exit, not the entry.
- **Avoid Over-Risking**: Prevents increasing the position size on a trade that is already playing out.

Trust the process. This logic is designed to optimize your performance and protect your capital, reflecting HarmoFinder's "Quantified Trust" philosophy.
