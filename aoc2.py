from dataclasses import dataclass

@dataclass
class Item:
    minima: int
    maxima: int
    char: str
    password: str

    def __init__(self, mn, mx, ch, ps):
        self.minima = mn
        self.maxima = mx
        self.char = ch
        self.password = ps


def process_password(s):
    l = s.split("-")
    l1= l[1].split(" ")
    
    it = Item(int(l[0]), int(l1[0]), l1[1][0], l1[2])
    return it

def get_result():
    items = []
    cnt = 0
    file = open('aoc2-1input.txt', 'r')
    lines = file.readlines()

    for line in lines:
        items.append(process_password(line))

    for it in items:
        if is_good(it):
            cnt += 1

    return cnt

def is_good(it):
    if (it.password.count(it.char) >= it.minima and it.password.count(it.char) <= it.maxima):
        return True
    return False
    
print(get_result())


