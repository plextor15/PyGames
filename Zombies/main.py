import pygame
from sys import exit
import getpass
from random import randint


def display_score():
    current_time = int( pygame.time.get_ticks() / 1000 ) - start_time

    score_text = game_font.render(f"My scores: {current_time}", False, 'Black')
    score_text_rect = score_text.get_rect(topleft=(380, 100))
    pygame.draw.rect(screen, '#c0e8ec', score_text_rect, 0, 10)
    screen.blit(score_text, score_text_rect)

    return current_time

def zombie_move(zombie_list):
    if zombie_list:
        for rect in zombie_list:
            rect.x -= 5

        new_zombie_list = [rect for rect in zombie_list if rect.x > -100] #aktualny wchodzi jesli
        #for rect in zombie_list:
        #    if rect.x > -100:
        #        new_zombie_list.append(rect)

        return new_zombie_list
    else:
        return []    # jak nic nie ma, nic nie daje

def collision(player, zombie_list):
    if zombie_list:
        for rect in zombie_list:
            if player.colliderect(rect):
                return True
    else:
        return False

def player_animation():
    global player_surf, player_index    #gdziekolwiek one sa

    if player_rect.bottom < 430:
        player_surf = player_jump
    else:
        player_index += 0.05     #czas trwania animacji
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

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
    zombie_surf = pygame.image.load('graphic/characters/zombie/zombie_walk1.png').convert_alpha()
    # Dodanie obszaru zombie
    zombie_rect = zombie_surf.get_rect(topleft=(700, 430))
    zombie_rect_list = []

    # Dodanie gracza do gry
    player_walk1 = pygame.image.load('graphic/characters/player/adventurer_walk1.png').convert_alpha()
    player_walk2 = pygame.image.load('graphic/characters/player/adventurer_walk2.png').convert_alpha()
    player_jump = pygame.image.load('graphic/characters/player/adventurer_jump.png').convert_alpha()
    player_walk = [player_walk1, player_walk2]
    player_index = 0
    player_surf = player_walk[player_index]
    # Dodanie obszaru gracza
    player_rect = player_surf.get_rect(topleft=(100, 430))

    player_gravity = 25


    game_is_active = False
    game_over = False
    start_time = 0
    score = 0

    own_game_event = pygame.USEREVENT
    pygame.time.set_timer(own_game_event,1500)

    background_music = pygame.mixer.music.load('music/Sneaky_Snitch.mp3')
    pygame.mixer.music.play(-1)


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
                     
                if event.type == own_game_event:
                    #print("OWN_EVENT")
                    zombie_rect_list.append(zombie_surf.get_rect(topleft=(randint(900,1100), 430)))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    game_is_active = True

                    # pozycjonowanie
                    zombie_rect.topleft = (700, 430)
                    player_rect.topleft = (100, 430)
                    player_gravity = 25



        if game_is_active:
            # Ruch Zombie
            #zombie_rect.x -= 5
            #if zombie_rect.x <= -100:
            #    zombie_rect.x = 1100

            # Dodanie backgroundu do okna gry
            screen.blit(background, (0, 0))
            # Dodanie elementow podlogi do okna gry
            screen.blit(ground, (0, 540))

            pygame.draw.rect(screen, '#c0e8ec', text_rect, 0, 10)
            # Dodanie tekstu do okna gry
            screen.blit(text, text_rect)

            score = display_score()
            

            zombie_rect_list = zombie_move( zombie_rect_list )
            for rect in zombie_rect_list:
                # Dodanie zombie do okna gry
                screen.blit(zombie_surf, rect)

            # Dodanie gracza do ekranu gry
            player_animation()
            screen.blit(player_surf, player_rect)



            #pygame.display.update() ############# UPDATE #############

            

            if player_rect.y < 430:
                player_gravity += 1

            player_rect.y += player_gravity
        
            #DEBUG ONLY!!
            #print(player_gravity)

            if player_rect.y >= 430: player_rect.y = 430

            if collision( player_rect, zombie_rect_list ):
                game_is_active = False
                game_over = True
                start_time = int( pygame.time.get_ticks() / 1000 ) # tu moze byc cheat z main menu

            #game_is_active = collision( player_rect, zombie_rect_list )
            
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
                zombie_rect_list = []

            #pygame.display.update()
            #clock.tick(50)

        pygame.display.update()  ############# UPDATE #############
        clock.tick(50)