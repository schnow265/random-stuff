# Zeichnen mit der Maus
from tkinter import *

# Fenstermaße
Breite = 500
Hoehe = 330

# Event-Funktion
def mouseDraw(event):
   x = event.x - 1
   y = event.y - 1
   Grafik.create_oval( x, y, x+3, y+3)

# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.bind("<B1-Motion>", mouseDraw)
Grafik.pack()
Anzeige = Label(Fenster, text = "Zeichne mit der Maus")
Anzeige.pack(side="bottom")
Fenster.mainloop()

