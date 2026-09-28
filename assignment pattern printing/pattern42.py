# 123456
# 54321
# 1234
# 321
# 12
# 1

for i in range(1,7):
    for j in range(1,7-i):
        if i%2!=0:
            print(j,end="")
        else:
            print(6-j,end="")
    print()    