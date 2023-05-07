# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, base) :
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    nums = ''
    for i in range(t * m):
        nums += str(convert(i, n))
        if len(nums) >= t * m:
            break
    answer = nums[p-1::m][:t]
    return answer