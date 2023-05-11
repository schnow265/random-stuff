# Seelenklempner
from tkinter import *
from tkinter import filedialog
import random

# Text-Konstanten
Bereich = ["Das sagst du mir:", "Das sag ich dir:", "Diagnose-Manipulator:"]
Diagnose = []
Psychose = []
Max = 0

# Menü-Funktionen
def initMenu() :
  Menuleiste = Menu(Fenster)
  Fenster.config(menu=Menuleiste)
  Dateimenu = Menu(Menuleiste, tearoff = 0)
  Menuleiste.add_cascade(label="Datei", menu=Dateimenu)
  Dateimenu.add_command(label="Öffnen", command=openFile)
  Dateimenu.add_command(label="Speichern", command=saveFile)
  Dateimenu.add_command(label="Ende", command=closeAll)
  Hilfemenu = Menu(Menuleiste, tearoff = 0)
  Menuleiste.add_cascade(label="Hilfe", menu=Hilfemenu)
  Hilfemenu.add_command(label="Info", command=showInfo)
def initPopup() :
  global KontextMenu
  KontextMenu = Menu(Fenster, tearoff = 0)
  KontextMenu.add_command(label="Öffnen", command=openFile)
  KontextMenu.add_command(label="Speichern", command=saveFile)
  KontextMenu.add_command(label="Ende", command=closeAll)
def openMenu(event):
  global KontextMenu
  KontextMenu.post(event.x_root, event.y_root)

# Datei-Funktionen
def loadDiagnose(Name) :
  global Max
  Nr = 0
  try :
    Datei = open(Name, "r")
    for Zeile in Datei :
      Diagnose.append(Zeile.rstrip())
      Nr += 1
    Max = Nr - 1
    Datei.close()
  except :
    Diagnose.append("Keine Sprechstunde")
def saveDiagnose(Name) :
  try :
    Datei = open(Name, "w")
    for Zeile in Psychose :
      Datei.write(Zeile+"\n")
    Datei.close()
  except :
    print("Kann Daten nicht speichern")

# Event-Funktionen
def button1Click() :
  Eingabe.delete(0,"end")
  Antwort.config(text="")
def button2Click() :
  Nr = random.randint(0,Max)
  Antwort.config(text=Diagnose[Nr])
  Psychose.append(Eingabe.get())
  Psychose.append(Diagnose[Nr])
  saveDiagnose("psychoX.txt") 
def scaleValue(event) :
  Nr = Schieber.get()
  Antwort.config(text=Diagnose[Nr])

# Menü-Optionen
def openFile() :
  Name = filedialog.askopenfilename(filetypes= \
          (("Textdateien","*.txt"),("Alle Dateien","*.*")))
  if Name != "":
    Diagnose.clear()
    loadDiagnose(Name)
    Schieber.config(to=Max) 
def saveFile() :
  Name = filedialog.asksaveasfilename()
  if Name != "":
    saveDiagnose(Name)
def closeAll() :
  Fenster.destroy()
def showInfo() :
  pass

# Hauptprogramm
Fenster = Tk()
Fenster.title("Seelenklempner")
Fenster.minsize(width=500, height=330)
initMenu()
initPopup()
Fenster.bind("<Button-3>", openMenu)
loadDiagnose("diagnose.txt")

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
Schieber = Scale(Rahmen[2], orient="horizontal", command=scaleValue)
Schieber.config(from_=0, to=Max, length=430, showvalue=0)
Schieber.pack(pady=10) 

# Buttons für Fertig und Neu
Button1 = Button(Fenster, text="Neu", command=button1Click)
Button1.place(x=120, y=285, width=120, height=30)
Button2 = Button(Fenster, text="Fertig", command=button2Click)
Button2.place(x=260, y=285, width=120, height=30)

# Ereignis-Schleife
Fenster.mainloop()

