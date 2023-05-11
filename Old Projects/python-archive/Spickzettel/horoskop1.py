# Horoskop mit Buttons
from tkinter import *

# Event-Funktionen
# Hier must du deine eigene Vorhersagen einfügen !!!
def button1Click() :
  Anzeige.config(text="Januar")
def button2Click() :
  Anzeige.config(text="Februar")
def button3Click() :
  Anzeige.config(text="Maerz")
def button4Click() :
  Anzeige.config(text="April")
def button5Click() :
  Anzeige.config(text="Mai")
def button6Click() :
  Anzeige.config(text="Juni")
def button7Click() :
  Anzeige.config(text="Juli")
def button8Click() :
  Anzeige.config(text="August")
def button9Click() :
  Anzeige.config(text="September")
def button10Click() :
  Anzeige.config(text="Oktober")
def button11Click() :
  Anzeige.config(text="November")
def button12Click() :
  Anzeige.config(text="Dezember")

# Hauptprogramm
Fenster = Tk()
Fenster.title("Horoskop")
Fenster.config(width=300, height=300)
Anzeige = Label(Fenster, text="Dein Sternzeichen:")
Anzeige.place(x=70, y=10, width=160, height=30)
# Sternzeichen
Button1  = Button(Fenster, text="Steinbock", command=button1Click)
Button2  = Button(Fenster, text="Wassermann", command=button2Click)
Button3  = Button(Fenster, text="Fische", command=button3Click)
Button4  = Button(Fenster, text="Widder", command=button4Click)
Button5  = Button(Fenster, text="Stier", command=button5Click)
Button6  = Button(Fenster, text="Zwillinge", command=button6Click)
Button7  = Button(Fenster, text="Krebs", command=button7Click)
Button8  = Button(Fenster, text="Loewe", command=button8Click)
Button9  = Button(Fenster, text="Jungfrau", command=button9Click)
Button10 = Button(Fenster, text="Waage", command=button10Click)
Button11 = Button(Fenster, text="Skorpion", command=button11Click)
Button12 = Button(Fenster, text="Schuetze", command=button12Click)
Button1.place(x=20, y=50, width=120, height=30)
Button2.place(x=160, y=50, width=120, height=30)
Button3.place(x=20, y=90, width=120, height=30)
Button4.place(x=160, y=90, width=120, height=30)
Button5.place(x=20, y=130, width=120, height=30)
Button6.place(x=160, y=130, width=120, height=30)
Button7.place(x=20, y=170, width=120, height=30)
Button8.place(x=160, y=170, width=120, height=30)
Button9.place(x=20, y=210, width=120, height=30)
Button10.place(x=160, y=210, width=120, height=30)
Button11.place(x=20, y=250, width=120, height=30)
Button12.place(x=160, y=250, width=120, height=30)
Fenster.mainloop()

