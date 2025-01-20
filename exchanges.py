import ccxt
from decouple import config

class ExchangeConnector:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.api_key = config(f"{exchange_name.upper()}_API_KEY")
        self.api_secret = config(f"{exchange_name.upper()}_API_SECRET")
        self.exchange = getattr(ccxt, exchange_name)({
            'apiKey': self.api_key,
            'secret': self.api_secret,
        })

    def get_balance(self, symbol):
        try:
            balance = self.exchange.fetch_balance()
            if symbol in balance and 'free' in balance[symbol] and 'total' in balance[symbol]:
                return {
                    'free': balance[symbol]['free'],
                    'used': balance[symbol]['used'],
                    'total': balance[symbol]['total']
                }
            else:
                raise KeyError(f"Symbol {symbol} not found in the account or insufficient data.")
        except Exception as e:
            raise Exception(f"Failed to fetch balance: {str(e)}")

    def get_total_balance_in_usdt(self):
        try:
            balance = self.exchange.fetch_balance()
            tickers = self.exchange.fetch_tickers()
            total_usdt = 0.0

            for asset, asset_data in balance['total'].items():
                if asset_data > 0:  # Only consider assets with a positive balance
                    if asset == 'USDT':
                        total_usdt += asset_data
                    else:
                        symbol = f"{asset}/USDT"
                        ticker = tickers.get(symbol)
                        if ticker and ticker['last'] is not None:
                            total_usdt += asset_data * ticker['last']
                        else:
                            print(f"Skipping asset {asset}: Price data unavailable.")
            return total_usdt
        except Exception as e:
            raise Exception(f"Failed to calculate total balance in USDT: {str(e)}")

    def create_order(self, symbol, order_type, side, amount, price=None):
        try:
            if order_type == 'limit':
                return self.exchange.create_limit_order(symbol, side, amount, price)
            elif order_type == 'market':
                return self.exchange.create_market_order(symbol, side, amount)
            else:
                raise ValueError("Invalid order type. Use 'limit' or 'market'.")
        except Exception as e:
            raise Exception(f"Failed to create order: {str(e)}")
