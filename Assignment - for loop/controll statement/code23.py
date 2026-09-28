# 23) 1	9	25	49	81	…..n
num=int(input("enter number : "))
for i in range(1,num+1):
    if i%2!=0:
        print(i*i,end=" ")