import sys
input = sys.stdin.readline
left_stack = list(input().rstrip())
right_stack = []
m = int(input())

for _ in range(m):
    cursor = input().split()
    if cursor[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cursor[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cursor[0] == 'B':
        if left_stack:
            left_stack.pop()
    else:
        left_stack.append(cursor[1])

print(''.join(left_stack + right_stack[::-1]))
