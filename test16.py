# 自定义广播函数

# 使用np.frompyfunc()定义广播函数：
'''
使用 np.frompyfunc() 将数值函数转换成数组函数需要提供三个参数：数值函数、输入函数的个数和返回值的个数。
另外, np.frompyfunc() 返回的广播函数，其返回值是 object 类型，最终需要根据实际情况显式地转换数据类型。
'''
import numpy as np

def func_demo(x, y):
    if x == 0 or y == 0 or x == y:
        return 0
    elif x&(x-1) == 0 and y&(y-1) == 0: # x和y都是2的整数次幂
        return max(x, y)
    elif x&(x-1) == 0: # 仅有x等于2的整数次幂
        return x
    elif y&(y-1) == 0: # 仅有y等于2的整数次幂
        return y
    else:
        return max(x, y)

uf = np.frompyfunc(func_demo, 2, 1)
a = np.random.randint(0, 256, (2,5), dtype=np.uint8)
b = np.random.randint(0, 256, (2,5), dtype=np.uint8)
c = uf(a, b)
print(c.dtype) # 此时c的数据类型为object
# object

c = c.astype(np.uint8) # 改变类型
print(c)
'''
[[226 204  87 189 114]
 [183 176  74 158  64]]
'''


# 使用 np.vectorize() 定义广播函数：
'''
np.frompyfunc() 适用于多个返回值的函数。
如果返回值只有一个，使用 np.vectorize() 定义广播函数更方便，并且还可以通过 otypes 参数指定返回数组的元素类型。
'''
import numpy as np

def func_demo(x, y):
    if x == 0 or y == 0 or x == y:
        return 0
    elif x&(x-1) == 0 and y&(y-1) == 0: # x和y都是2的整数次幂
        return max(x, y)
    elif x&(x-1) == 0: # 仅有x等于2的整数次幂
        return x
    elif y&(y-1) == 0: # 仅有y等于2的整数次幂
        return y
    else:
        return max(x, y)
uf = np.vectorize(func_demo, otypes=[np.uint8])
c = uf(a, b)
print(c.dtype)
print(c) # 此时c的数据类型为uint8
'''
uint8
[[146 217 121 117 103]
 [221 186  62  64 214]]
'''

"""
注意：
自定义广播函数并不是真正的广播函数，其运行效率和循环遍历几乎没有差别，因此除非确实必要，否则不应该滥用自定义广播函数。
"""