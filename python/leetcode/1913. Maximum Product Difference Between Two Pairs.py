class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        return nums[-2] * nums[-1] - nums[0] * nums[1]