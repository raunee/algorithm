# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def prime_number(n):
    for i in range(2, int(n**(1/2)+1)):
        if n%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for c in comb:
        s = sum(c)
        if prime_number(s):
            answer += 1
    return answer