# NumPy 数组的运算
'''
数组很重要, 因为它使你不用编写循环即可对数据执行批量运算。NumPy 用户称其为矢量化(vectorization)。
大小相等的数组之间的任何算术运算都会将运算应用到元素级：
（不需要循环即可对数据进行批量运算，叫做矢量化运算. 不同形状的数组之间的算数运算，叫做广播,后面会介绍）
'''
import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
'''
[[1. 2. 3.]
 [4. 5. 6.]]
'''

print(arr * arr)
'''
[[ 1.  4.  9.]
 [16. 25. 36.]]
'''

print(arr - arr)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''

# 数组与标量的算术运算会将标量值传播到各个元素：
print(1 / arr)
'''
[[1.         0.5        0.33333333]
 [0.25       0.2        0.16666667]]
'''

print(arr ** 0.5)
'''
[[1.         1.41421356 1.73205081]
 [2.         2.23606798 2.44948974]]
'''

# 大小相同的数组之间的比较会生成布尔值数组：
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)
'''
[[ 0.  4.  1.]
 [ 7.  2. 12.]]
'''

print(arr2 > arr)
'''
[[False  True False]
 [ True False  True]]
'''


# ----------------------------------------------------
#  数组索引和切片
# Numpy 数组的索引是一个内容丰富的主题，因为选取数据子集或单个元素的方式有很多。一维数组很简单。从表面上看，它们和Python列表的功能差不多。
###  数组索引和切片基本用法

import numpy as np

# 小x可以表示成数学中的向量：
x = np.arange(10)
print(x)
# [0 1 2 3 4 5 6 7 8 9]

# 大X表示矩阵：
X = np.arange(15).reshape((3, 5))
print(X)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

# 访问x中下标是1的元素：
print(x[1])
# 1

# 赋值,损失了精度，截断操作：
x[1] = 3.64
print(x)
# [0 3 2 3 4 5 6 7 8 9]

# 切片：
print(x[1:4])
# [3 2 3]

# 按照先行后列的访问方式：
print(X[1][4])
# 9

# 第二种写法，推荐， 逗号前面是行索引，逗号后面是列索引：
print(X[1,4])
# 9

X[1,4] = 33
print(X)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8 33]
 [10 11 12 13 14]]
'''


"""
由于切片操作是重点，故单独放于一个文件(test04-1.py)
"""


# ----------------------------------------------------------------
# numpy 的特殊之处
'''
当把一个数字值赋值给一个切片时，该值会自动传播到整个选区。
跟列表的区别在于，数组切片是原始数组的视图，这意味着数据不会被赋值，视图上的任何修改都会直接反应到源数组上.
大家可能对此感到不解，由于 Numpy 被设计的目的是处理大数据，如果 Numpy 将数据复制来复制去的话会产生何等的性能和内存问题.
如果要得到一个切片副本的话，必须显式进行复制操作.
'''
# 切片赋值
x[3:6] = 12
print(x)
# [ 0  3  2 12 12 12  6  7  8  9]

arr_slice = x[3:6]
# 对切片的值进行修改，也会体现到原数组身上
arr_slice[0] = 999
print(arr_slice)
# [999  12  12]

print(x)
# [  0   3   2 999  12  12   6   7   8   9]

arr_slice[:] =666
print(x)
# [  0   3   2 666 666 666   6   7   8   9]

# 如果你还是想要数组切片的拷贝而不是一份视图的话，可以进行如下操作：
print(X[:2, 2:4].copy())
'''
[[2 3]
 [7 8]]
'''

# 拿 x 数组做一次具体测试，验证copy()函数：
print(x)
# [  0   3   2 666 666 666   6   7   8   9]

x_copy = x[3:6].copy()
print(x_copy)
# [666 666 666]

x_copy[:] = 111.456
x_copy[0] = 123.789
print(x_copy)
# [123 111 111]

print(x)
# [  0   3   2 666 666 666   6   7   8   9]