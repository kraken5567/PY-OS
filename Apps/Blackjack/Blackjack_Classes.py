import random
import os
from PIL import ImageTk, Image
import tkinter as T

class Cards:
    
    #creates "Hand" which contains cards (letters and numbers)
    def initHand(self,cards):
        Hand = []
        for startingCards in range(2):
            Hand.append(random.choice(cards))
        return Hand
    
    #list of the values of the cards in "Hand"
    def getValue(self,Hand,):
        value_list = []
        for Card in Hand:
            if (Card in "AJKQ"):
                if Card in "JKQ":
                    value = 10
                elif Card in "A":
                    value = [1,11]
            else:
                value = int(Card)
            value_list.append(value)
        return value_list

    #retruns string as, num + num... OR num + ... + ?
    def label(self,value_list,Bool):
        if Bool != False:
            string = "Dealer's Hand: "
            for x in value_list:
                if n < len(value_list):
                    string += f"{x} + "
                else:
                    string += "?"
                n += 1
        elif Bool != True:
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
                imgDir = random.choice(os.listdir(f'{cardDir}\\{card}'))
                image = Image.open(f"{cardDir}\\{card}\\{imgDir}")
                image = image.resize((cardWidth, cardWidth))
                cardImg = ImageTk.PhotoImage(image)
                imgHolder.append(cardImg)
        return imgHolder
    
class Canvas:

    #takes list of Images
    def createImages(canvas,Images):
        cardWidth = 128
        createdImages = []
        for n, card in enumerate(Images):
            x = n * cardWidth
            img_tag = canvas.create_image(x, 0, image=Images[n], anchor=T.NW)
            createdImages.append(img_tag)
        return createdImages
        