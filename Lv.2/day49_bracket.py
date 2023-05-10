# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def right(p):
    r = True
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt < 0:
            r = False
            break
    return r

def solution(p):
    answer = ''
    if p != '':
        cnt = 0
        for i in range(len(p)):
            if p[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                u = p[:i+1]
                v = p[i+1:]
                break

        if right(u):
            answer += u + solution(v)
        else:
            answer += '(' + solution(v) + ')'
            u = u[1:-1]
            for j in u:
                if j == '(':
                    answer += ')'
                else:
                    answer += '('
            
    return answer