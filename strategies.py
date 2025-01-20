# strategies.py
class GridBot:
    def __init__(self, exchange, symbol, grid_levels, lower_price, upper_price):
        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.lower_price = lower_price
        self.upper_price = upper_price
        self.grid_spacing = (upper_price - lower_price) / grid_levels

    def execute_grid(self):
        for i in range(self.grid_levels):
            price = self.lower_price + i * self.grid_spacing
            amount = 1  # Adjust amount
            self.exchange.create_order(self.symbol, 'limit', 'buy', amount, price)

class DCABot:
    def __init__(self, exchange, symbol, dca_intervals, total_investment):
        self.exchange = exchange
        self.symbol = symbol
        self.dca_intervals = dca_intervals
        self.total_investment = total_investment
        self.amount_per_interval = total_investment / dca_intervals

    def execute_dca(self):
        for _ in range(self.dca_intervals):
            self.exchange.create_order(self.symbol, 'market', 'buy', self.amount_per_interval)
