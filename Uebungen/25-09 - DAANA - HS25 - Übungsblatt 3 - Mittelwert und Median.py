#%% Imports
import pandas as pd

#%% Daten erstellen und in DataFrame zusammenfügen
namen = ["PowerRacer", "SpeedDemon", "TurboCharge", "SuperVelocity", "ThunderBolt"]
leistungen_ps = [200, 250, 180, 600, 220]

autos = pd.DataFrame({
    "Name": namen,
    "Leistung_PS": leistungen_ps
})

autos


#%% Aufgabe 1: Durchschnitt der Leistungen berechnen
print(autos)
mittel = autos["Leistung_PS"].mean()
print()
print(mittel)
print()
#%% Aufgabe 2: Median der Leistungen berechnen
median = autos["Leistung_PS"].median()
print(median)
print()
#%% Aufgabe 3: Auto mit der niedrigsten Leistung finden
min_Leistung = autos.loc[autos["Leistung_PS"].idxmin(), "Name"]
print(min_Leistung)
print()
#%% Aufgabe 4: Auto mit der höchsten Leistung finden
max_Leistung = autos.loc[autos["Leistung_PS"].idxmax(), "Name"]
print(max_Leistung)
print()