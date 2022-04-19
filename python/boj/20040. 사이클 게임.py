import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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
        parent[a] = b

for i in range(m):
    x,y = map(int,input().split())
    if find(x) == find(y):
        print(i+1)
        break
    union(x,y)
else:
    print(0)