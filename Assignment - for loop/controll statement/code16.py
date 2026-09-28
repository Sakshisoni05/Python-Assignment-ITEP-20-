# 16) …... -6	-3	0	3	6	9	……. n terms [where n is even]	 

num = int(input("Enter number : "))
for i in range(-num,num+1):
    if i%3==0:
        print(i,end=" ")

        