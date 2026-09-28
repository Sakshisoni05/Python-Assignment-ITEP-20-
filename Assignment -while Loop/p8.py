#  8) WAP to print Fibonacci series.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

n= int(input("Enter number : "))
a = 0 
b = 1
i = 0
while i<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1



