Python Cookbook

第一章：数据结构和算法

1.1：	将序列分解为单独的变量

​	包含N个元素的元组或者序列，分解成N个变量

1.2：	从任意长度的可迭代对象中分解元素

​	从任意长度的可迭代对象中分解元素

1.3：	保存最后N个元素

​	希望在迭代或是其他形式的处理过程中对最后几项记录做一个有限的历史记录

​	collections.deque

1.4：	找到最大或最小的N个元素

​	在某个集合中找出最大或最小的N个元素

​	heapq模块，nlargest()和nsmallest()，能接受key作为比较的标准

​	heapq模块，heapify(可迭代对象)，0位置最小，heappop(heap)跳出最小的

1.5：	实现优先级队列

​	实现一个队列，能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的元素

​		将priority变为负值，这样求最小就能得出最大，pop直接可以取出最小值

​		将需要比较的值设为元组的第一个值，比较元组的方式会使得第一个值为比较对象

1.6：	在字典中将键映射到多个值上

​	创建一个能将key映射到多个值的字典

​		多个值保存到一个容器中，作为value

​		collections.defaultdict(list/set)

1.7：让字典保持有序

​	创建一个字典，对字典做迭代或序列化操作时，也能控制其中元素的顺序

​		collections.OrderedDict
1.8：与字典有关的计算问题

​	在字典上对数据执行各种计算

​		利用zip将key和value变成一个元组，然后sorted（zip可以反转键值对，这样更加方便）

​		sorted，min，max等函数的key值设定

1.9:	在两个字典中寻找相同点

​	keys，values，items方法返回的可以直接使用类似set的交并差集计算

1.10:	从序列中移除重复项且把钱藕池元素间顺序不变

​	使用生成器配合一个记录已出现值的列表来把重复值剔除

1.11:	对切片命名

​	slice(start,stop,step)

1.12：找出序列中出现次数最多的元素

​	collections.Counter类，most_common

1.13:	通过公共键对字典列表排序

​	获取字典一个key对应的值，operator.itemgetter函数

1.14:	对不原生支持比较操作的对象排序

​	sorted函数的key使用lambda或operator.attgetter函数来获得一个对象的对应属性值

1.15:	根据字段将记录分组

​	itertools.groupby函数（要先排序）

1.16:	筛选序列中的元素

​	列表推导式和生成器，filter函数

​	itertools.compress

1.17:	从字典中提取子集

​	字典推导式

1.18:	将名称映射到序列的元素中

​	collections.namedtuple

1.19：	同时对数据做转换和换算

​	在函数参数中使用生成器

1.20：	将多个映射合并为单个映射

​	collections中的ChainMap模块

