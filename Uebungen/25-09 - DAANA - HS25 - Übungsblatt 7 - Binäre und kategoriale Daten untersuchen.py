#%% Imports
import pandas as pd
import seaborn as sns

#%% Daten erstellen
# Klassenspiegel als Datensatz verteilt auf Listen
num_participants = 28

namen = [
    "Müller", "Schmid", "Fischer", "Kunz", "Zürcher",
    "Wüthrich", "Ammann", "Egger", "Gasser", "Wyss",
    "Meier", "Lehmann", "Frei", "Brunner", "Zahnd",
    "Zemp", "Rüegg", "Keller", "Marty", "Hug",
    "Schneider", "Stucki", "Steiner", "Häfliger", "Thüring",
    "Blaser", "Bürgi", "Ziegler"
]
assert len(namen) == num_participants

vornamen = [
    "Hans", "Ruedi", "Sepp", "Beat", "Urs",
    "Reto", "Bruno", "Marcel", "Peter", "Markus",
    "Heiri", None, "Daniel", "Simon", "Thomas",
    "Fritz", "Walter", "Heidi", "Kurt", "Roger",
    "Stefan", "Adrian", "Philipp", "Ruedi", "Toni",
    "Fritz", "Anita", "Christoph"
]
assert len(vornamen) == num_participants

koerpergroessen = [
    191, 171, 178, 171, 170,
    183, 180, 175, 185, 174,
    178, None, 184, 182, 188,
    172, 180, 170, 182, 182,
    180, 184, 174, 185, 187,
    174, 163, 174
]
assert len(koerpergroessen) == num_participants

schuhgroessen = [
    46, 41, 43, 43, 41,
    42, 43, 42, 43, 44,
    43, None, 45, 44, 43,
    43, 43, 39, 44, 42,
    43, 44, 45, 45, 45,
    43, 37, 43
]
assert len(schuhgroessen) == num_participants

alter = [
    28, 28, 28, 24, 24,
    32, 22, 23, 22, 24,
    29, None, 26, 23, 22,
    21, 22, 24, 24, 23,
    27, 39, 24, 21, 23,
    23, 43, 24
]
assert len(alter) == num_participants

augenfarben = [
    "braun", "braun", "grün", "blau", "braun",
    "braun", "blau", "braun", "braun", "blau",
    "braun", None, "braun", "blau", "braun",
    "braun", "blau", "braun", "braun", "braun",
    "grün", "braun", "grün", "blau", "blau",
    "braun", "grün", "grün"
]
assert len(augenfarben) == num_participants

motivation = [
    7, 6, 7, 6, 6,
    6, 7, 9, 7, 8,
    6, None, 6, 7, 7,
    6, 5, 6, 7, 10,
    6, 10, 7, 9, 8,
    7, 8, 6
]
assert len(motivation) == num_participants

data = {
    'Nachname': namen,
    'Vorname': vornamen,
    'Körpergrösse (cm)': koerpergroessen,
    'Schuhgrösse': schuhgroessen,
    'Alter (Jahre)': alter,
    'Augenfarbe': augenfarben,
    'Motivation (1-10)': motivation
}

df = pd.DataFrame(data)
print(df)




#%% Aufgabe 1: Anzahl Einträge je Augenfarbe
# Hint: Nutze `value_counts()`

#%% Aufgabe 2: Balkendiagramm Augenfarbe (einzeilig Seaborn)

#%% Aufgabe 3: Anzahl Teilnehmer pro Schuhgrösse

#%% Aufgabe 4a: Anzahl Teilnehmer je Motivationswert

#%% Aufgabe 4b: Relative Anteile statt Anzahl

#%% Aufgabe 5: Modus der Augenfarbe
