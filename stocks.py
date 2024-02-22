import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("stock_prices.csv", index_col="Date")
df.dropna(inplace=True)     # Drop the rows that have NaN values
corr_df = df.corr()         # correlation matrix
# that is, correlation coefficients of all the columns in a matrix format
sns.heatmap(corr_df, annot=True, cmap='Blues')
plt.show()
