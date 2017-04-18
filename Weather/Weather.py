import json
import urllib2
import Functions

# Gathers info from the API and puts the relevant info into an array. 
# Handles exceptions for a bad request. If that occurs, it returns an empty array
# And the program skips the rest of the while loop.
def gatherInformation(degree, c):
    url = "https://api.apixu.com/v1/current.json?key=369d9f23d92242feb1325926171804&q=" + c
    try:
        jsonText = urllib2.urlopen(url).read()
    except urllib2.HTTPError:
        print("Bad city name or zipcode. Please try again.\n")
        return []
    w = json.loads(jsonText)
    stats = (w["location"]["name"], w["location"]["region"], w["current"]["condition"]["text"], w["current"]["temp_" + degree],
             w["current"]["feelslike_" + degree])
    return stats
    

# stats = [city name, region, condition, actual degrees, real feel degrees]
def printInformation(stats, d):
    print "\nHere is the weather for %s, %s." % (stats[0], stats[1])
    print "%s and %s degrees (%s)." % (stats[2], stats[3], d.upper())
    print "It actually feels like %s (%s).\n" % (stats[4], d.upper())

def main():
    keepGoing = True
    while keepGoing: 
        city = Functions.userString("Please enter a zipcode or a city name:")
        degreeFormat = Functions.userString("Would you like degrees in Celsius (c) or Fahrenheit (f)?")
        stats = gatherInformation(degreeFormat, city)
        # Checks that the stats array was valid.
        if len(stats) > 0:
            printInformation(stats, degreeFormat)
            choice = Functions.userString("Would you like to check another location (y/n)?")
            if choice == "n":
                keepGoing = False
        

main()

