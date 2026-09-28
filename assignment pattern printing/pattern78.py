# 123456789
#  1+++++7
#   1+++5
#    1+3
#    1

print("123456789")

for i in range(7, 0, -2):
    for space in range(8-i):
        print(" ", end="")

    print("1", end="")

    if i == 7:
        print("*++++*+", end="")
    elif i == 5:
        print("*++*+", end="")
    elif i == 3:
        print("+", end="")

    if i != 1:
        print(i, end="")

    print()