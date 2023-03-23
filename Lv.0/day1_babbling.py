# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    speaking = ['aya', 'ye', 'woo', 'ma'] # 말할 수 있는 발음 리스트
    answer = 0
    for word in babbling: # 주어진 리스트의 단어들 하나씩 검증
        spell = '' # 스펠링 하나씩 추가할 문자열
        baby = [] # speaking에 들어있는 단어 나오면 넣을 리스트
        for w in word:
            spell += w
            if spell in speaking and spell not in baby: # 같은 단어에서는 해당 발음이 한 번만 나와야 함!
                baby.append(spell)
                spell = ''
            else:
                continue
        if spell == '' and baby != []:
            answer += 1            
    return answer