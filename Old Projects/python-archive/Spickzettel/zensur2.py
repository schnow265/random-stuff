# Zensuren
print("Gib deine Punkte ein: ", end="")
Punkte = int(input())
print("Das ist ", end = "")
if (Punkte >= 0) and (Punkte < 1) :
  print("ungenügend (6)")
if (Punkte >= 1) and (Punkte < 4) :
  print("mangelhaft (5)")
if (Punkte >= 4) and (Punkte < 7) :
  print("ausreichend (4)")
if (Punkte >= 7) and (Punkte < 10) :
  print("befriedigend (3)")
if (Punkte >= 10) and (Punkte < 13) :
  print("gut (2)")
if (Punkte >= 13) and (Punkte <= 15) :
  print("sehr gut (1)")
if (Punkte > 15) or (Punkte < 0) :
  print("ungültig (0)")
