def Main(OS):
    import tkinter as T
    import os
    import importlib.util
    from PIL import ImageTk, Image
    import random

    table = T.Toplevel(OS)
    table.title("Blackjack")
    table.transient(OS)
    
    #cards ar 2.5in x 3.5in; W x H
    # card images made by Aussiesim from Game-Icons.net

    ProgDir = "Apps"
    ProgFolder = "Blackjack"
    appDir = f"{ProgDir}\\{ProgFolder}"
    cardDir = f"{appDir}\\Cards"

    cardsLib = os.listdir(cardDir)
    cards = random.choice(cardsLib)
    card = random.choice(os.listdir(f"{cardDir}\\{cards}"))
    print(f"{cardDir}\\{cards}\\{card}")
    table.iconphoto(False, ImageTk.PhotoImage(Image.open(f"{cardDir}\\{cards}\\{card}")))

    
    #init values
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
            valueDisp.append([a,b])
        return valueDisp

    def display(cardsInPlay,valueDisp,cardDir):
        print(cardsInPlay,valueDisp)

        # make canvas

        for hand in cardsInPlay:
            for card in hand:
                # detect first player (dealer) so one card is hidden
                cardImage = random.choice(os.listdir(f"{cardDir}\\{card}"))
                # add to list
                # display on canvas
                # change position
    # game steps
    cardsInPlay = roundStart(cards)
    valueDisp = cardValues(cardsInPlay)
    display(cardsInPlay,valueDisp,cardDir)

    
    
    table.mainloop()