import sys
input = sys.stdin.readline

doc = input().strip()
find = input().strip()

cnt = 0
index = 0


while index <= len(doc)-len(find):
    if doc[index:index + len(find)] == find:
        cnt += 1
        index += len(find)
    else:
        index += 1


print(cnt)