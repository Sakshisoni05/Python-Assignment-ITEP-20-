#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1

for i in range(1, 10):
    if i <= 4:
        print("    " * 2, i)
    
    elif i == 5:
        for j in range(1, 6):
            print(j, end=" ")
        for j in range(4, 0, -1):
            print(j, end=" ")
        print()
    
    else:
        print("    " * 2, 10 - i)
