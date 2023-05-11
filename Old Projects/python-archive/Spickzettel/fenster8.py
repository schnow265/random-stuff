# Fenster-Layout
from tkinter import *

class Window() :
  
  # Initialisierungen
  def __init__(self, Titel) :
    self.Fenster = Tk()
    self.Fenster.title(Titel)
    self.Fenster.config(width=260, height=120)
    self.Anzeige = Label(self.Fenster, text="Wie geht es?")
    self.Anzeige.place(x=50, y=20, width=160, height=30)
    self.Button1 = Button(self.Fenster, text="Gut", \
    command=self.button1Click)
    self.Button2 = Button(self.Fenster, text="Schlecht", \
    command=self.button2Click)
    self.Button1.place(x=20, y=70, width=100, height=30)
    self.Button2.place(x=140, y=70, width=100, height=30)
    self.Fenster.mainloop()
    
  # Methoden
  def button1Click(self) :
    self.Anzeige.config(text="Das freut mich!")
  def button2Click(self) :
    self.Anzeige.config(text="Das tut mir leid!")

# Hauptprogramm
Fenster = Window("Hallo")

