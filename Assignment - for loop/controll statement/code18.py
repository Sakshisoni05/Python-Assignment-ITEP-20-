# 18) 1	2	2	4	8	32	…… n terms

# 1*2=2 2*2=4 2*4=8 
num =int(input("Enter number : "))

a = 1
b = 2

for i in range(num):
    print(a, end=" ")
    a, b = b, a * b