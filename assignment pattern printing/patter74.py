# 123456789
#  1234567
#   12345
#    123
#     1

for i in range(5):
    for space in range(i):
        print(" ", end="")

    for j in range(1, 10 - 2*i):
        print(j, end="")

    print()