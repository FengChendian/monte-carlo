# _*_ coding: utf-8 _*_

%matplotlib inline

import random
import time
import warnings
import math
import numpy as np
import matplotlib.pyplot as plt

warnings.simplefilter('ignore', np.RankWarning)

# 必要物理参数定义
T_0 = 0.5
Delta_T = 0.1
K = 1.0
J = 1.0

# 步长
feet = 1000
# 箭头宽度
wide = 0.4
# 箭头坐标调整
ajust = 4.5 * wide + 4
# 正方形点阵边长——单位长度表示一个自旋
side_length = 4

# 自旋数量
L = side_length * side_length
# 坐标轴最大值(不要更改)
axis_len = side_length * 10

# 能量坐标
E = []
Tem = []

# 初始化
random.seed(time.time())
state = np.empty((side_length, side_length))
for i in range(side_length):
    for j in range(side_length):
        state[i][j] = random.choice([4, -4])


def judge(state, Beta):
    random.seed(time.time())
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
    horizon = (state[(i - 1) % side_length][j] + state[(i + 1) % side_length][j])
    vertical = (state[i][(j - 1) % side_length] + state[i][(j + 1) % side_length])
    H = -J * (horizon + vertical)
    return H

def energy(state):
    H_0 = 0
    for i in range(side_length):
        for j in range(side_length):
            horizon = (state[(i - 1) % side_length][j] + state[(i + 1) % side_length][j])
            vertical = (state[i][(j - 1) % side_length] + state[i][(j + 1) % side_length])
            H_0 += -J * (horizon + vertical)

    return H_0            
# 生成画布
plt.figure(num=1, figsize=(20, 40), dpi=100)
# 打开交互模式
# plt.ion()
for times in range(45):
    T = T_0 + times * Delta_T

    # 温度坐标
    Tem.append(T)

    Beta = 1 / (T * K)
    # 循环
    for index in range(feet):
#         # 清除原有图像
#         plt.subplot(121)
#         plt.cla()

#         # 绘制恰当的坐标轴
#         plt.xlim(-10, axis_len)
#         plt.ylim(-5, axis_len)

        # 改变自旋
        judge(state, Beta)

#         # 绘图
#         for i in range(side_length):
#             for j in range(side_length):
#                 if state[i][j] == -4:
#                     plt.arrow(i * 10, j * 10 + ajust, 0, state[i][j], width=wide, color='black')
#                 else:
#                     plt.arrow(i * 10, j * 10, 0, state[i][j], width=wide, color='black')
#         # 暂停
#         plt.pause(0.0001)
    
    # 能量参数
    E_0 = energy(state)
    E.append(0.5 * E_0 / L)

    

# # 关闭交互模式
# plt.ioff()
# 最终图形显示

# 曲线拟合
fp2 = np.polyfit(Tem, E, 3)
f2 = np.poly1d(fp2)
fx = np.linspace(0,Tem[-1],1000)
plt.subplot(122)
# 设置横坐标最小值
plt.xlim(left=0.5, right=5)

plt.xlabel('T')
plt.ylabel('E')
plt.plot(fx,f2(fx),'g', Tem, E, "r*")
plt.pause(0.05)

plt.show()
