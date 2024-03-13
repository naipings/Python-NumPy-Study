# 数组排序函数
import numpy as np

# (1) 对一维数组排序：
ndarray1 = np.random.randint(1, 10, (1, 5))
print(ndarray1)
# [[4 6 3 3 5]]

ndarray1.sort()
print(ndarray1)
# [[3 3 4 5 6]]


# (2) 对二维数组排序：
ndarray2 = np.random.randint(1, 10, (5, 5))
print(ndarray2)
'''
[[9 8 5 3 2]
 [6 5 8 8 4]
 [1 2 1 3 9]
 [8 8 8 5 1]
 [2 8 5 4 3]]
'''

# 对每行数据进行排序：
ndarray2.sort()  
print(ndarray2)
'''
[[2 3 5 8 9]
 [4 5 6 8 8]
 [1 1 2 3 9]
 [1 5 8 8 8]
 [2 3 4 5 8]]
'''

# 对每列数据进行排序：
ndarray2.sort(axis=0)  
print(ndarray2)
'''
[[1 1 2 3 8]
 [1 3 4 5 8]
 [2 3 5 8 8]
 [2 5 6 8 9]
 [4 5 8 8 9]]
'''


ndarray2 = np.random.randint(1, 10, (5, 5))
print(ndarray2)
'''
[[5 5 5 2 1]
 [1 7 5 3 9]
 [2 2 1 1 5]
 [4 5 3 9 4]
 [9 7 2 8 8]]
'''

ndarray3 = np.sort(ndarray2)  # 返回排序副本，源数据不变
print(ndarray2)
print(ndarray3)
'''
[[5 5 5 2 1]
 [1 7 5 3 9]
 [2 2 1 1 5]
 [4 5 3 9 4]
 [9 7 2 8 8]]

[[1 2 5 5 5]
 [1 3 5 7 9]
 [1 1 2 2 5]
 [3 4 4 5 9]
 [2 7 8 8 9]]
'''


# (3) argsort 函数(很重要)， argsort 函数返回的是数组值从小到大的索引值：
import numpy as np
x = np.arange(10)
print(x)
# [0 1 2 3 4 5 6 7 8 9]

np.random.shuffle(x)
print(x)
# [0 6 4 7 5 8 2 9 3 1]

print(np.argsort(x))
# [0 9 6 8 2 4 1 3 5 7]



# 复制函数
import numpy as np

a = np.arange(6).reshape((2, 3))
b = a.view()
print(b is a)
print(b.base is a)
print(b.flags.owndata)
'''
False
False
False
'''

c = a.copy()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
'''
False
False
True
'''