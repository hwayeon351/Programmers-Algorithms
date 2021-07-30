from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0: return 5*len(cities)
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize: cache.popleft()
            cache.append(city)
            answer += 5
        else:
            del cache[cache.index(city)]
            cache.append(city)
            answer += 1
    return answer
