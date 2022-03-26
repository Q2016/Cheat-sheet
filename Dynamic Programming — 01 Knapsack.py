Question:
Given both weights and profits of N items, we want to put these items in a Knapsack which has a capacity C. 
The goal is to get the maximum profit from the items in the Knapsack. Each item can only be selected once, as we don’t 
have multiple quantities of any item.
Example:
Items: [A, B, C, D]                                           Items: [A, B, C, D]
Weights: [2, 3, 1, 4]                        select A,profit 4        /      \    Exclude A, profit 0
Profits: [4, 5, 3, 7]                                          [B, C, D]   [B, C, D]
Capacity: 5                                                     /   \        /    \


Youtube: https://www.youtube.com/watch?v=wJJ3FFjFSaM  

Time Complexity: O (N*W).
where ‘N’ is the number of weight elements and ‘W’ is the capacity of the knapsack.      
     
  
Basic solution: (The idea of knap/Sack is the select an element and skip an element)
  
def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)
    return max(profit1, profit2)


Top-down Dynamic Programming with Memoization:
  
We can use memoization to overcome the overlapping sub-problems. To reiterate, memoization is when we store the results of 
all the previously solved sub-problems and return the results from memory if we encounter a problem that has already been solved.
Since we have two changing values (capacity and currentIndex) in our recursive function knapsackRecursive(), we can use a 
two-dimensional array to store the results of all the solved sub-problems. As mentioned above, we need to store results for every 
sub-array (i.e. for every possible index ‘i’) and for every possible capacity ‘c’.


def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
      return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
      return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
      profit1 = profits[currentIndex] + knapsack_recursive(dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]
  
  
Bottom-up Dynamic Programming
Let’s try to populate our dp[][] array from the above solution, working in a bottom-up fashion. Essentially, we want to 
find the maximum profit for every sub-array and for every possible capacity.
This means, dp[i][c] will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items.

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity+1)] for y in range(n)]
    
    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0
    
    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profits1 = profits[i] + dp[i-1][c-weights[i]]
            profits2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    
    # maximum profit will be at the bottom-right corner.
    return dp[n-1][capacity]
  
Equal Subset Sum Partition — Leetcode #416
Subset Sum: Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
Minimum Subset Sum Difference: Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.  
Count of Subset Sum: Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.  
Target Sum -- Leetcode #494  
