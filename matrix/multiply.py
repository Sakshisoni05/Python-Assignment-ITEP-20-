# a*b 
a = [[1,2,3],
     [4,5,6],
     [7,8,9]
     ]

b=[[1,2,3],
   [4,5,6],
   [7,8,9]
   ]

for i in range(len(a)):
    for j in range(len(b[0])):
        sum = 0
        for k in range(len(b)):
            sum += a[i][k] * b[k][j]
        print(sum, end=" ")
    print()

