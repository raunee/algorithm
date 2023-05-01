# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for i, a in enumerate(answers):
        if a == stu1[i%len(stu1)]:
            scores[0] += 1
        if a == stu2[i%len(stu2)]:
            scores[1] += 1
        if a == stu3[i%len(stu3)]:
            scores[2] += 1
    answer = [i+1 for i, s in enumerate(scores) if s == max(scores)]
    return answer