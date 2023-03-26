# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    mid = total//num # 중간값 찾기
    diff = num//2 # 중간값과 끝값과의 차이
    last = mid+diff+1 # range로 리스트 생성하려면 마지막에 +1 해주어야 함
    answer = list(range(last-num, last)) # 첫번째 값은 last에서 num 만큼 빼줌
    return answer