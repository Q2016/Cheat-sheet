# if trust=[[1,2],[2,3]]
for (a, b) in trust:

 
def sub_lists(l,m): # maybe this can be replaced with itertools.permutation()
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return [p for p in lists if len(p)==m]  
