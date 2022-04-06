import pygame
from sys import exit
import getpass


def display_score():
    current_time = int( pygame.time.get_ticks() / 1000 ) - start_time

    score_text = game_font.render(f"My scores: {current_time}", False, 'Black')
    score_text_rect = score_text.get_rect(topleft=(380, 100))
    pygame.draw.rect(screen, '#c0e8ec', score_text_rect, 0, 10)
    screen.blit(score_text, score_text_rect)

    return current_time


if __name__ == '__main__':

    # Inicjalizacja wszystkich komponentow gry
    pygame.init()

    screen = pygame.display.set_mode((1000, 750))
    clock = pygame.time.Clock()

    # Nadanie nowej nazwy okna gry
    pygame.display.set_caption('Zombie Runner')

    # Czcionka gry
    game_font = pygame.font.Font('graphic/font/my_font.ttf', 60)

    # Dodanie background-u
    background = pygame.image.load('graphic/background/BG.png').convert_alpha()

    # Dodanie elementow podlogi
    ground = pygame.image.load('graphic/ground/ground.png').convert_alpha()

    # Dodanie tekstu
    text = game_font.render(f"{getpass.getuser()} ! Witaj w grze !", False, 'Black')
    text_rect = text.get_rect(topleft=(300, 30))


    intro_text = game_font.render("Press S to Start", True, "Black")
    intro_text_rect = intro_text.get_rect(topleft=(350, 600))

    intro_title = game_font.render("Zombie Runner", True, "Black")
    intro_title_rect = intro_title.get_rect(topleft=(370, 200))

    intro_game_over = game_font.render("Game Over!", True, "Black")
    intro_game_over_rect = intro_game_over.get_rect(topleft=(390, 300))


    # Dodanie Zombie do gry
    zombie = pygame.image.load('graphic/characters/zombie/zombie_walk1.png').convert_alpha()
    # Dodanie obszaru zombie
    zombie_rect = zombie.get_rect(topleft=(700, 430))

    # Dodanie gracza do gry
    player = pygame.image.load('graphic/characters/player/adventurer_walk1.png').convert_alpha()
    # Dodanie obszaru gracza
    player_rect = player.get_rect(topleft=(100, 430))

    player_gravity = 25


    game_is_active = False
    game_over = False
    start_time = 0
    score = 0


    # Main Loop
    while True:
        # Obsluga wyjatkow
        for event in pygame.event.get():
            # Obsluga wcisiecia X
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_is_active:

                if event.type == pygame.MOUSEBUTTONDOWN and player_rect.y == 430:
                    player_gravity = -25


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.y == 430:
                        player_gravity = -25
                     
                        
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    game_is_active = True

                    # pozycjonowanie
                    zombie_rect.topleft = (700, 430)
                    player_rect.topleft = (100, 430)
                    player_gravity = 25



        if game_is_active:
            # Ruch Zombie
            zombie_rect.x -= 5
            if zombie_rect.x <= -100:
                zombie_rect.x = 1100

            # Dodanie backgroundu do okna gry
            screen.blit(background, (0, 0))
            # Dodanie elementow podlogi do okna gry
            screen.blit(ground, (0, 540))

            pygame.draw.rect(screen, '#c0e8ec', text_rect, 0, 10)
            # Dodanie tekstu do okna gry
            screen.blit(text, text_rect)

            score = display_score()
            
            # Dodanie zombie do okna gry
            screen.blit(zombie, zombie_rect)
            # Dodanie gracza do ekranu gry
            screen.blit(player, player_rect)



            #pygame.display.update() ############# UPDATE #############

            

            if player_rect.y < 430:
                player_gravity += 1

            player_rect.y += player_gravity
        
            #DEBUG ONLY!!
            #print(player_gravity)

            if player_rect.y >= 430: player_rect.y = 430

            if player_rect.colliderect(zombie_rect):
                game_is_active = False
                game_over = True

                start_time = int( pygame.time.get_ticks() / 1000 )
            
            #clock.tick(50)      #FPSy
        else:
            screen.fill("#c0e8ec")
            screen.blit(intro_text, intro_text_rect)
            screen.blit(intro_title, intro_title_rect)
            if game_over:
                screen.blit( intro_game_over, intro_game_over_rect )

                intro_score = game_font.render( f"Score: {score}", True, "Black" )
                intro_score_rect = intro_score.get_rect(topleft=(360, 450))
                screen.blit( intro_score, intro_score_rect )

            #pygame.display.update()
            #clock.tick(50)

        pygame.display.update()  ############# UPDATE #############
        clock.tick(50)