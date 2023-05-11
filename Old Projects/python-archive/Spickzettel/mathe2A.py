# Mathe
print("Gib mal eine Zahl ein: ", end="")
Zahl1 = float(input())
print ("Und gleich noch eine : ", end="")
Zahl2 = float(input())
print ("Und jetzt den Operator (+,-,*,/): ", end="")
Operator = input()
print ("Ergebnis = ", end="")
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

