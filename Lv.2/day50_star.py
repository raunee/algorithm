# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    answer = []
    point = []
    point_x = []
    point_y = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            l, k = line[i], line[j]
            fra = (l[0] * k[1]) - (l[1] * k[0])
            if fra != 0:
                x = ((l[1] * k[2]) - (l[2] * k[1])) / fra
                y = ((l[2] * k[0]) - (l[0] * k[2])) / fra
                if x.is_integer() and y.is_integer() and [x, y] not in point:
                    point.append([x, y])
                    point_x.append(int(x))
                    point_y.append(int(y))
    max_x, min_x, max_y, min_y = max(point_x), min(point_x), max(point_y), min(point_y)
    for m in range(max_y-min_y+1):
        ln = ''
        for n in range(max_x-min_x+1):
            if [min_x+n, min_y+m] in point:
                ln += str('*')
            else:
                ln += str('.')
        answer.append(ln)
    answer.reverse()
    return answer