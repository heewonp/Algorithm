class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = [set() for i in range(10)]
        
        for j in range(0, len(rings),2):
            rods[int(rings[j+1])].add(rings[j])
            
        cnt = 0
        for rod in rods:
            if len(rod) == 3:
                cnt += 1
        return cnt
                