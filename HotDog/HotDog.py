import Functions
import random
import time

# Checks for a winner at each score interval
# But how do I make sure they don't tie?!?
def eat(players):
    count = 0
    w = ""
    for key in players.keys():
        players[key] = random.randrange(1,6) + players[key]
        print "%s has eaten %s too many!" % (key, players[key])
        if players[key] >= 50:
            w = key
            count = count + 1 
    if count > 0:
        return w
    else:
        return "None"
        

# Runs through the contest and returns the name of the winner
def runContest():
    players = {"Tom" : 0, "Sally" : 0, "Fred" : 0}
    winner = "None"
    
    while winner == "None":
        print "Gross noises of people eating way too many hot dogs . . . "
        print
        time.sleep(1)

        winner = eat(players);
    return winner    
    
    
def main():
    money = 150
    
    while money > 0:
        pick = Functions.userString("Pick a winner (Tom, Sally, or Fred)")
        bet = Functions.userInt("How much do you want to bet? Cash = %s" % money)
        print "Aaaaaaand go!!"
        
        winner = runContest()
        print "The winner is %s!" % winner
        if winner == pick:
            money = money + bet
            print "You've won! You now have $%s. :)" % money
            
        else: 
            money = money - bet
            print "You've lost! You now have $%s. :(" % money
    print "There are no more hot dogs in the entire world, sorry!"
    
    
main()