print("Simple Calculator")
def calculator():
    print()

num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
op = input("Enter the operation (+,-,*,/): ")

if op=='+':
    print("Result : ",num1+num2)
elif op=='-':
    print("Result : ",num1-num2)
elif op=='*':
    print("Result : ",num1*num2)
elif op=='/':
    if num2!=0:
        print("Result : ",num1/num2)    
    else:
        print("Error! Division by Zero")
else:
    print("Invalid Operation")

calculator()
