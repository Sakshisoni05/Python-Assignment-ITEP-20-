# 47. Tables of all numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "*", j, "=", i * j)