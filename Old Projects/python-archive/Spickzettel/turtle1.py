# Turtle-Grafik
from turtle import *

# Fenster einrichten
Breite, Hoehe = 600, 400
Fenster = Screen()
Fenster.title("Turtle")
Fenster.setup(width=Breite, height=Hoehe)

# Zeichnen
shape("turtle")
for step in range(0,4) :
  forward(150)
  left(90)


