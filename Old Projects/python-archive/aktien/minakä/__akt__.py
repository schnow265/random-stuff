from config import __cofig__ as conf
from minakä import things
import pyttsx3
import time



def boot():
    print(" ")
    print("   Aktienmaschine by TamSchnow265  ")
    print(" ")
    print("Please enter your Product-Key, to start the programm!")
    pw = input()
    if pw == "3XS6-GBO2-GYEL-BXIH":
        print("Key is correct. The programm will launch soon...")
        time.sleep(3)
        print(" ")
        print("Booting...")
        engine = pyttsx3.init()
        engine.say("Wilkommen bei Aktienmaschine")
        engine.runAndWait()
        print(" ")
        time.sleep(2)
        Anwahl()

    else:
        print("Wrong Key!")
        print("Press ENTER to exit")
        input()
        exit()


def Anwahl():
    print("Willkommen im Programm `Aktienmaschine`!")
    print("Bitte drücke nicht während des Startens die ENTER Taste auf der Tastatur!")
    time.sleep(3)
    print("Wir starten gleich mit der Generation der Kurse...")
    time.sleep(3)
    print("Wir bitten sie um etwas Geduld!")
    time.sleep(8)
    Aktienkurs()

def Aktienkurs():
    print("Starting VCG.exe ...")
    print("")
    time.sleep(5)
    print(" ")
    print("     -------------------------VCG-CREDITS---------------------------------")
    print("     I         Virtual Capital Generator V1.0 by TamSchnow265            I")
    print("     I           Created only for this Programm!                         I")
    print("     I            Copyright 2021 by TamSchnow 265                        I")
    print("     ---------------------------------------------------------------------")
    print(" ")
    time.sleep(8)
    print("Command Input -> VCG-generate-capital-akticusV3")
    print(" ")
    time.sleep(5)
    print("Das Firmenkapital wird nun mit AkticusV3 berechnet...")
    print(" ")
    time.sleep(4)
    print("----------------------------------------------")
    things.Tesla()
    time.sleep(3)
    things.Facebook()
    time.sleep(3)
    things.Google()
    time.sleep(3)
    things.CocaCola()
    time.sleep(3)
    things.ASUS()
    time.sleep(3)
    things.Amazon()
    time.sleep(3)
    things.Adidas()
    time.sleep(3)
    things.Maeggi()
    time.sleep(3)
    things.VW()
    time.sleep(3)
    things.Ford()
    time.sleep(3)
    things.RedBull()
    time.sleep(3)
    things.Apple()
    time.sleep(3)
    things.Windows()
    time.sleep(3)
    things.TeleBumm()
    time.sleep(3)
    print("----------------------------------------------")
    time.sleep(4)
    print(" ")
    time.sleep(1)
    creator()

def creator():
    print("Bitte gib die Firma an, von der du eine Aktie kaufen willst!")
    print("Wenn du die Kurse neu berechnen willst, dann gib reload ein. Um das Programm zu Beenden gib exit ein!")
    buy = input()
    if buy == "exit" :
        print("Press ENTER to exit savely")
        input()
        exit()
    if buy == "Google":
            print("Google Aktie gekauft!")
            engine = pyttsx3.init()
            engine.say("G o o g l e gekauft")
            engine.runAndWait()
            creator()
    if buy == "Tesla":
            print("Tesla Aktie gekauft!")
            engine = pyttsx3.init()
            engine.say("Stromschlag wird nun bestellt.")
            engine.runAndWait()
            creator()
    if buy == "Facebook":
            print("Facebook Aktie gekauft!")
            creator()
    if buy == "reload":
            print("Reload wird ausgeführt ...")
            time.sleep(3)
            Aktienkurs()
            creator()
    if buy == "SNOW-Animations":
            print("EASTER EGG HUNTER!!!!!!!")
            creator()
    if buy == "Coinbase":
        print("Importing Coinbase...")
        from minakä import __CBdb__ as db
        time.sleep(5)
        print("Download complete!")
        print("Wilkommen bei Coinbase!")
        print("Bitte gib deinen Key ein!")
        db.load()

    else:
            print("Nicht Verständlich!")
            print("Bitte nocheinmal eingeben!")
            creator()



def cf():
    pass
