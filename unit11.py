def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))

def quick_sort2_sub(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    quick_sort2_sub(a, start, i - 1)
    quick_sort2_sub(a, i + 1, end)

def quick_sort2(a):
    quick_sort2_sub(a, 0, len(a) - 1)

e = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort2(e)
print(e)

print("-" * 20)
def bubble_sort(a):
    cnt = 0
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            print(a)
            a[i - 1], a[i] = a[i], a[i - 1]
            cnt += 1
    if cnt == 0:
        return a
    else:
        bubble_sort(a)

f = [2, 4, 5, 1, 3]
bubble_sort(f)
print(f)
print("-" * 20)

def bubble_sort2(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
        if changed == False:
            return
g = [2, 4, 5, 1, 3]
bubble_sort2(g)
print(g)