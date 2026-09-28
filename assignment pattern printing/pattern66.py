#     *
#    *_*
#   *___* 
#  *_____* 
# *********

for i in range(1, 6):

    for space in range(5, i, -1):
        print(" ", end="")

    if i == 1:
        print("*")

    elif i == 2:
        print("*_*")

    elif i == 3:
        print("*___*")

    elif i == 4:
        print("*_____*")

    else:
        print("*********")