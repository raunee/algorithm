# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for a in list(s):
        if a in low:
            idx = (low.index(a)+n) % 26
            a = low[idx]
        elif a in upper:
            idx = (upper.index(a)+n) % 26
            a = upper[idx]
        answer += a
    return answer