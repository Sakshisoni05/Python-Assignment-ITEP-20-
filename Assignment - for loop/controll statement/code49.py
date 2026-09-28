# 49) WAP to find out all the perfect numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    sum = 0

    for j in range(1, i):
        if i % j == 0:
            sum = sum + j

    if sum == i:
        print(i, end=" ")
        