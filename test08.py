# 可以通过数组上的一组数学函数对整个数组或某些数据进行统计计算。
# 基本的数组统计方法：见截屏。

# 多维数组默认统计全部维度，axis 参数可以按指定轴心统计，值为 0 则按列统计，值为 1 则按行统计。
import numpy as np

ndarray1 = np.random.randint(1, 10, (4, 5))
print(ndarray1)
'''
[[5 7 8 6 6]
 [8 7 6 6 1]
 [1 4 7 8 1]
 [7 8 2 4 8]]
'''

# (1) sum 求元素和：
# 0-列 1-行
# sum-计算所有元素和：
print(np.sum(ndarray1))
'''
110
'''

# sum-计算每一列的元素和：
print(np.sum(ndarray1, axis=0))
'''
[21 26 23 24 16]
'''

# sum-计算每一行的元素和：
print(np.sum(ndarray1, axis=1))
'''
[32 28 21 29]
'''


# (2) argmax 求最大值索引：
# argmax-默认情况下按照一维数组索引：
print(np.argmax(ndarray1))
'''
2
'''

# argmax-统计每一列最大值的下标索引：
print(np.argmax(ndarray1, axis=0))
'''
[1 3 0 2 3]
'''

# argmax-统计每一行最大值的下标索引：
print(np.argmax(ndarray1, axis=1))
'''
[2 0 3 1]
'''


# (3) mean 求平均数：
# mean-求所有元素的平均值：
print(np.mean(ndarray1))
'''
5.5
'''

# mean-求每一列元素的平均值：
print(np.mean(ndarray1, axis=0))
'''
[5.25 6.5  5.75 6.   4.  ]
'''

# mean-求每一行元素的平均值：
print(np.mean(ndarray1, axis=1))
'''
[6.4 5.6 4.2 5.8]
'''


# (4) cumsum 求元素累计和：
# cumsum-前面元素的累计和：
print(np.cumsum(ndarray1))
'''
[  5  12  20  26  32  40  47  53  59  60  61  65  72  80  81  88  96  98
 102 110]
'''

# cumsum-每一列元素的累计和：
print(np.cumsum(ndarray1, axis=0))
'''
[[ 5  7  8  6  6]
 [13 14 14 12  7]
 [14 18 21 20  8]
 [21 26 23 24 16]]
'''

# cumsum-每一行元素的累计和：
print(np.cumsum(ndarray1, axis=1))
'''
[[ 5 12 20 26 32]
 [ 8 15 21 27 28]
 [ 1  5 12 20 21]
 [ 7 15 17 21 29]]
'''


# all 和 any 函数
import numpy as np

# 判断两个数组元素是否相等：
ndarray1 = np.arange(6).reshape((2, 3))
ndarray2 = np.arange(6).reshape((2, 3))
print(ndarray1)
print(ndarray2)
'''
[[0 1 2]
 [3 4 5]]

[[0 1 2]
 [3 4 5]]
'''

ndarray3 = np.array([[ 0,  1,  2], [ 8,  9, 10]])
print(ndarray3)
'''
[[ 0  1  2]
 [ 8  9 10]]
'''

print((ndarray1 == ndarray2).all())
'''
True
'''

print((ndarray1 == ndarray3).all())
'''
False
'''

print((ndarray1 == ndarray3).any())
'''
True
'''