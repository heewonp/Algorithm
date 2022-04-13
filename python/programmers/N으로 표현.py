def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9):
        num = set()
        num.add(int(str(N)*i))
        
        for j in range(0,i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    num.add(x+y)
                    num.add(x-y)
                    num.add(x * y)
                    
                    if y != 0:
                        num.add(x//y)
                
        if number in num:
            answer = i
            break

        dp.append(num)
                    
    return answer