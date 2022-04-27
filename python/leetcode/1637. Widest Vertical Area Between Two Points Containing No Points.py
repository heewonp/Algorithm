class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points)
        cnt = 0
        for i in range(len(points)-1):
            cnt = max(cnt,points[i+1][0]-points[i][0])
        
        return cnt