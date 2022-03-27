class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        num_pow = [x ** 2 for x in nums]
        
        
        return sorted(num_pow)