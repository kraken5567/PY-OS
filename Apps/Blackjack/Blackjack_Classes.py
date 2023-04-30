import random
import os
from PIL import ImageTk, Image
import tkinter as T

class Cards:

    def __init__(self):
        None

    #creates "Hand" which contains cards (letters and numbers)
    def initcards(self,cards):
        Hand = []
        for startingCards in range(2):
            Hand.append(random.choice(cards))
        return Hand
    
    #list of the values of the cards in "Hand"
    def getValue(self,Hand):
        value_list = []
        for Card in Hand:
            if Card in "AJKQ":
                if Card in "JKQ":
                    value = 10
                elif Card == "A":
                    value = [11, 1]
            else:
                value = int(Card)
            value_list.append(value)

        # Handle aces
        if any(isinstance(val, list) for val in value_list):
            value = 0
            for val in value_list:
                if isinstance(val, list):
                    if value + val[0] <= 21:
                        value += val[0]
                    else:
                        value += val[1]
                else:
                    value += val
        else:
            value = sum(value_list)

        return value, value_list
        """ value_list = []
        for Card in Hand:
            if (Card in "AJKQ"):
                if Card in "JKQ":
                    value = 10
                elif Card in "A":
                    value = [11,1]
            else:
                value = int(Card)
            value_list.append(value)
        value = 0
        for val in value_list:
            if type(val) != int:
                for num in val:
                    if value + num <= 21:
                        value += num
                        break
            else:
                value += val

        return value, value_list """

    #retruns string as, num + num... OR num + ... + ?
    def label(self,value_list,Bool):
        n = 1
        if Bool == True:
            string = "Dealer's Hand: "
            for x in value_list:
                if n < len(value_list):
                    string += f"{x} + "
                else:
                    string += "?"
                n += 1
        elif Bool == False:
            string = "Player's Hand: "
            for x in value_list:
                if n < len(value_list):
                    string += f"{x} + "
                else:
                    string += f"{x}"
                n += 1
        return string
    
    #creates a list of images for TKinter
    def cardImager(self,Hand,cardDir):
        imgHolder = []
        cardWidth = 128
        for i, card in enumerate(Hand):
                try:
                    imgDir = random.choice(os.listdir(f'{cardDir}\\{card}'))
                    image = Image.open(f"{cardDir}\\{card}\\{imgDir}")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg)
                except FileNotFoundError:
                    if type(Hand) == list:
                        imgDir = random.choice(os.listdir(f'{cardDir}\\{Hand[i]}'))
                        image = Image.open(f"{cardDir}\\{card}\\{imgDir}")
                    else: 
                        imgDir = random.choice(os.listdir(f'{cardDir}\\{Hand}'))
                        image = Image.open(f"{cardDir}\\{Hand}\\{imgDir}")
                    image = image.resize((cardWidth, cardWidth))
                    cardImg = ImageTk.PhotoImage(image)
                    imgHolder.append(cardImg)
        return imgHolder
    
class Player:

    #call with: (card list) and (Dealer/Player as True/False) and (Card's Directory)
    def __init__(self,cards,Bool,cardDir):
        self.Object = Cards()
        self.cards = self.Object.initcards(cards)
        [self.value, self.value_list] = self.Object.getValue(self.cards)
        self.label = self.Object.label(self.value_list,Bool)
        self.images = self.Object.cardImager(self.cards,cardDir)
    
    #returns card object
    def getCardObject(self):
        return self.Object

    #adds a card
    def addCard(self,cards):
        (self.cards).append(random.choice(cards))
        return self.cards

    #returns a list of Card(list of str), [total card value, Card values(list of int)], label(str), images(PIL object)
    def Return(self):
        return self.cards, [self.value,self.value_list], self.label, self.images
        