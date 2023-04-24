# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    return (n**(1/2)+1)**2 if int(n**(1/2)) == n**(1/2) else -1