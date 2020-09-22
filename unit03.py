def samename(l):
    n = len(l)
    sl = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                sl.add(l[i])
    return sl

name = ["Tom", "Jerry", "Mike", "Tom"]
print(samename(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name2))

def couple(l):
    n = len(l)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            print(l[i] + " - " + l[j])
name3 = ["Tom", "Jerry", "Mike"]
couple(name3)