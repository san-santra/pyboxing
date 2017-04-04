# With help from: https://pythonprogramming.net/pygame-python-3-part-1-intro/ 

import pygame

import sys

window_W = 640
window_H = 480

done = False
is_blue = True
white = (255, 255, 255)
black = (0, 0, 0)
title_string = 'Py-Boxing'

def game_intro(screen, clock):
    '''
    Displays the Intro screen
    '''
    intro = True
    fps = 15

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                intro = False

        screen.fill(white)
        display_text(screen, title_string, 70, window_W/2, window_H/4)
        display_text(screen, "Press any key to continue", 15, window_W/2, 3*window_H/4)

        
        pygame.display.update()
        clock.tick(fps)

def in_game(screen, clock):
    '''
    Main Game
    '''

    # parameter init
    fps = 60
    done = False
    time_lim = 20  #seconds
    
    cpu_score = 0
    player_score = 0
    score_size = 30
    window_div = 20
    time_size = score_size
    start_ticks = pygame.time.get_ticks()


    # Position
    timer_pos = 3
    ring_pos = 5
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(white)

        # main rendering
        # scores
        display_text(screen, str(cpu_score), score_size, window_W/window_div, window_H/window_div)
        display_text(screen, str(player_score), score_size, (window_div - 1)*window_W/window_div, window_H/window_div)

        # timer
        elapsed = (pygame.time.get_ticks() - start_ticks)/1000  # time elapsed in seconds
        rem = time_lim - elapsed
        rem_min = str(rem / 60)
        rem_sec = str(rem % 60).zfill(2)
        if rem == 0:
            done = True
        
        display_text(screen, str(rem_min)+":"+str(rem_sec), time_size, window_W/2, timer_pos*window_H/window_div)

        # The Ring
        pygame.draw.rect(screen, black,
                         pygame.Rect(window_W/window_div, ring_pos*window_H/window_div,
                                     (window_div - 2)*window_W/window_div,
                                     (window_div - 1 - ring_pos)*window_H/window_div), 2)
        

        pygame.display.update()
        clock.tick(fps)

    return (cpu_score, player_score)


def game_over(screen, clock, cpu_score, player_score):
    '''
    Displays the game over screen
    '''

    # params
    done = False
    fps = 15

    title_font_size = 60
    font_size = 30

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYUP:
                # Press Enter to restart and anyother key to exit
                if event.key == pygame.K_KP_ENTER:
                    return False

                return True

        display_text(screen, "Game Over", title_font_size, window_W/2, window_H/2)

        pygame.display.update()
        clock.tick(fps)
                

# helper functions
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_text(screen, text, font_size, x, y):
    font = pygame.font.Font(pygame.font.get_default_font(), font_size)
    textSurf, textRect = text_objects(text, font)
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)
                

if __name__=='__main__':
    # game init
    pygame.init()
    screen = pygame.display.set_mode((window_W, window_H))
    pygame.display.set_caption('pyboxing')

    clock = pygame.time.Clock()

    finish = False

    while not finish:
        game_intro(screen, clock)
        (cpu_score, player_score) = in_game(screen, clock)
        finish = game_over(screen, clock, cpu_score, player_score)
