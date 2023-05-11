class InterCalc(object) :

  # Attribute initialisieren
  def __init__(self) :
    self.Kapital = 1
    self.Prozent = 1
    self.Zinsen = 1
   
  # Methoden
  def setKapital(self) :
    self.Kapital = float(input())
  def setProzent(self) :
    self.Prozent = float(input())
  def setZinsen(self) :
    self.Zinsen = float(input())

  def getKapital(self) :
    self.Kapital = self.Zinsen * 100 / self.Prozent
    return self.Kapital
  def getProzent(self) :
    self.Prozent = self.Zinsen * 100 / self.Kapital
    return self.Prozent
  def getZinsen(self) :
    self.Zinsen = self.Kapital * self.Prozent / 100
    return self.Zinsen

# Hauptprogramm
Geld = InterCalc()
print("Kapital: ", end="")
Geld.setKapital()
print("Zinssatz: ", end="")
Geld.setProzent()
print("Zinsen = " + str(Geld.getZinsen()))

