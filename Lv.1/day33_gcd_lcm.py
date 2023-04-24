# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    n, m = min(n, m), max(n, m)
    div = []
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            if m%i == 0:
                div.append(i)
            if n/i != i:
                if m%(n//i) == 0:
                    div.append(n//i)
    gcd = sorted(div)[-1]
    lcm = n*(m//gcd)
    return [gcd, lcm]