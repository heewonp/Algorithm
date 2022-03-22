class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd


# 방법2

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = [evens for evens in nums if evens %2 == 0 ]
        odd = [odds for odds in nums if odds % 2 != 0]

        return even + odd
                