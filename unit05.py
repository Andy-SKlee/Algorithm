def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))

def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a % b)

print(gcd2(1, 5))
print(gcd2(3, 6))
print(gcd2(60, 24))
print(gcd2(81, 27))

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = 10
result = []
for i in range(0, n):
    result.append(fibo(i))
print(result)