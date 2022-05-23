from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int, input().split())
graph = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,input().split())))

queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx,ny,nz))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs()
flag = False
res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] ==0:
                flag = True
            res = max(res,graph[i][j][k])

if flag:
    print(-1)
else:
    print(res-1)
