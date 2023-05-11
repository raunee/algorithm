# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for case in permutations(dungeons):
        k_copy = k
        cnt = 0
        for i in range(len(case)):
            if k_copy >= case[i][0]:
                k_copy -= case[i][1]
                cnt += 1
                if i == len(case) - 1:
                    answer = max(answer, cnt)
                    break
            else:
                answer = max(answer, cnt)
                break
    return answer