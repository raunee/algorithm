# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    scores = [0, 0, 0, 0]
    pers_a = ['R', 'C', 'J', 'A']
    pers_b = ['T', 'F', 'M', 'N']
    for s, c in zip(survey, choices):
        c -= 4
        if s[0] in pers_a:
            scores[pers_a.index(s[0])] -= c
        else:
            scores[pers_a.index(s[1])] += c
    for i in range(len(scores)):
        if scores[i] >= 0:
            answer += pers_a[i]
        else:
            answer += pers_b[i]
    return answer