# 3) WAP to find out the sum of N natural number.

num=int(input("Enter a natural number : "))
sum=0

for i in range(1,num+1):
    sum=sum+i
print(f"sum = {sum}")    
