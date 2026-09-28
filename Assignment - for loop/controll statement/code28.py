# 28) 1	2	3	4	 Hello	6	7	8	9	Hello	11	12 ….

num = int(input("enter number : "))

for i in range(1,num+1):
    if i%5==0:
        print("Hello",end=" ")
    else:
        print(i,end=" ")    
        