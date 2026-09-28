# A B C D E
#  A B C D
#   A B C
#    A B
#     A

for i in range(5):
    for space in range(i):
        print(" ", end="")

    for j in range(1, 6-i):
        print(chr(64+j), end=" ")

    print()