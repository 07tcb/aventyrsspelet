import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Äventyrsspelet")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
text_surface = font.render("Which door would you like to choose?", False, "White")

def progress():
    with open('') as f:
        exec(f.read())


# loada dörrem
door_surfUNSCALED = pygame.image.load("graphics/door.png").convert_alpha()
door_surf = pygame.transform.scale(door_surfUNSCALED, (300, 300))

# dörr rects
door_rect1 = pygame.Rect(100, 40, 300, 300)  # Door 1
door_rect2 = pygame.Rect(400, 40, 300, 300)  # Door 2
door_rect3 = pygame.Rect(700, 40, 300, 300)  # Door 3
#loop main
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # checka musklick
            if door_rect1.collidepoint(event.pos):   
                progress()
            elif door_rect2.collidepoint(event.pos):   
                progress()
            elif door_rect3.collidepoint(event.pos):  
                progress()

    # blit dörrar
    screen.blit(door_surf, (100, 40))
    screen.blit(door_surf, (400, 40))
    screen.blit(door_surf, (700, 40))
    screen.blit(text_surface, (100, 500))

    pygame.display.update()
    clock.tick(60)
