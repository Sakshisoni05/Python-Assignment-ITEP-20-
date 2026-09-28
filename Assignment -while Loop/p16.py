#  …... -n -6	-3	0	3	6	9	……. n terms [where n is even]	

n = int(input("enter number : "))

i=1
term =-n
while i <=n:
    print(term, end=" ")
    term +=3
    i+=1