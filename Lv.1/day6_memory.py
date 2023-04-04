# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        lst = [yearning[name.index(p)] for p in pho if p in name]
        answer.append(sum(lst))
    return answer