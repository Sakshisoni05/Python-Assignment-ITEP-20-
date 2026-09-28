# 44) WAP to interchange first and last digit of a number..
n = int(input("Enter a number: "))

s = str(n)
first = s[0]
last = s[len(s) - 1]

middle = ""

for i in range(1, len(s) - 1):
    middle = middle + s[i]

result = last + middle + first

print("After interchange =", int(result))