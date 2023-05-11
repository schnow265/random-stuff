# Pygame Kreis
import pygame

# Farben festlegen
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Cyan = (0,255,255)
Magenta = (255,0,255)
Yellow = (255,255,0)
White = (255,255,255)
Black = (0,0,0)

# Pygame starten, Fenster erzeugen
pygame.init()
Fenster = pygame.display.set_mode((600, 400))
Fenster.fill(Green)

# Ereignis-Schleife
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False
  # Kreis zeichnen
  Kreis = pygame.draw.circle(Fenster, Red, (300, 200), 100)
  pygame.display.update()

# Pygame verlassen
pygame.quit()
