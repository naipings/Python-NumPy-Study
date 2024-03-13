# 数组I/O

import numpy as np

a = np.random.random((15, 5))
# 将数组 a 保存成 CSV 格式的数据文件：
np.savetxt('../python_numpy_study/test15.csv', a, delimiter=',')
# 打开CSV格式的数据文件：
data = np.loadtxt('../python_numpy_study/test15.csv', delimiter=',')
print(data.shape, data.dtype)
# (15, 5) float64


# 存储单个数组文件名：
single_arr_fn = '../python_numpy_study/test15_single_arr.npy'
# 存储多个数组文件名：
multi_arr_fn = '../python_numpy_study/test15_multi_arr.npz'
lon = np.linspace(10, 90, 9)
lat = np.linspace(20, 60, 5)
# 用save()函数把经度数组保存成.npy文件：
np.save(single_arr_fn, lon)

# 接着用load()函数读出来：
lon = np.load(single_arr_fn)

# 保存两个数组到一个文件：
np.savez(multi_arr_fn, longitude=lon, latitude=lat)

# 用load()函数把这个.npz文件读成一个结构：
data = np.load(multi_arr_fn)
# 查看所有的数组名：
print(data.files)
# ['longitude', 'latitude']

# 使用data[数组名]就可以取得想要的数据：
print(data['longitude'])
# [10. 20. 30. 40. 50. 60. 70. 80. 90.]