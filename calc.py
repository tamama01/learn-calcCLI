from math import sqrt

def addition(num1,num2):
    return num1 + num2
    
def substraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def power(num1,num2):
    return pow(num1,num2)

def square_root(num1):
    return sqrt(num1)

while True:
    print("\nMode List:-")
    print("\tMode 1: Addition")
    print("\tMode 2: Substraction")
    print("\tMode 3: Multiplication")
    print("\tMode 4: Division")
    print("\tMode 5: Power")
    print("\tMode 6: Square root")
    print("\tMode 7: Exit")

    while True:
        try:
            modeCalc = int(input("\n" + "Which mode?: "))
            break
        except ValueError:
            print("The input must be a number. Try again.")
            continue
    
    if  modeCalc == 1:
        while True:
            try:
                numTemp1 = float(input("\nFirst number: "))
                numTemp2 = float(input("Second number: "))
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue
        
        answer = addition(numTemp1,numTemp2)
        print("\n" + str(numTemp1) + " + " + str(numTemp2) + " = " + str(answer))
        continue

    elif modeCalc == 2:
        while True:
            try:
                numTemp1 = float(input("\nFirst number: "))
                numTemp2 = float(input("Second number: "))
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue
        
        answer = substraction(numTemp1,numTemp2)
        print("\n" + str(numTemp1) + " - " + str(numTemp2) + " = " + str(answer))
        continue

    elif modeCalc == 3:
        while True:
            try:
                numTemp1 = float(input("\nFirst number: "))
                numTemp2 = float(input("Second number: "))
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue

        answer = multiplication(numTemp1,numTemp2)
        print("\n" + str(numTemp1) + " * " + str(numTemp2) + " = " + str(answer))
        continue

    elif modeCalc == 4:
        while True:
            try:
                numTemp1 = float(input("\nFirst number: "))
                numTemp2 = float(input("Second number: "))
                numTemp1/numTemp2
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue
            except ZeroDivisionError:
                print("Cannot divide by zero. Try again.")
                continue

        answer = division(numTemp1,numTemp2)
        print("\n" + str(numTemp1) + " / " + str(numTemp2) + " = " + str(answer))
        continue

    elif modeCalc == 5:
        while True:
            try:
                numTemp1 = float(input("\nBase number: "))
                numTemp2 = float(input("Power: "))
                power(numTemp1,numTemp2)
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue

        answer = power(numTemp1,numTemp2)
        print("\n" + str(numTemp1) + " ^ " + str(numTemp2) + " = " + str(answer))
        continue

    elif modeCalc == 6:
        while True:
            try:
                numTemp1 = float(input("\nFirst number: "))
                square_root(numTemp1)
                break
            except ValueError:
                print("The input must be a number. Try again.")
                continue

        answer = square_root(numTemp1)
        print("\nsqrt(" + str(numTemp1) + ") = " + str(answer))
        continue

    elif modeCalc == 7:
        while True:
            exitChoice = input("Exit the program? (Y/N): ")
            if exitChoice.lower() == "y":
                break
            elif exitChoice.lower() == "n":
                break
            else:
                print("Invalid, Try Again.")
                continue

        if exitChoice.lower() == "y":
            break
        elif exitChoice.lower() == "n":
            continue
    else:
        print("Invalid, Try Again.")
        continue