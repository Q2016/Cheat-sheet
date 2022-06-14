# enumerate all possibilities, with the permutation() func
A=[1,2,3,4]        
for h, i, j, k in itertools.permutations(A):
  
  
  
people = iter(list1) # list1=[1,2,3]
# or
people = (i for i, seat in enumerate(seats) if seat)

future = next(people)
future = next(people, None) # If default is given, it is returned if the iterator is exhausted
