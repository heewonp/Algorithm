import sys
from collections import  deque
input = sys.stdin.readline

n,k = map(int,input().split())
su_arr = [i for i in range(1,n+1)]
q = deque(su_arr)
index = k -1
res = []

while len(q) > 0:
    q.rotate(-index)
    res.append(q.popleft())


print(f"<{', '.join(map(str,res))}>")