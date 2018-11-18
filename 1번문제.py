def Question1(n,arr1,arr2):
    if n < 1 or n > 16:
        return 'out of range!'
    arr = []
    for i in range(n):
        temp_str = format(arr1[i]|arr2[i],str(n)+'b')
        temp_str = temp_str.replace('0',' ')
        temp_str = temp_str.replace('1','#')
        arr.append(temp_str)
    return arr
