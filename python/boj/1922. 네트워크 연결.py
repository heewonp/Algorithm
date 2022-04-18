import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
m = int(input())
parent = [0] * (n+1)
rank =[0] * (n+1)
edges = []
res = 0
for i in range(n+1):
    parent[i] = i
    rank[i] =0

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
        
for i in range(m):
    x,y,z = map(int,input().split())
    edges.append([z,x,y])
edges.sort()

for edge in edges:
    weight,node_v,node_u = edge
    if find(node_v) != find(node_u):
        union(node_v,node_u)
        res += weight

print(res)