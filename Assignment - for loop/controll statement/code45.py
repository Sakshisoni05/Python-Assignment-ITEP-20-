# 45) WAP to find out the sum of all the digits of a number

n = int(input("Enter a number: "))

sum = 0

for i in str(n):
    sum = sum + int(i)

print("Sum of digits =", sum)