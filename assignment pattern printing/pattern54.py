# 12345
#  1__4
#   1_3
#    12
#     1

for i in range(1,6):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,7-i):
        if i==2 and j>1 and j<4:
            print("_",end="")
        elif i==3 and j==2:
            print("_",end="")
        else:        
            print(j,end="")
    print()        