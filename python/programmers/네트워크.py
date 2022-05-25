def dfs(node,visited,computers):
    visited[node] = 1
    for i in range(len(computers)):
        if computers[node][i] == 1 and visited[i] ==0:
            dfs(i,visited,computers)
            
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(i,visited,computers)
            answer += 1
    return answer