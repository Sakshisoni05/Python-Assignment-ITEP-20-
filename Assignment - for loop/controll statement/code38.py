# 38) WAP to check whether entered number is Armstrong or not

num = (int(input("enter number : ")))
original = num
r =len(str(original))
sum=0

for i in range(r):
    digit = num % 10
    sum += digit ** r
    num //= 10

if sum == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is NOT an Armstrong number.")
    