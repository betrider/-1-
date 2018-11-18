import re

def Question2(dartResult):
    result = re.findall('\d+\D+',dartResult)
    return result
    arr = []
    for i in range(3):
        arr.append(result[i])
        if '*' in arr[i]:
            if i != 0:
                total = total + '*2'
            arr[i] = arr[i]+'2'
        if 'S' in arr[i]:
            arr[i] = arr[i].replace('S','**1')
        if 'D' in arr[i]:
            arr[i] = arr[i].replace('D','**2')
        if 'T' in arr[i]:
            arr[i] = arr[i].replace('T','**3')
        if '#' in arr[i]:
            arr[i] = arr[i].replace('#','*(-1)')
        if i == 0:
            total = arr[i]
        else:
            total = total + '+' + arr[i]
    return eval(total)

