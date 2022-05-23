from collections import deque

t = int(input())

def bfs():
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if abs(x-end[0]) + abs(y-end[1]) <= 1000:
            return True
        for i in range(n):
            if not visited[i]:
                dx, dy = store[i]
            if abs(x-dx) + abs(y-dy) <= 1000:
                queue.append((dx, dy))
                visited[i] = 1
    return False


for i in range(t):
    n = int(input())
    start = list(map(int, input().split())) # 집좌표
    store =[] # 편의점 좌표
    for j in range(n):
        store.append(list(map(int,input().split())))
    end = list(map(int, input().split())) # 페스티벌 좌표
    visited = [0 for _ in range(n+1)]
    if bfs():
        print('happy')
    else:
        print('sad')


