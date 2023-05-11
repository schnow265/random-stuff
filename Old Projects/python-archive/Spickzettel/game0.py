# Pygame-Basis
import pygame

# Pygame starten, Fenster erzeugen
pygame.init()
pygame.display.set_mode((600, 400))

# Ereignis-Schleife
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False

# Pygame verlassen
pygame.quit()
