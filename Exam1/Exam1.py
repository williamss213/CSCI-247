# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    speeds = []
    file = open(filename, 'r')
    for line in file:
        speeds.append(float(line))
    return speeds
        
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    total = 0
    for num in l:
        total = total + num
    average = total/len(l)
    return average
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    count = 0
    for num in l:
        if num > maxSpeed:
            count = count + 1
    
    return count
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    maxspeed = 69
    rushHourFine = 150
    regFine = 100
    
    #Reading data
    rushHourSpeeds = readData('data-rush.txt')
    regSpeeds = readData('data-not-rush.txt')
    
    #Finding averages
    print "The average speed during rush hour was %.2f." % getAverage(rushHourSpeeds)
    print "The average speed not during rush hour was %.2f." % getAverage(regSpeeds)
    
    #Finding total speeders & fines
    rushHourCount = countSpeeders(rushHourSpeeds, maxspeed)
    regCount = countSpeeders(regSpeeds, maxspeed)
    print "There were %.0f speeders during rush hour. Total fine = $%.2f" % (rushHourCount, rushHourCount*rushHourFine)
    print "There were %.0f speeders during rush hour. Total fine = $%.2f" % (regCount, regCount*regFine)
    

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()