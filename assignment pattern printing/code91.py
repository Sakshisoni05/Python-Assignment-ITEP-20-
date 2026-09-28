#      1               
#     101            
#    10101         
#   1010101           
#  101010101   
# 10101010101

for i in range(1, 7):

    # spaces
    for space in range(6-i):
        print(" ", end="")

    # 1 and 0 pattern
    for j in range(2*i-1):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")

    print()