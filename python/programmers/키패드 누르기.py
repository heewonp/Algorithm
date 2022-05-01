def solution(numbers, hand):
    answer = ''
    point = { 1:[0,0],2:[0,1],3:[0,2],
             4:[1,0],5:[1,1],6:[1,2],
             7:[2,0],8:[2,1],9:[2,2],
             '*':[3,0],0:[3,1],'#':[3,2]}
    
    left = point['*']
    right = point['#']
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left = point[i]
            
        elif i in [3,6,9]:
            answer += 'R'
            right = point[i]
        else:
            left_d = abs(left[0]-point[i][0]) + abs(left[1]-point[i][1])
            right_d = abs(right[0]-point[i][0]) + abs(right[1]-point[i][1])
            
            if left_d < right_d:
                answer += 'L'
                left = point[i]
                
            elif left_d > right_d:
                answer += "R"
                right = point[i]
            
            else:
                if hand == 'left':
                    answer += 'L'
                    left = point[i]
                else:
                    answer += 'R'
                    right = point[i]
            
    return answer