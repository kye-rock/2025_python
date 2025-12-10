#예상 문제 2: 떨어지는 똥 피하기 (Enemy 로직)
#출제 의도: alien_game.py나 사과똥게임.py의 적 이동 로직(위에서 아래로)을 적용. 디벨롭 포인트:
#Enemy 클래스 생성 및 update 메서드에 자동 이동(rect.y += speed) 구현.
#화면 밖으로 나가면 위치 재설정(리사이클링).
#충돌 시 Game Over 상태로 전환.


import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Develop 2: Avoid Poop")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50) # 위치 하단으로 조정
        self.speed = 4
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

# [추가] 적(똥) 클래스
class Poop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\poop.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(-100, -30) # 화면 위에서 시작
        self.speed_y = random.randint(2, 6) # 랜덤 속도

    def update(self):
        self.rect.y += self.speed_y
        # 화면 아래로 벗어나면 위로 재설정 
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 30)
            self.rect.y = random.randint(-100, -30)
            self.speed_y = random.randint(2, 6)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8): # 똥 8개 생성
    poop = Poop()
    all_sprites.add(poop)
    enemies.add(poop)

running = True
game_over = False
font = pygame.font.SysFont(None, 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()
        
        # [추가] 충돌 체크 (게임 오버)
        if pygame.sprite.spritecollide(player, enemies, False):
            print("충돌!") # 
            game_over = True

    screen.fill((170, 200, 255))
    all_sprites.draw(screen)

    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()