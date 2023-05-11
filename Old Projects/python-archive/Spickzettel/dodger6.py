# Pygame Dodger
import pygame as pg
import random
from dplayer import *
from dthing import *
from game import *

# Startwerte festlegen
Red = (255,0,0)
Blue = (0,0,255)
Yellow = (255,255,0)
xMax, yMax = 800, 400

# Pygame starten, Spiel-Elemente erzeugen
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Fenster = pg.display.set_mode((xMax, yMax))
Figur = Player(20,30)
Ball = Thing("Bilder/ball1.png")
Ball.setPosition(xMax-50, yMax/2, True)
Spiel = Game(Yellow)

# Ereignis-Schleife
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False

    # Tasten abfragen
    if event.type == pg.KEYDOWN :
      if event.key == pg.K_UP :
        Figur.setState(2)
        Spiel.getTime(True)
      if event.key == pg.K_DOWN :
        Figur.setState(1)
        Spiel.getTime(True)
        
  # Zeit testen, ggf. Figur zurück in Stand
  Zeit = Spiel.getTime(False)
  if Zeit > 200 :
    Figur.setState(0)
     
  # Ball bewegen, ggf. zurücksetzen
  if not Figur.isHit :
    Ball.move(-1, 0)
    if Ball.controlRestart(xMax-50, yMax/2) :
      Spiel.setScore(1, Blue)
  # Kontrolle, ob Ball im Kontaktbereich
  if (Ball.x < Figur.x+150) : 
    # Wenn Player nicht ausweicht, Spiel-Ende
    if not Figur.dodge(Ball.y, yMax/2) :
      Figur.isHit = True
      Spiel.showMessage("Game over", Red)

  # Sprite in Fenster positionieren
  Fenster.fill(Yellow)
  Fenster.blit(Spiel.Text, (xMax/2, 10))
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  Fenster.blit(Ball.Bild, (Ball.x, Ball.y))
  pg.display.update()

# Pygame verlassen
pg.quit()

