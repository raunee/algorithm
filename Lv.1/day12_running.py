# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    player_dic = {i: player for i,player in enumerate(players)}
    rank_dic = {player: i for i,player in enumerate(players)}
    for calling in callings:
        rank = rank_dic[calling]
        front = player_dic[rank-1]
        rank_dic[calling] = rank-1
        rank_dic[front] = rank
        player_dic[rank-1] = calling
        player_dic[rank] = front
    answer = list(player_dic.values())
    return answer