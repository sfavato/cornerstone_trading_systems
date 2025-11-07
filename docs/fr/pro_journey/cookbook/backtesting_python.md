# Backtester les Signaux HarmoFinder avec `backtrader`

Ce guide fournit un exemple pratique et concret sur la manière de backtester les signaux générés par HarmoFinder en utilisant la populaire bibliothèque Python, `backtrader`.

## La `bt.Strategy`

Voici une `bt.Strategy` complète qui démontre comment consommer un CSV de signaux HarmoFinder et exécuter un backtest simple.

```python
import backtrader as bt
import pandas as pd

class HarmoFinderStrategy(bt.Strategy):
    params = (
        ('signals_csv', 'harmofinder_signals.csv'),
    )

    def __init__(self):
        # Charger les signaux depuis le CSV
        self.signals = pd.read_csv(self.p.signals_csv, index_col='timestamp', parse_dates=True)
        self.order = None

    def next(self):
        # Vérifier si nous avons un ordre en cours
        if self.order:
            return

        # Vérifier s'il y a un signal pour la bougie actuelle
        if self.datas[0].datetime.date(0) in self.signals.index:
            signal_row = self.signals.loc[self.datas[0].datetime.date(0)]
            if signal_row['action'] == 'buy':
                self.order = self.buy()
            elif signal_row['action'] == 'sell':
                self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Ordre d'achat/vente soumis/accepté par le courtier - Rien à faire
            return

        # Vérifier si un ordre a été complété
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'ACHAT EXÉCUTÉ, {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'VENTE EXÉCUTÉE, {order.executed.price:.2f}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Ordre Annulé/Marge/Rejeté')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f'PROFIT DE L\'OPÉRATION, BRUT {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')
```
