class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        dic = {}
        
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in dic:
                    dic[nums[i+1]] = 1
                else:
                    dic[nums[i+1]] +=1
        
        return max(dic, key = dic.get)