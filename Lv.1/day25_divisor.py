# https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            answer += i 
            if n/i != i: 
                answer += (n//i)
    return answer