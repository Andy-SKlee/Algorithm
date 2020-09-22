def find_max(l):
    max_x = l[0]
    for i in range(0, len(l)):
        if max_x <= l[i]:
            max_x = l[i]
    return max_x

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))

def find_max_idx(l):
    max_idx = 0
    for i in range(0, len(l)):
        if l[max_idx] <= l[i]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))

def find_min(l):
    min_x = l[0]
    n = len(l)
    for i in range(0, n):
        if min_x >= l[i]:
            min_x = l[i]
    return min_x
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))