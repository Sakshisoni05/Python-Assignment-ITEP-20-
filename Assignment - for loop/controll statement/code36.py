# 36) WAP to reverse a number

from unicodedata import digit


num=int(input("enter number : "))
temp=num
rev=0
for i in range(len(str(temp))):
    digit=num%10
    rev = rev*10+digit
    num=num//10
print(f"reverse of {temp} is {rev}")    
    