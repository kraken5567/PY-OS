def Main(OS):
    import tkinter as T
    import os
    import importlib.util
    from PIL import ImageTk, Image
    import random

    from Apps.Blackjack.Blackjack_Classes import Player

    #cards ar 2.5in x 3.5in; W x H
    # card images made by Aussiesim from Game-Icons.net <3

    ProgDir = "Apps"
    ProgFolder = "Blackjack"
    appDir = f"{ProgDir}\\{ProgFolder}"
    cardDir = f"{appDir}\\Cards"
    cardsLib = os.listdir(cardDir)
    cards = random.choice(cardsLib)
    card = random.choice(os.listdir(f"{cardDir}\\{cards}"))
    color = T.StringVar(value="green")

    table = T.Toplevel(OS,bg=color.get())
    table.title("Blackjack")
    table.transient(OS)
    iconImage = ImageTk.PhotoImage(Image.open(f"{cardDir}\\{cards}\\{card}"))
    table.iconphoto(False, iconImage) 

    #game related
    cards = os.listdir(cardDir)
    player_score = T.IntVar(value=100)
    dealerStr = T.StringVar()
    playerStr = T.StringVar()

    right_most = T.IntVar()

    resultLabel = T.Label(table)
    resultLabel.grid(row=5,columnspan=20)
    scoreLabel = T.Label(table)
    scoreLabel.grid(row=4,column=3, columnspan=17)

    def initGame():
        global shelf
        shelf = T.Canvas(table,bg=color.get(),scrollregion=(0, 0, 2000, 256))
        shelf.grid(row=1, columnspan=20)
        scrollbar = T.Scrollbar(table, orient=T.HORIZONTAL, command=shelf.xview)
        scrollbar.grid(row=2, column=0, columnspan=20, sticky=T.EW)
        right_most.set(0)
        shelf.config(scrollregion=(0, 0, right_most.get(), 256))
        GameRound()

    def initPlayers():
        dealer, player = Player(cards,True,cardDir), Player(cards,False,cardDir)
        return dealer, player

    def initdisplay(P):
        global imgHolder
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

    def initbuttons(P):
        global hit, stand, bet
        bet = T.Scale(table,bg=color.get(),from_=1, to=50, orient=T.HORIZONTAL)
        hit = T.Button(table,text="Hit",bg=color.get(), command= lambda: hitButtonClicked(P, bet))
        stand = T.Button(table,text="Stand",bg=color.get(), command= lambda: Stand(P))
        
        scoreLabel.config(text=f"Score: {player_score.get()}",bg=color.get())
        resultLabel.config(text="",bg=color.get())

        hit.grid(row=4,column=0)
        stand.grid(row=4,column=1)
        bet.grid(row=4,column=2)
    
    def Stand(players):
        global imgHolder

        del imgHolder
        table.update()

        dealer, player = players[0], players[1]
        dealerCard = dealer.getCardObject()

        playerCard = player.getCardObject()
        player.value,player.value_list = playerCard.getValue(player.cards)

        while (dealer.value <= player.value) and not ((player.value >= 21) or (dealer.value > 21)):
            dealer.addCard(cards)
            dealer.value,dealer.value_list = dealerCard.getValue(dealer.cards)

        updateDisplay(players)

        # buttons
        hit.config(state=T.DISABLED)
        stand.config(state=T.DISABLED)

        if ((dealer.value > 21) and (player.value <= 21)) or ((player.value > dealer.value) and (player.value <= 21)):
            result = "Player Wins!"
            player_score.set(player_score.get() + bet.get())

        if ((player.value > 21) and (dealer.value > 21)):
            result = "Draw!"

        if ((player.value > 21) and (dealer.value <= 21)) or (dealer.value > player.value):
            if ((player.value > 21) and (dealer.value > 21)):
                result = "Draw!"
            elif (dealer.value <= 21):
                result = "Dealer Wins!"
                player_score.set(player_score.get() - bet.get())

        result += f" | Player: {player.value}, Dealer:{dealer.value}"

        # display result and update score
        resultLabel.config(text=result)
        scoreLabel.config(text=f"Score: {player_score.get()}")

        table.update()

        players = None

        table.after(1500,shelf.destroy())

        initGame()

    def hitButtonClicked(players, bet):

        bet.config(state=T.DISABLED)

        player = players[1]

        player.addCard(cards)

        cardObj = player.getCardObject()

        player.value,player.value_list = cardObj.getValue(player.cards)
        player.label = cardObj.label(player.value_list,False)

        player.images.append(cardObj.cardImager(player.cards[-1], cardDir))

        updateDisplay(players)

        if player.value >= 21:
            Stand(players)
    
    def updateDisplay(players):
        cardWidth = 128
        try:
            for j, object in enumerate(players):
                cards, [value,value_list], label, images = object.Return()
                for i, image in enumerate(images):
                    height = j * cardWidth
                    x = i * cardWidth
                    try:
                        img_tag = shelf.create_image(x, height, image=image, anchor=T.NW)
                    except:
                        img_tag = shelf.create_image(x, height, image=image[1], anchor=T.NW)
            right_most.set(shelf.bbox("all")[2])
            shelf.config(scrollregion=(0, 0, right_most.get(), 256))
        except TypeError:
            raise TypeError("Players is None!")

    def GameRound():
        global imgHolder
        P = initPlayers()
        initdisplay(P)
        initbuttons(P)
        table.mainloop()
    
    initGame()