import pygame
import random

pygame.init()
pygame.mixer.init() # [추가] 사운드 믹서 초기화

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 12 - Sound Added")

clock = pygame.time.Clock() 

# ==========================================
# [추가] 사운드 파일 로드 영역
# ==========================================
try:
    apple_sound = pygame.mixer.Sound("이곳에 사과 먹는 효과음 경로를 입력하세요.wav")
    poop_sound = pygame.mixer.Sound("이곳에 똥 밟은(게임오버) 효과음 경로를 입력하세요.wav")
except:
    print("오류: 사운드 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    # 파일이 없을 경우 에러 방지용 가짜 클래스
    class DummySound:
        def play(self): pass
    apple_sound = DummySound()
    poop_sound = DummySound()


# 이미지 로드 (경로가 없으면 에러가 날 수 있으니 try-except 처리 권장하지만, 기존 코드 유지)
try:
    apple_img = pygame.image.load(r"C:\2025_python2\파이게임\apple.png")
    apple_img = pygame.transform.scale(apple_img, (40, 40))
    poop_img = pygame.image.load(r"C:\2025_python2\파이게임\poop.png")
    poop_img = pygame.transform.scale(poop_img, (40, 40))
    player_img = pygame.image.load(r"C:\2025_python2\파이게임\dukbird.png")
    player_img = pygame.transform.scale(player_img, (50, 50))
except:
    # 이미지가 없을 경우를 대비해 색상 상자로 대체 (테스트용)
    apple_img = pygame.Surface((40, 40)); apple_img.fill((255, 0, 0))
    poop_img = pygame.Surface((40, 40)); poop_img.fill((100, 50, 0))
    player_img = pygame.Surface((50, 50)); player_img.fill((0, 0, 255))


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = player_img     
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
    self.image = poop_img             
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.speed_x = 3                  
    self.speed_y = 2                  

  def update(self):
    self.rect.x += self.speed_x       
    self.rect.y += self.speed_y
    
    if self.rect.left < 0 or self.rect.right > WIDTH:
      self.speed_x *= -1
    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
      self.speed_y *= -1

all_sprites = pygame.sprite.Group()   
enemy_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)                
all_sprites.add(enemy)
enemy_group.add(enemy)

apples = []   
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30   

score = 0
running = True
game_over = False        

def spawn_apple():
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

  rect = pygame.Rect(x, y, size, size)
  apples.append({"rect": rect, "vx": vx, "vy": vy}) 


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if game_over and event.key == pygame.K_RETURN:
        game_over = False         
        score = 0                 
        player.rect.center = (WIDTH // 2, HEIGHT // 2)
        enemy.rect.topleft = (50, 260)
        enemy.speed_x = 3
        enemy.speed_y = 2
        apples.clear()
        apple_spawn_timer = 0

  if not game_over:
    all_sprites.update()  

    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_apple()

    new_apples = []
    for apple in apples:
      rect = apple["rect"]
      vx = apple["vx"]
      vy = apple["vy"]

      rect.x += vx
      rect.y += vy

      if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
        continue

      # 사과 충돌 처리
      if player.rect.colliderect(rect):
        score += 1
        apple_sound.play()  # [추가] 사과 먹는 소리 재생
        print("사과 먹음!")
        continue

      new_apples.append(apple)

    apples = new_apples

    # 똥 충돌 처리
    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
      print("똥에 닿음! 게임 오버")
      poop_sound.play()   # [추가] 똥 밟은 소리(게임오버) 재생
      game_over = True

  # ------------------ 그리기 ------------------
  screen.fill((170, 200, 255))  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60)) 

  for apple in apples:
    screen.blit(apple_img, apple["rect"])

  all_sprites.draw(screen) 

  font = pygame.font.SysFont(None, 24)
  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))

  if game_over:
    over_text = font.render("GAME OVER (Press Enter)", True, (255, 0, 0))
    over_x = (WIDTH - over_text.get_width()) // 2 
    over_y = (HEIGHT - over_text.get_height()) // 2 
    screen.blit(over_text, (over_x, over_y))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()