#55). Odd numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i, end=" ")