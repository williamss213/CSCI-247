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
