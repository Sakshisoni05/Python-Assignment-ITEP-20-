# 6) WAP to find out the factors of a number.

num=int(input("Enter number : " ))
print(f"factors of {num} = ",end="")

for i in range(1,(num//2)+1):
    if num%i==0:
       print(i,end=" ")

       