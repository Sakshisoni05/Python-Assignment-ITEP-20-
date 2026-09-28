# 1
# 22
# 3 3
# 4  4
# 55555

for i in range(1,6):
    if i==5:
        for j in range(1,6):
            print(i,end="")
    else:
        for j in range(1,i+1):
            if j==1 or j==i:
                print(i,end="")
            else:
                print(" ",end="") 

        print()
