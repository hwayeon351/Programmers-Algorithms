def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0: return len(cities)*5
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
    return answer
