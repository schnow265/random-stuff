# Millionär?
print("Wie viel Geld willst du anlegen: ", end="")
Kapital = float(input())
print("Wie hoch soll der Zinssatz sein: ", end="")
Prozent = float(input())
Laufzeit = 0
while Kapital < 1000000 :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen
  Laufzeit += 1
if Laufzeit > 0 :
  print("Um Millionär zu werden, musst du das Geld ", end="")
  print(str(Laufzeit) + " Jahre auf der Bank braten lassen.")
else :
  print("Willkommen im Club der Millionäre!")
