# _*_ coding: utf-8 _*_

import random
import math
import numpy as np
import matplotlib.pyplot as plt

# 必要物理参数定义
T = 1.5
K = 1.0
J = 1.0
Beta = 1 / (T * K)
# 步长
feet = 1000
# 箭头宽度
wide = 0.4
# 箭头坐标调整
ajust = 4.5 * wide + 4
# 正方形点阵边长——每单位长度上存在一个自旋
side_length = 10

# 坐标轴最大值(不要更改)
axis_len = side_length * 10

# 初始化
state = np.empty((side_length, side_length))
for i in range(side_length):
    for j in range(side_length):
        state[i][j] = random.choice([4, -4])


def judge(state):
    i = random.randint(0, side_length - 1)
    j = random.randint(0, side_length - 1)
    H_1 = calculate(state, i, j, 1)
    H_2 = calculate(state, i, j, -1)
    if H_2 - H_1 < 0:
        state[i][j] *= -1
    else:
        A = math.exp(-Beta * (H_2 - H_1))
        if random.random() <= A:
            state[i][j] *= -1
        else:
            pass


def calculate(state, i, j, real):
    horizon = -J * (state[(i - 1) % side_length][j] + state[(i + 1) % side_length][j])
    vertical = -J * (state[i][(j - 1) % side_length] + state[i][(j + 1) % side_length])
    H = horizon + vertical
    return H


# 生成画布
plt.figure(figsize=(15, 15), dpi=100)

# 打开交互模式
plt.ion()

# 循环
for index in range(feet):
    # 清除原有图像
    plt.cla()

    # 绘制恰当的坐标轴
    plt.xlim(-10, axis_len)
    plt.ylim(-5, axis_len)

    # 改变自旋
    judge(state)

    # 绘图
    for i in range(side_length):
        for j in range(side_length):
            if state[i][j] == -4:
                plt.arrow(i * 10, j * 10 + ajust, 0, state[i][j], width=wide, color='black')
            else:
                plt.arrow(i * 10, j * 10, 0, state[i][j], width=wide, color='black')
    
    # 暂停
    plt.pause(0.05)
# 关闭交互模式
plt.ioff()
# 最终图形显示
plt.show()
