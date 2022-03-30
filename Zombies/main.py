import pygame
from sys import exit
import getpass

from pygame import mouse
from pygame import key

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
    #

    #Background
    background = pygame.image.load('graphic/background/BG.png').convert_alpha()

    #Ground

    ground = pygame.image.load('graphic/ground/ground.png').convert_alpha()
    
    #Teksty
    game_font = pygame.font.Font('graphic/font/my_font.ttf', 100) #default - (None, 60)
    
    #Welcome
    text = game_font.render(f"{getpass.getuser()} Witaj!", True, 'Black')
    text_rect = text.get_rect(topleft=(300,30))

    #Score
    score_text = game_font.render("My score:", False, 'Black')
    score_text_rect = score_text.get_rect(topleft=(330,100))

    #PCs
    #Player
    player = pygame.image.load('graphic/characters/player/adventurer_walk1.png').convert_alpha()
    player_rect = player.get_rect(topleft = (100, 430))

    #NPCs
    #Zombie
    zombie = pygame.image.load('graphic/characters/zombie/zombie_walk1.png').convert_alpha()
    #zombie_x_pos = 700
    zombie_rect = player.get_rect(topleft = (700, 430))


    player_gravity = 0  #trzeba poprawic grawitacje

    #Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      #zeby byl exit code 0
            
            if event.type == pygame.MOUSEMOTION:
                print( event.pos )
                if player_rect.collidepoint( event.pos ):
                    print("collide")
            
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.y == 430: # and player_gravity == 0:
                #print( "Down" )
                player_gravity = -20    #jump
            if event.type == pygame.MOUSEBUTTONUP:
                #print( "Up" )
                pass    #zeby zblowalo double jump


            if event.type == pygame.KEYDOWN:
                #print("Key Down")
                if event.key == pygame.K_SPACE:
                    #print("Space")
                    player_gravity = -20
                if event.key == pygame.K_PAGEUP:
                    print("PageUp")
            if event.type == pygame.KEYUP:
                print("Key Up")


        #chodzenie zombiaka w lewo
        zombie_rect.x -= 2
        if zombie_rect.x <= -100:
            zombie_rect.x = 1000

        #screen.blit(test_surface, (10,10))
        screen.blit(background, (0,0))
        screen.blit(ground, (0,540))


        pygame.draw.rect( screen, '#c0e8ec', text_rect, 0, 10 )
        screen.blit(text, text_rect)
        pygame.draw.rect( screen, '#c0e8ec', score_text_rect, 0, 10 )
        screen.blit(score_text, score_text_rect)


        screen.blit(player, player_rect)
        screen.blit(zombie, zombie_rect)




        #Kolizje

        #DEBUG ONLY
        #print( player_rect.colliderect( zombie_rect ) )
        #print( pygame.mouse.get_pos() )
        
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint( mouse_pos ):
            #print("LOLXD")
            #print( pygame.mouse.get_pressed() )
        
        keys = pygame.key.get_pressed()
        if keys[ pygame.K_SPACE ]:
            print( "Jump" )
        if keys[ pygame.K_F1 ]:
            print( "F1" )
        

        pygame.display.update() ############# UPDATE #############


        player_gravity += 1 #kiedys sie przepelni bufor
        player_rect.y += player_gravity

        if player_rect.y >= 430: player_rect.y = 430


        clock.tick(50)      #FPSy
