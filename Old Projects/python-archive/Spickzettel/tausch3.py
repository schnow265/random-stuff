# Stringtausch

def exchange(x1, x2) :
  Tausch = x1
  x1 = x2
  x2 = Tausch
  print ("Tausch : " + str(x1) + " und " +str(x2))
  return x1, x2

# Hauptprogramm
print("Gib ein Wort ein: ", end="")
Wort1 = input()
print ("Und noch eins : ", end="")
Wort2 = input()
print ("Vorher : " + Wort1 + " und " + Wort2)
Wort1, Wort2 = exchange(Wort1, Wort2)
print ("Nachher: " + Wort1 + " und " + Wort2)

