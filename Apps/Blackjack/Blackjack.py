def Main(OS):
    import tkinter as T
    import os
    import importlib.util
    from PIL import ImageTk, Image
    import random

    from Apps.Blackjack.Blackjack_Classes import Player

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
    right_most = T.IntVar()

    player_score = T.IntVar(value=100)

    table = T.Toplevel(OS,bg=color.get())
    table.title("Blackjack")
    table.transient(OS)
    iconImage = ImageTk.PhotoImage(Image.open(f"{cardDir}\\{cards}\\{card}"))
    table.iconphoto(False, iconImage)

    cards = os.listdir(cardDir)

    shelf = T.Canvas(table,bg=color.get(),scrollregion=(0, 0, 2000, 256))
    shelf.grid(row=1, columnspan=20)
    scrollbar = T.Scrollbar(table, orient=T.HORIZONTAL, command=shelf.xview)
    scrollbar.grid(row=2, column=0, columnspan=20, sticky=T.EW)
    right_most.set(0)
    shelf.config(scrollregion=(0, 0, right_most.get(), 256))

    def initPlayers():
        dealer, player = Player(cards,True,cardDir), Player(cards,False,cardDir)
        return dealer, player

    def initdisplay(P):
        imgHolder = [] #used just for blank
        cardWidth = 128
        
        for j, object in enumerate(P):
            cards, value, label, images = object.Return()
            for i, image in enumerate(images):
                height = j * cardWidth
                x = i * cardWidth
                
                img_tag = shelf.create_image(x, height, image=image, anchor=T.NW)
                if (j == len(P) - 2) and (i+1 == len(images)):
                    image = Image.open(f"{appDir}\\Blank\\Blank.png")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg) 
                    img_tag = shelf.create_image(x, height, image=cardImg, anchor=T.NW)
        return [imgHolder, x, height]

    def initbuttons(P):
        hit = T.Button(table,text="Hit",bg=color.get(), command= lambda: hitButtonClicked(P))
        stand = T.Button(table,text="Stand",bg=color.get())
        bet = T.Scale(table,bg=color.get(),from_=1, to=50, orient=T.HORIZONTAL)

        hit.grid(row=4,column=0)
        stand.grid(row=4,column=1)
        bet.grid(row=4,column=2)

        return [hit,stand,bet]

    def hitButtonClicked(players):
        player = players[1]

        player.addCard(cards)

        cardObj = player.getCardObject()

        player.value = cardObj.getValue(player.cards)
        player.label = cardObj.label(player.value,False)

        player.images.append(cardObj.cardImager(player.cards[-1], cardDir))

        # update the display
        updateDisplay(players)

    def updateDisplay(players):
        global imgHolder
        imgHolder = [] #used just for blank
        cardWidth = 128
        for j, object in enumerate(players):
            cards, value, label, images = object.Return()
            for i, image in enumerate(images):
                height = j * cardWidth
                x = i * cardWidth

                img_tag = shelf.create_image(x, height, image=image, anchor=T.NW)
                if (j == len(players) - 2) and (i+1 == len(images)):
                    image = Image.open(f"{appDir}\\Blank\\Blank.png")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg) 
                    img_tag = shelf.create_image(x, height, image=cardImg, anchor=T.NW)
        right_most.set(shelf.bbox("all")[2])
        shelf.config(scrollregion=(0, 0, right_most.get(), 256))

    def GameRound():
        P = initPlayers()
        blank = initdisplay(P)
        initbuttons(P)
        table.mainloop()
    
    GameRound()