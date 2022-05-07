import sys
input = sys.stdin.readline

h,k = map(int,input().split())
cnt = 0
for i in range(h+1):
    if i < 10:
        i = '0'+str(i)
    for j in range(60):
        if j < 10:
            j = '0'+str(j)
        for x in range(60):
            if x < 10:
                x = '0'+str(x)
            if str(k) in str(i)+str(j)+str(x):
                cnt +=1

print(cnt)