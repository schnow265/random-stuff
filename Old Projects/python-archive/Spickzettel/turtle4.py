# Turtle-Grafik
from turtle import *

# Fenster einrichten
Breite, Hoehe = 600, 400
Fenster = Screen()
Fenster.title("Turtle")
Fenster.setup(width=Breite, height=Hoehe)
# Rechteck
penup()
goto(-245,150)
pendown()
for step in range(0,2) :
  forward(480)
  right(90)
  forward(290)
  right(90)
# Kreis
penup()
goto(-25,-140)
pendown()
circle(145)

