def sum_all(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(sum_all(10))

def sum_all2(n):
    s = n * (n + 1) // 2
    return s

print(sum_all2(10))

def sum_sqr(n):
    s = 0
    for i in range(1, n+1):
        s += i * i
    return s

def sum_sqr2(n):
    s = n * (n + 1) * (2 * n + 1) // 6
    return s
print(sum_sqr(10))
print(sum_sqr2(10))