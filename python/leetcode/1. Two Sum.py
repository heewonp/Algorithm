
# 풀이 1 o(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 temp = nums[i] + nums[j]
#                 if temp == target:
#                     return [i,j]


# 풀이 2 o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict ={}
        
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in num_dict:
                return [i,num_dict[temp]]
            num_dict[nums[i]]=i