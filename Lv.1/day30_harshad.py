# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    s = sum(map(int,str(x)))
    if x % s == 0:
        return True
    else:
        return False