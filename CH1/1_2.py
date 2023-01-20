#需要从一个长度超过N的迭代对象中分解出N个元素


#去掉第一个和最后一个求中间的平均值
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)  #avg表示平均数函数


record = ('Dave', 'dave@example.com', '773-555-1212', '847-5555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

record = ['ACME', 50, 91.1, (2012, 12, 21)]
name, *_, (*_, day) = record
print(name)
print(day)