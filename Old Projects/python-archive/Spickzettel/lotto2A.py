# Lotto
import random, time
Kugel = []
# Alle Zahlen im "Pott" auf "noch nicht gezogen"
for Nr in range(1,50) :
  Kugel.append(0)
Zufall = random.randint(1,49)
# Sechs Zahlen "ziehen"
for Nr in range(6) :
  # noch nicht verwendete Zufallszahl suchen
  while Kugel[Zufall] == 1 :
    Zufall = random.randint(1,49)
  # Benutzte Zahl als "gezogen" markieren
  Kugel[Zufall] = 1
  print("Nr. " + str(Nr+1) + " => " + str(Zufall))
  time.sleep(2)
  
  

