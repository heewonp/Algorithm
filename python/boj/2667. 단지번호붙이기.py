from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


cnt_list = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]


# bfs
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_list.append(bfs(i,j))


# dfs
def dfs(x,y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            cnt_list.append(cnt)
            cnt = 0



print(len(cnt_list))
for i in sorted(cnt_list):
    print(i)



