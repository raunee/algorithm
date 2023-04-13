# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def rank(n):
    if n == 0:
        return 6
    else:
        return 7-n

def solution(lottos, win_nums):
    correct = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
    answer = [rank(correct+lottos.count(0)), rank(correct)]
    return answer