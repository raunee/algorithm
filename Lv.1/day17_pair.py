# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        str_i = str(i)
        if str_i in X and str_i in Y:
            cnt = min(X.count(str_i), Y.count(str_i))
            answer += str_i*cnt
    if answer == '':
        return '-1'
    else:
        if answer[0] == '0':
            return '0'
        else:
            return answer