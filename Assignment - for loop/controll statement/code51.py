# 51) WAP to reverse all the numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    n = i
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    print(i, "=", rev)