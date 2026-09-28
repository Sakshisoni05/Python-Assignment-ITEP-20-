# 55555
#  4__4
#   3_3
#    22
#     1

for i in range(1,6):
    for space in range(1,i):
        print(" ",end="")

    for j in range(i,6):    
        if i == 2 and j > 2 and j < 5:
            print("_", end="")
        elif i == 3 and j == 4:
            print("_", end="")
        else:
            print(6-i, end="")

    print()    