def Main(OS):
    import tkinter as T
    import os
    import importlib.util
    from PIL import ImageTk, Image
    import random

    #cards ar 2.5in x 3.5in; W x H
    # card images made by Aussiesim from Game-Icons.net

    ProgDir = "Apps"
    ProgFolder = "Blackjack"
    appDir = f"{ProgDir}\\{ProgFolder}"
    cardDir = f"{appDir}\\Cards"

    cardsLib = os.listdir(cardDir)
    cards = random.choice(cardsLib)
    card = random.choice(os.listdir(f"{cardDir}\\{cards}"))
    
    
    #init values
    dealerStr = T.StringVar()
    playerStr = T.StringVar()
    color = T.StringVar(value="green")

    player_score = T.IntVar(value=100)

    table = T.Toplevel(OS,bg=color.get())
    table.title("Blackjack")
    table.transient(OS)
    table.iconphoto(False, ImageTk.PhotoImage(Image.open(f"{cardDir}\\{cards}\\{card}")))

    cards = os.listdir(cardDir)

    def Initbuttons():
        hit = T.Button(table,text="Hit",bg=color.get())
        stand = T.Button(table,text="Stand",bg=color.get())
        bet = T.Scale(table,bg=color.get(),from_=1, to=50, orient=T.HORIZONTAL)

        hit.grid(row=4,column=0)
        stand.grid(row=4,column=1)
        bet.grid(row=4,column=2)

        return [hit,stand,bet]


    def display():

        dealers = T.Canvas(table,bg=color.get(),height=128)
        players = T.Canvas(table,bg=color.get(),height=128)

        button_list = Initbuttons()

    

    display()