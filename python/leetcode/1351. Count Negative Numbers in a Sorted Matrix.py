# 풀이 1

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        answer = []
        for i in grid:
            for j in i:
                if j < 0 :
                    answer.append(j)
        return len(answer)
    
    

# 풀이 2 binary search 방식

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        for i in grid:
            answer += len(i) - self.binary(i,-1,0,len(i))
        
        return answer
    
    
    def binary(self,row,target,left,right):

        while left < right:
            mid = (left + right) // 2

            if row[mid] > target:
                left = mid + 1
            else:
                right = mid

        return left 
        