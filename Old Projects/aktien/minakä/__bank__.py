import __CBdb__ as cbdb

def v1():
    print("Please enter your Wallte key or your Username")
    enter = input()
    if enter == "1":
        henter = hash(enter)
        print(henter)
        print("This is your wallet key")
    if enter == "2150051738125647861":
        print("Welcome. ")
    else:
        print("ERROR IN LINE. Ending Coinbase")
        cbdb.bye()