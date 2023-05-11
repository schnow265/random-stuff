# Summe Ganzzahlen
print("Summe bis ", end="")
Summe = 0
Anzahl = int(input())
for Zahl in range(1,Anzahl+1) :
  Summe += Zahl
print("Ergebnis " + str(Summe))
