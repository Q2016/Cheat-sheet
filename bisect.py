Given a list of tuples default buckets and a list of scores, compare each item in scores with every tuple in default_bucket and count 
how many fall under such buckets. Output has to be a dictionary with tuple as keys and the count as values.

default_bucket = [(300,400), (401, 500), (501, 600), (601, 700), (701, 800), (801, 900), (901, 1000)]

scores = [420, 410, 908, 700, 450, 310, 200, 555, 996, 1000]

output = {(300, 400): 2, (401, 500): 3, (501, 600): 1, (601, 700): 1, (901, 1000): 3}




import bisect
# arr1=[1,2,3,4,5]
# bisect.bisect_left(arr1,4)
def ques(db,scores):
  scores.sort()
  dic={}
  for i in db:
    dic[i]=bisect.bisect_left(scores,i[1]+1)-bisect.bisect_left(scores,i[0])
  return dic

db = [(300,400), (401, 500), (501, 600), (601, 700), (701, 800), (801, 900), (901, 1000)]
scores = [420, 410, 908, 700, 450, 310, 200, 555, 996, 1000]
ques(db,scores)
