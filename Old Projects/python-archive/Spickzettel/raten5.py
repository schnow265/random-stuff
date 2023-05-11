# Computer muss raten
import random
Regel = "DU denkst dir eine Zahl zwischen 1 und 1000."
print(Regel)
print("Merk sie dir gut! Ich rate:")
Unten = 1
Oben = 1000 
Versuche = 0
Info = ""
while Info != "richtig" :
  Versuche += 1
  Zahl = int((Oben+Unten)/2)
  print(str(Versuche) + ". Versuch: " + str(Zahl))
  print("Ist die Zahl richtig/zu klein/zu groß? ", end="")
  Info = input()
  if Info == "zu klein" :
    Unten = Zahl
  if Info == "zu groß" :
    Oben  = Zahl
  if Info == "richtig" : 
    print("OK - ", end="")
  else :
    print("Schade - ", end="")
print("Das waren " + str(Versuche) + " Versuche.")

