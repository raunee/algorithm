# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def calculation(priority, expression):
    ops = ['+', '-', '*']
    spl = re.split('(\d+)', expression)[1:-1]
    for op in priority:
        exp = []
        while len(spl) != 0:
            s = spl.pop(0)
            if s != op:
                exp.append(s)
            else:
                a, b = int(exp.pop()), int(spl.pop(0))
                if op == '+':
                    exp.append(a+b)
                elif op == '-':
                    exp.append(a-b)
                else:
                    exp.append(a*b)
        spl = exp
    return abs(spl[0])
            

def solution(expression):
    answer = 0
    ops = list(set(filter(None, re.split('\d+', expression))))
    priorities = permutations(ops)
    for priority in priorities:
        answer = max(calculation(list(priority), expression), answer)
    return answer