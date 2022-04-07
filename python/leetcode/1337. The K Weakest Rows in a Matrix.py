
# 풀이1
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for i in range(len(mat)):
            result.append((i, sum(mat[i])))
        
        result.sort(key=lambda x:x[1])
        return [x[0] for x in result[:k]]


# 풀이 2
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        answer = {}
        for i in range(len(mat)):
            answer[i] = sum(mat[i])
        
        answer = sorted(answer, key= answer.get)
        return answer[:k]