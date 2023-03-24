# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    diff1 = common[1] - common[0]
    diff2 = common[2] - common[1]
    if diff1 == diff2: # 등차수열인지 확인
        answer = common[-1] + diff1
    else: # 등비수열
        if common[1] != 0: # 혹시 0의 이슈..
            div = common[1] / common[0]
            answer = common[-1] * div
        else: # 등비에서 0이 나오면 무조건 0
            answer = 0
    return answer