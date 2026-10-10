x=[[1,2,3],[4,5,6],[7,8,9]]

for row in range(len(x)):
    for col in range(len(x[row])):
        if row + col == len(x)-1:
            print(x[row][col], end=" ")
        else:
            print(" ", end=" ")
    print()
    