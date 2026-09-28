# 1	2	2	4	8	32	…… n terms

n = int(input("ENTER NUMBER : "))

a=1
b=2
i=1
while i<=n:
    print(a,end=" ")
    c=a*b
    a=b
    b=c
    i +=1
