# 有一个字典列表，想根据一个或多个字典中的值来对列表排序

rows = [
    {
        'fname': 'Brain',
        'lname': 'Jones',
        'uid': 1003
    },
    {
        'fname': 'David',
        'lname': 'Beazley',
        'uid': 1002
    },
    {
        'fname': 'John',
        'lname': 'Cleese',
        'uid': 1001
    },
    {
        'fname': 'Big',
        'lname': 'Jones',
        'uid': 1004
    },
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
#itemgetter 接受多个键
print(rows_by_fname)
print(rows_by_uid)