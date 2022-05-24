n,m = map(int,input().split())
r,c,d = map(int,input().split())
visited = [[0]*m for i in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited[r][c] =1
cnt = 1
while True:
    flag = False
    for i in range(4):
        nx = r +dx[(3+d)%4]
        ny = c + dy[(3+d)%4]
        if 0 <= nx < n and 0<= ny <= m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            d = (3+d) % 4
            visited[nx][ny] = 1
            r = nx
            c = ny
            cnt +=1
            flag = True
            break
        else:
            d = (3+d)%4

    if not flag:
        if graph[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]
