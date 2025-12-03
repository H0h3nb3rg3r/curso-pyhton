#Functions:
#do the same things and tasks again and again and again
#You can just create a "button" in your code to do it

#it's like a method - have a name


#Some functions that we alreasy use:
#print
#open
#write
#close

#They reduce and simplify your code, thei also make it easier to make changes

#E.g.:
# def printMessage():
#     print("Hello World")
#     return
#printMessage()

#Another e.g.:
# #When someone calls this function, execute this code:
# def main():
#     printMessage()
#     return
# def printMessage():
#      print("Hello World")
#      return
# #Executes the main function, in order to do that the funcion must be created:
# main()


#Other e.g.:
def main():
    printNames()
    return
def printNames():
     names = ["Christopher", "Susan", "Bruno", "Nicole"]
     for name in names:
          print(name)
     return
main()