# Lotto
import random

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
Lotto.sort()
print(Lotto)

