class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        temp ={}
        for i in nums:
            if not i in temp.keys():
                temp[i] = 1
            else:
                temp[i] += 1
        
        return max(temp, key = temp.get)