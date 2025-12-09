#You made a shopping list and forget it at home


#Syntax erros:
#print(Hello World")
#prnit("Hello World")


#E.g. of a calculator:
# firstNumber = float(input("Enter the first number: "))
# secondNumber = float(input("Enter the second number: "))

# result = firstNumber / secondNumber

# print(result)




#Using try and except:
# firstNumber = float(input("Enter the first number: "))
# secondNumber = float(input("Enter the second number: "))
# try:
#     result = firstNumber / secondNumber
#     print(result)
# except:
#     print("I'm sorry something went wrong")

#Using sys:
import sys
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
try: #try this:
    result = firstNumber / secondNumber
    print(result)
except: #if try doesn't work, try this:
    error = sys.exc_info()[0]
    print("I'm sorry something went wrong")
    print(error)
finally: #finnaly, after try and except, it will always be working:
    print("I will always run!!!")