def process_input():
    file = open('aoc6-input.txt', 'r')
    raw = file.read()
    lines = raw.split("\n\n")

    linesModified = []
    for i in range(len(lines)):
        linesModified.append(lines[i].split("\n"))
    return linesModified

def get_result():
    lines = process_input()
    res = 0

    for sl in lines:
        temp = {}
        cnt = 0
        for st in sl:
            for ch in st:
                if (ch in temp):
                    temp[ch] += 1
                else:
                    temp[ch] = 1
             
        for k in temp:
            if (temp[k] == len(sl)):
                res += 1

    return res
    
print(get_result())
