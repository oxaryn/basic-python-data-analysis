import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Load dataset
# ============================
df = pd.read_csv("life_expectancy.csv")

# ============================
# Data cleaning
# ============================
# Keep only the necessary columns and rename them
df_clean = df.rename(columns={
    "Geographic area": "Country",
    "TIME_PERIOD": "Year",
    "OBS_VALUE": "LifeExpectancy"
})[["Country", "Year", "LifeExpectancy"]]

# ============================
# Descriptive statistics
# ============================
print("Life Expectancy Statistics:")
print(df_clean["LifeExpectancy"].describe())

# Last year available
last_year = df_clean["Year"].max()
print(f"\nLast year available: {last_year}")

# ============================
# Top 10 countries (latest year)
# ============================
top10 = (
    df_clean[df_clean["Year"] == last_year]
    .groupby("Country")["LifeExpectancy"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 countries:")
print(top10)

# ============================
# Life Expectancy in Greece
# ============================
greece = df_clean[df_clean["Country"] == "Greece"]

plt.figure(figsize=(10, 5))
plt.plot(greece["Year"], greece["LifeExpectancy"], marker="o", color="blue")
plt.title("Life Expectancy in Greece (1950–2023)")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("greece_life_expectancy.png")
plt.close()

# ============================
# Top 10 Countries Bar Chart
# ============================
plt.figure(figsize=(10, 6))
top10.plot(kind="bar", color="green")
plt.title("Top 10 Countries by Life Expectancy (2023)")
plt.ylabel("Life Expectancy (Years)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top10_countries.png")
plt.close()
