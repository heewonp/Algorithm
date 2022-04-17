import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 최대 재귀함수 깊이 설정 해주지 않으면 런타임에러 발생
n,m = map(int,input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
 
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] =b

for _ in range(m):
    x,a,b = map(int,input().split())
    if x:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)