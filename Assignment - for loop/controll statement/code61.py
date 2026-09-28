# 61) WAP to find out all the leap years between two entered years

a = int(input("Enter first year: "))
b = int(input("Enter second year: "))

for year in range(a, b + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, end=" ")

        