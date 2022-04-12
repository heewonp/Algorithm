from collections import deque
def solution(n, edge):
    answer = 0
    
    graph = [[] for i in range(n+1)]
    distance = [0] * (n+1)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    distance[1] = 1
    q = deque([1])
    
    while q:
        n = q.popleft()
        
        for i in graph[n]:
            if distance[i] == 0:
                q.append(i)
                distance[i] = distance[n]+1
        
    for j in distance:
        if j == max(distance):
            answer += 1
                
    return answer