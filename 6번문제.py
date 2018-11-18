def Question6(m,n,board):
    arr = [[board[m][n] for n in range(n)] for m in range(m)]
    count = 0

    while True:
        removeList = set('') #제거 리스트 초기화
        
        for height in range(m-1): #제거할 블록 체크
            for width in range(n-1):
                if arr[height][width] == arr[height][width+1] == arr[height+1][width] == arr[height+1][width+1] != '':
                    removeList.add(str(height)+'/'+str(width))
                    removeList.add(str(height)+'/'+str(width+1))
                    removeList.add(str(height+1)+'/'+str(width))
                    removeList.add(str(height+1)+'/'+str(width+1))

        if len(removeList) == 0:
            return count

        for removeCount in removeList: #제거
            splitData = removeCount.split('/')
            height = int(splitData[0])
            width = int(splitData[1])
            arr[height][width] = ''
            count += 1

        for width in range(n-1): #정렬
            for height in range(m-1):
                if arr[height+1][width] == '':
                    arr[height][width],arr[height+1][width] = arr[height+1][width],arr[height][width]
    
    
