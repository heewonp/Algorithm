class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res = []
        
        for i in range(len(boxes)):
            n = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    n += abs(i-j)
            res.append(n)
        return res