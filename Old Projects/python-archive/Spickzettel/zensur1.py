# Zensuren
print("Gib deine Punkte ein: ", end="")
Punkte = int(input())
print("Das ist ", end = "")
if (Punkte >= 0) and (Punkte < 25) :
  print("ungenügend (6)")
if (Punkte >= 25) and (Punkte < 45) :
  print("mangelhaft (5)")
if (Punkte >= 45) and (Punkte < 65) :
  print("ausreichend (4)")
if (Punkte >= 65) and (Punkte < 80) :
  print("befriedigend (3)")
if (Punkte >= 80) and (Punkte < 90) :
  print("gut (2)")
if (Punkte >= 90) and (Punkte <= 100) :
  print("sehr gut (1)")
if (Punkte > 100) or (Punkte < 0) :
  print("ungültig (0)")
