# Hallo mit Radio+Check
from tkinter import *

# Text-Konstanten
Antwort = ["Prima", "Gut", "Geht so", "Schlecht", "Miserabel", "Sag ich nicht"]
Bereich = ["Seele", "Geist", "Körper"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktionen
def buttonClick() :
  Anzeige.config(text=Diagnose[OptNum.get()])
def checkClick() :
  Text = "Hallo! "
  for Nr in range (0,3) :
    if ChkNum[Nr].get() == 1 :
      Text = Text + Bereich[Nr] + " ";
  Fenster.title(Text)

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.minsize(width=420, height=300)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=50, y=10)
Links = Frame(Fenster, borderwidth=2, relief="sunken")
Links.place(x=20, y=50, width=180, height=220)
Rechts = Frame(Fenster, borderwidth=2, relief="raised")
Rechts.place(x=220, y=50, width=180, height=110)

# Hilfsvariablen
ChkNum = [0,0,0]
OptNum = IntVar()
OptNum.set(-1)

# Optionsfelder
Option = []
for Nr in range(0,6) :
  Option.append(Radiobutton(Links, variable=OptNum, value=Nr, text=Antwort[Nr]))
  Option[Nr].config(command=buttonClick)
  Option[Nr].grid(row=Nr+1, column=0, sticky="w")

# Kontrollfelder
Wahl = []
for Nr in range(0,3) :
  ChkNum[Nr] = IntVar()
  Wahl.append(Checkbutton(Rechts, variable=ChkNum[Nr], text= Bereich [Nr]))
  Wahl[Nr].config(command=checkClick)
  Wahl[Nr].grid(row=Nr+1, column=2, sticky="w")

# Ereignis-Schleife
Fenster.mainloop()

