import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# start point of the circle
start_circle_center_x = 0.0
start_circle_center_y = 0.0

# 圆形的参数
circle_radius = 1.0
circle_center_x = 0.0
circle_center_y = 0.0
step_size = 0.1
total_steps = 100

# 创建一个图形和轴
fig, ax = plt.subplots()
ax.set_xlim(-5, 20)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# 创建一个圆形
circle = plt.Circle((circle_center_x, circle_center_y), circle_radius, facecolor='red', edgecolor='black')
ax.add_artist(circle)

# 创建一个圆形，用于显示起始位置
start_circle = plt.Circle((start_circle_center_x, start_circle_center_y), circle_radius, color='red', alpha=0.8)
ax.add_artist(start_circle)

# 创建一个矩形，用于显示覆盖过的面积
rectangle = plt.Rectangle((circle_center_x, circle_center_y-circle_radius+0.05), 0, circle_radius*2, color='red', alpha=0.8)
ax.add_artist(rectangle)

# 创建一条直线，用于显示圆形的路径
line, = ax.plot([-4, 14], [-1, -1], color='blue')

def update(frame):
    # 更新圆形的位置
    circle_center_x = frame * step_size
    circle.center = (circle_center_x, circle_center_y)

    # 更新矩形的位置和宽度
    rectangle.set_width(circle_center_x - start_circle_center_x)

    # 计算覆盖过的面积
    S = np.pi * circle_radius * circle_radius
    r_str = str(circle_radius)
    S_str = str(S)
    S_covered = str(S+rectangle.get_width()*rectangle.get_height())
    print('S_covered='+S_covered)

    #ax.set_title(f'r='+r_str+'\nS_circle=pi X '+r_str+' X '+r_str+'='+S_str+'\nS_covered='+S_covered)

    return rectangle,circle

# 创建动画
ani = FuncAnimation(fig, update, frames=total_steps, interval=50, blit=True)

# 显示图形
plt.show()