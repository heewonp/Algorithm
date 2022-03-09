def solution(s):
    answer = []
    temp_word = s.split(' ')
    for word in temp_word:
        res =''
        for i in range(len(word)):
            if i % 2:
                res += word[i].lower()
            else:
                res += word[i].upper()
        answer.append(res)
    return ' '.join(answer)