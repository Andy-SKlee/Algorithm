def find_min_idx(a):
    min_idx = 0
    for i in range(0, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        result.append(a.pop(min_idx))
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))

def sel_sort2(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
d = [2, 4, 5, 1, 3]
sel_sort2(d)
print(d)

def sel_sort3(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
d = [2, 4, 5, 1, 3]
sel_sort3(d)
print(d)