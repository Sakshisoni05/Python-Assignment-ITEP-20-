# 56). Factorial of all numbers between two entered numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    print("Factorial of", i, "=", fact)

    