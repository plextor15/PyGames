import pygame
from sys import exit
import getpass

if __name__ == '__main__':
    pygame.init()

    #Game properties
    pygame.display.set_caption('Pierwsza Gra')
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    #Warstwy
    #DEBUG
    test_surface = pygame.Surface((200,200))
    test_surface.fill('blue')

    #Background
    background = pygame.image.load('graphic/background/BG.png').convert_alpha()

    #Ground
#    ground01 = pygame.image.load('graphic/ground/1.png')
#    ground02 = pygame.image.load('graphic/ground/2.png')
#    ground03 = pygame.image.load('graphic/ground/3.png')
    ground = pygame.image.load('graphic/ground/ground.png').convert_alpha()
    
    #Teksty
    game_font = pygame.font.Font('graphic/font/my_font.ttf', 100) #default - (None, 60)
    text_surface = game_font.render(f"{getpass.getuser()} Witaj!", True, 'Red')

    #PCs
    #Player
    player = pygame.image.load('graphic/characters/player/adventurer_walk1.png').convert_alpha()
    player_rect = player.get_rect(topleft = (100, 430))

    #NPCs
    #Zombie
    zombie = pygame.image.load('graphic/characters/zombie/zombie_walk1.png').convert_alpha()
    #zombie_x_pos = 700
    zombie_rect = player.get_rect(topleft = (700, 430))

    #Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      #zeby byl exit code 0

        #chodzenie zombiaka w lewo
        zombie_rect.x -= 2
        if zombie_rect.x <= -100:
            zombie_rect.x = 1000

        #screen.blit(test_surface, (10,10))
        screen.blit(background, (0,0))
        screen.blit(ground, (0,540))
        screen.blit(text_surface, (300,100))

        screen.blit(player, player_rect)
        screen.blit(zombie, zombie_rect)

        pygame.display.update()
        clock.tick(50)      #FPSy
