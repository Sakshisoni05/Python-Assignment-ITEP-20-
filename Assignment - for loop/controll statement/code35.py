# 35) WAP to count number of digits
num=int(input("enter number: "))
original=num
count=0

if num==0:
    count=1 
else:    
    for i in range(num):
        if num==0:
            break
        num=num//10
        count+=1

print(f"number of digits in {original} = {count}")

