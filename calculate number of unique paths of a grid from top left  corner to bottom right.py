def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):  
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print(f"The number of unique paths in a {m}x{n} grid: {unique_paths(m, n)}")
