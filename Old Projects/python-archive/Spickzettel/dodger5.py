# Pygame Dodger
import pygame as pg
import random
from dplayer import *
from dthing import *

# Startwerte festlegen
Red = (255,0,0)
Blue = (0,0,255)
Yellow = (255,255,0)
xMax, yMax = 800, 400
Start = 0
Punkte = 0

# Textfeld erzeugen
Text = pg.Surface((300,50))
Text.fill(Yellow)

# Info anzeigen
def showMessage(text, Farbe) :
  global Text
  Font = pg.font.SysFont("arial", 48)
  Text = Font.render(text, True, Farbe)

# Punkte zählen und anzeigen
def setScore(num) :
  global Punkte
  Punkte += num
  showMessage("Punkte: " + str(Punkte), Blue)

# Timer
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

Figur = Player(20,30)
Ball = Thing("Bilder/ball1.png")
Ball.setPosition(xMax-50, yMax/2, True)

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
        
  # Zeit testen, ggf. Figur zurück in Stand
  Zeit = getTime(False)
  if Zeit > 200 :
    Figur.setState(0)
     
  # Ball bewegen, ggf. zurücksetzen
  if not Figur.isHit :
    Ball.move(-1, 0)
    if Ball.controlRestart(xMax-50, yMax/2) :
      setScore(1)
  # Kontrolle, ob Ball im Kontaktbereich
  if (Ball.x < Figur.x+150) : 
    # Wenn Player nicht ausweicht, Spiel-Ende
    if not Figur.dodge(Ball.y, yMax/2) :
      Figur.isHit = True
      showMessage("Game over", Red)

  # Sprite in Fenster positionieren
  Fenster.fill(Yellow)
  Fenster.blit(Text, (xMax/2, 10))
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  Fenster.blit(Ball.Bild, (Ball.x, Ball.y))
  pg.display.update()

# Pygame verlassen
pg.quit()

