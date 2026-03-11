import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")

df_dur_cal = df[["Duration", "Calories"]]

df_dur_cal.dropna(inplace=True)

df_dur_cal.plot(x="Duration", y="Calories", kind="scatter")
plt.title("Calories over Time")
plt.show()

""" df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.title("Maxpulse over Time")
plt.show() """

""" df["Duration"].plot(kind = 'hist')
plt.title("Duration Distribution")
plt.show() """
