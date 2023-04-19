import random
import os
import csv
import argparse
import matplotlib.pyplot as plt
import time
import configparser

# Konfiguration
config = configparser.ConfigParser()
config.read('matches.conf')


# Input Variables
num_players = config.getint('INPUT', 'players', fallback=3)
num_simulations = config.getint('INPUT', 'games', fallback=30)

# Working with se Data
verbose_output = config.getboolean('DEBUG', 'verbose_output', fallback=False)
runtime_out = config.getboolean('DEBUG', 'runtime', fallback=True)
cvs_verdict = config.getboolean('DATA', 'removeCSV', fallback=False)
result_file = config.get('DATA', 'result_file', fallback='results.csv')


# Spiel-Simulation
start_time = time.time()
results = []
for i in range(num_simulations):
    sticks = ["lang"] * num_players
    sticks.append("kurz")
    random.shuffle(sticks)
    loser = sticks.index("kurz") + 1
    results.append(loser)
    if verbose_output:
        print(f"Round {i+1} lost Player {loser}.")

end_time = time.time()
elapsed_time = end_time - start_time

if runtime_out:
    print(f"Runtime: {elapsed_time:.2f} seconds")

# Ergebnis in CSV-Datei speichern
with open(result_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Result"])
    for loser in results:
        writer.writerow([loser])

if config.getboolean('DATA', 'genplot', fallback=False) or args.genplot:
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
    plt.title("Match of Matches")

    # Maximalwert
    max_value = max(counts)
    max_index = counts.index(max_value)
    text = f"Hightest Value: {max_value}, Player {max_index+1}"
    plt.text(max_index+0.5, max_value*0.9, text, ha="center", va="center")

    plt.xticks(range(1, num_players+1), [f"Player {i}" for i in range(1, num_players+1)])
    plt.ylabel("Times the short match has been chosen.")
    plt.show()

if cvs_verdict:
    os.remove(result_file)
