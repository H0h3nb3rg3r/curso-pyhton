#you need to import CSV:
import csv
#dataFromFile = csv.reader(mtCSVfile)
#dataFromFile = csv.reader(myCSVfile, delimiter=",")

#E.g. of open and read:
# fileName = "GuestList.txt"
# accessMode = "r"
# with open(fileName, accessMode) as myCSVfile:
#     dataFromFile = csv.reader(myCSVfile)
#with it's like a loop or something to automatically do the reader


#E.g.:
with open("Tasmania.txt", "r") as AnimalFile:
    allRowsList = csv.reader(AnimalFile)
    for currentRow in allRowsList:
        print(currentRow)
        for currentWord in currentRow:
            print(currentWord)
#Row = "linha" in portuguese






#E.g. of printing individual values:
# for row in dataFromFile:
#     for value in row:
#         print(value + "\n")


#E.g. of removing the brackets and quotes:
# for row in dataFromFile:
#     print(",".join(row))