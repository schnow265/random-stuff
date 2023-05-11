# Seelenklempner
from tkinter import *

# Text-Konstanten
Bereich = ["Das sagst du mir:", "Das sag ich dir:", "Diagnose-Manipulator:"]
Diagnose = ["Das ist ja toll!", "Das freut mich!", "Das geht ja noch.", \
            "Das tut mir leid!", "Das ist ja schlimm!", "Wenn du meinst ..."]

# Event-Funktionen
def button1Click() :
  pass
def button2Click() :
  pass
  
# Hauptprogramm
Fenster = Tk()
Fenster.title("Seelenklempner")
Fenster.minsize(width=500, height=330)

# Bereiche festlegen
Anzeige = []
Rahmen = []
for pos in range(0,3) :
  Anzeige.append(Label(Fenster, text=Bereich[pos]))
  Anzeige[pos].place(x=20, y=10+pos*90, width=460, height=30)
  Rahmen.append(Frame(Fenster, borderwidth=2, relief="groove"))
  Rahmen[pos].place(x=20, y=40+pos*90, width=460, height=50)

# Eingabe, Antwort und Schieberegler
Eingabe = Entry(Rahmen[0])
Eingabe.place(x=10, y=10, width=440, height=30)
Antwort = Label(Rahmen[1])
Antwort.place(x=10, y=10, width=440, height=30)
Schieber = Scale(Rahmen[2], orient="horizontal")
Schieber.config(length=430, showvalue=0)
Schieber.pack(pady=10)

# Buttons für Fertig und Neu
Button1 = Button(Fenster, text="Neu", command=button1Click)
Button1.place(x=120, y=285, width=120, height=30)
Button2 = Button(Fenster, text="Fertig", command=button2Click)
Button2.place(x=260, y=285, width=120, height=30)

# Ereignis-Schleife
Fenster.mainloop()

