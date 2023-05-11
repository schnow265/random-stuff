# Zeit bis zur Million
print("Wie viel Geld willst du anlegen: ")
Kapital = float(input())
print("Wie hoch soll der Zinssatz sein: ")
Prozent = float(input())
print("Und wie lange willst du warten: ")
Laufzeit = int(input())
while Laufzeit > 0 :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen
  Laufzeit -= 1
print("Dann hast du " + str(Kapital) + " Euro")
if Kapital < 1000000 :
  print("Damit bist du aber noch kein Millionär!")
else :
  print("Willkommen im Club der Millionäre!")



