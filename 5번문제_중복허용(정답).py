import collections

def Question5(str1,str2): #중복허용 할때

    if not(len(str1) >= 2 and len(str1) <= 1000):
        return 'out of range!'
    if not(len(str2) >= 2 and len(str2) <= 1000):
        return 'out of range!'

    str1 = str1.upper()
    str2 = str2.upper()

    collect1 = collections.defaultdict(int)
    collect2 = collections.defaultdict(int)
    collectList = set('')
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            collect1[str1[i]+str1[i+1]] += 1
            collectList.add(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            collect2[str2[i]+str2[i+1]] += 1
            collectList.add(str2[i]+str2[i+1])

    intersectionCount = 0
    unionCount = 0

    for i in collectList: 
        if collect1[i]>0 and collect2[i]>0: #교집합 카운트
            if collect1[i] < collect2[i]:
                intersectionCount += collect1[i]
            else:
                intersectionCount += collect2[i]
        if collect1[i] > collect2[i]: #합집합 카운트
            unionCount += collect1[i]
        else:
            unionCount += collect2[i]

    if intersectionCount == 0 or unionCount == 0:
        result = 65536
    else:
        result = int(intersectionCount/unionCount*65536)
            
    return result
