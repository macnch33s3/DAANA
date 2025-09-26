#%% Imports
import pandas as pd

#%% Daten erstellen und in DataFrame zusammenfügen
daten = {
    "Produkt": ["Produkt A", "Produkt B", "Produkt C", "Produkt D", "Produkt E"],
    "Umsatz": [1200, 1500, 1800, 900, 2000]
}

df = pd.DataFrame(daten)
print(df)
print()
df

#%% Aufgabe 1: Anzahl der Produkte
Anzahl_Produkte = df["Produkt"].count()
print(Anzahl_Produkte)
print()
#%% Aufgabe 2: Produkt mit dem höchsten Umsatz
# max_Umsatz = df.sort_values(by="Umsatz")
max_Umsatz = df.loc[df["Umsatz"].idxmax(), "Produkt"]
print(max_Umsatz)
#print(df.loc[2, "Umsatz"])
print()
#%% Aufgabe 3: Produkt mit dem niedrigsten Umsatz
min_Umsatz = df.loc[df["Umsatz"].idxmin(), "Produkt"]
print(min_Umsatz)
print()
#%% Aufgabe 4: Summe aller Umsätze
sum = df["Umsatz"].sum()
print(sum)
print()
#%% Aufgabe 5: Durchschnittsumsatz pro Produkt
sum = df["Umsatz"].sum()
mean = sum/df.count()
print(mean)
print()
#%% Aufgabe 6: Produkt mit mittlerem Umsatz (Median)
# mittel = df["Umsatz"].mean()
# print(mittel)
# print()

median = df["Umsatz"].median()
print("Median-Ansatz:", median)
pmedian = df[df["Umsatz"] == median]
print(pmedian)