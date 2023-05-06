# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    s_list = s.split(' ')
    for word in s_list:
        for i, w in enumerate(word):
            if i % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()
        answer += ' '
    return answer[:-1]