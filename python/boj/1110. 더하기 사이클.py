N = int(input())
num = N
cnt = 0

while True:
    a = num // 10 # 10으로 나눈 몫
    b = num % 10 # 10으로 나눈 나머지
    c = (a+b) % 10 # 둘을 더해주고 10으로 나눈 나머지 
    num = (b*10)+c # 새로운 수 만들어 줌
    cnt += 1 # 사이클 더해줌
    if(num == N): 
        break
print(cnt)