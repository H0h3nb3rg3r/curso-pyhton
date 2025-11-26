#Calculate the total to charge for an order from an online store in Canada
#Ask user what country they are from and their order total
#If the user is from Canada, ask which province
#If the order is from outside Canada do not charge any taxes
#If the order was placed in Canada calculate tax based on the province:
#Alberta charge .05% General sales Tax (GST)
#Ontario, New Brunswick, Nova Scotia charge .13% Harmonized sales tax
#All other provinces charge .06% provincial sales tax + .05% GST tax

print("WELCOME TO OUR CANADIAN ONLINE STORE")
sell = 100
print("Your sell is $100")
country = input("What country are you from? ").upper()
if country == "CANADA":
    province = input("What province are you from? ").upper()
    if province == "ALBERTA":
        print("You got 5 per cent of GST")
        abertaSell = sell * 1.05
        print("Your new total with taxes is going to be $", abertaSell)
    elif province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
        print("You got 13 per cent of Harmonized sales tax")
        onnSell = sell * 1.13
        print("Your new total with taxes is going to be $", onnSell)
    else:
        print("You got 6 per cent of GST")
        othersSell = sell * 1.06
        print("Your new total with taxes is going to be $", othersSell)
else:
    print("You got no taxes!!!")
    print("Your total is going to be $", sell)