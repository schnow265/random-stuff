# 0 bis 100 %
from tkinter import *

# Text-Konstanten
Bereich = ["Das sagst du mir:", "Das sag ich dir:", "Diagnose-Manipulator:"]
Diagnose = []
Psychose = []
Max = 0

def scaleValue(event) :
  Nr = Schieber.get()
  Anzeige.config(text=str(Nr))

# Hauptprogramm
Fenster = Tk()
Fenster.title("Prozente")
Fenster.minsize(width=400, height=180)
Anzeige = Label(Fenster, text="0", font=("Arial", 24))
Anzeige.place(x=20, y=30, width=350, height=60)

Schieber = Scale(Fenster, orient="horizontal", command=scaleValue)
Schieber.config(from_=0, to=100, length=360, showvalue=0)
Schieber.place(x=20, y=120)
Fenster.mainloop()

