def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name))
print(find_same_name(name2))

def find_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"

stu = {39 : "Justin",
       14 : "John",
       67 : "Mike",
       105 : "Summer"}
print(find_name(stu, 14))
print(find_name(stu, 140))