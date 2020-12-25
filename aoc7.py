res = []
def trim_pref(st):
    stCopy = st
    trimmed = ""
    for i in range(len(st)):
        if (st[i].isnumeric()):
            trimmed += st[i]
            stCopy = st[i + 1:]

    return stCopy, trimmed

class Node:
    color: str
    number: int
    
    def __init__(self, c):
        c1 = c.replace("\n", "")
        c2 = c1.replace(" ", "")
        c2 = c2.removesuffix(".")
        c2 = c2.removesuffix("s")
        c2, trimmed = trim_pref(c2)
        self.color = c2
        if (len(trimmed) > 0):
            self.number = int(trimmed)
        else:
            self.number = 0

def process_input():
    file = open('aoc7-input.txt', 'r')
    lines = file.readlines()

    adj = {}
    for line in lines:
        elems = line.split(" contain ")
        right_part = elems[1].split(",")
        elems[0] = elems[0].replace(" ", "")
        elems[0] = elems[0].removesuffix("s")
        adj[elems[0]] = []
        for el in right_part:
            adj[elems[0]].append(Node(el))


    return adj

def dfs_util(adj, k, visited):
    visited.add(k)
    res = 1
    for neighbor in adj[k]:
        if neighbor.color == "nootherbag":
            return 1
        if neighbor not in visited:
            res += neighbor.number * dfs_util(adj, neighbor.color, visited)
    return res
    


def dfs(k):
    adj = process_input()
    res.append(0)
    visited = set()
    
    return dfs_util(adj, k, visited)

adj = process_input()
for k in adj:
    if (k == "shinygoldbag"):
        print(dfs(k) - 1)
