import pygame

pygame.init()
# 추가: 사운드 믹서 초기화 (소리를 다루기 위해 필수, pygame.init()에 포함되기도 하지만 명시적으로 적어줌)
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Collision with Sound")

clock = pygame.time.Clock()

# ==========================================
# [추가] 사운드 파일 로드 영역
# 주의: 실제로 존재하는 파일 경로(.wav 또는 .ogg 추천)를 넣어야 에러가 나지 않습니다.
# ==========================================
try:
    coin_sound = pygame.mixer.Sound("이곳에 코인 효과음 파일 경로를 넣으세요.wav")
    game_over_sound = pygame.mixer.Sound("이곳에 게임오버 효과음 파일 경로를 넣으세요.wav")
except:
    print("오류: 사운드 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    # 파일이 없을 경우 빈 소리 객체를 만들어 에러 방지 (테스트용)
    class DummySound:
        def play(self): pass
    coin_sound = DummySound()
    game_over_sound = DummySound()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 이미지 경로가 없다면 주석 처리하고 아래 Surface를 사용하세요
        try:
            self.image = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
        except:
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 255)) # 파란색 네모 대체

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

        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 2

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 50 or self.rect.right > 200:
            self.speed_x *= -1

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)
all_sprites.add(enemy)
enemy_group.add(enemy)

coin_rect = pygame.Rect(430, 130, 40, 40)
score = 0

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        # 1) Rect 기반 충돌: 플레이어 vs 코인
        if player.rect.colliderect(coin_rect):
            print("코인 충돌!")
            coin_sound.play()  # [추가] 코인 획득 사운드 재생
            score += 1
            coin_rect.x = 430 if score % 2 == 0 else 350

        # 2) Sprite 그룹끼리 충돌: 플레이어 vs enemy_group
        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            print("적과 충돌! 게임 오버")
            game_over_sound.play()  # [추가] 게임오버 사운드 재생
            game_over = True

    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    pygame.draw.circle(screen,(0, 255, 0),
                       (coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2),
                       20,)

    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()