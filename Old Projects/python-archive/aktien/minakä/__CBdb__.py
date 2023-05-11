import time
import minakä.__bank__ as vault
import minakä.__akt__ as akt

def bye():
    print("Sie werden nun von Coinbase abgemeldet.")
    print("Um ihre Privatsfähre zu wahren, löschen wir das Coinbase-Modul von ihrem Computer")
    time.sleep(10)
    print("Coinbase wurde gelöscht. Sie werden wieder mit dem Kaufprogramm verbunden.")
    akt.creator()

def load():
    password = input()
    if password == "1":
        print("User1")
        vault.v1()
        print("Hier werden bald Funktionen kommen. Aber es ist noch im Bau")
        bye()
    if password == "2":
        print("User2")
