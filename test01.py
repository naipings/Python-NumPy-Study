# 我们来直观感受一下 numpy 的运行速度：
# 导入numpy
# 我们将依照标准的Numpy约定，即总是使用import numpy as np
# 当然你也可以为了不写np, 而直接在代码中使用from numpy import *,
# 但是建议你最好还是不要养成这样的坏习惯。
import numpy as np
# 生成一个numpy对象， 一个包含一百万整数的数组
np_arr = np.arange(1000000)
# 一个等价的Python列表：
py_list = list(range(1000000))

# 对各个序列分别平方操作（%time是ipython的特殊功能，用于测试语句运行的时间需要安装ipython， pip install ipython)
for _ in range(10): np_arr2 = np_arr ** 2

for _ in range(10): py_list2 = [x ** 2 for x in py_list]
