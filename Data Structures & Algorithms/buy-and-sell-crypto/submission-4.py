class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  We try the two pointer solution

        maxp = 0

        l,r = 0,1

        while r < len(prices):

            # the sell condtion 
            if prices[l] < prices[r]:

                profit  = prices[r] - prices[l]
                maxp = max(profit,maxp)

            else:
                l = r
            r += 1

        return maxp



        