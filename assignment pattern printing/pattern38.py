# *****
# *  *
# * *
# **
# *

for i in range(1,6):
    for j in range(1,7-i):
        if i==2 and j>1 and j<4 or i==3 and j==2:
            print(" ",end="")
        else:    
           print("*",end="")
    print()    