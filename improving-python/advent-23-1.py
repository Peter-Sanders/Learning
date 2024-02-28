import time

file = 'advent-23-1.txt'

def solution1(file):
    res = 0
    with open(file, 'r') as f:
        contents = f.read()
        for line in contents.split('\n'):
            if not line:
                break
            arr = []
            for char in line:
                if char.isnumeric():
                    arr.append(char)    
            calibration = arr[0] + arr[-1]
            res += int(calibration) 
    return res 


def solution2(file):
    res = 0
    with open (file, 'r') as f:
        for line in f.readlines():
            print(line)
            back = line[::-1]
            print(back)
            for char in line:
                if char.isnumeric():
                    first = char
                    break 
            for char in back:
                if char.isnumeric():
                    last = char
                    break
            res += int(first + last)
    return res 



start1 = time.time()
sol1 = solution1(file=file)
perf1 = time.time() - start1


start2 = time.time()
sol2 = solution2(file=file)
perf2 = time.time() - start2


print(f'Solution 1: {sol1} in {perf1} seconds')
print(f'Solution 2: {sol2} in {perf2} seconds')
