#%% Imports
import pandas as pd

#%% Daten erstellen und DataFrame aufbauen
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

klassenspiegel = pd.DataFrame({
    'Nachname': namen,
    'Vorname': vornamen,
    'Körpergrösse': koerpergroessen,
    'Schuhgrösse': schuhgroessen,
    'Alter': alter,
    'Augenfarbe': augenfarben,
    'Motivation': motivation
})

klassenspiegel

#%% Aufgabe 1: Größte Person

#%% Aufgabe 2: Spannweite der Körpergrößen

#%% Aufgabe 3: Mittelwert und Median der Körpergrößen

#%% Aufgabe 4: Quantile/Perzentile der Körpergröße

#%% Aufgabe 5: Varianz der Körpergrößen

#%% Aufgabe 6: Standardabweichung der Körpergrößen

#%% Aufgabe 7: Wiederhole die Rechnungen mit den anderen metrischen Variablen.

#%% Aufgabe 8: Stelle sicher, dass du alle verwendeten Lagemasse und Streuungsmasse verstanden hast.
