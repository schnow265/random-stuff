# Horoskop mit Buttons
from tkinter import *

# Hier must du deine eigene Vorhersagen setzen !!!
Vorhersage = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", \
  "Juli", "August", "September", "Oktober", "November", "Dezember"]
Zeichen = ["Steinbock", "Wassermann", "Fische", "Widder", "Stier", \
  "Zwillinge", "Krebs", "Loewe", "Jungfrau", "Waage", "Skorpion", "Schuetze"]

# Event-Funktion
def buttonClick(Nr) :
  Anzeige.config(text=Vorhersage[Nr])

# Hauptprogramm
Fenster = Tk()
Fenster.title("Horoskop")
Fenster.minsize(width=300, height=400)
Anzeige = Label(Fenster, text="Dein Sternzeichen:")
Anzeige.place(x=70, y=10, width=160, height=30)

# Sternzeichen
Stern = []
for Nr in range(0,12) :            
  Stern.append(Button(Fenster, text=Zeichen[Nr]))
for pos in range(0,6) :
  Stern[pos].place(x=20, y=60+pos*40, width=120, height=30)
  Stern[pos+6].place(x=160, y=60+pos*40, width=120, height=30)
  
# Ereignisse einzeln konfigurieren
Stern[0].config(command=lambda: buttonClick(0))
Stern[1].config(command=lambda: buttonClick(1))
Stern[2].config(command=lambda: buttonClick(2))
Stern[3].config(command=lambda: buttonClick(3))
Stern[4].config(command=lambda: buttonClick(4))
Stern[5].config(command=lambda: buttonClick(5))
Stern[6].config(command=lambda: buttonClick(6))
Stern[7].config(command=lambda: buttonClick(7))
Stern[8].config(command=lambda: buttonClick(8))
Stern[9].config(command=lambda: buttonClick(9))
Stern[10].config(command=lambda: buttonClick(10))
Stern[11].config(command=lambda: buttonClick(11))

# Ereignis-Schleife
Fenster.mainloop()

