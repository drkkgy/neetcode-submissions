class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def helper(n):
            if n in mem:
                return mem[n]
            if n <= 2:
                return n
            mem[n] = helper(n-1) + helper(n-2)
            return mem[n]
        return helper(n)
        