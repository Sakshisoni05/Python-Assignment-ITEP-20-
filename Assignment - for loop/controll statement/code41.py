a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM =", i)
        break

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = (a * b) // hcf

print("LCM =", lcm)
