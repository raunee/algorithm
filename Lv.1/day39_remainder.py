# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(n-1):
        if n % (i+1) == 1:
            return i+1