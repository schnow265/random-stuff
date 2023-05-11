# Frankensteins Labor
class Monster :
  # Attribute initialisieren
  def __init__(self, name, wesen) :
    self.Name = name
    self.Wesen = wesen
  # Methoden
  def Type(self) :
    return "Monster"
  def show(self) :
    print("Name : " + self.Name)
    print("Wesen: " + self.Wesen)
    print("Typ:   " + self.Type())

class GMonster (Monster):
  # Methode
  def Type(self) :
    return "Geistes-Monster"

class SMonster (Monster):
  # Methode
  def Type(self) :
    return "Seelen-Monster"

# Hauptprogramm
Frank = Monster("Frankie", "ungewöhnlich")
Frank.show()
Albert = GMonster("Bertie", "nachdenklich")
Albert.show()
Sigmund = SMonster("Sigi", "einfühlsam")
Sigmund.show()

