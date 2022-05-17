class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(x,y):
            if x <0 or x >=m or y < 0 or y >=n:
                return 1

            if (x,y) in v :
                return 0

            if grid[x][y] == 1:
                v.add((x,y))
            
                return dfs(x-1,y) + dfs(x,y-1) + dfs(x+1,y) + dfs(x,y+1)
            return 1
                
        
        m = len(grid)
        n = len(grid[0])
        v = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)
        