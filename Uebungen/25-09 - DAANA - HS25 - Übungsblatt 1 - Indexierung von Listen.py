#%% Imports
import pandas as pd

#%% Daten erstellen und in DataFrame zusammenfügen
daten = {
    "Nachname": ["Schmid", "Müller", "Meier", "Schulz", "Lehmann"],
    "Vorname": ["Anna", "Max", "Laura", "Felix", "Sophie"],
    "Körpergrösse": [170, 185, 168, 176, 162]
}

df = pd.DataFrame(daten)

#%% Aufgabe 1: Erster Nachname
snn = df.sort_values(by=["Nachname"])
print(snn)
print(/n)

#%% Aufgabe 2: Letzter Vorname
svn = df.sort_values(by=["Vorname"])
print(svn)
#%% Aufgabe 3: Körpergrösse von Max

#%% Aufgabe 4: Zweitkleinster Nachname (alphabetisch)

#%% Aufgabe 5: Nachname der grössten Person

#%% Aufgabe 6: Vorname der kleinsten Person
