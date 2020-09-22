def search(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search(v, 18))
print(search(v, 33))
print(search(v, 900))

def search2(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if a[i] == x:
            result.append(i)
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search2(v, 18))
print(search2(v, 33))
print(search2(v, 900))

def search_stu(a, b, x):
    for i in range(0, len(a)):
        if a[i] == x:
            return b[i]
    return "?"
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(search_stu(stu_no, stu_name, 39))
print(search_stu(stu_no, stu_name, 14))
print(search_stu(stu_no, stu_name, 10))