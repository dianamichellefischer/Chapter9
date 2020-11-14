"""
File: CH9_P9.py
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from cards import Deck, Card
import os

class dealCards(EasyFrame):
    """Illustrates command"""
    

    def __init__(self):
        """Sets up the GUI"""
        EasyFrame.__init__(self, title = "Game Time")
        self.setSize(440, 400)
        self.cardLabel1 = self.addLabel("", row = 0,
                                       column = 0,
                                       sticky = "NSEW")
        self.cardLabel2 = self.addLabel("", row = 0,
                                       column = 1,
                                       sticky = "NSEW")
        self.cardLabel3 = self.addLabel("", row = 0,
                                       column = 2,
                                       sticky = "NSEW")
        self.stateLabel = self.addLabel("", row = 1, column = 0,
                                        sticky = "NSEW",
                                        columnspan = 2)
        self.addButton(row = 2, column = 0,
                       text = "New game",
                       command = self.newDeal)
        self.addButton(row = 2, column = 2,
                       text = "Quit",
                       command = self.quit)


    def newDeal(self):
        """new deal shows 2 cards from the deck and the back of a card/the deck"""
        self.deck = Deck()
        self.deck.shuffle()
        self.card1 = self.deck.deal()
        self.card2 = self.deck.deal()
        self.card3 = self.deck.deal()
        self.stateLabel["text"] = ""
        self.card1.faceUp = True
        self.card2.faceUp = True
        self.refreshImages()



    def exit(self):
        return False

    def refreshImages(self):
        """brings images from the DECK folder"""
        fileName1 = "DECK/" + str(self.card1) + ".gif"
        fileName2 = "DECK/" + str(self.card2) + ".gif"
        fileName3 = "DECK/" + str(self.card3) + ".gif"
        fileName4 = "DECK/" + "b.gif"
        if self.card1.faceUp == False:
            self.image1 = PhotoImage(file = fileName4)
            self.cardLabel1["image"] = self.image1
        else:
            self.image1 = PhotoImage(file = fileName1)
            self.cardLabel1["image"] = self.image1
        if self.card2.faceUp == False:
            self.image2 = PhotoImage(file = fileName4)
            self.cardLabel2["image"] = self.image2
        else:
            self.image2 = PhotoImage(file = fileName2)
            self.cardLabel2["image"] = self.image2
        if self.card3.faceUp == False:
            self.image3 = PhotoImage(file = fileName4)
            self.cardLabel3["image"] = self.image3
        else:
            self.image3 = PhotoImage(file = fileName3)
            self.cardLabel3["image"] = self.image3




def main():
    """Instantiate and pop up the window."""
    dealCards().mainloop()

if __name__ == "__main__":
    main()
