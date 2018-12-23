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

# 初始化
state = np.empty((5, 5))
for i in range(5):
    for j in range(5):
        state[i][j] = random.choice([4, -4])


def judge(state):
    i = random.randint(0, 4)
    j = random.randint(0, 4)
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
    horizon = -J * (state[(i - 1) % 5][j] + state[(i + 1) % 5][j])
    vertical = -J * (state[i][(j - 1) % 5] + state[i][(j + 1) % 5])
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
    plt.xlim(-10, 50)
    plt.ylim(-5, 50)

    # 改变自旋
    judge(state)

    # 绘图
    for i in range(5):
        for j in range(5):
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
