# 数组函数
# 通用函数：快速的元素级数组函数
'''
通用函数（即 universal function ）是一种对 ndarray 中的数据执行元素级运算的函数。
你可以将其看做简单函数（接受一个或多个标量值，并产生一个或多个标量值）的矢量化包装器。 
许多 ufunc 都是简单的元素级变体，如 sqrt 和 exp :
'''
import numpy as np

# 测试一元函数：
ndarray1 = np.array([3.5, 1.7, 2.2, -7.8, np.nan, 4.6, -3.4])
print(ndarray1)
'''
[ 3.5  1.7  2.2 -7.8  nan  4.6 -3.4]
'''

# abs 计算整数、浮点数的绝对值：
print(np.abs(ndarray1))
'''
[3.5 1.7 2.2 7.8 nan 4.6 3.4]
'''

# square 计算各元素的平方，相当于 arr ** 2 ：
print(np.square(ndarray1))
'''
[12.25  2.89  4.84 60.84   nan 21.16 11.56]
'''

# sign 计算各元素的正负号,1(正数)、0（零）、-1(负数) ：
print(np.sign(ndarray1))
'''
[ 1.  1.  1. -1. nan  1. -1.]
'''

# ceil 计算各元素的celling值，即大于该值的最小整数：
print(np.ceil(ndarray1))
'''
[ 4.  2.  3. -7. nan  5. -3.]
'''

# floor 计算各元素的floor值，即小于等于该值的最大整数：
print(np.floor(ndarray1))
'''
[ 3.  1.  2. -8. nan  4. -4.]
'''

# rint 将各元素值四舍五入到最近的整数，保留 dtype ：
print(ndarray1.dtype)
print(np.rint(ndarray1))
print(np.rint(ndarray1).dtype)
'''
float64
[ 4.  2.  2. -8. nan  5. -3.]
float64
'''

# isnan 返回一个表示“那些是NaN（这不是一个数字）”的布尔类型数组：
print(np.isnan(ndarray1))
'''
[False False False False  True False False]
'''


# 测试二元函数：
ndarray2 = np.random.randint(1, 20, (4, 5))
ndarray3 = np.random.randint(-10, 10, (4, 5))
ndarray3 = np.where(ndarray3 == 0, 1, ndarray3)
print(ndarray2)
print(ndarray3)
'''
[[ 7 19 11  1  3]
 [ 4  5  6 19  9]
 [10  1  4 15 18]
 [13 17 11 17 17]]

[[  1 -10  -4  -5  -6]
 [-10 -10   9   8   9]
 [ -8   3   1  -2   9]
 [-10   8   7   8  -8]]
'''

# add 将数组中对应的元素相加：
print(np.add(ndarray2, ndarray3))
'''
[[ 8  9  7 -4 -3]
 [-6 -5 15 27 18]
 [ 2  4  5 13 27]
 [ 3 25 18 25  9]]
'''

# subtract 从第一个数组中减去第二个数组中的元素：
print(np.subtract(ndarray2, ndarray3))
'''
[[ 6 29 15  6  9]
 [14 15 -3 11  0]
 [18 -2  3 17  9]
 [23  9  4  9 25]]
'''

# maximum、fmax 从两个数组中取出最大值。fmax 将忽略NaN ：
print(np.maximum(ndarray2, ndarray3))
'''
[[ 7 19 11  1  3]
 [ 4  5  9 19  9]
 [10  3  4 15 18]
 [13 17 11 17 17]]
'''

# mod 元素级的求模计算.相当于Python模运算符``x1％x2``，并且与除数x2具有相同的符号：
print(np.mod(ndarray2, ndarray3))
'''
[[ 0 -1 -1 -4 -3]
 [-6 -5  6  3  0]
 [-6  1  0 -1  0]
 [-7  1  4  1 -7]]
'''

# copysign 将第二个数组中的值的符号复制给第一个数组中的值：
print(np.copysign(ndarray2, ndarray3))
'''
[[  7. -19. -11.  -1.  -3.]
 [ -4.  -5.   6.  19.   9.]
 [-10.   1.   4. -15.  18.]
 [-13.  17.  11.  17. -17.]]
'''

# greater、greater_equal 执行元素级的运算比较，最终产生布尔类型数组：
print(np.greater(ndarray2, ndarray3))
'''
[[ True  True  True  True  True]
 [ True  True False  True False]
 [ True False  True  True  True]
 [ True  True  True  True  True]]
'''