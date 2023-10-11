# LRU(Least Recently Used) 알고리즘
def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if city not in cache :
            cache.append(city)
            time += 5
            if len(cache)>cacheSize:
                cache.pop(0)
        else:
            cache.remove(city)
            cache.append(city) # 가장 최근에 참조되었다는 뜻이기 때문에 맨 끝에 append
            time += 1
    return time