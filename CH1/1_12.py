# 找出序列中出现次数最多的元素

words = [1, 2, 3, 4, 5, 1, 2, 3, 8, 5, 10, 29, 23, 45]

from collections import Counter

word_counts = Counter(words)
print(word_counts.most_common(3))
print(word_counts[1])

#counter的对象支持+和-

