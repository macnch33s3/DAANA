#%% Daten der Teilnehmer:innen
import pandas as pd

df = pd.DataFrame({
"nachnamen": ["Müller", "Schmid", "Meier", "Schneider", "Fischer", "Weber"],
"vornamen":["Anna", "Ben", "Clara", "David", "Eva", "Felix"],
"koerpergroessen": [164, 172, 168, 180, 174, 182],
"schuhgroessen": [38, 42, 40, 44, 41, 45],
"alter": [22, 43, 22, 21, 24, 22],
"augenfarben": ["blau", "grün", "braun", "braun", "blau", "grau"]
})
# %% Aufgabe 1: Erstelle einen DataFrame und gib ihn in der Konsole aus.
print(df)
print()
# %% Aufgabe 2: Zeige die ersten 2 Zeilen des Datensatzes an
sec_rows = df.loc[[0, 1]]
print(sec_rows)
print()
#%% Aufgabe 3: Greife auf die Spalte "Körpergrösse" zu und drucke sie aus
koegr = df["koerpergroessen"]
print(koegr)
print()
#%% Aufgabe 4: Greife auf die Spalten "Name" und "Alter (Jahre)" zu und drucke sie aus
vn_alt = df[["vornamen", "alter"]]
print(vn_alt)
print()
#%% Aufgabe 5: Zeige die Anzahl der Zeilen und Spalten im Datensatz an
z_sp = df.shape
print(z_sp)
print()
#%% Zusatz: Was erwartest du auf der Konsole, wenn du df.head(2).shape ausführst?
# Die ersten 2 Zeilen des Dataframes werden ausgegeben
#%% Aufgabe 6: Drucke Vorname und Körpergrösse der grössten Person auf die Konsole
groesste_Person = df.loc[df["koerpergroessen"].idxmax(), ["vornamen", "koerpergroessen"]]
print(groesste_Person)
print()
#%% Aufgabe 7: Älteste und jüngste Person und ihre Namen
a_Person = df.loc[df["alter"].idxmax(), ["vornamen", "nachnamen"]]
j_Person = df.loc[df["alter"].idxmin(), ["vornamen", "nachnamen"]]
print(*a_Person)
print(*j_Person)
print()
#%% Aufgabe 8: Durchschnitt und Median der Schuhgrösse
groesse = "schuhgroessen"
m = df[groesse].mean()
d = df[groesse].median()
print(f'{groesse} median: {m}')
print(f'{groesse} durchscnitt: {d}')
print()
#%% Aufgabe 9: Durchschnitt und Median des Alters
groesse = "alter"
m = df[groesse].mean()
d = df[groesse].median()
print(f'{groesse} median: {m}')
print(f'{groesse} durchscnitt: {d}')
print()
#%% Zusatzaufgabe: Welche Masszahl ist aussagekräftiger?
# Der Median ist aussagekräftiger, da er weniger empfindlich auf Ausreisser reagiert und mit Ben ein altersmässiger Ausreisser in der Gruppe ist.