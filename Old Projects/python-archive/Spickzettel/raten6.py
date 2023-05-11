import random, time
Regel = "Der PC denkt und rät"
Zufall = random.randint(1,1000)
print(Regel)
print("Zahl: " + str(Zufall))
Unten = 1
Oben = 1000 
Versuche = 0
Zahl = 0
while Zufall != Zahl :
  Versuche = Versuche + 1
  Zahl = Zahl = int((Oben+Unten)/2)
  time.sleep(1)
  print(str(Versuche) + ". Versuch: " + str(Zahl))
  if Zahl < Zufall : 
    print("zu klein")
    Unten = Zahl
  if Zahl > Zufall :
    print("zu groß")
    Oben  = Zahl
print("Richtig nach " + str(Versuche) + " Versuchen.")
