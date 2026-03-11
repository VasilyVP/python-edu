import pandas as pd

df = pd.read_csv("dirty_data.csv")

df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")

median_calories = df["Calories"].median()
df["Calories"] = df["Calories"].fillna(median_calories)

df.dropna(inplace=True)

median_duration = df["Duration"].median()
std_deviation_duration = df["Duration"].std()
max_up_duration = median_duration + 2 * std_deviation_duration
min_down_duration = median_duration - 2 * std_deviation_duration

# iterating over rows and replacing duration values which exceed +/- 2 standard deviations with the median duration
for index, row in df.iterrows():
    if row["Duration"] > max_up_duration or row["Duration"] < min_down_duration:
        df.at[index, "Duration"] = median_duration

df.drop_duplicates(inplace=True)

print(df.to_string())
