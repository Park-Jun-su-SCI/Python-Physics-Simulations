import numpy as np
import matplotlib
matplotlib.use('Agg')  # GUI 없이 이미지 생성
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# 포물선 운동 매개변수
g = 9.81  # 중력 가속도 (m/s^2)
v0 = 10   # 초기 속도 (m/s)
theta = 45  # 발사 각도 (도)
theta = np.radians(theta)

# 초기 속도 성분
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# 시간 설정
t_max = 2 * v0y / g
t = np.linspace(0, t_max, 200)

# 포물선 운동 궤적 함수
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# 애니메이션 생성
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, max(x)*1.1)
ax.set_ylim(0, max(y)*1.1)
ax.grid(True, alpha=0.3)
line, = ax.plot([], [], 'b-', lw=2, label='Trajectory')
point, = ax.plot([], [], 'ro', markersize=10, label='Projectile')
ax.legend()

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data([x[frame]], [y[frame]])  # 배열로 감싸기
    return line, point

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

plt.title('Projectile Motion Animation (v0=10m/s, angle=45deg)')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')

# GIF로 저장
print("애니메이션 생성 중... (약 10-20초 소요)")
ani.save('projectile_animation.gif', writer=PillowWriter(fps=30))
print("애니메이션 저장 완료: projectile_animation.gif")
