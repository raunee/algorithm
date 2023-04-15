# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def getTernary(n, t):
    q, r = divmod(n, 3)
    t += str(r)
    if q == 0 :
        return t
    else :
        return getTernary(q, t)

def solution(n):
    answer = 0
    s = ''
    ternary = getTernary(n, s)
    for i in range(len(ternary), 0, -1):
        answer += int(ternary[-i])*(3**(i-1))
    return answer