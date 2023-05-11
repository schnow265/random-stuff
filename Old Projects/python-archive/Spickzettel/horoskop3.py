# Horoskop mit Liste
from tkinter import *

# Hier must du deine eigene Vorhersagen setzen !!!
Vorhersage = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", \
  "Juli", "August", "September", "Oktober", "November", "Dezember"]
Zeichen = ["Steinbock", "Wassermann", "Fische", "Widder", "Stier", \
  "Zwillinge", "Krebs", "Loewe", "Jungfrau", "Waage", "Skorpion", "Schuetze"]

# Event-Funktion
def listboxSelect(event) :
  Auswahl = Box.curselection()
  Nr = Auswahl[0]
  Anzeige.config(text=Vorhersage[Nr])
  

# Hauptprogramm
Fenster = Tk()
Fenster.title("Horoskop")
Fenster.minsize(width=300, height=400)
Anzeige = Label(Fenster, text="Dein Sternzeichen:")
Anzeige.place(x=40, y=10, width=160, height=30)

# Sternzeichen
Box = Listbox(Fenster)
for Nr in range(0,12) :
  Box.insert(Nr, Zeichen[Nr])
Box.bind("<<ListboxSelect>>", listboxSelect) 
Box.place(x=30,y=50, width=200, height=300)
  
# Ereignis-Schleife
Fenster.mainloop()

