# key映射到多个值的字典

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(10)

print(d)

s = defaultdict(set)
s['a'].add(1)
s['a'].add(1)
s['a'].add(2)
s['b'].add(3)
s['b'].add(4)
print(s)