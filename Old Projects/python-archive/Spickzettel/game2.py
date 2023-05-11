# Pygame Figur
import pygame as pg

# Player-Klasse
class Player(pg.sprite.Sprite) :
  def __init__(self) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")

# Farbe festlegen
Green = (0,255,0)

# Pygame starten, Spielfeld erzeugen
pg.init()
Fenster = pg.display.set_mode((600, 400))
Fenster.fill(Green)

# Spielfigur erzeugen
Figur = Player()

# Ereignis-Schleife
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
  # Sprite in Fenster positionieren
  Fenster.blit(Figur.image, (250, 150))
  pg.display.update()

# Pygame verlassen
pg.quit()
