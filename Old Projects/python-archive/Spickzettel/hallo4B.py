# Hallo mit Buttons
from tkinter import *

# Text-Konstanten
Antwort = ["Prima", "Gut", "Geht so", "Schlecht", "Miserabel", "Sag ich nicht"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktionen
def buttonClick(Nummer) :
  Anzeige.config(text=Diagnose[Nummer.get()])

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.config(width=300, height=190)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=80, y=10, width=160, height=30)

Nummer = IntVar()
Knopf = []
for Nr in range(0,6) :
  Knopf.append(Button(Fenster, text=Antwort[Nr]))
  Knopf[Nr].config(command=lambda : buttonClick(Nummer))
for pos in range(0,3) :
  Knopf[pos].place(x=20, y=60+pos*40, width=120, height=30)
  Knopf[pos+3].place(x=160, y=60+pos*40, width=120, height=30)

# Ereignis-Schleife
Fenster.mainloop()

