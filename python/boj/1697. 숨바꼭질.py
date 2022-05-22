from collections import deque

max = 100000
n,k = map(int,input().split())
visited = [0] * (max+1)

def bfs():
    queue = deque([n])

    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v])
            break
        for i in (v-1,v+1,2*v):
            if 0 <= i <= max and not visited[i]:
                visited[i] = visited[v]+1
                queue.append(i)

bfs()