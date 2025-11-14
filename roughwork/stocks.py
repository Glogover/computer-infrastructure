

# Yahoo Finance data.
import yfinance as yf

# Get historical data for multiple tickers at once.
df = yf.download(['MSFT', 'AAPL','GOOG'], period='1mo')
