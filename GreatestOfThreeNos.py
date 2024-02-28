
num1= int(input("Enter first number : "))
num2= int(input("Enter second number : "))
num3=int(input("Enter the third number : "))
if (num1>num2):
    if(num1>num3):
        print(f"The largest number is {num1}")
    else:
        print("num3 is greatest")
else:
    if(num2>num3):
        print("num2 is greatest");
    else:
        print("num3 is greatest")