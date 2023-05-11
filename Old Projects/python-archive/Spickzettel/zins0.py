class InterCalc(object) :
  Kapital = 1
  Prozent = 1
  Zinsen = 1

  # Funktionen
  def setKapital(self, Kapital) :
    self.Kapital = float(input())
  def setProzent(self, Prozent) :
    self.Prozent = float(input())
  def setZinsen(self, Zinsen) :
    self.Zinsen = float(input())

  def getKapital(self, Kapital) :
    self.Kapital = self.Zinsen * 100 / self.Prozent
    return self.Kapital
  def getProzent(self, Prozent) :
    self.Prozent = self.Zinsen * 100 / self.Kapital
    return self.Prozent
  def getZinsen(self, Zinsen) :
    self.Zinsen = self.Kapital * self.Prozent / 100
    return self.Zinsen

# Hauptprogramm

Geld = InterCalc()
Geld.setKapital(Geld)
print(str(Geld.getKapital(Geld)))


