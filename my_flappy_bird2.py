import pygame as pg
import sys, random
from PIL import Image

def draw_floor():
    window.blit(floor_surface, (floor_x_pox, 550))
    window.blit(floor_surface, (floor_x_pox + 336, 550))

def create_pipe():
    randon_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_surface.get_rect(midtop = (700, randon_pipe_pos))
    bottom_pipe = pipe_surface.get_rect(midbottom =(700, randon_pipe_pos -400))
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 700:
            window.blit(pipe_surface, pipe)
        else:
            flip_pipe = pg.transform.flip(pipe_surface, False, True)
            window.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            # print("collide")
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        # print("collide")
        return False

    return True

def rotate_bird(bird):
    new_bird = pg.transform.rotate(bird, bird_movement*3)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center= (45, bird_rect.centery))
    return bird_surface, bird_rect

def score_display():
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(288, 45))
    window.blit(score_surface, score_rect)


pg.init()

#bird movement variables

gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


window = pg.display.set_mode((576,700))
clock = pg.time.Clock()
bg_surface = pg.image.load("assets/background-day.png").convert()
#set default image size
SURFACE_IMAGE_SCALAR = (576, 650)
bg_surface = pg.transform.scale(bg_surface, SURFACE_IMAGE_SCALAR)
game_font = pg.font.Font("04B_19.TTF", 40)


#
floor_surface = pg.image.load("assets/base.png").convert()
# floor_surface = pg.transform.scale2x(floor_surface)
#set default size
FLOOR_DEFAULT_SIZE = (336,150)
floor_surface = pg.transform.scale(floor_surface, FLOOR_DEFAULT_SIZE)
floor_x_pox = 0

bird_downflap = pg.transform.scale2x(pg.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pg.transform.scale2x(pg.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pg.transform.scale2x(pg.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (45,350))
BIRDFLAP = pg.USEREVENT + 1
pg.time.set_timer(BIRDFLAP, 200)

# bird_surface = pg.image.load("assets/bluebird-midflap.png").convert()
# bird_surface = pg.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center = (45, 350))

pipe_surface = pg.image.load("assets/pipe-green.png").convert()
PIPE_IMAGE_SCALAR = (52, 400)
pipe_surface = pg.transform.scale(pipe_surface, PIPE_IMAGE_SCALAR)
pipe_list = []
pipe_height = [400, 600, 800]
SPANPIPES = pg.USEREVENT
pg.time.set_timer(SPANPIPES, 1200)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and game_active:
                #print("flap")
                bird_movement = 0
                bird_movement -= 12

            if event.key == pg.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (45, 350)
                bird_movement = 0
                score = 0


        if event.type == SPANPIPES:
            # print("span")
            pipe_list.extend(create_pipe())
            # print(pipe_list)

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()


    window.blit(bg_surface, (0,0))
    #floor surface
    floor_x_pox -= 1
    draw_floor()
    if floor_x_pox <= -50:
        floor_x_pox = 0
    if game_active:
        #bird movement
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        window.blit(rotated_bird, bird_rect)

        #pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collision(pipe_list)
        score += 0.01
        score_display()



    clock.tick(120)
    pg.display.update()
