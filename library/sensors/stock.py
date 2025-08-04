from vnstock import Trading
from stock_price import StockPrice

class StockPrice():
    def __init__(self, stock_names):
        self.stock_names = stock_names

    def fetch_stock_data(self):
        stocks_data = []
        for stock_name in self.stock_names:
            try:
                trading = Trading(source='VCI')
                
                df = trading.price_board([stock_name])
                if not df.empty:
                    difference = (df['match']['match_price'].iloc[0] - df['match']['reference_price'].iloc[0])/ df['match']['reference_price'].iloc[0] * 100
                    stock_data = StockPrice(
                        stock_name=df['listing']['symbol'].iloc[0],
                        price=df['match']['match_price'].iloc[0],
                        volume=df['match']['accumulated_volume'].iloc[0],
                        difference=difference
                    )
                    stocks_data.append(stock_data)
                else:
                    stocks_data.append(None)
            except Exception as e:
                print(f"Error fetching data for {stock_name}: {e}")
        return stocks_data
    

                