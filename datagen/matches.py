import random
import os
import csv
import argparse
import matplotlib.pyplot as plt
import time
import configparser

# Konfiguration
num_simulations = 30
num_players = 3
result_file = "ergebnis.csv"

config = configparser.ConfigParser()
config.read('matches.conf')

num_players = config.getint('GAME', 'players')
num_games = config.getint('GAME', 'games')

# Spiel-Simulation
start_time = time.time()
results = []
for i in range(num_simulations):
    sticks = ["lang"] * num_players
    sticks.append("kurz")
    random.shuffle(sticks)
    loser = sticks.index("kurz") + 1
    results.append(loser)
    print(f"In Runde {i+1} hat Spieler {loser} den kürzeren gezogen.")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Laufzeit: {elapsed_time:.2f} Sekunden")

# Ergebnis in CSV-Datei speichern
with open(result_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ergebnis"])
    for loser in results:
        writer.writerow([loser])

# Diagramm generieren, falls -genplot gesetzt wurde
parser = argparse.ArgumentParser()
parser.add_argument("-genplot", action="store_true")
args = parser.parse_args()

if config['DATA'].getboolean('genplot', fallback=False):
    # Ergebnisse gruppieren und zählen
    with open(result_file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Spaltenüberschriften überspringen
        results_dict = {}
        for row in reader:
            result = int(row[0])
            if result in results_dict:
                results_dict[result] += 1
            else:
                results_dict[result] = 1

    # Diagramm erstellen
    counts = []
    for i in range(1, num_players+1):
        if i in results_dict:
            counts.append(results_dict[i])
        else:
            counts.append(0)
    plt.bar(range(1, num_players+1), counts)
    plt.title("Mach of Matches")
    
    # Maximalwert
    max_value = max(counts)
    max_index = counts.index(max_value)
    text = f"Maximalwert: {max_value}, Spieler {max_index+1}"
    plt.text(max_index+0.5, max_value*0.9, text, ha="center", va="center")
    
    plt.xticks(range(1, num_players+1), [f"Spieler {i}" for i in range(1, num_players+1)])
    plt.ylabel("Anzahl der kurzen Streichhölzer")
    plt.show()
