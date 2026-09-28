# 48) WAP to find out the factors of all the numbers between two entered numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    print("Factors of", i, ":", end=" ")

    for j in range(1, i + 1):
        if i % j == 0:
            print(j, end=" ")

    print()