# 改变数组结构
'''
NumPy 之所以拥有极高的运算速度，除了并行、广播和矢量化等技术因素外，
其数组存储顺序和数组视图相互独立也是一个很重要的原因。
改变数组结构的操作通常不会改变所操作的数组本身的存储顺序，只是生成了一个新的视图。
np.resize()函数是个例外，它不返回新的视图，而是真正改变了数组的存储顺序
'''

import numpy as np

a = np.arange(12)
# reshape() 函数返回数组a的一个新视图，但不会改变数组a ：
b = a.reshape((3, 4))
print(a.shape)
# (12,)

print(b is a)
# False

print(b.base is a)
# True

# resize() 函数没有返回值，但真正改变了数组a的结构：
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
a.resize([4, 3])
print(a)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

# 返回多维数组一维化的视图，但不会改变原数组：
print(a.ravel())
print(a)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11]

[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

# 返回行变列的视图，但不会改变原始图：

print(a.transpose())
print(a)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]

[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

# 返回行变列的视图，等价于 transpose() 函数：
print(a.T)
print(a)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]

[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

# 翻滚轴，1轴变0轴：
print(np.rollaxis(a, 1, 0))
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
'''


'''
翻滚轴函数有一个很容易理解的应用，就是用它来实现图像的通道分离。
下面的代码生成了一个宽为 800 像素、高为 600 像素的彩色随机噪声图，使用翻滚轴函数可以将其分离成 RGB 三个颜色通道：
'''
from PIL import Image
import numpy as np

img = np.random.randint(0, 256, (600, 800, 3), dtype=np.uint8)
print(img.shape)
# (600, 800, 3)

# 将图像数据分离成 RGB 三个颜色通道：
r, g, b = np.rollaxis(img, 2, 0)
print(r.shape, g.shape, b.shape)
# (600, 800) (600, 800) (600, 800)

Image.fromarray(img).show()
