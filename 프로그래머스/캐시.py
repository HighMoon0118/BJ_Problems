cache = {"start":["","end"], "end":["start",""]}

def remove(a):
    left, right = cache[a]
    cache[left][1] = right
    cache[right][0] = left
def add(a):
    recent = cache["end"][0]
    cache[a] = [recent, "end"]
    cache[recent][1] = a
    cache["end"][0] = a


def solution(cacheSize, cities):
    
    if not cacheSize:
        return 5*len(cities)
    
    cacheSize += 2
    ans = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            remove(city)
            add(city)
            ans += 1
        elif len(cache) < cacheSize:
            add(city)
            ans += 5
        else:
            oldest = cache["start"][1]
            remove(oldest)
            cache.pop(oldest)
            add(city)
            ans += 5
            
    return ans