# Lotto
import random

# Funktionen
def exchange(x1, x2) :
  Tausch = x1
  x1 = x2
  x2 = Tausch
  return x1, x2
def bubblesort(x, Index) :
  for i in range(Index) :
    for j in range(Index-i-1) :
      if x[j] > x[j+1] :
        x[j], x[j+1] = exchange(x[j], x[j+1]);

# Hauptprogramm
Kugel = []
Lotto = [0,0,0,0,0,0]
# Alle Zahlen im "Pott" auf "noch nicht gezogen"
for Nr in range(1,50) :
  Kugel.append(False)
Zufall = random.randint(1,49)
# Sechs Zahlen "ziehen"
for Nr in range(6) :
  # noch nicht verwendete Zufallszahl suchen
  while Kugel[Zufall] :
    Zufall = random.randint(1,49)
  # Benutzte Zahl als "gezogen" markieren und merken
  Kugel[Zufall] = True
  Lotto[Nr] = Zufall
# Sortieren und anzeigen
bubblesort(Lotto,6)
for Nr in range(6) :
  print("Nr. " + str(Nr+1) + " => " + str(Lotto[Nr]))
