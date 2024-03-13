# 随机数生成函数
'''
numpy.random 模块对 Python 内置的 random 进行了补充。
我们使用 numpy.random 可以很方便根据需要产生大量样本值。而 python 内置的 random 模块则一次生成一个样本值。
具体函数见截屏。
'''
import numpy as np

ndarray1 = np.arange(10)
print(ndarray1)
# [0 1 2 3 4 5 6 7 8 9]

print(np.random.permutation(5))
# [3 1 4 0 2]

print(np.random.permutation(ndarray1))
# [9 1 7 5 3 8 4 0 6 2]

print(ndarray1)
np.random.shuffle(ndarray1)
print(ndarray1)
'''
[0 1 2 3 4 5 6 7 8 9]

[3 9 1 2 4 6 5 0 7 8]
'''

print(np.random.randint(10, 20))
# 18

print(np.random.randint(10, 20, 20))
# [13 17 11 12 19 16 19 18 13 12 16 10 16 16 12 12 19 15 19 16]

print(np.random.randint(10, 20, (3, 4)))
'''
[[10 13 19 19]
 [19 19 17 12]
 [12 17 17 12]]
'''