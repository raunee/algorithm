# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if not s:
            a = -a
        answer += a
    return answer