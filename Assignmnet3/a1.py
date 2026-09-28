# 1. Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == breadth:
    print("It is a square")
else:
    print("It is not a square")