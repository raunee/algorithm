# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    lth = []
    for order in orders:
        lth.append(len(order))
    
    for c in course:
        if c <= max(lth):
            menu = []
            for order in orders:
                menu += combinations(sorted(order), c)
            cnts = Counter(menu)
            if max(cnts.values()) > 1:
                for cnt in cnts:
                    if cnts[cnt] == max(cnts.values()):
                        answer.append(''.join(cnt))
        answer.sort()
    return answer