class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = 10**5
        n = len(nums)

        max1 = max2 = max3 = -math.inf
        min1 = min2 =  math.inf

        for x in nums:
            # Track the 3 largest numbers
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x

            # Track the 2 smallest numbers
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x

        # Compute the largest possible pair product
        max_pair = max(max1 * max2, min1 * min2)

        # Compute the most negative (lowest) pair product
        min_pair = min(min1 * max1, min1 * max2, min2 * max1, min2 * max2)

        # Try replacing one number with +100000 or -100000
        with_M = max(M * max_pair, -M * min_pair)

        if n == 3:
            # If there are only 3 numbers, one of them must be replaced
            return with_M

        # If there are more than 3 numbers, maybe the original best triple is better
        keep_orig = max(max1 * max2 * max3, min1 * min2 * max1)

        # Return the best possible product
        return max(keep_orig, with_M)
            
