N,X = map(int,input().split()) # n과 x를 map함수를 이용하여 숫자를 입력받음

num = list(map(int,input().split())) # list값을 입력받음

for i in range(N): # 수열의 개수 n개를 loop
    if num[i] < X: # x보다 작은 수열을 찾아줌
        print(num[i],end=' ') # 참인경우 출력,공백을 위하여 end사용