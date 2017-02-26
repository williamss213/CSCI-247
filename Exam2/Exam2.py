# Sara Williams
# Programming in Python
# Exam 2

# Reads in data from a file while sorting it into proper categories
def buildDictionary(fileName):
    d = {"Cube Head" : [], "Square Master" : [],
            "Advanced Twister" : [],
            "Intermediate Turner" : [],
            "Average Mover" : [], "Pathetic" : []
         }
    file = open(fileName, 'r')
    for line in file:
        line = line.split(',')
        name = line[0].strip()
        time = float(line[1].strip())
        
        if time >= 0 and time < 10:
            d["Cube Head"].append(name)
        if time >= 10 and time < 20:
            d["Square Master"].append(name)
        if time >= 20 and time < 30:
            d["Advanced Twister"].append(name)
        if time >= 30 and time < 40:
            d["Intermediate Turner"].append(name)
        if time >= 40 and time < 60:
            d["Average Mover"].append(name)
        if time >= 60:
            d["Pathetic"].append(name)
    return d
            
# Prints out a dictionary in a specific format, order had to be hardcoded because
# dictionaries do not retain order.
def printDictionary(d):
    print "\nCube Head (0 - 9.99):"
    for n in d["Cube Head"]:
        print "\t" + n
    
    print "\nSquare Master (10 - 19.99):"
    for n in d["Square Master"]:
        print "\t" + n
    
    print "\nAdvanced Twister (20 - 29.99):"
    for n in d["Advanced Twister"]:
        print "\t" + n
    
    print "\nIntermediate Turner (30 - 39.99):"
    for n in d["Intermediate Turner"]:
        print "\t" + n
    
    print "\nAverage Mover (40 - 59.99):"
    for n in d["Average Mover"]:
        print "\t" + n
        
    print "\nPathetic (60 and beyond):"
    for n in d["Pathetic"]:
        print "\t" + n
       
    
    
def main():
    d = buildDictionary("Timings.txt")
    printDictionary(d)
    
main()