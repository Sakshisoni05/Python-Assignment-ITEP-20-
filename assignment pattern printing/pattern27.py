for i in range(1,6):
    for j in range(1,i+1):
        if i>j and j!=1 and i!=5 :
            print("e",end="")
        else:
            print("*",end="")    
    print()
