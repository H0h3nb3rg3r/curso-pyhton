#Create a function to simplify writing to files
#Set the function to accept parameters:
#one for text
#one for the name of a file
#Add the code that will write the text out to the file

def writeText(data, fileName):
    file = open(fileName, mode = "w")
    file.write(data)
    return
writeText("Hello, world", "hello.txt")