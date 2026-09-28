# 7) WAP to check whether entered number is prime or not.

num = int(input("Enter number : "))
flag = False

for i in range(1,(num//2)+1):
    if num%i==0:
        flag = True 
        break

if flag:
    print("Number is not prime")

else:
    print("Number is prime")

