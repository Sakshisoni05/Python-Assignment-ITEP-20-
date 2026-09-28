# A
# AB
# A C
# A  D
# ABCDE

for i in range(1,6):
    if i==5:
        for j in range(1,6):
            print(chr(64+j),end=" ")
    else:
        for j in range(1,i+1):
            if j==1 or j ==i:
                print(chr(64+i),end="")
            else:
                print(" ",end="")
        print()