# Fenster-Layout
from tkinter import *
from tkinter import messagebox

# Event-Funktionen
def button1Click() :
  messagebox.showinfo("Antwort", "Das freut mich!")
def button2Click() :
  messagebox.showinfo("Antwort", "Das tut mir leid!")

# Hauptprogramm
Fenster = Tk()
Fenster.title("Hallo")
Fenster.config(width=260, height=120)
Anzeige = Label(Fenster, text="Wie geht es?")
Anzeige.place(x=50, y=20, width=160, height=30)
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.place(x=20, y=70, width=100, height=30)
Button2.place(x=140, y=70, width=100, height=30)
Fenster.mainloop()

