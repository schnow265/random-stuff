# Zeit bis zur Million
print("Wie viel Geld willst du anlegen: ")
Kapital = float(input())
print("Wie hoch soll der Zinssatz sein: ")
Prozent = float(input())
print("Und wie lange willst du warten: ")
Laufzeit = int(input())
for Anzahl in range(Laufzeit) :
  Zinsen   = Kapital * Prozent / 100
  Kapital  = Kapital + Zinsen
print("Dann hast du " + str(Kapital) + " Euro")
if Kapital < 1000000 :
  print("Damit bist du aber noch kein Millionär!")
else :
  print("Willkommen im Club der Millionäre!")



