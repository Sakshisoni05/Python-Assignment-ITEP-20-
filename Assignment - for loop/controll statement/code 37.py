# 37) WAP to check whether entered number is palindrome or not

num=int(input("enter number: "))
original=num
rev=0
for i in range (len(str(num))):
    digit=num%10
    rev = rev* 10+digit
    num=num//10

if rev == original:
    print(f"{original} is pellindrome")    

else:
    print(f"{original} is not pellindrome")       
    