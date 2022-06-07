import sys
input = sys.stdin.readline

s = list(input().strip()) # 공백제거 안해주면 공백포함해서 답이 나오지 않음
t = list(input().strip())

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)