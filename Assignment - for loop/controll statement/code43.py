# 43) WAP to convert binary number into decimal number
n = int(input("Enter binary number: "))

decimal = 0
power = 0

for i in str(n)[::-1]:
    decimal = decimal + int(i) * (2 ** power)
    power = power + 1

print("Decimal number =", decimal)