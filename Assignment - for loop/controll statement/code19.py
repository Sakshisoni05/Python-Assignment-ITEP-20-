# 19) 1	+	1/2	+	1/3	+	1/4	+	1/5	….. n terms(find out sum)

num=int(input("Enter number : "))
sum=0
for i in range(1,num+1):
    print(f"1/{i}",end=" ")
    sum= sum+(1/i)
print(f"\nsum = {sum}")    