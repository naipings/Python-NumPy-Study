# ndarray的数据类型及索引

# 3.1.1. ndarray 的数据类型
# dtype（数据类型）是一个特殊的对象，它含有 ndarray 将一块内存解释为特定数据类型所需的信息：
import numpy as np
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)
'''
float64
int32
'''

# Tips：记不住这些 NumPy 的 dtype 也没关系，新手更是如此。
# 通常只需要知道你所处理的数据的大致类型是浮点数、复数、整数、布尔值、字符串，还是普通的Python对象即可。
# 当你需要控制数据在内存和磁盘中的存储方式时（尤其是对大数据集），那就得了解如何控制存储类型。

# 你可以通过 ndarray 的 astype 方法明确地将一个数组从一个 dtype 转换成另一个 dtype ： 
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
# int64
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
# float64

# 在上例中，整数被转换成了浮点数。
# 如果将浮点数转换成整数，则小数部分将会被截取删除：
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
# [ 3.7 -1.2 -2.6  0.5 12.9 10.1]
arr = arr.astype(np.int32)
print(arr)
# [ 3 -1 -2  0 12 10]

# 如果某字符串数组表示的全是数字，也可以用 astype 将其转换为数值形式：
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.dtype)
numeric_strings = numeric_strings.astype(float)
print(numeric_strings)
# [ 1.25 -9.6  42.  ]

'''
注意：使用 numpy.string_ 类型时，一定要小心，因为 NumPy 的字符串数据是大小固定的，发生截取时，不会发出警告。
pandas 提供了更多非数值数据的便利的处理方法

如果转换过程因为某种原因而失败了（比如某个不能被转换为 float64 的字符串），就会引发一个 ValueError。
这里，我比较懒，写的是 float 而不是 np.float64; NumPy 很聪明，它会将 Python 类型映射到等价的 dtype 上。

数组的 dtype 还有另一个属性：
'''
int_array = np.arange(10)
print(int_array)
# [0 1 2 3 4 5 6 7 8 9]
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array = int_array.astype(calibers.dtype)
print(int_array)
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

# 还可以用简洁的类型代码来表示 dtype ：
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
# [41414240        0        0        0       16        0       16        0]

'''
Tips ：调用 astype 总会创建一个新的数组（一个数据的备份），即使新的 dtype 与旧的 dtype 相同。
'''


# 数组显示操作(属性)

# (1) 数组维度 ndim ：
'''
维，就是维度。通常说数组是几维的，就是指维度数，如三维数组的维度数就是 3。
维度数还有一个专用名字，叫秩，也就是数组属性 ndim。
一维数组，类比于一维空间，只有一个轴，那就是 0轴。
二维数组，类比于二维空间，有两个轴，习惯表示成行和列，行的方向是 0轴, 列的方向是 1轴。
三维数组，类比于三维空间，有三个轴，习惯表示成层、行和列，层的方向是 0轴, 行的方向是 1轴, 列的方向是 2轴。
'''
# ndim 属性代表数组维度：
data = np.array([1,2,3])
# data = np.random.randint(1,10, (2,3))
print(data.ndim)
# 1

# (2) 数组形状 shape ：
# shape 属性代表数组形状，可以这么理解shape是各个方向的维度(ndim)。
print(data.shape)
# (3,)

# (3) 数组中元素个数：
print(data.size)
# 3

# (4) 数组的数据类型 dtype ：
print(data.dtype)
# int64