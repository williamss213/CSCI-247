import json
import Functions

# Reads and parses json file
def readFile():
    jsonText = ""
    file = open('Food.json')
    for line in file:
        line = line.strip()
        jsonText = jsonText + line
    food = json.loads(jsonText)
    return food
    
# Searches for any recipe with a name that contains the search term
def searchByName(food, name):
    results = []
    for r in food: 
        if name in r["Name"]:
            results.append(r)
    return results
            
# Searches for any recipe with ingredients that contain the search term
def searchByIngredient(food, i):
    results = []
    for r in food: 
        for ingredient in r["Ingredients"]:
            if i in ingredient:
                results.append(r)
    return results
    
# Searches for any recipe with calories up to the given amount
def searchByCalories(food, cal):
    results = []
    for r in food:
        if int(r["Calories"]) <= cal:
            results.append(r)
    return results
    
# Formats all results from the search and prints them
def printResults(results):
    if len(results) > 0:
        for r in results: 
            iText = ""
            for i in r["Ingredients"]:
                iText = iText + i + ", "
            print "%s - %s- %s calories" % (r["Name"], iText, r["Calories"])
    else:
        print "There were no results found."

    
def main():
    
    food = readFile()
    
    option = Functions.userInt("How would you like to search? 1) by name, 2) by ingredient, 3) by calorie amount:")
    
    if(option == 1):
        name = Functions.userString("What recipe would you like to search for?")
        results = searchByName(food, name)
    if(option == 2):
        ingredient = Functions.userString("What ingredient would you like to search for?")
        results = searchByIngredient(food, ingredient)
    if(option == 3):
        calories = Functions.userInt("What calorie amount would you like to search for? (This will return any recipes up to the amount specified.")
        results = searchByCalories(food, calories)
    
    printResults(results)
    
main()
    