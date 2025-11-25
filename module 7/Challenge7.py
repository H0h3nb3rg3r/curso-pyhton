#Calculate shipping charges for a shopper
#Ask the user to enter the amount for their total purchase
#If their total is under $50 add $10, otherwise shipping is free
#Tell the user their final total including shipping costs and format the number so it looks a monetary value - "$" symbol
#Don't forget to test your solution with:
#a value > 50
#a value < 50
#a value of exactly 50

purchase = float(input("How much is your purchase? "))
if purchase < 50:
    newValue = purchase + 10
    print("You got $10 as a shipping fee")
    print("Your purchase value is:", newValue)
else:
    print("You got shipping free")
    print("You purchase value is:", purchase)