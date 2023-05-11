# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    result=[]
    if len(s)==1:
        answer = 1
    else:
        for i in range(1, (len(s)//2)+1):
            z = ''
            cnt = 1
            tmp=s[:i]
            for j in range(i, len(s), i):
                if tmp==s[j:i+j]:
                    cnt+=1
                else:
                    if cnt!=1:
                        z = z + str(cnt)+tmp
                    else:
                        z = z + tmp
                    tmp=s[j:j+i]
                    cnt = 1
            if cnt!=1:
                z = z + str(cnt) + tmp
            else:
                z = z + tmp
            result.append(len(z))
        answer = min(result)
    return answer