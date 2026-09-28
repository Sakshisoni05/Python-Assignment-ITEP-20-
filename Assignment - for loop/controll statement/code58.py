# 58) WAP to convert decimal number into binary number without using array.

n = int(input("Enter decimal number: "))

binary = 0
place = 1

for i in range(n):
    if n == 0:
        break

    rem = n % 2
    binary = binary + rem * place
    place = place * 10
    n = n // 2

print("Binary number =", binary)