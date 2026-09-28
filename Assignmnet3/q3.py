# 3.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("enter your salary : "))
year = int(input("YEAR OF SERVICES : "))
bonus = 0

if year > 5  :
    bonus = salary * 5 /100

print(f"Net bonus amount he get : {bonus}")