import datetime
from time import localtime,strftime

def Question7(lines):
    start = []
    end = []
    maxCount = 0

    #시간저장
    for i in range(len(lines)):
        endTime = datetime.datetime.strptime(lines[i][0:23],'%Y-%m-%d %H:%M:%S.%f')
        processTime = int(float(lines[i][24:30].replace('s',''))*1000000) - 1000 #-1000 시작시간 포함
        startTime = endTime + datetime.timedelta(microseconds = -processTime)
        end.append(endTime.strftime('%Y%m%d%H%M%S%f'))
        start.append(startTime.strftime('%Y%m%d%H%M%S%f'))

    return len(lines)

    #스캔
    for i in range(len(lines)):
        startNum = int(end[i])
        endNum = int(end[i])+1000000 - 1000 #100만 = 1초
        count = 0
        for j in range(len(lines)):
            if i == j: #자신포함
                count += 1
            elif startNum <= int(start[j]) <= endNum: #끝~끝+1초 사이에 시작점있을경우
                count += 1
            elif startNum <= int(end[j]) <= endNum: #끝~끝+1초 사이에 끝점있을경우
                count += 1
            elif int(start[j]) <= startNum <= int(end[j]):
                count += 1
            elif int(start[j]) <= endNum <= int(end[j]):
                count += 1

        if maxCount < count:
            maxCount = count
    
    return maxCount
