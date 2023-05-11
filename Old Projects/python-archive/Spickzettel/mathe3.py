# Mathe
try :
  print("Gib mal eine Zahl ein: ")
  Zahl1 = float(input())
  print ("Und gleich noch eine : ")
  Zahl2 = float(input())
  print ("Und jetzt den Operator (+,-,*,/): ")
  Operator = input()
  print ("Ergebnis = ")
  if Operator == "+" :
    print(Zahl1 + Zahl2)
  if Operator == "-" :
    print(Zahl1 - Zahl2)
  if Operator == "*" :
    print(Zahl1 * Zahl2)
  if Operator == "/" :
    if Zahl2 != 0:
      print(Zahl1 / Zahl2)
    else:
      print("nicht möglich")
except :
  print("Keine Zahl!")

