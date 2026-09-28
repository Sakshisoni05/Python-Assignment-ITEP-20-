# 12345
#  1234
#   123
#    12
#     1
#  i=1 j=5 

for i in range(1,6):
    for space in range(1,i):
        print(" ",end="")
    for j in range(1,7-i):
        print(j,end="")
    print()    
    