# Millionär?
import random
Kapital = random.randint(2,10)*10000
print("Du hast im Lotto " + str(Kapital) + " Euro gewonnen!")
print("Das solltest du nicht gleich verprassen, ", end="")
print("sondern lieber mit Zinsen anlegen!")
print("Wie hoch soll der Zinssatz sein: ", end="")
Prozent = float(input())
Laufzeit = 0
while Kapital < 1000000 :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen
  Laufzeit += 1
print("Zum Millionär brauchst du ", end="")
print(str(Laufzeit) + " Jahre.")
