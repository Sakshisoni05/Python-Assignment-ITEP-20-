# 45. Find the sum of 28 terms of an Arithmetic Progression -21 -18 -15 -12 . . . . .

# First term \(a = -21\)
# Common difference \(d = -18 - (-21) = 3\)
# Term number n=28

a=-21
dif=3
n = 28


# Sum of n terms of an AP = n/2 * (2a + (n-1)d)
sum_of_n_terms = n / 2 * (2 * a + (n -1) * dif)
print(f'The sum of 28 terms of the Arithmetic Progression is {sum_of_n_terms}')
