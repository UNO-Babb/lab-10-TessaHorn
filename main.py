#MapPlot.py
#Name: Tessa Horn
#Date:
#Assignment:

import astronauts
import pandas as pd
import matplotlib.pyplot as plt

data = astronauts.get_mission()

df = pd.DataFrame(data)

df_clean = pd.DataFrame({
    "Name": df["Profile"].apply(lambda x: x.get("Name")),
    "BirthYear": df["Profile"].apply(lambda x: x.get("Birth Year")),
    "Nationality": df["Profile"].apply(lambda x: x.get("Nationality"))
})

df_clean = df_clean.dropna(subset=["BirthYear", "Nationality"])

plt.switch_backend("Agg")

plt.figure(figsize=(10,6))
df_clean["Nationality"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Nationalities of Astronauts")
plt.xlabel("Nationality")
plt.ylabel("Number of Astronauts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph1.png")

plt.figure(figsize=(10,6))
plt.hist(df_clean["BirthYear"], bins=20)
plt.title("Distribution of Astronaut Birth Years")
plt.xlabel("Birth Year")
plt.ylabel("Number of Astronauts")
plt.tight_layout()
plt.savefig("graph2.png")

plt.figure(figsize=(10,6))
df_clean.groupby("Nationality")["BirthYear"].mean().sort_values().head(10).plot(kind="bar")
plt.title("Average Birth Year by Nationality (Top 10)")
plt.xlabel("Nationality")
plt.ylabel("Average Birth Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph3.png")
