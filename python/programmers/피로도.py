from itertools import permutations

def solution(k, dungeons):
    
    dungeons_all = list(permutations(dungeons,len(dungeons)))
    res = []
                        
    for dungeon in dungeons_all:
        p = k
        answer = 0
        for x in dungeon:
            if p >= x[0]:
                p -= x[1]
                answer += 1
            else:
                break
        res.append(answer)

    return max(res)