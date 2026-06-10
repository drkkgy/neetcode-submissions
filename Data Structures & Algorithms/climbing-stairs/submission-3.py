class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dp(n):
            
            if n in mem:
                return mem[n]

            if n <= 2:
                return n

            mem[n] = dp(n-1) + dp(n-2)
            return mem[n]
        return dp(n)

            
            
                 
        