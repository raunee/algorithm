# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant)-Counter(completion)
    return list(answer.keys())[0]