def check(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True

def sep(p):
    open_c = 0
    close_c = 0
    u = ''
    v = ''
    
    for i in range(len(p)):
        if p[i] == '(':
            open_c += 1
        else:
            close_c += 1
        
        if open_c == close_c:
            u = p[:i + 1]
            v = p[i + 1:]
            break
        
    return u,v

def change(p):
    temp = ''
    for i in p:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def solution(p):
    if len(p) == 0:
        return ''
    
    if check(p):
        return p
    
    u,v = sep(p)
    if check(u):
        u += solution(v)
        return u
    else:
        return '(' + solution(v) + ')' + change(u[1:-1])