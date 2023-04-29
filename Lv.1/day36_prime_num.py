# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def prime_number(n):
    for i in range(2, int(n**(1/2)+1)):
        if n%i==0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime_number(i):
            answer += 1
    return answer

# 에라토스테네스의 체 사용하는 방법

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)