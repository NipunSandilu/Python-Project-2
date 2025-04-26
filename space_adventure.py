# In class Enemy
def update(self):
    self.rect.y += self.speedy
    self.rect.x += self.speedx
    
    if (self.rect.top > SCREEN_HEIGHT + 10 or 
        self.rect.right < 0 or self.rect.left > SCREEN_WIDTH):
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

# In class Player
def update(self):
    if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
        self.hidden = False
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

    if self.power_level > 1 and pygame.time.get_ticks() - self.power_timer > 5000:
        self.power_level = 1
        self.power_timer = pygame.time.get_ticks()

    self.speed_x = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        self.speed_x = -8
    if keystate[pygame.K_RIGHT]:
        self.speed_x = 8

    self.rect.x += self.speed_x
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.left < 0:
        self.rect.left = 0

def powerup(self):
    self.power_level = min(self.power_level + 1, 2)
    self.power_timer = pygame.time.get_ticks()

# In main_game game loop
hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
for hit in hits:
    score += 100
    explosion = Explosion(hit.rect.center, 30)
    all_sprites.add(explosion)
    new_enemy = Enemy()
    all_sprites.add(new_enemy)
    enemies.add(new_enemy)
    if random.random() > 0.9:
        powerup = Powerup()
        all_sprites.add(powerup)
        powerups.add(powerup)

# Game over handling
if game_over:
    draw_text(screen, "Game Over!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False
    pygame.quit()
    sys.exit()
