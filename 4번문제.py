def Question4(n,t,m,timeTable):
    shuttleTime = [] #셔틀버스 도착시간 초기화
    timeTable = sorted(timeTable) #크루 도착시간 정렬
    
    for i in range(n):
        shuttleTime.append(getShuttleTime(i,t)) #셔틀버스 도착시간 입력

    k = 0 #timeTable 순서
    lastTime = ''

    for i in range(len(shuttleTime)):
        for j in range(m):
            if k < len(timeTable):
                if 1 <= getNumber(timeTable[k]) and getNumber(timeTable[k])<=getNumber(shuttleTime[i]):
                    lastTime = timeTable[k]
                    k += 1
            else:
                return shuttleTime[len(shuttleTime)-1] #자리가 남아있을 경우 맨마지막 셔틀버스 도착시간 입력

    if lastTime == '':
        return shuttleTime[len(shuttleTime)-1] #타는사람이 하나도 없을경우 맨마지막 셔틀버스 도착시간 입력
    
    return getTime(getNumber(lastTime)) #꽉 찼을경우 맨마지막 크루 도착시간 -1분전 입력

def getShuttleTime(n,t):
    oldMin = n*t
    if oldMin < 60:
        newMin = 900 + oldMin
    else:
        newMin = 900+100*int(oldMin/60)+int(oldMin%60)
    result = str(newMin).rjust(4, '0')
    return result[0:2]+':'+result[2:4]

def getNumber(time):
    return 100*int(time[0:2])+int(time[3:5])

def getTime(Number):
    if Number%100 == 0:
        Number -= 41
    else:
        Number -= 1
    result = str(Number).rjust(4, '0')
    return result[0:2]+':'+result[2:4]
    
