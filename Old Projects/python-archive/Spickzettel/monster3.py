# Frankensteins Labor
class Monster :
  # Attribute initialisieren
  def __init__(self, name, wesen) :
    self.Name = name
    self.Wesen = wesen
  # Methoden
  def show(self) :
    print("Name : " + self.Name)
    print("Wesen: " + self.Wesen)

class GMonster (Monster):
  pass

class SMonster (Monster):
  pass

# Hauptprogramm
Frank = Monster("Frankie", "ungewöhnlich")
Frank.show()
Albert = GMonster("Bertie", "nachdenklich")
Albert.show()
Sigmund = SMonster("Sigi", "einfühlsam")
Sigmund.show()

