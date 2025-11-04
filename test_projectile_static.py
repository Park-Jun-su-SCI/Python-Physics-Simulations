import numpy as np
import matplotlib
matplotlib.use('Agg')  # GUI 없이 이미지 생성
import matplotlib.pyplot as plt

# 포물선 운동 매개변수
g = 9.81  # 중력 가속도 (m/s^2)
v0 = 10   # 초기 속도 (m/s)
theta = 45  # 발사 각도 (도)
theta_rad = np.radians(theta)

# 초기 속도 성분
v0x = v0 * np.cos(theta_rad)
v0y = v0 * np.sin(theta_rad)

# 시간 설정
t_max = 2 * v0y / g
t = np.linspace(0, t_max, 200)

# 포물선 운동 궤적 함수
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# 전체 궤적 플롯
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', lw=2, label='궤적')
ax.plot(x[0], y[0], 'go', markersize=10, label='시작점')
ax.plot(x[-1], y[-1], 'ro', markersize=10, label='착지점')
ax.set_xlim(0, max(x)*1.1)
ax.set_ylim(0, max(y)*1.1)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title(f'포물선 운동 궤적 (v0={v0}m/s, θ={theta}°)')
ax.set_xlabel('거리 (m)')
ax.set_ylabel('높이 (m)')

# 주요 정보 텍스트 추가
info_text = f'최대 높이: {max(y):.2f}m\n'
info_text += f'최대 거리: {max(x):.2f}m\n'
info_text += f'비행 시간: {t_max:.2f}s'
ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('projectile_trajectory.png', dpi=150)
print("정적 이미지 저장 완료: projectile_trajectory.png")
print(f"\n계산 결과:")
print(f"- 초기 속도: {v0} m/s")
print(f"- 발사 각도: {theta}°")
print(f"- 최대 높이: {max(y):.2f} m")
print(f"- 최대 거리: {max(x):.2f} m")
print(f"- 비행 시간: {t_max:.2f} s")
