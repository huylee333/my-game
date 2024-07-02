import pygame
import sys
import random
import webbrowser

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Đối tượng người chơi (bóng)
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height - 2 * ball_radius
ball_speed = 5

# Đối tượng chổi
broom_width = 150
broom_height = 20
broom_x = screen_width // 2 - broom_width // 2
broom_y = screen_height - broom_height - 10
broom_speed = 10
broom_vertical_speed = 5

# Đối tượng điểm
score = 0
font = pygame.font.Font(None, 36)

# Hàm vẽ điểm số lên màn hình
def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Hàm vẽ đối tượng bóng và chổi
def draw_objects():
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, WHITE, (broom_x, broom_y, broom_width, broom_height))

# Hàm cập nhật vị trí của các đối tượng
def update_objects():
    global ball_y, score, broom_y, broom_x, ball_x  # Thêm ball_x vào global để có thể thay đổi giá trị global
    
    ball_y -= ball_speed
    
    # Nếu bóng chạm vào đỉnh chổi, tăng điểm và đặt lại vị trí bóng
    if ball_y <= broom_y + broom_height and broom_x <= ball_x <= broom_x + broom_width:
        score += 1
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        ball_y = screen_height - 2 * ball_radius
    
    # Nếu bóng rơi xuống dưới màn hình, đặt lại vị trí bóng
    if ball_y <= 0:
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        ball_y = screen_height - 2 * ball_radius
    
    # Xử lý điều khiển thanh chổi lên, xuống, sang trái và sang phải
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        broom_y -= broom_vertical_speed
    if keys[pygame.K_DOWN]:
        broom_y += broom_vertical_speed
    if keys[pygame.K_LEFT]:
        broom_x -= broom_speed
    if keys[pygame.K_RIGHT]:
        broom_x += broom_speed

# Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Giới hạn vị trí chổi trong màn hình
    if broom_y < 0:
        broom_y = 0
    elif broom_y > screen_height - broom_height:
        broom_y = screen_height - broom_height
    if broom_x < 0:
        broom_x = 0
    elif broom_x > screen_width - broom_width:
        broom_x = screen_width - broom_width
    
    # Cập nhật vị trí các đối tượng và vẽ lên màn hình
    screen.fill(BLACK)
    draw_objects()
    draw_score()
    update_objects()
    
    # Kiểm tra điều kiện chiến thắng
    if score >= 20:
        font_win = pygame.font.Font(None, 72)
        text_win = font_win.render("You Win!", True, WHITE)
        screen.blit(text_win, (screen_width // 2 - text_win.get_width() // 2, screen_height // 2 - text_win.get_height() // 2))
        
        # Vẽ link "Play Again"
        font_link = pygame.font.Font(None, 36)
        text_link = font_link.render("An Zo day nhoe", True, WHITE)
        text_rect = text_link.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(text_link, text_rect)
        
        # Xử lý sự kiện click vào link "Play Again"
        mouse_pos = pygame.mouse.get_pos()
        if text_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            # Mở trang web khi click vào link
            webbrowser.open("https://phamvulinh18.github.io/crush4/?fbclid=IwZXh0bgNhZW0CMTAAAR1YOP0TVzZmZ7T02Js1U6eeJDmrNIJgHQ9fHMKSjROb760o1fNYo1zI4e8_aem_cMXHeE8IQI7vS-XW4v84tQ")  # Thay đổi link của trang web cần mở
        
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình
    pygame.time.Clock().tick(60)

# Kết thúc Pygame
pygame.quit()
sys.exit()