#     1
#    1*1
#   1***1
#  1*****1
# 111111111
for i in range(1, 6):

    for space in range(5, i, -1):
        print(" ", end="")

    if i == 1:
        print("1")

    elif i == 2:
        print("1*1")

    elif i == 3:
        print("1***1")

    elif i == 4:
        print("1*****1")

    else:
        print("111111111")