def solution(numbers, target):
    answer = 0
    tree = [0]
    
    for number in numbers:
        sub_tree =[]
        for i in tree:
            sub_tree.append(i + number)
            sub_tree.append(i - number)
        tree = sub_tree
    return tree.count(target)