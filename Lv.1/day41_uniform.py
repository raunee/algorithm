# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    res = [r for r in sorted(reserve) if r not in lost]
    los = [l for l in sorted(lost) if l not in reserve]
    for r in res:
        if r-1 in los:
            los.remove(r-1)
        elif r+1 in los:
            los.remove(r+1)
    return n-len(los)