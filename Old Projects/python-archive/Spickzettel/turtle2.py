# Turtle-Grafik
from turtle import *
import random

# Fenster einrichten
Breite, Hoehe = 600, 400
Fenster = Screen()
Fenster.title("Turtle")
Fenster.setup(width=Breite, height=Hoehe)

# Zeichnen
for step in range(0,10) :
  forward(random.randint(10,100))
  left(random.randint(60,90))

