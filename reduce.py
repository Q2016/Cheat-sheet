from fractions import gcd
vals = collections.Counter(deck).values()
return reduce(gcd, vals) >= 2 # vals is a list

