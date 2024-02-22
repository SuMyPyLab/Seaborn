import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

start_date = '2023-01-01'
end_date = '2023-12-31'

stock_tickers = ['JPM', 'WFC', 'JNJ', 'PG', 'SBIN.NS',
                 'MSFT', 'GOOGL', 'AMZN', 'TCS.NS', 'INFY.NS']

stock_prices = yf.download(stock_tickers, start=start_date, end=end_date)['Adj Close']
stock_prices.dropna(inplace=True)       # Remove the records with NaN values
# calculate daily returns for the stocks
stock_returns = stock_prices.pct_change()
# Let's calculate the correlation matrix
stock_corr = stock_returns.corr()       # correlation matrix for returns
print(stock_corr)
sns.set(font_scale=1.4)
sns.set(style="white")      # background style
ax = sns.heatmap(stock_corr, annot=True, cmap="coolwarm",
            linewidths=0.5, annot_kws={"size" : 20}, fmt="0.2f")
ax.set_title("Stock Returns Heatmap", weight="bold", size=20)
plt.show()

