# Hallo mit Buttons
from tkinter import *

# Event-Funktionen
def button1Click() :
  Anzeige.config(text="Das ist ja toll!")
def button2Click() :
  Anzeige.config(text="Das freut mich!")
def button3Click() :
  Anzeige.config(text="Das geht ja noch.")
def button4Click() :
  Anzeige.config(text="Das tut mir leid!")
def button5Click() :
  Anzeige.config(text="Das ist ja schlimm!")
def button6Click() :
  Anzeige.config(text="Wenn du meinst ...")
  

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo!")
Fenster.config(width=300, height=190)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=80, y=10, width=160, height=30)
# Button-Texte
Button1 = Button(Fenster, text="Prima", command=button1Click)
Button2 = Button(Fenster, text="Gut", command=button2Click)
Button3 = Button(Fenster, text="Geht so", command=button3Click)
Button4 = Button(Fenster, text="Schlecht", command=button4Click)
Button5 = Button(Fenster, text="Miserabel", command=button5Click)
Button6 = Button(Fenster, text="Sag ich nicht", command=button6Click)
# Buttons platzieren
Button1.place(x=20, y=60, width=120, height=30)
Button2.place(x=160, y=60, width=120, height=30)
Button3.place(x=20, y=100, width=120, height=30)
Button4.place(x=160, y=100, width=120, height=30)
Button5.place(x=20, y=140, width=120, height=30)
Button6.place(x=160, y=140, width=120, height=30)
# Ereignis-Schleife
Fenster.mainloop()

