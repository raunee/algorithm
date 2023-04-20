# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    n = sorted(str(n), reverse=True)
    answer = ''.join(n)
    return int(answer)