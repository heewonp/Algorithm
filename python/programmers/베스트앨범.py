def solution(genres, plays):
    answer = []
    tot_dic ={}
    cat_dic = {}
    
            
    for i in range(len(genres)):
        genre =  genres[i]
        play = plays[i]
        
        if genre not in cat_dic:
            tot_dic[genre]=play
            cat_dic[genre]=[(play,i)]
        else:
            tot_dic[genre] += play
            cat_dic[genre].append((play,i))
            
    gen_sort = sorted(tot_dic.items(),key =lambda x: x[1],reverse=True)
    
    
    for genre,totplay in gen_sort:
        cat_dic[genre] = sorted(cat_dic[genre],key=lambda x: (-x[0],x[1]))
        answer += [idx for play, idx in cat_dic[genre][:2]]
    
    
    return answer