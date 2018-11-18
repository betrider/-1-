def Question5(str1,str2): #중복허용 안할때
    
    arr1 = ['' for i in range(len(str1)-1)] #배열초기화
    for i in range(len(str1)-1):
        for j in range(2):
            arr1[i] = arr1[i]+str1[i+j].upper() #대소문자 통일


    arr2 = ['' for i in range(len(str2)-1)] #배열초기화
    for i in range(len(str2)-1):
        for j in range(2):
            arr2[i] = arr2[i]+str2[i+j].upper() #대소문자 통일

    return arr2

    intersection = list(set(arr1).intersection(arr2))
    union = list(set(arr1).union(arr2))

    intersectionCount = 0
    unionCount = 0

    for i in range(len(intersection)):
        if intersection[i].isalpha():
            intersectionCount +=1

    for i in range(len(union)):
        if union[i].isalpha():
            unionCount +=1


    if intersectionCount == 0 or unionCount == 0:
        result = 65536
    else:
        result = int(intersectionCount/unionCount*65536)

    return result
