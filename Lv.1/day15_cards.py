# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for g in goal:
        if cards1 != [] and g == cards1[0]:
            cards1.pop(0)
        elif cards2 != [] and g == cards2[0]:
            cards2.pop(0)
        else:
            print(g)
            answer = 'No'
            break
    return answer