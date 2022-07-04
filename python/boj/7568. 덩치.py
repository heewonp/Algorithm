import sys
input = sys.stdin.readline
n = int(input())

wh_data = []

for _ in range(n):
    weight, height = map(int,input().split())
    wh_data.append([weight,height])


for i in wh_data:
    rank = 1
    for j in wh_data:
        if i[0] < j[0] and i[1] <j[1]:
            rank += 1

    print(rank, end= " ")
