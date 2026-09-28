# 3) Strong numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    n = i
    sum = 0

    while n > 0:
        digit = n % 10

        fact = 1
        for j in range(1, digit + 1):
            fact = fact * j

        sum = sum + fact
        n = n // 10

    if sum == i:
        print(i, end=" ")