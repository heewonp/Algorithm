import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[]for _ in range(n+1)]
distance = [INF] * (n+1)
queue = []

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    
start, end = map(int, input().split())

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

dijkstra(start)
print(distance[end])