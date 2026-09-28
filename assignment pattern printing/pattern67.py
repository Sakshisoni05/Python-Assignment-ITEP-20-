#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

for i in range(5):
    
    for space in range(4 - i):
        print(" ", end=" ")

    num = 1

    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)

    print()