% 포물선 운동 매개변수 설정
g = 9.81; % 중력가속도 (m/s^2)
v0 = 10; % 초기 속도 (m/s)
theta = 45; % 발사 각도 (deg)
theta = deg2rad(theta); % 라디안 변환

% 초기 속도 성분 분해
v0x = v0 * cos(theta);
v0y = v0 * sin(theta);

% 최대 비행 시간
t_max = 2 * v0y / g;

% 시간 벡터 생성
t = linspace(0, t_max, 200);

% 포물선 좌표 계산
x = v0x .* t;
y = v0y .* t - 0.5 * g .* t.^2;

% 그래프 창 설정
figure;
axis([0 max(x)*1.1 0 max(y)*1.1]);
xlabel('거리 (m)');
ylabel('높이 (m)');
title('포물선 운동 애니메이션');

% 애니메이션 실행
for i=1:length(t)
    plot(x(1:i), y(1:i), 'b-', 'LineWidth', 2);
    hold on;
    plot(x(i), y(i), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
    hold off;
    pause(0.02);
end
