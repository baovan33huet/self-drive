import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Đường dẫn đến hình ảnh của bạn
image_path = "resized_map4.png"
image = pygame.image.load(image_path)

# Kích thước cửa sổ phù hợp với kích thước của ảnh
screen = pygame.display.set_mode(image.get_size())
pygame.display.set_caption("Click to get coordinates")

# Vòng lặp sự kiện
running = True
while running:
    # Hiển thị hình ảnh
    screen.blit(image, (0, 0))
    pygame.display.flip()
    
    # Lắng nghe sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Lấy tọa độ của vị trí nhấp chuột
            x, y = pygame.mouse.get_pos()
            print(f"Coordinates: ({x}, {y})")

# Thoát khỏi Pygame
pygame.quit()
sys.exit()
