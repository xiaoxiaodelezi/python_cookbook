#在两个字典中寻找可能相同的地方（相同的键、相同的值）

a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
