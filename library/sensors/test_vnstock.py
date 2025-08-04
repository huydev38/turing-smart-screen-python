from vnstock import Trading
from stock_price import StockPrice
import pandas as pd

pd.set_option('display.max_columns', None)

trading = Trading(source='VCI')
df = trading.price_board(['VIC'])
stock_price = StockPrice(df['listing']['symbol'].iloc[0], df['match']['match_price'].iloc[0], df['match']['accumulated_volume'].iloc[0], (df['match']['match_price'].iloc[0] - df['match']['reference_price'].iloc[0])/ df['match']['reference_price'].iloc[0] * 100)
print(f"Stock Name: {stock_price.stock_name}")
print(f"Price: {stock_price.price}")
print(f"Volume: {stock_price.volume}")
print(f"Difference: {stock_price.difference}")