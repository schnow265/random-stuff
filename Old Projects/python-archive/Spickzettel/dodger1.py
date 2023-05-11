# Pygame Dodger
import pygame as pg
import random
from dplayer import *

# Startwerte festlegen
Yellow = (255,255,0)
xMax, yMax = 800, 400

# Pygame starten, Spielfeld und Spielfigur erzeugen
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Fenster = pg.display.set_mode((xMax, yMax))
Figur = Player(20,30)

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
      if event.key == pg.K_DOWN :
        Figur.setState(1)
      if event.key == pg.K_RETURN :
        Figur.setState(0)
        
  # Sprite in Fenster positionieren
  Fenster.fill(Yellow)
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  pg.display.update()

# Pygame verlassen
pg.quit()

