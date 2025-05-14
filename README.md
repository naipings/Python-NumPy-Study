# Python-NumPy-Study

## 项目简介

这是一个用于学习和实践 NumPy 的代码仓库，包含各种 NumPy 基础知识和简单应用的代码示例。

## 目录结构

```
.
├── .vscode/                # VS Code 配置文件
├── 原理图/                 # 相关原理图或说明文档
└── testxx.py               # 各章节学习脚本
```

## 环境需求

- **Python**：3.8 及以上版本
- **NumPy**：1.24.3 版本
- **Jupyter Notebook**（可选，用于交互式学习）

## 使用说明

1. 克隆仓库：

```bash
git clone https://github.com/naipings/Python-NumPy-Study.git
```

2. 创建并激活 Conda 环境：

```bash
conda create -n numpy_env python=3.8
conda activate numpy_env
```

3. 安装依赖：

```bash
conda install numpy jupyter
```

4. 运行代码：

- 直接运行 Python 脚本：

```bash
python test01.py
```

- 或在 Jupyter Notebook 中运行：

```bash
jupyter notebook
```

## 学习资源推荐

- [NumPy 官方文档](https://numpy.org/doc/stable/)
- [NumPy 教程](https://numpy.org/numpy-tutorials/)
- 书籍：《Python for Data Analysis》

## 问题解决与调试技巧

1. **数据类型错误**：NumPy 数组有固定的数据类型，进行不兼容的操作时会报错。
2. **广播机制问题**：NumPy 的广播规则可能导致意外结果，建议使用 `.shape` 检查数组维度。
3. **内存问题**：创建超大数组时可能耗尽内存，建议分块处理或使用生成器。

## 贡献指南

1. 提交 Issue：详细描述您发现的问题或改进建议。
2. 提交 Pull Request：按照仓库的代码规范提交您的代码改进。
