class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0

        # buy = float('inf')
        # maxi = 0

        # for price in prices:
        #     buy = min(buy, price)
        #     profit = price - buy
        #     maxi = max(maxi, profit)

        # return maxi

        l=0             #using sliding window
        maxi=0

        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxi=max(maxi,profit)
            else:
                l=r

        return maxi

