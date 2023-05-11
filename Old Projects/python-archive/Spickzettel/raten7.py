import random

# Funktionen
def initGame() :
  global Versuche, Eingabe
  Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
  print(Regel)
  Versuche = 0
  Eingabe = 0
def playGame() :
  global Versuche, Eingabe
  Zufall = random.randint(1,1000)
  # print(Zufall)
  while Eingabe != Zufall :
    print("Rate mal: ", end="")
    Eingabe = int(input())
    Versuche += 1
    if Eingabe < Zufall :
      print("Zu klein!")
    if Eingabe > Zufall :
      print("Zu groß!")
    if Eingabe == Zufall :
      print("Richtig!")
def endGame() :
  global Versuche
  print("Du hast " + str(Versuche) + " Mal geraten.")

# Hauptprogramm
initGame()
playGame()
endGame()
