import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# start point of the circle
start_circle_center_x = -3.0
start_circle_center_y = 0.0

# 圆形的参数
circle_radius = 1.0
circle_center_x = start_circle_center_x
circle_center_y = start_circle_center_y
step_size = 0.1
total_steps = 360

# 创建一个图形和轴
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

# 创建一个圆形
circle = plt.Circle((circle_center_x, circle_center_y), circle_radius, facecolor='red', edgecolor='black')
ax.add_artist(circle)

# 创建一个圆形，用于显示起始位置
start_circle = plt.Circle((start_circle_center_x, start_circle_center_y), circle_radius, color='red', alpha=0.8)
ax.add_artist(start_circle)

# 创建一个环形，用于显示覆盖过的面积

#rectangle = plt.Rectangle((circle_center_x, circle_center_y-circle_radius+0.05), 0, circle_radius*2, color='red', alpha=0.8)
#ax.add_artist(rectangle)

# 创建一个圆形，用于显示圆形的路径
path_circle = plt.Circle((0.0, 0.0), 2.0, color='black', fill=False)
ax.add_artist(path_circle)

def update(frame):
    # 使用 sin 和 cos 函数来更新圆形的位置
    print('frame='+str(frame))
    circle_center_x = np.cos((frame+180)/180*np.pi) * 3.0
    circle_center_y = np.sin(frame/180*np.pi) * 3.0
    circle.center = (circle_center_x, circle_center_y)

    # 更新环形的位置和宽度
    #rectangle.set_width(circle_center_x - start_circle_center_x)

    return circle,

# 创建动画
ani = FuncAnimation(fig, update, frames=total_steps, interval=50, blit=True)

# 显示图形
plt.show()