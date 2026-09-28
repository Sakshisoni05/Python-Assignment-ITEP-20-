#  1	+	1/2	+	1/3	+	1/4	+	1/5	….. n terms(find out sum)

n = int(input("Enter number : "))
i=1
sum = 0
while i <=n:
    sum=sum + (1/i)
    i +=1
print("SUM = ",sum)    
