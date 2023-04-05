# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for i in range(len(food[1:])):
        half = food[i+1]//2
        answer += half*str(i+1)
    answer += '0' + answer[::-1]
    return answer