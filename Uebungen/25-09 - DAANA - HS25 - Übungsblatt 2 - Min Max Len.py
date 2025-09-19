#%% Imports
import pandas as pd

#%% Daten erstellen und in DataFrame zusammenfügen
daten = {
    "Produkt": ["Produkt A", "Produkt B", "Produkt C", "Produkt D", "Produkt E"],
    "Umsatz": [1200, 1500, 1800, 900, 2000]
}

df = pd.DataFrame(daten)
df

#%% Aufgabe 1: Anzahl der Produkte
print(df.count("coulumns"))
print()
#%% Aufgabe 2: Produkt mit dem höchsten Umsatz


#%% Aufgabe 3: Produkt mit dem niedrigsten Umsatz


#%% Aufgabe 4: Summe aller Umsätze


#%% Aufgabe 5: Durchschnittsumsatz pro Produkt


#%% Aufgabe 6: Produkt mit mittlerem Umsatz (Median)
