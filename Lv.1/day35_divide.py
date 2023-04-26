# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = [a for a in arr if a%divisor==0]
    return sorted(answer) or [-1]