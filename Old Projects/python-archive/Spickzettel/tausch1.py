# Zahlentausch

def exchange(x1, x2) :
  Tausch = x1
  x1 = x2
  x2 = Tausch
  print ("Tausch : " + str(x1) + " und " + str(x2))

# Hauptprogramm
print("Gib eine Zahl ein: ", end="")
Zahl1 = int(input())
print ("Und noch eine : ", end="")
Zahl2 = int(input())
print ("Vorher : " + str(Zahl1) + " und " + str(Zahl2))
exchange(Zahl1, Zahl2)
print ("Nachher: " + str(Zahl1) + " und " + str(Zahl2))

