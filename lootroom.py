import pygame
from sys import exit

# Initialize
pygame.init()

# Screen settings
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Armory")
clock = pygame.time.Clock()

Inv=[]
def progress():
    with open('boss.py') as f:
        exec(f.read())

# character image
character_img = pygame.image.load("graphics/oldman.png").convert_alpha()
character_img = pygame.transform.scale(character_img, (100, 120))
bg_img = pygame.image.load("graphics/bg.png")
bg_img = pygame.transform.scale(bg_img, (1100, 900))
armor_img = pygame.image.load("graphics/helm.png")
armor_img = pygame.transform.scale(armor_img, (200, 300))
sword_img = pygame.image.load("graphics/sword.png")
sword_img = pygame.transform.scale(sword_img, (350, 300))

# Font
font = pygame.font.Font(None, 37)
text1 = "Place hasn't collapsed after all these years, incredible..."
text2 = "Pick 1 profession, each one helps you in a different way."
text_armor = "+50HP"
text_sword = "+20DMG"
text_surface1 = font.render(text1, True, "Black", "Gray")
text_surface2 = font.render(text2, True, "Black", "Gray")
text_surf_sword = font.render(text_sword, True, "Black", "Gray")
text_surf_armor = font.render(text_armor, True, "Black", "Gray")


text_rect = pygame.Rect(100, 650, 900, 100)


armor_rect = pygame.Rect(100, 200, 200, 300)  # Armor image clickable area (bör funka nu?)
sword_rect = pygame.Rect(400, 200, 350, 300)  # Sword image clickable area

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # checka event (om musen tryckts)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if armor_rect.collidepoint(event.pos): 
                Inv.append("armor")
                print (f"Here is your loadout:{Inv}")
                progress()
            elif sword_rect.collidepoint(event.pos):  
                Inv.append("sword")
                print (f"Here is your loadout:{Inv}")
                progress()
                
    # Screen refresh
    screen.blit(bg_img, (0, 0))

    # char img
    screen.blit(character_img, (150, 640))


    pygame.draw.rect(screen, (0, 0, 0), text_rect, 2)  #border brevid boxen
    screen.blit(text_surface1, (300, 670)) 
    screen.blit(text_surface2, (300, 700))  

    #loot rita
    screen.blit(armor_img, (100, 200))
    screen.blit(text_surf_armor, (160, 100)) 

    screen.blit(sword_img, (400, 200))
    screen.blit(text_surf_sword, (500, 100)) 

    # Update
    pygame.display.update()
    clock.tick(60)
