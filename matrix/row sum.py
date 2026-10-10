x = [[1,2,3,4],
     [5,6,8,9],
     [2,6,7,8]
     ]

min_sum =0
min_row=0
max_sum =0
max_row =0
for row in range(len(x)):
    sum=0
    for col in range(len(x[row])):
       sum = sum+ x[row][col]
    if max_sum < sum:
        max_sum = sum 
        max_row = row
    if min_sum>sum:
        min_sum = sum
        min_row = row    
    print(f"sum of row {row} = {sum}")    

print(f"row {max_row} has maximum sum = {max_sum}")

print(f"row {min_row} has minimum sum = {min_sum}")