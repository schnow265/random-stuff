# Turtle-Grafik
from turtle import *

# Fenster einrichten
Breite, Hoehe = 600, 400
Fenster = Screen()
Fenster.title("Turtle")
Fenster.setup(width=Breite, height=Hoehe)

# Zeichnen
Strecke = 5 
Winkel = 45
while Winkel > 28 :
  Strecke += 2
  Winkel -= 0.2
  left(Winkel)
  forward(Strecke)
Winkel = 0
for Nr in range(1,13) :
  Winkel += 30
  home()
  left(Winkel)
  forward(500)
  forward(-500)
