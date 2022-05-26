from collections import deque
def solution(begin, target, words):

    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin,0))
    
    while queue:
        k,cnt = queue.popleft()
        
        if k == target:
            return cnt
        
        for i in range(0,len(words)):
            flag = 0
            word = words[i]
            for j in range(len(k)):
                if k[j] != word[j]:
                    flag += 1
            if flag == 1:
                queue.append((word,cnt + 1))
    return 