import pandas as pd

df = pd.read_csv("data.csv")

pearsCorr = df.corr(method="pearson")
print("Pearson Correlation:\n", pearsCorr)

spearmanCorr = df.corr(method="spearman")
print("Spearman Correlation:\n", spearmanCorr)
