# Sara Williams
# Exam 3

import Functions
import random 

# Builds and returns a shuffled deck of 10 cards, with one repeated card. 
def buildDeck():
    cards = ["Unicorn", "Lion", "Giant Anteater", "Narwhal", "Doggo", "Snow Leopard", "River Dolphin", "Gryphon", "Smaug"]
    cards.append(cards[random.randrange(0,9)])
    random.shuffle(cards)
    
    return cards

# Allows a player to pick two cards. Checks if they are valid guesses, and then 
# checks if there is a match. Returns false if a match has been found, true if not. 
# This is used to control the while loop.
def playerTurn(c):
    cardOne = Functions.userInt("Please pick your first card (0-9):")
    cardTwo = Functions.userInt("Please pick your second card (0-9):")
    
    if cardOne > -1 and cardOne < 10 and cardTwo > -1 and cardTwo < 10 and cardTwo != cardOne:
        print "Card %s is a(n) %s!" % (cardOne, c[cardOne])
        print "Card %s is a(n) %s!" % (cardTwo, c[cardTwo])
        
        if c[cardOne] == c[cardTwo]:
            return False
        else:
            return True
    else:
        print "Invalid guess! You must guess two different cards between 0-9."
        return True

def main():
    deck = buildDeck()
    tries = 0
    playing = True
    while playing:
        tries = tries + 1
        playing = playerTurn(deck)
    print "Congrats! You've won in %s turns!" % tries
        

main()