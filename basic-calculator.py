import math

def funcAdd(num1,num2,operation_str):
    print(num1, operation_str, num2 , '= ', num1 + num2)

def funcMinus(num1,num2,operation_str):
    print(num1, operation_str, num2 , '= ', num1 - num2)

def funcMult(num1,num2,operation_str):
    print(num1, operation_str, num2 , '= ', num1 * num2)

def funcDiv(num1,num2,operation_str):
    print(num1, operation_str, num2 , '= ', num1 / num2)
    
def funcMod(num1,num2,operation_str):
    print(num1, operation_str, num2 , '= ', num1 % num2)

def funcPow(num1,num2,operation_str):
    print(num1, operation_str, num2, '= ', pow(num1,num2))

def funcAbs(num1, operation_str):
    print('The Absolute Value of ', num1,'= ', abs(num1))

def funcLog(num1, operation_str):
    print('The Natural Log of ', num1,'= ', math.log(num1))

def funcExp(num1, operation_str):
    print('The Exponential Value of ', num1,'= ', math.exp(num1))        

print('Question 1')
while True:
    operand1 = input('Enter the first number: ')
    if(operand1 == 'x' or operand1 == 'X'):
        print('You typed', operand1,'to Exit, closing the Calculator!')
        break
    try:    
        foperand1 = float(operand1)
        print('You entered', foperand1)
        print("Operations: +, -, *, /, %, ^, exp, log, abs")  
        operation = input('Now enter the operation that you would like to perform: ')
        if(operation == '+'):
            print('You typed', operation,'to perform Addition!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcAdd(foperand1, foperand2, operation)
                continue      
            except:
              print("You didn't enter a number try again.")
              continue
        elif(operation == '-'):
            print('You typed', operation,'to perform Subtraction!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcMinus(foperand1, foperand2, operation)
                continue
            except:
              print("You didn't enter a number try again.")
              continue
        elif(operation == '*'):
            print('You typed', operation,'to perform Multiplication!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcMult(foperand1, foperand2, operation)
                continue 
            except:
              print("You didn't enter a number try again.")
              continue
        elif(operation == '/'):
            print('You typed', operation,'to perform Division!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcDiv(foperand1, foperand2, operation)
                continue 
            except:
              print("You didn't enter a number try again.")
              continue
        elif(operation == '%'):
            print('You typed', operation,'to perform Modulus!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcMod(foperand1, foperand2, operation)
                continue 
            except:
              print("You didn't enter a number try again.")
              continue
        elif(operation == '^'):
            print('You typed', operation,'to perform the Power Function!')
            operand2 = input('Enter the second number: ')
            if(operand2 == 'x' or operand2 == 'X'):
                print('You typed', operand2,'to Exit, closing the Calculator!')
                break
            try:    
                foperand2 = float(operand2)
                print('You entered', foperand2)
                funcPow(foperand1, foperand2, operation)
                continue 
            except:
              print("You didn't enter a number try again.")
              continue      
        elif(operation == 'abs'):
            print('You typed', operation,'to perform Absolute Value!')
            funcAbs(foperand1, operation)
            continue
        elif(operation == 'log'):
            print('You typed', operation,'to perform Natural Log!')
            funcLog(foperand1, operation)
            continue
        elif(operation == 'exp'):
            print('You typed', operation,'to perform Exponential Value!')
            funcExp(foperand1, operation)
            continue
        elif(operation == 'x' or operation == 'X'):
            print('You typed', operation,'to Exit, closing the Calculator!')
            break                   
        else:
          print('Operation not available, try again')
          continue
    except:
        print("You didn't enter a number try again.")
        continue   

