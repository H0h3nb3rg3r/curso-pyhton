#A pirameter is a piece of data

#E.g.:
# def displayMessage(greeting, name):
#     message = greeting + ", " + name
#     print(message)
#     return
# displayMessage("Hi", "Christopher")


#Another e.g.:
# def main():
#     names = ["Christopher", "Susan", "Bruno", "Nicole"]
#     newName = input("Enter last guest: ")
#     names.append(newName)
#     printNames()
#     return
# def printNames(names):
#      for name in names:
#           print(name)
#      return
# main()



#Other e.g.:
# def getMessage(name):
#      message = "Hello," + name
#      return message
# def printMessage(message):
#      print(message)
#      return
# output = getMessage("Christopher")
# printMessage(output)



#Other functional e.g.:
def main():
    names = getNames()
    printNames(names)
    return
def getNames():
    names = ["Christopher", "Susan", "Bruno", "Nicole"]
    newName = input("Enter last guest: ")
    names.append(newName)
    return names
def printNames(names):
    for name in names:
        print(name)
    return
main()
#We also can do it with numbers, just put int or float before the input