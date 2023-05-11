# Mittelwert Ganzzahlen
print("Mittelwert bis ", end="")
Summe = 0
Anzahl = int(input())
for Zahl in range(1,Anzahl+1) :
  Summe += Zahl
Mittel = Summe / Anzahl
print("Ergebnis " + str(Mittel))
