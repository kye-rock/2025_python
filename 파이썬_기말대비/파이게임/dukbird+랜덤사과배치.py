import pygame
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Develop 1: Random Items")
clock = pygame.time.Clock()

# 플레이어 클래스 (dukbird_9 유지)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

# [추가] 아이템 클래스 정의
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\apple.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # 랜덤 위치 설정 
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)

# 그룹 생성
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group() # [추가] 아이템 관리 그룹

player = Player()
all_sprites.add(player)

# [추가] 아이템 5개 생성
for _ in range(5):
    apple = Apple()
    all_sprites.add(apple)
    items.add(apple)

score = 0
font = pygame.font.SysFont(None, 30)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # [추가] 충돌 처리 (플레이어가 아이템을 먹음) 
    hits = pygame.sprite.spritecollide(player, items, True) # True면 아이템 삭제
    for hit in hits:
        score += 1
        # 먹으면 다시 새로운 사과 생성 (무한 리필)
        new_apple = Apple()
        all_sprites.add(new_apple)
        items.add(new_apple)

    screen.fill((170, 200, 255))
    all_sprites.draw(screen)
    
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()