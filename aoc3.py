import math

def process_input(inc):
    file = open('aoc3-1.txt')
    lines = file.readlines()

    mult = math.ceil((len(lines)/len(lines[0])) * (inc + 1))
    processed = []
    for line in lines:
        temp = line.replace("\n", "")
        temp = mult * temp
        processed.append(temp)
    return processed

def get_result(inc):
    cnt = 0
    f = process_input(inc)

    begin = 0
    end = begin + inc + 1

    for i in range(len(f) - 1):
        if (f[i+1][end - 1] == "#"):
            cnt += 1
        begin += inc
        end += inc
    return cnt

def get_result_down_2(inc):
    cnt = 0
    f = process_input(inc)

    begin = 0
    end = begin + inc + 1

    for i in range(0,len(f) - 2, 2):
        if (f[i+2][end - 1] == "#"):
            cnt += 1
        begin += inc
        end += inc

    return cnt
    
    

print(get_result(1) * get_result(3) * get_result(5) * get_result(7) * get_result_down_2(1))
        
