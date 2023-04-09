# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_en = ['zero', 'one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine']
    for i in range(len(num_en)):
        s = s.replace(num_en[i], str(i))
    return int(s)