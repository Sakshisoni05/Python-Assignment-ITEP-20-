# 46) WAP to find out the sum of first and last digit of a user entered number ...


n = int(input("Enter a number: "))

temp = n
last = n % 10

for i in range(1, n):
    temp = temp // 10
    if temp < 10:
        break

first = temp

print("Sum =", first + last)