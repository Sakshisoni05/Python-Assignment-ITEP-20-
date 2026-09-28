# 30) 1+11+111+1111+11111. 

n = int(input("Enter number of terms: "))

term = 0
total_sum = 0

for i in range(1, n + 1):
    term = term * 10 + 1  #  1, 11, 111, 1111...
    total_sum += term

print("Sum:", total_sum)