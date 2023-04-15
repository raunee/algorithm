# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def find_divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            cnt += 1 
            if n/i != i: 
                cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        cnt = find_divisor(n)
        if cnt%2 == 0:
            answer += n
        else:
            answer -= n
    return answer