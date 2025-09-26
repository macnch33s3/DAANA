# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', None)

# %%
# Aufgaben 1-3: Korrelation mit Beispieldaten

# Beispiel-Daten erstellen
data = {'Variable1': [1, 2, 3, 4, 5],
        'Variable2': [1, 1, 1, 1, 2],
        'Variable3': [5, 4, 3, 2, 1],
        'Variable4': [2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

# Korrelationsmatrix berechnen
correlation_matrix = df.corr()

# Ausgabe der Korrelationsmatrix
print(correlation_matrix)

# %%
# Aufgabe 2: Heatmap der Korrelationsmatrix

# %%
# Aufgabe 3: Scatterplot Variable1 vs Variable2

# %%
# Aufgaben 4-6: Korrelation mit dem Klassenspiegel

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

vornamen = [
    "Hans", "Ruedi", "Sepp", "Beat", "Urs",
    "Reto", "Bruno", "Marcel", "Peter", "Markus",
    "Heiri", None, "Daniel", "Simon", "Thomas",
    "Fritz", "Walter", "Heidi", "Kurt", "Roger",
    "Stefan", "Adrian", "Philipp", "Ruedi", "Toni",
    "Fritz", "Anita", "Christoph"
]

koerpergroessen = [
    191, 171, 178, 171, 170,
    183, 180, 175, 185, 174,
    178, None, 184, 182, 188,
    172, 180, 170, 182, 182,
    180, 184, 174, 185, 187,
    174, 163, 174
]

schuhgroessen = [
    46, 41, 43, 43, 41,
    42, 43, 42, 43, 44,
    43, None, 45, 44, 43,
    43, 43, 39, 44, 42,
    43, 44, 45, 45, 45,
    43, 37, 43
]

alter = [
    28, 28, 28, 24, 24,
    32, 22, 23, 22, 24,
    29, None, 26, 23, 22,
    21, 22, 24, 24, 23,
    27, 39, 24, 21, 23,
    23, 43, 24
]

augenfarben = [
    "braun", "braun", "grün", "blau", "braun",
    "braun", "blau", "braun", "braun", "blau",
    "braun", None, "braun", "blau", "braun",
    "braun", "blau", "braun", "braun", "braun",
    "grün", "braun", "grün", "blau", "blau",
    "braun", "grün", "grün"
]

motivation = [
    7, 6, 7, 6, 6,
    6, 7, 9, 7, 8,
    6, None, 6, 7, 7,
    6, 5, 6, 7, 10,
    6, 10, 7, 9, 8,
    7, 8, 6
]

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

# %%
# Aufgabe 4: Korrelationsmatrix für numerische Spalten

# %%
# Aufgabe 5: Heatmap der Klassenspiegel-Korrelation

# %%
# Aufgabe 6: Scatterplot Körpergrösse vs Schuhgrösse

# %%
# Aufgabe 7: Scatterplot Alter vs Schuhgrösse
