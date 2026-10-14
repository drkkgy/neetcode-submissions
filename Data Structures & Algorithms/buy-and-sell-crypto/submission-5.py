class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i , num in enumerate(prices):
            j = i + 1
            while j < len(prices):

                if (prices[j] - num) > best:

                    best = prices[j] - num
                j += 1

        return best
                




            



        