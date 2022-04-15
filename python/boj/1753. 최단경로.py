import heapq
import sys

x,y = map(int,input().split())
k = int(input())
INF = int(1e9)

graph = [[]for _ in range(x+1)]
queue = []
distance = [INF] * (x+1)

for i in range(y):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
   
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(queue, [distance[start],start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distance[current_node] < current_distance:
            continue
        for next_node, weight in graph[current_node]:
            next_w = current_distance + weight
            
            if next_w < distance[next_node]:
                distance[next_node] = next_w
                heapq.heappush(queue,[next_w,next_node])
dijkstra(k)

for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")