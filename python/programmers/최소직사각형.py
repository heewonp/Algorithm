def solution(sizes):
    
    return max(max(i)for i in sizes) * max(min(j) for j in sizes)