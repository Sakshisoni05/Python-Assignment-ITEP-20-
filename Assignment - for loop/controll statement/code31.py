# 31) 9	99	999	9999	  99999 …….

n = int(input("Enter number of terms: "))
for i in range(1, n + 1):
    print("9" * i, end=" ")

#second method------

n = int(input("Enter number of terms: "))
term = 0

for i in range(1, n + 1):
    term = term * 10 + 9
    print(term, end=" ")

