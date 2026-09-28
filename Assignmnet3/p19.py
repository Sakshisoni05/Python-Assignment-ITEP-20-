# 19. Write a program to input choice from user. 
# If user enter ‘+’ as choice then calculate addition of 2 number.
# If Choice ‘>’ then check which number is greaterst. 
# If choice is ‘==’ then check both number is equal or not.

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
choice = input("ENTER YOUR CHOICE (+ , > , ==) :  ")

if choice == "+":
    result = num1 + num2 
    print(f"ADDITION OF {num1} and {num2} = {result}")

elif choice == ">":
    print(f"{num1} is greater") if num1>num2 else print(f"{num2} is greater")

elif choice == "==":
    if num1 == num2 :
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num1} and {num2} are not equal ")    

