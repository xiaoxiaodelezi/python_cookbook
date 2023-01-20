# 有一系列的字典或者对象实例，根据某个特定的字段来分组迭代数据

rows = [
    {
        'address': '5412 N CLARK',
        'date': '07/01/2012'
    },
    {
        'address': '5418 N CLARK',
        'date': '07/01/2012'
    },
    {
        'address': '5800 E 58TH',
        'date': '07/02/2012'
    },
    {
        'address': '2122 N CLARK',
        'date': '07/03/2012'
    },
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
