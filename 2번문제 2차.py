import re

def Question2(dartResult):
    arr = re.findall('\d+\D+',dartResult)
    for i in range(3):
        if '*' in arr[i]:
            if i == 0:
                arr[i] += '2'
            else:
                arr[i] += '2'
                arr[i-1] += '*2'
        if 'S' in arr[i]:
            arr[i] = arr[i].replace('S','**1')
        if 'D' in arr[i]:
            arr[i] = arr[i].replace('D','**2')
        if 'T' in arr[i]:
            arr[i] = arr[i].replace('T','**3')
        if '#' in arr[i]:
            arr[i] = arr[i].replace('#','*(-1)')
    total = '+'.join(arr)
    return eval(total)

