# Alter
print("Hallo, ich bin dein PC und nicht mal 5 Jahre alt.")
print("Wie alt bist du eigentlich? ")
Alter = int(input())
if (Alter > 0) and (Alter <= 15) :
  print("Dann bist du ja noch grün hinter den Ohren")
if (Alter > 15) and (Alter <= 25) :
  print("Also noch schön knackig und frisch")
elif (Alter > 25) and (Alter <= 40) :
  print("Also bestes Mittelalter")
elif (Alter > 40) and (Alter <= 65) :
  print("Auf dem Weg zur Rente")
elif (Alter > 65) and (Alter <= 80) :
  print("Eigentlich schon unbezahlbar für die Jugend")
else :
  print("Da bist du ja schon " + str(Alter-80) + " Jahre überfällig")


