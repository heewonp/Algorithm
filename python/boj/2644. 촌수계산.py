from collections import deque
n = int(input())
a,b = map(int,input().split())
graph = [[]for i in range(n+1)]
visited = [0] * (n+1)
m = int(input())


# bfs
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v]+1
                queue.append(i)

# dfs
def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = visited[start]+1
            dfs(i)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(a)
dfs(a)
print(visited[b] if visited[b] >0 else -1)