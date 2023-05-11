# Haus
from tkinter import *

# Fenstermaße
Breite = 500
Hoehe = 330

# Event-Funktion
def buttonClick() :
  Grafik.create_rectangle(20, Hoehe/2-20, Breite-20, Hoehe-20, fill="gray")
  Grafik.create_polygon((20, Hoehe/2-20), (Breite/2, 20), (Breite-20, Hoehe/2-20)) 
  # Tür und Fenster
  Grafik.create_rectangle(50, Hoehe/2+10, 150, Hoehe/2+90, fill="blue")
  Grafik.create_rectangle(Breite-50, Hoehe/2+10, Breite-150, Hoehe/2+90, fill="blue")
  Grafik.create_rectangle(Breite/2-40, Hoehe/2+20, Breite/2+40, Hoehe-20, fill="brown")

# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = Button(Fenster, text="My House", bg="gray", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe-45, width=120, height=30)
Fenster.mainloop()

