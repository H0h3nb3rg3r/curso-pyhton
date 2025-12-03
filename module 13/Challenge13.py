#Write a program that will print the names and ages of the guests in the guest list file you created in the last module


GuestList = open("GuestList.txt", "r")
AllFileContents = GuestList.read()
print(AllFileContents)