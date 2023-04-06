# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    w, h = 0, 0
    for size in sizes:
        w = max(w, size[0])
        h = max(h, size[1])
    return w*h