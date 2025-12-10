import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Develop 4: Multi-direction Spawn")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
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

# [추가] 사방팔방 적 클래스 
class RandomEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\2025_python2\파이게임\poop.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        
        # 사방팔방 생성 로직
        side = random.choice(["left", "right", "top", "bottom"])
        if side == "left":
            self.rect.x = -30
            self.rect.y = random.randint(0, HEIGHT)
            self.vx = random.randint(2, 4)
            self.vy = random.randint(-2, 2)
        elif side == "right":
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.vx = -random.randint(2, 4)
            self.vy = random.randint(-2, 2)
        elif side == "top":
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = -30
            self.vx = random.randint(-2, 2)
            self.vy = random.randint(2, 4)
        else: # bottom
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = HEIGHT
            self.vx = random.randint(-2, 2)
            self.vy = -random.randint(2, 4)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # 화면 밖으로 멀리 나가면 삭제
        if not screen.get_rect().colliderect(self.rect):
             self.kill()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 적 생성 타이머
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 500) # 0.5초마다 생성

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # [추가] 타이머 이벤트로 적 생성
        if event.type == SPAWN_EVENT:
            e = RandomEnemy()
            all_sprites.add(e)
            enemies.add(e)

    all_sprites.update()
    
    # 충돌 체크
    if pygame.sprite.spritecollide(player, enemies, False):
        print("충돌!") 

    screen.fill((170, 200, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()