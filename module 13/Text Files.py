#Text files:
#Shopping list

#Search "open data" on internet or "open data and your city or state or country"


#What is access mode?:
#Is what you will do with the file:
#Acess mode | Action
#   r       | read the file
#   w       | write to the file
#   a       | append to the existinh file content
#   b       | open a binary file

#to read:
#fileContent = myFile.read
#to read one line per time:
#fileContent = myFile.readline


#E.g.:
#Open my file
AnimalFile = open("Tasmania.txt", "r")
AllFileContents = AnimalFile.read()
print(AllFileContents)

firstAnimal = AnimalFile.readline()
print(firstAnimal)
secondAnimal = AnimalFile.readline()
print(secondAnimal)