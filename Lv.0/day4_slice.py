# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n): # range(0, len(my_str), n): 0부터 n번째 숫자 리스트
        answer.append(my_str[i:i+n])
    return answer