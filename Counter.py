// most k common items in counter
dic=cnt.most_common(k)

// count frequencies, note output of count is orderes from largest frequency to lowest
        
import collections
	cnt = Counter(arr)
        frequencies = list(cnt.values()) -------------------------> returns frequency
        frequencies.sort()

// using heap with dictionary
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)-----------------------> returns keys in array format
// accessing Counter
	for k,v in cnt.items():
// or 
>>> theList = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
>>> newList = Counter(theList)
>>> newList['blue']


# example
ans = collections.Counter()
ans[i] += count
return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
