R = 3
C = 3
def min_cost_memo(cost,m,n,memo):
    if (n<0 or m<0) :
        return float('inf')
    elif (m==0 and n==0):
        return cost[m][n]
    if memo[m][n] != -1:
        return memo[m][n]
    memo[m][n] = cost[m][n]+ min(min_cost_memo(cost, m-1, n-1, memo),min_cost_memo(cost, m-1, n, memo),min_cost_memo(cost, m, n-1,memo))
    return memo[m][n]

def min_cost(cost,m,n):
    memo = [[-1]*C for _ in range(R)]
    return min_cost_memo(cost,m,n,memo)

cost = [
    [1,2,3],
    [4,8,2],
    [1,5,3]
]
print(min_cost(cost,2,2))