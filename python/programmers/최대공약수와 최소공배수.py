def gcd(n,m):
    while(m):
        n,m = m,n%m
    return n

def lcm(n,m):
    res = (n*m)//gcd(n,m)
    return res

def solution(n, m):
    return [gcd(n,m),lcm(n,m)]