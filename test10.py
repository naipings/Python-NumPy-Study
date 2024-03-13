# 唯一化和集合函数
'''
Numpy提供了一些针对一维 ndarray 的基本集合运算。最常用的就是 np.unique 了，它用于找出数组中的唯一值并返回已排序的结果。
'''
import numpy as np

# (1) 唯一化
# 测试 np.unique 函数：
ndarray0 = np.random.randint(-10, 10, 10)
print(ndarray0)
ndarray0 = np.unique(ndarray0)
print(ndarray0)
'''
[-10   6   4   4   1  -7   7   7  -8   2]

[-10  -8  -7   1   2   4   6   7]
'''

names = np.array(['aaa', 'bbb', 'ccc', 'aaa', 'ddd', 'eee', 'ccc'])
ndarray1 = np.random.randint(1, 5, 10)
ndarray2 = np.random.randint(1, 5, (3, 4))
print(ndarray1)
print(ndarray2)
'''
[1 4 1 3 4 4 3 2 1 2]

[[1 3 3 2]
 [4 2 2 2]
 [2 4 3 2]]
'''

print(np.unique(names))
'''
['aaa' 'bbb' 'ccc' 'ddd' 'eee']
'''

print(np.unique(ndarray1))
'''
[1 2 3 4]
'''

# 计算两个数组交集：
ndarray3 = np.arange(1, 10)
ndarray4 = np.arange(5, 15)
print(ndarray3)
print(ndarray4)
'''
[1 2 3 4 5 6 7 8 9]

[ 5  6  7  8  9 10 11 12 13 14]
'''

print(np.intersect1d(ndarray3, ndarray4))
'''
[5 6 7 8 9]
'''


# 计算两个数组并集：
ndarray5 = np.arange(1, 10)
ndarray6 = np.arange(5, 15)
print(ndarray5)
print(ndarray6)
'''
[1 2 3 4 5 6 7 8 9]

[ 5  6  7  8  9 10 11 12 13 14]
'''

print(np.union1d(ndarray5, ndarray6))
'''
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
'''


# 数组中的元素是否在另一个数组中存在：
ndarray7 = np.arange(1, 6)
ndarray8 = np.arange(3, 8)
print(ndarray7)
print(ndarray8)
'''
[1 2 3 4 5]

[3 4 5 6 7]
'''

print(np.in1d(ndarray7, ndarray8))
'''
[False False  True  True  True]
'''


# 计算两个数组的差集：
ndarray9 = np.arange(1, 6)
ndarray10 = np.arange(3, 8)
print(ndarray9)
print(ndarray10)
'''
[1 2 3 4 5]

[3 4 5 6 7]
'''

print(np.setdiff1d(ndarray9, ndarray10))
'''
[1 2]
'''