# 44. Find the 28th term of an Arithmetic Progression -21 -18 -15 -12 . . . . . 

# First term \(a = -21\)
# Common difference \(d = -18 - (-21) = 3\)
# Term number n=28


a=-21
dif=3
n = 28

# nth term of an AP = a + (n-1)d
term = a + (n - 1) * dif
print(f'The 28th term of the Arithmetic Progression is {term}')
