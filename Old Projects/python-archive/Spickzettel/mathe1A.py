# Mathe
print("Gib mal eine Zahl ein: ", end="")
Zahl1 = int(input())
print ("Und gleich noch eine : ", end="")
Zahl2 = int(input())
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
  print(Zahl1 / Zahl2)
