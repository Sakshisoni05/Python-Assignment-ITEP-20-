# 24) 0	4	16	36	64	….. 1 2 3 4 5 6 7 8

num=int(input("enter number : "))
for i in range(0,num+1):
    if i%2==0:
        print(i*i,end=" ")