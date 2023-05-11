import random
Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
Zufall = random.randint(1,1000)
print(Regel)
Versuche = 0
Eingabe = 0
while Eingabe != Zufall :
  print("Rate mal: ", end="")
  Eingabe = int(input())
  if Eingabe == 0 :
    print("Die richtige Zahl ist " + str(Zufall))
    break
  Versuche = Versuche + 1
  if Eingabe < Zufall :
    print("Zu klein!")
  if Eingabe > Zufall :
    print("Zu groß!")
  if Eingabe == Zufall :
    print("Richtig!")
print("Du hast " + str(Versuche) + " Mal geraten.")


