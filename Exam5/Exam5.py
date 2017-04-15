import Functions
import json

# Reads in the json file
def readFile():
    jsonText = ""
    file = open('PetStore.json')
    for line in file:
        line = line.strip()
        jsonText = jsonText + line
    items = json.loads(jsonText)
    return items

# Searches through the parsed json using a key entered by the user
def searchByKey(i):
    key = Functions.userString("Please enter a keyword to search:")
    found = False
    for product in i:
        if key.lower() in product["Product"].lower():
            print "%s - $%s" % (product["Product"], product["Price"])
            found = True
    if found == False:
        print "This keyword returned no results."
    
# Searches through the parsed json using a category entered by the user
def searchByCategory(i):
    cat = Functions.userString("Please enter a category to search:")
    found = False
    for product in i:
        if cat.lower() == product["Category"].lower():
            print "%s - $%s" % (product["Product"], product["Price"])
            found = True
    if found == False:
        print "This category does not exist."
            
    

def main():
    items = readFile()
    choice = Functions.userString("Would you like to search by category (c) or keyword (k)?")
    
    if choice == "c":
        searchByCategory(items)
    if choice == "k":
        searchByKey(items)
    
    
main()