def process_input():
    file = open("aoc5-input.txt")
    lines = file.readlines()
    return lines

def generate_possible():
    pos = []
    for i in range(128):
        for j in range(8):
            pos.append((8 * i) + j)

    return pos

def get_result():
    lines = process_input()
    pos = generate_possible()
    mx = 0
    for line in lines:
        row = 0
        col = 0
        st = 0
        end = 127
        stCol = 0
        endCol = 7
        i = 0
        k = 0
        for ch in line:
            if (ch == "F"):
                end = end - 2**(6 - i)
            if (ch == "B"):
                st = st + 2 **(6 - i)
            if (ch == "R"):
                stCol = stCol + 2**(2-k)
                k += 1
            if (ch == "L"):
                endCol = endCol - 2**(2 - k)
                k += 1
            i += 1

        if (line[6] == "F"):
            row = st
        if (line[6] == "B"):
            row = end
        if (line[9] == "L"):
            col = stCol
        if (line[9]  == "R"):
            col = endCol

        ID = row * 8 + col

        if (ID > mx):
            mx = ID

        pos.remove(ID)

    print(pos)

    print(mx)
    return mx

get_result()
        
