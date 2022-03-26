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
#refrence regarding complexity of knapSack: (At the end)    
  
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




Knapsack Problem
Different methods to solve the Knapsack Problem
While solving problems on Dynamic Programming I came across the Knapsack Problem. It is one of the standard problems that every programmer must solve. In this article, I will discuss what exactly a knapsack problem is and what are the different methods that can be used to solve this problem.
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack
In other words, the statement of 0/1 knapsack problem can be explained as, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively, and an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0–1 property).

Therefore in this problem, we are given a set of items, each with a weight and a value and we have to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible i.e. we have to maximize the profit by selecting the items to be included in our knapsack.
METHODS TO SOLVE KNAPSACK PROBLEM
While you will find this problem as an example of dynamic programming various algorithms can be used to solve this problem namely Greedy Algorithm and Branch and Bound Algorithm. In this section, I will discuss all these methods (including Dynamic Programming) briefly and compare all of them to find the most efficient algorithm.
1)Dynamic Programming:
Dynamic algorithm is an algorithm design method, which can be used when the problem breaks down into simpler sub-problems. Wherever there is a recursive solution that has repeated calls for the same inputs, it can be optimized by using dynamic programming. The idea is to simply store the results of sub-problems so that they do not have to be re-computed when needed later. This algorithm thus utilizes the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems. This simple optimization reduces time complexities from exponential to polynomial. It solves problems that display the properties of overlapping sub-problems and optimal sub-structure both of which are present in the 0–1 knapsack problem.

Example for finding an optimal solution using dynamic programming.
Time Complexity: O (N*W).
where ‘N’ is the number of weight elements and ‘W’ is the capacity of the knapsack.
2)Greedy Algorithm:
Greedy is an algorithmic method that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal solutions also lead to the global solution are best fit for Greedy. This method is mainly used for the Fractional Knapsack Problem. The basic idea of the greedy approach in this problem is to calculate the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can. This will always be the optimal solution to this problem.
But the greedy algorithm does not always give the optimal solution for the 0/1 knapsack problem because this algorithm does not always consider the full object but can consider a fraction of the object too to maintain the capacity of the knapsack and maximize the profit. But in the 0/1 knapsack problem, we cannot consider a fraction of the object and have to consider the full object only. Thus it can be seen that the greedy method does not always guarantee the optimal solution for the 0/1 problem but works for the fractional one.
Time Complexity: O(n*logn)
If using a simple sort algorithm (selection, bubble) then the complexity of the whole problem is O(n²).
If using quick sort or merge sort then the complexity of the whole problem is) O(n*logn). As the main time taking step is sorting, the whole problem can be solved in O(n*logn) only.
3)Branch and Bound Algorithm:
A Branch-and-Bound algorithm is based on two main operations: branching, that is, dividing the problem to be solved in smaller subproblems, in such a way that no feasible solution is lost; and bound, that is, computing an upper bound (for a maximization problem) on the optimal solution value of the current subproblem so that eventually the subproblem can be solved.
This algorithm is based on a state-space tree. The state-space tree is a root of the tree where every level represents a decision in the solution space that relies on the upper level and any conceivable solution is represented by a few ways beginning at the root and finishing with a leaf. The root stays at level 0 and represents the state where no incomplete solution has been made. A leaf has no youngsters and represents the state where all decisions making up an answer have been made.

The brute force method can be improved by backtracking. This backtracking method can be improved further if we know the bound on the best possible optimal solution making the branch and bound approach to be better than backtracking or brute force.
Time complexity: O(2n)
In the worst case, the algorithm will generate all intermediate stages and all leaves. Therefore, the tree will be complete then the Time complexity = O (2n)
CONCLUSION:
Greedy algorithm seems to be the most efficient (time complexity) but it fails to give the correct optimal solution for the 0/1 knapsack problem. The Dynamic programming technique is also very efficient and the most favorable algorithm to solve the 0/1 knapsack problem in general but the memory utilized by this technique is the highest among the three approaches considered. Thus, the most efficient approach for the Knapsack Problem among the three is the Branch and Bound technique. It is simple and is easy to apply, and can be applied to solve the knapsack problem under all the circumstances.
The above-given article is a summary of what I learned about the 0/1 knapsack problem. Though it does not cover everything it can give one a basic idea about the problem and different methods to solve it. Hope this helps!
