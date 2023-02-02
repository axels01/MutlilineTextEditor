from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    # Opens file dialog
    Tk().withdraw()
    global filename
    filename = askopenfilename()

    # Opens file and reads data into list
    file = open(filename, "r")
    data = []
    for line in file:
        data.append(line)

    operations = {
        "d": "delete characters",
        "i": "insert characters",
        "r": "replace characters",
        "x": "exit"
    }

    print("Selected file: " + filename)
    print("\n")
    print("Operations:")
    for line in operations:
        print(line + " - " + operations[line])
    print("\n")
    operation = input("Enter operation: ")
    
    if operation != "x" or "d" or "i" or "r":
        print("Invalid operation")
        return

    if operation == "d":
        charRange = input("Delete, enter character range (ex. 12:18): ")
        save(remove(charRange, data))
    
    elif operation == "i":
        insertPoint = input("Insert, enter insert point (ex. 12): ")
        character = input("Insert, enter character(s) (ex. a): ")
        save(insert(insertPoint, character, data))

    elif operation == "r":
        charRange = input("Replace, enter character range (ex. 12:18): ")
        character = input("Replace, enter character(s) (ex. a): ") 
        # Runs remove function, then runs insert function
        save(insert(charRange.split(':')[0], character, remove(charRange, data)))


def remove(charRange, data):
    # Splits character range into start and endpoint
    charRange = [int(x) for x in charRange.split(':')]

    for i, line in enumerate(data):
        data[i] = line[:charRange[0]] + line[charRange[1]:]
    
    return data


def insert(insertPoint, character, data):
    # Inserts character at insert point
    for i, line in enumerate(data):
        data[i] =  line[:int(insertPoint)] + character + line[int(insertPoint):]
    
    return data
        


def save(data):
    # Breaks filename into path steps
    path = filename.split('/')
    # Replaces filename with edited filename
    path = filename.replace(path[-1], path[-1].split('.')[0] + "_edited." + path[-1].split('.')[1])

    file = open(path, "w")
    for line in data:
        file.write(line)


if __name__ == '__main__':
    main()  