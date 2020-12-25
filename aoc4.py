import re
import string

def process_input():
    file = open("aoc4-input.txt", 'r')
    data = file.read()

    items = data.split("\n\n")
    return items

def byr_good(st):
    p = re.compile("byr:[0-9]{4}")
    x =  p.findall(st)
    if (len(x) == 0):
        return False

    xInt = int(x[0].replace("byr:", ""))

    if (xInt < 1920 or xInt > 2002):
        return False
    return True

def iyr_good(st):
    p = re.compile("iyr:[0-9]{4}")
    x =  p.findall(st)
    if (len(x) == 0):
        return False

    xInt = int(x[0].replace("iyr:", ""))

    if (xInt < 2010 or xInt > 2020):
        return False
    return True

def eyr_good(st):
    p = re.compile("eyr:[0-9]{4}")
    x =  p.findall(st)
    if (len(x) == 0):
        return False

    xInt = int(x[0].replace("eyr:", ""))

    if (xInt < 2020 or xInt > 2030):
        return False
    return True

def hgt_good(st):
    p = re.compile("hgt:[0-9]{2,3}(?:in|cm)")
    x =  p.findall(st)
    if (len(x) == 0):
        return False

    if (x[0].count("in") > 0):
         xM = x[0].replace("hgt:", "")
         xInt = int(xM.replace("in", ""))
         if (xInt < 59 or xInt > 76):
             return False

    if (x[0].count("cm") > 0):
        xM = x[0].replace("hgt:", "")
        xInt = int(xM.replace("cm",""))
        if (xInt < 150 or xInt > 193):
            return False
    return True

def hcl_good(st):
    p = re.compile("hcl:#[0-9a-f]{6}")
    x =  p.findall(st)
    if (len(x) == 0):
        return False
    if (len(x[0]) != 11):
        return False
    return True

def ecl_good(st):
    a = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for i in a:
        if (st.count("ecl:" + i) > 0):
            return True

    return False

def pid_good(st):
    p = re.compile("pid:[0-9]{9}")
    x =  p.findall(st)
    if (len(x) == 0):
        return False
    
    x1 = x[0].replace("pid:", "")
    if (len(x1) != 9):
        return False
    return True

def get_result():
    items = process_input()
    
    cnt = 0

    for it in items:
        if (byr_good(it) and pid_good(it) and eyr_good(it) and
            hcl_good(it) and ecl_good(it) and iyr_good(it) and hgt_good(it)):
            cnt += 1
    print(cnt)

get_result()


