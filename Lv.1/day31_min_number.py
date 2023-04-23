# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    if arr == []:
        arr = [-1]
    return arr