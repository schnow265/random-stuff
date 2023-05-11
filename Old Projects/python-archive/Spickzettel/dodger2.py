# Pygame Dodger
import pygame as pg
import random
from dplayer import *

# Startwerte festlegen
Yellow = (255,255,0)
xMax, yMax = 800, 400
Start = 0

def getTime(Reset) :
  global Start
  if Reset :
    Start = pg.time.get_ticks()
  Diff = pg.time.get_ticks() - Start
  return Diff

# Pygame starten, Spielfeld und Spielfigur erzeugen
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Fenster = pg.display.set_mode((xMax, yMax))
Figur = Player(20, 30)

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
        getTime(True)
      if event.key == pg.K_DOWN :
        Figur.setState(1)
        getTime(True)
        
  # Zeit testen, ggf. zurück zum Stand
  Zeit = getTime(False)
  if Zeit > 1000 :
     Figur.setState(0)

  # Sprite in Fenster positionieren
  Fenster.fill(Yellow)
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  pg.display.update()

# Pygame verlassen
pg.quit()

