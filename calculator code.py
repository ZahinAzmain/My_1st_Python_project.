while True :
    print("------New Calculation------")
    
    operator= (input("Enter an operator [+,-,*,/,%,X(to exit)]: "))
    if operator == "X":
        print("Good Luck!")
        break
    
    num1= float(input("Enter first number: "))
    num2= float(input("Enter second number: "))

    if operator== "+":
        print("Result: ",num1+num2)
    
    elif operator=="-":
        print("Result: ",num1-num2)
    
    elif operator== "*":
        print("Result: ",num1*num2)
    
    elif operator== "/":
        if num2 >0 or num2<0:
            print("Result: ",num1/num2)
        else:
            print("Math error")
    
    elif operator=="%":
        if num2 >0 or num2<0:
            print("Result: ",num1%num2)
        else:
            print("Math error")

    else:
        print("Syntex error")
