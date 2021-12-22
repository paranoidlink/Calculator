usrinput = None
inputlst = []
prevResult = None
run = False

def addition(prevResult, run):
    result = 0

    if prevResult != None:
        inputlst.append(prevResult)

    print("Type any numbers you'd like to add together, then type run to perform the opperation")
    while run == False:
        usrInput = input()
        try:
            usrInput = int(usrInput)
            inputlst.append(usrInput)
        except ValueError:
            usrInput = str(usrInput)

    
        if usrInput == "run":
            run = True
            break

    if run == True:
        for i in range(len(inputlst)):
            result += inputlst[i]
            prevResult = result
        inputlst.clear()
        print(result)
        run = False
        return prevResult

def subtraction(prevResult, run):
    result = 0

    if prevResult != None:
        inputlst.append(prevResult)

    print("Type any numbers you'd like to subtract, then type run to perform the opperation")
    while run == False:
        usrInput = input()
        try:
            usrInput = int(usrInput)
            inputlst.append(usrInput)
        except ValueError:
            usrInput = str(usrInput)

    
        if usrInput == "run":
            run = True
            break

    if run == True:
        result = inputlst[0]
        for i in range(len(inputlst)-1):
            result -= inputlst[i+1]
            prevResult = result
        inputlst.clear()
        print(result)
        run = False
        return prevResult

def multiplication(prevResult, run):
    result = 0

    print("Type any numbers you'd like to multiply, then type run to perform the opperation")
    if prevResult != None:
        inputlst.append(prevResult)

    while run == False:
        usrInput = input()
        try:
            usrInput = int(usrInput)
            inputlst.append(usrInput)
        except ValueError:
            usrInput = str(usrInput)

    
        if usrInput == "run":
            run = True
            break

    if run == True:
        result = inputlst[0]
        for i in range(len(inputlst)-1):
            result *= inputlst[i+1]
            prevResult = result
        inputlst.clear()
        print(result)
        run = False
        return prevResult

def division(prevResult, run):
    result = 0

    if prevResult != None:
        inputlst.append(prevResult)

    print("Type any numbers you'd like to divide, then type run to perform the opperation")
    while run == False:
        usrInput = input()
        try:
            usrInput = int(usrInput)
            inputlst.append(usrInput)
        except ValueError:
            usrInput = str(usrInput)

    
        if usrInput == "run":
            run = True
            break

    if run == True:
        result = inputlst[0]
        for i in range(len(inputlst)-1):
            result /= inputlst[i+1]
            prevResult = result
        inputlst.clear()
        print(result)
        run = False
        return prevResult

def clear():
    inputlst.clear
    prevResult = None
    return prevResult

while True:
    print("Type the opperation you'd wish to perform 'addition', subtraction', mutiplication or division, or their respective symbols you can type clear to clear the memory of your last result and exit to exit the program")
    usrinput = str(input())
    if usrinput == "addition" or "+":
        prevResult = addition(prevResult, run)
    if usrinput == "subtraction" or "-":
        prevResult = subtraction(prevResult, run)
    if usrinput == "multiplication" or "*":
        prevResult = multiplication(prevResult, run)
    if usrinput == "division" or "/":
        prevResult = division(prevResult, run)
    if usrinput == "clear":
        prevResult = clear()
    if usrinput == "exit":
        exit()