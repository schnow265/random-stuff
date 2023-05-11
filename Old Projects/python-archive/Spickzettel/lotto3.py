# Lotto
import random
Kugel = []
# Alle Zahlen im "Pott" auf "noch nicht gezogen"
for Nr in range(1,50) :
  Kugel.append(False)
Zufall = random.randint(1,49)
# Sechs Zahlen "ziehen"
for Nr in range(6) :
  # noch nicht verwendete Zufallszahl suchen
  while Kugel[Zufall] :
    Zufall = random.randint(1,49)
  # Benutzte Zahl als "gezogen" markieren
  Kugel[Zufall] = True
  print("Nr. " + str(Nr+1) + " => " + str(Zufall))
  

