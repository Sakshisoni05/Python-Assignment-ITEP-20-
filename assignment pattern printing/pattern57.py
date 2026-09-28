#  ABCDE
#   ABCD
#    ABC
#     AB
#      A

for i in range(1,6):
    for space in range(1,i):
        print(" ",end="")
    for j in range(6-i):
        print(chr(65+j),end="")
    print()        
