carry, A[i] = divmod(A[i], 10) # If x and y are integers, the return value from divmod() is same as (a // b, x % y)

# enumerate all possibilities, with the permutation() func
for h, i, j, k in itertools.permutations(A):
