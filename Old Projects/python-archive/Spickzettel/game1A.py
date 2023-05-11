# Pygame Grafik
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
Fenster.fill(White)

# Ereignis-Schleife
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False
  # Zeichnen
  pygame.draw.rect(Fenster, Blue, (100, 50, 400, 100))
  pygame.draw.ellipse(Fenster, Yellow, (100, 250, 400, 100))
  pygame.draw.line(Fenster, Black, (50,50), (550,350), 5)
  pygame.draw.line(Fenster, Black, (550,50), (50,350), 5) 
  pygame.display.update()

# Pygame verlassen
pygame.quit()
