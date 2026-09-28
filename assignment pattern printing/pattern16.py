# a
# bc
# def
# ghij
# klmno
a=96
for i in range(1,6):
    for j in range(i):
        print(chr(a+1),end="")
        a+=1
    print()    