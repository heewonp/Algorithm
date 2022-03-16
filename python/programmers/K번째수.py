def solution(array, commands):
    answer = []
    for command in commands:
        com_list = array[command[0]-1:command[1]]
        com_list.sort()
        answer.append(com_list[command[2]-1])
    return answer