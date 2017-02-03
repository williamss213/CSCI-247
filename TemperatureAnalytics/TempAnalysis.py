import Functions

# Read the temps from the file and return them in a list
# Copying the data from canvas did not copy over any line breaks
def readTemps():
    file = open('temps.txt', 'r')
    temps = []
    numbers = []
    
    # This loop will only run once, and it will break that big first line into
    # an array
    for line in file:
        numbers = line.split(' ')
    
    # This second loop turns all of the data into floats so I don't need to 
    # worry about it later.
    for num in numbers:
        num = float(num)
        temps.append(num)
    return temps
    
# Calculates the average of a range of numbers as specified by 
# start (inclusive) and stop (inclusive)
def calculateAve(temps, start, stop):
    total = 0
    index = 1
    count = 0
    for num in temps:
        
        # Only includes the range in the average
        if index >= start and index <= stop:
            total = total + num
            count = count + 1
        index = index + 1
    average = total/count
    return average
            
# Counts all the values that have a positive deviation in the
# range as specified by start (inclusive) and stop (inclusive)
def countPositive(temps, start, stop):
    count = 1
    total = 0
    for num in temps:
        
        # Only includes values in range
        if count >= start and count <= stop and num > 0:
            total = total + 1
        count = count + 1
    return total
    
# Data downloaded from http://climate.nasa.gov/
# Data represents the deviation in global surface temperature
# relative to 1951-1980 average temperatures
def main():
    
    percentSplit = Functions.userFloat("Please enter what percentage split you would like - e.g., .25 for 25%/75%, .60 for 60%/40%: ")
    
    temps = readTemps()
    length = len(temps)
    # integerSplit represents the exact index that the data will be split on
    integerSplit = int(len(temps)*percentSplit)
    # Starting point for second half
    secondStart = integerSplit + 1
    # Size of second half
    secondLength = length - integerSplit
    
    print "During the first %s years, the average deviation from the temperature anomoly  is %s" % (integerSplit, calculateAve(temps, 0, integerSplit))
    print "During the first %s years, %s had a positive temperature anomoly" % (integerSplit, countPositive(temps, 0, integerSplit))
    print "During the last %s years, the average deviation from the temperature anomoly  is %s" % (secondLength, calculateAve(temps, secondStart, length))
    print "During the last %s years, %s had a positive temperature anomoly" % (secondLength, countPositive(temps, secondStart, length))
   
main()