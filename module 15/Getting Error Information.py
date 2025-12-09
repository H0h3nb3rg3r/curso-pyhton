#E.g. of the code using ZeroDivisonError:
# import sys
# firstNumber = float(input("Enter the first number: "))
# secondNumber = float(input("Enter the second number: "))
# try:
#     result = firstNumber / secondNumber
#     print(result)
# except ZeroDivisionError:
#     print("The answer is infinity")
# finally:
#     print("I will always run!!!")

#Another e.g.:
import sys
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
try:
    result = firstNumber / secondNumber
    print(result)
except ZeroDivisionError:
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]
    print("I'm sorry something went wrong")
    print(error)
finally:
    print("I will always run!!!")
print("This message always displays!")



#How can I force my program to exit?
#use: sys.exit() inside a try or a except or a finally

#Using if statments, use that after the try and the except:
# import sys
# firstNumber = float(input("Enter the first number: "))
# secondNumber = float(input("Enter the second number: "))
# try:
#     result = firstNumber / secondNumber
#     print(result)
# except ZeroDivisionError:
#     print("The answer is infinity")
# except:
#     error = sys.exc_info()[0]
#     print("I'm sorry something went wrong")
#     print(error)
# finally:
#     print("I will always run!!!")
# print("This message always displays!")
#if:
#   noidksfnbadsfdoasnf
#Use like this