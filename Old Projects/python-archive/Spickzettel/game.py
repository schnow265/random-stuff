import pygame as pg

class Game :

  # Startwerte und Textfeld erzeugen
  def __init__(self, Farbe) :
    self.Start = 0
    self.Punkte = 0
    self.Text = pg.Surface((300,50))
    self.Text.fill(Farbe)

  # Info anzeigen
  def showMessage(self, text, Farbe) :
    self.Font = pg.font.SysFont("arial", 48)
    self.Text = self.Font.render(text, True, Farbe)

  # Punkte zählen und anzeigen
  def setScore(self, num, Farbe) :
    self.Punkte += num
    self.showMessage("Punkte: " + str(self.Punkte), Farbe)

  # Timer
  def getTime(self, Reset) :
    if Reset :
      self.Start = pg.time.get_ticks()
    self.Diff = pg.time.get_ticks() - self.Start
    return self.Diff

  # Punkte und Zeit
  def showAll(self, num, Farbe) :
    self.Punkte += num
    ptext = "  |  Punkte: " + str(self.Punkte)
    ztext = "Zeit: " + str(int(self.Diff/1000))
    self.showMessage(ztext+ptext, Farbe)
