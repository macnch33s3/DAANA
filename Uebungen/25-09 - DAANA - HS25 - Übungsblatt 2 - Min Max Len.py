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
#%% Aufgabe 2: Produkt mit dem höchsten Umsatz
max_Umsatz = df.sort_values(by="Umsatz")
print(df.loc[2, "Umsatz"])
print()
#%% Aufgabe 3: Produkt mit dem niedrigsten Umsatz


#%% Aufgabe 4: Summe aller Umsätze


#%% Aufgabe 5: Durchschnittsumsatz pro Produkt


#%% Aufgabe 6: Produkt mit mittlerem Umsatz (Median)
