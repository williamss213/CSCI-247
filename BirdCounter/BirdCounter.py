# Programming in Python - Assignment 4
# Sara Williams
# Badge Attempt

import Functions

# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------

###### Function was moved to Functions.py

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    bird = Functions.userString("Please enter a bird name:")
    
    # Enables the user to look up birds until they enter exit.
    while bird != "Exit":
        bird = bird.lower()
        
        if bird in d:
            print "I have seen that bird %s time(s)." % d[bird]
        else:
            print "I have seen that bird 0 time(s)."
            
        # Finding most viewed bird. searchValue is the highest value in a sorted list
        # of the values. searchValue is then used to make sure only keys with values 
        # that match the searchValue are being printed.
        values = sorted(d.values())
        searchValue = values[len(values)-1]
        for key in d.keys():
            if d[key] == searchValue:
                print "The most viewed bird is the %s, which has been seen %s time(s)." % (key, d[key])
        print
        bird = Functions.userString("Please enter a bird name:")
    
        


def main():
    birds = Functions.fileToDictionary('birds.txt')
    askUser(birds)

main()