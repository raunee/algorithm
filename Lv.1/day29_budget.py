# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    for a in d:
        budget -= a
        if budget < 0:
            break
        answer += 1
    return answer