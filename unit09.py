def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result
d = [2, 4, 5, 1, 3]
print(ins_sort(d))

def ins_sort2(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value

b = [2, 4, 5, 1, 3]
ins_sort2(b)
print(b)

def ins_sort2(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] < value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value

c = [2, 4, 5, 1, 3]
ins_sort2(c)
print(c)