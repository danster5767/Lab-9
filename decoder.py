key = {"4":"1", "5":"2", "6":"3", "7":"4", "8": "5", "9":"6", "1":"7", "8":"2", "9":"3"}

def decoder(value):
    newValue = ""
    for i in range(len(value)):
        newValue += key.get(value[i])
    return newValue