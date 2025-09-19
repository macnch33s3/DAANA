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
print()
#%% Aufgabe 2: Letzter Vorname
svn = df.sort_values(by=["Vorname"])
print(svn)
print()
#%% Aufgabe 3: Körpergrösse von Max
print(df.loc[1, "Körpergrösse"])
print()
#%% Aufgabe 4: Zweitkleinster Nachname (alphabetisch)
snn = df.sort_values(by=["Nachname"])
print(df.loc[2, "Nachname"])
print()
#%% Aufgabe 5: Nachname der grössten Person
# snng = df.sort_values(by="Körpergrösse")
snng = df.loc[df["Körpergrösse"].idxmax(), "Nachname"]
print(snng)
print()
#%% Aufgabe 6: Vorname der kleinsten Person
svnk = df.loc[df["Körpergrösse"].idxmin(), "Vorname"]
print(svnk)
print()