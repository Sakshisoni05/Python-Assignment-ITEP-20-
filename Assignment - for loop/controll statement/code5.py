# 5) WAP to find out the factorial of a number.

num=int(input("ENTER NUMBER : "))
fact= 1
for i in range(num,0,-1):
    fact=fact*i
print(f"Factorial of {num} = {fact}")    