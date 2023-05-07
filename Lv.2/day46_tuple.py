# https://school.programmers.co.kr/learn/courses/30/lessons/64065

from collections import Counter
import re

def solution(s):
    answer = []
    s = re.findall("\d+", s)
    c = Counter(s).most_common()
    for i in c:
        answer.append(int(i[0]))
    return answer