#针对任意多的分隔符拆分字符串
import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))
