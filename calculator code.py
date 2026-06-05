print("-------Calculator-------")

while True :
    print("")
    print("------New Calculation------")
    
    go_on= (input("Do you want to go on?: "))
    
    if go_on.lower() == "no":
        print("OK, happy to be with you. Good bye!!!")
        break
    
    elif go_on.lower() == "yes":
        
        num1= float(input("Enter first number: "))
        operator= input("Enter your operator: ")
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
                print("Math error!")
    
        elif operator=="%":
            
            if num2 >0 or num2<0:
                print("Result: ",num1%num2)
                
            else:
                print("Math error")

        else:
            print("Syntex error")
            
    else:
        print("Only Yes or No is valid")
        
