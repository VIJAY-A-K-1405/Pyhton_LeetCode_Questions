class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         # Create a 2D array with all values initialized to 1
        dp = [[1] * n for v in range(m)]
        
        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]