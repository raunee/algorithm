# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alph = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    alph = sorted(set(alph) - set(skip))
    for a in s:
        answer += alph[(alph.index(a) + index) % len(alph)]
    return answer