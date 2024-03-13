# 创建 ndarray
'''
NumPy最重要的一个特点就是 ndarray(N-dimensional array)，即 N 维数组），该对象是一个快速而灵活的大数据集容器。
你可以利用这种数组对整块数据执行一些数学运算，其语法跟标量元素之间的运算一样。
'''

# 创建numpy数组的方式：
import numpy as np

print(np.__version__)
# 1.24.3

nparr = np.array([i for i in range(10)])
print(nparr)
# [0 1 2 3 4 5 6 7 8 9]


# (2) arange 创建数组:
# arange函数是python内置函数range函数的数组版本。
# 产生0-9共10个元素：
ndarray = np.arange(10)
print(ndarray)
# [0 1 2 3 4 5 6 7 8 9]

# 产生从10-19共10个元素：
ndarray1 = np.arange(10, 20)
print(ndarray1)
# [10 11 12 13 14 15 16 17 18 19]

# 产生10 12 14 16 18；2为 step ：
ndarray2 = np.arange(10, 20, 2)
print(ndarray2)
# [10 12 14 16 18]
print(ndarray2.shape)
# (5,)


# (3) linspace 创建有连续间隔的数组：
'''
也可以称为线性等分向量(linear space)，在一个指定区间内按照指定的步长，将区间均等分，生成的是一个线段类型的数组。
生成的线性间隔数据中，是有把区间的两端加进去的。
'''
# 创建线段型数据：
data= np.linspace(1,10,20) # 开始端1，结束端10，且分割成20个数据，生成线段
print(data)
# 


# (4) repeat 重复构造法
'''
repeat()函数用来重复数组元素。
但如果被重复的数组是一个多维数组，且 repeat() 函数指定了 axis 参数，情况就会变得有些复杂。
'''
a = np.arange(5)
print(a)
# [0 1 2 3 4]

# 重复一维数组元素3次：
print(np.repeat(a, 3))
# [0 0 0 1 1 1 2 2 2 3 3 3 4 4 4]

a = np.arange(6).reshape((2, 3))
print(a)
'''
[[0 1 2]
 [3 4 5]]
'''
# 重复二维数组元素3次，不指定轴：
print(np.repeat(a, 3))
# [0 0 0 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5]

# 重复二维数组元素3次，指定0轴：
print(np.repeat(a, 3, axis=0))
'''
[[0 1 2]
 [0 1 2]
 [0 1 2]
 [3 4 5]
 [3 4 5]
 [3 4 5]]
'''

# 重复二维数组元素3次，指定1轴：
print(np.repeat(a, 3, axis=1))
'''
[[0 0 0 1 1 1 2 2 2]
 [3 3 3 4 4 4 5 5 5]]
'''

# 补充，注意：(与repeat() 不同)，tile() 函数将整个数组而非数组元素水平和垂直重复指定的次数：
a = np.arange(5)
print(a)
# [0 1 2 3 4]

# 重复一维数组3次：
print(np.tile(a, 3))
# [0 1 2 3 4 0 1 2 3 4 0 1 2 3 4]

# 重复一维数组3行2列：
print(np.tile(a, (3, 2)))
'''
[[0 1 2 3 4 0 1 2 3 4]
 [0 1 2 3 4 0 1 2 3 4]
 [0 1 2 3 4 0 1 2 3 4]]
'''

a = np.arange(6).reshape((2, 3))
print(a)
'''
[[0 1 2]
 [3 4 5]]
'''
# 重复二维数组3次：
print(np.tile(a, 3))
'''
[[0 1 2 0 1 2 0 1 2]
 [3 4 5 3 4 5 3 4 5]]
'''

# 重复二维数组2行3列：
print(np.tile(a, (2, 3)))
'''
[[0 1 2 0 1 2 0 1 2]
 [3 4 5 3 4 5 3 4 5]
 [0 1 2 0 1 2 0 1 2]
 [3 4 5 3 4 5 3 4 5]]
'''


# (5) 其他创建 numpy 数组的方式
# (5-1) 使用 zeros 和 eros_like 创建数组：
'''
用于创建数组，数组元素默认值是 0. 
注意: zeros_linke 函数只是根据传入的 ndarray 数组的 shape 来创建所有元素为 0 的数组，并不是拷贝源数组中的数据.
'''
ndarray4 = np.zeros(10)
ndarray5 = np.zeros((3, 3))
ndarray6 = np.zeros_like(ndarray5)  # 按照 ndarray5 的shape创建数组
# 打印数组元素类型
print("以下为数组类型:")
print('ndarray4:', type(ndarray4))
print('ndarray5:', type(ndarray5))
print('ndarray6:', type(ndarray6))
print("-------------")
print("以下为数组元素类型:")
print('ndarray4:', ndarray4.dtype)
print('ndarray5:', ndarray5.dtype)
print('ndarray6:', ndarray6.dtype)
print("-------------")
print("以下为数组形状:")
print('ndarray4:', ndarray4.shape)
print('ndarray5:', ndarray5.shape)
print('ndarray6:', ndarray6.shape)
'''打印结果如下：
以下为数组类型:
ndarray4: <class 'numpy.ndarray'>
ndarray5: <class 'numpy.ndarray'>
ndarray6: <class 'numpy.ndarray'>
-------------
以下为数组元素类型:
ndarray4: float64
ndarray5: float64
ndarray6: float64
-------------
以下为数组形状:
ndarray4: (10,)
ndarray5: (3, 3)
ndarray6: (3, 3)
'''


# (5-2) 使用 ones 和 ones_like 创建数组：
# 用于创建所有元素都为 1 的数组. ones_like 用法同 zeros_like 用法。
# 创建数组，元素默认值是 1
ndarray7 = np.ones(10)
print(ndarray7)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

ndarray8 = np.ones((3, 3))
ndarray9 = np.ones_like(ndarray5)  # 按照 ndarray5 的 shape 创建数组
print(ndarray9)
'''打印结果：
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''


# (5-3) 使用 empty 和 empty_like 创建数组：
ndarray10 = np.empty(5)
print(ndarray10)
'''
[6.94322984e-310 1.85024422e-316 3.75028236e-317 3.66256792e-317
 2.37151510e-322]
'''

ndarray11 = np.empty((2, 3))
ndarray12 = np.empty_like(ndarray11)
print(ndarray12)
'''
[[6.94322984e-310 6.94322984e-310 1.77459490e+248]
 [4.29058029e+270 1.33733641e+160 3.85175668e-110]]
'''


# (5-4) 使用 eye 创建对角矩阵数组：
# 该函数用于创建一个 N*N 的矩阵，对角线为 1，其余为 0.
ndarray13 = np.eye(5)
print(ndarray13)
'''
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
'''


# (5-5) 使用 full 创建数组：
ndarray14 = np.full((3, 5), 666)
print(ndarray14)
'''
[[666 666 666 666 666]
 [666 666 666 666 666]
 [666 666 666 666 666]]
'''