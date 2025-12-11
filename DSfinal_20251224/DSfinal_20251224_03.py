import pygame
import sys
import random

pygame.init()

# 게임 화면 크기
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 추가: 게임 상태 변수
lives = 5
kill_count = 0
game_over = False

# 추가: 폰트
font = pygame.font.SysFont(None, 24)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\20251224_py\DSfinal_20251224\dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

#사과
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\20251224_py\DSfinal_20251224\apple.png")
        self.image = pygame.transform.scale(self.image,(40,40))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 2)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)

            
    
# 레이저 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# 추가: 게임 전체를 초기화하는 함수
def reset_game():
    global lives, kill_count, game_over, all_sprites, aliens, bullets, player

    lives = 3                  # 목숨 초기화
    kill_count = 0             # 점수 초기화
    game_over = False          # 게임 오버 해제

    # 스프라이트 그룹 재생성
    all_sprites.empty()
    aliens.empty()
    bullets.empty()

    # 플레이어 다시 생성
    player = Player()
    all_sprites.add(player)

    for _ in range(2):
        alien = Apple()
        all_sprites.add(alien)
        aliens.add(alien)

# 게임 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 최초 1회 초기화
reset_game()   # 추가

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ★추가: R로 게임 재시작
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: 
                reset_game()

        # 게임오버 상태에서는 입력 금지
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

    # 게임 오버가 아닐 때만 움직임/충돌 처리
    if not game_over:
        all_sprites.update()

        # 총알이 외계인 명중
        hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
        for hit in hits:
            alien = Apple()
            all_sprites.add(alien)
            aliens.add(alien)
            kill_count += 1       # 추가

        # 플레이어가 외계인에 닿음
        if pygame.sprite.spritecollide(player, aliens, False):
            lives -= 1            # 추가
            if lives <= 0:
                game_over = True  # 추가

    # ---------------- 화면 출력 ----------------
    screen.fill((170, 200, 255))

    all_sprites.draw(screen)
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    # 추가: 점수 & 목숨 UI
    ui_text = font.render(f"Kills: {kill_count}   Lives: {lives}", True, black)
    screen.blit(ui_text, (10, 10))

    # 추가: 게임오버 메시지
    if game_over:
        over_text = font.render("GAME OVER (Press R to Restart)", True, red)
        x = (WIDTH - over_text.get_width()) // 2
        y = (HEIGHT - over_text.get_height()) // 2
        screen.blit(over_text, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()