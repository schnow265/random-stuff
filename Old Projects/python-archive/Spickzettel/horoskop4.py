# Horoskop mit Radiobuttons
from tkinter import *

# Hier must du deine eigene Vorhersagen setzen !!!
Vorhersage = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", \
  "Juli", "August", "September", "Oktober", "November", "Dezember"]
Zeichen = ["Steinbock", "Wassermann", "Fische", "Widder", "Stier", \
  "Zwillinge", "Krebs", "Loewe", "Jungfrau", "Waage", "Skorpion", "Schuetze"]

# Event-Funktion
def buttonClick() :
  Anzeige.config(text=Vorhersage[Nummer.get()]) 

# Hauptprogramm
Fenster = Tk()
Fenster.title("Horoskop")
Fenster.minsize(width=300, height=250)
Anzeige = Label(Fenster, text="Dein Sternzeichen:")
Anzeige.grid(row=0, column=0)

# Hilfsvariable
Nummer = IntVar()
Nummer.set(-1)

# Sternzeichen
Stern = []
for Nr in range(0,12) :
  Stern.append(Radiobutton(Fenster, variable=Nummer, value=Nr, text=Zeichen[Nr]))
  Stern[Nr].config(command=buttonClick)
for pos in range(0,6) :
  Stern[pos].grid(row=pos+1, column=0, sticky="w")
  Stern[pos+6].grid(row=pos+1, column=1, sticky="w")
  
# Ereignis-Schleife
Fenster.mainloop()

