print("Welcome to Calc :This is developed by Vaishali Baghel")
print("Please type in the math operation you would like to complete :")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for division")
print("** for power")
print("% for modulo")
print("Enter your choice : ",end="")
ch=input()
print("Enter first number : ",end="")
num1=int(input())
print("Enter second number : ",end="")
num2=int(input())
if(num1==45 and num2==3 and ch=='*'):
    print("555")
elif (num1 == 45 and num2 == 3 and ch == '*'):
    print("555")
elif(num1==56 and num2==9 and ch=='+'):
    print("77")
elif(num1==56 and num2==6 and ch=='/'):
    print("4")
elif(ch=='+'):
    print(num1+num2)
elif(ch=='-'):
    print(num1-num2)
elif(ch=='*'):
    print(num1*num2)
elif(ch=='/'):
    print(num1/num2)
elif(ch=='%'):
    print(num1%num2)
elif(ch=='**'):
    print(num1**num2)
else:
    print("Invalid choice")

