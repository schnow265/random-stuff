# Grafik mit Canvas
from tkinter import *

# Fenstermaße
Breite = 500
Hoehe = 330

# Event-Funktion
def buttonClick() :
  Grafik.create_rectangle(20, 20, Breite-20, Hoehe-20)
  Grafik.create_oval(20, 20, Breite-20, Hoehe-20)
  Grafik.create_line(Breite/2, 20, Breite/2, Hoehe-20)
  Grafik.create_line(20, Hoehe/2, Breite-20, Hoehe/2)

# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = Button(Fenster, text="Mal mal!", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe/2-15, width=120, height=30)
Fenster.mainloop()

