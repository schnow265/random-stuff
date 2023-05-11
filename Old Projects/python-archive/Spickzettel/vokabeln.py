# Vokabeln
from tkinter import *
import random

# Text-Konstanten
Deutsch = []
English = []
Max = 0
Richtig = -1

# Datei-Funktionen
def loadDiagnose() :
  global Max
  Nr = 0
  XY = 1
  try :
    Datei = open("vokabeln.txt", "r")
    for Zeile in Datei :
      Text = Zeile.rstrip()
      if XY == 1 :
        Deutsch.append(Text)
      else :
        English.append(Text)
      XY = -XY
      Nr += 1
    Max = Nr/2 - 1
    Datei.close()
  except :
    Deutsch.append("Nichts")
    English.append("Nothing")

# Event-Funktionen
def buttonClick() :
  global Richtig
  Aktuell = random.randint(0,Max)
  Anzeige.config(text=Deutsch[Aktuell])
  Oben = random.randint(0,Max)
  Mitte = random.randint(0,Max)
  Unten = random.randint(0,Max)
  Richtig = random.randint(0,2)
  Antwort[0].config(text=English[Oben])
  Antwort[1].config(text=English[Mitte])
  Antwort[2].config(text=English[Unten])
  Antwort[Richtig].config(text=English[Aktuell])
def getWord(Nr) :
  global Richtig
  if Nr == Richtig :
    Anzeige.config(text="Richtig")
  else :
    Anzeige.config(text="Falsch")
    print(Nr)
  
# Hauptprogramm
Fenster = Tk()
Fenster.title("Vokabeln")
Fenster.minsize(width=400, height=300)
loadDiagnose()

# Anzeige und Antworten festlegen
Anzeige = Label(Fenster, text="Klick auf Neu!")
Anzeige.place(x=20, y=20, width=360, height=40)
Knopf = Button(Fenster, text="Neu", command=buttonClick)
Knopf.place(x=140, y=230, width=120, height=40)
Antwort = []
for pos in range(0,3) :
  Antwort.append(Button(Fenster, text="???"))
  Antwort[pos].place(x=20, y=70+pos*50, width=360, height=40)
Antwort[0].config(command=lambda: getWord(0))
Antwort[1].config(command=lambda: getWord(1))
Antwort[2].config(command=lambda: getWord(2))

# Ereignis-Schleife
Fenster.mainloop()

