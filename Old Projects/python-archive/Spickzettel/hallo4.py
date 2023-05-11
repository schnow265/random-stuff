# Hallo mit Buttons
from tkinter import *

# Text-Konstanten
Antwort = ["Prima", "Gut", "Geht so", "Schlecht", "Miserabel", "Sag ich nicht"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktion
def buttonClick(Nr) :
  Anzeige.config(text=Diagnose[Nr])

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.config(width=300, height=190)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=80, y=10, width=160, height=30)

# Schaltflächen
Knopf = []
for Nr in range(0,6) :
  Knopf.append(Button(Fenster, text=Antwort[Nr]))
for pos in range(0,3) :
  Knopf[pos].place(x=20, y=60+pos*40, width=120, height=30)
  Knopf[pos+3].place(x=160, y=60+pos*40, width=120, height=30)

# Ereignisse einzeln konfigurieren
Knopf[0].config(command=lambda: buttonClick(0))
Knopf[1].config(command=lambda: buttonClick(1))
Knopf[2].config(command=lambda: buttonClick(2))
Knopf[3].config(command=lambda: buttonClick(3))
Knopf[4].config(command=lambda: buttonClick(4))
Knopf[5].config(command=lambda: buttonClick(5))

# Ereignis-Schleife
Fenster.mainloop()

