# UX Content for HarmoGrid

## Tooltips

### 1. `GRID_PENDING` Status
**Text:** "The system has placed a grid of 4 entry orders. The status will change to 'in-trade' as soon as the first order is executed."

### 2. `grid_order_ids` List
**Text:** "These are the IDs of the 4 limit orders in the HarmoGrid. The system is building the position through these entry points."

## FAQ Entries

### 1. Why did my trade place 4 entry orders?
**Answer:** Your trade is using the HarmoGrid strategy. This is an advanced entry mechanism that spreads your entry point across four weighted limit orders. The goal is to achieve a better average entry price and increase the chances of your trade being executed, even in a volatile market.

### 2. My trade was profitable and hit TP1. Why did the bot cancel my other entry orders?
**Answer:** This is an intentional protective feature of the HarmoGrid strategy. When your trade is already profitable (TP1 is hit), the system cancels the remaining entry orders to avoid buying an asset that is already in the process of being sold. This is a risk management measure that secures your gains and protects your capital.
