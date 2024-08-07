def Main(OS):
    import tkinter as T
    import os
    import importlib.util
    from PIL import ImageTk, Image
    import random

    from Apps.Blackjack.Blackjack_Classes import Player
    from WindowsClass import MovableFrame as MF 

    #cards ar 2.5in x 3.5in; W x H
    # card images made by Aussiesim from Game-Icons.net <3

    ProgDir = "Apps"
    ProgFolder = "Blackjack"
    appDir = f"{ProgDir}\\{ProgFolder}"
    cardDir = f"{appDir}\\Cards"
    color = T.StringVar(value="green")

    cardsLib = os.listdir(cardDir)
    cards = random.choice(cardsLib)
    card = random.choice(os.listdir(f"{cardDir}\\{cards}"))

    Frame = MF(OS, Image.open(f"{cardDir}\\{cards}\\{card}"), [750, 300])
    Frame.config_barColor(color.get())

    table = Frame.frame 

    #game related
    cards = os.listdir(cardDir)
    player_score = T.IntVar(value=100)
    dealerStr = T.StringVar()
    playerStr = T.StringVar()

    right_most = T.IntVar()

    doubleDown = False

    resultLabel = T.Label(table)
    resultLabel.grid(row=5,columnspan=20)
    scoreLabel = T.Label(table)
    scoreLabel.grid(row=4,column=5, columnspan=17)

    def initGame():
        global shelf
        shelf = T.Canvas(table,bg=color.get(),scrollregion=(0, 0, 2000, 256))
        shelf.grid(pady= 30, row=1, columnspan=20)
        scrollbar = T.Scrollbar(table, orient=T.HORIZONTAL, command=shelf.xview)
        scrollbar.grid(row=2, column=0, columnspan=20, sticky=T.EW)
        right_most.set(0)
        shelf.config(scrollregion=(0, 0, right_most.get(), 256))
        GameRound()

    def initPlayers():
        dealer, player = Player(cards,True,cardDir), Player(cards,False,cardDir)
        return dealer, player

    def initdisplay(P):
        global imgHolder, notBetted
        imgHolder = [] #used just for blank
        cardWidth = 128
        
        for j, object in enumerate(P):
            cards, value, label, images = object.Return()
            for i, image in enumerate(images):
                height = j * cardWidth
                x = i * cardWidth
                
                img_tag = shelf.create_image(x, height, image=image, anchor=T.NW)
                if notBetted: #(j == len(P) - 2) and (i+1 == len(images))
                    image = Image.open(f"{appDir}\\Blank\\Blank.png")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg) 
                    img_tag = shelf.create_image(x, height, image=cardImg, anchor=T.NW)

    def initbuttons(P):
        global hit, stand, bet, setBet, double

        current_score = player_score.get()
        if current_score <= 10: 
            bet = T.Scale(table,bg=color.get(),from_=1, to=10, orient=T.HORIZONTAL)
        else:
            bet = T.Scale(table,bg=color.get(),from_=1, to=player_score.get(), orient=T.HORIZONTAL)

        setBet = T.Button(table,text="Lock in Bet",bg=color.get(), command= lambda: startRound(P))
        
        hit = T.Button(table,text="Hit",bg=color.get(), command= lambda: hitButtonClicked(P, bet))
        double = T.Button(table,text="Double Down",bg=color.get(), command= lambda: DoubleButtonClicked(P, bet))

        stand = T.Button(table,text="Stand",bg=color.get(), command= lambda: Stand(P))
        
        scoreLabel.config(text=f"Score: {player_score.get()}",bg=color.get())
        resultLabel.config(text="",bg=color.get())

        hit.grid(row=4,column=0)
        double.grid(row=5,column=0)

        stand.grid(row=4,column=1)

        hit.config(state=T.DISABLED)
        stand.config(state=T.DISABLED)
        double.config(state=T.DISABLED)

        bet.grid(row=4,column=2)
        setBet.grid(row=4,column=3)
    
    def Stand(players):
        global imgHolder, notBetted

        del imgHolder; notBetted = True
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
        double.config(state=T.DISABLED)

        if ((dealer.value > 21) and (player.value <= 21)) or ((player.value > dealer.value) and (player.value <= 21)):
            result = "Player Wins!"
            player_score.set(player_score.get() + (1 + doubleDown)*bet.get())

        if ((player.value > 21) and (dealer.value > 21)):
            result = "Draw!"

        if ((player.value > 21) and (dealer.value <= 21)) or (dealer.value > player.value):
            if ((player.value > 21) and (dealer.value > 21)):
                result = "Draw!"

            elif (dealer.value <= 21):
                result = "Dealer Wins!"
                player_score.set(player_score.get() - (1 + doubleDown)*bet.get())

        result += f" | Player: {player.value}, Dealer:{dealer.value}"

        # display result and update score
        resultLabel.config(text=result)
        scoreLabel.config(text=f"Score: {player_score.get()}")

        table.update()

        players = None

        table.after(1500,shelf.destroy())

        initGame()

    def DoubleButtonClicked(P, bet):

        player = P[1]

        player.addCard(cards)

        cardObj = player.getCardObject()

        player.value,player.value_list = cardObj.getValue(player.cards)
        player.label = cardObj.label(player.value_list,False)

        player.images.append(cardObj.cardImager(player.cards[-1], cardDir))

        updateDisplay(P)

        doubleDown = True

        Stand(P)

    def startRound(P):
        global imgHolder, notBetted
        notBetted = False

        hit.config(state=T.ACTIVE)
        stand.config(state=T.ACTIVE)
        double.config(state=T.ACTIVE)

        while len(imgHolder) > 1:
            del imgHolder[1]

        bet.config(state=T.DISABLED)
          
        updateDisplay(P)

    def hitButtonClicked(players, bet):

        player = players[1]

        player.addCard(cards)

        cardObj = player.getCardObject()

        double.config(state=T.DISABLED)

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
        global imgHolder, notBetted
        notBetted = True; doubleDown = False
        P = initPlayers()
        initdisplay(P)
        initbuttons(P)
        table.mainloop()
    
    initGame()