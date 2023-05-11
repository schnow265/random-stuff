from tkinter import *

Fenster = Tk()
Menuleiste = Menu(Fenster)
Fenster.config(menu=Menuleiste)

Dateimenu = Menu(Menuleiste)
Menuleiste.add_cascade(label="Datei", menu=Dateimenu)
Dateimenu.add_command(label="öffnen")
Dateimenu.add_command(label="Speichern")
Dateimenu.add_command(label="Ende")

Hilfemenu = Menu(Menuleiste)
Menuleiste.add_cascade(label="Hilfe", menu=Hilfemenu)
Hilfemenu.add_command(label="Info")

Fenster.mainloop()
