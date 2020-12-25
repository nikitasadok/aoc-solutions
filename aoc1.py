input_string = input()

a = input_string.split(" ")

for i in range(len(a)):
    a[i] = int(a[i])

def f():
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if ((a[i] + a[j] + a[k]) == 2020):
                    return a[j] *a[i] * a[k]

    return 0
print(f())
