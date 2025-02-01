import pygame
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 设置字体
font = pygame.font.Font(None, 36)

# 设置挡板
paddle_width = 100
paddle_height = 20
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10
paddle_speed = 10

# 设置球
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = 5
ball_speed_y = -5

# 设置砖块
brick_width = 75
brick_height = 20
brick_rows = 5
brick_cols = screen_width // brick_width
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# 设置分数
score = 0

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动挡板
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # 移动球
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 球与墙的碰撞检测
    if ball_x <= 0 or ball_x >= screen_width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 球与挡板的碰撞检测
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y < paddle_y + paddle_height):
        ball_speed_y = -ball_speed_y

    # 球与砖块的碰撞检测
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            score += 1  # 每打一个砖块加1分
            break

    # 球掉出屏幕
    if ball_y >= screen_height:
        running = False

    # 清屏
    screen.fill(BLACK)

    # 绘制挡板
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 绘制球
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # 绘制砖块
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # 显示分数
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()