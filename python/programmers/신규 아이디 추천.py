import re
def solution(new_id):
    
    # 1번,2번
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())

    # 3번
    answer = re.sub('\.\.+','.',answer)
    
    # 4번
    answer = answer.strip('.')
    
    # 5번
    if answer =='':
        answer ='a'
    else :
        answer
        
    #6번
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    
    #7번
    answer  += answer[-1] * (3-len(answer))
    return answer