def calculation(num1, operation, num2):
    if num1 == None:
        print("Please enter the first number in the operation")
        num1 = float(input())
    if (operation in ["addition", "add", "+"]):
        num1 += num2
        return num1
    elif (operation in ["subtraction", "-", "minus"]):
        num1 -= num2
        return num1
    elif (operation in ["multiplication", "multiply", "*", "x"]):
        num1 *= num2
        return num1
    elif (operation in ["divide", "division", "/"]):
        if (num2 == 0):
            print ("Please don't attempt to divide by 0")
            return None
        num1 /= num2
        return num1
    else:
          print("Plaese Enter a Valid Opperation")
          return
    
def script():
    print("Please enter the operation you'd like to perform")
    operation = input()
    print("Please enter the number you'd like to perform the operation on")
    num2 = float(input()) 
    return operation, num2

print("Please enter the first number in the operation")
num1 = float(input())
operation, num2 = script()
while True:
    num1 = calculation(num1, operation, num2)
    print(num1)
    print("Would you like to perform another operation on this number or exit")
    reply = input()
    if reply == "exit":
        exit()
    operation, num2 = script()
