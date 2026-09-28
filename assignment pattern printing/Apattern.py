#     *
#    * *
#   * * *
#  *     *
# *       *

for i in range(1,6):
    for space in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i<=3:
            print("* ",end="")  
        elif j==1 or j==i:
            print("* ",end="")  
        else:
            print("  ",end="")
    print()                
