# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    s = s[::-1]
    for i in range(len(s)):
        idx = s[i+1:].find(s[i])
        if idx == -1:
            answer.append(idx)
        else:
            answer.append(idx+1)
    return answer[::-1]