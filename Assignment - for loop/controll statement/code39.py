# 39) Check Whether Entered Number is Strong or Not..

num = int(input("Enter a number: "))
temp = num
total_sum = 0

for i in range(len(str(temp))):
    digit = temp % 10
    
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
        
    total_sum += fact
    temp //= 10

if total_sum == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is NOT a Strong number.")