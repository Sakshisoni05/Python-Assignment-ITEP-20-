# 8) WAP to print Fibonacci series.
# 0 1 1 2 3 5 8 13 21 44.......
num=int(input("enter number : "))
a=0
b = 1
print("Fibonacci series -- ")
for i in range(num+1):
    print(a,end= " ")
    a,b =b, a+b
  
