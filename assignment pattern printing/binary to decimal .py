# write a program to convert binary number to decimal number...

num = int(input("Enter binary number : "))
decimal = 0
i = 0
while num != 0:
    rem = num % 10
    decimal = decimal + rem * pow(2, i)
    num = num // 10
    i += 1

print("Decimal number is : ", decimal)
