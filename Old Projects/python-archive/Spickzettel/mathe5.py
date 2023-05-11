# Zufalls-Mathe
import random
Zahl1 = random.randint(0,50)
Zahl2 = random.randint(1,20)
Operation = random.randint(1,4)
if Operation == 1 :
  Ergebnis = Zahl1 + Zahl2
  Op = " + "
if Operation == 2 :
  Ergebnis = Zahl1 - Zahl2
  Op = " - "
if Operation == 3 :
  Ergebnis = Zahl1 * Zahl2
  Op = " * "
if Operation == 4 :
  Ergebnis = Zahl1 / Zahl2
  Op = " / "
print("Die Aufgabe lautet:")
print(str(Zahl1) + Op + str(Zahl2) + " =")
print("Dein Ergebnis: ", end="")
Eingabe = int(input())
if Eingabe == Ergebnis :
  print("Richtig")
else :
  print("Ergebnis = " + str(Ergebnis))
