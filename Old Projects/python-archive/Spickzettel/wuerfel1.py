# Würfeln
import random, time
print("Lass uns würfeln!")
Versuche = 0
DeinWert = 0
MeinWert = 0
while Versuche < 5 :
  Versuche = Versuche + 1
  print(str(Versuche) + ". Runde")
  print("Du bist dran: ", end="")
  Wurf1 = random.randint(1,6)  # Dein Würfel rollt
  time.sleep(0.5)  #Halbe Sekunde warten
  print(Wurf1)
  print("Ich bin dran: ", end="")
  Wurf2 = random.randint(1,6)  # Mein Würfel rollt
  time.sleep(0.5)  # Halbe Sekunde warten
  print(Wurf2)
  if Wurf1 > Wurf2 :
    DeinWert = DeinWert + 1
  if Wurf1 < Wurf2 :
    MeinWert = MeinWert + 1
  print(str(DeinWert) + " zu " + str(MeinWert))
  time.sleep(1)  #Eine Sekunde warten
  print()
if DeinWert > MeinWert :
  print("Du hast gewonnen")
elif DeinWert < MeinWert :
  print("Ich habe gewonnen")
else :
  print("Unentschieden")

