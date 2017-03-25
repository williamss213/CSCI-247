import Functions

def buildDeck(rank, suit):
    d = []
    for r in rank:
        for s in suit: 
            d.append(r +  " of " + s)
    return d

def shuffle(deck):
    first = deck[:26]
    second = deck[26:]
    d = []
    
    # This will accomplish the perfect shuffle without the need for mod
    for i in range(26):
        d.append(first[i])
        d.append(second[i])
    return d

def deal(deck):
    return deck[:5]

def main():
    rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit = ["Clubs", "Hearts", "Diamonds", "Spades"]
    
    deck = buildDeck(rank, suit)

    times = Functions.userInt("How many times would you like to shuffle the deck?")
    
    for i in range(times):
        deck = shuffle(deck)

    print deal(deck)
    
main()
