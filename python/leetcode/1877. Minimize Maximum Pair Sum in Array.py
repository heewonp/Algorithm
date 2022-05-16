class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        temp = []
        
        for i in range(len(nums)//2):
            nums_sum = nums[i] + nums[~i]
            temp.append(nums_sum)
        
        return max(temp)