#     5
#    44
#   333
#  2222
# 11111

for i in range(1,6):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(i):
        print(6-i,end="")
    print()        

