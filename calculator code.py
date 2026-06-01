
num1= float(input("Enter first number: "))
operator= (input("Enter an operator ( only valid for +,-,*,/,%): "))
num2= float(input("Enter second number: "))

if operator== "+":
    print(num1+num2)
    
elif operator=="-":
    print(num1-num2)
    
elif operator== "*":
    print(num1*num2)
    
elif operator== "/":
    print(num1/num2)
    
elif operator=="%":
    print(num1%num2)

else:
    print("Math error")