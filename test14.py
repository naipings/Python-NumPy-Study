# 查找
'''
这里约定：查找是返回数组中符合条件的元素的索引号，或返回和数组具有相同结构的布尔型数组，
元素符合条件在布尔型数组中对应 True, 否则对应 False。
'''

# (1)最大值和最小值查找
# 下面的代码演示了返回数组中最大值和最小值的索引号，如果是多维数组，这个索引号是数组转成一维之后的索引号：
import numpy as np

a = np.random.random((2, 3))
print(a)
'''
[[8.87088817e-01 7.79736355e-02 1.41140542e-01]
 [6.77817843e-04 1.53763453e-01 9.19320791e-01]]
'''
# 最大值的索引号：
print(np.argmax(a))
# 5

# 最小值的索引号：
print(np.argmin(a))
# 3


# (2)非零元素查找
# 下面代码演示了返回数组中非零元素的索引号：
import numpy as np

a = np.random.randint(0, 2, (2, 3))
print(a)
print(np.nonzero(a))
'''
[[0 0 0]
 [1 1 0]]

(array([1, 1]), array([0, 1]))
'''


# (3)使用逻辑表达式查找
# 下面的代码演示了使用逻辑表达式查找符合条件的元素，返回结果是一个和原数组结构相同的布尔型数组，
# 元素符合条件在布尔型数组中对应True，否则对应False ：
import numpy as np

a = np.arange(10).reshape((2, 5))
print(a)
print((a>3)&(a<8))
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]

[[False False False False  True]
 [ True  True  True False False]]
'''


# (4)使用where条件查找
# np.where() 函数返回数组中满足给定条件的元素和索引号，其结构为元组，元组的第 k 个元素对应符合条件的元素在数组 k 轴上的索引号。
# 这句话可以简单理解为，一维数组返回一个元素的元组，二维数组返回两个元素的元组，以此类推。
# np.where() 函数还可以用于替换符合条件的元素：
import numpy as np

a = np.arange(10)
print(a)
print(np.where(a<5))
'''
[0 1 2 3 4 5 6 7 8 9]

(array([0, 1, 2, 3, 4]),)
'''

a = a.reshape((2, -1))
print(a)
print(np.where(a<5))
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]

(array([0, 0, 0, 0, 0]), array([0, 1, 2, 3, 4]))
'''

# 满足条件的元素不变，其他元素乘10 ：
print(np.where(a<5, a, 10*a))
'''
[[ 0  1  2  3  4]
 [50 60 70 80 90]]
'''