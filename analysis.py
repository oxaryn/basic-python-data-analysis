import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση δεδομένων
df = pd.read_csv("life_expectancy.csv")

# Καθαρισμός δεδομένων
df_clean = df[["Geographic area", "TIME_PERIOD", "OBS_VALUE"]].copy()
df_clean = df_clean.rename(columns={
    "Geographic area": "Country",
    "TIME_PERIOD": "Year",
    "OBS_VALUE": "LifeExpectancy"
})
df_clean["Year"] = df_clean["Year"].astype(int)

# Βασικά στατιστικά
print(df_clean.head())
print(df_clean["LifeExpectancy"].describe())

# Top 10 χώρες 2023
latest_year = df_clean["Year"].max()
latest = df_clean[df_clean["Year"] == latest_year]
top10 = latest.groupby("Country")["LifeExpectancy"].mean().sort_values(ascending=False).head(10)
print("\nTop 10 countries:")
print(top10)

# Μέσο προσδόκιμο Ελλάδας
greece = latest[latest["Country"] == "Greece"]["LifeExpectancy"].mean()
if pd.notna(greece):
    print(f"\nΜέσο προσδόκιμο ζωής στην Ελλάδα το {latest_year}: {greece:.2f} έτη")
else:
    print("\nΗ Ελλάδα δεν βρέθηκε στο dataset.")

# --- Γράφημα εξέλιξης Ελλάδας ---
greece_df = df_clean[df_clean["Country"] == "Greece"]

plt.figure(figsize=(10,6))
plt.plot(greece_df["Year"], greece_df["LifeExpectancy"], marker='o', color='blue')
plt.title("Εξέλιξη Προσδόκιμου Ζωής στην Ελλάδα (1950-2023)")
plt.xlabel("Έτος")
plt.ylabel("Προσδόκιμο Ζωής (έτη)")
plt.grid(True)
plt.show()

# --- Bar chart Top 10 χώρες ---
top10_countries = top10.sort_values(ascending=True)  # για καλύτερη εμφάνιση στο horizontal bar

plt.figure(figsize=(10,6))
plt.barh(top10_countries.index, top10_countries.values, color='green')
plt.title(f"Top 10 χώρες σε προσδόκιμο ζωής το {latest_year}")
plt.xlabel("Προσδόκιμο Ζωής (έτη)")
plt.ylabel("Χώρα")
plt.grid(axis='x')
plt.show()

plt.savefig("greece_life_expectancy.png")
plt.savefig("top10_countries.png")
