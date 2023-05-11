import random
Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
Zufall = random.randint(1,1000)
print(Zufall)
print(Regel)
print("Rate mal: ", end="")
Eingabe = int(input())
if Eingabe < Zufall :
  print("Zu klein!")
if Eingabe > Zufall :
  print("Zu groß!")
if Eingabe == Zufall :
  print("Richtig!")

