# Monster-Modul
class Monster :
  # Attribute initialisieren
  def __init__(self, name, wesen) :
    self.__Name = name
    self.__Wesen = wesen
  # Methoden
  def _Type(self) :
    return "Monster"
  def show(self) :
    print("Name : " + self.__Name)
    print("Wesen: " + self.__Wesen)
    print("Typ:   " + self._Type())

class GMonster (Monster):
  # Methode
  def _Type(self) :
    return "Geistes-Monster"

class SMonster (Monster):
  # Methode
  def _Type(self) :
    return "Seelen-Monster"

