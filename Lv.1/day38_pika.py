# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    choice = len(nums)/2
    nums = list(set(nums))
    if len(nums) > choice:
        answer = choice
    else:
        answer = len(nums)
    return answer