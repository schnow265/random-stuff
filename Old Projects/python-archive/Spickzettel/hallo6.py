# Hallo mit Optionen
from tkinter import *

# Text-Konstanten
Antwort = ["Prima", "Gut", "Geht so", "Schlecht", "Miserabel", "Sag ich nicht"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktion
def buttonClick() :
  Anzeige.config(text=Diagnose[Nummer.get()])

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.minsize(width=260, height=260)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.pack()

# Hilfsvariable
Nummer = IntVar()
Nummer.set(-1)

# Optionsfelder
Option = []
for Nr in range(0,6) :
  Option.append(Radiobutton(Fenster, variable=Nummer, value=Nr, text=Antwort[Nr]))
  Option[Nr].config(command=buttonClick)
  Option[Nr].pack(anchor="w")

# Ereignis-Schleife
Fenster.mainloop()

