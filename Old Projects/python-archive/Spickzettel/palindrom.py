# Palindrom?

print("Schreib was (nur klein, ohne Leerzeichen: ")
Text1 = input()
Text2 = ""
Kette = len(Text1)
for Nr in range(0, Kette) :
  Text2 += Text1[Kette-Nr-1]
print(Text2)
if Text1 == Text2 :
  print ("Palindrom")


