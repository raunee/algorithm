# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        s = t[i:i+len(p)]
        if int(s) <= int(p):
            answer += 1
    return answer