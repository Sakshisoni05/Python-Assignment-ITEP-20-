# 60) WAP to print Square, Cube and Square Root of all numbers from 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print("Number =", i)
    print("Square =", i ** 2)
    print("Cube =", i ** 3)
    print("Square Root =", i ** 0.5)
    print()