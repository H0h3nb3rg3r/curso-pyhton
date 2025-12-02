#How do you write to a file with code?
#Use the open function:

#myFile = open(fileName, accessMode)

#You need to specify:
#full name
#access mode

#What is the file name:
#You need to put the name AND the extension, e.g.:
#data.txt
#cristopher.pdf


#What is access mode?:
#Is what you will do with the file:
#Acess mode | Action
#   r       | read the file
#   w       | write to the file
#   a       | append to the existinh file content
#   b       | open a binary file

#E.g.:
fileName = "GuestList.txt"
WRITE = "w"
#E.g.:APPEND = "a"
#E.g.:READWRITE = "w+"
myFile = open(fileName, mode = WRITE)
#Writing to Files:
#It don't put in a brand new line, you need to put in mannualy:
myFile.write("Hi there!\n")
myFile.write("How are you?")
myFile.close()

print("File written successfully")