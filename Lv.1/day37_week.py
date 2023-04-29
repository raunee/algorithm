# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = sum(month[:a-1]) if a != 1 else 0
    date += b
    answer = day[date%7]
    return answer