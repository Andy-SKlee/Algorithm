def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(fact(1))
print(fact(5))
print(fact(10))

def fact2(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact2(1))
print(fact2(5))
print(fact2(10))

def sumall(n):
    if n <= 1:
        return 1
    return n + sumall(n-1)
print(sumall(10))

def find_max(a, n):
    if n == 1:
        return a[0]
    max_num = find_max(a, (n - 1))
    if max_num >= a[n - 1]:
        return max_num
    else:
        return a[n - 1]
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))