# Hallo mit Liste
from tkinter import *

# Text-Konstanten
Antwort = ["Prima", "Gut", "Geht so", "Schlecht", "Miserabel", "Sag ich nicht"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktion
def listboxSelect(event) :
  Auswahl = Box.curselection()
  Nr = Auswahl[0]
  Anzeige.config(text=Diagnose[Nr])

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.config(width=260, height=230)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=20, y=10, width=160, height=30)

# Listenfeld
Box = Listbox(Fenster)
for Nr in range(0,6) :
  Box.insert(Nr, Antwort[Nr])
Box.bind("<<ListboxSelect>>", listboxSelect) 
Box.place(x=30,y=50, width=200, height=150)

# Ereignis-Schleife
Fenster.mainloop()

