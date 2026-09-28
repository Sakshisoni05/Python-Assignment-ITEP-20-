#     A
#    AB
#   ABC
#  ABCD
# ABCDE
for i in range(1,6):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(i):
        print(chr(65+(j)),end="")
    print()        