# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def find_divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            cnt += 1 
            if n/i != i: 
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        cnt = find_divisor(i)
        if cnt > limit:
            cnt = power
        answer += cnt
    return answer