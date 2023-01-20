# 序列中的数据，需要根据某些要求提取或者删减

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

#输出换成生成器
pos = (n for n in mylist if n < 0)
print(pos)

#使用fliter函数
values = ['1', '2', '-3', 'N/A', '-']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


isvals = list(filter(is_int, values))
print(isvals)
