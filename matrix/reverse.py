x = [[1,2,3,4],
     [5,6,8,9],
     [2,6,7,8]
     ]

for row in range(len(x)):
    for col in range(len(x[row])-1, -1, -1):
        print(x[row][col], end=" ")
    print()    