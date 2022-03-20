class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        num_dic={}
        
        for i in nums:
            num_dic[i] = 0
        
        for i in range(len(nums)+1):
            if not i in num_dic:
                return i