#     A
#    AB
#   A_C
#  A__D
# ABCDE
for i in range(1,6):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(i):
        if i == 3 and j == 1:
            print("_", end="")
        elif i == 4 and (j == 1 or j == 2):
            print("_", end="")
        else:
            print(chr(65+j), end="")

    print()        