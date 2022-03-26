class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
            
        res = []
        for i,j in enumerate(sorted(nums)):
            if j == target:
                res.append(i)
                
        return res