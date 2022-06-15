############################################################################
Set

visited = set()
visited.add(front)


// first element of a set
list.pop()
//pop
# remove the element at index 2
removed_element = prime_numbers.pop(2)
.pop()// with no index drops the last item

# reverse loop
for i in range(l,n,-1):
starts from l stops at n (not included): l, l-1,..,n+1


#############################################################################
List

// common items between two lists
list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)
intersection_as_list = list(intersection)

// reverse list list[::-1]

// remove item from list
prime_numbers = [2, 3, 5, 7, 9, 11]


// 1d list, 2d list (Array Allocation)
d=[0]*10
d[1]=d[0]+1
//2d
t = [ [0]*N1 for i in range(N2)]



# remove 9 from the list
prime_numbers.remove(9)

for i in res:
   if(i == "00"):
     res.remove(i)
     
//insert in list
    for p in people:
        queue.insert(p[1], p)     

# extend	
ans=[]	
ans.extend([i] * cnt.pop(i)) 	
	


// list of list to list
t is list of list
flat_list = [item for sublist in t for item in sublist]

// python slicing intro
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
Similarly, step may be a negative number:

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
>>> seq[:]                # [seq[0],   seq[1],          ..., seq[-1]    ]
>>> seq[low:]             # [seq[low], seq[low+1],      ..., seq[-1]    ]
>>> seq[:high]            # [seq[0],   seq[1],          ..., seq[high-1]]
>>> seq[low:high]         # [seq[low], seq[low+1],      ..., seq[high-1]]
>>> seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
>>> seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
>>> seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
>>> seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]
Of course, if (high-low)%stride != 0, then the end point will be a little lower than high-1.

If stride is negative, the ordering is changed a bit since we're counting down:

>>> seq[::-stride]        # [seq[-1],   seq[-1-stride],   ..., seq[0]    ]
>>> seq[high::-stride]    # [seq[high], seq[high-stride], ..., seq[0]    ]
>>> seq[:low:-stride]     # [seq[-1],   seq[-1-stride],   ..., seq[low+1]]
>>> seq[high:low:-stride] # [seq[high], seq[high-stride], ..., seq[low+1]]

#############################################################################
// stack in python is just a list, you can use .pop() to drop last element
stack=[]


##############################################################################
Dictionary

// using array of dictionaries
d = collections.defaultdict(list)

for i in xrange(n):
    for j in xrange(m):
        d[i - j].append(A[i][j])
        
//sort dictionary by value--> works only in python3
dict(sorted(x.items(), key=lambda item: item[1]))
 or
dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

//dictionary elements
first_pair = next(iter((word_freq.items())) )
print('First Key: ', first_pair[0])
print('First Value: ', first_pair[1])

cnt.most_common(1)[0][1]        


// dictionary of lists
from collections import defaultdict
d = defaultdict(list)
a = ['1', '2']
for i in a:
   for j in range(int(i), int(i) + 2):
     d[j].append(i)

// defaultdict         
	groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return groups.values()
        

// dictionary by value and key
// given value get key
mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george
// given key get value
my_dict ={"java":100, "python":112, "c":11}
 
# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
 
# print key with val 100
position = val_list.index(100)
print(key_list[position])



# map
map({a: i+1 for i, a in enumerate(sorted(set(A)))}.get, A)

###################################### deque() ##########################
self.slide_window = deque()
self.slide_window.append(t)
self.slide_window.popleft()
