# 52). armstrong between two numbers .

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    n = i
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    n = i
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** count
        n = n // 10

    if sum == i:
        print(i, end=" ")
        