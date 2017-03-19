def userList(prompt):
    print prompt, 
    line = raw_input()
    l = line.split(",");
    return l

def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userFloat(prompt):
    print prompt,
    num = float(raw_input())
    return num

def userString(prompt):
    print prompt,
    text = raw_input()
    return text

def kmToMi(km):
    return 0.62 * km

#Turns a file with comma-separated key, value pairs into a dictionary. 
#Expects value to be an int.

def fileToDictionary(filename):
    d = {}
    file = open(filename, 'r')
    for line in file:
        line = line.lower().split(',')
        key = line[0].strip()
        value = line[1].strip()
        
        if key in d:
            d[key].append(value)
        else:
            d[key] = value
    return d