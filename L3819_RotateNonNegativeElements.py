class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        indices = [i for i, v in enumerate(nums) if v >= 0]
        m = len(indices)
        
        if m <= 1:
            return nums
        
        k %= m

        values = [nums[i] for i in indices]
        
        # Rotate left using slicing 
        values = values[k:] + values[:k]
        
        # Put back
        for idx, val in zip(indices, values):
            nums[idx] = val
        
        return nums
