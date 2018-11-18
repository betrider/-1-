def Question3(cacheSize,cities):
    if cacheSize<0 or cacheSize > 30:
        return 'out of range!'
    if cacheSize == 0:
        return len(cities)*5
    cities = [x.lower() for x in cities]
    page = [0 for i in range(cacheSize)]
    rank = [0 for i in range(cacheSize)]
    latestValue = 1
    cacheTime = 0
    for i in range(len(cities)):
        if cities[i] in page:
            Check_num = page.index(cities[i])
            rank[Check_num] = latestValue
            latestValue += 1
            cacheTime += 1 #cache hit
        else:
            Check_num = getLeastRecently(rank)
            page[Check_num] = cities[i]
            rank[Check_num] = latestValue
            latestValue += 1
            cacheTime += 5 #cache miss
    return cacheTime

def getLeastRecently(rank):
    latestValue = rank[0]
    index = 0
    for i in range(len(rank)):
        if latestValue > rank[i]:
            latestValue = rank[i]
            index = i
    return index
