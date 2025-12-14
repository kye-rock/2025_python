import pygame
import random
import sys

# 1. 초기화
pygame.init()

WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("외계인 구하기")

clock = pygame.time.Clock()

# 파일 절대 경로 구현
base_path = r"C:\2025_python2\기말보고서_20251224강예은"

# 레벨업, 아이템, BGM 등 사운드 효가 추가
levelup_sound = pygame.mixer.Sound(f"{base_path}\\levelup.mp3")
item_sound = pygame.mixer.Sound(f"{base_path}\\item.mp3")
title_sound = pygame.mixer.Sound(f"{base_path}\\title.mp3")
run_sound = pygame.mixer.Sound(f"{base_path}\\run.mp3")
game_over_sound = pygame.mixer.Sound(f"{base_path}\\game_over.mp3")
success_sound = pygame.mixer.Sound(f"{base_path}\\success.mp3")

try:
    # 포인트 아이템 이미지
    item_01 = pygame.image.load(f"{base_path}\\item_01.png")
    item_01 = pygame.transform.scale(item_01, (50, 50))
    item_02 = pygame.image.load(f"{base_path}\\item_02.png")
    item_02 = pygame.transform.scale(item_02, (50, 50))

    item_list = [item_01, item_02]

    # 적 이미지
    debris_01 = pygame.image.load(f"{base_path}\\debris_01.png")
    debris_01 = pygame.transform.scale(debris_01, (80, 80))
    debris_02 = pygame.image.load(f"{base_path}\\debris_02.png")
    debris_02 = pygame.transform.scale(debris_02, (80, 80))
    debris_03 = pygame.image.load(f"{base_path}\\debris_03.png")
    debris_03 = pygame.transform.scale(debris_03, (80, 80))
    debris_04 = pygame.image.load(f"{base_path}\\debris_04.png")
    debris_04 = pygame.transform.scale(debris_04, (80, 80))
    enemy_images = [debris_01, debris_02, debris_03, debris_04]

    # 플레이어 이미지
    # 기본
    alien_idle = pygame.image.load(f"{base_path}\\alien_idle.png")
    alien_idle = pygame.transform.scale(alien_idle, (80, 80))
    # 1단계 레벨업
    alien_up = pygame.image.load(f"{base_path}\\alien_up.png")
    alien_up = pygame.transform.scale(alien_up, (80, 80))
    # 2단계 레벨업
    alien_upup = pygame.image.load(f"{base_path}\\alien_upup.png")
    alien_upup = pygame.transform.scale(alien_upup, (80, 80))


    # 배경 이미지 / 스크롤
    bg_img_raw = pygame.image.load(f"{base_path}\\back.png")
    bg_height = bg_img_raw.get_height()
    bg_width = bg_img_raw.get_width()
    new_bg_width = int(bg_width * (HEIGHT / bg_height))
    bg_img = pygame.transform.scale(bg_img_raw, (new_bg_width, HEIGHT))

    # 게임 설명, 클리어시 출력될 이미지 설정
    clear_image = pygame.image.load(f"{base_path}\\clear.png")
    story_image = pygame.image.load(f"{base_path}\\story.png")

except pygame.error as e:
    print(f"이미지 파일을 찾을 수 없습니다. : {e}")
    sys.exit()

# 배경 이미지 스크롤을 위한 변수 추가
BG_WIDTH = bg_img.get_width()
bg_x = 0
bg_speed = 2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_idle
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

        # 충돌 감지 위해 Mask 사용
        self.mask = pygame.mask.from_surface(self.image)

        # 현재 레벨 단계(기본: 0, 1단계, 2단계 존재함)
        self.current_level = 0

        # 레벨업 텍스트용 타이머
        self.levelup_timer = 0

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

        # 타이머가 켜져있으면 시간 줄이기
        if self.levelup_timer > 0:
            self.levelup_timer -= 1

        # 레벨업 처리 메서드 추가(이미지 교체, 가운드 재생, 타이머 설정)
    def level_up(self, target_level):
        if self.current_level >= target_level:
            return
        
        if target_level == 1:
            self.image = alien_up   # 1차 레벨업 이미지 교체
            print("플레이어 1차 레벨업 - 낡은 우주선\n우주 쓰레기의 속도가 빨라집니다!")
            self.levelup_timer = 120    # 레벨업시 타이머를 2초로 설정
            levelup_sound.play()

            # 1단계 클리어시 적 속도 1.3배 상승
            for enemy in enemy_group:
                enemy.speed_x *= 1.3
                enemy.speed_y *= 1.3
        
        elif target_level == 2:
            self.image = alien_upup
            print("플레이어 2차 레벨업! - 멋진 우주선\n우주 쓰레기의 속도가 더욱 빨라집니다!")
            self.levelup_timer = 120
            levelup_sound.play()

            # 2단계 클리어시 적 속도 1.5배 상승
            for enemy in enemy_group:
                enemy.speed_x *= 1.3
                enemy.speed_y *= 1.3

        # 이미지 변경시 충돌 영역 다시 만들기
        self.mask = pygame.mask.from_surface(self.image)
        self.current_level = target_level

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 3
        self.speed_y = 3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

item = []
item_spawn_timer = 0
ITEM_SPAWN_INTERVAL = 30
score = 0

def spawn_item():
    side = random.choice(["left", "right", "top", "bottom"])
    size = 40
    if side == "left":
        x = -size
        y = random.randint(0, HEIGHT - size)
        vx = random.randint(2, 4)
        vy = random.randint(-2, 2)
    elif side == "right":
        x = WIDTH
        y = random.randint(0, HEIGHT - size)
        vx = -random.randint(2, 4)
        vy = random.randint(-2, 2)
    elif side == "top":
        x = random.randint(0, WIDTH - size)
        y = -size
        vx = random.randint(-2, 2)
        vy = random.randint(2, 4)
    else:  # "bottom"
        x = random.randint(0, WIDTH - size)
        y = HEIGHT
        vx = random.randint(-2, 2)
        vy = -random.randint(2, 4)

        # 두개의 아이템 이미지 중 하나를 랜덤 선택
    chosen_image = random.choice(item_list)
    rect = pygame.Rect(x, y, size, size)
    item.append({"rect": rect, "vx": vx, "vy": vy, "img": chosen_image})

def reset_game():
    global score, item, item_spawn_timer, bg_x

    run_sound.stop()
    run_sound.play(-1)
    
    score = 0
    item = [] # 리스트 초기화
    item_spawn_timer = 0
    bg_x = 0

    all_sprites.empty()
    enemy_group.empty()

    new_player = Player()
    all_sprites.add(new_player)

    for i in range(4):  # 적 4마리 생상, 다른 이미지 순서대로 부여하는 코드
        while True:
            rand_x = random.randint(50, WIDTH - 50)
            rand_y = random.randint(50, HEIGHT - 50)
            # 플레이어와 너무 가까우면 위치 다시 정하기 = 바로 게임오버 방지하기
            if abs(rand_x - WIDTH // 2) > 150 or abs(rand_y - HEIGHT // 2) > 150:
                break
        
        assigned_image = enemy_images[i % 4]
        new_enemy = Enemy(rand_x, rand_y, assigned_image)
        
        all_sprites.add(new_enemy)
        enemy_group.add(new_enemy)
    
    return new_player

# 스토리 설명 이미지 출력을 위한 함수
def show_story_intro():
    start_ticks = pygame.time.get_ticks()   # 시간 기록(이미지 자동 꺼짐 위해)

    while True:
        current_ticks = pygame.time.get_ticks()
        elapsed_seconds = (current_ticks - start_ticks) / 1000

        # 3초가 지나면 함수 종료 (다음 화면으로 넘어감)
        if elapsed_seconds > 4.0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(story_image, (0, 0))
        pygame.display.flip()
        clock.tick(60)
 
# 게임 시작 화면 구현
def game_start():
    waiting = True
    start_font = pygame.font.SysFont(None, 40)

    title_image = pygame.image.load(f"{base_path}\\title.png")

    # 타이틀 음악 재생, (-1은 무한 반복을 의미한다)
    title_sound.play(-1)

    while waiting:
        clock.tick(60)
        
        screen.blit(title_image, (0, 0))

        start_text = start_font.render("GAME START (Press Enter)", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(start_text, start_rect)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    title_sound.stop()
                    waiting = False

# 메인 실행 + 스토리 이미지 먼저 실행 / 스토리 이미지 -> 타이틀 화면 -> 게임시작
show_story_intro()
game_start()
player = reset_game()

running = True
game_over = False
game_clear = False  # 게임 클리어 상태 변수 추가

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # 게임 클리어 상태에서도 재시작 가능하도록 추가함
        if event.type == pygame.KEYDOWN:
            if (game_over or game_clear) and event.key == pygame.K_RETURN:
                player = reset_game()
                game_over = False
                game_clear = False

            elif game_clear and event.key == pygame.K_SPACE:
                success_sound.stop()
                game_start()

                player = reset_game()
                game_clear = False

    if not game_over and not game_clear:
        all_sprites.update()
        
        if score >= 10: # 점수에따른 레벨업과 클리어 + 클리어 사운드
            game_clear = True
            run_sound.stop()
            success_sound.play()
        elif score >= 5:
            player.level_up(2)
        elif score >= 3:
            player.level_up(1)

        # 배경 스크롤 구현(계속 이동 하도록 구현 = 속도감 구현)
        bg_x -= bg_speed
        if bg_x <= -BG_WIDTH:
            bg_x = 0

        item_spawn_timer += 1
        if item_spawn_timer >= ITEM_SPAWN_INTERVAL:
            item_spawn_timer = 0
            spawn_item()

        new_items = []
        for item_n in item:
            rect = item_n["rect"]
            rect.x += item_n["vx"]
            rect.y += item_n["vy"]

            if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
                continue

            if player.rect.colliderect(rect):
                score += 1
                item_sound.play()
                continue 

            new_items.append(item_n)
        item = new_items

        # 여기도 충돌 감지 방식 collide_mask로 변경하여 체크하게 구현했음
        hits = pygame.sprite.spritecollide(player, enemy_group, False, pygame.sprite.collide_mask)
        if hits:
            print("우주 쓰레기에 닿음! 게임 오버")
            run_sound.stop()
            game_over_sound.play()
            game_over = True

    # 화면 그리기
    #배경 이미지를 두번그려서 끊김없는 스크롤 구현하기
    screen.blit(bg_img, (bg_x, 0))
    screen.blit(bg_img, (bg_x + BG_WIDTH, 0))

    for apple in item:
        screen.blit(apple["img"], apple["rect"])

    all_sprites.draw(screen)

    # 레벨업시 머리위에 텍스트로 표시하기
    if player.levelup_timer > 0:
        levelup_font = pygame.font.SysFont(None, 30)
        levelup_text = levelup_font.render("Level Up!", True, (255, 255, 0))

        text_rect = levelup_text.get_rect(center = (player.rect.centerx, player.rect.top - 5))
        screen.blit(levelup_text, text_rect)

    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        over_font = pygame.font.SysFont(None, 60)
        over_text = over_font.render("GAME OVER (Press Enter)", True, (255, 81, 54))
        over_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        f_score_font = pygame.font.SysFont(None, 40)
        f_score_text = f_score_font.render(f"SCORE : {score}", True, (255, 81, 54))
        f_score_rect = f_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.blit(over_text, over_rect)
        screen.blit(f_score_text, f_score_rect)

        #게임 클리어 화면
    elif game_clear:
        screen.blit(clear_image, (0, 0))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()