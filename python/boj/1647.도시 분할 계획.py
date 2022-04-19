import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
parent = [0] * (n+1)
edges = []

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
    x,y,z = map(int,input().split())
    edges.append([z,x,y])
edges.sort()

answer = []
res = 0

for edge in edges:
    weight,node_v,node_u = edge
    if find(node_v) != find(node_u):
        union(node_v,node_u)
        res += weight
        answer.append(weight)
        
res -= answer.pop()

print(res)