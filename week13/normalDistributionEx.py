import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
df = pd.read_csv("path to file")
min_t,max_t = df.price_per_sqft.quantile([0.001,0.999])
print(min_t,max_t)
new_df = df[(df.price_per_sqft >= min_t) & (df.price_per_sqft <= max_t)]
print(new_df.head())
print(new_df.describe())
minStd = new_df.price_per_sqft.mean() - 4 * new_df.price_per_sqft.std()
maxStd = new_df.price_per_sqft.mean() + 4 * new_df.price_per_sqft.std()
print(minStd,maxStd)

new_df_v1 = new_df[(new_df.price_per_sqft > minStd) & (new_df.price_per_sqft < maxStd)]
print(new_df_v1.shape)
# sn.histplot(new_df_v1.price_per_sqft,kde=True)
# plt.show()
new_df['zscore'] = (new_df.price_per_sqft - new_df.price_per_sqft.mean())/new_df.price_per_sqft.std()
print(new_df.head())