#7) WAP to check whether entered number is prime or not.

n =  int(input("ENTER NUMBER : "))
count = 0
i=1
while i<=n:
    if n%i == 0:
        count +=1
    i+=1
if count == 2:
    print(f"{n} is prime number ")       

else:
    print(f"{n} is not prime")

    