# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer