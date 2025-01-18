import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Boss Battle")
clock = pygame.time.Clock()

# Image load
pov_img = pygame.image.load("graphics/swordpov.png")
pov_img = pygame.transform.scale(pov_img, (900, 800))
bg_boss = pygame.image.load("graphics/bg_boss.jpg")
bg_boss = pygame.transform.scale(bg_boss, (1100, 800))
boss_img = pygame.image.load("graphics/endboss.gif")
boss_img = pygame.transform.scale(boss_img, (400, 500))

# Font
font = pygame.font.Font(None, 36)

# health
player_health = 100
boss_health = 200

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

       #exempel demo grej för o se om det funkar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # p för damage till player
                player_health -= 10
                if player_health < 0:
                    player_health = 0
            if event.key == pygame.K_b:  #B för damage till bossen
                boss_health -= 20
                if boss_health < 0:
                    boss_health = 0  # Prevent negative health

    # Screen refresh
    screen.fill((0, 0, 0))  # Placeholder

    # Blit
    screen.blit(bg_boss, (0, 0))
    screen.blit(pov_img, (200, 0))
    if boss_health > 0:  # visa bara bossen om den lever
        screen.blit(boss_img, (350, 50))

    # Render
    player_health_text = font.render(f"Player Health: {player_health}", True, "White")
    boss_health_text = font.render(f"Boss Health: {boss_health}", True, "White")
    screen.blit(player_health_text, (20, 20))
    screen.blit(boss_health_text, (20, 60))

    # Update
    pygame.display.update()
    clock.tick(60)
