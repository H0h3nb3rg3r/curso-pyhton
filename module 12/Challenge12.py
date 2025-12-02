#Create a CSV File:

fileName = "Challenge.csv"
WRITE = "w"
#E.g.:APPEND = "a"
#E.g.:READWRITE = "w+"
myFile = open(fileName, mode = WRITE)
#Writing to Files:
#It don't put in a brand new line, you need to put in mannualy:
myFile.write("Susan, 29\n")
myFile.write("Christopher, 31\n")
myFile.write("Bruno, 17\n")
myFile.write("Nicole, 16\n")
myFile.close()

print("File written successfully")