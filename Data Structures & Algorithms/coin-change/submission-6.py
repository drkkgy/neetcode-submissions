class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem = {}

        def dp(a):

            if a == 0:
                return 0
            if a in mem:
                return mem[a]
            
            result = float('inf')
            for coin in coins:
                if coin <= a:
                    result = min(result, 1 + dp(a - coin))

            mem[a] = result
            return result
        ans = dp(amount)
        return ans if ans != float('inf') else -1
        
        
        
        