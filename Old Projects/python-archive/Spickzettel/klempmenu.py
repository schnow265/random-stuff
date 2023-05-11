from tkinter import *
from tkinter import filedialog

class KlempMenu :
 
  def __init__(self, fenster) :
    self.Fenster = fenster
    Menuleiste = Menu(self.Fenster)
    self.Fenster.config(menu=Menuleiste)
    Dateimenu = Menu(Menuleiste, tearoff = 0)
    Menuleiste.add_cascade(label="Datei", menu=Dateimenu)
    Dateimenu.add_command(label="öffnen", command=self.openFile)
    Dateimenu.add_command(label="Speichern", command=self.saveFile)
    Dateimenu.add_command(label="Ende", command=self.closeAll)
    Hilfemenu = Menu(Menuleiste, tearoff = 0)
    Menuleiste.add_cascade(label="Hilfe", menu=Hilfemenu)
    Hilfemenu.add_command(label="Info")            

  def openFile(self) :
    self.Datei = filedialog.askopenfilename(filetypes= \
                 (("Textdateien","*.txt"),("Alle Dateien","*.*")))   
  def saveFile(self) :
    self.Datei = filedialog.asksaveasfilename()
  def closeAll(self) :
    self.Fenster.quit()
    self.Fenster.destroy()
    
  def getName(self) :
    return self.Datei  


