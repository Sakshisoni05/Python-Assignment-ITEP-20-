# 26) 0	8	64	216	…………

num = int(input("enter number : "))
for i in range(0,num+1):
    if i%2==0:
        print(i**3,end=" ")