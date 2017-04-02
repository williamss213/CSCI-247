import os
import Functions

# gathers files and returns a dictionary with the format (fileName, [])
def findFiles():
    files = os.listdir(".")
    textFiles = {}
    for f in files:
        if f[-3:] == "txt":
            textFiles[f] = []
    return textFiles
        
# searches through files and adds valid lines into the list for its respective file   
def searchFiles(names, term):
    for f in names.keys():
        file = open(f, 'r')
        for line in file:
            line = line.upper().strip()
            if term in line:
                names[f].append(line)
    return names            

# prints out the results with formatting    
def printResults(r):
    for name in r.keys():
        for line in r[name]:
            print ("%s: %s" % (name, line))
    
    
def main(): 
    searchTerm = Functions.userString("Please enter the word you would like to search:").upper()
    
    fileNames = findFiles()
    
    results = searchFiles(fileNames, searchTerm)
    
    printResults(results)
    
main()
    
    
    