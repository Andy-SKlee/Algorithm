import random
def weigh(a, b, c, d):
    fake = random.randint(0, n)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i
    return -1

n = 100
print(find_fakecoin(0, n - 1))

def weigh2(a, b, c, d):
    fake = random.randint(0, n)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

def find_fakecoin2(left, right):
    if left == right:
        return left
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weigh2(g1_left, g1_right, g2_left, g2_right)
    if result == -1:
        return find_fakecoin2(g1_left, g1_right)
    elif result == 1:
        return find_fakecoin2(g2_left, g2_right)
    else:
        return right
n = 100
print(find_fakecoin2(0, n - 1))