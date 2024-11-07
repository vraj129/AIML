import pandas as pd
df = pd.read_csv("path to file")
min_t,max_t = df.price.quantile([0.01,0.999],interpolation="lower")
print(min_t,max_t)
new_df = df[(df.price>=min_t)&(df.price <= max_t)]
print(new_df.shape)
print(new_df.sample(5))