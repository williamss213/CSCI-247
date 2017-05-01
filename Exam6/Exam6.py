import Functions

# Gets clue information from the user and removes anything containing the clue from 
# the list of possibilities.
def processClue (p, s, w):
    opt = Functions.userString("Is the clue a suspect or a weapon? (s or w):")
    if opt.lower() == "s":
        clue = Functions.userString("Enter the innocent person (%s):" % s)
    elif opt.lower() == "w":
        clue = Functions.userString("Enter the weapon that was not used (%s):" % w)
    else:
        print "Not a valid option"
    # Adds possibilities to be cleared to another list, because 
    # removing items while iterating is a bad time.
    cleared = []
    for item in p:
        if clue.lower() in item.lower():
            cleared.append(item)
    # Loops through cleared possibilities and removes them.
    for i in cleared:
        p.remove(i)
    return p
    
    # Generates a list of possibilities formatted as strings that are ready to be printed.
def generatePossibilities(suspect, weapon):
    p = []
    for s in suspect:
        for w in weapon:
            p.append("%s with the %s" % (s, w))
    return p
    
def main():
    suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
    weapons = ["Lead Pipe", "Candlestick", "Wrench"]
    possibilities = generatePossibilities(suspects, weapons)
    while len(possibilities) > 1:
        print "There are %s possibilities left." % len(possibilities)
        possibilities = processClue(possibilities, suspects, weapons)
    print "There is only one possibility left."
    print "It was %s!" % possibilities[0]
    
main()