n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)


# dfs
def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return True

dfs(graph,1,visited)

print(sum(visited)-1)

# bfs
from collections import deque
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    global cnt
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt +=1

cnt = 0
bfs(graph,1,visited)
print(cnt)