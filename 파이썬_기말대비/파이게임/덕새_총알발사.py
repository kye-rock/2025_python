#출제 의도: alien_game.py의 핵심 기능인 총알 발사(Bullet 클래스) 구현 능력 평가. 
# 디벨롭 포인트:
#Bullet 클래스 추가 (위로 이동).
#Player 클래스 내 shoot 메서드 또는 이벤트 루프에서 총알 생성.
#groupcollide를 사용하여 적과 총알이 닿으면 둘 다 삭제(또는 적 재생성).


import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Develop 3: Shooting")
clock = pygame.time.Clock()

# [추가] 총알 클래스 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15)) # 간단한 네모 총알 
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -7 # 위로 이동

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill() # 화면 밖으로 나가면 삭제

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

    # [추가] 발사 기능
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\alien.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(-100, -30)
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 30)
            self.rect.y = random.randint(-100, -30)

all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    alien = Enemy()
    all_sprites.add(alien)
    aliens.add(alien)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # [추가] 스페이스바로 발사 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # [추가] 총알과 적 충돌 (둘 다 사라짐: True, True) 
    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    for hit in hits:
        # 적이 죽으면 새로 생성 (게임 유지 위해)
        e = Enemy()
        all_sprites.add(e)
        aliens.add(e)

    screen.fill((0, 0, 0)) # 우주 배경
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()