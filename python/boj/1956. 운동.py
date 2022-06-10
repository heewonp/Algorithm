import sys
input = sys.stdin.readline
v,e = map(int,input().split())

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

graph = graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    # a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(v+1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)