# Frankensteins Labor
class Monster :
  # Attribute initialisieren
  def init(self, name, wesen) :
    self.Name = name
    self.Wesen = wesen
  # Methoden
  def show(self) :
    print("Name : " + self.Name)
    print("Wesen: " + self.Wesen)

# Hauptprogramm
Frank = Monster()
Frank.init("Frankie", "ungewöhnlich")
Frank.show()

