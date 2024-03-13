# 添加和删除函数
# reshape：有返回值，即不对原始多维数组进行修改； 
# resize：无返回值，即会对原始多维数组进行修改。

import numpy as np

ndarray1 = np.arange(4)
ndarray2 = np.arange(4)
print(ndarray2)
'''
[0 1 2 3]
'''

ndarray3 = np.arange(12).reshape((3, 4))
print(ndarray3)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''


# (1) append 数组中追加元素：
'''
NumPy 数组一旦创建不能再改变其元素数量。
如果要动态改变数组元素数量，只能通过合并或拆分的方法生成新的数组。
NumPy 仍然保留了 append() 函数，只不过这个函数不再是数组的函数，而是升级到最外层的 NumPy 命名空间了，
并且该函数的功能不再是追加元素，而是合并数组。
'''
# 数组追加一个数值元素：
print(ndarray1)
print(np.append(ndarray1, 100))
'''
[0 1 2 3]

[  0   1   2   3 100]
'''

# 在一维数组后追加一维数组：
print(ndarray2)
print(np.append(ndarray1, ndarray2))
'''
[0 1 2 3]

[0 1 2 3 0 1 2 3]
'''

# 在二维数组后追加标量元素：
print(ndarray3)
print(np.append(ndarray3, 100))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

[  0   1   2   3   4   5   6   7   8   9  10  11 100]
'''

# append总是返回一维数组：
print(np.append(ndarray1, ndarray3))
'''
[ 0  1  2  3  0  1  2  3  4  5  6  7  8  9 10 11]
'''

print('----------------------------------------------------------------')
'''
补充：
hstack() 水平合并函数, vstack() 垂直合并函数, dstack() 深度合并函数：
'''
a = np.arange(4).reshape(2, 2)
b = np.arange(4, 8).reshape(2, 2)
print(a)
print(b)
'''
[[0 1]
 [2 3]]

[[4 5]
 [6 7]]
'''
# 水平合并
print(np.hstack((a, b)))
'''
[[0 1 4 5]
 [2 3 6 7]]
'''
# 垂直合并
print(np.vstack((a, b)))
'''
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
'''
# 深度合并
print(np.dstack((a, b)))
'''
[[[0 4]
  [1 5]]

 [[2 6]
  [3 7]]]
'''

# stack() 函数使用 axis 轴参数指定合并的规则：
a = np.arange(60).reshape(3, 4, 5)
b = np.arange(60).reshape(3, 4, 5)
print(a.shape, b.shape)
print(np.stack((a, b), axis=0).shape)
print(np.stack((a, b), axis=1).shape)
print(np.stack((a, b), axis=2).shape)
print(np.stack((a, b), axis=3).shape)
'''
(3, 4, 5) (3, 4, 5)
(2, 3, 4, 5)
(3, 2, 4, 5)
(3, 4, 2, 5)
(3, 4, 5, 2)
'''


# (2) concatenate 合并两个数组元素：
ndarray4 = np.arange(12).reshape((3, 4))
print(ndarray4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 合并两个一维数组：
print(np.concatenate((ndarray1, ndarray2)))
'''
[0 1 2 3 0 1 2 3]
'''

# 合并两个二维数组：
print(np.concatenate((ndarray3, ndarray4), axis=0))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 合并两个二维数组：
print(np.concatenate((ndarray3, ndarray4), axis=1))
'''
[[ 0  1  2  3  0  1  2  3]
 [ 4  5  6  7  4  5  6  7]
 [ 8  9 10 11  8  9 10 11]]
'''


# (3) delete 删除一行或者一列数组元素：
ndarray5 = np.arange(20).reshape((4, 5))
print(ndarray5)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''

# 删除第0行元素：
print(np.delete(ndarray5, 0, axis=0))
'''
[[ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''

# 删除第2列元素：
print(np.delete(ndarray5, 1, axis=1))
'''
[[ 0  2  3  4]
 [ 5  7  8  9]
 [10 12 13 14]
 [15 17 18 19]]
'''

# 删除第0、2、3列元素：
print(np.delete(ndarray5, [0, 2, 3], axis=1))
'''
[[ 1  4]
 [ 6  9]
 [11 14]
 [16 19]]
'''

# 使用np.s_[::]创建切片对象，
# 删除从1、2列元素：
print(np.delete(ndarray5, np.s_[1:3], axis=1))
'''
[[ 0  3  4]
 [ 5  8  9]
 [10 13 14]
 [15 18 19]]
'''


# (4) insert 插入元素：
# 在第2个位置插入元素 100 ：
ndarray6 = np.arange(4)
print(ndarray6)
print(np.insert(ndarray6, 1, 100))
'''
[0 1 2 3]

[  0 100   1   2   3]
'''

# 在第3个位置插入两个元素10、20 ：
print(np.insert(ndarray6, 2, [10, 20]))
'''
[ 0  1 10 20  2  3]
'''

# 在第2行插入一行元素：
print(np.insert(ndarray6, 1, np.array([100, 200, 300, 400]), axis=0))
'''
[  0 100 200 300 400   1   2   3]
'''

# 在第3列插入一列元素：
ndarray7 = np.arange(12).reshape((3, 4))
print(ndarray7)
print(np.insert(ndarray7, 2, np.array([100, 200, 300]), axis=1))
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

[[  0   1 100   2   3]
 [  4   5 200   6   7]
 [  8   9 300  10  11]]
'''