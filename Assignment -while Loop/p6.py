# 6) WAP to find out the factors of a number.
n= int(input("enter number : "))
i=1
print(f"Factors of {n} are :- ")
while(i<=n) : 
    if n%i == 0:
        print(i,end=" ")
    i+=1    