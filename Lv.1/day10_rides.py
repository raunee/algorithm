# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    for c in range(count):
        money = money - price*(c+1)
    if money > 0:
        money = 0
    return -money