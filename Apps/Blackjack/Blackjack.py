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

    table = T.Toplevel(OS,bg=color.get())
    table.title("Blackjack")
    table.transient(OS)
    table.iconphoto(False, ImageTk.PhotoImage(Image.open(f"{cardDir}\\{cards}\\{card}")))

    cards = os.listdir(cardDir)

    #functions
    def roundStart(cards):
        dealerHand = []
        playerHand = []
        for startingCards in range(2):
            dealerHand.append(random.choice(cards))
            playerHand.append(random.choice(cards))
        
        return [dealerHand,playerHand]
    
    def cardValues(cardsInPlay):
        valueDisp = []
        for hand in cardsInPlay:
            a, b = 0, 0
            if (hand[0] in "AJKQ") and not (hand[1] in "AJKQ"):
                b = int(hand[1])
                if hand[0] in "JKQ":
                    a = 10
                elif hand[0] in "A":
                    a = [1,11]
            elif (hand[1] in "AJKQ") and not (hand[0] in "AJKQ"):
                a = int(hand[0])
                if hand[1] in "JKQ":
                    b = 10
                elif hand[1] in "A":
                    b = [1,11]
            elif (hand[1] and hand[0]) not in  "AJKQ":
                a = int(hand[0])
                b = int(hand[1])
            elif (hand[1] and hand[0]) in  "AJKQ":
                if hand[0] in "JKQ":
                    a = 10
                elif hand[0] in "A":
                    a = [1,11]
                if hand[1] in "JKQ":
                    b = 10
                elif hand[1] in "A":
                    b = [1,11]
            valueDisp.append([a,b])
        return valueDisp

    def labelMaker(val,Bool):
        n = 1
        if Bool != False:
            string = "Dealer's Hand: "
            for x in val:
                if n < len(val):
                    string += f"{x} + "
                else:
                    string += "?"
                n += 1
        elif Bool != True:
            string = "Player's Hand: "
            for x in val:
                if n < len(val):
                    string += f"{x} + "
                else:
                    string += f"{x}"
                n += 1
        return string

    def cardloader(cardsInHand,Bool,canvas):
        imgHolder = []
        cardWidth = 128
        if Bool == True:
            height = 0
            for i, card in enumerate(cardsInHand):
                imgDir = random.choice(os.listdir(f'{cardDir}\\{card}'))
                image = Image.open(f"{cardDir}\\{card}\\{imgDir}")
                image = image.resize((cardWidth, cardWidth))
                cardImg = ImageTk.PhotoImage(image)
                imgHolder.append(cardImg)
                x = i * cardWidth
                img_tag = canvas.create_image(x, height, image=cardImg, anchor=T.NW)

                if i + 1 >= len(cardsInHand):
                    image = Image.open(f"{appDir}\\Blank\\Blank.png")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg)
                    x = i * cardWidth
                    img_tag = canvas.create_image(x, height, image=cardImg, anchor=T.NW)

        elif Bool == False:
            height = cardWidth
            for i, card in enumerate(cardsInHand):
                imgDir = random.choice(os.listdir(f'{cardDir}\\{card}'))
                image = Image.open(f"{cardDir}\\{card}\\{imgDir}")
                image = image.resize((cardWidth, cardWidth))
                cardImg = ImageTk.PhotoImage(image)
                imgHolder.append(cardImg)
                x = i * cardWidth
                img_tag = canvas.create_image(x, height, image=cardImg, anchor=T.SW)
        else:
           raise ValueError
        
        return imgHolder
        

    def display(cardsInPlay,valueDisp):

        dealers = T.Canvas(table,bg=color.get(),height=128)
        dealers.grid(row=1,columnspan=3)
        dealer_text = labelMaker(valueDisp[0],True)
        dealer_label = T.Label(table,text = dealer_text,bg=color.get())
        dealer_label.grid(row=0,columnspan=3)
        dealer_cards = cardloader(cardsInPlay[0],True,dealers)

        players = T.Canvas(table,bg=color.get(),height=128)
        players.grid(row=2,columnspan=3)
        player_text = labelMaker(valueDisp[1],False)
        player_label = T.Label(table,text = player_text,bg=color.get())
        player_label.grid(row=3,columnspan=3)
        player_cards = cardloader(cardsInPlay[1],False,players)

        table.mainloop()
    
    # game steps
    cardsInPlay = roundStart(cards)
    valueDisp = cardValues(cardsInPlay)
    display(cardsInPlay,valueDisp)