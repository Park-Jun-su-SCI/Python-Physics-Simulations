"""
MATLAB 코드를 Python으로 변환한 버전
원본 MATLAB 코드와 동일한 동작을 수행합니다.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# 포물선 운동 매개변수 설정
g = 9.81  # 중력가속도 (m/s^2)
v0 = 10   # 초기 속도 (m/s)
theta = 45  # 발사 각도 (deg)
theta = np.deg2rad(theta)  # 라디안 변환

# 초기 속도 성분 분해
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# 최대 비행 시간
t_max = 2 * v0y / g

# 시간 벡터 생성
t = np.linspace(0, t_max, 200)

# 포물선 좌표 계산
x = v0x * t
y = v0y * t - 0.5 * g * t**2

print("=" * 60)
print("MATLAB 코드 실행 결과")
print("=" * 60)
print(f"\n매개변수:")
print(f"  - 중력가속도 (g): {g} m/s²")
print(f"  - 초기 속도 (v0): {v0} m/s")
print(f"  - 발사 각도: 45°")
print(f"\n계산 결과:")
print(f"  - 초기 속도 x 성분 (v0x): {v0x:.3f} m/s")
print(f"  - 초기 속도 y 성분 (v0y): {v0y:.3f} m/s")
print(f"  - 최대 비행 시간 (t_max): {t_max:.3f} s")
print(f"  - 최대 높이: {np.max(y):.3f} m")
print(f"  - 최대 거리: {np.max(x):.3f} m")
print(f"  - 시간 포인트 수: {len(t)}")

# 정적 이미지 생성 (전체 궤적)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label='Trajectory')
ax.plot(x[0], y[0], 'go', markersize=10, label='Start')
ax.plot(x[-1], y[-1], 'ro', markersize=10, label='End')
ax.set_xlim([0, np.max(x)*1.1])
ax.set_ylim([0, np.max(y)*1.1])
ax.set_xlabel('거리 (m)')
ax.set_ylabel('높이 (m)')
ax.set_title('포물선 운동 애니메이션')
ax.grid(True, alpha=0.3)
ax.legend()

# 정보 박스 추가
info_text = f'Max Height: {np.max(y):.2f}m\n'
info_text += f'Max Range: {np.max(x):.2f}m\n'
info_text += f'Flight Time: {t_max:.2f}s'
ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('matlab_projectile_static.png', dpi=150)
print(f"\n정적 이미지 저장: matlab_projectile_static.png")

# 애니메이션 생성 (MATLAB의 for 루프와 동일한 동작)
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.set_xlim([0, np.max(x)*1.1])
ax2.set_ylim([0, np.max(y)*1.1])
ax2.set_xlabel('거리 (m)')
ax2.set_ylabel('높이 (m)')
ax2.set_title('포물선 운동 애니메이션')
ax2.grid(True, alpha=0.3)

line, = ax2.plot([], [], 'b-', linewidth=2)
point, = ax2.plot([], [], 'ro', markersize=8, markerfacecolor='r')

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(i):
    # MATLAB: plot(x(1:i), y(1:i), 'b-', 'LineWidth', 2);
    line.set_data(x[:i+1], y[:i+1])
    # MATLAB: plot(x(i), y(i), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
    point.set_data([x[i]], [y[i]])
    return line, point

print("\n애니메이션 생성 중... (약 10-20초 소요)")
ani = FuncAnimation(fig2, update, frames=len(t), init_func=init,
                    blit=True, interval=20)  # MATLAB의 pause(0.02)와 동일

# GIF로 저장
ani.save('matlab_projectile_animation.gif', writer=PillowWriter(fps=50))
print("애니메이션 저장: matlab_projectile_animation.gif")

print("\n" + "=" * 60)
print("실행 완료!")
print("=" * 60)
print("\n생성된 파일:")
print("  1. matlab_projectile_static.png - 전체 궤적")
print("  2. matlab_projectile_animation.gif - 애니메이션")
