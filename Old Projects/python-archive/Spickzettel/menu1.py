from tkinter import *

def newFile():
  pass
def openFile():
  pass
def saveFile():
  pass

# Hauptprogramm    
Fenster = Tk()
Menuleiste = Menu(Fenster)
Fenster.config(menu=Menuleiste)

Dateimenu = Menu(Menuleiste,tearoff = 0)
Menuleiste.add_cascade(label="Datei", menu=Dateimenu)
Dateimenu.add_command(label="Neu", command=newFile)
Dateimenu.add_command(label="öffnen", command=openFile)
Dateimenu.add_command(label="Speichern", command=saveFile)
Dateimenu.add_command(label="Ende", command=Fenster.destroy)

Hilfemenu = Menu(Menuleiste,tearoff = 0)
Menuleiste.add_cascade(label="Hilfe", menu=Hilfemenu)
Hilfemenu.add_command(label="Info")

Fenster.mainloop()
