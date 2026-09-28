# 25) 1	27	125	343	…………

num = int(input("enter number : "))
for i in range(1,num+1):
    if i%2!=0:
        print(i**3,end=" ")