# 从序列中移除重复项目且保持元素间顺序不变


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


def dedupe_(items, key=None):
    seen = set()
    for item in items:
        val = item if key == None else key(item)
        if val not in seen:
            yield item
            seen.add(val)