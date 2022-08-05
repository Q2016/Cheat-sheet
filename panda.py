df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df
   A  B
0  4  9
1  4  9
2  4  9

df.apply(lambda x: [1, 2], axis=1)
0    [1, 2]
1    [1, 2]
2    [1, 2]


# How to use loop to generate a column
vif["col1"] = [variance_inflation_factor(col1.values, i) for i in range(col1.shape[1])]



def get(w0, w1):
     pass 

df["col1"]=df.apply(lambda x: get(x.col1, x.col2), axis=1)


daily=df.cumprod() # cumulative product
daily=df["col1"].cumsum(axis=0)  # in panda column comes first, as you might guess
daily=df["col1"].cumsum(axis=1) 


df.groupby("col1")['col2'].sum()


df.mycolumn.pct_change()


df.count(0) # number of data in the columns
df.count(1) # number of data in the rows


df['col1'].value_counts() # output is the distribution of values in the given column


pd.crosstab(df['col2'], df['col1'])  # provides cross tabulation, the distribution between two columns


pd.cut(df['col1'], bins = 5).value_counts()  # creating a histogram bin
Output:

(-100500.0, 20100000.0]      16102 
(20100000.0, 40200000.0]        40 
(40200000.0, 60300000.0]        10 
(60300000.0, 80400000.0]         2 
(80400000.0, 100500000.0]        1 
 
 
 df['col1'].describe()
Output:

count     16155.000000
mean      13056.453110
std       23488.182571
min           0.000000
25%        2000.000000
50%        5000.000000
75%       10000.000000
max      550000.000000
 
 

df.nlargest(5, "col1") # list 5 largest in that column
df.nsmallest(5, "col1")
 
 

df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                   'B': 1,
                   'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
df
           A  B          C
0  [0, 1, 2]  1  [a, b, c]
1        foo  1        NaN
2         []  1         []
3     [3, 4]  1     [d, e]
 
df.explode('A')
     A  B          C
0    0  1  [a, b, c]
0    1  1  [a, b, c]
0    2  1  [a, b, c]
1  foo  1        NaN
2  NaN  1         []
3    3  1     [d, e]
3    4  1     [d, e] 
