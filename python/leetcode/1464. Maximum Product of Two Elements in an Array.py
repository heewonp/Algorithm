class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        num_sort = self.sort(nums)
        
        return (num_sort[-1]-1) * (num_sort[-2]-1)
    
    
    # sort함수 대신 퀵소트 직접 구현 
    def sort(self, nums):
        if len(nums) <= 1 : return nums
        
        left,right = list(),list()
        pivot = nums[0]
        
        for index in range(1,len(nums)):
            if nums[index] < pivot:
                left.append(nums[index])
            else:
                right.append(nums[index])
        
        num_sort = self.sort(left) + [pivot] + self.sort(right)
        
        return num_sort