# 40) WAP to count no. Of even and odd digits in a number

n = int(input("Enter a number: "))

even = 0
odd = 0

for i in str(n):
    digit = int(i)

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even digits =", even)
print("Odd digits =", odd)