# 字典在做迭代化或序列化操作时，能控制其元素顺序

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['gork'] = 4

for key in d:
    print(key, d[key])

import json

print(json.dumps(d))
